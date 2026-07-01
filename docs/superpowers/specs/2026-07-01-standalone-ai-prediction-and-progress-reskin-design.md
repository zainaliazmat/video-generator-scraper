# Standalone AI Prediction tool + scrape-progress re-skin

Date: 2026-07-01
Status: Approved (ready for implementation plan)

## Summary

Two independent changes to the Voyara Signal web app:

1. **Make AI prediction its own tool.** Today prediction is chained to a
   just-finished scrape job. Move it out into a standalone tool where the user
   feeds it a TSV — by drag-and-drop **or** by picking a saved snapshot from
   history — and clicks **Predict**. Remove the in-results AI tab entirely.

2. **Re-skin the scrape "in progress" screen** to match the provided template
   `Run progress (1).html`. Pure visual/structural rework of the existing
   progress UI; no new scraping capability. (This is NOT a video
   transcript/script extractor — the word "script extraction" refers to the
   scraping run itself.)

The two parts share no state and can be built and reviewed independently.

## Part 1 — Standalone AI Prediction tool

### User-facing flow

- The Hub home page gains a **second "Live" card: "AI Prediction"** (it replaces
  one of the three "Coming soon" placeholder cards so the 2-column grid stays
  tidy).
- Opening it shows a single screen with its own lightweight header ("All tools"
  back link + title "AI Prediction"). Layout (autoplan D2): **history is the
  primary column**, drag-drop is the smaller secondary affordance beside/below it —
  this app makes its own TSVs, so picking a saved snapshot is the common path.
  - **Pick from history** (primary): a list built from `GET /api/history`. Each
    item shows the snapshot date, video count, and keyword list (long keyword
    lists truncated, A15), and is selectable (single selection). Empty state when
    there are no snapshots yet: "No snapshots yet — run Content Research or drop a
    TSV" (A10). Loading + fetch-error (retry) states specified (A10).
  - **Drag-and-drop zone** (secondary): "or upload a `.tsv`." Clicking opens a
    native file picker. Client-side rejection (wrong extension, unparseable,
    >10 MB) shown inline before Predict is enabled (A11).
  - The active source (dropped file OR selected snapshot) is shown as a single
    removable **chip** above Predict, so "exactly one source" is visible, not just
    modeled — selecting elsewhere visibly swaps the chip (A12).
  - A primary **Predict** button, enabled only when a source is selected. When
    the tool is opened via the Results "Predict next video" deep-link, that run's
    snapshot arrives preselected (D1).
- On **Predict**: call `POST /api/predict` to obtain a `job_id`, then reuse the
  existing `watchPredict(job_id)` streaming path. The screen then renders the
  same three states already used today: live "Claude session" log (loading),
  error card (with the existing reason codes), and the final prediction result
  card. A **Regenerate** action re-runs prediction on the same source.

### Backend

Reuse the existing `Job` + prediction streaming machinery. Two new endpoints in
`backend/server/app.py`:

- `GET /api/history`
  - Lists `*.tsv` files in `history/`, **excluding** `diff_*.tsv` (those are diff
    reports, not video tables). Newest first (by date in filename, falling back
    to mtime).
  - For each file, parse with `analyze.load_rows` and return:
    `{ file, date, count, keywords }` where `keywords` is the sorted unique set
    and `count` is the row count. Files that fail to parse are skipped (logged,
    not fatal).
  - Includes both web (`web_youtube_results_*`) and CLI (`youtube_results_*`)
    snapshots — all snapshots, per decision below.

