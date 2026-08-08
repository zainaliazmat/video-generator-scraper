---
summary: Chapter-2 draft render + contact sheet for passive-income-number-hi, attempt 2 (style E, s9-s21). The encode is mechanically clean on every axis, and the ONE measurement that decides locking says NO — s16 is 7th of 13 by p90, 4th by median, 7th by mean; s11 is still the brightest and three more photographs sit between them.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 (mtime 2026-08-08 16:19)
---

# fin-render — passive-income-number hi ch2, attempt 2

Mode: **CHAPTER DRAFT** (orchestrator §3b step 4). Gate two and the full encode were NOT
run — this is a draft for judging images, motion and timing.

## Provenance — what these numbers were measured on

| Artifact | mtime | Note |
|---|---|---|
| `renders/DRAFT-ch2.mp4` | **2026-08-08 16:19** | 18.4 MB, rendered in 2m 32.8s, this run |
| `renders/SHEET-ch2.jpg` | **2026-08-08 16:19** | 13 cells, built from the mp4 above |
| `renders/SHEET-ch2.json` | **2026-08-08 16:19** | sample-time index (orchestrator reads this) |
| `index.html` | 2026-08-08 16:12 | the attempt-3 build |
| `build.mjs` | 2026-08-08 16:12 | same pass |

Both outputs **overwritten and confirmed by mtime** — the 13:02 attempt-1 draft is gone.
Retired files still present in `renders/` and NOT reported on: `DRAFT-ch2-v2.mp4`,
`SHEET-ch2-v2.*`, `SHEET.*` (13:19, an alias copy of the 13:02 sheet),
`SHEET-ch2.json.superseded`.

    npx hyperframes render . -c index.html -o renders/DRAFT-ch2.mp4 -q draft -f 30
    python3 tools/chapter_sheet.py studio/videos/passive-income-number-hi-ch2 \
            studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 \
            -o studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2.jpg

Draft quality only, no `--resolution`, no `--gpu`, no chunked encode.

---

## 1 · THE UN-INVERSION — settled from the encode. **s16 is NOT the brightest. It is 7th.**

p90 / median / mean of luma over each scene's **SETTLED** span (start+0.45 to the next
scene's start, so dissolve frames are excluded and cannot flatten the endpoints), sampled
at 4 fps on full-resolution frames (326 samples). Y plane as stored.

| Scene | Settled span | **p90** | p90 min | p90 max | **median** | **mean** | p10 | span s |
|---|---|---|---|---|---|---|---|---|
| s9  | 0.00–5.29   | 40.9 | 40 | 41 | 24.5 | 31.6 | 15.7 | 5.29 |
| s10 | 5.74–11.55  | 44.6 | 42 | 45 | 21.5 | 30.8 | 16.0 | 5.81 |
| s11 | 12.00–17.68 | **55.1** | 55 | 56 | **44.0** | **46.1** | 34.5 | 5.68 |
| s12 | 18.13–25.54 | 52.7 | 52 | 54 | 36.9 | 39.0 | 21.7 | 7.40 |
| s13 | 25.98–31.25 | 42.9 | 42 | 44 | 21.0 | 28.1 | 15.2 | 5.26 |
| s14 | 31.70–37.66 | 53.3 | 52 | 54 | 39.2 | 39.2 | 15.0 | 5.97 |
| s15 | 38.11–44.73 | 52.2 | 52 | 54 | 40.0 | 40.4 | 15.0 | 6.62 |
| **s16 (payoff)** | 45.18–50.08 | **47.1** | 47 | 48 | **37.0** | **35.3** | 14.0 | 4.89 |
| s17 | 50.53–55.42 | 48.9 | 48 | 49 | 32.8 | 36.2 | 17.0 | 4.89 |
| s18 | 55.87–60.06 | 50.0 | 50 | 50 | 34.0 | 34.8 | 19.0 | 4.19 |
| s19 | 60.51–66.61 | **38.6** | 37 | 40 | 29.2 | 32.9 | 13.0 | 6.10 |
| s20 | 67.06–73.03 | 43.0 | 41 | 44 | 31.0 | 35.0 | 24.0 | 5.97 |
| s21 | 73.48–81.53 | 43.9 | 43 | 44 | 35.0 | 38.3 | 23.0 | 8.06 |

