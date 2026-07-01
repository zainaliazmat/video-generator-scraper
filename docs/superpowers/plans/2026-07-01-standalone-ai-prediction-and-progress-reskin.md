# Standalone AI Prediction Tool + Scrape-Progress Re-skin — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn AI prediction into a standalone tool that predicts from any TSV (drag-drop upload or a picked history snapshot), and re-skin the scrape "in progress" screen to match the `Run progress (1).html` template.

**Architecture:** Backend adds two endpoints (`GET /api/history`, `POST /api/predict`) that reuse the existing `Job` + prediction-streaming machinery — a TSV is parsed into scraper-style row dicts, dropped onto a synthetic `Job(status="done")`, and the existing `predict-start`/`predict-events` stream unchanged. Frontend adds a `Predict.svelte` screen (history-first, drag-drop secondary), a Hub card, a deep-link button on Results, and a re-skinned `RunProgress.svelte` driven by a pure, unit-tested progress parser.

**Tech Stack:** Python 3.12, FastAPI, pytest + httpx `TestClient`; Svelte 5 + Vite 5, vitest (added here for the progress parser).

## Global Constraints

- Server binds `127.0.0.1`, single user, runs ONE scrape at a time. Predictions are NOT gated by the scrape lock (only `run_in_thread` sets `_running`).
- History files live in `history/` and are written `utf-8-sig` (BOM). Video-table snapshots match `*_YYYY-MM-DD.tsv`; `diff_*.tsv` are diff reports (different columns) and MUST be excluded.
- Scraper columns (order): `keyword, title, channel, channel_url, channel_id, subscribers, channel_verified, views, likes, comments, duration, duration_sec, upload_date, tags, categories, language, channel_description, channel_tags, video_url, video_id, thumbnail`.
- Breakout = `views / subscribers` (needs `subscribers` present AND > 0), per `serialize.row_to_api`. The predict guard must mirror this, NOT mere column presence.
- Upload cap: 10 MB. Reason codes surfaced to the client via HTTP `detail`: `empty`, `bad_columns`, `no_breakout_data` (all 422), `too_large` (413).
- Run pytest from `backend/` (its `conftest.py` puts the dir on `sys.path`). Tests import top-level modules (`server.app`, `analyze`, …) directly.
- No em dashes in user-facing copy is NOT a constraint here — the existing UI uses them; match existing style.

---

## File Structure

**Backend**
- Create `backend/server/tsv_sources.py` — list history snapshots; resolve a history filename safely; parse a TSV (bytes/text, BOM-tolerant) into rows; classify whether rows can drive a prediction. Pure, no HTTP.
- Modify `backend/server/app.py` — add `GET /api/history` and `POST /api/predict`.
- Modify `backend/server/jobs.py` — eviction never drops a job mid-prediction.
- Modify `backend/requirements.txt` — declare `python-multipart`.
- Create `backend/tests/test_tsv_sources.py`, `backend/tests/test_predict_endpoint.py`.
- Modify `backend/tests/test_jobs.py` — eviction guard test.

**Frontend**
- Modify `frontend/src/lib/api.js` — `getHistory()`, `startPredict(source)`.
- Modify `frontend/src/lib/store.js` — predict-tool state; `ai` view → `predict`; `runStartMs`.
- Create `frontend/src/lib/progress.js` — pure `computeProgress(lines)` + `estimateTimeLeft(...)`.
- Create `frontend/src/lib/progress.test.js` — vitest unit tests.
- Create `frontend/src/screens/Predict.svelte` — the standalone tool (history-first + drag-drop + chip + states + reused result card).
- Create `frontend/src/screens/RunProgress.svelte` — re-skinned progress screen.
- Modify `frontend/src/screens/Hub.svelte` — add the AI Prediction live card.
- Modify `frontend/src/screens/Results.svelte` — render `RunProgress` while running; add "Predict next video" deep-link button on results.
- Modify `frontend/src/screens/ToolHeader.svelte` — remove the AI-prediction tab.
- Modify `frontend/src/App.svelte` — route `predict` view; drop `ai`.
- Delete `frontend/src/screens/AiPrediction.svelte` (markup moves into `Predict.svelte`).
- Modify `frontend/package.json` — add `vitest` + `test` script.

---

## Task 1: Backend deps + eviction guard (foundational)

**Files:**
- Modify: `backend/requirements.txt`
- Modify: `backend/server/jobs.py:51-57` (`JobManager.create`), `:45` (`max_jobs` default)
- Test: `backend/tests/test_jobs.py`

**Interfaces:**
- Produces: `JobManager.create(params)` still returns a `Job`; now never evicts a job whose `predicting` is `True`.

- [ ] **Step 1: Add the failing eviction-guard test**

Append to `backend/tests/test_jobs.py`:

```python
def test_create_never_evicts_a_predicting_job():
    from server.jobs import JobManager
    m = JobManager(max_jobs=2)
    keep = m.create({})
    keep.predicting = True                     # mid-stream prediction
    # Create enough jobs to force eviction well past the cap.
    for _ in range(5):
        m.create({})
    assert m.get(keep.id) is keep              # survived eviction
```

- [ ] **Step 2: Run it, verify it fails**

Run: `cd backend && pytest tests/test_jobs.py::test_create_never_evicts_a_predicting_job -v`
Expected: FAIL (`keep` gets evicted → `m.get(keep.id)` is `None`).

- [ ] **Step 3: Implement the eviction guard**

In `backend/server/jobs.py`, change the `max_jobs` default and the eviction loop.

Replace `def __init__(self, max_jobs=10):` with:

```python
    def __init__(self, max_jobs=50):
```

Replace the `create` method body's eviction loop:

```python
    def create(self, params):
        job = Job(uuid.uuid4().hex[:12], params)
        with self._lock:
            self._jobs[job.id] = job
            # Evict oldest to stay under the cap, but NEVER a job whose
            # prediction is still streaming (its predict-events SSE would 404
            # and the client would retry forever). If every over-cap job is
            # predicting, keep them all.
            while len(self._jobs) > self._max_jobs:
                victim = next((jid for jid, j in self._jobs.items()
                               if not j.predicting), None)
                if victim is None:
                    break
                del self._jobs[victim]
        return job
```

- [ ] **Step 4: Run tests, verify pass**

Run: `cd backend && pytest tests/test_jobs.py -v`
Expected: PASS (all, including the new test).

- [ ] **Step 5: Declare python-multipart**

In `backend/requirements.txt`, under the `# Web app` block (after `sse-starlette>=2.0`), add:

```
python-multipart>=0.0.9   # required by FastAPI for multipart/form-data (file upload)
```

- [ ] **Step 6: Commit**

```bash
git add backend/requirements.txt backend/server/jobs.py backend/tests/test_jobs.py
git commit -m "feat(jobs): never evict a predicting job; declare python-multipart"
```

---

## Task 2: Backend `tsv_sources` module

**Files:**
- Create: `backend/server/tsv_sources.py`
- Test: `backend/tests/test_tsv_sources.py`

