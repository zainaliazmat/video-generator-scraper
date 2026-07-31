# fin-package — first-lakh-first-thousand · cut hi · attempt 1

**Date:** 2026-07-31 · **Result:** ok · `pipeline_check check package --slug first-lakh-first-thousand --cut hi --tier medium` → **PASS package-hi**

## Artifacts

- `vault/videos/first-lakh-first-thousand/youtube-metadata-hi.md` (the pack)
- `studio/videos/first-lakh-first-thousand-thumbs/thumbnail-hi.png` (1280×720)
- `studio/videos/first-lakh-first-thousand-thumbs/` — new HyperFrames project (`index.html` §v2, `package.json`, `meta.json`, `assets/{img,js,fonts}`, `snapshots/`)

## Thumbnail — ONE build (creator rule 2026-07-29)

Built the v2 style directly; no 3-variant A/B. Composition: left-aligned type over the
video's **own** scene photo for line 1.5 (`s5.jpg`, macro ₹5 coin in raking light — the
"hardest money you will ever save" frame), regraded `grayscale(.32) brightness(1.28)
contrast(1.16)` (the plate is already low-key monochrome, so the design system's 0.62
pull-down would have buried the coin — graded UP, contrast held).

- **Lines:** `PEHLA LAKH` (10 chars, ink) / `20 MAHINE` (9 chars, red mega). Two lines, both ≤12. Pass.
- **Colour:** focal red `--warn` (= "the stretch nobody helps you with", storyboard-hi §1) + accent green `--fund` on `7 mahine` in the sub. Amber deliberately absent — it means "a rate under examination" and no rate is on the frame.
- **Legibility assert:** downscaled to 320×180 and measured off the PNG (not estimated) — the red mega spans x 16→223 = **208 px = 65.0 %** of frame width, threshold ≥40 %.
- **`npm run check`:** 0 lint / 0 runtime / 0 layout (9 samples) / 0 motion / **25/25 WCAG AA**.
- **Export:** `npx hyperframes@0.7.66 snapshot --at 0.5` → `snapshots/frame-00-at-0.5s.png` → copied to `thumbnail-hi.png`.
- **Numeral discipline:** 20 (lines 1.1, 2.3) · 7 (1.2, 3.6) · ₹5,000 (1.1, 2.1) · 1 lakh (1.1, 1.5). All four on screen in the render. **₹ only, no dollar glyph.**

**One rebuild inside the attempt** (not a failure, recorded for the trail): the first
composition put an ink line *and* a `Pehla ₹1 Lakh` label *and* the red mega on the frame;
`20 MAHINE` wrapped to two lines, making three lines total and duplicating the label's
wording. Rebuilt with the label carrying the *condition* (`₹5,000 / MAHINA`) as a neutral
ink module and `white-space: nowrap` on the mega at 150px.

**Two deliberate variations from the last two packs' markup**, both traceable to this
cut's own render: the label is a **squared module** (every prior @cashguruguides thumbnail
used `border-radius: 999px`) and the statement **hangs from a rule**. That is `.swiss-band`
grammar — the architecture this video actually shipped in — so the thumbnail and the video
now agree.

**Sameness (last 3 on the channel):** nearest relative is good-debt-vs-bad-debt v2
(`208 MAHINE` / `17 SAAL`) — same "duration in the red mega slot" idea. Named in the pack.
Not a near-duplicate: different number, different unit line, first macro-object photo on
this channel, and the first time the accent colour carries a *second contrasting figure*
rather than restating the focal one.

## Search evidence — fresh pull, 2026-07-31, gl=in hl=hi

16 seeds fetched via `tools/autocomplete.py` this session. Full results in the pack.

**Best evidence any pack on this channel has had:** the bare seed `pehla 1 lakh` returns
four completions and *all four* are this exact video. `1 lakh kaise banaye` is the #1
completion of its own seed.

**The load-bearing finding:** the demand verb is **`kamaye` (earn)**, not `bachaye` (save)
— six of seven completions, and English confirms it (`earn your first 1 lakh`,
`how to earn first 1 lakh as a student`). This video teaches accumulating from a fixed
salary, not earning. Every recommended title leads with the verified *build* spelling
`kaise banaye`; the `kamaye` strings are kept as tags only, and that trade is stated in
the pack rather than hidden.

**Empties recorded, not papered over:**
- `sabse mushkil 1 lakh` → **NO SUGGESTIONS.** This **retires the script's own recommended
  title** ("Pehla 1 Lakh Sabse Mushkil Kyun Hai"). The thesis is the argument, not a query;
  the thumbnail carries hardness, the title carries the query.
