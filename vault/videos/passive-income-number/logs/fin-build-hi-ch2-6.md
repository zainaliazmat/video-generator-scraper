---
summary: Chapter-2 hi, attempt 6 — re-drafted and re-sheeted the 18:49 composition, then RE-MEASURED the s16 serial-safe re-frame that attempt 5 built but never recorded. The margin did NOT invert: s16 leads s12 by +1.493 median (was +1.053) and by +1.694 photograph-only (was +0.494), and the serial `962971` is verifiably absent from every frame of the encode. One real regression: s16's p10 fell 26.12 → 23.97 and its p10 rank went #1 → #2, still inside the clause but no longer with room.
updated: 2026-08-09
source: measured from studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 (rendered this pass, 2026-08-09 00:34:56), all 2446 frames decoded at 1920x1080
---

# fin-build — passive-income-number hi ch2, attempt 6

Attempt 5 was killed by a session limit after doing the s16 re-frame and before
writing its log. **The re-frame was verified, not redone.** This pass re-rendered,
re-sheeted, and re-measured from scratch — the lost number is restated below, and
it is a fresh measurement of the current encode, not a recovery.

## 0 · Provenance — mtimes first, before any measurement

| Artifact | mtime | Ordering |
|---|---|---|
| `build.mjs` | 2026-08-08 **18:49:17** | — |
| `index.html` | 2026-08-08 **18:49:17** | with build.mjs, untouched this pass |
| `renders/DRAFT-ch2.mp4` | 2026-08-09 **00:34:56** | after index.html ✓ |
| `renders/SHEET-ch2.jpg` | 2026-08-09 **00:35:09** | after the mp4 ✓ |

`hyperframes render -q draft -f 30 -o renders/DRAFT-ch2.mp4` → **2446 frames /
81.536s container** (2446/30 = 81.533s of video; root duration 81.531s). ffprobe:
1920x1080, r_frame_rate 30/1, nb_frames 2446. Timing untouched.
`tools/chapter_sheet.py` → 13 frames, one per scene.

**Nothing in the composition was edited this pass.** No file under
`studio/videos/passive-income-number-hi-ch2/` changed except the two renders.

---

## 1 · THE MEASURED MARGIN — this is the number attempt 5 lost

### 1.1 · Method, stated before the answer

- **Statistic:** luma (Y as stored) **pooled median over each scene's settled
  span** (`start + 0.45` → next scene's start), full frame, 1920x1080. Same
  statistic as `fin-render-hi-ch2-3`, so the two are directly comparable.
- **Sampling density: EVERY frame. No sampling at all.** One streaming decode of
  the whole mp4 produced a 256-bin histogram per frame for all **2446** frames.
  s16 contributes **147** frames, s12 **223**, s15 **198**. The population is
  complete; there is no frame-choice error to quote.
- **Precision.** The percentile is linearly interpolated inside the 8-bit bin, so
  it is continuous. Interpolation step at the median bin: **3.18e-08 DN** for s16
  (304,819,200 px pooled), **5.61e-08 DN** for s12 (462,412,800 px). Quantisation
  is not the limiting error; the per-frame spread is.
- ⚠ **Convention offset, and it is a free cross-validation.** My percentile
  returns *bin lower edge + fraction*; fin-render's returned the bin centre. On
  **all twelve scenes other than s16** my median is exactly **+0.500** above
  fin-render's attempt-3 table (s12 36.712→37.212, s21 35.014→35.514, s18
  33.906→34.406, s20 31.389→31.889, s15 30.335→30.835, s13 20.936→21.436, …;
  s17 differs by +0.504, rounding). Two things follow for free: **the renderer is
  deterministic** (a brand-new encode reproduces twelve scenes to three decimals),
  and **s16 is the only thing that moved.** Differences are convention-free.
  Subtract 0.500 from any absolute below to read it in fin-render's convention.

### 1.2 · THE ANSWER: **s16 − s12 = +1.493 median. It did not invert — it widened.**

| | before the re-frame (attempt 3) | now | change |
|---|---|---|---|
| **full frame (the ranking statistic)** | **+1.053** | **+1.493** | **+0.440** |
| **photograph only, rows 0–360 + 760–1080** | **+0.494** | **+1.694** | **+1.200** |
| rows 0–320 + 720–1080 | +0.727 | +2.138 | +1.411 |
| rows 0–420 + 820–1080 | +0.869 | +1.695 | +0.826 |
| left + right thirds | +4.263 | +3.397 | −0.866 |

The clause the brief flagged as the one at risk is the photograph-only reading,
because a 2.42x window on a different region of the file changes the
photograph's contribution completely. It did — **in the right direction, and by
more than the full-frame margin.** The tightest reading went from +0.494 (a
margin a re-crop could plausibly have moved) to **+1.694**. Sign stable across
all five regions, as before.

Where it came from: s12's numbers are unchanged to three decimals in every
region (36.384 / 35.963 / 36.395 / 34.718 — all exactly +0.500 on attempt 3).
s16's photograph-only median rose 36.878 → **38.077 (+1.199)**. The whole change
is the window: it sits on the lit focus plane of the note instead of averaging in
the dark surround.

