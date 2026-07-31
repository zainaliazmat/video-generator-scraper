---
summary: fin-render gate-two FRAME CHECK, hi cut, attempt 1 — FAIL. All 86 scene frames captured at their last-cue time and inspected. Five scenes carry wrong-currency imagery on a ₹/India cut (including the 11.7s hook and RECAP ONE), and s17 loses 40% of the frame to a flat-black block. No encode was run. 80/86 frames pass.
updated: 2026-07-31
source: studio/videos/first-lakh-first-thousand-hi/snapshots/qa/b1..b11 (86 frames) + index.html + assets/img/CREDITS.txt + storyboard-hi.md
stage: fin-render, cut hi, attempt 1 — invocation 1 of 2 (frame check only)
---

# fin-render — «पहला एक लाख» hi, attempt 1 — GATE TWO: FAIL

**No encode was run.** Per the orchestrator scope this invocation is the frame check only.
`renders/` does not exist and must not be created until fin-build lands a fix.

## Method

- Snapshot times were **not** taken on trust. Every `rise`/`fill`/`fade` cue was parsed out of
  the inline script and each scene's **last non-`ken` cue end** computed. All 86 values in
  `snapshots-at.txt` match that end to within 0.6s **and** fall inside their own scene
  (`scene_start ≤ t ≤ scene_start + scene_duration`). 0 mismatches. Reused as-is.
- Captured all 86 into `snapshots/qa/b1…b11`, then read every frame (11 contact sheets +
  8 full-resolution pulls on the flagged scenes).
- **CLI defect worth recording:** `hyperframes snapshot` **wipes its `-o` directory on every
  run**, so batching into one dir keeps only the last batch. This is why `snapshots/` held
  8 of the 86 fin-build claims to have captured. Per-batch dirs are the fix.
- Second CLI defect: the run fails with `Navigation timeout of 10000 ms exceeded` on roughly
  2 of every 3 attempts, independent of frame count (measured at 2, 10 and 29 frames).
  `--timeout` does not govern it. Worked around with a retry loop; 11/11 batches succeeded
  within 5 tries.

## Blocking findings

### 1. Wrong-currency imagery — 5 scenes, ~31s of a 514.8s cut

The channel is @cashguruguides, ₹, India. Every figure on screen is in ₹.

| scene | on screen | window | file | what the photo actually shows |
|---|---|---|---|---|
| **s1 + s2** | THE FIRST LAKH · 20 MONTHS / THE TENTH LAKH · 7 MONTHS | **0.0 – 11.74s** | `s1.jpg` | euro + Polish coins; `…ZŁOTYCH` and `…CIE ODZNA…` legible right of centre. **This is the hook** — and s1/s2 share one continuous zoom on the same file, so it is the first 11.7 unbroken seconds of the video |
| **s12** | ₹60,000 | 66.64 – 71.75s | `s12.jpg` | stacked euro cents (copper 1/2/5c, gold 10/20/50c) |
| **s34** | "How much of each month's income leaves and stays out" | 197.16 – 202.82s | `s34.jpg` | US quarters, dimes, pennies — and an envelope printed **`PRESORTED STANDARD · U.S. POSTAGE`**, legible at 1080p |
| **s79** | **₹1,500 works. ₹500 works.** | 467.40 – 473.17s | `s79.jpg` | **`1 ZŁOTY`** and `2 ZŁOTE` legible and in focus, filling the band. The scene is *about* the amount |
| **s81** | RECAP ONE · "The first lakh: 100% you" | 478.28 – 486.13s | `s81.jpg` | **`UNITED STATES OF AMERICA`** and **`ONE CENT`** legible on Lincoln cents |

Sources confirm it (`assets/img/CREDITS.txt`): s81 = pixabay "pennies", s79 = Mateusz Dach
"two coins", s34 = "stacked of bills and coins on marble", s1 = Łukasz Pajzert "close-up of coins".

Counter-example, so the fix is scoped correctly: **s41, s50, s53, s54, s56 are right** —
RBI notes, ₹100 and ₹500 notes, ₹20 coins, Indian coin set. The cut is not uniformly wrong;
these five are.

Minor, same class, no full-res confirmation possible: **s19** (113.27s, `100% savings · 0% returns`)
drops an unidentifiable foreign coin into a piggy bank among scattered foreign coins. Swap it
if a candidate is already in `assets/img/_cand`; not on its own a blocker.

### 2. s17 — 40% of the frame is flat black

`s17` (96.29 – 104.22s), the reversed-field thesis scene, **`WHAT THE MARKET BOUGHT YOU` /
`2 MONTHS`**. Measured over the un-toned right region (crop `767×900+1153+180`):

```
s17   YAVG = 16.03   (16 = video black floor)
s1    YAVG = 29.89
s33   YAVG = 90.02
s84   YAVG = 89.27
```

767 × 1080 px of dead black, hard-edged against the toned left. Held 8.4s.

**It is not a CSS bug.** s17's markup is byte-identical in structure to s33's (`v-r` +
`v-ap-r` + `v-tone`), and `s17.jpg` is 1880×1253 — same as `s1.jpg`. The image itself
(Pexels "hourglass and book") is low-key on the right, and the system grade
`grayscale(.32) brightness(.62)` crushes that side to the floor. Fix is the asset or a
per-scene grade lift, not the stylesheet. Note fin-build has already spent its one permitted
per-scene grade override on s46 (`brightness(1.40)`); replacing `s17.jpg` is the cleaner route.

## Non-blocking, fix while you are in there

- **s63** (372.21s): the statement wraps to an orphan `to` on line 2, and line 1
  (`The rain puts in what your bucket used`) ends flush against the tone-block edge at
  x = 1153 px. One more character and green type would sit on the bright side of the tone
  with no contrast. Shorten the line or widen the tone.
- **s67** (395.25s) shows a **German** calendar (`Mi Do Fr Sa`, `August`) and **s30**
  (174.09s) a German form (`Bescheinigung`, `Beförderung`). Not currency, low legibility,
  cosmetic only — but on a Hindi cut it is the same class of error as the coins.

## What passes (80 of 86)

Layout inside the safe area on every frame; furniture (`CH n · i / 86`) present and
consistent on all 86; ₹ renders in real FinanceSans at weight 900 everywhere it appears
(no Arial Black fallback); the `.stamp` fix holds — s19 red, s46 green, s64 amber, s76 red
and the s85 orange CTA all read dark-on-fill; one role colour per scene throughout; no brand
marks, no phone screens, no faces; the C-R/C-L alternation and the mosaic minors sit on
their column lines. The three colour scenes the build log flagged (s43, s58, s83) are the
most saturated in the cut but are legible and deliberate — not raised as a defect.

## Numbers

| | |
|---|---|
| Scenes checked | **86 / 86** at last-cue time |
| Snapshot-time audit | 86 / 86 in-scene, 0 drift from computed last cue |
| Frames failing | **6** (s1, s2, s12, s17, s34, s79, s81 → 5 distinct defects) |
| s17 dead region | 767 × 1080 px, YAVG **16.03** |
| Encode | **not run** |
| Runtime / drift / dBTP | not measured — QA is invocation 2, after the master exists |
