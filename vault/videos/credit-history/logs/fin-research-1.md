# fin-research log — credit-history, attempt 1 (2026-07-29)

## What I did
1. Read `vault/CLAUDE.md`, `vault/workflows/video-study.md`,
   `vault/templates/video-study.md`, `tools/format.json` (short tier: 165s
   target, blockframe-9, 9 lines) and `vault/videos/credit-history/run.json`
   (creator brief: hook "An invisible record decides whether you get a loan.";
   beats = what credit history is / what builds it / what destroys it / why it
   matters before you need it; hero example = one missed payment stays visible
   for years; CIBIL for hi, FICO for en).
2. Built the study packet — both queries in the topic space:
   - `venv/bin/python backend/study.py "credit history"` → non-zero:
     `No usable videos in the library for 'credit history' (need >=100 views,
     >=240s). Scrape first.`
   - `venv/bin/python backend/study.py "credit score"` → non-zero, same message.
   No third query; no packet was produced, so nothing was downloaded, no
   transcript and no keyframe exists to analyze.

## What failed
`library.db` holds no comparable long-form video on credit history / credit
score, so study.py could not pick TOP/MID/LOW. Per contract a study of
thumbnails or of the manifest alone is not a study — therefore
`vault/knowledge/video-studies/credit-history.md` was deliberately NOT written.
No hook type, beat map or low-performer autopsy is reported: none of the three
can be derived without transcripts, and inventing them would put a fabricated
fact in the vault's one home for study evidence.

## Evidence
- Two study.py runs above, both exiting non-zero with the "Scrape first" message.
- `library.db` mtime is 2026-07-07 — it predates the finance pivot (2026-07-18)
  entirely. `vault/knowledge/scraping-playbook.md` records its actual contents:
  552 videos / 377 channels from the 2026-07-04 AI-tools/HyperFrames lane sweep.
  There is no finance lane in it at all, which is why every finance topic
  (pay-yourself-first on 2026-07-28, credit-history today) fails at this stage.
- `vault/knowledge/video-studies/` contains only claude-video-editing-launch and
  pompeii-last-day — neither is finance.

## Untrusted input
None read. No transcript, title or description was fetched, so there was no
attacker-controllable text in this run.

## What the run falls back on (vault knowledge, no fabrication)
Scripting/packaging stages should lean on already-earned evidence rather than a
missing study:
- `vault/knowledge/best-practices.md` → US personal-finance title formula
  (specific number + time bound + objection-killer; plain-label penalty), the
  split-the-demand-between-cuts rule, and the title-research method
  (autocomplete + `youtube_scraper.build_search_url` / `scrape_url`).
- `vault/videos/emergency-fund/youtube-metadata-en.md` — the closest real
  competitor board we own in this niche.
- `vault/knowledge/niches/india-finance-market.md`,
  `vault/knowledge/niches/us-market-2026.md`,
  `vault/knowledge/design-finance-blockframe.md`.

## Owed
A scrape into `library.db` before this stage can succeed for any finance topic.
Suggested lanes (last-12-months filter, both markets, long-form ≥240s):
`credit score explained`, `how to build credit`, `credit report`,
`CIBIL score kaise badhaye`, `credit card late payment`. Re-run
`backend/study.py "credit history"` afterwards; two of three picks need
captions or the stage fails again.