**Interfaces:**
- Produces:
  - `HISTORY_DIR: Path` (absolute, anchored to project root).
  - `MAX_UPLOAD_BYTES: int` (10 MB).
  - `list_snapshots() -> list[dict]` — each `{"file": str, "date": str, "count": int, "keywords": list[str]}`, newest first, excludes `diff_*`.
  - `resolve_history_path(name: str) -> Path | None` — safe map into `HISTORY_DIR`; `None` on traversal / non-`.tsv` / missing.
  - `parse_tsv(data: bytes | str) -> list[dict]` — BOM-tolerant TSV rows.
  - `source_error(rows: list[dict]) -> str | None` — reason code or `None` if usable.

- [ ] **Step 1: Write the failing tests**

Create `backend/tests/test_tsv_sources.py`:

```python
import io

import pytest

from server import tsv_sources as ts


def _write(dirpath, name, rows, header="keyword\tsubscribers\tviews\n"):
    p = dirpath / name
    body = header + "".join(rows)
    p.write_text(body, encoding="utf-8-sig")   # BOM, like history.save_snapshot
    return p


def test_parse_tsv_is_bom_tolerant():
    data = "﻿keyword\tsubscribers\tviews\nai\t100\t1000\n".encode("utf-8")
    rows = ts.parse_tsv(data)
    assert rows[0]["keyword"] == "ai"          # not "﻿keyword"
    assert rows[0]["subscribers"] == "100"


def test_source_error_codes():
    assert ts.source_error([]) == "empty"
    assert ts.source_error([{"title": "t"}]) == "bad_columns"          # no subscribers col
    assert ts.source_error([{"subscribers": ""}]) == "no_breakout_data"
    assert ts.source_error([{"subscribers": "0"}]) == "no_breakout_data"
    assert ts.source_error([{"subscribers": "100"}]) is None


def test_list_snapshots_excludes_diffs_and_sorts_newest_first(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "HISTORY_DIR", tmp_path)
    _write(tmp_path, "web_youtube_results_2026-06-01.tsv", ["ai\t10\t100\n"])
    _write(tmp_path, "youtube_results_2026-07-01.tsv", ["ml\t20\t200\n", "ml\t5\t50\n"])
    _write(tmp_path, "diff_a__b.tsv", ["x\ty\tz\n"])   # must be skipped
    snaps = ts.list_snapshots()
    names = [s["file"] for s in snaps]
    assert "diff_a__b.tsv" not in names
    assert names[0] == "youtube_results_2026-07-01.tsv"    # newest by trailing date
    assert snaps[0]["count"] == 2
    assert snaps[0]["keywords"] == ["ml"]


def test_resolve_history_path_blocks_traversal(tmp_path, monkeypatch):
    monkeypatch.setattr(ts, "HISTORY_DIR", tmp_path)
    real = _write(tmp_path, "web_youtube_results_2026-07-01.tsv", ["ai\t10\t100\n"])
    assert ts.resolve_history_path("web_youtube_results_2026-07-01.tsv") == real.resolve()
    assert ts.resolve_history_path("../../etc/passwd") is None
    assert ts.resolve_history_path("nope.tsv") is None          # missing
    assert ts.resolve_history_path("web_youtube_results_2026-07-01.csv") is None  # not .tsv
```

- [ ] **Step 2: Run, verify fail**

Run: `cd backend && pytest tests/test_tsv_sources.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server.tsv_sources'`.

- [ ] **Step 3: Implement the module**

Create `backend/server/tsv_sources.py`:

```python
"""TSV sources for the standalone AI-prediction tool.

Lists history snapshots and parses a TSV (uploaded or picked from history) into
scraper-style row dicts, with a breakout-data guard so we never ask Claude to
predict from data it cannot use. Pure — no HTTP, no Job knowledge.
"""
import csv
import io
import re
from pathlib import Path

import analyze

# Anchor history/ to the project root, NOT the process cwd. history.HISTORY_DIR
# is the relative string "history"; resolving it here makes the endpoints
# independent of where uvicorn was launched from.
BACKEND = Path(__file__).resolve().parent.parent
PROJECT = BACKEND.parent
HISTORY_DIR = PROJECT / "history"

MAX_UPLOAD_BYTES = 10 * 1024 * 1024   # 10 MB

_DATE_RE = re.compile(r"_(\d{4}-\d{2}-\d{2})\.tsv$")


def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _date_key(name):
    m = _DATE_RE.search(name)
    return m.group(1) if m else ""


def list_snapshots():
    """Return [{file, date, count, keywords}] for every video-table TSV in
    history/, newest first. Skips diff_* reports and unparseable files."""
    if not HISTORY_DIR.exists():
        return []
    out = []
    for p in sorted(HISTORY_DIR.glob("*.tsv")):
        if p.name.startswith("diff_"):
            continue
        try:
            rows = analyze.load_rows(str(p))
        except Exception:
            continue
        keywords = sorted({r.get("keyword", "") for r in rows if r.get("keyword")})
        out.append({"file": p.name, "date": _date_key(p.name),
                    "count": len(rows), "keywords": keywords})
    out.sort(key=lambda d: d["date"], reverse=True)
    return out


def resolve_history_path(name):
    """Map a client-supplied history filename to a real file inside HISTORY_DIR.
    Returns a resolved Path, or None on traversal / non-.tsv / missing."""
    if not name or not name.endswith(".tsv"):
        return None
    candidate = (HISTORY_DIR / Path(name).name).resolve()
    try:
        candidate.relative_to(HISTORY_DIR.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def parse_tsv(data):
    """Parse TSV bytes or text (BOM-tolerant) into a list of row dicts."""
    if isinstance(data, bytes):
        text = data.decode("utf-8-sig", errors="replace")
    else:
        text = data.lstrip("﻿")
    reader = csv.DictReader(io.StringIO(text), delimiter="\t")
    return list(reader)


def source_error(rows):
    """Return a reason code if these rows cannot drive a prediction, else None.

    Mirrors serialize.row_to_api breakout math (views/subs, subs>0): without a
    usable subscriber count there is nothing to analyse. A comma-separated
    (CSV-as-TSV) file yields one giant column and trips 'bad_columns'.
    """
    if not rows:
        return "empty"
    if "subscribers" not in rows[0].keys():
        return "bad_columns"
    if not any(_int(r.get("subscribers")) for r in rows):
        return "no_breakout_data"
    return None
```

- [ ] **Step 4: Run, verify pass**

Run: `cd backend && pytest tests/test_tsv_sources.py -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add backend/server/tsv_sources.py backend/tests/test_tsv_sources.py
git commit -m "feat(predict): tsv_sources — list history, safe-resolve, parse, breakout guard"
```

---

## Task 3: Backend `GET /api/history` + `POST /api/predict`

**Files:**
- Modify: `backend/server/app.py` (imports near top; new routes after the download route ~`:161`)
- Test: `backend/tests/test_predict_endpoint.py`

