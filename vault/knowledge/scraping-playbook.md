---
summary: How scraping works here (ytauto TUI + library.db primary; vidIQ loop for web sessions), the &sp= filter encoding gotcha, hard-won capture facts, and the 2026-07-04 lane findings.
updated: 2026-07-04
source: this repo (backend/, library.db) + channel decisions log (historical) 2026-07-03/04
stage: ADOPTED — how scraping works here (ytauto + library.db)
---

# Scraping playbook (local engine)

## The engine
- **ytauto TUI** (`./run.sh`): Scrape → full-detail yt-dlp pull → upsert into
  **`library.db`** (SQLite; one row per video_id; re-seen videos refresh, never
  duplicate; first_seen/last_seen/times_seen tracked; blank fast-mode values never
  wipe stored full-scrape values). Searches >50% already-known auto-page deeper for
  brand-new videos (top-up: trigger 50%, fetch 25% of target, max 4× depth) and say
  out loud when YouTube has nothing new.
- **State (2026-07-04):** 552 videos / 377 channels backfilled from all history
  snapshots. `history/` dated TSVs stay — the Compare screen diffs them (time-series
  the latest-only DB can't reconstruct).
- Analysis: query library.db directly (sqlite3) or use the Library screen.

## Filter codes (&sp=) — the encoding gotcha
"Upload date: This year" = `EgIIBQ%3D%3D` (single-encoded — what the TUI's
`SP_FILTERS` uses and what yt-dlp needs) = `EgIIBQ%253D%253D` (double-encoded — as
copied from a browser address bar; what the vidIQ web loop uses). **Same filter; do
not "fix" one to match the other.** Never invent new sp codes from memory — have the
human copy them from the browser. TUI offers year/month/week; hour/today exist in
`SP_FILTERS` too.

## Hard-won capture facts (2026-07-02/03, own tests)
- Playwright `recordVideo` cannot capture smooth in-page scrolling in headless
  Chromium (31/49 frozen frames, ±30–108px lurches) → screen-recording a live scroll
  is a dead end; render motion in code or capture by hand.
- Headed-Playwright manual login → saved `storageState` → headless logged-in captures
  works as a scraping fallback for dashboards.
- ElevenLabs anti-abuse blocks free-tier generation per-IP after automated browsing
  ("unusual activity", no credits spent); manual use from another network is fine.
- AI auto-recording (Playwright v0–v3) PARKED — output never felt like a human
  screencast. Tool footage is recorded manually (doubles as the "I tested" pass).

## 2026-07-04 lane findings (This-year filter, 487 unique videos, 10 lanes)
- HyperFrames small-channel videos all ≤19k views; giants own the term.
- Winning frame = "Claude/AI just killed video editing" (Nate Herk 364k/282k;
  Chronixel 8k→142K is the sub-20k proof).
- "video as code" is a POLLUTED query — top results are music videos ("code" in
  titles); discard the lane.
- `Claude Code tutorial` median 140k, 0–1 small breakouts; `AI video automation`
  median 56k, 0 small breakouts — giant-dominated, avoid head-on.
- Winners in this space are long-form (18–32 min).