- `POST /api/predict`
  - Accepts **one** of two sources:
    - a multipart file upload (the dropped/browsed `.tsv`), or
    - JSON/body field `history=<filename>` naming a file in `history/`.
  - Validation:
    - History filename must resolve to a real file inside `history/` (reject path
      traversal — basename only, must exist in the dir).
    - Uploaded content is decoded as UTF-8 (BOM-tolerant, matching
      `utf-8-sig` used elsewhere) and size-capped (e.g. 10 MB) to avoid abuse.
    - Parse rows via `analyze.load_rows` (upload written to a temp path, or parse
      the decoded text through the same `csv.DictReader(delimiter="\t")` logic).
    - **Breakout guard:** if no row has a usable `subscribers` value, respond
      `422` with reason `no_breakout_data` and a message matching the existing
      Fast-mode copy ("AI prediction needs Full-mode data …"). The frontend shows
      this instead of starting a prediction.
  - On success: `MANAGER.create({...})`, set `job.rows = parsed_rows`,
    `job.status = "done"`, and return `{ "job_id": job.id }`. This synthetic job
    is not gated by the scrape `_running` lock (only real scrapes set it), so it
    never conflicts with a live scrape.
  - The existing `POST /api/jobs/{job_id}/predict-start` and
    `GET /api/jobs/{job_id}/predict-events` then work unchanged, because they only
    read `job.rows` and stream — they don't care how the rows arrived.