**Interfaces:**
- Consumes: `tsv_sources.*` (Task 2); `MANAGER.create` (Task 1); existing `predict-start`/`predict-events`.
- Produces:
  - `GET /api/history` → `{"snapshots": [ {file,date,count,keywords}, ... ]}`.
  - `POST /api/predict` (multipart: optional `file`, optional `history` form field) → `{"job_id": str}`, or HTTP error whose `detail` is a reason code.

- [ ] **Step 1: Write the failing endpoint tests**

Create `backend/tests/test_predict_endpoint.py`:

```python
import io

from fastapi.testclient import TestClient

import server.app as app_mod
from server import tsv_sources

client = TestClient(app_mod.app)

_FULL = ("keyword\tsubscribers\tviews\tvideo_id\ttitle\n"
         "ai tools\t100\t1000\tv1\tHello\n")
_FAST = "keyword\tsubscribers\tviews\tvideo_id\nai\t\t1000\tv1\n"   # subs blank


def test_history_lists_snapshots(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    (tmp_path / "web_youtube_results_2026-07-01.tsv").write_text(_FULL, encoding="utf-8-sig")
    r = client.get("/api/history")
    assert r.status_code == 200
    snaps = r.json()["snapshots"]
    assert snaps[0]["file"] == "web_youtube_results_2026-07-01.tsv"
    assert snaps[0]["count"] == 1
    assert snaps[0]["keywords"] == ["ai tools"]


def test_predict_upload_creates_done_job():
    files = {"file": ("snap.tsv", _FULL, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 200
    jid = r.json()["job_id"]
    job = app_mod.MANAGER.get(jid)
    assert job.status == "done"
    assert job.rows[0]["title"] == "Hello"
    assert job.params["predict"] is True


def test_predict_from_history(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    (tmp_path / "web_youtube_results_2026-07-01.tsv").write_text(_FULL, encoding="utf-8-sig")
    r = client.post("/api/predict", data={"history": "web_youtube_results_2026-07-01.tsv"})
    assert r.status_code == 200
    assert app_mod.MANAGER.get(r.json()["job_id"]).rows[0]["title"] == "Hello"


def test_predict_history_traversal_404(tmp_path, monkeypatch):
    monkeypatch.setattr(tsv_sources, "HISTORY_DIR", tmp_path)
    r = client.post("/api/predict", data={"history": "../../etc/passwd"})
    assert r.status_code == 404


def test_predict_fast_mode_tsv_rejected():
    files = {"file": ("fast.tsv", _FAST, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 422
    assert r.json()["detail"] == "no_breakout_data"


def test_predict_empty_file_rejected():
    files = {"file": ("empty.tsv", "", "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 422
    assert r.json()["detail"] == "empty"


def test_predict_too_large_rejected():
    big = "keyword\tsubscribers\n" + ("ai\t100\n" * 1_600_000)  # > 10 MB
    files = {"file": ("big.tsv", big, "text/tab-separated-values")}
    r = client.post("/api/predict", files=files)
    assert r.status_code == 413
    assert r.json()["detail"] == "too_large"


def test_predict_requires_a_source():
    assert client.post("/api/predict").status_code == 400
```

- [ ] **Step 2: Run, verify fail**

Run: `cd backend && pytest tests/test_predict_endpoint.py -v`
Expected: FAIL (routes 404 — not defined yet).

- [ ] **Step 3: Add imports**

In `backend/server/app.py`, extend the FastAPI import and add the module import.

Change:

```python
from fastapi import FastAPI, HTTPException
```

to:

```python
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
```

And add alongside the other `from server import ...` lines (near `:21`):

```python
from server import tsv_sources
```

- [ ] **Step 4: Add the routes**

In `backend/server/app.py`, immediately AFTER the `download` route (ends ~`:161`) and BEFORE the `predict_start` route, insert:

```python
# --------------------------------------------------------------------------- #
# Standalone prediction: history listing + TSV -> synthetic job
# --------------------------------------------------------------------------- #
_REASON_STATUS = {"empty": 422, "bad_columns": 422,
                  "no_breakout_data": 422, "too_large": 413}


@app.get("/api/history")
def history_list():
    """List saved TSV snapshots the predict tool can analyse."""
    return {"snapshots": tsv_sources.list_snapshots()}


@app.post("/api/predict")
async def predict_source(file: UploadFile | None = File(default=None),
                         history: str | None = Form(default=None)):
    """Build a synthetic done-job from an uploaded TSV or a history snapshot,
    so the existing predict-start/predict-events endpoints can stream on it."""
    snapshot_date = ""
    if file is not None:
        data = await file.read()
        if len(data) > tsv_sources.MAX_UPLOAD_BYTES:
            raise HTTPException(413, "too_large")
        rows = tsv_sources.parse_tsv(data)
    elif history:
        path = tsv_sources.resolve_history_path(history)
        if path is None:
            raise HTTPException(404, "Unknown history file")
        rows = tsv_sources.parse_tsv(path.read_bytes())
        snapshot_date = tsv_sources._date_key(path.name)
    else:
        raise HTTPException(400, "Provide a file upload or a history filename.")

    reason = tsv_sources.source_error(rows)
    if reason:
        raise HTTPException(_REASON_STATUS.get(reason, 422), reason)

    # Synthetic job: not gated by the scrape lock; params carry enough for the
    # results screen if it is ever queried. Never remembered as the last job.
    job = MANAGER.create({"fast": False, "date": snapshot_date, "predict": True})
    job.rows = rows
    job.status = "done"
    return {"job_id": job.id}
```

- [ ] **Step 5: Run, verify pass**

Run: `cd backend && pytest tests/test_predict_endpoint.py -v`
Expected: PASS (8 tests).

- [ ] **Step 6: Full backend suite green**

Run: `cd backend && pytest -q`
Expected: PASS (all files).

- [ ] **Step 7: Commit**

```bash
git add backend/server/app.py backend/tests/test_predict_endpoint.py
git commit -m "feat(api): GET /api/history + POST /api/predict (upload or history -> synthetic job)"
```

---

## Task 4: Frontend API + store wiring

**Files:**
- Modify: `frontend/src/lib/api.js` (append helpers)
- Modify: `frontend/src/lib/store.js:8-37` (state), `:9` (view enum comment), add `runStartMs`

**Interfaces:**
- Produces:
  - `getHistory() -> Promise<{snapshots}>`.
  - `startPredict(source) -> Promise<{job_id}>` where `source` is `{kind:'file', file: File}` or `{kind:'history', file: string}`.
  - store fields: `history`, `historyState`, `source`, `runStartMs`; view enum value `predict` (replaces `ai`).
- Consumes: existing `watchPredict(jobId, onText, onResult)` unchanged.

- [ ] **Step 1: Add API helpers**

Append to `frontend/src/lib/api.js`:

```javascript
export async function getHistory() {
  return jsonOrThrow(await fetch('/api/history'))
}

// source = {kind:'file', file:File} | {kind:'history', file:string(filename)}
export async function startPredict(source) {
  const body = new FormData()
  if (source.kind === 'file') body.append('file', source.file)
  else body.append('history', source.file)
  return jsonOrThrow(await fetch('/api/predict', { method: 'POST', body }))
}
```

