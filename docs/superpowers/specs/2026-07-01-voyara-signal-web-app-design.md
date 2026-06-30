# Voyara Signal — Web App Integration Design

**Date:** 2026-07-01
**Status:** Approved (design), pending implementation plan

## Goal

Turn the `Voyara Signal.dc.html` Claude design prototype into a real, runnable
web app backed by the existing Python YouTube content-research system. The app
lets a user paste YouTube search URLs/keywords, run a real scrape with live
progress, browse/sort/filter the results, get an AI "next video" prediction,
and download the data as TSV — matching the prototype's exact look and 4-screen
flow (Hub → Input → Results → AI Prediction).

## Why the prototype can't be used as-is

`Voyara Signal.dc.html` is a Claude "design component": it uses a proprietary
runtime (`x-dc`, `DCLogic`, `sc-if`, `sc-for`, `{{ }}` bindings) loaded from a
`support.js` file that is not present, runs on baked-in mock data, and calls
`window.claude.complete` for AI. It only renders inside Claude's design canvas.
It must be re-implemented as a standard web app while preserving its design.

## Decisions (approved)

| Decision | Choice | Reason |
|---|---|---|
| Deployment | **Local tool** (`localhost`, single user) | Scraper uses local `yt-dlp`, reads local browser cookies for bot-checks, and AI uses the local Claude subscription — none of which work on a public server. |
| Backend framework | **FastAPI** | Async, native background jobs + SSE progress streaming, reuses existing Python modules directly. |
| Run handling | **Background job + live progress (SSE)** | Full-detail scrapes take 15–30 min; UI must not freeze. Matches the prototype's loading screen. |
| Frontend | **Svelte** (Vite build → static files) | Maps cleanly onto the prototype's state-driven `{{ }}`/`sc-if`/`sc-for` structure; room to grow into the full multi-tool toolkit. |

## Architecture

```
Svelte frontend (browser)  ──HTTP/SSE──►  FastAPI backend (Python)
  Hub / Input / Results /                   - serves built UI (static)
  AI Prediction screens                     - /api endpoints
  (exact prototype design)                  - background scrape jobs
                                            - calls existing modules:
                                              youtube_scraper / history /
                                              analyze / ideas
```

**Core principle:** do NOT rewrite scraping or AI logic. The backend *calls*
the existing modules. Only a thin web layer is added, plus surgical refactors so
those modules can be invoked as functions (today they print to a terminal and
`sys.exit` on error).

### Project structure (new in **bold**)

```
YoutubeScraper/
├── youtube_scraper.py   (light refactor: callable run() + progress hook)
├── history.py           (reused as-is)
├── analyze.py           (reused as-is)
├── ideas.py             (ADD: structured-JSON prediction function)
├── server/              ← NEW backend
│   ├── app.py           FastAPI app + routes + static serving
│   ├── jobs.py          background scrape job manager + progress events
│   └── predict.py       AI prediction → JSON wrapper
└── web/                 ← NEW Svelte frontend (Vite)
    ├── src/
    │   ├── App.svelte           view router (hub/input/results/ai)
    │   ├── lib/api.js           fetch + SSE helpers
    │   └── screens/             Hub, Input, Results, AiPrediction
    └── (npm build → web/dist/, served by FastAPI)
```

## API endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/run` | Start a scrape job. Body: `{ inputs: string[], per_link: int, date_filter: str, fast: bool, cookies: str\|null }`. Returns `{ job_id }`. |
| `GET`  | `/api/jobs/{id}/events` | SSE stream of progress lines + terminal `done`/`error` event. |
| `GET`  | `/api/jobs/{id}/results` | Scraped videos as JSON array (see Data shape). |
| `GET`  | `/api/jobs/{id}/download` | The run's `.tsv` file (existing scraper format). |
| `POST` | `/api/predict` | Body: `{ job_id }` (or rows). Returns the prediction JSON. |
| `GET`  | `/api/history/diff` | (Foundation for future Trend Tracker; optional in v1.) Diff of two latest snapshots. |

### Run flow

1. `POST /api/run` → backend parses inputs (URLs pass through; plain keywords →
   `build_search_url` with the chosen date filter), starts a background thread,
   returns `job_id` immediately. UI shows spinner.
2. Frontend opens SSE on `/api/jobs/{id}/events`; backend pushes per-keyword
   progress (`[i/n] keyword … N videos`) and channel-lookup progress, then a
   terminal event.
3. On `done`, frontend fetches `/api/jobs/{id}/results`; Results screen does
   sorting/filtering/breakout math client-side (as the prototype already does).