No changes required to `ideas.py` / `analyze.py`: `build_digest` →
`analyze.score_rows` already tolerate string-typed TSV rows (that is how the
CLI's `ideas.run(data_path=...)` already works).

### Frontend

- **New screen** `frontend/src/screens/Predict.svelte`:
  - Owns the drop zone + history list + Predict button.
  - Reuses the loading / error / result markup currently in `AiPrediction.svelte`
    (moved into this screen). The result card, reason-code table, and Regenerate
    button are carried over verbatim.
- **Hub** (`Hub.svelte`): add the "AI Prediction" live card; wire its button to
  open the new view.
- **Routing** (`App.svelte`): add a `predict` view that renders `Predict.svelte`.
  Remove the old chained `ai` view wiring.
- **Remove old tab** (`ToolHeader.svelte`): drop the "AI prediction" chip and its
  `goAi` handler. Scrape results show only Results + Download.
- **Delete** `AiPrediction.svelte` once its markup is reused in `Predict.svelte`.
- **Store** (`store.js`): keep the existing `aiState` / `ai` / `predictLog` /
  `jobId` fields (reused). Add `predict`-tool UI state: `history` (list),
  `source` (`{kind:'file'|'history', ...}` or null), and the new default `view`
  option `predict`. The `ai` view enum value is removed.
- **API** (`api.js`): add `getHistory()` and `startPredict(source)` helpers.
  `watchPredict` is unchanged and reused.

## Part 2 — Scrape progress screen re-skin

### Scope

Rebuild the `$state.running` block currently inside
`frontend/src/screens/Results.svelte` (lines ~27-50) to match the layout of
`Run progress (1).html`:

- A **phase stepper**: Searched keywords → Pulled videos → Looking up channels
  (subs + topics) → Score breakout multipliers, with the active/done state driven
  by the real progress stream.
- The **Live feed** panel (the existing streamed terminal log, restyled).
- **Elapsed time** (always shown) and **Channels / Videos** counters. A
  **"time left"** estimate is shown **only after the first phase completes** and
  after a smoothed sample; before that (and if it still reads jittery) show
  elapsed only — never a fake early number (autoplan D3).
- **Cancel run** button (existing behaviour).

### Data wiring — no fabricated numbers

- Drive the stepper and counters from the existing `$state.progress` lines and
  the `runProgress` derived store (`pct`, `phase`). Extend `runProgress` (or add a
  sibling derived store) to expose: current phase index, videos-scraped and
  channels-looked-up counts, and the smoothed time-left (per D3).
- **Stepper state machine must be specified explicitly (A13):** the 4 steps
  (Searched keywords → Pulled videos → Looking up channels → Score breakout) are
  advanced by *named* log-line patterns, not a bare `[i/n]` count. The `[i/n]`
  marker is ambiguous between the video-pull and channel-lookup phases (see
  `store.js` `runProgress` today), so the Videos vs Channels counters must each
  read the specific line text for their phase, not any `[i/n]`. The plan lists the
  exact patterns per step/counter.
- Where the template shows a value we genuinely do not have, compute it from the
  progress lines if possible; otherwise omit that element rather than show a fake
  number.

### Refactor

Extract this progress UI out of `Results.svelte` into a new
`frontend/src/screens/RunProgress.svelte` component, rendered by `Results.svelte`
while `$state.running`. `Results.svelte` is already large; this keeps each screen
focused on one responsibility.

## Decisions

1. The new AI Prediction Hub card **replaces one "Coming soon" placeholder**
   (keeps the grid tidy) rather than adding a fifth card.
2. The history list shows **all** `.tsv` snapshots in `history/` (web + CLI),
   excluding `diff_*` reports.
3. The old chained AI-prediction **tab** is removed, but the Results screen keeps
   a single **"Predict next video"** button that deep-links into the new standalone
   tool with *this run's snapshot preselected* as the source (autoplan D1). The
   duplicate in-results tab is gone; the one-click path to predict on the run you
   just made stays.
4. Template `Run progress (1).html` re-skins the **existing scrape progress
   screen** — it is not a new transcript/script-extraction feature.

## Testing

- **Backend (pytest):**
  - `GET /api/history`: lists snapshots newest-first, excludes `diff_*`, returns
    count + keywords, skips unparseable files.
  - `POST /api/predict`: upload path creates a done job with parsed rows; history
    path resolves and parses; path-traversal filename rejected; a subscriber-less
    (Fast-mode) TSV returns `422 no_breakout_data`.
- **Manual:**
  - Drop a full-mode TSV → Predict → streaming log → result card → Regenerate.
  - Pick a history snapshot → Predict.
  - Drop a Fast-mode TSV → see the no-breakout message.
  - Run a real scrape and watch the re-skinned progress screen; verify Cancel.

## GSTACK REVIEW REPORT (/autoplan)

Ran 2026-07-01. Voices: **subagent-only** — Codex unavailable in this
environment (bubblewrap `RTM_NEWADDR` blocked; it could not read the repo).
Three independent Claude reviewers (CEO / Design / Eng), no shared context.

### Consensus (CEO + Design + Eng)

| Dimension | Verdict | Note |
|---|---|---|
| Right problem? | PARTIAL | Re-predicting past runs is real; making it a *separate* tool that drops the inline flow is the contested part. |
| Premises valid? | PARTIAL | Drag-drop-a-foreign-TSV is unproven for a single-user app that makes its own TSVs; keep it (user asked) but history should lead. |
| Scope calibrated? | PARTIAL | Backend precise; progress-reskin state machine + time-left under-specified. |
| Architecture sound? | YES (7/10) | Synthetic `status="done"` Job reuse is lock-safe and works; eviction + relative `HISTORY_DIR` are the real risks. |
| Error/edge paths | NO (4/10) | Several concrete gaps, folded in below. |

### One User Challenge (NOT auto-decided — see gate)

Both CEO and Design independently judged that **removing the inline
"predict right after a scrape" path (decision #3 / your 2B) is a regression**
for the 90% flow. Surfaced to the user at the approval gate.

**Gate outcome (user chose A — approve all):** D1 adopted (Results keeps a
"Predict next video" deep-link button), D2 adopted (history primary, drag-drop
secondary), D3 adopted (elapsed always; time-left only after phase 1, smoothed).
All three are now reflected in the Decisions + Part 1/Part 2 sections above.

### Auto-decided spec hardening (folded into this spec; principle in brackets)

Engineering (from the Eng reviewer, all confirmed against code):
- **A1 [P1]** Add `python-multipart` to `backend/requirements.txt` (used by
  `UploadFile`/`Form`; currently only transitively present). *high*
- **A2 [P5]** `history.HISTORY_DIR` is `"history"` **relative to cwd**. Anchor
  it absolutely (resolve under `PROJECT`, matching `WEB_RUNS`) in the new
  endpoints so `/api/history` and `/api/predict` read the right dir regardless
  of where the server started. Path check: basename-only, must `realpath` under
  the resolved history dir, must end `.tsv`. *high*
- **A3 [P2]** Synthetic predict jobs must not be evicted mid-stream
  (`max_jobs=10` eviction in `jobs.py:55`). Exclude predict jobs from eviction
  (or bump the cap) **and** give `watchPredict` the same terminal safety-net
  poll `watchJob` has (`api.js` — today its `EventSource` retries forever if the
  job is gone). *high*
- **A4 [P5]** Breakout guard keys off **value truthiness** of `subscribers`
  (`_int(r.get("subscribers"))`), matching `serialize.row_to_api` breakout math
  (`views/subs`, subs>0) — not mere column presence. Fast-mode CLI snapshots
  (`youtube_results_*`) carry an empty `subscribers` column and must fail the
  guard. *medium*
- **A5 [P5]** Distinct reason codes: `empty`, `bad_format`, `bad_columns`,
  `too_large` (413), `no_breakout_data` — don't collapse them all into one. *low/med*
- **A6 [P5]** Synthetic job gets `params={"fast": False, "date": <parsed>,
  "predict": True}`; do **not** `rememberJob()` a predict job id (keeps the
  `lastJob()` reconnect from routing a refreshed predict session to Results). *med*
- **A7 [P5]** History sort parses the trailing `_YYYY-MM-DD` from the filename
  (lexical sort mis-orders across the `web_youtube_results_` vs CLI
  `youtube_results_` prefixes). *medium*
- **A8 [P3]** History listing reads header + row count rather than full
  `load_rows` per file where practical (cheap now; `history/` is unpruned and
  grows). *low — may defer.*
- **A9 [P1]** App shell: add `predict` to the nav/`inTool` handling in
  `App.svelte`; sweep the `ai` view enum from `store.js`/`ToolHeader`. *medium*

Design (from the Design reviewer):
- **A10 [P1]** Specify the **empty-history** state ("No snapshots yet — run
  Content Research or drop a TSV"), and **history loading / fetch-error** states.
- **A11 [P1]** Client-side drop-zone rejection (wrong extension, unparseable,
  >10 MB) shown inline **before** Predict is enabled, mapped to A5's reason codes.
- **A12 [P5]** Surface the active source as a single removable **chip** above
  Predict so "exactly one source" is visible, not just modeled.
- **A13 [P5]** Define the **progress stepper state machine** explicitly: the
  exact log-line patterns that advance each of the 4 steps and that feed the
  Channels/Videos counters (today `runProgress` only distinguishes 2 phases and
  the `[i/n]` marker is ambiguous between video-pull and channel-lookup).
- **A14 [P5]** Regenerate reuses the existing `job_id` (rows already held on the
  synthetic job) — it does **not** re-upload.
- **A15 [P5]** Truncate long keyword lists in history rows.

### Deferred (not in scope now)

- History item delete/rename; per-item "no breakout data" badge; pruning
  `history/`; full-file-read caching for `/api/history` (A8); predict-session
  restore across a browser refresh (F11 reconnect). Logged, low value now.

## Decision Audit Trail

| # | Phase | Decision | Class | Principle | Rationale |
|---|-------|----------|-------|-----------|-----------|
| 1 | CEO | Keep drag-drop (user asked) but make history the primary column | Taste | P6 | User explicitly requested drag-drop; reviewers want history-first layout — both satisfiable. → GATE D2 |
| 2 | CEO/Design | Inline predict removal (2B) is a regression | **User Challenge** | — | Never auto-decided → GATE D1 |
| 3 | Design | time-left counter honesty | Taste | P5 | Fake early estimate erodes trust → GATE D3 |
| 4 | Eng | A1–A9 hardening folded into spec | Mechanical | P1/P5/P2 | Confirmed against code; one right answer each |
| 5 | Design | A10–A15 spec-explicitness folded in | Mechanical | P1/P5 | Missing states/definitions; completeness |

## Out of scope

- Any actual video transcript/subtitle/"script" extraction.
- Changes to the scraper, `ideas.py` prediction model, or `analyze.py` scoring.
- Persisting predictions or a prediction history.