- [ ] **Step 2: Update the store's view enum + add predict-tool state**

In `frontend/src/lib/store.js`, change the view comment line:

```javascript
  view: 'hub',                 // hub | input | results | predict
```

Then, inside the `writable({...})` object, in the `// ai` block near the end, replace:

```javascript
  // ai
  aiState: 'idle',             // idle | loading | done | error
  ai: null,
  predictLog: '',              // streamed Claude text (live AI session)
```

with:

```javascript
  // predict tool (standalone)
  history: [],                 // [{file,date,count,keywords}]
  historyState: 'idle',        // idle | loading | error
  source: null,                // {kind:'file',file:File,name} | {kind:'history',file,label}
  aiState: 'idle',             // idle | loading | done | error
  ai: null,
  predictLog: '',              // streamed Claude text (live AI session)
```

And in the `// run` block, add `runStartMs` after `progress: []`:

```javascript
  progress: [],
  runStartMs: 0,               // Date.now() when the scrape started (for time-left)
```

- [ ] **Step 3: Verify the build still compiles**

Run: `cd frontend && npm run build`
Expected: build succeeds (no references broken yet — `App.svelte` still imports `AiPrediction`; that is fixed in Task 5, so this build is just a syntax check of api.js/store.js).
Note: if the build fails ONLY because `App.svelte` references the `ai` view, that is expected and resolved in Task 5. It should still compile here because `ai` is only compared as a string, not the enum.

- [ ] **Step 4: Commit**

```bash
git add frontend/src/lib/api.js frontend/src/lib/store.js
git commit -m "feat(predict-ui): api getHistory/startPredict; store predict state + runStartMs"
```

---

## Task 5: Predict screen, Hub card, routing, tab removal, deep-link

**Files:**
- Create: `frontend/src/screens/Predict.svelte`
- Modify: `frontend/src/screens/Hub.svelte` (second live card)
- Modify: `frontend/src/App.svelte` (route `predict`; drop `AiPrediction`)
- Modify: `frontend/src/screens/ToolHeader.svelte` (remove AI tab)
- Modify: `frontend/src/screens/Results.svelte` (add "Predict next video" button)
- Delete: `frontend/src/screens/AiPrediction.svelte`

**Interfaces:**
- Consumes: `getHistory`, `startPredict`, `watchPredict` (Task 4); store `source`/`history`/`aiState`/`ai`/`predictLog`.
- Produces: view `predict`; a deep-link that sets `state.source = {kind:'history', file, label}` and `view='predict'`.

- [ ] **Step 1: Create `Predict.svelte`**

Create `frontend/src/screens/Predict.svelte`:

