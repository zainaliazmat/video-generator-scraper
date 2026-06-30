import time

from fastapi.testclient import TestClient

import server.app as app_mod

client = TestClient(app_mod.app)


def _seed_done_job(rows, **params):
    job = app_mod.MANAGER.create({"fast": True, **params})
    job.rows = rows
    job.status = "done"
    return job


def test_results_returns_serialized_rows():
    job = _seed_done_job([{"video_id": "a", "views": "1000", "subscribers": "100",
                           "channel_verified": "Yes", "title": "T",
                           "keyword": "best ai tools"}])
    r = client.get(f"/api/jobs/{job.id}/results")
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 1
    assert body["rows"][0]["breakout"] == 10.0
    assert body["rows"][0]["verified"] is True
    assert "date" in body            # R8: real date wired through
    assert "keywords" in body        # R8: distinct keywords for the dropdown


def test_results_unknown_job_404():
    assert client.get("/api/jobs/nope/results").status_code == 404


def test_status_poll_returns_terminal():
    job = _seed_done_job([{"video_id": "a"}])
    r = client.get(f"/api/jobs/{job.id}")
    assert r.status_code == 200
    assert r.json()["status"] == "done"


def test_events_emits_terminal_for_finished_job():
    # R2: a job that finished before the browser connected must still get a
    # terminal frame (not hang on the spinner forever).
    job = _seed_done_job([{"video_id": "a"}])
    with client.stream("GET", f"/api/jobs/{job.id}/events") as r:
        assert r.status_code == 200
        body = "".join(chunk for chunk in r.iter_text())
    assert '"type": "done"' in body or '"type":"done"' in body


def test_predict_start_runs_generate_prediction(monkeypatch):
    job = _seed_done_job([{"video_id": "a", "views": "1000", "subscribers": "100"}])

    def fake_predict(rows, on_text=None):
        if on_text:
            on_text("thinking...")
        return {"ok": True, "source": "ai", "topic": "MOCK", "ideas": []}

    monkeypatch.setattr(app_mod.ideas, "generate_prediction", fake_predict)
    r = client.post(f"/api/jobs/{job.id}/predict-start")
    assert r.status_code == 200
    # wait for the background prediction thread to finish
    for _ in range(50):
        if job.prediction is not None:
            break
        time.sleep(0.05)
    assert job.prediction["topic"] == "MOCK"
    assert "thinking..." in "".join(job.predict_log)


def test_download_writes_per_job_path(tmp_path, monkeypatch):
    job = _seed_done_job([{"video_id": "a", "title": "T", "keyword": "k"}])
    r = client.get(f"/api/jobs/{job.id}/download")
    assert r.status_code == 200
    assert "tab-separated" in r.headers["content-type"]
    # Per-job file (R6): must NOT clobber the CLI's youtube_results.tsv
    assert job.id in r.headers.get("content-disposition", "")


def test_run_rejects_second_while_running(monkeypatch):
    # Force the manager to look busy, then assert /api/run returns 409.
    monkeypatch.setattr(app_mod.MANAGER, "run_in_thread",
                        lambda *a, **k: (_ for _ in ()).throw(app_mod.JobBusyError("busy")))
    r = client.post("/api/run", json={"inputs": "ai tools", "fast": True})
    assert r.status_code == 409


def test_cancel_marks_job(monkeypatch):
    job = app_mod.MANAGER.create({"fast": True})
    job.status = "running"
    r = client.post(f"/api/jobs/{job.id}/cancel")
    assert r.status_code == 200
    assert job.cancelled is True