- `pehla lakh` without the numeral → devotional/folk corpus (`pehla lakhon salam`,
  `pehla lakhindar`). **The `1` is load-bearing**; every title option keeps `1 Lakh`.
- `30000 salary me saving` → three loosely-related strings only; the ₹30,000 example has no
  direct query.
- `1 lakh kitne din me` → piggy-bank + devotional strings. "How long does it take" is not
  searched in this lane — which is why it is the thumbnail's job.

## Competitor scoreboard

`library.db` now holds **2,970 rows** and the finance lane has finally been scraped —
**423 rows** match `lakh|crore|saving|compound|sip|invest|bachat` (it was **0 of 1,124** at
credit-history). Raw-view leaders tabulated in the pack.

**Limit stated, not worked around:** the `subscribers` column is empty on essentially every
lane row, so **views÷subs cannot be recomputed from library.db today.** The 48×-subs
ranking that selected this topic lives in `knowledge/niches/finance-topics-2026-07-31.md`
and the proof video's transcript is still owed (run.json `owed_rescrape` — `study.py
"Story of Success"` 429'd).

Two reads that survive: (1) every non-podcast lane leader runs **11–26 min** and the 48×
proof ran **21:50** — this cut is 8:35, the channel's longest by 2.7× but still shorter
than every competitor, so the niche note's "breakouts ran 15–22 min" warning is only
half-answered and is the open question for the analytics readback; (2) lane winners title a
first-person conditional ("If I Started Investing in 2026") or a step-by-step, **neither of
which we may use** (persona rules; not a fund-picking video) — our differentiator is that
**no competitor title in the pull carries a months-to-milestone figure.**

## Chapters — read from the render, not from the script

Chapter starts = `scene_start` of each chapter's first line in
`studio/videos/first-lakh-first-thousand-hi/assets/voice/timing.json`:
`0.000 · 60.454 · 114.256 · 161.538 · 222.253 · 278.658 · 340.078 · 387.804 · 456.816`
→ `0:00 · 1:00 · 1:54 · 2:41 · 3:42 · 4:38 · 5:40 · 6:27 · 7:36`.
Total 514.789s timeline vs the upload file's 514.900s container. 9 chapters, first at 0:00,
smallest gap 47s — YouTube-valid. **The script's own chapter table was estimates
(0:55/1:48/2:31/3:32/4:28/5:30/6:19/7:24) and is superseded by these.**

Description carries the on-screen source citations verbatim from the render's scene foots
(DEA notification 30 Jun 2026 for 7.1% and the nine unchanged quarters; Nifty 50 TRI *shape*
for ~12%; PLFS Annual Report 2025 for ₹18,353–₹24,217; RBI Annual Report May 2026 for the
7.0%-of-GNDI savings rate; AMFI for the ₹500/₹250 SIP minimum as **price evidence**), plus
the ILLUSTRATIVE condition on every months-figure.

## Tags

17 strings, **446 chars** (limit 500). Every one appeared in a pull recorded above; **zero
invented filler**. `1 lakh ko 1 crore kaise banaye` was verified but **dropped** — it
promises a multiplier this video does not teach.

## Gate 2

- **Altered-content toggle: "No".** Synthetic narration (ElevenLabs Harsh) but no realistic
  synthetic media presented as real — motion graphics over licensed stock. **No on-screen
  disclosure required and none appears.** No AI host persona: no name, no face, no
  credentials, no first-person expertise (the word "मैं" appears nowhere in the script),
  second person throughout, and **no product pick** — PPF / post-office / the AMFI SIP
  minimum are on screen as price evidence with foots that say so.
- **Channel sameness: ✅ NOT FLAGGED — the streak breaks here.** The last 5 uploads were all
  blockframe-9, all the same 9-beat order, all 2:24–3:15; credit-history recorded a hard
  flag on the 6th. This upload changes architecture (swiss-band), tier (MEDIUM), runtime
  (8:34.8 vs a 3:15 previous max), scene count (86 vs 9), chapter model (per-line) and
  register (first *offense* video after six *defense* ones).
- **The one thing left open, in code:** `tools/format.json` still carries
  `architecture_lock: blockframe-9`, which **disagrees with the creator's swiss-band pick**
  in `run.json`; today that disagreement is resolved by hand per run. Per the creator's
  "fix defaults, not gates" rule this belongs in the config, not in a warning — flagged for
  the orchestrator, not changed here (`tools/` is out of this stage's write scope).

## Writes made

- `vault/videos/first-lakh-first-thousand/youtube-metadata-hi.md`
- `studio/videos/first-lakh-first-thousand-thumbs/` (new project + `thumbnail-hi.png`)
- this log

No `.env` read. No `.claude/` or `tools/` write. No git.