### 1.3 · How resolved is +1.493

| Check | Result |
|---|---|
| per-frame median range, s16 | 38.64 – 38.83 (sd 0.07, n=147) |
| per-frame median range, s12 | 36.64 – 37.60 (sd 0.24, n=223) |
| **min(s16) − max(s12)** | **+1.035 — the distributions are disjoint** |
| bootstrap, 4000 resamples over frames | **+1.496, 95% CI [+1.462, +1.530]**, P(s16>s12) = 1.0000 |
| span-definition sensitivity, 10 definitions (settle +0.30/0.45/0.60/0.90/1.20 × tail trim 0.00/0.45) | **+1.437 … +1.530** — never near zero, never changes sign |

**Signed margin: +1.49 ± 0.04. About 35x its own error bar. Resolved.**

### 1.4 · The thirteen-scene table (this encode)

| Rank | Scene | Settled span | n | **MEDIAN** | **p10** | p90−p50 | per-frame range | sd |
|---|---|---|---|---|---|---|---|---|
| **1** | **s16 (payoff)** | 45.182–50.077 | 147 | **38.705** | 23.973 | 8.881 | 38.64–38.83 | 0.07 |
| 2 | s12 | 18.132–25.535 | 223 | 37.212 | 22.109 | 15.678 | 36.64–37.60 | 0.24 |
| 3 | s21 | 73.475–81.531 | 241 | 35.514 | 23.533 | 8.588 | 35.34–35.83 | 0.10 |
| 4 | s18 | 55.872–60.062 | 125 | 34.406 | 19.389 | 15.928 | 34.36–34.49 | 0.03 |
| 5 | s17 | 50.527–55.422 | 147 | 33.211 | 17.586 | 15.866 | 31.88–33.36 | 0.46 |
| 6 | s20 | 67.059–73.025 | 179 | 31.889 | **24.507** | 11.064 | 31.80–31.96 | 0.05 |
| 7 | s15 | 38.112–44.732 | 198 | 30.835 | 19.290 | 16.864 | 30.59–31.08 | 0.14 |
| 8 | s14 | 31.696–37.662 | 179 | 30.170 | 19.099 | 17.470 | 29.65–30.55 | 0.24 |
| 9 | s11 | 12.003–17.682 | 170 | 29.756 | 17.415 | 19.120 | 29.26–30.24 | 0.26 |
| 10 | s19 | 60.512–66.609 | 183 | 29.622 | 13.691 | 9.147 | 28.44–30.58 | 0.64 |
| 11 | s9 | 0.450–5.293 | 145 | 24.785 | 15.951 | 16.594 | 24.45–26.52 | 0.64 |
| 12 | s10 | 5.743–11.553 | 174 | 21.910 | 16.244 | 23.421 | 21.35–22.55 | 0.35 |
| 13 | s13 | 25.985–31.246 | 158 | 21.436 | 15.631 | 22.000 | 21.03–21.88 | 0.22 |

    p10 rank  s20 24.51 · s16 23.97 · s21 23.53 · s12 22.11 · s18 19.39 · s15 19.29
              · s14 19.10 · s17 17.59 · s11 17.41 · s10 16.24 · s9 15.95 · s13 15.63 · s19 13.69

### 1.5 · The binding clause, re-checked — PASSES, but p10 lost its cushion

| Clause | Requirement | Measured | Verdict |
|---|---|---|---|
| Sound-off gate (floor) | nameable object with type covered | ₹500 banknote — ₹ + `५००` + guilloche + microtext | **PASS**, degraded — see §3 |
| Median | top quartile, ceil(13/4)=4 ⇒ top 4 | **#1 of 13**, 38.705 | **PASS** |
| p10 | #1 or #2 | **#2 of 13**, 23.973 — s20 leads by 0.534 | **PASS** |
| Median step IN | non-negative at the entering joint | s15 30.835 → s16 **+7.870** | **PASS** |

⚠ **THE ONE THING THE RE-FRAME COST, stated plainly.** s16's p10 fell **26.120 →
23.973 (−2.147)** and its rank fell **#1 → #2**, overtaken by s20 (24.507). The
clause says "#1 or #2", so it passes — but attempt 3 passed with s16 +1.61 clear
of the field, and it now passes 0.534 *behind* the leader. The cause is visible
in the frame: the window's lower half is an out-of-focus note in shadow, which
the old full-bleed framing did not have. **This is the trade the re-frame made
and it is a real one — the hero is no longer the darkest-floor-safe scene in the
chapter, it is second.** Anything that darkens s16 further from here breaks the
clause; the slot has no margin left on p10.

Attempt 4 replaced this photograph specifically because it measured p10 14.0,
last of thirteen. 23.97 at #2 is nowhere near that failure, so the re-frame has
not re-opened it — but the direction of travel is worth one line in the next
pass's brief.

---

## 2 · THE SERIAL IS GONE FROM THE ENCODE — verified from frames, not arithmetic