```svelte
<script>
  import { onMount } from 'svelte'
  import { state } from '../lib/store.js'
  import { getHistory, startPredict, watchPredict } from '../lib/api.js'
  import { autoscroll } from '../lib/ui.js'
  import { fmtDate } from '../lib/fmt.js'

  const goHub = () => state.update(s => ({ ...s, view: 'hub' }))

  let dragOver = false
  let fileError = ''            // client-side drop rejection

  const REASONS = {
    cli_missing: { title: 'AI prediction needs the Claude CLI', body: 'Install it and log in with your Claude subscription, then retry:' },
    not_logged_in: { title: 'Claude isn’t logged in', body: 'Log in with your Claude subscription, then retry:' },
    parse_failed: { title: 'Couldn’t read a prediction from this data', body: 'The model didn’t return a usable result. Try again.' },
    no_breakout_data: { title: 'This file has no breakout data', body: 'Prediction reads views ÷ subscribers. This TSV has no subscriber counts (a Fast-mode export), so there’s nothing to analyse.' },
    empty: { title: 'That file is empty', body: 'Pick a snapshot or drop a TSV that has rows in it.' },
    bad_columns: { title: 'That doesn’t look like a results TSV', body: 'Export a snapshot from YouTube Content Research, or drop a tab-separated file with a subscribers column.' },
    too_large: { title: 'That file is too large', body: 'The limit is 10 MB. Pick a snapshot from history instead.' },
    error: { title: 'Couldn’t generate a prediction', body: 'Something went wrong talking to Claude. Try again.' },
  }
  $: reason = $state.ai && (REASONS[$state.ai.reason] || REASONS.error)
  $: needsCli = $state.ai && ($state.ai.reason === 'cli_missing' || $state.ai.reason === 'not_logged_in')
  $: canPredict = !!$state.source && $state.aiState !== 'loading'

  onMount(loadHistory)

  async function loadHistory() {
    state.update(s => ({ ...s, historyState: 'loading' }))
    try {
      const { snapshots } = await getHistory()
      state.update(s => ({ ...s, history: snapshots, historyState: 'idle' }))
    } catch (_) {
      state.update(s => ({ ...s, historyState: 'error' }))
    }
  }

  function pickHistory(item) {
    fileError = ''
    state.update(s => ({ ...s, source: { kind: 'history', file: item.file, label: `${fmtDate(item.date)} · ${item.count} videos` } }))
  }

  function onFiles(fileList) {
    const f = fileList && fileList[0]
    if (!f) return
    if (!f.name.toLowerCase().endsWith('.tsv')) { fileError = 'That’s not a .tsv file.'; return }
    if (f.size > 10 * 1024 * 1024) { fileError = 'That file is larger than 10 MB.'; return }
    fileError = ''
    state.update(s => ({ ...s, source: { kind: 'file', file: f, label: f.name } }))
  }

  function onDrop(e) {
    e.preventDefault(); dragOver = false
    onFiles(e.dataTransfer.files)
  }

  const clearSource = () => state.update(s => ({ ...s, source: null }))

  function run() {
    if (!canPredict) return
    const source = $state.source
    state.update(s => ({ ...s, aiState: 'loading', ai: null, predictLog: '' }))
    startPredict(source).then(({ job_id }) => {
      state.update(s => ({ ...s, jobId: job_id }))
      watchPredict(job_id,
        (chunk) => state.update(s => ({ ...s, predictLog: s.predictLog + chunk })),
        (pred) => {
          if (pred && pred.ok) state.update(s => ({ ...s, aiState: 'done', ai: pred }))
          else state.update(s => ({ ...s, aiState: 'error', ai: pred || { reason: 'error' } }))
        })
    }).catch((e) => {
      state.update(s => ({ ...s, aiState: 'error', ai: { reason: e.message || 'error' } }))
    })
  }

  // Regenerate reuses the existing synthetic job (rows already held there).
  function regenerate() {
    if (!$state.jobId) return run()
    state.update(s => ({ ...s, aiState: 'loading', ai: null, predictLog: '' }))
    watchPredict($state.jobId,
      (chunk) => state.update(s => ({ ...s, predictLog: s.predictLog + chunk })),
      (pred) => {
        if (pred && pred.ok) state.update(s => ({ ...s, aiState: 'done', ai: pred }))
        else state.update(s => ({ ...s, aiState: 'error', ai: pred || { reason: 'error' } }))
      })
  }
</script>

<div style="max-width:960px;margin:0 auto;padding:30px 24px 60px">
  <a on:click={goHub} style="display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:600;color:#5C6470;margin-bottom:14px;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>All tools</a>
  <h1 style="margin:0;font-weight:600;font-size:1.85rem;letter-spacing:-.025em;color:#1B1D21">AI Prediction</h1>
  <p style="margin:9px 0 0;color:#5C6470;font-size:.96rem;max-width:56ch">Pick a saved research snapshot, or drop a TSV export, and predict your next video.</p>

  {#if $state.aiState === 'idle' || (!$state.ai && $state.aiState !== 'loading')}
    <!-- SOURCE PICKER: history primary, upload secondary -->
    <div style="display:grid;grid-template-columns:1.6fr 1fr;gap:16px;margin-top:22px">
      <!-- history (primary) -->
      <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:20px 22px">
        <div style="font-weight:600;font-size:1rem;color:#1B1D21;margin-bottom:12px">Your snapshots</div>
        {#if $state.historyState === 'loading'}
          <div style="color:#8A93A0;font-size:.88rem;padding:18px 0">Loading history…</div>
        {:else if $state.historyState === 'error'}
          <div style="font-size:.88rem;color:#B23B3B">Couldn’t load history. <a on:click={loadHistory} style="color:#1B1D21;font-weight:600;cursor:pointer;text-decoration:underline">Retry</a></div>
        {:else if $state.history.length === 0}
          <div style="color:#8A93A0;font-size:.9rem;line-height:1.55;padding:10px 0">No snapshots yet — run YouTube Content Research, or drop a TSV on the right.</div>
        {:else}
          <div style="display:flex;flex-direction:column;gap:8px;max-height:340px;overflow:auto">
            {#each $state.history as item (item.file)}
              {@const active = $state.source && $state.source.kind === 'history' && $state.source.file === item.file}
              <div on:click={() => pickHistory(item)} role="button" tabindex="0"
                style="cursor:pointer;border-radius:12px;padding:12px 14px;border:1.5px solid {active ? '#121316' : '#E7EBEF'};background:{active ? '#fff' : '#FBFCFE'}">
                <div style="font-weight:600;font-size:.9rem;color:#1B1D21">{fmtDate(item.date)} · {item.count} videos</div>
                <div style="font-size:.76rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{item.keywords.slice(0, 4).join(', ')}{item.keywords.length > 4 ? ` +${item.keywords.length - 4}` : ''}</div>
              </div>
            {/each}
          </div>
        {/if}
      </div>

      <!-- upload (secondary) -->
      <div>
        <label
          on:dragover|preventDefault={() => dragOver = true}
          on:dragleave={() => dragOver = false}
          on:drop={onDrop}
          style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;height:100%;min-height:160px;cursor:pointer;border-radius:18px;border:2px dashed {dragOver ? '#121316' : '#CBD5E1'};background:{dragOver ? '#F2F6FF' : '#FBFCFE'};padding:22px">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8A93A0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 16V4M7 9l5-5 5 5M5 20h14"/></svg>
          <span style="font-size:.86rem;font-weight:600;color:#1B1D21">Drop a .tsv here</span>
          <span style="font-size:.76rem;color:#8A93A0">or click to browse</span>
          <input type="file" accept=".tsv" on:change={(e) => onFiles(e.target.files)} style="display:none">
        </label>
        {#if fileError}<p style="margin:8px 2px 0;font-size:.8rem;color:#B23B3B;font-weight:600">{fileError}</p>{/if}
      </div>
    </div>

    <!-- active source chip + predict -->
    <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:18px;flex-wrap:wrap">
      <div style="min-height:34px;display:flex;align-items:center">
        {#if $state.source}
          <span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:7px 8px 7px 14px;font-weight:600;font-size:.84rem;color:#1B1D21">
            {$state.source.label}
            <button on:click={clearSource} title="Clear" style="width:20px;height:20px;border:none;border-radius:50%;background:#F2F4F6;color:#5C6470;cursor:pointer;display:flex;align-items:center;justify-content:center"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
          </span>
        {:else}
          <span style="font-size:.84rem;color:#8A93A0">Pick a snapshot or drop a TSV to enable Predict.</span>
        {/if}
      </div>
      <button on:click={run} disabled={!canPredict} style="display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;border:none;border-radius:999px;padding:11px 20px;font-weight:600;font-size:.88rem;cursor:{canPredict ? 'pointer' : 'not-allowed'};opacity:{canPredict ? 1 : .45};box-shadow:0 8px 20px rgba(18,19,22,.25)">Predict <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </div>

  {:else if $state.aiState === 'loading'}
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:26px 28px;margin-top:22px">
      <div style="display:flex;align-items:center;gap:13px">
        <span style="display:inline-block;width:26px;height:26px;flex:none;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
        <div>
          <div style="font-weight:600;color:#1B1D21">Analysing your snapshot…</div>
          <div style="font-size:.84rem;color:#8A93A0">Live output from Claude as it reads your data</div>
        </div>
      </div>
      <div use:autoscroll style="margin-top:16px;background:#0E1116;border-radius:12px;padding:16px 18px;height:300px;overflow:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.65;color:#C7D0DA;white-space:pre-wrap;word-break:break-word">{$state.predictLog || 'starting…'}<span style="color:#5B6675">▌</span></div>
    </div>

  {:else if $state.aiState === 'error'}
    <div style="background:#fff;border:1px solid #F3D3D3;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:34px;margin-top:22px">
      <div style="font-weight:700;font-size:1.05rem;color:#B23B3B">{reason.title}</div>
      <p style="margin:8px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">{reason.body}</p>
      {#if needsCli}
        <pre style="margin:12px 0 0;background:#F7F8FA;border:1px solid #E7EBEF;border-radius:10px;padding:12px 14px;font-size:.8rem;color:#1B1D21;white-space:pre-wrap">npm install -g @anthropic-ai/claude-code
claude        # then /login</pre>
      {/if}
      <button on:click={() => state.update(s => ({ ...s, aiState: 'idle', ai: null }))} style="margin-top:16px;background:#121316;color:#fff;border:none;border-radius:999px;padding:10px 17px;font-weight:600;font-size:.85rem;cursor:pointer">Choose another source</button>
    </div>

  {:else if $state.ai}
    {@const ai = $state.ai}
    <div style="animation:fadeup .4s ease;margin-top:22px">
      <div style="background:#121316;border-radius:22px;padding:30px 32px;color:#fff;position:relative;overflow:hidden">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap">
          <div style="font-size:.68rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#9ED4F8">Predicted next video</div>
          <span style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:6px 13px;font-weight:700;font-size:.8rem">est. breakout ×<b style="color:#9ED4F8">{ai.est}</b></span>
        </div>
        <h2 style="margin:14px 0 0;font-weight:600;font-size:1.72rem;letter-spacing:-.02em;line-height:1.18;color:#fff;max-width:24ch">{ai.topic}</h2>
        <p style="margin:14px 0 0;color:#C7CDD4;font-size:.96rem;line-height:1.6;max-width:64ch">{ai.rationale}</p>
        {#if ai.angle}
        <div style="display:inline-flex;align-items:flex-start;gap:9px;margin-top:18px;background:rgba(207,234,255,.12);border:1px solid rgba(158,212,248,.3);border-radius:12px;padding:12px 15px;max-width:64ch">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ED4F8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;margin-top:1px"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg>
          <span style="font-size:.88rem;color:#E7EBEF;line-height:1.5">{ai.angle}</span>
        </div>
        {/if}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px">
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">Why this will work</h3>
          <div style="display:flex;flex-direction:column;gap:13px">
            {#each ai.evidence as e}
              <div style="display:flex;gap:11px"><span style="flex:none;width:23px;height:23px;border-radius:50%;background:#DFF6EA;color:#1E7A4D;display:flex;align-items:center;justify-content:center;margin-top:1px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span style="font-size:.87rem;color:#5C6470;line-height:1.5">{e}</span></div>
            {/each}
          </div>
        </div>
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">More ideas to test</h3>
          <div style="display:flex;flex-direction:column;gap:10px">
            {#each ai.ideas as idea}
              <div style="display:flex;align-items:center;gap:12px;background:#FBFCFE;border:1px solid #E7EBEF;border-radius:12px;padding:11px 13px"><span style="flex:1;font-weight:600;font-size:.86rem;color:#1B1D21;line-height:1.35">{idea.title}</span>{#if idea.est}<span style="flex:none;display:inline-flex;align-items:center;background:#121316;color:#fff;font-weight:700;font-size:.74rem;padding:4px 9px;border-radius:999px">×<b style="color:#9ED4F8">{idea.est}</b></span>{/if}</div>
            {/each}
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:18px;flex-wrap:wrap">
        <button on:click={() => state.update(s => ({ ...s, aiState: 'idle', ai: null, source: null }))} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:9px 16px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer">Predict another</button>
        <button on:click={regenerate} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:9px 16px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 4v4h-4"/></svg>Regenerate</button>
      </div>
    </div>
  {/if}
</div>
```