**Duration-weighted over 76.13s of settled span: p90 47.2 · median 33.0 · mean 36.3.**
Whole-timeline mean p90 including dissolves 47.1. Range 38.6–55.1 = **16.5 points** (was
21.7). Open (0–2s) 41.0, close (last 2s) 44.0.

### The ranking, all three measures

    p90     s11 55.1 · s14 53.3 · s12 52.7 · s15 52.2 · s18 50.0 · s17 48.9 · s16 47.1
            · s10 44.6 · s21 43.9 · s20 43.0 · s13 42.9 · s9 40.9 · s19 38.6
    median  s11 44.0 · s15 40.0 · s14 39.2 · s16 37.0 · s12 36.9 · s21 35.0 · s18 34.0
            · s17 32.8 · s20 31.0 · s19 29.2 · s9 24.5 · s10 21.5 · s13 21.0
    mean    s11 46.1 · s15 40.4 · s14 39.2 · s12 39.0 · s21 38.3 · s17 36.2 · s16 35.3
            · s20 35.0 · s18 34.8 · s19 32.9 · s9 31.6 · s10 30.8 · s13 28.1

**Stated plainly, as asked: s16 is not the chapter's brightest frame on any measure.
Its rank is 7th of 13 by p90, 4th of 13 by median, 7th of 13 by mean. The chapter's
brightest is s11 on all three.** The operable clause of
`ground_and_payoff_legibility_2026-08-08` — *the payoff frame's photograph must be the
most legible in its chapter, never the least* — is **not yet satisfied.**

### The predictor missed by ~8 points in BOTH directions, and the errors compounded

| Frame | fin-assets predicted | **measured** | error |
|---|---|---|---|
| s16 (hero) | 37.3 → **54.2** | **47.1** | **−7.1** (over-predicted, the exact en ch2 signature) |
| s14 (plateau) | 59.0 → **44.7** | **53.3** | **+8.6** (under-predicted) |
| s15 (plateau) | 59.0 → **44.7** | **52.2** | **+7.5** |

The declared hedge was "s16 leads s11 by 1.4 predicted points". Measured, **s16 trails s11
by 8.0 p90 points** — because the hero rose 7 less than predicted *and* the plateau fell 8
less than predicted, and the two errors point the same way. The hedge did not survive
contact with the encode; the ±7 over-prediction fin-assets flagged on itself is real and
is now measured twice on this chapter.

### s11 alone does not fix it. FOUR distinct photographs sit above s16.

The brief names s11 as the next file to move. It is necessary and **not sufficient** —
move s11 only and s16 rises from 7th to 6th, not 1st. Above s16 (47.1) by p90:

| Above s16 | p90 | Distinct photograph? |
|---|---|---|
| s11 water tank on pale sky | 55.1 | yes — the named lever |
| s14 / s15 dotted notebook (ONE photo, one hold) | 53.3 / 52.2 | yes — the replacement landed 8 too bright |
| s12 two taps on a wall | 52.7 | yes — **and see §2, this file was replaced too** |
| s18 / s17 adding machine (ONE photo, derived-crop hold) | 50.0 / 48.9 | yes |

Either four photographs come down below 47.1, or s16's own photograph goes up past 55.1.
The lever is always the photograph (never the ground, scrim or grade).

### And the FIRST clause of the ruling is now violated by a different scene

The inversion was not removed; **the trough moved.** s16 rose +9.8 (37.3 → 47.1, the
largest single-scene gain in the pass) and is no longer the darkest. The new darkest frame
is **s19 at 38.6, held 6.10s** — a black phone, screen off, on dark planks, carrying
*"The phone recharge and the home internet."* That is a **consequence example**, not the
chapter's most substantive beat, so *"the darkest longest-held frame must be the chapter's
most substantive beat"* now fails at s19 instead of s16. s19 was one of the replaced files
and it moved **53.9 → 38.6, −15.3** — the largest move in the pass, in the wrong
direction. (Longest-held scene overall is s21 at 8.06s / 43.9.)

### The live metric question, answered on data

Both measures are given above so the en ch2 CEO can rule once for both cuts. What this
chapter's data actually shows:

