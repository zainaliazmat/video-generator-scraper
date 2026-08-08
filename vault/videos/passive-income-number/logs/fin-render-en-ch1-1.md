---
summary: Chapter-1 draft render + contact sheet for passive-income-number-en. 1393 frames / 46.433s at 30fps, exact against the declared 46.420s. Zero black segments. The phone_notify_credit_usd Lottie is confirmed drawing and moving in the encoded frames, with its onset lag traced to the asset's own authored 5-frame park.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1 draft render, attempt 1
---

# fin-render — passive-income-number · en · chapter 1 · attempt 1

**Mode: chapter draft (orchestrator §3b step 4).** No gate-two frame check, no
dissolve sampling, no 1080p encode — those run once at cut level. This pass
exists so images / motion / timing get judged in minutes. Image *judgement* is
fin-editor's, from these two artifacts; everything below is measurement.

## Commands run (verbatim)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1.mp4 -q draft -f 30

python3 tools/chapter_sheet.py studio/videos/passive-income-number-en-ch1 \
        studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4 \
        -o studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30`
matches the final fps, so this chapter's frame count sums with its siblings.
Render: 1m 21.5s wall, 1 worker, browserGpuMode auto → hardware (ANGLE / Mesa
Intel HD 520), captureMode `beginframe`, exit 0.

## Measured numbers

| Quantity | Measured | Expected | Verdict |
|---|---|---|---|
| Frame count (`ffprobe -count_frames`) | **1393** | ceil(46.420 × 30) = 1393 | exact |
| `nb_frames` header | 1393 | 1393 | agrees with the decoded count |
| Video stream duration | **46.4333s** | 1393 / 30 = 46.43333 | exact |
| Container / audio duration | 46.4427s | — | +0.0094s AAC frame pad, benign |
| Declared root `data-duration` | 46.420s | timing.json | matches (ceil is the 0.0133s) |
| Frame rate | 30/1 CFR (`r_frame_rate` = `avg_frame_rate`) | 30 | ok |
| Resolution | 1920×1080 | 1920×1080 | ok |
| File size | 11,042,242 B (10.5 MB) | — | draft quality |
| Chapter offset | 0.000s | ch1 opens the cut | concatenates as-is |
| **Black segments** (`blackdetect d=0.05 pix_th=0.10`) | **0** | 0 | ok |
| Black frames (`blackframe amount=98 thresh=32`, looser) | **0** | — | ok, cross-check |
| Audio elements compiled | 8 | 8 VO clips | no SFX/bed — that is the post-mix step |
| Draft audio peak (`astats`) | −5.18 dB sample peak | < −1 dBTP | ok, but VO-only; the master figure is the cut-level QA |
| Draft audio RMS | −24.59 dB | — | informational |

`staticDuration` reported by the compiler: 46.42. `videoCount 0, audioCount 8,
imageCount 0` — every photograph is a CSS `background-image`, so nothing went
through the video-frame extractor.

Render lint: 2 warnings only, both `timeline_track_too_dense` (track 1 and
track 2 each hold 4 timed elements). Advisory — it wants scenes split into
sub-compositions under `compositions/`. No errors, nothing blocking.

## The Lottie on s4 — verified from the ENCODED frames, not from a snapshot

The asset is `window.L_phone_notify_credit_usd`, 75 frames at `fr` 30, native
box 820×300, staged by the one-off `.v-lstage` rule at `left:550 top:602
width:820 height:300`. `playLottie(s4art, S.s4 + 1.13, 2.50)` scrubs frame
0 → 74 linearly over 2.50s, i.e. **29.600 lottie-frames/s**, firing at
S.s4 + 1.13 = 14.599 + 1.13 = **15.729s** and ending at 18.229s.

### Method

Per-frame luma difference (`crop → tblend=difference → signalstats → YAVG`)
inside the exact stage box, against two background-only control crops that see
only the `plateKen` push:

- LOTTIE  `crop=820:300:550:602`
- CTRL_top  `crop=820:300:550:150`
- CTRL_left `crop=300:300:0:700`

Timebase was independently anchored on the s3→s4 cross-dissolve: the declared
overlap is 14.599–15.049 and the measured signal ramps 14.633, peaks 14.833 and
returns to floor at 15.067. It was anchored a second time on the s4 statement
rise (cue 17.349): CTRL_top jumps 0.043 → 2.965 → 5.138 at 17.367–17.400 while
the Lottie box sits at floor. Both anchors land within one frame.

### Result — it animates

| Window | LOTTIE YAVG | CTRL_top | CTRL_left | Reading |
|---|---|---|---|---|
| 15.07 – 15.90 (pre-fire) | 0.013 – 0.022 | 0.033 – 0.088 | 0.033 – 0.077 | box is *quieter* than the plate push behind it — nothing drawn |
| 15.90 – 15.93 (onset) | 0.107 → **1.711** | 0.032 | 0.058 | ~80× step, isolated to the box |
| 16.27 – 16.54 (jitter 1) | 0.61 – 1.56 sustained | 0.03 – 0.06 | 0.04 – 0.07 | the buzz shake |
| 16.54 – 17.42 (hold) | decays 0.50 → 0.006 | floor | floor | banner settled, still on screen |
| 17.43 – 17.73 (jitter 2) | 0.26 – 2.41 | floor after 17.73 | floor throughout | second shake |
| 17.77 – 22.01 (tail) | 0.008 – 0.070 | floor | floor | banner held, no exit |

Visually confirmed too: a 4×5 tile of the stage box at 6 fps across
15.60–18.50, plus a 21-frame consecutive tile across 15.60–16.27. The banner
fades up as a shell, the `$` chip fills, the title line draws, the amount pill
grows, and the banner's x-position visibly wobbles a few px during both jitter
windows. It is drawing, and it is moving.

### The +0.204s onset lag is the asset's own head, not a pipeline fault

First visible pixel change is at **15.933**, i.e. 0.204s (≈6 frames) after the
declared 15.729 fire. Cause, read straight out of the asset's keyframes:

```
LAYER notification   p anim: (t=0, [410,222]) (t=5, [410,222]) (t=15, [410,168]) …
LAYER bloom          o anim: (t=0, [0.0])     (t=5, [0.0])     (t=15, [100.0]) …
```

Lottie frames 0–5 are deliberately parked: the banner sits at y 222 (below the
visible band) with the bloom at opacity 0. At 29.600 frames/s, frame 5 lands at
15.729 + 5/29.600 = **15.898s** — the measured onset. The timeline fires on
time; the artwork is authored to hold for 5 frames first. No action needed.

### The buzz SFX offset is legal against the artwork

`assets/audio.json` puts the diegetic buzz at 16.449 (= S.s4 + 1.85) and claims
"the Lottie banner is jittering on this offset". Checked against the asset's
position keyframes mapped to absolute chapter time:

```
jitter 1: f16 16.270 · f18 16.337 · f20 16.405 · f22 16.472 · f24 16.540 (settle)
jitter 2: f51 17.452 · f53 17.520 · f55 17.587 · f57 17.655 · f59 17.722 (settle)
```

16.449 sits between f20 and f22 — inside the first shake, 0.09s before it
settles. The audio.json rationale holds.

Note the SFX is **not in this draft**: the composition compiles 8 audio
elements and all 8 are `vo-1-1 … vo-1-8`. `audio.json` is the spec the mix
step consumes, not something ch1's `index.html` plays. Judge the buzz timing at
mix, not from this file.

## VO coverage (supplementary — not the drift gate)

`silencedetect n=-50dB d=0.35` finds 13 silence windows and all 8 VO clips
present. Speech onset after each inter-line gap vs the `data-start` table:

| Clip | `data-start` | silencedetect onset | Δ |
|---|---|---|---|
| 1.1 | 0.250 | (no ≥0.35s lead silence — speech from the top) | — |
| 1.2 | 3.793 | 3.8266 | +0.034 |
| 1.3 | 9.504 | 9.5672 | +0.063 |
| 1.4 | 14.849 | 14.8765 | +0.028 |
| 1.5 | 21.814 | 21.8828 | +0.069 |
| 1.6 | 25.801 | 25.9022 | +0.101 |
| 1.7 | 31.512 | 31.5745 | +0.063 |
| 1.8 | 38.399 | 38.4521 | +0.053 |

Max +0.101s, mean +0.059s, all one-sided positive — the expected shape of a
detector threshold plus each clip's own lead-in, not timeline drift. **These are
`silencedetect` numbers, not Silero VAD**, so `format.json`
`qa.vad_onset_latency_seconds` (0.101) does NOT apply to them and must not be
subtracted here. The real per-line drift check is faster-whisper + VAD on the
1080p master at cut level; this table only proves no clip is missing or
mis-slotted.

The five remaining silence windows (4.523–4.897, 5.852–6.290, 27.307–27.722,
34.223–34.684, 41.084–41.470, all 0.37–0.46s) are intra-line punctuation
pauses, consistent with `tts.pause_seconds`. Tail silence 45.569–46.443
(0.874s) after clip 1.8 ends at 45.870.

## Contact sheet

`renders/SHEET-ch1.jpg` — 8 cells, one per scene, plus `SHEET-ch1.json` for the
orchestrator's numbered cross-chapter PNG. Sample times, all scene start + 2.6
(`SETTLE`):

| Cell | Scene | t |
|---|---|---|
| 1 | s1 | 2.600 |
| 2 | s2 | 6.143 |
| 3 | s3 | 11.854 |
| 4 | s4 | 17.199 |
| 5 | s5 | 24.164 |
| 6 | s6 | 28.151 |
| 7 | s7 | 33.862 |
| 8 | s8 | 40.749 |

Every t = its scene's `data-start` + 2.600 exactly. Chapter 1 renders no
`countUp`, so `SETTLE_COUNTUP` (4.5) never engaged and nothing here depends on
it — the shorter settle was not re-introduced. s4's 17.199 lands inside the
Lottie's 16.54–17.42 hold, so that cell shows the banner fully formed rather
than mid-draw, which is what fin-editor needs to see.

## Not done in this mode, by design

Gate-two frame check, dissolve sampling at `qa.dissolve_sample_offsets`
[0.225, 0.38], faster-whisper re-transcription, true-peak / loudnorm on the
master, runtime vs `timing.json` total for the whole cut. All of those are
cut-level and run once, after every chapter is locked.

## Artifacts

- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/DRAFT-ch1.mp4`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.jpg`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-en-ch1/renders/SHEET-ch1.json`
