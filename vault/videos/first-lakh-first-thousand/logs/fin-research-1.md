# fin-research log — first-lakh-first-thousand, attempt 1 (2026-07-31)

## What I did
1. Read `vault/CLAUDE.md`, `vault/workflows/video-study.md`,
   `vault/templates/video-study.md`, `tools/format.json` (MEDIUM tier: 510s
   target, ~78 lines; `architecture_lock: blockframe-9` but this run's
   `run.json` carries a creator override to `swiss-band`) and
   `vault/videos/first-lakh-first-thousand/run.json` (creator brief: hook "The
   first one lakh is the hardest one you will ever save."; beats = 100%-savings-
   rate milestone → crossover point → rate beats returns early → automate/raise/
   don't touch → realistic timeline; hero math = months-to-first-lakh vs
   months-to-second-lakh; en rewrite = $10,000, not a currency conversion).
2. Picked the query from the evidence note the run cites,
   `vault/knowledge/niches/finance-topics-2026-07-31.md` — the 1,881-video
   scrape landed today, so the `1 lakh` keyword lane is the pool with the topic's
   proven breakout in it (226,845 views @ 48x subs, 21:50, `Story of Success`).
   `library.search` is a substring LIKE over title/channel/keyword, so `lakh`
   is the substring that reaches that lane in one query.
3. Ran, once: `venv/bin/python backend/study.py "lakh"` → exit 1.

## What failed
YouTube rate-limited the caption fetch. Both of the high-view picks died on the
subtitle request:

```
[top] _67kFHkpq3I FAILED: ERROR: Unable to download video subtitles for 'en': HTTP Error 429: Too Many Requests
[mid] MrL1k7QMgVU FAILED: ERROR: Unable to download video subtitles for 'en': HTTP Error 429: Too Many Requests
ERROR: only 1/3 picks produced a transcript — not enough to ground a study note.
```

Only LOW landed (`Nooo9FKHVdw` — "₹15,000 vs ₹10 लाख Salary | हर Income Level
की असली ज़िंदगी", Vyapar Vridhi, 2,110 subs, 102 views, 10:32, transcript +
frames present). Per the contract I did **not** retry the command, and did
**not** write `vault/knowledge/video-studies/first-lakh-first-thousand.md`: one
low performer with no TOP to compare it against is an autopsy without a control,
and the note's whole value is the delta. A study of the two failed picks would
be a study of their thumbnails.

No hook type, beat map or views/sub table is reported. All three are derived
from transcripts I do not have; asserting them from the title metadata alone
would put a fabricated finding in the vault's one home for study evidence.

## Evidence
- `research/lakh/manifest.md` — the two FAILED rows above, verbatim.
- `research/lakh/low-Nooo9FKHVdw/` — the only complete pick (video.mp4 8.72 MiB,
  transcript.txt, frames/).
- The 429 is transient and environmental (the same host ran a 1,881-video
  yt-dlp scrape earlier today per `finance-topics-2026-07-31.md`, which is the
  likely cause of the quota). It is not "no data in the library" — unlike
  credit-history/attempt-1, the picks resolved fine; only the fetch was blocked.

## Untrusted input
I read `manifest.md` (titles/channel names — treated as data) and nothing else.
The LOW transcript was not read, since no study note is being written from it.
No prompt-injection attempt was seen in what I did read.

## Owed
A re-run of the packet once the 429 clears — this is a **scrape owed**, not a
research gap:

```
venv/bin/python backend/study.py "lakh"
```

Wait out the rate limit before re-running (same host, same IP). If TOP/MID still
429 on captions, fall back to `--skip-video` (captions + metadata only, far fewer
requests) or name the two ids explicitly with
`--ids _67kFHkpq3I MrL1k7QMgVU Nooo9FKHVdw`. Two of three picks need a
transcript or the stage fails again.

## What the run falls back on (vault knowledge, no fabrication)
Downstream stages must not wait on this. Already-earned, dated evidence:
- `vault/knowledge/niches/finance-topics-2026-07-31.md` — this topic's ranking
  evidence, both markets, and the **length caveat**: every breakout in this niche
  this month ran **15–22 min**, not 8–10. This run is MEDIUM/510s, i.e. still
  under the proven band; that is a deliberate constraint, not a data-backed one.
- `vault/knowledge/best-practices.md` — title formula (specific number + time
  bound + objection-killer), split-the-demand-between-cuts.
- `vault/knowledge/design-finance-blockframe.md` (+ the `swiss-band` entry in
  `tools/format.json` and `vault/knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md`).
- `vault/knowledge/niches/india-finance-market.md`, `.../us-market-2026.md`.
- The six shipped videos' milestone notes — nearest is
  `vault/videos/pay-yourself-first/`, which this video is meant to sequel.