1. **The two measures DO disagree, materially, and median/mean is the fairer one.** p90
   reads the brightest decile and is fooled exactly as the en fin-assets argues: **s10**
   ranks 8th on p90 (44.6) but **last-but-two on median (21.5)** — a near-black night desk
   with one white lamp shade. **s13** is 11th on p90 (42.9) and **13th on median (21.0)**.
   Conversely **s16 gains three places on median** (7th → 4th), because the ₹500 note fills
   most of the frame at an even mid-tone rather than blowing one small highlight. On the
   question "which frame is most *legible*", median/mean is the better proxy: it rewards a
   uniformly readable field and refuses to reward one bright object on black.
2. **It does not change this chapter's verdict, and it does not rescue s16.** s11 wins on
   all three, and its lead is *wider* on the fairer measures — **+1.8 on p90, +4.0 on
   median, +5.7 on mean.** s11 is a flat, even pale-sky field (p90 min 55 = max 56, i.e. no
   spread at all), which is the shape a median-based rule is designed to rank first.
3. So: adopting median/mean is defensible on its merits and should be ruled on separately —
   but on ch2-hi it moves s16 from 7th to 4th and nothing further. **Any ruling on the
   metric leaves this chapter needing a re-source.**

The curve, 4s buckets (this is the shape, not the endpoints):

    0-  4s  41.0     32- 36s  53.9   \
    4-  8s  42.5     36- 40s  52.4    >  s14/s15 hold — still the plateau, 12.6s, still #2
    8- 12s  45.3     40- 44s  52.0   /
   12- 16s  55.2  <- s11, the peak    44- 48s  48.2  <- s16 payoff, +9.8 vs attempt 1
   16- 20s  53.4                      48- 52s  47.8
   20- 24s  52.8                      52- 56s  49.0
   24- 28s  47.3                      56- 60s  50.0
   28- 32s  44.0                      60- 64s  38.6  <- s19, the NEW trough
                                      64- 68s  39.8
                                      68- 72s  43.1
                                      72- 84s  43.7 / 44.0 / 44.0

Strip the s14/s15 hold and the other eleven scenes average p90 46.1 (was 44.9), so the
chapter is *slightly* less flat than before but the plateau is still a single sustained
image carrying most of the range. Open 41.0 / close 44.0 — still effectively no arc.

---

## 2 · ⚠ A SEVENTH PHOTOGRAPH CHANGED, UNDECLARED IN THE BRIEF: s12

The brief names six replaced files (s9, s14, s15, s16, s19, s20). **`assets-ch2/final/s12.jpg`
was replaced too** — mtime **13:50**, i.e. 48 minutes *after* the attempt-1 draft (13:02),
and its predecessor sits in `assets-ch2/superseded-r1/s12.jpg` (173,820 B, 10:47) against
the shipped file (693,924 B). Different dimensions: 1880×1253 → 1733×1300.

It matters to the decision in §1, so it cannot be treated as bookkeeping:

