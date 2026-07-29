---
summary: Milestone note for the "Pay Yourself First" pair (Hindi/₹ 2:58.9 · US/$ 2:57.8) — both cuts rendered + QA-passed 2026-07-28, publish packs written. **LIVE on YouTube 2026-07-28** (hi youtu.be/PKU0_TeJ9_c · en youtu.be/mlvp4xZTROg); source archived to `src/`, studio dir deleted 2026-07-29. Owed — thumbnail-pick readback off the live videos · competitor scrape for this lane · analytics after 28 days.
updated: 2026-07-29
source: run.json + fin-render/fin-package logs in logs/ (attempt 1, /finance-video pipeline)
---

# Pay Yourself First — milestone note

Run 2026-07-27→28, `/finance-video` pipeline, all 18 stages attempt-1 pass
(fin-research failed EmptyStudyPacket and was rescued — see Run events).
Budget: **18 of 30 ElevenLabs calls**, 0 Pixabay calls.

## The two cuts

| | Hindi / India (@cashguruguides) | US / English (@moneymavens101) |
|---|---|---|
| Master *(deleted on archive — now on YouTube)* | was `…-hi/renders/FINAL-1080p-hi.mp4` | was `…-en/renders/FINAL-1080p-en.mp4` |
| Archived source | `src/hi/` | `src/en/` |
| Runtime | **178.9 s (2:58.9)** · 12.89 Mb/s | **177.8 s (2:57.8)** · 12.85 Mb/s |
| Voice | ElevenLabs **Harsh** (standard Hindi) | ElevenLabs **Brian** |
| Script | [[script-hi]] (9 lines h1–h9) | [[script-en]] (9 lines en1–en9, US rewrite not translation) |
| Publish pack | [[youtube-metadata-hi]] | [[youtube-metadata-en]] |

## Hero numbers (with sources)

- **hi: ₹12,000 auto-moved on the 1st → ₹1,44,000 in a year** (creator brief;
  counter animates month by month, en-IN lakh grouping in s7). Supporting feet
  on screen: RBI Annual Report May 2026 — net household financial savings 7.0%
  of GNDI FY25 (the ₹100→₹7 scene, s5); PLFS 2025 salaried-average foot (s7).
  fin-facts staged a **plausibility flag**: ₹12,000/mo is ambitious against the
  PLFS ₹24,217 average — the script answers it with the "even 5%" ladder.
- **en: $400 every payday → $4,800 in a year** (sourced independently per the
  US-rewrite rule). Supporting feet: BofA Institute Nov 2025 ~25% of households
  paycheck-to-paycheck (s1); BLS median usual weekly earnings $1,251 Q2 2026 +
  BEA "$1.00 earned → 3¢ saved" (s5); Fed SHED foot on the $400 card (s7).
- Both markets' facts staged in [[facts-staging]] (promotion to
  money-facts-2026 is the orchestrator's step). Known conflict recorded both
  ways: 25% (BofA) vs 66% (PYMNTS) paycheck-to-paycheck.

## QA (from the fin-render logs, both PASS)

| | hi | en |
|---|---|---|
| Runtime vs timing.json | +0.005 s | +0.041 s (AAC priming) |
| VO drift (xcorr, authoritative) | **0.021 s** max, uniform | **0.021 s** max, uniform |
| True peak | **−3.27 dBTP** (< −1 limit) | **−3.91 dBTP** |
| Loudness | −22.24 LUFS, LRA 3.3 | −21.13 LUFS, LRA 3.2 |
| Frame check | 9/9 scenes pass | 9/9 + s7 mid-count pass |
| blackdetect | 2 windows = photo-free navy scenes, false positives | same, false positives |

## Thumbnails (3 variants per cut, creator picks at upload)

`vault/videos/pay-yourself-first/src/thumbs/thumbnail-{hi,en}-v{1,2,3}.png` —
v1 THE MATH (green, centered, photo-free — recommended pattern-breaker) ·
v2 THE HOOK (red, money photo, "20 tak khali / empty by the 20th") ·
v3 THE FLIP (calculator, struck spend-first / green save-first).
`chosen:` line sits in each publish pack — **still unfilled as of 2026-07-29, i.e. it
survived a real upload blank** (read back by fin-archive on the credit-history run).

**But the creator did give feedback — in a different place.** [[youtube-metadata-en]]
records a **creator title pick, 2026-07-28**: option 8, "The $5 Trick That Saves You
Thousands Without Thinking" (vidIQ 83), plus a **`thumbnail-en-v4.png`** built for it
(`vault/videos/pay-yourself-first/src/thumbs/thumbnail-en-v4.png`, on disk). So by upload
day the `chosen:` field's own option set (v1/v2/v3) could not express the answer, and
the pick that matters may well be **v4**. Feedback lands as prose in the section the
creator was already editing — design the loop around that, not around an empty field.

**Recoverable without asking again:** the chosen thumbnail is the public thumbnail —
compare the live videos (youtu.be/mlvp4xZTROg · youtu.be/PKU0_TeJ9_c) against the four
PNGs on disk and record the match here. fin-archive has no network access, so this is
owed to whoever can open the URLs. Full argument: [[../credit-history/index]].

## Run events worth keeping

- **fin-research EmptyStudyPacket, rescued**: the library has never been
  scraped for this lane — run continued on vault knowledge; scrape owed (below).
- **Render-backgrounding fix**: subagent background tasks die on return, so
  the **orchestrator now owns encodes** (both fin-render logs note "encode run
  by orchestrator"). Pipeline-level fix, keep.
- **en assets R-5 dedupe** caught 3 byte-identical cross-channel images before
  they shipped in the en cut.
- **Channel sameness FLAG (both packages)**: this is the **4th consecutive
  blockframe-9 ~3-min structure on each channel** — the next upload should vary
  the architecture, or it's a 5-in-a-row template run.
  *(unvalidated — no analytics yet)*
- Thumbnail observation: v1 would be the first-ever green/centered/photo-free
  thumb on either channel; last 3 on both are red/left-text/money-photo.
  *(unvalidated — no analytics yet)*

## Published + archived (uploaded 2026-07-28 · archived 2026-07-29)

**State: LIVE on YouTube (both cuts) · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
| hi | @cashguruguides | https://youtu.be/PKU0_TeJ9_c | not recorded |
| en | @moneymavens101 | https://youtu.be/mlvp4xZTROg | not recorded |

**Source: `src/{hi,en,thumbs}/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO
lines (`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
seven thumbnail PNGs. `studio/videos/pay-yourself-first*` is **deleted** per the
finished-video rule ([[../../CLAUDE]]). **Re-render is reproducible, not free** — scene
photos and VO mp3s are gone; a rebuild re-pays image gens + ElevenLabs.

Still owed:
- **thumbnail pick** — no longer "fill `chosen:` at upload" (that already failed once
  on a live upload): **recover it off the two live videos** by comparing the public
  thumbnail against the archived `src/thumbs/thumbnail-{hi,en}-v*.png` (en has four
  candidates, incl. v4) and record the answer in the Thumbnails section above
- **competitor scrape for this lane** (`pay-yourself-first` / saving-first —
  library empty, from run.json `owed`)
- **analytics after 28 days** (only then may learnings touch best-practices)

~~proof-listen (hi, en)~~ · ~~upload~~ — both cuts went live 2026-07-28.
