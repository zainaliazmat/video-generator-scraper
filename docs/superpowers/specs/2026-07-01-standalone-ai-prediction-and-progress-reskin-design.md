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
  back link + title "AI Prediction"), containing:
  - A **drag-and-drop zone**: "Drop a `.tsv` here, or click to browse." Clicking
    opens a native file picker. Dropping/selecting a file shows its name and
    marks it as the chosen source.
  - **"Or pick from history"**: a list built from `GET /api/history`. Each item
    shows the snapshot date, video count, and keyword list, and is selectable
    (single selection). Selecting a history item clears any dropped file and
    vice-versa — exactly one source is active.
  - A primary **Predict** button, enabled only when a source (dropped file OR
    history item) is selected.
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
- **Time left** estimate and **Channels / Videos** counters.
- **Cancel run** button (existing behaviour).

### Data wiring — no fabricated numbers

- Drive the stepper and counters from the existing `$state.progress` lines and
  the `runProgress` derived store (`pct`, `phase`). Extend `runProgress` (or add a
  sibling derived store) to also expose: current phase index, videos-scraped and
  channels-looked-up counts (parsed from the `[i/n]` progress markers), and a
  crude **time-left** estimate from elapsed time vs. `pct`.
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
3. The old chained AI-prediction tab is **removed entirely** (not kept
   alongside the new tool).
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

## Out of scope

- Any actual video transcript/subtitle/"script" extraction.
- Changes to the scraper, `ideas.py` prediction model, or `analyze.py` scoring.
- Persisting predictions or a prediction history.
