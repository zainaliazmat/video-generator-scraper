---
summary: en ch1 draft re-render after the five-photograph swap. 1393 frames / 46.4333s at 30fps, exact; zero black segments; all five new photographs confirmed painting from encoded frames; the s4 Lottie still fires at +1.13. The open question is answered with a number — the chapter is cold because of the CHROME, not the photographs: only 9.3% of a photograph's R-B reaches the screen and the layer stack contributes a fixed -6.43 floor.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1 draft render, attempt 2 · fin-build-en-ch1-2.md · tools/format.json qa
stage: fin-render, cut en, chapter 1, attempt 2 (CHAPTER DRAFT mode)
---

# fin-render — passive-income-number · en · chapter 1 · attempt 2

**Mode: chapter draft (command §3b step 4).** No gate-two frame check, no dissolve
sampling at `qa.dissolve_sample_offsets`, no faster-whisper, no 1080p encode — all
of those are cut-level and run once, after every chapter is locked. Everything
below is measurement. Image *judgement* stays fin-editor's.

## Commands run (verbatim)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1.mp4 -q draft -f 30

python3 tools/chapter_sheet.py studio/videos/passive-income-number-en-ch1 \
        studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4 \
        -o studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30`
matches the final fps so this chapter's frame count sums with its siblings.
Render: 1m 21.8s wall, 1 worker, captureMode `beginframe`, exit 0.

## 1 · Structural numbers

| Quantity | Measured | Expected | Verdict |
|---|---|---|---|
| Frame count (`ffprobe -count_frames`) | **1393** | ceil(46.420 x 30) = 1393 | **exact** |
| `nb_frames` header | 1393 | 1393 | agrees with the decoded count |
| Video stream duration | **46.433333s** | 1393/30 = 46.43333 | exact |
| Container / audio duration | 46.442667s | — | +0.0093s AAC frame pad, benign |
| Declared root `data-duration` | 46.420s | timing.json | matches (ceil is the 0.0133s) |
| Frame rate | 30/1 CFR (`r_frame_rate` = `avg_frame_rate`) | 30 | ok |
| Resolution | 1920x1080 | 1920x1080 | ok |
| File size | 10,833,613 B (10.3 MB) | — | draft quality |
| Chapter offset | 0.000s | ch1 opens the cut | concatenates as-is |
| **Black segments** (`blackdetect d=0.05 pix_th=0.10`) | **0** | 0 | **ok** |
| Black frames (`blackframe amount=98 thresh=32`, looser cross-check) | **0** | — | ok |

Identical in every structural respect to attempt 1 (1393 / 46.4333 / 0 black),
which is the mechanical confirmation of fin-build's claim that no timing moved.
File is 208 KB smaller — five different photographs, same encoder settings.

## 2 · All five new photographs paint

Verified from **encoded frames**, not from snapshots and not from the fact that a
file loaded. One frame per scene pulled out of `DRAFT-ch1.mp4`, brightened
+0.20 / contrast 1.45 for inspection only, read at 960x540 against the source
files:

| | source file (md5) | what the ENCODED frame shows | verdict |
|---|---|---|---|
| s1 | `b4e0430…` | white phone, dead screen, warm bamboo, hard sunbeam | unchanged, paints |
| s2 | `9f62848…` | alarm clock on book stack, unmade bed | unchanged, paints |
| **s3** | `8fa18b3…` | **overhead speckled-terrazzo table, whole black-screen phone, black coffee, bud vase** | **NEW, paints** |
| **s4** | `9657c44…` | **same table tighter, phone centred and dominant, notification banner under it** | **NEW, paints** |
| **s5** | `a1f1ec9…` | **archery target, one arrow standing in it, red/gold/teal rings** | **NEW, paints** |
| **s6** | `7e98216…` | **grocery bags on a doorstep — bottle, pineapple, milk jug, sauce jar, oranges, brick + white door** | **NEW, paints** |
| s7 | `fcb2302…` | hands on a laptop keyboard, warn-red statement | unchanged, paints |
| **s8** | `a2c9638…` | **wooden ladder against a curved adobe/stucco wall, blue sky behind** | **NEW, paints** |

Eight distinct photographs, each matching its own source file. The
`image_per_scene`-satisfied-by-a-file-that-never-paints failure mode did not
occur.

**One method note, recorded because it failed.** I first tried to prove this
mechanically — high-pass NCC of each encoded frame against all eight sources,
expecting scene N to classify to source N. It returned |r| < 0.11 for every
pair, i.e. noise, and would have read as eight mismatches. The cause is my
geometry emulation, not the render: `.bg` is `inset:-8%` with `background-size:
cover` **and** a live ken transform, so the visible window is a moving sub-crop
that a static cover-crop guess does not reproduce (s3 in particular shows the
table as a large ellipse the full source never presents). The test was discarded
rather than reported. Reading the frames is the standard that holds here.

Two visible confirmations of fin-build's two edits, incidentally: s2's chip row
is right-aligned and the alarm clock is clear of it, and s3's phone has its
bottom edge **inside** the frame with table below it — `background-position:
center 70%` does what fin-build measured.

## 3 · The s4 Lottie still animates at +1.13

`playLottie(s4art, S.s4 + 1.13, 2.50)` — unchanged at line 295. Fire =
14.599 + 1.13 = **15.729s**. Stage `.v-lstage` unchanged at
`left:550 top:602 width:820 height:300`. Asset is 75 frames scrubbed over 2.50s
= 29.600 lottie-frames/s.

Method as attempt 1: per-frame luma difference
(`crop -> tblend=difference -> signalstats -> YAVG`) inside the exact stage box,
against two background-only controls that see only the plate push —
CTRL_top `crop=820:300:550:150`, CTRL_left `crop=300:300:0:700`.

| Window | STAGE YAVG | CTRL_top | CTRL_left | Reading |
|---|---|---|---|---|
| 15.43 – 15.90 (pre-fire) | 0.017 – 0.046 | 0.036 – 0.058 | 0.030 – 0.058 | **below** the controls — nothing drawn |
| **15.933 (onset)** | 0.046 -> **1.652** | 0.036 | 0.036 | **45.8x** the control floor, isolated to the box |
| 15.93 – 16.53 (draw + jitter 1) | 0.62 – 1.65 sustained | floor | floor | 15x–39x controls throughout |
| 16.57 – 17.30 (settle / hold) | decays 0.30 -> 0.026 | floor | floor | banner assembled, still on screen |
| 17.43 – 17.73 (jitter 2) | 0.24 – 2.40 | (statement rise at 17.367) | floor | matches asset frames 51–59 |
| 17.77 – 18.57 (tail) | 0.009 – 0.065 | floor | floor | banner held, no exit |

**34 frames of motion** above 0.30 inside the box between 15.40 and 18.60, with
the controls at their 0.03–0.06 floor. It draws and it moves.

Onset lands at **15.933**, i.e. **lottie frame 6.0** — the asset's own authored
5-frame park (notification layer held at y222 with the bloom at opacity 0 for
frames 0–5), identical to attempt 1's finding. The timeline fires on time; the
artwork holds first. No action needed.

The 17.367–17.40 spike on CTRL_top is the `s4-stmt` cue at 17.349 rising above
the stage — it independently anchors the timebase to within one frame, as it did
last round.

## 4 · THE OPEN QUESTION — measured temperature of the ENCODED frames

fin-build reported four off-wood replacements at source R-B of −6.0 / −4.3 /
−1.8 / −0.1 against a ~+40 guideline, and judged `--f1` at `.field` opacity .38
too weak to compensate. **The source-file estimate is the wrong instrument, and
the encode says the diagnosis is aimed at the wrong layer.**

### 4a · Per-scene, measured off the encode

Mean over 8 frames spanning each scene's body (dissolve excluded), 960x540,
whole frame. Median is reported because it is robust to the white type; `settle`
is the single frame the contact sheet shows.

| scene | window | **mean R-B** | median R-B | p10 | p90 | mean luma | settle |
|---|---|---|---|---|---|---|---|
| s1 | 0.45–3.54 | **+0.76** | −1.00 | −8 | +9 | 31.8 | +1.18 |
| s2 | 3.99–9.25 | **−6.42** | −8.00 | −11 | 0 | 25.2 | −6.42 |
| **s3** | 9.70–14.60 | **−7.17** | −8.00 | −11 | −4 | 35.9 | −6.98 |
| **s4** | 15.05–21.56 | **−7.58** | −8.00 | −13 | 0 | 32.7 | −8.64 |
| **s5** | 22.01–25.55 | **−3.59** | +4.00 | −29 | +13 | 29.1 | −3.64 |
| **s6** | 26.00–31.26 | **−6.50** | −8.00 | −13 | +1 | 32.4 | −7.72 |
| s7 | 31.71–38.15 | **+3.59** | 0.00 | −10 | +14 | 26.2 | +5.39 |
| **s8** | 38.60–44.92 | **−3.77** | −3.00 | −11 | +2 | 33.5 | −3.93 |

Chapter mean **−3.84**. Every scene but s1 and s7 is negative, and s7 is positive
only because it carries `--tint: rgba(239,68,68,.12)`.

Delta against the attempt-1 draft (measured on that file before it was
overwritten), so the swap can be priced:

| | s1 | s2 | **s3** | **s4** | **s5** | **s6** | s7 | **s8** |
|---|---|---|---|---|---|---|---|---|
| attempt 1 | +0.76 | −5.25 | +3.09 | +0.59 | +0.75 | +6.77 | +3.17 | −7.85 |
| attempt 2 | +0.76 | −6.42 | −7.17 | −7.58 | −3.59 | −6.50 | +3.59 | −3.77 |
| delta | 0.00 | −1.17 | **−10.26** | **−8.17** | **−4.34** | **−13.27** | +0.42 | **+4.08** |

s1 is identical to two decimal places, which is the control: the pipeline did not
move, only the photographs did. The swap cooled s3/s4/s5/s6 and **warmed** s8 by
+4.08 — the opposite of what its source R-B (+25.37, the warmest of the five)
would predict, because s8 trades a warm mid-luma subject for a warm mass plus a
large cool sky.

### 4b · Source R-B does not survive, and here is the coefficient

| scene | source R-B | after `.bg` filter alone | **encoded** |
|---|---|---|---|
| s1 | **+73.53** | +31.00 | **+0.76** |
| s2 | +17.21 | +7.26 | −6.42 |
| s3 | +1.48 | +0.63 | −7.17 |
| s4 | +1.13 | +0.48 | −7.58 |
| s5 | −2.01 | −0.85 | −3.59 |
| s6 | −0.44 | −0.19 | −6.50 |
| s7 | +1.63 | +0.69 | +3.59 |
| s8 | +25.37 | +10.70 | −3.77 |

(My source numbers reproduce fin-assets' independently: s8 measured +25.37 here
against their logged +25.7.)

`.bg { filter: grayscale(.32) brightness(.62) contrast(1.05) }` alone multiplies
source R-B by exactly **(1 − .32) x .62 = 0.4216** — s1's +73.53 becomes +31.00.
Then the overlay stack eats the rest.

**Measured pass-through, no model — from scene pairs:**

| pair | source ΔR-B | encoded ΔR-B | pass-through |
|---|---|---|---|
| s1 vs s3 | +72.05 | +7.93 | **11.0%** |
| s1 vs s4 | +72.40 | +8.34 | **11.5%** |
| s8 vs s6 | +25.81 | +2.73 | **10.6%** |
| s8 vs s3 | +23.89 | +3.40 | **14.2%** |
| s2 vs s4 | +16.08 | +1.16 | **7.2%** |

In every pair the `--f1` difference works *against* the warmer photograph, so
these are if anything under-estimates. Least squares over the seven scenes
without a `--tint`:

```
encoded R-B = 0.0927 x source R-B  −  6.43        residual std 1.43
```

**9.3% of a photograph's colour temperature reaches the screen, and the layer
stack adds a fixed −6.43.** A photograph would need a source R-B of about **+69**
to reach neutral on screen, and about **+500** to hit the +40 guideline. The
guideline as written is not achievable through the photograph under this grade.

### 4c · Why — read straight out of the CSS, not modelled

`--bg` is `#0d1017` = R13 G16 B23, i.e. **R-B = −10**, and it is:

