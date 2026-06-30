# Voyara Signal Web App Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the `Voyara Signal.dc.html` prototype into a real local web app that drives the existing Python YouTube scraper, shows live results with sort/filter, generates an AI "next video" prediction, and downloads TSV — matching the prototype's 4-screen design.

**Architecture:** A FastAPI backend wraps the existing Python modules (`youtube_scraper`, `history`, `analyze`, `ideas`) as HTTP+SSE endpoints and serves a built Svelte single-page app. Scrapes run in a background thread with live progress streamed over Server-Sent Events; the browser does all sorting/filtering client-side. No scraping or AI logic is rewritten — only a thin web layer plus surgical refactors so the modules are callable as functions.

**Tech Stack:** Python 3.12, FastAPI, uvicorn, sse-starlette, pytest, httpx (test client); Svelte 5 + Vite (frontend, built to static files served by FastAPI); existing `yt-dlp` + `claude-agent-sdk`.

## Global Constraints

- Python floor: 3.8+ (match existing `run.sh`); dev/CI uses the repo `venv/` (3.12).
- Do NOT modify the behavior of the existing CLI: `./run.sh`, `./run.sh ideas`, `./run.sh diff` must keep working exactly as before. Refactors must be behavior-preserving for `main()`.
- Reuse existing modules; never duplicate scraping/metric logic. `breakout` mirrors `analyze.views_per_sub` (= views / subscribers).
- AI runs through the Claude subscription via `claude-agent-sdk` (same auth as `ideas.py`); never require `ANTHROPIC_API_KEY`.
- Local single-user tool only. Bind the server to `127.0.0.1`. No auth, no multi-user.
- TSV output format (columns, `utf-8-sig`, tab delimiter) stays identical to `youtube_scraper.write_tsv`.
- Date-filter labels map to YouTube `sp` codes that actually exist (`SP_FILTERS`): `Any time→none`, `This year→year`, `This month→month`, `This week→week`. (The prototype's "Last 6 months" has no real YouTube code, so it is replaced by "This week".)
- New Python deps pinned in `requirements.txt`: `fastapi>=0.110`, `uvicorn>=0.29`, `sse-starlette>=2.0`, and test-only `pytest>=8.0`, `httpx>=0.27`.

---

## File Structure

**Backend (new in `server/`):**
- `server/__init__.py` — package marker.
- `server/inputs.py` — parse the textarea into scrape URLs; map UI labels (date filter, per-link, fast) to scraper params. Pure functions.
- `server/serialize.py` — convert a scraper row dict into the API/JSON shape the frontend table consumes, including computed `breakout`. Pure functions.
- `server/jobs.py` — `JobManager` + `Job`: background scrape jobs, progress capture, status, error capture, TSV path.
- `server/app.py` — FastAPI app: routes, SSE, static file serving, wiring to existing modules.

**Existing Python (surgical changes):**
- `youtube_scraper.py` — extract a callable `run_scrape(...)` from `main()`; `main()` calls it with a print callback (behavior unchanged).
- `ideas.py` — add structured-JSON prediction (`generate_prediction`, `parse_prediction_json`, `normalize_prediction`, `PREDICTION_FALLBACK`). Existing markdown `run()` untouched.

**Tests (new in `tests/`):**
- `tests/test_inputs.py`, `tests/test_serialize.py`, `tests/test_jobs.py`, `tests/test_predict.py`, `tests/test_run_scrape.py`, `tests/test_app.py`.

**Frontend (new in `web/`, Vite + Svelte):**
- `web/package.json`, `web/vite.config.js`, `web/index.html`, `web/src/main.js`
- `web/src/lib/api.js` — fetch + SSE helpers.
- `web/src/lib/store.js` — app state (view, run params, results, sort/filter, ai state).
- `web/src/App.svelte` — nav + view router.
- `web/src/screens/Hub.svelte`, `Input.svelte`, `Results.svelte`, `AiPrediction.svelte`
- Build output `web/dist/` is served by FastAPI (gitignored).

**Runner:**
- `run.sh` — add a `web` subcommand that installs deps (first run) and launches the server.

---

## Task 1: Refactor `youtube_scraper` into a callable `run_scrape`

**Files:**
- Modify: `youtube_scraper.py` (extract from `main()`, add `run_scrape`)
- Test: `tests/test_run_scrape.py`

**Interfaces:**
- Produces: `run_scrape(urls: list[str], limit: int, fast: bool, channel_info: bool, cookies: str | None = None, progress=None) -> list[dict]`. `progress` is an optional callable `progress(str) -> None` invoked with human-readable status lines. Returns the same row dicts `entry_to_row` produces. `COLUMNS` remains importable and unchanged.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_run_scrape.py
import youtube_scraper as ys


def test_run_scrape_calls_progress_and_returns_rows(monkeypatch):
    # Stub the network layer so no YouTube call happens.
    fake_rows = {
        "https://yt/?search_query=a": [{"video_id": "x1", "keyword": "a", "views": 10}],
        "https://yt/?search_query=b": [{"video_id": "x2", "keyword": "b", "views": 20}],
    }
    monkeypatch.setattr(ys, "scrape_url", lambda url, limit: fake_rows[url])
    # In fast mode channel enrichment must NOT run.
    monkeypatch.setattr(ys, "enrich_with_channel_info",
                        lambda rows: (_ for _ in ()).throw(AssertionError("should not enrich")))

    seen = []
    rows = ys.run_scrape(list(fake_rows), limit=5, fast=True, channel_info=False,
                         progress=seen.append)

    assert [r["video_id"] for r in rows] == ["x1", "x2"]
    assert any("[1/2]" in line for line in seen)
    assert any("[2/2]" in line for line in seen)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_run_scrape.py -v`
Expected: FAIL with `AttributeError: module 'youtube_scraper' has no attribute 'run_scrape'`

- [ ] **Step 3: Write minimal implementation**

Add to `youtube_scraper.py` (above `main`):

```python
def run_scrape(urls, limit, fast, channel_info, cookies=None, progress=None):
    """Callable core of the scraper. Returns row dicts; reports status via
    progress(str). Behavior matches main()'s loop but never prints/exits."""
    global RESULTS_PER_KEYWORD, COOKIES_FROM_BROWSER
    global FETCH_FULL_VIDEO_DETAILS, FETCH_CHANNEL_INFO
    RESULTS_PER_KEYWORD = limit
    COOKIES_FROM_BROWSER = cookies or None
    FETCH_FULL_VIDEO_DETAILS = not fast
    FETCH_CHANNEL_INFO = channel_info and not fast

    def say(msg):
        if progress:
            progress(msg)

    all_rows = []
    total = len(urls)
    for i, url in enumerate(urls, start=1):
        kw = keyword_from_url(url)
        try:
            rows = scrape_url(url, RESULTS_PER_KEYWORD)
            all_rows.extend(rows)
            say(f"[{i}/{total}] {kw} ... {len(rows)} videos")
        except Exception as exc:
            say(f"[{i}/{total}] {kw} ... FAILED ({exc})")
        if i < total and PAUSE_BETWEEN_URLS:
            time.sleep(PAUSE_BETWEEN_URLS)

    if all_rows and FETCH_CHANNEL_INFO:
        say(f"Looking up channels for description + subscriber counts ...")
        enrich_with_channel_info(all_rows)
    return all_rows
```

- [ ] **Step 4: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_run_scrape.py -v`
Expected: PASS

- [ ] **Step 5: Make `main()` call `run_scrape` (behavior-preserving)**

Replace the scrape loop + enrichment block in `main()` (currently `youtube_scraper.py:399-420`) with:

```python
    all_rows = run_scrape(
        urls,
        limit=RESULTS_PER_KEYWORD,
        fast=args.fast,
        channel_info=not args.no_channel_info,
        cookies=COOKIES_FROM_BROWSER,
        progress=print,
    )

    if not all_rows:
        sys.exit("\nNo data was collected. See README.txt -> Troubleshooting.")
```

- [ ] **Step 6: Verify the CLI still works (smoke, list-only)**

Run: `venv/bin/python youtube_scraper.py --keywords keywords.txt --fast --limit 3 --no-history`
Expected: prints `[1/N] ... K videos` lines and writes `youtube_results.tsv` (network permitting). If YouTube blocks, the run still exits cleanly with the existing "No data" message — no traceback.

- [ ] **Step 7: Commit**

```bash
git add youtube_scraper.py tests/test_run_scrape.py
git commit -m "refactor: extract callable run_scrape() from youtube_scraper.main()"
```

---

## Task 2: Input parsing (`server/inputs.py`)

**Files:**
- Create: `server/__init__.py` (empty), `server/inputs.py`
- Test: `tests/test_inputs.py`

**Interfaces:**
- Produces:
  - `DATE_FILTERS: dict[str, str]` = `{"Any time": "none", "This year": "year", "This month": "month", "This week": "week"}`
  - `parse_inputs(text: str, date_filter_label: str) -> list[str]` — each non-blank line: if it looks like a YouTube URL, pass through; else treat as a keyword and build a search URL with the mapped `sp` period (reusing `youtube_scraper.build_search_url`).
  - `per_link_to_int(label: str) -> int` — `"60 videos" -> 60`; default 60.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_inputs.py
from server import inputs


def test_parse_inputs_mixes_urls_and_keywords():
    text = ("https://www.youtube.com/results?search_query=best+ai+tools\n"
            "how to make money with ai\n"
            "\n"  # blank ignored
            "  # a comment\n")
    out = inputs.parse_inputs(text, "This year")
    assert out[0] == "https://www.youtube.com/results?search_query=best+ai+tools"
    assert out[1].startswith("https://www.youtube.com/results?search_query=how")
    assert "sp=" in out[1]            # keyword got the year filter
    assert len(out) == 2             # blank + comment dropped


def test_parse_inputs_any_time_has_no_sp():
    out = inputs.parse_inputs("ai agents", "Any time")
    assert "sp=" not in out[0]


def test_per_link_to_int():
    assert inputs.per_link_to_int("90 videos") == 90
    assert inputs.per_link_to_int("garbage") == 60
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_inputs.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server'` then (after creating package) import error for `inputs`.

- [ ] **Step 3: Write minimal implementation**

```python
# server/inputs.py
import youtube_scraper as ys

DATE_FILTERS = {
    "Any time": "none",
    "This year": "year",
    "This month": "month",
    "This week": "week",
}


def _looks_like_url(line):
    return line.startswith("http://") or line.startswith("https://")


def parse_inputs(text, date_filter_label):
    period = DATE_FILTERS.get(date_filter_label, "none")
    urls = []
    for raw in (text or "").splitlines():
        line = raw.strip().lstrip("*").strip()
        if not line or line.startswith("#"):
            continue
        urls.append(line if _looks_like_url(line) else ys.build_search_url(line, period))
    return urls


def per_link_to_int(label):
    try:
        return int(str(label).split()[0])
    except (ValueError, IndexError):
        return 60
```

Create empty `server/__init__.py`.

- [ ] **Step 4: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_inputs.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add server/__init__.py server/inputs.py tests/test_inputs.py
git commit -m "feat: input parsing (URLs vs keywords, date-filter mapping)"
```

---

## Task 3: Row serialization + breakout (`server/serialize.py`)

**Files:**
- Create: `server/serialize.py`
- Test: `tests/test_serialize.py`

**Interfaces:**
- Produces:
  - `row_to_api(row: dict) -> dict` with keys: `video_id, title, video_url, thumbnail, upload_date, duration, duration_sec, keyword, channel, channel_url, subscribers (int|None), verified (bool|None), views (int|None), likes (int|None), comments (int|None), breakout (float|None)`.
  - `breakout` = `round(views / subscribers, 1)` when both are positive ints, else `None`.
  - Blank scraper fields (`""`) become `None`; `verified` maps `"Yes"→True`, `"No"→False`, `""→None`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_serialize.py
from server import serialize


def test_full_row_computes_breakout():
    row = {"video_id": "x1", "title": "T", "channel": "C",
           "subscribers": "57000", "channel_verified": "No",
           "views": "1230000", "likes": "48200", "comments": "3110",
           "duration": "12:40", "duration_sec": "760", "upload_date": "2026-06-14",
           "keyword": "best ai tools", "thumbnail": "http://t", "channel_url": "http://c",
           "video_url": "http://v"}
    out = serialize.row_to_api(row)
    assert out["views"] == 1230000
    assert out["verified"] is False
    assert out["breakout"] == round(1230000 / 57000, 1)


def test_fast_mode_blanks_become_none_and_breakout_none():
    row = {"video_id": "x2", "title": "T", "channel": "C",
           "subscribers": "", "channel_verified": "", "views": "5000",
           "likes": "", "comments": "", "duration": "", "duration_sec": "",
           "upload_date": "", "keyword": "k", "thumbnail": "", "channel_url": "",
           "video_url": ""}
    out = serialize.row_to_api(row)
    assert out["subscribers"] is None
    assert out["verified"] is None
    assert out["breakout"] is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_serialize.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server.serialize'`

- [ ] **Step 3: Write minimal implementation**

```python
# server/serialize.py
def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _verified(v):
    if v == "Yes":
        return True
    if v == "No":
        return False
    return None


def row_to_api(row):
    views = _int(row.get("views"))
    subs = _int(row.get("subscribers"))
    breakout = round(views / subs, 1) if (views and subs and subs > 0) else None
    return {
        "video_id": row.get("video_id", ""),
        "title": row.get("title", ""),
        "video_url": row.get("video_url", ""),
        "thumbnail": row.get("thumbnail", ""),
        "upload_date": row.get("upload_date", ""),
        "duration": row.get("duration", ""),
        "duration_sec": _int(row.get("duration_sec")),
        "keyword": row.get("keyword", ""),
        "channel": row.get("channel", ""),
        "channel_url": row.get("channel_url", ""),
        "subscribers": subs,
        "verified": _verified(row.get("channel_verified", "")),
        "views": views,
        "likes": _int(row.get("likes")),
        "comments": _int(row.get("comments")),
        "breakout": breakout,
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_serialize.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add server/serialize.py tests/test_serialize.py
git commit -m "feat: row serialization with computed breakout + fast-mode nulls"
```

---

## Task 4: Background job manager (`server/jobs.py`)

**Files:**
- Create: `server/jobs.py`
- Test: `tests/test_jobs.py`

**Interfaces:**
- Produces:
  - `Job` with attributes `id, status ("pending"|"running"|"done"|"error"), params (dict), rows (list[dict]), error (str|None), progress (list[str])`.
  - `JobManager.create(params: dict) -> Job`
  - `JobManager.run(job: Job, scrape_fn) -> None` — synchronous core: calls `scrape_fn(progress=job.add_progress)`, stores rows, sets `status="done"`; on empty result sets `status="error"` with a bot-check message; on exception sets `status="error"` with the message. (The HTTP layer runs this in a thread; the core is sync so it is unit-testable.)
  - `JobManager.get(job_id) -> Job | None`
  - `Job.add_progress(msg: str) -> None` — appends and notifies waiters (a `queue.Queue` drained by the SSE endpoint).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_jobs.py
from server.jobs import JobManager


def test_run_success_collects_rows_and_progress():
    mgr = JobManager()
    job = mgr.create({"limit": 5})

    def fake_scrape(progress):
        progress("[1/1] k ... 2 videos")
        return [{"video_id": "a"}, {"video_id": "b"}]

    mgr.run(job, fake_scrape)
    assert job.status == "done"
    assert len(job.rows) == 2
    assert "[1/1] k ... 2 videos" in job.progress


def test_run_empty_is_botcheck_error():
    mgr = JobManager()
    job = mgr.create({})
    mgr.run(job, lambda progress: [])
    assert job.status == "error"
    assert "no videos" in job.error.lower()


def test_run_exception_is_captured():
    mgr = JobManager()
    job = mgr.create({})

    def boom(progress):
        raise RuntimeError("yt-dlp exploded")

    mgr.run(job, boom)
    assert job.status == "error"
    assert "yt-dlp exploded" in job.error
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_jobs.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'server.jobs'`

- [ ] **Step 3: Write minimal implementation**

```python
# server/jobs.py
import queue
import threading
import uuid

BOTCHECK_MSG = ("No videos were collected. YouTube may be showing a bot check — "
                "try enabling browser cookies, or check your keywords/URLs.")


class Job:
    def __init__(self, job_id, params):
        self.id = job_id
        self.params = params
        self.status = "pending"
        self.rows = []
        self.error = None
        self.progress = []
        self.events = queue.Queue()      # drained by the SSE endpoint

    def add_progress(self, msg):
        self.progress.append(msg)
        self.events.put({"type": "progress", "message": msg})


class JobManager:
    def __init__(self):
        self._jobs = {}
        self._lock = threading.Lock()

    def create(self, params):
        job = Job(uuid.uuid4().hex[:12], params)
        with self._lock:
            self._jobs[job.id] = job
        return job

    def get(self, job_id):
        return self._jobs.get(job_id)

    def run(self, job, scrape_fn):
        job.status = "running"
        try:
            rows = scrape_fn(progress=job.add_progress)
            if not rows:
                job.status = "error"
                job.error = BOTCHECK_MSG
                job.events.put({"type": "error", "message": job.error})
                return
            job.rows = rows
            job.status = "done"
            job.events.put({"type": "done", "count": len(rows)})
        except Exception as exc:  # capture, never crash the thread silently
            job.status = "error"
            job.error = str(exc)
            job.events.put({"type": "error", "message": job.error})

    def run_in_thread(self, job, scrape_fn):
        t = threading.Thread(target=self.run, args=(job, scrape_fn), daemon=True)
        t.start()
        return t
```

- [ ] **Step 4: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_jobs.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add server/jobs.py tests/test_jobs.py
git commit -m "feat: background scrape job manager with progress + error capture"
```

---

## Task 5: Structured AI prediction (`ideas.py`)

**Files:**
- Modify: `ideas.py` (add prediction functions; existing `run()`/markdown path untouched)
- Test: `tests/test_predict.py`

**Interfaces:**
- Produces:
  - `parse_prediction_json(text: str) -> dict | None` — extract first `{`…last `}` and `json.loads`; `None` on failure.
  - `normalize_prediction(obj: dict) -> dict` — coerce to `{topic, angle, est, rationale, evidence (<=4 strings), ideas (<=4 {title, est})}`; `est` is digits/`.` only.
  - `PREDICTION_FALLBACK: dict` — the design's built-in fallback (copied from `Voyara Signal.dc.html` `fallback()`).
  - `generate_prediction(rows: list[dict]) -> dict` — build digest (reusing `analyze`), call Claude via the SDK, parse+normalize; on ANY failure return `PREDICTION_FALLBACK | {"source": "fallback"}`. Success returns `normalized | {"source": "ai"}`.

- [ ] **Step 1: Write the failing test** (pure parse/normalize only — no network)

```python
# tests/test_predict.py
import ideas


def test_parse_prediction_extracts_embedded_json():
    text = 'sure! {"topic":"X","ideas":[]} done'
    assert ideas.parse_prediction_json(text)["topic"] == "X"


def test_parse_prediction_bad_returns_none():
    assert ideas.parse_prediction_json("no json here") is None


def test_normalize_clamps_and_cleans():
    obj = {"topic": "T", "angle": "A", "est_breakout": "x12",
           "rationale": "R",
           "evidence": ["a", "b", "c", "d", "e"],     # >4 -> clipped
           "ideas": [{"title": "i1", "est": "x11"}, {"title": "i2", "est": "9"},
                     {"title": "i3"}, {"title": "i4"}, {"title": "i5"}]}
    out = ideas.normalize_prediction(obj)
    assert out["est"] == "12"                  # stripped to digits
    assert len(out["evidence"]) == 4
    assert len(out["ideas"]) == 4
    assert out["ideas"][0] == {"title": "i1", "est": "11"}


def test_fallback_shape():
    fb = ideas.PREDICTION_FALLBACK
    assert fb["topic"] and isinstance(fb["evidence"], list) and len(fb["ideas"]) == 4
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_predict.py -v`
Expected: FAIL with `AttributeError: module 'ideas' has no attribute 'parse_prediction_json'`

- [ ] **Step 3: Write minimal implementation**

Add to `ideas.py`:

```python
import json
import re

PREDICTION_SYSTEM = (
    "You are a sharp YouTube content strategist. You are given real scraped "
    "data about what is currently ranking for a set of search keywords. Predict "
    "the single best NEW video a small/mid creator should make next to maximise "
    "breakout (views relative to channel size), plus 4 alternatives. Cite real "
    "numbers and titles from the data."
)

PREDICTION_INSTRUCTION = (
    "Return ONLY minified JSON, no prose: "
    '{"topic":string,"angle":string (one sentence, why now),'
    '"est_breakout":string (like \"x12\"),"rationale":string (2 sentences),'
    '"evidence":[3-4 short strings citing the data/patterns],'
    '"ideas":[{"title":string,"est":string}] (exactly 4)}.\n\nDATA DIGEST:\n'
)

PREDICTION_FALLBACK = {
    "topic": "I Built an AI Agency in 30 Days With $0 — Full Roadmap",
    "angle": ("AI agencies are the highest-breakout theme in this niche yet only "
              "~7% of videos cover them — wide open for a smaller channel."),
    "est": "12",
    "rationale": ("Agency and freelancing angles massively outperform the saturated "
                  "tool-roundup format, and long-form roadmaps are exactly what's "
                  "ranking right now. A numbered, dated, dollar-specific title stacks "
                  "every title pattern that's already working in this niche."),
    "evidence": [
        "AI agencies average ×12.1 breakout vs ×6.1 for tool roundups",
        "Numbered titles pull ~2.3× more views than non-numbered",
        "20–40 min videos hit ×9.1 — long-form dominates the leaderboard",
        "Only ~7% of tracked videos cover agencies — low supply, high demand",
    ],
    "ideas": [
        {"title": "7 AI Tools Every Real Estate Agent Needs in 2026", "est": "11"},
        {"title": "I Tried to Run My Whole Business on AI for a Week", "est": "10"},
        {"title": "The AI Tool Everyone Recommends — That Failed Me", "est": "9"},
        {"title": "Make $100/Day With AI — A Realistic Beginner Plan", "est": "8"},
    ],
}


def parse_prediction_json(text):
    if not text:
        return None
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < 0 or b < a:
        return None
    try:
        return json.loads(text[a:b + 1])
    except (ValueError, TypeError):
        return None


def _digits(x):
    return re.sub(r"[^0-9.]", "", str(x if x is not None else "")) or ""


def normalize_prediction(obj):
    ev = obj.get("evidence") if isinstance(obj.get("evidence"), list) else []
    ideas_in = obj.get("ideas") if isinstance(obj.get("ideas"), list) else []
    ideas = []
    for it in ideas_in[:4]:
        it = it if isinstance(it, dict) else {}
        ideas.append({"title": str(it.get("title", "")), "est": _digits(it.get("est"))})
    return {
        "topic": str(obj.get("topic", "")),
        "angle": str(obj.get("angle", "")),
        "est": _digits(obj.get("est_breakout")) or "10",
        "rationale": str(obj.get("rationale", "")),
        "evidence": [str(e) for e in ev[:4]],
        "ideas": ideas[:4],
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_predict.py -v`
Expected: PASS

- [ ] **Step 5: Add the network-calling `generate_prediction` (not unit-tested; verified in QA)**

```python
async def _prediction_async(digest):
    from claude_agent_sdk import (query, ClaudeAgentOptions, AssistantMessage,
                                  TextBlock, ResultMessage)
    options = ClaudeAgentOptions(
        system_prompt=PREDICTION_SYSTEM, model=MODEL, fallback_model=FALLBACK_MODEL,
        allowed_tools=[], max_turns=1, setting_sources=None,
    )
    parts, result_text = [], ""
    async for message in query(prompt=PREDICTION_INSTRUCTION + digest, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    parts.append(block.text)
        elif isinstance(message, ResultMessage):
            if message.is_error:
                raise RuntimeError(message.result or "Claude error")
            result_text = message.result or ""
    return "".join(parts) or result_text


def generate_prediction(rows):
    try:
        import anyio
        digest = build_digest(rows)
        text = anyio.run(_prediction_async, digest)
        obj = parse_prediction_json(text)
        if not obj or not obj.get("topic"):
            raise ValueError("model returned no usable prediction")
        return {**normalize_prediction(obj), "source": "ai"}
    except Exception:
        return {**PREDICTION_FALLBACK, "source": "fallback"}
```

- [ ] **Step 6: Commit**

```bash
git add ideas.py tests/test_predict.py
git commit -m "feat: structured JSON video prediction (reuses Claude SDK + analyze digest)"
```

---

## Task 6: FastAPI app + routes (`server/app.py`)

**Files:**
- Create: `server/app.py`
- Modify: `requirements.txt` (add fastapi, uvicorn, sse-starlette, pytest, httpx)
- Test: `tests/test_app.py`

**Interfaces:**
- Produces an importable `app` (FastAPI). `MANAGER = JobManager()` module-level. Routes:
  - `POST /api/run` body `{inputs, per_link, date_filter, fast, cookies}` → `{job_id}`; starts `MANAGER.run_in_thread` with a `scrape_fn` closing over `youtube_scraper.run_scrape` + parsed inputs.
  - `GET /api/jobs/{id}/events` → SSE stream of `job.events` until a `done`/`error` event.
  - `GET /api/jobs/{id}/results` → `{count, rows: [row_to_api...], date, fast}`; 404 if unknown, 409 if not done.
  - `GET /api/jobs/{id}/download` → TSV (existing `write_tsv` format) as a file response.
  - `POST /api/predict` body `{job_id}` → prediction dict from `ideas.generate_prediction(job.rows)`.
  - `GET /` and static mount serve `web/dist/` when built (skipped if absent).

- [ ] **Step 1: Write the failing test** (seed a finished job; avoid real scraping/network)

```python
# tests/test_app.py
from fastapi.testclient import TestClient
import server.app as app_mod
from server import serialize

client = TestClient(app_mod.app)


def _seed_done_job(rows):
    job = app_mod.MANAGER.create({"fast": True})
    job.rows = rows
    job.status = "done"
    return job


def test_results_returns_serialized_rows():
    job = _seed_done_job([{"video_id": "a", "views": "1000", "subscribers": "100",
                           "channel_verified": "Yes", "title": "T"}])
    r = client.get(f"/api/jobs/{job.id}/results")
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 1
    assert body["rows"][0]["breakout"] == 10.0
    assert body["rows"][0]["verified"] is True


def test_results_unknown_job_404():
    assert client.get("/api/jobs/nope/results").status_code == 404


def test_predict_uses_generate_prediction(monkeypatch):
    job = _seed_done_job([{"video_id": "a", "views": "1000", "subscribers": "100"}])
    monkeypatch.setattr(app_mod.ideas, "generate_prediction",
                        lambda rows: {"topic": "MOCK", "ideas": [], "source": "ai"})
    r = client.post("/api/predict", json={"job_id": job.id})
    assert r.status_code == 200
    assert r.json()["topic"] == "MOCK"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `venv/bin/python -m pytest tests/test_app.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'fastapi'` (until deps installed) then `No module named 'server.app'`.

- [ ] **Step 3: Install deps**

Append to `requirements.txt`:

```
fastapi>=0.110
uvicorn>=0.29
sse-starlette>=2.0
pytest>=8.0
httpx>=0.27
```

Run: `venv/bin/python -m pip install -r requirements.txt -q`

- [ ] **Step 4: Write minimal implementation**

```python
# server/app.py
import asyncio
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import youtube_scraper as ys
import history
import ideas
from server import inputs as inputs_mod
from server.jobs import JobManager
from server.serialize import row_to_api

app = FastAPI(title="Voyara Signal")
MANAGER = JobManager()
DIST = Path(__file__).resolve().parent.parent / "web" / "dist"


class RunBody(BaseModel):
    inputs: str = ""
    per_link: str = "60 videos"
    date_filter: str = "Any time"
    fast: bool = True
    cookies: str | None = None


class PredictBody(BaseModel):
    job_id: str


@app.post("/api/run")
def run(body: RunBody):
    urls = inputs_mod.parse_inputs(body.inputs, body.date_filter)
    if not urls:
        raise HTTPException(400, "No keywords or URLs provided.")
    limit = inputs_mod.per_link_to_int(body.per_link)
    job = MANAGER.create({"fast": body.fast, "urls": urls, "limit": limit})

    def scrape_fn(progress):
        rows = ys.run_scrape(urls, limit=limit, fast=body.fast,
                             channel_info=not body.fast, cookies=body.cookies,
                             progress=progress)
        try:
            history.save_snapshot(rows, ys.COLUMNS, "youtube_results")
        except Exception:
            pass
        return rows

    MANAGER.run_in_thread(job, scrape_fn)
    return {"job_id": job.id}


@app.get("/api/jobs/{job_id}/events")
async def events(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")

    async def gen():
        while True:
            try:
                evt = job.events.get_nowait()
            except Exception:
                if job.status in ("done", "error"):
                    break
                await asyncio.sleep(0.25)
                continue
            import json as _json
            yield f"data: {_json.dumps(evt)}\n\n"
            if evt["type"] in ("done", "error"):
                break

    return StreamingResponse(gen(), media_type="text/event-stream")


@app.get("/api/jobs/{job_id}/results")
def results(job_id: str):
    job = MANAGER.get(job_id)
    if not job:
        raise HTTPException(404, "Unknown job")
    if job.status == "error":
        raise HTTPException(409, job.error or "Job failed")
    if job.status != "done":
        raise HTTPException(409, "Job not finished")
    return {"count": len(job.rows), "fast": job.params.get("fast", False),
            "rows": [row_to_api(r) for r in job.rows]}


@app.get("/api/jobs/{job_id}/download")
def download(job_id: str):
    job = MANAGER.get(job_id)
    if not job or job.status != "done":
        raise HTTPException(404, "No finished job")
    out = Path(f"youtube_results.tsv")
    ys.write_tsv(job.rows, out)
    return FileResponse(out, filename="youtube_results.tsv",
                        media_type="text/tab-separated-values")


@app.post("/api/predict")
def predict(body: PredictBody):
    job = MANAGER.get(body.job_id)
    if not job or job.status != "done":
        raise HTTPException(404, "No finished job to analyse")
    return ideas.generate_prediction(job.rows)


if DIST.exists():
    app.mount("/", StaticFiles(directory=str(DIST), html=True), name="static")
```

- [ ] **Step 5: Run test to verify it passes**

Run: `venv/bin/python -m pytest tests/test_app.py -v`
Expected: PASS

- [ ] **Step 6: Run the whole suite**

Run: `venv/bin/python -m pytest -q`
Expected: all tests pass.

- [ ] **Step 7: Commit**

```bash
git add server/app.py requirements.txt tests/test_app.py
git commit -m "feat: FastAPI routes (run/events/results/download/predict) + static serving"
```

---

## Task 7: Svelte frontend scaffold + API layer

**Files:**
- Create: `web/package.json`, `web/vite.config.js`, `web/index.html`, `web/src/main.js`, `web/src/lib/api.js`, `web/src/lib/store.js`, `web/src/App.svelte`
- Test: build succeeds + dev server proxies API (manual verification step)

**Interfaces:**
- `api.js` produces: `startRun(params) -> {job_id}`, `openEvents(jobId, onEvent)` (EventSource), `getResults(jobId) -> {count,rows,fast}`, `predict(jobId) -> prediction`, `downloadUrl(jobId) -> string`.
- `store.js` produces a Svelte store `state` with `{view, running, urls, perLink, dateFilter, fastMode, rows, sort, keyword, verifiedOnly, query, aiState, ai}` plus the derived `rows()` sorting/filtering logic ported verbatim from the prototype's `list()`/`rows()` (Task 8 consumes it).

- [ ] **Step 1: Scaffold Vite + Svelte**

```bash
cd web && npm create vite@latest . -- --template svelte && npm install
```
Set `vite.config.js` to proxy `/api` to `http://127.0.0.1:8000` and build to `dist/`:

```js
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
export default defineConfig({
  plugins: [svelte()],
  build: { outDir: 'dist' },
  server: { proxy: { '/api': 'http://127.0.0.1:8000' } },
})
```

- [ ] **Step 2: Write `web/src/lib/api.js`**

```js
export async function startRun(params) {
  const r = await fetch('/api/run', { method: 'POST',
    headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(params) })
  if (!r.ok) throw new Error((await r.json()).detail || 'run failed')
  return r.json()
}
export function openEvents(jobId, onEvent) {
  const es = new EventSource(`/api/jobs/${jobId}/events`)
  es.onmessage = (e) => { const evt = JSON.parse(e.data); onEvent(evt); if (evt.type !== 'progress') es.close() }
  es.onerror = () => es.close()
  return es
}
export async function getResults(jobId) {
  const r = await fetch(`/api/jobs/${jobId}/results`); if (!r.ok) throw new Error('results failed'); return r.json()
}
export async function predict(jobId) {
  const r = await fetch('/api/predict', { method: 'POST',
    headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ job_id: jobId }) })
  if (!r.ok) throw new Error('predict failed'); return r.json()
}
export const downloadUrl = (jobId) => `/api/jobs/${jobId}/download`
```

- [ ] **Step 3: Write `web/src/lib/store.js`** (port the prototype's sort/filter)

```js
import { writable, derived } from 'svelte/store'
export const state = writable({
  view: 'hub', running: false, jobId: null, fast: true,
  urls: 'https://www.youtube.com/results?search_query=best+ai+tools\nhow to make money with ai',
  perLink: '60 videos', dateFilter: 'Any time', fastMode: true,
  rows: [], sort: 'breakout', keyword: 'all', verifiedOnly: false, query: '',
  aiState: 'idle', ai: null,
})
const keyFns = {
  breakout: v => v.breakout ?? -1, views: v => v.views ?? 0, likes: v => v.likes ?? 0,
  comments: v => v.comments ?? 0, newest: v => Date.parse(v.upload_date || 0) || 0,
  longest: v => v.duration_sec ?? 0,
}
export const visibleRows = derived(state, ($s) => {
  let r = $s.rows.slice()
  if ($s.keyword !== 'all') r = r.filter(v => v.keyword === $s.keyword)
  if ($s.verifiedOnly) r = r.filter(v => v.verified)
  const q = $s.query.trim().toLowerCase()
  if (q) r = r.filter(v => (`${v.title} ${v.channel}`).toLowerCase().includes(q))
  const k = keyFns[$s.sort] || keyFns.views
  return r.sort((a, b) => k(b) - k(a))
})
```

- [ ] **Step 4: Write `App.svelte`** — nav (from the prototype) + `{#if}` view router delegating to the four screens (Task 8). Background gradient and nav markup copied from `Voyara Signal.dc.html` lines 23-36.

- [ ] **Step 5: Verify it builds**

Run: `cd web && npm run build`
Expected: `web/dist/index.html` produced, no errors.

- [ ] **Step 6: Commit**

```bash
git add web/package.json web/package-lock.json web/vite.config.js web/index.html web/src/main.js web/src/lib web/src/App.svelte
git commit -m "feat: Svelte scaffold + API layer + state store (sort/filter ported)"
```

---

## Task 8: Svelte screens (Hub, Input, Results, AiPrediction)

**Files:**
- Create: `web/src/screens/Hub.svelte`, `Input.svelte`, `Results.svelte`, `AiPrediction.svelte`

**Interfaces:**
- Consumes: `state`/`visibleRows` from `store.js`; `startRun/openEvents/getResults/predict/downloadUrl` from `api.js`.
- Each screen mirrors the matching `<sc-if>` block in `Voyara Signal.dc.html` (Hub = lines 39-79, Input = 82-116, Results = 129-187, AiPrediction = 190-238). Markup/inline styles are copied verbatim from the prototype; `{{ }}` bindings become Svelte expressions; `sc-for` becomes `{#each}`; `sc-if` becomes `{#if}`.

- [ ] **Step 1: `Hub.svelte`** — copy the hub grid; the live "YouTube Content Research" card's button sets `state.view = 'input'`; the other three stay "Coming soon" (non-interactive), exactly as the design.

- [ ] **Step 2: `Input.svelte`** — textarea bound to `urls`; per-link + date-filter selects (date options: Any time / This year / This month / This week per Global Constraints); fast-mode toggle; the live `linkCount × perLink ≈ estTotal` line; "Run research" calls:

```js
async function run() {
  const { job_id } = await startRun({ inputs: $state.urls, per_link: $state.perLink,
    date_filter: $state.dateFilter, fast: $state.fastMode })
  state.update(s => ({ ...s, view: 'results', running: true, jobId: job_id, progress: [] }))
  openEvents(job_id, async (evt) => {
    if (evt.type === 'progress') state.update(s => ({ ...s, progress: [...(s.progress||[]), evt.message] }))
    else if (evt.type === 'done') { const res = await getResults(job_id)
      state.update(s => ({ ...s, running: false, rows: res.rows, fast: res.fast })) }
    else state.update(s => ({ ...s, running: false, error: evt.message }))
  })
}
```

- [ ] **Step 3: `Results.svelte`** — spinner while `running` (show the latest progress line under it); the table from `{#each $visibleRows as v}`; sort chips; keyword select; "Verified only" toggle; search box; "Download TSV" links to `downloadUrl($state.jobId)`. When `$state.fast` is true, render breakout cells as `—`, and disable the Breakout sort chip + Verified-only toggle with a small "needs full mode" note (per spec). Real thumbnails use `v.thumbnail` with the gradient as background fallback.

- [ ] **Step 4: `AiPrediction.svelte`** — on first open call `predict($state.jobId)`; show the spinner state, then the hero prediction + "Why this will work" (`{#each ai.evidence}`) + "More ideas" (`{#each ai.ideas}`) blocks copied from the prototype. "Regenerate" re-calls `predict`. A small note shows when `ai.source === 'fallback'` ("estimate unavailable — showing a sample").

- [ ] **Step 5: Build + commit**

```bash
cd web && npm run build && cd ..
git add web/src/screens
git commit -m "feat: Svelte screens (hub/input/results/ai) matching the prototype design"
```

---

## Task 9: `run.sh web` launcher + README update

**Files:**
- Modify: `run.sh` (add a `web` subcommand), `README.txt` (document it)

**Interfaces:**
- `./run.sh web` → ensures deps, builds the frontend if `web/dist` is missing, launches `uvicorn server.app:app --host 127.0.0.1 --port 8000`, prints the URL.

- [ ] **Step 1: Add the `web` case to `run.sh`** (after the `ideas` case, before the yt-dlp update block)

```bash
    web)
        shift
        if [ ! -d "web/dist" ]; then
            echo "Building the web UI (first run)..."
            ( cd web && npm install && npm run build )
        fi
        echo "Voyara Signal running at http://127.0.0.1:8000  (Ctrl-C to stop)"
        exec "$PY" -m uvicorn server.app:app --host 127.0.0.1 --port 8000
        ;;
```

- [ ] **Step 2: Document in `README.txt`** — add a "WEB APP" section: `./run.sh web`, what it does, the bot-check/cookies note, that it reuses the same scraper + AI.

- [ ] **Step 3: Manual smoke**

Run: `./run.sh web` (with `web/dist` already built), open `http://127.0.0.1:8000`, confirm the Hub renders.

- [ ] **Step 4: Commit**

```bash
git add run.sh README.txt
git commit -m "feat: ./run.sh web launcher + README web-app section"
```

---

## Task 10: End-to-end QA + visual review

**Files:** none (verification task); fixes land in the relevant file from Tasks 1-9.

- [ ] **Step 1: Full backend suite green**

Run: `venv/bin/python -m pytest -q`
Expected: all pass.

- [ ] **Step 2: Live QA** — invoke the `/qa` skill against `http://127.0.0.1:8000`: enter 1-2 keywords, run a **fast** real scrape (seconds), verify the table fills, sort chips reorder, keyword filter + search work, breakout shows `—` in fast mode, Download TSV returns a valid file, AI tab returns a prediction (or labelled fallback). Fix any bug found (use `/investigate` for root cause).

- [ ] **Step 3: Visual fidelity** — invoke `/design-review` comparing the running app to `Voyara Signal.dc.html` (color, spacing, typography, the 4 screens). Fix drift.

- [ ] **Step 4: One full-detail run** — confirm live progress streams (`[i/n] ...` lines) without freezing the UI, then results load with real breakout numbers.

- [ ] **Step 5: Regression** — confirm the CLI is intact: `./run.sh --keywords keywords.txt --fast --limit 3 --no-history` still scrapes and writes TSV.

- [ ] **Step 6: Commit any fixes**

```bash
git add -A
git commit -m "fix: QA + design-review findings for the web app"
```

---

## Self-Review Notes

- **Spec coverage:** Local/FastAPI/background-job/Svelte decisions → Tasks 1-9. Live progress → Tasks 4,6,8. Fast-mode degradation → Tasks 3,8 (`breakout` null + disabled chips). AI JSON shape + fallback → Task 5. Bot-check handling → Task 4 (`BOTCHECK_MSG`) + Task 8 (error display) + Task 9 (cookies/README). Snapshots → Task 6 (`history.save_snapshot`). CLI untouched → Task 1 Step 6 + Task 10 Step 5.
- **Out of scope (per spec):** the three "Coming soon" tools (Hub shows them, inert), the `.xlsx` workbook, hosting/auth.
- **Type consistency:** `run_scrape(...progress=)` signature consistent across Tasks 1/6; `row_to_api` keys consistent across Tasks 3/6/8; prediction `{topic,angle,est,rationale,evidence,ideas,source}` consistent across Tasks 5/8.
</content>
