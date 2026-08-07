---
summary: Chapter 2 draft render + contact sheet for passive-income-number-hi. 2328 frames / 77.600s at 30fps. The s13->s14 continuous zoom is confirmed invisible by scdet and by page-luminance continuity; no corpus figure appears without its rate; two real defects found by eye that every static check passed — a foot/mega collision on s15 and an invisible funnel on s16.
updated: 2026-08-07
source: renders/DRAFT-ch2.mp4 (encoded frames), ffprobe/ffmpeg signalstats+scdet+ssim, tools/chapter_sheet.py
---

# fin-render · passive-income-number · hi · CHAPTER 2 · attempt 1

Mode: **chapter draft** (§3b step 4). No gate two, no encode, no QA of a master.
Build treated as complete but UNREVIEWED — this is its first eye.

## Commands run

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch2.mp4 -q draft -f 30
python3 tools/chapter_sheet.py studio/videos/passive-income-number-hi-ch2 \
        studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 \
        -o studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30` as required.

## Artifacts

| Path | What |
|---|---|
| `studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4` | 18.9 MB, h264, 1920x1080, 30/1 |
| `studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2.jpg` | 13 cells, 4 cols |
| `studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2.json` | index the orchestrator's cross-chapter PNG reads |

## Measured numbers

| Metric | Value |
|---|---|
| Frame count (`-count_frames`) | **2328** |
| Video stream duration | 77.600 s |
| Container duration | 77.610667 s |
| Frame rate | 30/1 |
| Render wall time | 2 m 40.3 s |
| Declared chapter root (`index.html` `data-duration`) | 77.571 s |
| Declared length in frames at 30fps | 77.571 x 30 = **2327.13** |
| Delta | +0.87 frame / +0.029 s |
| Audio (VO only, pre-mix) | Peak −5.25 dB, RMS −25.29 dB, flat factor 0 |
| `blackdetect` d=0.1 pic_th=0.97 | **0** segments |

### Is the frame count exact against the declared length? No — and it cannot be.

77.571 s is not a whole number of frames at 30fps. The renderer takes `ceil(2327.13) = 2328`,
so the draft runs 0.029 s long. **This is harmless for the master and dangerous only for the
preview path.** `tools/cut_assemble.py` writes ONE rebased `index.html` — the seven chapters
become a single composition, not a video concat, so the per-chapter ceil never accumulates.
`tools/chapter_preview.py` DOES stream-concat, and its own docstring already records that up to
eight frames of rounding accumulate there. Nothing to fix; recorded so the next chapter's
identical +0.9-frame delta is not re-investigated.

## Check 1 — the s13 -> s14 continuous zoom: **PASS**

Construction: `plateKen("#s13-bg", 30.384, 5.998, 1.000, 1.090)` then
`plateKen("#s14-bg", 36.382, 8.036, 1.000, 1.065)` on a 91.74% derived crop.

**Crop geometry is exact.** s13.jpg 1880x1249, s14.jpg 1725x1146.
1725/1880 = 0.91755, 1146/1249 = 0.91753 — both the declared 1/1.09, and the two files share an
aspect ratio to 4 decimal places, so `background-size: cover` maps them onto the identical
displayed rect and the centres coincide.
Full-res SSIM of s13's centre crop against s14 = 0.659, which looks alarming and is not: at 1/4
linear scale (high-frequency JPEG + resample noise removed) SSIM = **0.986**. s14 is sharper than
a crop of s13 would be because it was re-cropped from the higher-res original (705 KB vs 353 KB) —
that is the correct way to build this, not a defect.

**The joint is invisible in the encode.** `scdet` per-frame scores:

| Boundary | What it is | Peak score in the 0.45 s overlap |
|---|---|---|
| s12 -> s13 @ 30.384 | normal dissolve, two different photos | **0.184** |
| s14 -> s15 @ 44.418 | normal dissolve, two different photos | **0.214** |
| **s13 -> s14 @ 36.382** | the hold | **0.073** |

Mid-scene baseline is 0.005–0.020. The 0.073 at the joint is entirely the TEXT cross-dissolve
(it lands at 36.4–36.7, where the s13 stack fades and the s14 kicker rises) — the image layer
contributes nothing measurable. One third the delta of a real photo boundary.

**No tone step.** Luminance of a text-free strip of the notebook page (crop 700x220 at 500,80):

| t | 36.100 | 36.300 | 36.900 | 37.200 |
|---|---|---|---|---|
| YAVG | 59.61 | 59.63 | 59.75 | 59.82 |

Monotonic 0.2-unit drift over 1.1 s across the joint at 36.382. No step, no reset.

**Eye check.** Frames at 32.000 / 35.000 / 36.300 / 36.607 / 36.762 / 36.900 / 38.000 / 43.500.
The notebook's top-left spiral corner walks from ~(320,175) at t=32 to ~(230,130) at t=43.5 —
one continuous tightening. No jump, no reset, and **no self-dissolve**: the picture never returns
to a wider framing. The 36.607 (midpoint) frame and the 36.900 frame are the same framing to the
eye, which is exactly what the construction is for.

## Check 2 — the corpus/rate rule: **PASS, with one figure worth naming**

Read from the encoded frames, not from the assert.

| Frame | Corpus on screen | Rate in the SAME frame |
|---|---|---|
| s15 @ 48.1 | `₹10,00,000` | `at a 3.0% withdrawal rate` (above) AND `ILLUSTRATIVE · 3.0% of the corpus, divided by 12 — arithmetic, not a forecast` (below) |
| s16 @ 54.3 | `₹10,00,000` | `3.0% of` is the same line; foot repeats `withdrawal rate 3.0%` |

**No corpus figure appears without its rate.** The count-up on s15 (`countUp` 0 -> 1000000 over
46.318–47.518) passes through intermediate values — the sheet caught it at `₹8,36,874` — and the
`at a 3.0% withdrawal rate` line is already up at +1.10, i.e. before the count starts, so even the
transient values carry the rate. Final value lands on `₹10,00,000` correctly.

**Named for the editor, outside the rule as written:** `s17` renders the kicker `WHAT ₹2,500 BUYS`
with no rate and no ILLUSTRATIVE marker anywhere in the frame. ₹2,500 is not a corpus figure — the
build's `CORPUS` regex covers only ₹9,00,000 … ₹1,00,00,000, so the assert correctly passes — but
it IS the output of the 3.0% assumption, presented bare on its own frame. This is the same shape as
the two failures fin-audit found on the shipped cut ("both OUTSIDE the rung ladder — which is where
it breaks, because that is where nobody checks"). Not a build failure; an editorial call.

## Check 3 — the grade against ch1's flat-charcoal-slab failure

Per-scene luminance from the encoded frames (`signalstats`). YLOW/YHIGH are the 10th/90th
percentiles; **spread = YHIGH − YLOW is the flatness measure** — ch1's failed frames were high YAVG
with a narrow spread. YMAX is contaminated by white/orange type where type is present.

| Scene | t | YMIN | YLOW | YAVG | YHIGH | YMAX | spread |
|---|---|---|---|---|---|---|---|
| s8 strongbox | 2.60 | 0 | 28 | 45.3 | 54 | 247 | 26 |
| s9 card index | 7.58 | 7 | 37 | 47.6 | 50 | 249 | **13** |
| s10 calendar | 14.13 | 7 | 49 | 61.7 | 66 | 247 | 17 |
| s11a clay pots | 19.60 | 0 | 31 | 42.9 | 50 | 250 | 19 |
| s11b hand+notes | 23.10 | 3 | 31 | 40.8 | 48 | 249 | 17 |
| s12 tap+bucket | 28.19 | 4 | 33 | 48.1 | 55 | 250 | 22 |
| s13 notebook | 32.98 | 12 | 31 | 50.7 | 67 | 175 | **36** |
| s14 notebook tight | 38.98 | 13 | 31 | 52.8 | 66 | 183 | **35** |
| s15 cash box | 47.02 | 0 | 29 | 52.3 | 55 | 255 | 26 |
| s16 graph paper | 53.25 | 8 | 47 | 57.2 | 66 | 172 | 19 |
| s17 ethernet | 59.67 | 1 | 27 | 40.0 | 53 | 250 | 26 |
| s18 filed paper | 65.14 | 0 | 38 | 49.9 | 58 | 175 | 20 |
| s19 bricks | 71.82 | 0 | 32 | 43.6 | 48 | 255 | 16 |

**Reads as a grey panel rather than an object — one frame: `s16`.** YAVG 57.2 with a 19-unit
spread and the high-key signature of ch1's three failures. The source is
`squared graph paper grid texture close up@pexels` — a uniformly-lit flat texture, so even
before the grade it is a panel, and `grayscale(.32) brightness(.62)` finishes it. You cannot tell
a photograph is present. The build's own note concedes this ("the photograph (flat graph paper)
states nothing"), which is the near-miss `format.json layout.image_relevance` explicitly forbids:
*"When a slot cannot be photographed, change the SOURCE or draw it — never accept a near-miss."*
Compounded by `art-lift` painting a dark plate rect over pale grey — the frame reads as a UI panel
on a UI background, the only frame in the chapter that does not read as film.

`s10` (calendar, YAVG 61.7 / spread 17) carries the same numeric signature and **passes on the
eye**: the numerals and three red pins give it real structure and it reads unmistakably as a wall
calendar. Numbers alone would have failed it; looking is what cleared it.

**Nothing has crushed.** The darkest frames are s17 (YAVG 40.0, YLOW 27) and s11b (40.8). On s17
roughly the bottom third is a black void with no recoverable detail, but the RJ45 plug and cable
read clearly in the upper half, so the object survives — it is at the edge, not over it. s19
(bricks, YAVG 43.6, YMIN 0) holds its texture across the whole frame. No per-scene brightness
override is needed anywhere in this chapter.

## Defects found by eye that every static check passed

`hyperframes check` reported 11/11 text checks at WCAG AA and 0 lint errors. Neither of these is a
contrast or lint condition, which is the point.

### D1 — `s15`: the foot line collides with the mega numeral. REAL, and it is the chapter's hero frame.

At native resolution the comma descenders of `₹10,00,000` pass **through** the foot line
`ILLUSTRATIVE · 3.0% of the corpus, divided by 12 — arithmetic, not a forecast`: the first comma
strikes the `f` of `of`, the second strikes `ari` of `arithmetic`. Both strings stay readable, so
no automated check can see it, but it is a collision on the single most important frame in the
chapter — the rung-one corpus reveal.

`s13` uses the same variant-B stack (kicker / mega / foot) and does NOT collide — its `.mega`
is `3.0%`, which has no comma descenders. The trigger is the comma, so this will recur on every
lakh/crore rung in chapters 3–7, not just here. Fix the mega-to-foot spacing (or the `.mega`
line-height), not this one scene.

### D2 — `s16`: the funnel is invisible, so the chapter's one drawn mechanism does not connect.

`#s16-afunnel` is `points="719,244 740,244 740,330 40,330"` at `fill-opacity=".18"`. On the encoded
frame it is gone. What survives is the corpus bar (`.30`, reads as a pale grey rect), the 3% sliver
at its right end (full opacity, correct — 21/700 = 3.00%, the truth bar is met), and the twelve
ticks (full opacity). Without the funnel the drawing reads as **two unrelated objects**: a grey bar
with a green tip, and a row of twelve green bars. The causal sentence it exists to state — *that
sliver, split twelve ways* — is not on screen.