4. Download button hits `/api/jobs/{id}/download`.
5. AI tab calls `/api/predict`.
6. Every run also writes a dated snapshot via `history.save_snapshot` (already
   wired into the scraper) — foundation for the future Trend Tracker tool.

## Data shape (results JSON, per video)

Derived directly from the scraper's existing columns:

```
video_id, title, video_url, thumbnail, upload_date,
duration, duration_sec, keyword,
channel, channel_url, subscribers, channel_verified (Yes/No/""),
views, likes, comments,
breakout  (computed = views / subscribers, null when subs missing)
```

The frontend Results table columns (Video, Channel, Views, Likes, Breakout,
Len) and the AI digest both consume this shape. `breakout` mirrors
`analyze.views_per_sub`.

## AI prediction

Add **one function** to `ideas.py` (reusing its existing `claude-agent-sdk`
plumbing + subscription auth) that:

1. Builds a compact digest from the *real* scraped rows, reusing
   `analyze.score_rows` / breakout / `pattern_stats` so the model cites real
   numbers.
2. Prompts Claude to return ONLY minified JSON in the shape the design expects:
   `{ topic, angle, est_breakout, rationale, evidence[3-4], ideas[4]{title,est} }`.
3. Parses it defensively (extract first `{`…last `}`, `json.loads`, validate
   required keys).

Failure handling: if parsing fails, the CLI isn't logged in, or the SDK errors,
the backend returns a structured error; the frontend renders the design's
built-in fallback prediction so the screen never appears broken. The existing
`./run.sh ideas` Markdown report path is untouched — this is an *added* mode.

## Fast-mode degradation (explicit behavior)

In `--fast` mode the scraper skips per-video/per-channel lookups, so
`subscribers`, `likes`, `comments`, and `channel_verified` come back blank.
Therefore:

- `breakout` (views ÷ subs) cannot be computed → display `—`.
- The "Breakout" sort chip and "Verified only" filter are **disabled** with a
  small inline note ("needs full mode") rather than producing wrong values.
- Default sort falls back to "Most views" when breakout is unavailable.

## Error handling

- **YouTube bot-check** ("Sign in to confirm you're not a robot"): surface a
  cookies setting in the Input screen (`chrome`/`firefox`/`edge`/`brave`), passed
  through to the scraper's existing `--cookies` path. On a 0-video / bot-check
  result, show a clear actionable error, not a silent empty table.
- **Module errors:** the existing modules call `sys.exit` on failure; the
  refactor wraps the callable paths to raise exceptions instead, which the job
  manager captures and emits as an `error` SSE event with a readable message.
- **AI errors:** see AI section (structured error → frontend fallback).

## Refactor required in existing code (minimal, surgical)

`youtube_scraper.py`: extract the scrape loop from `main()` into a callable like
`run_scrape(urls, limit, fast, channel_info, cookies, progress_cb) -> rows` that
returns rows and reports progress via `progress_cb` instead of only `print`.
`main()` keeps working by calling it with a print-based callback (CLI behavior
unchanged). No change to `scrape_url`, `enrich_with_channel_info`, `write_tsv`.

## Testing & QA

- **TDD for pure logic:** job manager / progress events, fast-mode blank-field
  handling, breakout computation, AI-response JSON parsing & validation, input
  parsing (URL vs keyword, date filter mapping). Tests first, then code.
- **Not unit-tested** (external/slow): live YouTube extraction and live Claude
  calls — verified during QA instead.
- **`/qa`:** drive the real app headless — enter keywords, run a small fast real
  scrape, verify sort/filter/download and the AI tab; fix bugs found.
- **`/design-review`:** compare built Svelte UI vs `Voyara Signal.dc.html` for
  visual fidelity (color, spacing, typography, the exact look).
- **`/investigate`:** systematic root-cause debugging for any failures.

## Out of scope (v1)

- Hosting / multi-user / auth / API-key billing.
- The "Coming soon" tools (Title & Thumbnail Tester, Channel Audit, Trend
  Tracker) — the Hub will show them as in the design, but only YouTube Content
  Research is wired up. Architecture leaves room to add them as Svelte screens +
  endpoints later.
- The Excel analysis workbook (`analyze.py`'s `.xlsx` output) — remains a CLI
  feature; not surfaced in the web UI in v1.

## Success criteria

1. `localhost` app renders the 4-screen flow matching the prototype design.
2. A real run (small keyword set, fast mode) scrapes via the existing code and
   shows real results in the table with working sort/filter.
3. A full-detail run streams live progress and never freezes the UI.
4. TSV download produces the existing scraper file format.
5. AI tab returns a real, data-grounded prediction (or graceful fallback).
6. Existing CLI (`./run.sh`, `./run.sh ideas`, `./run.sh diff`) still works.
</content>
</invoke>
