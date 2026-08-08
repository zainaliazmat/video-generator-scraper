---
summary: en ch1 draft re-render after fin-build's three fix-pass edits. 1393 frames / 46.4333s at 30fps exact, zero black segments, all 8 scenes painting. All three changes confirmed on the ENCODE — the s3->s4 matched-frame hold measures a 0.313 peak frame-delta against 3.016 and 2.006 at the real boundaries either side (and 0.056 scdet against 0.202-0.446), with a monotone 0.13 max luminance step and one phone / one mug / one vase at 14.900; s6's cascade draws progressively with a stagger of exactly 0.600s, completing at +3.116; s5's type clears the bullseye by 83-125px. The s4 Lottie still fires at +1.13 and the banner now straddles the phone.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1 draft render, attempt 3 · fin-build-en-ch1-3.md · editor-en-ch1-2.md · tools/format.json qa
stage: fin-render, cut en, chapter 1, attempt 3 (CHAPTER DRAFT mode)
---

# fin-render — passive-income-number · en · chapter 1 · attempt 3

**Mode: chapter draft (§3b step 4).** No gate-two frame check, no dissolve sampling
at `qa.dissolve_sample_offsets`, no faster-whisper, no VAD drift, no true-peak, no
1080p encode — all cut-level, run once after every chapter is locked. Everything
below is measurement. Image *judgement* stays fin-editor's; I did not judge the
photographs.

## Commands run (verbatim)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1.mp4 -q draft -f 30