This is the documented gotcha, one notch below where it was set:
`format.json chapter_design.gotchas` — *"Over a graded still, thin outline scaffolding is not on
screen … draw with SOLID FILLS … and let the ghost/track shapes be filled rects at ~.2 rather than
outlines."* The funnel IS a solid fill, at .18 — under the ~.2 floor. Raise it (or give the funnel
the same treatment as the ticks).

## Non-defects — sheet sampling artifacts, do not chase

`tools/chapter_sheet.py` samples every non-Lottie scene at start + 2.6 s. Two cells will read as
broken and are not:

* **`s13` cell shows no `3.0%`.** `pop("#s13-num", 34.061)` is scene start + 3.677 — the number is
  anchored to its own spoken word per storyboard §5 variant B, so it legitimately arrives 1.1 s
  after the sheet's sample. Verified present and correct at t=34.884.
* **`s15` cell shows `₹8,36,874` and no foot.** Mid `countUp` (46.318 -> 47.518) and 0.1 s before
  `fade("#s15-foot", 47.118)`. Verified at t=48.100: `₹10,00,000` with both rate lines up.

Design note, not a defect: s13 holds a kicker and a foot with an empty mega slot for 2.58 s
(31.484 -> 34.061). Deliberate — the number lands on the spoken word — but it is the longest
hole in the chapter and it is what the sheet cell shows the reviewer.