| | old s12 | new s12 |
|---|---|---|
| p90 | 46.0 (below s16's new 47.1) | **52.7 (above it)** |
| `.src` note | full round/cell provenance + the YHIGH-88 rejection it replaced | **a bare query string, no round, no cell, no rationale** |

So one of the four photographs now blocking the un-inversion is a file that (a) was not
declared as changed and (b) is the only replacement in this pass shipped **without a `.src`
rationale**, while s9 / s14 / s15 / s16 / s19 / s20 all carry long ones. Had s12 stayed at
46.0 it would have been below the hero. Flagging as provenance, not as a picture defect —
the frame itself is fine (two taps on a wall, more than one tap in frame, which is what
`TWO TAPS` needs).

Full before/after for every scene, so the pass can be audited in one place:

| Scene | attempt 1 p90 | attempt 2 p90 | Δ | file replaced? |
|---|---|---|---|---|
| s9  | 43.6 | 40.9 | −2.7 | yes (declared) |
| s10 | 45.2 | 44.6 | −0.6 | no |
| s11 | 55.0 | 55.1 | +0.1 | no |
| s12 | 46.0 | 52.7 | **+6.7** | **yes — UNDECLARED** |
| s13 | 43.3 | 42.9 | −0.4 | no |
| s14 | 59.0 | 53.3 | −5.7 | yes (declared) |
| s15 | 59.0 | 52.2 | −6.8 | yes (declared) |
| s16 | 37.3 | 47.1 | **+9.8** | yes (declared) |
| s17 | 48.8 | 48.9 | +0.1 | no |
| s18 | 49.9 | 50.0 | +0.1 | no |
| s19 | 53.9 | 38.6 | **−15.3** | yes (declared) |
| s20 | 38.9 | 43.0 | +4.1 | yes (declared) |
| s21 | 42.9 | 43.9 | +1.0 | no |

---

## 3 · Frame count, duration, CFR from packet timestamps

| Measure | Expected | Measured | Verdict |
|---|---|---|---|
| Frames | ceil(81.531 × 30) = **2446** | **2446** (`ffprobe -count_frames`) | PASS |
| Video stream duration | 81.531s | 81.533333s | PASS |
| Container duration | — | 81.536000s | PASS |
| Root `data-duration` | — | 81.531 (s21 73.025 + 8.506) | consistent |
| fps tag | 30/1 | r_frame_rate 30/1, avg 30/1 | (not used as evidence) |
| Resolution / pix_fmt | — | 1920×1080 yuv420p | — |

**CFR verified from PACKET TIMESTAMP deltas, not the fps tag.** 2446 packets, 2445 deltas,
exactly two values and no third:

    0.033333  × 1630
    0.033334  ×  815

First pts 0.0, last pts 81.5. Frame counts sum; the chapters will not drift at the joint.

## 4 · Black-segment scan

`blackdetect=d=0.05:pix_th=0.10` → **0 segments**. No dip-to-black at any joint.

---

## 5 · s18's ₹2,500 — the video's first derived income figure. **FIXED, confirmed from the encode.**

Measured on the green-glyph ink mask of the `.huge` band (rows 525–660), frame by frame at
30 fps:

| Event | Measured t | Derivation |
|---|---|---|
| First paint | **58.267** | pop at S.s18+2.81 = 58.232 + fade-in |
| countUp value lands | **58.682** | 58.232 + `countDur` 0.45 |
| Last glyph-mask change (pop scale ends) | **58.833** | 58.232 + pop 0.60 |
| Foot fade complete | 59.032 | `fade("#s18-foot", S.s18+3.11, 0.5)` |
| Dissolve to s19 begins | 60.062 | |

**Settled time = 60.062 − 58.682 = 1.380s** — exactly the figure the build asserted, up
from **0.629s**. Even measured from the stricter moment (final geometry, 58.833) it is
**1.229s**, still over the 1.20s floor. Mask pixel count is flat at 16 154/16 155 from
58.833 to 60.062 — nothing moves. Hero benchmark s16 remains **2.245s**.

Ink history confirming the shorter roll: 0 px through 58.233 → 6 438 at 58.300 → 12 898 at
58.400 → 16 032 at 58.500 → stable ~16 155 from 58.833.

**The two things that were not to be touched were not touched.**
`index.html:441` reads `pop("#s18-num", S.s18 + 2.81, 0.6)` — the spoken anchor is
unmoved — and `studio/videos/passive-income-number-hi/assets/voice/timing.json` has mtime
**2026-08-08 06:32**, ten hours older than `build.mjs` (16:12). Corroborated from the audio:
peak (−3.800364 dB) and all ten `silencedetect` boundaries are **identical to attempt 1 to
the millisecond** (e.g. 65.5897–66.9862 / 1.3965s), so the VO track is byte-for-byte the
same render input.

---

## 6 · THE DRAWN LAYER — s20's twelve cells. Renders, clears the floor, states the count.

**Twelve cells render.** 3 columns × 4 rows, all twelve marks present and countable at a
glance at 72.50. Grid geometry from the encode matches the authored plate space exactly
(`p-c` at left 1046 / top −60, viewBox 934×1200 at 1:1, so screen x = 1046 + svgx): column
lefts land at 1202 / 1408 / 1614, row tops at 156 / 362 / 568 / 774. All twelve inside the
frame.

**It clears the ~.2 fill-opacity floor for art over a graded still.** Measured per cell,
ghost ring (the 22px border of the `fill-opacity=".2"` cell) against its own local
background, and the `--fund` mark against the same background:

| | mean | min | max |
|---|---|---|---|
| Ghost-ring ΔY vs local bg | **+7.78** | +5.09 (c12, darkest corner) | +10.30 |
| Green mark ΔY vs local bg | **+19.72** | +15.28 | +23.37 |

Absolute: ring Y ≈ 37.4, mark Y ≈ 49.3, wall ≈ 30. The mark also separates by **chroma**,
not only luma: mean mark RGB (19, 59, 43) against a wall of (24, 33, 36), i.e. **G−R
+39.8**. The weakest cell is +5.1 ΔY, which reads, and the ghost grid is up from frame one
— at 68.10, before the cascade, **all twelve empty cells are visible**, so the frame says
TWELVE before it says PAID, as designed.

**s20 now states its count.** At 69.00 (mid-cascade) six marks are in and the remaining six
ghosts are legible; at 72.50 all twelve are filled. The `popEach` derives to exactly **one**
`chip` cue (§9), not twelve.

Contrast of the green `.huge` statement over this frame: **4.74:1** — the chapter's lowest,
and still clear of AA for both large (3:1) and normal (4.5:1) text.

---

## 7 · The s14→s15 CONTINUOUS ZOOM — one photograph, verified three ways

The risk named in the brief is real and specific: s15 is a 91.754% crop of s14's **source**
and both files were replaced in the same pass, so a wrong crop dissolves mid-hold to a
different picture with every check green. Three independent confirmations that it did not:

1. **Geometry.** `s15.jpg` is 1725×1142 against `s14.jpg` 1880×1245 → **0.917553** (spec
   0.91754). Aspect 1.51051 vs 1.50964. The crop is derived from the *new* s14, and the
   `.src` records the re-derivation.
2. **scdet.** Joint peak **0.063** — the **lowest of the twelve joints**, identical to
   attempt 1's value on the old pair. No cut is being made.
3. **Frame-to-frame difference across the joint (the decisive one).** Photograph-only MAD
   (text rows excluded), 30 fps, over 36.33–39.07:

       in-scene baseline (ken motion)   ~0.047-0.055 per frame
       dissolve window 37.667-38.100    mean 0.048, max 0.132 (one frame)
       inside the window it DIPS to     0.011-0.039  (two near-identical pictures)

   For scale, the same measurement at real dissolves: **s16→s17 mean 0.892 / max 2.031**,
   **s19→s20 mean 0.580 / max 1.253**. So the s14→s15 "dissolve" produces *less*
   frame-to-frame change than the Ken Burns move already running through it — it is
   arithmetically indistinguishable from in-scene motion. The declared HOLD is real.
   (The other declared hold, s17→s18, measures mean 0.137 / max 0.286 against an 0.083
   baseline — slightly higher only because s18 adds the `--fund` green tint.)

Read by eye across 32.00 / 34.50 / 36.50 / 37.40 / **37.66** / 37.90 / 38.20 / 38.60 /
41.00 / 44.20: the same dotted notebook, the same sharpened pencil and technical pen at the
same diagonal, growing steadily. **The hold reads as one continuous move on one
photograph.** The pencil is in frame, so s14/s15 is no longer a blank page.

---

## 8 · Joints — scdet peak, Δp90, and what each joint SHOWS

| Joint | t | scdet peak | Δp90 | Kind | What it shows |
|---|---|---|---|---|---|
| s9→s10  | 5.293  | 0.180 | +3.7  | dissolve | ₹5-coin stacks on wood → white desk lamp over paper stacks. No shared object; bridged by warm tungsten only. Two pictures. |
| s10→s11 | 11.553 | 0.300 | **+10.5** | dissolve | Night interior desk → exterior water tank on pale dusk sky. Interior→exterior, dark→light, nothing shared. Still the hardest visual break in the chapter. |
| s11→s12 | 17.682 | 0.138 | −2.4  | dissolve | Water tank → two taps on a wall. Same subject matter (water plumbing), wide→close, and now also close in luminance (55.1→52.7 vs −9.0 last pass). Reads as one argument stepping forward. |
| s12→s13 | 25.535 | 0.259 | −9.8  | dissolve | Wall taps → hands on an old brass hand-pump. Same object class, push to hands. Strongest continuity in the chapter, but the new s12 makes this the second-largest DROP. |
| s13→s14 | 31.246 | 0.215 | **+10.5** | dissolve | Hands with brass tap → dotted notebook with pencil and pen. The water metaphor ends and the abstraction begins — a deliberate chapter turn, still a hard break. |
| s14→s15 | 37.662 | **0.063** | −1.2 | **HOLD** | Same notebook, 91.755% derived crop. Lowest score in the chapter (§7). |
| s15→s16 | 44.732 | 0.123 | −5.0 | dissolve | Notebook → current-series ₹500 note with coin stacks. **Was −21.7; now −5.0**, the biggest single improvement at any joint. Object change is wanted here (rate → corpus). |
| s16→s17 | 50.077 | 0.243 | +1.7 | dissolve | ₹500 note and coins → adding-machine keys. No shared object; both close-up, hand-scale. Cash → arithmetic. Both scenes carry the string ₹10,00,000, so this is the double-paint worst case (§10). |
| s17→s18 | 55.422 | **0.099** | +1.1 | **HOLD** | Same adding machine, derived-crop push-in. Second lowest; reads as one continuous shot. |
| s18→s19 | 60.062 | 0.179 | **−11.4** | dissolve | Adding machine (green-tinted) → black phone on dark planks. **Now the chapter's largest luminance DROP** and the entry to the new trough. Both are hard, dark, man-made objects, so the picture-to-picture read is not bad; the −11.4 is. |
| s19→s20 | 66.609 | **0.391** | +4.5 | dissolve | Phone on planks → cool grey plaster wall with the drawn grid. Highest joint score in the chapter (was 0.546). Wood→plaster, object→field. |
| s20→s21 | 73.025 | 0.113 | +0.9 | dissolve | Cool smooth plaster → warm coursed brick. Wall→wall, as fin-assets declared. Both flat frontal surfaces at similar scale; it works, and the temperature shift carries the topic change. |

**⚠ scdet cannot rank these — confirmed a second time on this chapter.** Top in-scene
(non-joint) peaks:

    t=47.833  0.583   <- s16 countUp landing on ₹10,00,000
    t=75.000  0.543   <- s21 statement rise
    t=61.200  0.525   <- s19 statement rise
    t= 1.133  0.519   <- s9 statement rise
    t=25.000  0.465
    t=26.667  0.406
    t= 6.433  0.401

Joint peaks span **0.063–0.391**. **All twelve joints score below the top four in-scene
peaks, and the top three scores in the whole chapter are TEXT RISES and a countUp, not
cuts.** A gate that ranked joints by scdet would flag s16's number landing and pass
s10→s11. The two holds are the only joints scdet places correctly, and only because a hold
genuinely has no cut.

---

## 9 · Cue list — `tools/audio/cues.py` read-only diff

    python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch2

**Exit 0, empty stderr.** Both new behaviours it gained today were exercised and neither
disagrees with the build.

| | Generated | Shipped `assets/audio.json` |
|---|---|---|
| Cue count | 17 | 17 |
| Times | **identical** (all 17) | identical |
| `music` | `bed-resolve` | `bed-resolve` |
| transition / reveal / hero / tick / chip | 11 / 2 / 2 / 1 / 1 | 11 / 3 / 1 / 1 / 1 |
| Minimum gap | **1.100s** (floor `cue_min_gap_seconds` 0.8) | 1.100s, every gap ≥ 0.8 |
| `_dry` / `_hold` annotations | 7 `_dry` + 2 `_hold` | byte-identical |

**One difference, intentional and documented in the shipped file:** the derived `hero` at
35.736 (s14 `pop(#s14-num)`) is **downgraded to `reveal` by build.mjs** — storyboard §2
rings s16, s62 and s64 and no other rung, and cues.py cannot know which number lands. The
`_hero` key records it. Every other cue matches.

The **speech-anchored `pop()` cascade** reading is exercised by s20 and agrees: the single
`popEach("#s20 .mk", S.s20+1.75, 0.11, 0.40)` derives to exactly **one** `chip` at
**68.359** in both. Twelve `pop()` calls would have derived twelve chips 0.11s apart,
straight through the 0.8s floor — the build's stated reason for one `popEach` is confirmed
by the tool.

Both suppressed joints are right: s15 (37.662) and s18 (55.422) take no `transition`
because they are declared holds, and §7/§8 confirm from the encode that neither is a cut.

---

## 10 · Dissolve interiors — no double-paint

Sampled at **BOTH** `format.json` `qa.dissolve_sample_offsets` (**0.225** and **0.38**) at
**all twelve** joints — 24 frames, all read — plus a fine strip at
0.00/0.10/0.20/0.30/0.38/0.44/0.50/0.60 on **s16→s17**, the worst case, because both scenes
carry the string `₹10,00,000` and a double-paint would show as a doubled number.

The japanese-money-methods stacking-context defect is **NOT present**. The outgoing
`.stack` fades monotonically with its own scene and composites UNDER the incoming
background. Measured on the s16 number band (rows 430–620), pixels above Y 170:

    +0.000   25 334 px   (full)
    +0.100   24 952 px
    +0.200        5 px   band max 179
    +0.300        0 px   band max  95
    +0.380        0 px   band max 115, p99 52   <- faint ghost only
    +0.440        0 px
    +0.500        0 px   band settled at the incoming scene

Monotonic decay to zero, gone well before the overlap ends. At +0.38 the incoming kicker is
crisp and the outgoing headline is a faint fading ghost at every joint — visible in the
contact strip, and it is the same brief co-occupancy of the centred y that attempt 1 flagged
for fin-editor (inherent to a centred stack under a 0.45s dissolve, ~0.1s, faint). Raised
again as an observation for a ruling, not as a defect.

---

## 11 · Comma-descender clearance — measured on `.huge`, and why `.mega` is moot

**There is exactly ONE `.mega` element in this chapter** (`s14`'s `3.0%`) **and it has no
comma**, so `.arch-b .mega { padding-bottom: .11em }` at `assets/chapter-design.css:141`
has nothing to protect. Confirmed by grep: one `.mega`, twelve `.huge`. Per-column minimum
vertical clearance between the ink of one line and the ink of the line below, measured on
full-resolution frames from the mp4:

| Scene | String | Pair measured | **Min per-column clearance** | median |
|---|---|---|---|---|
| s16 | `₹10,00,000` (`.huge`) | number → foot | **28px** | 51px |
| s17 | `₹10,00,000 AT 3.0%` / `IS ₹30,000 A YEAR` (`.huge` 88px, two lines) | line 1 commas → line 2 caps | **12px** (at x=712) | 30px |
| s17 | — | line 2 → foot | 33px | 48px |
| s18 | `₹2,500` (`.huge`) | number → foot | **36px** | 49px |
| s14 | `3.0%` (`.mega` 300px, no comma) | mega → foot | 71px | 85px |

**No comma descender touches the glyph below it anywhere in the chapter.** The tightest case
is s17's two-line `.huge` at **12px** — clear, unchanged from attempt 1, and the number to
watch. The clearance ch3–7 actually depend on is `.huge`'s, which **no rule guarantees**:
the `.mega` fix is correct and applied but is not what is protecting these rungs. If a later
chapter promotes a comma'd figure to `.mega`, the fix carries it; if one raises `.huge` or
adds a digit to a two-line rung, nothing does. (Reference: en ch2 measured 26–27px on the
equivalent pair; hi ch2 measures 12px.)

---

## 12 · Headline contrast — settled frame, per scene

Ink vs local background in the tallest type band, WCAG contrast:

| Scene | contrast | Scene | contrast | Scene | contrast |
|---|---|---|---|---|---|
| s9  | 14.84:1 | s13 | 16.64:1 | s18 | 5.56:1 (green) |
| s10 | 17.13:1 | s14 | 7.85:1 (mega) | s19 | 16.20:1 |
| s11 | 7.07:1  | s15 | 8.00:1 | s20 | **4.74:1** (green, lowest) |
| s12 | 6.57:1  | s16 | 15.69:1 | s21 | 15.52:1 |
|     |         | s17 | 16.46:1 |     |         |

**Every band clears AA for large text (3:1) and for normal text (4.5:1).** Lowest is s20's
green statement over the grey wall at 4.74:1. `npm run check` independently reported 13/13
text checks passing AA on this build.

## 13 · Audio on the draft

| Measure | Value |
|---|---|
| Stream | aac, 48 kHz, stereo, 81.536s |
| **Sample peak** (`astats`) | **−3.80 dB** — limit is below −1 dBTP, PASS |
| **True peak** (`ebur128 peak=true`) | **−3.7 dBFS** |
| Integrated loudness | −22.9 LUFS (threshold −33.4) |
| LRA | 2.8 LU (low −25.5, high −22.7) |
| RMS level / RMS peak | −26.23 dB / −16.50 dB |
| Flat factor | 0.000 |
| Longest silence (`silencedetect n=-45dB:d=1.2`) | 1.397s at 65.590–66.986 |

Ten silences, all 1.212–1.397s, all at scene joints — consistent with MEDIUM's per-line
padding (tail 0.55 + lead_in 0.25) plus the 0.45s transition. No dead zone; every scene
carries VO. Music bed and SFX are not in the draft. **These figures are identical to
attempt 1**, which is the proof that the VO was not re-timed (see §5).

---

## 14 · Other things read from this encode

1. **s21's recess is present at 79.50 AND at 81.30** (0.23s before the chapter ends), not
   gone by 79.5s as fin-editor #10 recorded. The dark recess with one pale brick set proud
   at its foot is unambiguous in both frames. The photograph and its ken are unchanged from
   attempt 1, so the earlier reading was of the frame, not of a change. **Worth noting for
   the re-rule:** the two-line statement lands across the *upper* half of the recess, so the
   recess reads as the type's shadow box; the protruding brick below is fully clear.
2. **s16's photograph is verifiably real currency at full resolution.** `भारतीय रिज़र्व बैंक` and
   the modern ascending serial panel `6HP 962971` are legible, and no second note in frame
   repeats it. The prop-money file with the duplicated `ILR 176177` is gone.
3. **s19's phone is screen-off and lands directly behind the headline** — the black screen is
   the darkest region of the darkest frame and happens to be exactly where the two-line
   statement sits, so the type reads at 16.20:1. Legible, brand-free, currency-neutral. It
   is the picture, not the type, that is the §1 problem.
4. **s9 no longer repeats the ch4 trunk.** It is now ₹5-coin stacks on wood, so the
   cross-chapter object-repetition risk flagged in attempt 1 is retired at s9. (Two money
   still-lifes now sit seven scenes apart, s9 coins and s16 notes — declared by fin-assets.)
5. **The s14 cell of the contact sheet still shows no big number, and that is still honest.**
   s14's mega is anchored to the spoken «तीन परसेंट» and pops at 35.736 (start+4.49);
   `chapter_sheet.py` samples s14 at start+2.6 = 33.846. The mega does render — verified at
   36.50/36.80, 300px, 71px of clearance. Do not read the empty s14 cell as a missing number.
   The sheet handles s16 and s18 correctly (both sampled at start+4.5, after the countUps).

---

## Verdict

Mechanically the draft is clean on every axis measured: **2446/2446 frames**, CFR from
packet deltas with two delta values and no third, **0 black segments**, cue list matching
17/17 with the one documented downgrade, comma clearance holding with 12px at its tightest,
peak **−3.80 dB** sample / **−3.7 dBFS** true, AA contrast on all thirteen scenes. The three
build fixes all verified from the encode: **s18's ₹2,500 settles for 1.380s** (was 0.629s),
**s20's twelve cells render, clear the fill-opacity floor and state the count**, and the
**s14→s15 hold is one continuous move on one photograph.**

**The chapter does not lock, and the reason is §1.** The un-inversion is settled from the
encode and it went the other way: **s16 is 7th of 13 by p90, 4th by median, 7th by mean.**
s11 is still the brightest on all three measures, three further photographs sit between
s11 and s16, and the trough has moved to s19 — so both clauses of
`ground_and_payoff_legibility_2026-08-08` are still unmet. This is a photograph decision
(fin-assets' lever), not a build defect, so nothing here is a gate-two failure; it is the
measurement the CEO gate asked for, and the answer is no.