python3 tools/chapter_sheet.py studio/videos/passive-income-number-en-ch1 \
        studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4 \
        -o studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30`
matches the final fps so this chapter's frame count sums with its siblings.
Render: **1m 24.9s wall, 1 worker, captureMode `beginframe`, exit 0, 0 errors,
0 warnings** in the render log.

`assets/audio.json` md5 `e411096987b8fe28d671687f8eaf2739` — unchanged, as stated
in the handoff. Nothing I did touched any file in the project.

## 1 · Structural numbers

| Quantity | Measured | Expected | Verdict |
|---|---|---|---|
| Frame count (`ffprobe -count_frames`) | **1393** | ceil(46.420 x 30) = 1393 | **exact** |
| `nb_frames` header | 1393 | 1393 | agrees with the decoded count |
| Video stream duration | **46.433333s** | 1393/30 = 46.43333 | exact |
| Container / audio duration | 46.442667s | — | +0.0093s AAC frame pad, benign |
| Frame rate | 30/1 CFR (`r_frame_rate` = `avg_frame_rate`) | 30 | ok |
| Resolution | 1920x1080 | 1920x1080 | ok |
| Audio | aac 48000 Hz stereo, 46.442667s | — | present |
| File size | 10,909,029 B (10.4 MB) | — | draft quality |
| Chapter offset | 0.000s | ch1 opens the cut | concatenates as-is |
| **Black segments** (`blackdetect d=0.05 pix_th=0.10`) | **0** | 0 | **ok** |
| Black frames (`blackframe amount=98 thresh=32`) | **0** | — | ok |

Identical structurally to attempts 1 and 2 (1393 / 46.4333 / 0 black) — the
mechanical confirmation that no `data-start` moved. File is +75 KB over attempt 2,
which is the drawn tick row and the new s4 crop, same encoder settings.

**All 8 scenes paint**, eight cells on the contact sheet, each carrying its
photograph and its type. s3 and s4 are deliberately the same photograph — that IS
the fix, not a duplicate.

`url()` audit of `index.html`: `s3.jpg` appears **twice** (s3 and s4), `s4.jpg`
appears **zero** times outside one prose comment. The hold is one file by
construction, exactly as fin-build claimed.

---

## 2 · CHANGE 1 — the s3 -> s4 matched-frame hold at 14.599

Confirmed independently, by the method hi ch2 used for its continuous zoom:
**scdet at the joint versus the real photo boundaries either side, plus a
luminance-step check**, plus fin-build's own frame-delta metric re-run on the
encode rather than on snapshots. Four instruments, one answer.

### 2a · scdet — photograph-only crop (x1650-1900, y60-380)

| joint | start | **scdet max** | scdet mean |
|---|---|---|---|
| s1 -> s2 | 3.543 | 0.409 | 0.065 |
| s2 -> s3 | 9.254 | **0.446** | 0.167 |
| **s3 -> s4 (the HOLD)** | 14.599 | **0.056** | **0.014** |
| s4 -> s5 | 21.564 | **0.352** | 0.118 |
| s5 -> s6 | 25.551 | 0.202 | 0.086 |
| s6 -> s7 | 31.262 | 0.282 | 0.148 |
| s7 -> s8 | 38.149 | 0.309 | 0.113 |

The hold scores **0.056** against a real-boundary range of **0.202-0.446** —
**3.6x to 8.0x lower**, and **8.0x / 6.3x** below its own two neighbours. It is
also below the mid-scene ambient of s4 itself (0.184), i.e. the joint is quieter
than the push that runs through it.

### 2b · Consecutive-frame delta — fin-build's own region and metric, on the encode

| joint | start | **peak delta** | ambient pre | ambient post |
|---|---|---|---|---|
| s1 -> s2 | 3.543 | 1.387 | 0.111 | 0.075 |
| s2 -> s3 | 9.254 | **3.016** | 0.020 | 0.170 |
| **s3 -> s4 (the HOLD)** | 14.599 | **0.313** | 0.165 | 0.272 |
| s4 -> s5 | 21.564 | **2.006** | 0.275 | 0.123 |
| s5 -> s6 | 25.551 | 1.840 | 0.204 | 0.307 |
| s6 -> s7 | 31.262 | 2.859 | 0.220 | 0.206 |
| s7 -> s8 | 38.149 | 2.465 | 0.189 | 0.060 |

The hold's peak of **0.313** sits *between* its own ambient either side (0.165 and
0.272). There is no event at 14.599 in the photograph at all. Real boundaries run
**1.387-3.016**, i.e. **4.4x to 9.7x** higher; the two neighbours are **3.016** and
**2.006**, i.e. **9.6x** and **6.4x**.

fin-build measured 0.81 against 5.29 on snapshot PNGs; I measure 0.313 against
3.016 / 2.006 on encoded YUV. Different absolute scale, same structure, and my
ratio is if anything the stronger of the two. **Independently confirmed.**

### 2c · Luminance step

Per-frame `YAVG` in the same photograph-only region through the 0.45s overlap:

| joint | max per-frame ΔY | YAVG before -> after |
|---|---|---|
| s2 -> s3 (real) | **2.90** | 31.4 -> 51.7 (**+20.4**) |
| **s3 -> s4 (HOLD)** | **0.13** | 47.5 -> 46.1 (**−1.4**) |
| s4 -> s5 (real) | 0.64 in this region; **3.88** in a second region (x60-360) | 65.7 -> 40.2 (**−25.5**) |

The hold's frame-by-frame trace is a smooth monotone ramp with **no step anywhere**:

```
14.500  47.38                14.833  47.06  Δ−0.06
14.567  47.31  Δ−0.03        14.900  46.84  Δ−0.09
14.633  47.24  Δ−0.03        14.967  46.62  Δ−0.13
14.700  47.22  Δ−0.01        15.067  46.40  Δ−0.04
14.767  47.17  Δ−0.03        15.167  46.19  Δ−0.08
```

−1.19 units over 0.67s, max single-frame Δ **0.13**. That is the `plateKen`
1.08->1.30 push and nothing else. The s2->s3 control by contrast steps +20.4 units
with Δ up to 2.90, and the step begins at **+0.046** and ends at **+0.446** —
confined exactly to the 0.45s overlap, which is what a real dissolve looks like in
this instrument.

### 2d · Read with eyes, at the editor's own instant

**14.900 (frame 447), the peak of the editor's double exposure: ONE phone, ONE mug,
ONE vase.** s3's "Money is deposited." ghosting out, s4's `brule` fading in. Nothing
else changes.

14.500 / 14.900 / 15.200 read as one unchanging composition under a continuous
push — same vase top-centre, same mug top-right, same phone centre — with only the
type crossfading (centred "BEFORE NOON / Money is deposited." out, top-left
"ONE BUZZ" + the rule in).

**The instrument is not blind:** the control frame at **9.467** (s2->s3, +0.213)
plainly shows both photographs superimposed — alarm clock, book stack and bed on
top of the terrazzo table, phone, mug and vase. When there is a double exposure this
method shows it. At 14.900 there is not one.

**Blocker cleared.**

---

## 3 · CHANGE 2 — s6's drawn count animates in the encode

Not "the SVGs are present" — measured frame by frame as white-ink pixel count per
cell region on the encoded video.

### 3a · The cell cascade

| cell | glyph | first ink | cue | measured stagger |
|---|---|---|---|---|
| 1 Groceries | grocery-bag.svg | **26.733** | 26.651 | — |
| 2 Gas and the car | fuel-pump.svg | **27.333** | 27.251 | **0.600** |
| 3 Rent or the mortgage | house-door.svg | **27.933** | 27.851 | **0.600** |

Stagger measured at **exactly 0.600s twice**, matching the authored
`popEach(..., 0.60, 0.45)`.

### 3b · The tick draws — progressive, not switched on

Measured against the empty-box baseline (the checkbox rect arrives with the cell
pop; the checkmark is the +683 to +723 ink on top of it):

| tick | baseline -> full | draw starts | completes | visible draw |
|---|---|---|---|---|
| 1 | 2270 -> 2953 (+683) | 27.300 | **27.467** | 0.17s |
| 2 | 2267 -> 2952 (+685) | 27.900 | **28.067** | 0.17s |
| 3 | 2267 -> 2990 (+723) | 28.500 | **28.667** | 0.17s |

Per-frame percentage drawn, identical in shape on all three:

```
tick1   27.30: 9%   27.33: 27%   27.37: 54%   27.40: 76%   27.43: 98%   27.47: 100%
tick2   27.90: 7%   27.93: 26%   27.97: 52%   28.00: 74%   28.03: 96%   28.07: 100%
tick3   28.50: 9%   28.53: 25%   28.57: 51%   28.60: 72%   28.63: 93%   28.67: 100%
```

Six intermediate states per mark. **It is drawn, not revealed.** Completion stagger
is **0.600s / 0.600s** exactly. Last mark complete at **S.s6 + 3.116s** — inside
`chapter_design`'s "assemble by about +3.3".

Each draw begins **+0.149s after its cue**, identical to the millisecond on all
three. That is geometry, not a timing fault: `draw(..., len=110)` sets a 110-unit
dasharray over a path (`M28 50 L45 68 L88 16`) that is 92.2 units long, so the
first ~33% of the eased tween reveals nothing. Deterministic and self-consistent.

The negative readings just before each draw (−4% to −22%) are the checkbox still
settling out of its `back.out` pop overshoot — independent evidence the cell pop
animates too.

**Both new SVGs render as recognisable glyphs.** The grocery bag reads as a bag
(straight-sided body under one semicircular handle — not the salt shaker fin-build
discarded); the fuel pump reads as a pump (body, display window, nozzle and hose on
the right). Neither is ambiguous at 220px.

### 3c · One consequence for the contact sheet, worth knowing

`SHEET-ch1.json` samples s6 at `data-start + 2.600` = **28.151**, which is **0.35s
before tick 3 even begins to draw**. The s6 cell therefore shows the third box
**empty** — the sheet under-represents the finished state. s6's mechanism settles at
**+3.116**, later than the sheet's `SETTLE` of +2.600. Nothing is wrong with the
render; fin-editor and fin-ceo should read the completed state as 28.667, not as the
sheet cell.

---

## 4 · CHANGE 3 — s5 at `background-position: center 100%`

Measured on full-resolution encoded frames, not on the brightened inspection copies.

| element | rows (1080) |
|---|---|
| X-ring, innermost circle of the target | ~248 - 376 |
| the dark aiming cross at the centre | ~309 - 334 |
| arrow's impact point (shaft meets target) | ~387 |
| **kicker "NOT RICH"** | **460 - 480** |
| **statement "One specific number."** | **534 - 646** |

**Clearances, type top (460) minus:**

- X-ring bottom edge -> **83 px**
- the aiming cross -> **125 px**
- the arrow's impact point -> **72 px**

**The type is clear of the bullseye at every sample** — 22.000 (dissolve end),
22.333 (the editor's own instant), 23.367 (max density), 24.333, 25.400. The type
band is unchanged across the whole scene (460-646 at every sampled frame), so the
ken push does not walk the mark into it. The statement runs across bare gold and
lower red, as fin-build described.

**One residue, measured and reported, not judged:** the arrow's fletching
(x ~1203-1374, reaching down to y ~537) meets the ascender line of "number"
(cap top y ~530) at the top right. They are adjacent — the letterforms are unbroken
and the white type stays fully legible over the dark red vane — and there is no
horizontal overlap with the kicker at all ("NOT RICH" ends at x ~1049, the fletching
starts at x ~1203). This is exactly the residue fin-build documented at attempt 3;
it does not touch the bullseye question and it is the editor's call, not mine.

---

## 5 · The s4 Lottie still fires at +1.13, and it lands on the phone

`playLottie(s4art, S.s4 + 1.13, 2.50)` at line 344, unchanged. Fire =
14.599 + 1.13 = **15.729s**. Stage `.v-lstage` now `left:815 top:602 width:820
height:300` (moved from 550 with the s4 repoint).

Method as attempts 1 and 2: per-frame luma difference
(`crop -> tblend=difference -> signalstats -> YAVG`) inside the exact stage box,
against two background-only controls — CTRL_top `crop=820:300:815:150`, CTRL_left
`crop=300:300:0:700`.

| Window | STAGE YAVG | CTRL_top | CTRL_left | Reading |
|---|---|---|---|---|
| 15.40 - 15.80 (pre-fire) | 0.045 - 0.061 | 0.116 - 0.158 | 0.057 - 0.081 | **below** the controls — nothing drawn |
| **15.933 (onset)** | 0.048 -> **1.670** | 0.133 | 0.057 | **12.5x** the control floor, isolated to the box |
| 15.93 - 16.53 (draw) | 0.84 - 1.67 sustained | floor | floor | 5x-12x the controls throughout |
| 16.60 - 17.33 (settle / hold) | decays 0.50 -> 0.051 | floor | floor | banner assembled, still on screen |
| 17.47 - 17.73 (jitter 2) | 0.27 - 0.98 | (stmt rise at 17.40) | floor | matches the asset's late frames |
| 17.80 - 18.73 (tail) | 0.026 - 0.067 | floor | floor | banner held, no exit |

**35 frames of motion** above 0.30 inside the box between 15.35 and 18.75, with
CTRL_left at its 0.019-0.270 floor throughout.

Onset lands at **15.933** = **lottie frame 6.1** — **identical to attempts 1 and 2**.
That is the asset's own authored 5-frame park, not a timeline fault: the cue fires
at 15.729 and the artwork holds first. Three attempts, same number. No action.

The 3.44 spike on CTRL_top at 17.400 is the `s4-stmt` cue at 17.349 rising above the
stage — it independently anchors the timebase to within ~1.5 frames, as in both
previous rounds.

**On the phone.** The banner spans **x ~905-1547**, the phone **x ~1047-1380**: the
phone runs down the middle of the card, not under its right edge. Read at 16.433
(mid-build, near the `buzz` cue at 16.449) and at 17.200 (assembled — $ badge, two
text lines, timestamp dash). The stage move to `left: 815` did what fin-build
intended.

---

## 6 · Contact sheet

`renders/SHEET-ch1.jpg` — 8 cells, one per scene, plus `SHEET-ch1.json` for the
orchestrator's numbered cross-chapter PNG. Sample times all `data-start` + 2.600
(`SETTLE`): 2.600 / 6.143 / 11.854 / 17.199 / 24.164 / 28.151 / 33.862 / 40.749.
Chapter 1 renders no `countUp`, so `SETTLE_COUNTUP` (4.5) never engaged. s4's 17.199
lands inside the Lottie's settled hold, so that cell shows the banner fully formed.
See §3c for the s6 cell's early sample.

No rail, no chapter title, no counter, no slide number in any frame I read; the
`cut-en` watermark rides bottom-right in all of them.

## 7 · Nits — reported, not fixed. I changed no file.

1. **Stale contact sheet from attempt 1.** `renders/SHEET.jpg` and
   `renders/SHEET.json` (04:42, default filenames) are still in the directory and are
   still stale — flagged last round, still present. Not an input to anything; delete
   or ignore. The live artifacts are the `-ch1` pair.
2. **`index.html` line 283 comment is wrong.** It reads "plateKen chains
   1.00->1.08->**1.16**"; the code at line 288 is `plateKen("#s4-bg", S.s4, D.s4,
   1.08, **1.30**)`. The code is correct and is what I measured — the prose is left
   over from an earlier draft of the fix. Worth correcting in `build.mjs` so the next
   build does not trust it.
3. `assets-ch1/final/s4.jpg` (175,925 B) remains on disk with zero `url()`
   references. Intended per fin-build; noted so archive does not treat it as live.

## 8 · Not done in this mode, by design

Gate-two frame check, dissolve sampling at both `qa.dissolve_sample_offsets`
[0.225, 0.38] for the two-scenes'-text double-paint defect, faster-whisper
re-transcription, VAD onset drift with `qa.vad_onset_latency_seconds` (0.101)
subtracted, true-peak / loudnorm, runtime vs `timing.json` total for the whole cut.
The seven-joint reads in §2 are photographic-continuity measurements at chapter
level and are **not** a substitute for gate two, which runs once on the assembled
cut.

## Artifacts

- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.json`
