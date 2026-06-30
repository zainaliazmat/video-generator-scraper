"""Voyara Signal — local FastAPI backend.

Wraps the existing scraper + AI as HTTP/SSE endpoints and serves the built
Svelte UI. Single-user, binds 127.0.0.1, runs ONE scrape at a time.
"""
import asyncio
import json
import queue
import threading
from datetime import date
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import history
import ideas
import youtube_scraper as ys
from server import inputs as inputs_mod
from server.jobs import JobBusyError, JobManager
from server.serialize import row_to_api

app = FastAPI(title="Voyara Signal")
MANAGER = JobManager()

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "web" / "dist"
WEB_RUNS = ROOT / "web_runs"


class RunBody(BaseModel):
    inputs: str = ""
    per_link: str = "60 videos"
    date_filter: str = "Any time"
    fast: bool = True
    cookies: str | None = None


class PredictBody(BaseModel):
    job_id: str


# --------------------------------------------------------------------------- #
# Run + progress
# --------------------------------------------------------------------------- #
@app.post("/api/run")
def run(body: RunBody):
    urls = inputs_mod.parse_inputs(body.inputs, body.date_filter)
    if not urls:
        raise HTTPException(400, "Add at least one keyword or URL.")
    limit = inputs_mod.per_link_to_int(body.per_link)
    cookies = body.cookies or None
    job = MANAGER.create({"fast": body.fast, "urls": urls, "limit": limit,
                          "date": date.today().isoformat()})

    def scrape_fn(progress, should_cancel):
        rows = ys.run_scrape(urls, limit=limit, fast=body.fast,
                             channel_info=not body.fast, cookies=cookies,
                             progress=progress, should_cancel=should_cancel)
        try:  # web snapshots use a distinct basename so the CLI's are untouched
            history.save_snapshot(rows, ys.COLUMNS, "web_youtube_results")
        except Exception as exc:
            progress(f"(snapshot skipped: {exc})")
        return rows

    try:
        MANAGER.run_in_thread(job, scrape_fn)
    except JobBusyError as exc:
        raise HTTPException(409, str(exc))
    return {"job_id": job.id}


def _status_payload(job):
    return {"status": job.status, "progress": job.progress,
            "count": len(job.rows), "error": job.error}