The brief is right that the arithmetic is not the evidence: the previous
clearance was also convincing and also wrong. Verified by inspecting the encode.

**One geometric fact makes a small number of frames exhaustive.** `ken(…, false)`
sweeps scale 1.16 → 1.00 with xPercent +2.5 → −2.5 on a `.bg` at `inset:-8%`
(box 2227.2 x 1252.8, centred at 960). Visible source-x interval:

- t = scene open, s=1.16, dx=+55.68 → **[84.4, 1739.6]**
- t = ken end, s=1.00, dx=−55.68 → **[55.68, 2015.68]**

The final interval **strictly contains** the opening one on both axes (scale only
on y), and after the ken ends the frame holds at that value for the transition
tail. **Every frame of s16 shows a subset of what the last frame shows.** So a
full-resolution inspection of the last frame is exhaustive for the scene — and it
also confirms empirically what the corrected comment claims: the field of view
*widens* from 45.2 to 50.05 (the `५००` gets smaller), i.e. the move is a PULL
BACK, exactly as emitted, not the push-in the old note asserted.

Frames pulled from the encode and read at full resolution, plus each one split
into four 960x540 quadrants upscaled 2x with brightness+contrast lifted (the
serial was previously "legible at full resolution", so the check was done at
better than delivery legibility):

| t | position in scene | what is in frame | serial |
|---|---|---|---|
| 44.740 | pre-open — still s15 (pencils) under the dissolve | n/a | n/a |
| 45.200 | scene open, most zoomed (s≈1.16) | `५००` partly clipped at the right edge, guilloche, dark note edge left | **none** |
| 47.400 | middle | `₹५००` legible upper right, microtext strip | **none** |
| 50.050 | ken end, WIDEST — the superset frame | full `₹५००`, guilloche rosette, microtext, inked note edge left, blurred note below | **none in any of the four quadrants** |

**No digit block, no serial panel, nothing resembling `962971`, anywhere in the
superset frame.** The nearest thing to lettering outside the denomination is the
`भारत` microtext strip right of the rosette, which is not a serial.

---

## 3 · Sound-off, type covered — PASS, and honestly weaker than what it replaced

With the `.stack` masked, the upper ~45% of the frame carries a banknote surface
with the `₹` sign and Devanagari `५००` large and unambiguous, the guilloche
rosette, microtext, and the inked edge of a second note across the upper left.
**Nameable as money: yes — an Indian ₹500 banknote, macro.**

Recorded against it, because the note's own reasoning for rejecting one of the
alternative windows applies partly here too: the lower ~55% of the frame is a
large out-of-focus pale note that names nothing on its own. The frame is carried
entirely by its top half. The pre-re-frame framing was stronger sound-off (a fan
of ₹500s *plus* a coin stack, unmistakable at a glance); this one requires the
viewer to read the top of the frame. It clears the gate, it is not the best
version of the gate. Same root cause as the p10 drop in §1.5 — one defect, two
symptoms.

The composition's own `₹10,00,000` sits over the blurred lower half and is fully
clear of the `₹५००`, so the note's claim about the denomination "clearing the
composition's own figure" holds on the encode.

---

## 4 · Confirmations

| Check | Result |
|---|---|
| `npm run check` (`hyperframes check`) | **passed** — 0 errors, 0 warnings, 11 infos (all `container_overflow` on `.bg` under `ken`, and `#s20-plate`; the known-benign set). Motion 0/0. Contrast **13/13 pass WCAG AA**. |
| `tools/check_vo_frame.py passive-income-number --cut hi --chapter 2` | **PASS**, exit 0 — 13 scenes cross-checked against their VO lines |
| `tools/audio/cues.py studio/videos/passive-income-number-hi-ch2` | **exit 0** |
| draft newer than `index.html` | ✓ 00:34:56 vs 18:49:17 |
| sheet newer than `index.html` | ✓ 00:35:09 vs 18:49:17 (and after the mp4) |
| duration | 2446 frames / 81.533s video, root 81.531s, offset 42.475s — unchanged |

Contact sheet read end to end: 13 tiles, one per scene, each with a photograph,
the watermark riding bottom-right on every one. Nothing overflows the safe area.
s16's tile shows the re-framed note and sits correctly in the tonal ladder.

## 5 · Not touched, per the brief

The re-frame · s14→s15 · s11's stepped water tank · s18's 1.380s settled figure ·
s20's twelve drawn cells · the rate asserts · timing. No design token was edited,
no scene note rewritten. The only thing this pass produced is the two renders and
this log.

## 6 · Carried forward

1. **s16's p10 has no cushion left** (#2, 0.534 behind s20, down 2.147 from
   attempt 3). Any further darkening of that slot breaks the clause.
2. **s20 still fails the sound-off gate at #6** (blank dark plaster; its twelve
   cells are drawn, not photographed) — unchanged, still fin-assets' open ruling
   request.
3. `s16`'s scene note points at `fin-build-hi-ch2-5.md` for this measurement.
   That file does not exist and never will; **the number lives here, in §1.2.**