- [ ] **Step 2: Add the Hub card**

In `frontend/src/screens/Hub.svelte`, add a handler and a second live card. In `<script>`, after the existing `openTool`:

```javascript
  const openPredict = () => state.update(s => ({ ...s, view: 'predict', source: null, aiState: 'idle', ai: null }))
```

Then, in the grid, immediately AFTER the closing `</div>` of the first (YouTube Content Research) live card and BEFORE the `{#each [` block, insert:

```svelte
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:24px;display:flex;flex-direction:column;gap:16px">
      <div style="display:flex;align-items:center;justify-content:space-between">
        <span style="width:44px;height:44px;border-radius:13px;background:#121316;display:flex;align-items:center;justify-content:center"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg></span>
        <span style="display:inline-flex;align-items:center;gap:6px;background:#DFF6EA;color:#1E7A4D;border-radius:999px;padding:5px 11px;font-weight:700;font-size:.72rem"><span style="width:7px;height:7px;border-radius:50%;background:#34A86B"></span>Live</span>
      </div>
      <div>
        <h3 style="font-weight:600;font-size:1.12rem;color:#1B1D21;margin:0">AI Prediction</h3>
        <p style="margin:7px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">Feed a research snapshot (or any results TSV) to Signal AI and get your predicted next video, with the breakout evidence behind it.</p>
      </div>
      <button on:click={openPredict} style="align-self:flex-start;margin-top:2px;display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;border:none;border-radius:999px;padding:11px 19px;font-weight:600;font-size:.88rem;cursor:pointer;box-shadow:0 8px 20px rgba(18,19,22,.25)">Open tool <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </div>
```

Then remove ONE placeholder from the `{#each [ ... ]}` array so the grid stays even — delete the `{ t: 'Trend Tracker', ... }` object (keep the other two coming-soon cards).

- [ ] **Step 3: Route the predict view in App.svelte; drop AiPrediction**

In `frontend/src/App.svelte`:

Remove the import line:

```javascript
  import AiPrediction from './screens/AiPrediction.svelte'
```

Add:

```javascript
  import Predict from './screens/Predict.svelte'
```

Change the `inTool` derived line:

```javascript
  $: inTool = $state.view === 'results'
```

Replace the render block:

```svelte
  {:else if inTool}
    {#if $state.view === 'results'}
      <Results />
    {:else}
      <AiPrediction />
    {/if}
  {/if}
```

with:

```svelte
  {:else if $state.view === 'results'}
    <Results />
  {:else if $state.view === 'predict'}
    <Predict />
  {/if}
```

- [ ] **Step 4: Remove the AI tab from ToolHeader**

In `frontend/src/screens/ToolHeader.svelte`, delete the `goAi` handler line and the AI-prediction `<button>` (the second chip). Keep the "New run" link and the "Results" chip. The tab row becomes a single Results chip:

Remove:
```javascript
  const goAi = () => state.update(s => ({ ...s, view: 'ai' }))
```
Remove the `<button on:click={goAi} ...>…AI prediction</button>` element.

- [ ] **Step 5: Add the "Predict next video" deep-link on Results**

In `frontend/src/screens/Results.svelte`, in `<script>` add a handler:

```javascript
  function predictThisRun() {
    const s = $state
    // Deep-link into the standalone tool with THIS snapshot preselected when it
    // came from history; the store already holds the rows/jobId either way.
    state.update(v => ({ ...v, view: 'predict', aiState: 'idle', ai: null, predictLog: '',
      source: v.date ? { kind: 'history', file: `web_youtube_results_${v.date}.tsv`, label: `${v.date} · ${v.rows.length} videos` } : null }))
  }
```

Then in the results header row (the `div` at `:60` holding the Download link), add a Predict button just before the Download `<a>`, inside that flex container:

```svelte
      <div style="display:flex;gap:10px">
        {#if !fast}
          <button on:click={predictThisRun} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;color:#1B1D21;border-radius:999px;padding:10px 16px;font-weight:600;font-size:.85rem;cursor:pointer"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg>Predict next video</button>
        {/if}
        <a href={downloadUrl($state.jobId)} ...existing Download link unchanged...>...</a>
      </div>
```

Note: wrap the existing Download `<a>` and the new button in the `div style="display:flex;gap:10px"` shown above (replace the bare `<a ...>Download TSV</a>` with the wrapped pair). Leave the Download link's own attributes/markup exactly as they are.

- [ ] **Step 6: Delete AiPrediction.svelte**

```bash
git rm frontend/src/screens/AiPrediction.svelte
```

- [ ] **Step 7: Build**