@app.get("/api/jobs/{job_id}")
def job_status(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")
    return _status_payload(job)


@app.get("/api/jobs/{job_id}/events")
async def events(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")

    async def gen():
        sent_terminal = False
        idle = 0
        while True:
            try:
                evt = job.events.get_nowait()
            except Exception:
                evt = None
            if evt is not None:
                yield f"data: {json.dumps(evt)}\n\n"
                if evt["type"] in ("done", "error", "cancelled"):
                    sent_terminal = True
                    break
                continue
            # No queued event. If the job is already terminal, emit a synthetic
            # terminal frame so a late/reconnecting client never hangs (R2).
            if job.status in ("done", "error", "cancelled"):
                frame = {"type": job.status, "count": len(job.rows)}
                if job.error:
                    frame["message"] = job.error
                yield f"data: {json.dumps(frame)}\n\n"
                sent_terminal = True
                break
            idle += 1
            if idle % 60 == 0:        # ~15s heartbeat keeps proxies from killing it
                yield ": ping\n\n"
            await asyncio.sleep(0.25)
        if not sent_terminal:
            yield "data: {\"type\": \"error\", \"message\": \"stream ended\"}\n\n"

    return StreamingResponse(gen(), media_type="text/event-stream")


@app.post("/api/jobs/{job_id}/cancel")
def cancel(job_id: str):
    job = MANAGER.cancel(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")
    return {"cancelled": True}


# --------------------------------------------------------------------------- #
# Results + download + predict
# --------------------------------------------------------------------------- #
@app.get("/api/jobs/{job_id}/results")
def results(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")
    if job.status == "error":
        raise HTTPException(409, job.error or "Job failed")
    if job.status not in ("done", "cancelled"):
        raise HTTPException(409, "Job not finished")
    rows = [row_to_api(r) for r in job.rows]
    keywords = sorted({r["keyword"] for r in rows if r["keyword"]})
    return {"count": len(rows), "fast": job.params.get("fast", False),
            "date": job.params.get("date", ""), "keywords": keywords,
            "cancelled": job.status == "cancelled", "rows": rows}


@app.get("/api/jobs/{job_id}/download")
def download(job_id: str):
    job = MANAGER.get(job_id)
    if not job or job.status not in ("done", "cancelled"):
        raise HTTPException(404, "No finished job")
    WEB_RUNS.mkdir(exist_ok=True)
    out = WEB_RUNS / f"{job.id}.tsv"     # per-job path; never the CLI's file (R6)
    ys.write_tsv(job.rows, out)
    return FileResponse(out, filename=f"voyara_{job.id}.tsv",
                        media_type="text/tab-separated-values")


@app.post("/api/predict")
def predict(body: PredictBody):
    job = MANAGER.get(body.job_id)
    if not job or job.status not in ("done", "cancelled"):
        raise HTTPException(404, "No finished job to analyse")
    return ideas.generate_prediction(job.rows)


@app.post("/api/jobs/{job_id}/predict-start")
def predict_start(job_id: str):
    """Kick off a streaming prediction in the background (idempotent)."""
    job = MANAGER.get(job_id)
    if not job or job.status not in ("done", "cancelled"):
        raise HTTPException(404, "No finished job to analyse")
    if job.predicting:
        return {"ok": True, "already": True}
    job.predicting = True
    job.prediction = None
    job.predict_events = queue.Queue()
    job.predict_log = []
    model = getattr(ideas, "MODEL", "claude")

    def emit(line):
        job.predict_log.append(line)
        job.predict_events.put({"type": "text", "chunk": line})

    def work():
        try:
            emit(f"$ signal predict --videos {len(job.rows)}\n")
            emit("building digest from your scraped data...\n")
            emit(f"connecting to Claude ({model})...\n\n")
            result = ideas.generate_prediction(job.rows, on_text=emit)
            job.prediction = result
            if result.get("ok"):
                emit("\n\n[done] prediction ready.\n")
            else:
                emit(f"\n\n[error] {result.get('reason')}: {result.get('detail','')}\n")
            job.predict_events.put({"type": "result", "prediction": result})
        except Exception as exc:  # safety net
            job.prediction = {"ok": False, "reason": "error", "detail": str(exc)}
            job.predict_events.put({"type": "result", "prediction": job.prediction})
        finally:
            job.predicting = False

    threading.Thread(target=work, daemon=True).start()
    return {"ok": True}


@app.get("/api/jobs/{job_id}/predict-events")
async def predict_events(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")

    async def gen():
        while True:
            try:
                evt = job.predict_events.get_nowait()
            except Exception:
                evt = None
            if evt is not None:
                yield f"data: {json.dumps(evt)}\n\n"
                if evt["type"] == "result":
                    break
                continue
            # If a prediction already finished before this client connected,
            # replay the log + result so it never hangs.
            if not job.predicting and job.prediction is not None:
                for line in job.predict_log:
                    yield f"data: {json.dumps({'type': 'text', 'chunk': line})}\n\n"
                yield f"data: {json.dumps({'type': 'result', 'prediction': job.prediction})}\n\n"
                break
            await asyncio.sleep(0.1)

    return StreamingResponse(gen(), media_type="text/event-stream")


# --------------------------------------------------------------------------- #
# Static UI (served only when built)
# --------------------------------------------------------------------------- #
if DIST.exists():
    app.mount("/", StaticFiles(directory=str(DIST), html=True), name="static")
else:
    @app.get("/")
    def not_built():
        return PlainTextResponse(
            "Web UI not built yet. Run `./run.sh web` (needs Node.js installed) "
            "to build and serve it.", status_code=200)
