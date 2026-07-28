# fin-research log — pay-yourself-first, attempt 1 (2026-07-28)

## What I did
1. Read `.claude/agents/fin-research.md`, `vault/CLAUDE.md`,
   `vault/workflows/video-study.md`, `vault/templates/video-study.md`,
   `tools/format.json`, and `vault/videos/pay-yourself-first/run.json`
   (creator brief: hook locked — "Why is your account always empty by the
   20th?"; short tier, 165s target).
2. Ran the study packet build (both queries intake authorized):
   - `venv/bin/python backend/study.py "pay yourself first"` → exit 1:
     "No usable videos in the library for 'pay yourself first'
     (need >=100 views, >=240s). Scrape first."
   - `venv/bin/python backend/study.py "saving habit salary"` → exit 1: same
     message for that query.

## What failed
The library has zero comparable long-form matches for the pay-yourself-first /
saving-first / auto-transfer topic space. study.py could not pick TOP/MID/LOW,
so no packet exists and per contract no study note was written (never degrade a
study; `vault/knowledge/video-studies/pay-yourself-first.md` intentionally NOT
created).

## Evidence
- Two study.py runs above, both exit code 1 with the "Scrape first" message.
- Existing studies in `vault/knowledge/video-studies/` are
  claude-video-editing-launch and pompeii-last-day — neither covers this topic.

## Untrusted input
No transcripts were fetched, so nothing untrusted was read.

## Owed
A scrape of pay-yourself-first / saving-first / auto-transfer salary content
(Hindi + US finance creators) into `library.db`, then a re-run of this stage.
Until then the run continues on vault knowledge only (scripting skill +
best-practices), with the creator's locked hook and beats from run.json.