- **all four `.scrim` layers** (`rgba(13, 16, 23, .46 / .14→.58 / .40→.10→.52)`);
- **the `.band` on s4** (`rgba(13,16,23,0) → .45 → .72` over the bottom 54%);
- **the far stop of `.field`** — `linear-gradient(158deg, var(--f1) 0%, var(--bg) 64%)`,
  so past 64% of the diagonal the "warm ground" *is* the cool ink.

fin-build's read that `--f1` on s3/s4 is invisible is correct, but the cause is
not only the .38 opacity. `#241d15` (R-B +15) occupies one corner of a gradient
whose other 36%+ is R-B −10, at 38% opacity, underneath four ink scrims.

Three of the eight `--f1` values are themselves **cool**: s1 `#161f2b` (−21),
s5 `#1c2027` (−11), s2 `#1a1e24` (−10). s8 `#1f1e1c` is +3, effectively neutral.

### 4d · Lever pricing — MODELLED, flagged as such

I built an analytic composite of the shipped stack (`.bg` filter → `.field` at
.38 → `.band` where present → the four `.scrim` layers → `--tint`) and validated
it against the measured encode: it lands within **±1.0 R-B on seven of eight
scenes** (s5 −4.03 and s7 −4.13 are the two misses, both from ken crop and radial
placement approximations). Good enough to rank levers, not to quote as fact.