Run: `cd frontend && npm run build`
Expected: build succeeds; no remaining references to `AiPrediction` or the `ai` view.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "feat(predict-ui): standalone Predict screen, Hub card, routing, deep-link; remove AI tab"
```

---

## Task 6: Progress parser + re-skinned RunProgress screen

**Files:**
- Modify: `frontend/package.json` (add vitest + `test` script)
- Create: `frontend/src/lib/progress.js`
- Create: `frontend/src/lib/progress.test.js`
- Create: `frontend/src/screens/RunProgress.svelte`
- Modify: `frontend/src/screens/Results.svelte` (render `RunProgress` while running)
- Modify: `frontend/src/screens/Input.svelte` (set `runStartMs` at run start)

**Interfaces:**
- Consumes: store `progress`, `runStartMs`, `cancelling`; `cancelJob` (existing).
- Produces:
  - `computeProgress(lines) -> {pct, phaseIndex, phase, videos, channels, totalChannels}`.
  - `estimateTimeLeft(pct, elapsedMs, phaseIndex) -> number | null` (ms, null when not confident).
  - `STEPS: string[]` (4 labels).

- [ ] **Step 1: Add vitest to package.json**

In `frontend/package.json`, add a `test` script and `vitest` devDependency:

```json
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "test": "vitest run"
  },
  "devDependencies": {
    "@sveltejs/vite-plugin-svelte": "^4.0.0",
    "svelte": "^5.0.0",
    "vite": "^5.4.0",
    "vitest": "^2.1.0"
  }
```

Then install:

Run: `cd frontend && npm install`
Expected: vitest added.

- [ ] **Step 2: Write the failing parser tests**

Create `frontend/src/lib/progress.test.js`:

```javascript
import { describe, it, expect } from 'vitest'
import { computeProgress, estimateTimeLeft, STEPS } from './progress.js'

describe('computeProgress', () => {
  it('counts videos from search-phase lines and reaches phase 1', () => {
    const r = computeProgress([
      '[1/2] Searching "ai tools" ...',
      '[1/2] ai tools — 30 videos',
      '[2/2] Searching "ml" ...',
      '[2/2] ml — 20 videos',
    ])
    expect(r.videos).toBe(50)
    expect(r.phaseIndex).toBe(1)
    expect(r.phase).toBe(STEPS[1])
  })

  it('tracks channel lookups as phase 2 with channel counts', () => {
    const r = computeProgress([
      'Looking up 12 channels for subscriber counts + topics ...',
      '[3/12] Some Channel ... ok',
    ])
    expect(r.phaseIndex).toBe(2)
    expect(r.channels).toBe(3)
    expect(r.totalChannels).toBe(12)
  })

  it('derives pct from the most recent [i/n] marker', () => {
    const r = computeProgress(['[1/2] Searching "a" ...', '[1/4] X ... ok'])
    expect(r.pct).toBe(25)
  })
})

describe('estimateTimeLeft', () => {
  it('returns null before the first phase or with too little signal', () => {
    expect(estimateTimeLeft(0, 1000, 0)).toBeNull()
    expect(estimateTimeLeft(5, 1000, 1)).toBeNull()   // pct < 10
    expect(estimateTimeLeft(100, 1000, 2)).toBeNull() // done
  })
  it('extrapolates once past the first phase', () => {
    // 25% took 10s -> total ~40s -> ~30s left
    expect(estimateTimeLeft(25, 10000, 2)).toBe(30000)
  })
})
```

- [ ] **Step 3: Run, verify fail**

Run: `cd frontend && npm test`
Expected: FAIL (`progress.js` not found).

- [ ] **Step 4: Implement the parser**

Create `frontend/src/lib/progress.js`:

```javascript
// Pure progress parsing for the scrape run screen. No Svelte — unit-tested.
// Log-line shapes come from backend/youtube_scraper.py run_scrape/helpers:
//   search:   [i/n] Searching "kw" ...      /  [i/n] kw — N videos
//   detail:   "   video N — fetching ..."   (full mode per-video)
//   channels: "Looking up N channels ..."   /  [i/n] name ... ok

export const STEPS = [
  'Searched keywords',
  'Pulled videos',
  'Looking up channels',
  'Score breakout multipliers',
]

export function computeProgress(lines) {
  let phaseIndex = 0
  let videos = 0, channels = 0, totalChannels = 0
  for (const raw of lines) {
    const line = raw || ''
    const v = line.match(/—\s*(\d+)\s*videos?/i)
    if (v) { videos += +v[1]; phaseIndex = Math.max(phaseIndex, 1) }
    if (/^\s*video\s+\d+\s+—/i.test(line)) phaseIndex = Math.max(phaseIndex, 1)
    const lu = line.match(/Looking up\s+(\d+)\s+channels/i)
    if (lu) { totalChannels = +lu[1]; phaseIndex = Math.max(phaseIndex, 2) }
    const ch = line.match(/^\[(\d+)\/(\d+)\].*\.\.\.\s*ok$/i)
    if (ch) { channels = +ch[1]; totalChannels = +ch[2]; phaseIndex = Math.max(phaseIndex, 2) }
  }
  let pct = 0
  for (let i = lines.length - 1; i >= 0; i--) {
    const m = (lines[i] || '').match(/\[(\d+)\/(\d+)\]/)
    if (m) { pct = Math.round((+m[1] / +m[2]) * 100); break }
  }
  return { pct, phaseIndex, phase: STEPS[phaseIndex], videos, channels, totalChannels }
}

// Time-left in ms, or null when we should not show a number yet (D3):
// before the first phase, too little signal, or already complete.
export function estimateTimeLeft(pct, elapsedMs, phaseIndex) {
  if (phaseIndex < 1 || pct < 10 || pct >= 100) return null
  const total = elapsedMs / (pct / 100)
  return Math.max(0, Math.round(total - elapsedMs))
}
```

- [ ] **Step 5: Run, verify pass**

Run: `cd frontend && npm test`
Expected: PASS (5 tests).

- [ ] **Step 6: Create the re-skinned RunProgress screen**

Create `frontend/src/screens/RunProgress.svelte`:

```svelte
<script>
  import { onMount, onDestroy } from 'svelte'
  import { state } from '../lib/store.js'
  import { cancelJob } from '../lib/api.js'
  import { autoscroll } from '../lib/ui.js'
  import { computeProgress, estimateTimeLeft, STEPS } from '../lib/progress.js'

  let now = Date.now()
  const tick = setInterval(() => { now = Date.now() }, 1000)
  onDestroy(() => clearInterval(tick))

  $: p = computeProgress($state.progress)
  $: elapsedMs = $state.runStartMs ? now - $state.runStartMs : 0
  $: leftMs = estimateTimeLeft(p.pct, elapsedMs, p.phaseIndex)

  const fmtClock = (ms) => {
    const s = Math.round(ms / 1000)
    const m = Math.floor(s / 60)
    return `${m}:${String(s % 60).padStart(2, '0')}`
  }

  async function cancel() {
    state.update(s => ({ ...s, cancelling: true }))
    await cancelJob($state.jobId)
  }
</script>

