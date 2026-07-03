# ytauto — Terminal UI for the YouTube scraper

**Date:** 2026-07-04
**Status:** Approved (verbal), building v1

## Goal

Replace the web UI (Svelte + FastAPI) with a single Python **terminal app** so the
project stops being a website and becomes a launcher you drive from the keyboard.

The point is **not** aesthetics. It is: *stop memorizing commands.* Today you must
remember `./run.sh`, `./run.sh ideas`, `./run.sh diff`, and hand-edit `urls.txt`.
Instead:

> Type `ytauto` → a menu appears → arrow to the task → answer a few prompts →
> hit Generate → watch it run. Like launching `claude` in a terminal.

## Non-goals (v1)

No themes, no ASCII-art banner, no `/slash` commands, no "secret" easter eggs, no
mouse-required interactions. Simplest thing that guides you through the real work.

## Why this is *simpler*, not more complex

The scraper already has a complete CLI (`youtube_scraper.py:main`). The web layer
(~984 lines of Svelte + FastAPI/uvicorn/SSE/JobManager) exists **only** because a
browser cannot call Python directly. A TUI calls the backend functions **in the
same process** — no HTTP, no SSE, no Node build. We delete the web stack and add
**one** dependency (`textual`).

## Architecture

```
ytauto (launcher: `ytauto` shell command / `./run.sh` no-arg)
        │
        ▼
backend/tui/            ← new, Textual app (the only front end)
  app.py                YtAutoApp + MenuScreen (arrow-key task picker)
  scrape_screen.py      URL/keyword form → live-progress run
  predict_screen.py     pick source (last scrape or a snapshot) → streaming AI
  diff_screen.py        pick two snapshots → run diff → show result
  inputs.py             parse_inputs / per_link_to_int (moved out of server/)
  ytauto.tcss           styling
        │  calls in-process, no network
        ▼
backend/  youtube_scraper.py · ideas.py · history.py   ← unchanged core
```

### Screen flow

1. **MenuScreen** — an `OptionList`: *Scrape YouTube · Predict content ideas ·
   Compare snapshots · Quit*. ↑/↓ to move, Enter to select. This is the landing
   screen and the "home" every task returns to.

2. **ScrapeScreen** — a form:
   - `TextArea` to paste URLs **or** plain keywords (one per line) — replaces
     editing `urls.txt`.
   - Date filter: Any time / This year / This month / This week (`Select`).
   - Videos per link: 30 / 60 / 120 (`Select`).
   - Fast mode: on/off (`Switch`) — off = richer per-video detail (slower).
   - **Generate** button → runs the scrape.

3. **RunScreen** (shared progress view) — a `RichLog` that fills live from the
   scraper's `progress(str)` callback while it runs in a **background thread**
   (`@work(thread=True)`, UI updated via `call_from_thread`). On completion:
   summary line (N videos), saves a TSV + history snapshot, and offers
   *[P]redict on this · [M]enu*.

4. **PredictScreen** — choose the source: the rows from the last scrape (if any)
   or a saved snapshot from `history/`. Runs `ideas.generate_prediction(rows,
   on_text=…)`; the streamed text fills a `RichLog`; the final normalized
   prediction is shown. Handles the `{ok:false, reason}` path (e.g. no API key)
   with a plain message.

5. **DiffScreen** — pick two snapshots (defaults to the two most recent); run
   `history.diff(old, new)`; show where the diff TSV was written + a short
   summary.

### Concurrency

One task at a time (matches the scraper's "one scrape at a time" constraint).
Long work runs in a Textual thread worker; the UI thread only renders. A running
task can be cancelled (Esc / a Cancel binding) via the scraper's existing
`should_cancel` hook.

### Data / outputs

Unchanged from the CLI: scrapes write `youtube_results.tsv` and a timestamped
`history/…tsv` snapshot via `history.save_snapshot`. No `web_runs/`, no per-job
files.

## What gets deleted

- `frontend/` (entire Svelte app + `dist/`)
- `backend/server/app.py`, `jobs.py`, `serialize.py`, `__init__.py`
- Web-only tests: `test_app.py`, `test_predict_endpoint.py`, `test_jobs.py`,
  `test_serialize.py`
- Web deps from `requirements.txt`: fastapi, uvicorn, sse-starlette,
  python-multipart, httpx
- `run.sh web` subcommand; `web_runs/`

Reusable logic in `server/inputs.py` and `server/tsv_sources.py` is **moved** into
`backend/tui/` (not deleted); their tests move with them.

## Launching

- `ytauto` — a thin executable on PATH (installed by `run.sh`, or run directly)
  that activates the venv and runs `python -m tui`.
- `./run.sh` with no args launches the TUI (the new default). Scrape/ideas/diff
  remain reachable as CLI subcommands for scripting.

## Testing

- Keep the pure-logic tests (`test_inputs`, `test_run_scrape`, `test_predict`,
  `test_tsv_sources`) passing after the move.
- Textual apps are testable headlessly via `App.run_test()` + `Pilot`; add a
  smoke test that boots the app, opens each screen, and quits — no network.

## Success criteria

Type `ytauto`, arrow to **Scrape YouTube**, paste a URL, pick options, hit
Generate, watch live progress, get a TSV — without touching `urls.txt` or
remembering a single flag.