**Raising `.has-photo .field` opacity makes the chapter COLDER, not warmer:**

| `.field` opacity | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|
| **0.38 (shipped)** | −0.03 | −5.61 | −6.23 | −6.85 | −7.62 | −6.18 | −0.54 | −4.27 |
| 0.50 | −2.20 | −6.46 | −6.41 | −6.95 | −8.10 | −6.22 | −0.62 | −5.09 |
| 0.65 | −4.91 | −7.52 | −6.64 | −7.07 | −8.71 | −6.27 | −0.72 | −6.12 |
| 0.80 | −7.62 | −8.59 | −6.87 | −7.19 | −9.31 | −6.32 | −0.81 | −7.16 |
| 1.00 | −11.24 | −10.00 | −7.18 | −7.35 | −10.11 | −6.39 | −0.94 | −8.53 |

It buys s3/s4/s6 nothing (−0.2 to −1.0) and costs s1 eleven units, because the
gradient it strengthens is 64%-to-100% pure `--bg`. **The half of fin-build's
proposed fix that raises `.field` opacity is backwards.**

Raising `--f1` alone, even to opacity 1.0, cannot clear the floor:

| `--f1` at opacity 1.00 | s3 | s4 | s6 |
|---|---|---|---|
| `#241d15` (R-B +15, shipped) | −7.18 | −7.35 | −7.18 |
| `#3a2a18` (R-B +34) | −5.04 | −5.33 | −5.04 |
| `#5a3a1c` (R-B +62) | −1.88 | −2.37 | −1.88 |