<div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:26px 28px">
  <!-- header: phase + cancel -->
  <div style="display:flex;align-items:center;gap:13px">
    <span style="display:inline-block;width:26px;height:26px;flex:none;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
    <div style="flex:1;min-width:0">
      <div style="font-weight:600;color:#1B1D21">{p.phase}…</div>
      <div style="font-size:.84rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{$state.progress.length ? $state.progress[$state.progress.length - 1] : 'Starting the scrape…'}</div>
    </div>
    <button on:click={cancel} disabled={$state.cancelling} style="flex:none;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:8px 16px;font-weight:600;font-size:.84rem;color:#1B1D21;cursor:pointer">{$state.cancelling ? 'Cancelling…' : 'Cancel run'}</button>
  </div>

  <!-- phase stepper -->
  <div style="display:flex;gap:8px;margin-top:18px;flex-wrap:wrap">
    {#each STEPS as label, i}
      {@const done = i < p.phaseIndex}
      {@const active = i === p.phaseIndex}
      <div style="flex:1;min-width:130px;border-radius:12px;padding:10px 12px;border:1.5px solid {active ? '#121316' : '#E7EBEF'};background:{done ? '#F1FAF4' : (active ? '#fff' : '#FBFCFE')}">
        <div style="display:flex;align-items:center;gap:7px">
          <span style="width:18px;height:18px;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;background:{done ? '#DFF6EA' : (active ? '#121316' : '#E7EBEF')};color:{done ? '#1E7A4D' : '#fff'};font-size:.66rem;font-weight:700">{#if done}<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>{:else}{i + 1}{/if}</span>
          <span style="font-size:.76rem;font-weight:600;color:{active || done ? '#1B1D21' : '#8A93A0'}">{label}</span>
        </div>
      </div>
    {/each}
  </div>

  <!-- progress bar -->
  <div style="margin-top:16px;height:7px;border-radius:999px;background:#EEF1F4;overflow:hidden">
    <div style="height:100%;border-radius:999px;background:#121316;width:{p.pct}%;transition:width .4s ease"></div>
  </div>

  <!-- counters -->
  <div style="display:flex;gap:22px;margin-top:14px;flex-wrap:wrap">
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Videos</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{p.videos}</div></div>
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Channels</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{p.channels}{#if p.totalChannels}/{p.totalChannels}{/if}</div></div>
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Elapsed</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{fmtClock(elapsedMs)}</div></div>
    {#if leftMs !== null}
      <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Time left</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">~{fmtClock(leftMs)}</div></div>
    {/if}
  </div>

  <!-- live feed -->
  <div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0;margin:18px 0 7px">Live feed</div>
  <div use:autoscroll style="background:#0E1116;border-radius:12px;padding:14px 16px;height:200px;overflow:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.7;color:#C7D0DA">
    {#each $state.progress as line}
      <div><span style="color:#4B5563">$</span> <span style="color:{line.includes('FAILED') ? '#F0A0A0' : (line.includes('Cancelled') ? '#F0C674' : '#9ED4F8')}">{line}</span></div>
    {/each}
    <div style="color:#5B6675">▌</div>
  </div>
</div>
```

- [ ] **Step 7: Render RunProgress from Results.svelte**

In `frontend/src/screens/Results.svelte`:

Add the import in `<script>`:

```javascript
  import RunProgress from './RunProgress.svelte'
```

Replace the entire `{#if $state.running} … {:else if $state.error}` running block (the inline card at `:27-50`) with:

```svelte
  {#if $state.running}
    <RunProgress />
  {:else if $state.error}
```

(Leave everything from `{:else if $state.error}` onward unchanged.) The now-unused imports `cancelJob` and `autoscroll` in Results.svelte can stay or be removed; remove `cancelJob` and the `cancel()` function and the `runProgress` store import if they are no longer referenced elsewhere in the file — verify with the build.

- [ ] **Step 8: Set runStartMs when a scrape starts**

In `frontend/src/screens/Input.svelte`, in `doRun()`, find the `state.update` that sets `view: 'results', running: true, ...` and add `runStartMs: Date.now()`:

```javascript
    state.update(s => ({ ...s, view: 'results', running: true, cancelling: false,
      jobId: job.job_id, progress: [], error: null, rows: [], ai: null, aiState: 'idle',
      runStartMs: Date.now() }))
```

- [ ] **Step 9: Tests + build green**

Run: `cd frontend && npm test && npm run build`
Expected: vitest PASS (5), build succeeds.

- [ ] **Step 10: Commit**

```bash
git add -A
git commit -m "feat(progress): re-skinned RunProgress screen + unit-tested progress parser"
```

---

## Task 7: Full verification

- [ ] **Step 1: Backend suite**

Run: `cd backend && pytest -q`
Expected: all pass.

- [ ] **Step 2: Frontend unit + build**

Run: `cd frontend && npm test && npm run build`
Expected: vitest pass; build ok.

- [ ] **Step 3: Manual smoke (per spec Testing section)**

Start the app (`./run.sh web`), then:
1. Hub shows two live cards. Open **AI Prediction** → history list populated (or empty state if none), drag-drop box on the right.
2. Pick a history snapshot → chip appears → **Predict** → live log → result card. **Regenerate** works.
3. Drop the fast-mode TSV (or a `youtube_results_*` fast snapshot) → after Predict, "This file has no breakout data".
4. Drop a `.csv` → inline "not a .tsv" rejection before Predict.
5. Run a **Full** scrape from YouTube Content Research → the new progress screen shows the stepper advancing, Videos/Channels/Elapsed counters, time-left appearing only after phase 1, live feed streaming, Cancel works.
6. On the results screen, **Predict next video** deep-links into the tool with the run preselected.

- [ ] **Step 4: Final commit (if any manual fixes)**

```bash
git add -A && git commit -m "chore: post-verification fixes"
```

---

## Self-Review Notes (author)

- **Spec coverage:** GET /api/history (T3), POST /api/predict upload+history+guard (T2/T3), synthetic job reuse (T3), eviction guard A3 (T1), python-multipart A1 (T1), absolute HISTORY_DIR A2 (T2), traversal guard A8 (T2), breakout guard A4/A5 + fast-mode reject F5 (T2/T3), date-sort A7 (T2), Predict screen with history-first D2 + empty/loading/error states A10 + client rejection A11 + chip A12 (T5), reuse result markup + delete AiPrediction (T5), Hub card + placeholder swap (T5), remove AI tab + route predict + drop `ai` enum A9 (T5), deep-link D1 (T5), progress re-skin with explicit stepper state machine A13 + honest time-left D3 (T6), progress unit tests (T6). Regenerate reuses job_id A14 (T5). Keyword truncation A15 (T5, `slice(0,4)`).
- **Deferred (spec §Deferred):** history delete/rename, per-item no-breakout badge, history pruning, full-file-read caching A8-perf, predict-session restore across refresh — intentionally NOT in this plan.
- **Type consistency:** `source` shape `{kind, file, label}` is identical in store, `startPredict`, `Predict.svelte`, and the Results deep-link. `computeProgress` return keys match `RunProgress.svelte` usage.