## Cross-dissolve boundary forensics (the japanese-money-methods-hi defect)

`.scene { isolation: isolate }` is present in `assets/blockframe.css`. Verified on the encode
rather than in CSS: four boundaries sampled at `qa.dissolve_sample_offsets[1]` = start + 0.38,
which is the only window where both scenes' text can be up.

| Boundary | t | Result |
|---|---|---|
| s8 -> s9 | 5.360 | incoming `THE NAME` crisp, outgoing `How saved money pays a monthly amount` a faint ghost UNDER it |
| s13 -> s14 | 36.762 | incoming `A CHOICE, NOT A FORECAST` crisp, outgoing `THE WORKING NUMBER` / `3.0%` ghosted under |
| s15 -> s16 | 51.032 | incoming `THE SUM` crisp, outgoing `₹10,00,000` ghosted under |
| s17 -> s18 | 62.924 | incoming `ALL TWELVE MONTHS` crisp, outgoing `The phone recharge…` ghosted under |

Correct z-order at every sample. No double-paint.

## What I did not do

No gate-two frame set, no encode, no faster-whisper pass, no VO-drift measurement, no
loudnorm/dBTP read. All of that belongs to the full-cut render, not the chapter loop. The audio
figures above are the raw VO track only — `assets/audio.json` (23 cues, bed `bed-resolve`) is a
post-mix step and is not in this draft.