The one lever with real authority is the ink itself, because it is every scrim
layer:

| `--bg` R-B | s3 | s4 | s6 |
|---|---|---|---|
| **−10 `#0d1017` (shipped)** | −6.23 | −6.85 | −6.18 |
| −2 `#111013` | −0.57 | −0.74 | −0.52 |
| +4 `#141010` | +3.67 | +3.85 | +3.72 |
| +10 `#17100d` | +7.92 | +8.43 | +7.97 |

That is a **global design token** in `blockframe.css` shared by every cut on the
channel, so it is a system decision, not a chapter one, and not mine. Reported,
not touched. I changed no file in the project.

## 5 · Contact sheet

`renders/SHEET-ch1.jpg` — 8 cells, one per scene, plus `SHEET-ch1.json` for the
orchestrator's numbered cross-chapter PNG. Sample times all `data-start` + 2.600
(`SETTLE`): 2.600 / 6.143 / 11.854 / 17.199 / 24.164 / 28.151 / 33.862 / 40.749.
Chapter 1 renders no `countUp`, so `SETTLE_COUNTUP` (4.5) never engaged.
s4's 17.199 lands inside the Lottie's settled hold, so that cell shows the banner
fully formed.

**Housekeeping:** `renders/SHEET.jpg` and `renders/SHEET.json` (04:42, attempt 1,
default filenames) are still in the directory and are now **stale**. They are not
inputs to anything; delete or ignore. The live artifacts are the `-ch1` pair.

## 6 · Not done in this mode, by design

Gate-two frame check, dissolve sampling at both `qa.dissolve_sample_offsets`
[0.225, 0.38], faster-whisper re-transcription, VAD onset drift with
`qa.vad_onset_latency_seconds` (0.101) subtracted, true-peak / loudnorm on the
master, runtime vs `timing.json` total for the whole cut.

## Artifacts

- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.json`
