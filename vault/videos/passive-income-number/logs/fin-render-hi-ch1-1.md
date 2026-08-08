---
summary: hi ch1 draft render + contact sheet (style-E rebuild). 1275 frames / 42.500s exactly as predicted, 0 black segments. Found one isolated build defect — #s4-stmt has no motion call, so s4's headline is up at scene-open and paints against s3's for the whole s3->s4 dissolve.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch1/renders/DRAFT-ch1.mp4 (rendered 2026-08-08 10:26:40)
---

# fin-render · passive-income-number · hi · ch1 · attempt 1

Mode: **CHAPTER DRAFT** (orchestrator §3b step 4). Gate two and the full-quality
encode were NOT run — this is the judge-images/motion/timing pass only.

## 1 · Commands run (exact)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1.mp4 -q draft -f 30
python3 tools/chapter_sheet.py studio/videos/passive-income-number-hi-ch1 \
        studio/videos/passive-income-number-hi-ch1/renders/DRAFT-ch1.mp4 \
        -o studio/videos/passive-income-number-hi-ch1/renders/SHEET-ch1.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode.
`-f 30` verified correct: `index.html` declares **no `data-fps`**, so the
composition takes the 30 default and the final will too.

## 2 · Freshness (the retired style-A files were NOT mistaken for output)

| file | mtime | status |
|---|---|---|
| `renders/DRAFT-ch1.mp4` | **2026-08-08 10:26:40** | written by this run |
| `renders/SHEET-ch1.jpg` | **2026-08-08 10:29:23** | written by this run |
| `renders/SHEET-ch1.json` | **2026-08-08 10:29:23** | written by this run |
| `DRAFT-ch1-v2/v3/v4.mp4`, `SHEET-ch1-v2/v3/v4.*`, `SHEET.*`, `*.superseded` | 2026-08-07 | untouched style-A leftovers, ignored |

Every number below is read off the 10:26:40 mp4.

## 3 · Frame count and duration — measured from the encode

| measure | value | expected | verdict |
|---|---|---|---|
| `nb_read_frames` (decoded, not estimated) | **1275** | ceil(42.475 x 30) = 1275 | exact |
| video stream duration | **42.500000 s** | 1275/30 = 42.500 | exact |
| container duration | 42.517333 s | — | +0.0173s AAC frame padding on the audio stream, normal |
| `r_frame_rate` / `avg_frame_rate` | **30/1** / **30/1** | 30 | exact, CFR |
| resolution | 1920x1080 | — | draft is full-res by design |
| codec / size / bitrate | h264 / 10,456,086 B / 1.967 Mb/s | — | draft quality |
| audio | aac 48 kHz stereo, 42.517333 s | — | present |

Renderer's own trace agrees: `totalFrames: 1275, framesCompleted: 1275`,
`artifact validated`, 2m 21.3s wall.

Root `data-duration="42.475"` and the scene table sum correctly:
s8 `data-start` 35.171 + `data-duration` 7.304 = 42.475. No drift to inherit at
the ch1/ch2 joint.

## 4 · Black-segment scan

```
ffmpeg -i renders/DRAFT-ch1.mp4 -vf blackdetect=d=0.05:pic_th=0.98:pix_th=0.10 -an -f null -
```

**0 segments.** Nothing reported at any threshold crossing, including the
opening and closing frames. (Note the chapter is a dark cold open — plateau
YAVG runs 38-51 — so a loose `pix_th` would have been the risk here, and 0.10
still returned clean.)

## 5 · The s3 -> s4 joint — measured, NOT ruled on

Structure confirmed in source before measuring: `sceneTransitions(IDS, S)` with
the 0.45s default, no `acts`, no `HOLDS` entry for ch1 — so the joint is a
**0.45s cross-dissolve at 12.222 -> 12.672 s** (frames 367-380), exactly as
storyboard §10 declares and not the script's continuous zoom. Both s3 and s4
carry a single `.bg` each, so there are no in-scene framing swaps confusing the
window.

### 5a · scdet, all seven joints (peak score inside each 0.45s overlap)

| joint | start | peak scdet | at | sum over window |
|---|---|---|---|---|
| s1->s2 | 4.222 | 0.224 | 4.500 | 2.28 |
| s2->s3 | 8.366 | 0.205 | 8.333 | 1.73 |
| **s3->s4** | **12.222** | **0.232** | **12.300** | **2.08** |
| s4->s5 | 17.985 | 0.187 | 18.067 | 1.57 |
| s5->s6 | 21.659 | 0.170 | 21.800 | 1.50 |
| s6->s7 | 29.825 | 0.116 | 29.967 | 0.91 |
| s7->s8 | 35.171 | 0.213 | 35.333 | 1.88 |

s3->s4 is the highest-scoring joint, but only just — it sits 0.008 above
s1->s2 and 0.019 above s7->s8, inside the spread of the other six. For scale,
the video's **global** scdet maxima are all IN-SCENE motion, not joints:
0.384 @ 1.133s (s1 ken + kicker rise), 0.367 @ 30.967s, 0.355 @ 9.500s. The
s3->s4 change is smaller than three ordinary in-scene moments.

### 5b · Luminance step across each joint (signalstats YAVG)

Plateaus sampled 0.9s before the overlap and 1.0s after it.

| joint | pre Y | post Y | step | max dY/frame in window |
|---|---|---|---|---|
| s1->s2 | 38.28 | 50.88 | **+12.599** | 1.843 |
| s2->s3 | 50.13 | 41.27 | -8.856 | 1.367 |
| **s3->s4** | **44.09** | **40.93** | **-3.160 (-7.2%)** | **0.556** |
| s4->s5 | 44.26 | 42.02 | -2.243 | 0.512 |
| s5->s6 | 45.42 | 39.29 | -6.127 | 0.965 |
| s6->s7 | 42.32 | 38.25 | -4.077 | 0.743 |
| s7->s8 | 41.28 | 42.17 | +0.887 | 0.108 |

s3->s4 is the **second-smallest luminance step of the seven** and the
third-smallest per-frame delta. The ramp is monotonic and smooth across
f369-f379 (-0.083, -0.216, -0.336, -0.410, -0.472, -0.556, -0.435, -0.386,
-0.207, -0.152, -0.166), then flat from f380. **No step, no pop, no flash.**
Photometrically the two photographs match: the s4 fetch's "same counter
material" brief held.

### 5c · What the joint actually shows (frames sampled inside the overlap)

Sampled at both `format.json qa.dissolve_sample_offsets`:
12.222+0.225 = **12.447** and 12.222+0.38 = **12.602**.

- 12.447 — **both scenes' headlines are legible at once.** s4's
  "That one buzz is the money arriving." (top band) and s3's "Money lands in
  the account." (centred) both paint at roughly half opacity.
- 12.602 — s4 fully up, s3's headline a faint ghost still visible.

This is NOT the japanese-money-methods stacking-context bug: `.scene` carries
`isolation: isolate` (blockframe.css:63) and the outgoing scene is genuinely
crossfading, not sitting on top at full opacity. The cause is §6 below.

**Not ruled on here** — `storyboard_hi_decisions.s4_dissolve_overrides_the_
script_cue` asks fin-editor to rule from the encode. The measured numbers say
the joint is optically the *gentlest* real cut in the chapter.

## 6 · DEFECT FOUND — `#s4-stmt` has no motion call

`index.html`'s own cue-ladder comment states the contract:

> THE TYPE — cue ladder variant A (storyboard §5): kicker +0.30 rise y24,
> statement +1.10 rise y40, foot +1.90 fade. Fixed offsets, constant whatever a
> clip's length

Six scenes carry a `#sN-stmt` (s1, s3, s4, s5, s7, s8). Five are animated:

```
rise("#s1-stmt", S.s1 + 1.10, 0.7, 40);
rise("#s3-stmt", S.s3 + 1.10, 0.7, 40);
rise("#s5-stmt", S.s5 + 1.10, 0.7, 40);
rise("#s7-stmt", S.s7 + 1.10, 0.7, 40);
pop ("#s8-stmt", S.s8 + 1.10, 0.6);
```

**`#s4-stmt` has none.** (s2 and s6 have no `-stmt` element at all — chip and
tick scenes — so they are correctly absent, not missing.) The consequence is
measurable and lands squarely on the joint I was asked to measure: with no
tween, s4's headline is at full local opacity from the scene's first frame, so
it rides the scene dissolve up from 12.222 and collides with s3's outgoing
headline. Control frame at the s4->s5 joint (18.210, same 0.225 offset) shows
the intended behaviour: only the outgoing s4 text is up, s5's kicker and
statement are still at opacity 0 because their rises are at +0.30/+1.10, well
past the 0.45s overlap.

Also unmet at s4: the kicker/statement ladder ordering. `rise("#s4-kick",
S.s4 + 0.30, ...)` fires 0.30s AFTER a statement that is already fully up, so
at 12.447 the frame shows the statement with no kicker, and the kicker arrives
second. Every other scene reads kicker-then-statement.

One-line fix, matching its five siblings exactly:

```js
rise("#s4-stmt", S.s4 + 1.10, 0.7, 40);
```

## 7 · s4 Lottie banner — currency mark present, mask shape differs from the brief

Zoom snapshot of `#s4l` at 16.882s (the frame `chapter_sheet.py` picked, Lottie
fully built): the **₹ mark IS in frame**, on the banner's icon tile, so the
round-1 blocker ("a banner with no currency mark says 'a notification
arrived'") is satisfied.

Discrepancy against the build's own scene comment, which says *"the card reads
₹ • • • •"*: it does not. The card renders as a ₹ icon tile plus three plain
grey rounded bars — a loading-skeleton shape, not a dotted mask. No dots, and
no currency on the amount line itself. Whether the skeleton bars read as
"amount deliberately withheld" or as "the banner hasn't finished loading" is a
taste call for fin-editor, not mine. Recorded so the comment and the render can
be reconciled either way.

Background is confirmed a **dead-black phone screen** as §10 requires — the
picture never claims the money arrived.

## 8 · audio.json vs `tools/audio/cues.py` — read-only diff

Ran `python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch1`
**without `--write`**. The build's `assets/audio.json` was not modified.

Both lists carry **12 cues**. Ten are byte-identical in time and name
(transitions at 4.222 / 8.366 / 12.222 / 17.985 / 21.659 / 29.825 / 35.171,
buzz at 15.702, chip #1 at 22.759, stamp at 36.271). **One difference, in the
s6 chip cascade:**

| cue | build's audio.json | cues.py output | delta |
|---|---|---|---|
| s6 chip 1 | 22.759 | 22.759 | 0 |
| s6 chip 2 | **23.359** | 23.209 | -0.150 |
| s6 chip 3 | **23.959** | 23.659 | -0.300 |

**The build is right and the tool is wrong.** `assets/js/motion.js:48` defines
`function popEach(sel, at, stagger, dur)` — stagger is the THIRD argument. The
call is `popEach("#s6-ticks .v-tickcell", S.s6 + 1.10, 0.60, 0.45)`, so the
cells land at +1.10 / +1.70 / +2.30 = 22.759 / 23.359 / 23.959. `cues.py`'s
`counted` branch reads the step out of popEach's **fourth** positional argument
(`tools/audio/cues.py`, the `popEach\(...,\s*([\d.]+)` regex in the COUNTED
branch), which is the DURATION 0.45, giving a 0.45 step. Corroborated
independently by the three `draw("#s6-tickN", ...)` calls at +1.45 / +2.05 /
+2.65 — a 0.60 spacing. The generator's clicks would land 0.15s and 0.30s
before the pops they are supposed to be clicking.

fin-build flagged this in `build.mjs:591-596` and said it had reported it; this
run confirms it independently from the helper's signature. Running
`cues.py --write` on this chapter would REGRESS the cue list. The tool bug is
live for every future `counted` cascade on any cut.

Remaining differences are `_comment`/`_density` prose and the five `{"_dry":
...}` marker objects the generator emits and the build's hand-written file
omits — no cue times, no audible effect.

## 9 · Artifacts

- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-hi-ch1/renders/DRAFT-ch1.mp4`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-hi-ch1/renders/SHEET-ch1.jpg`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/passive-income-number-hi-ch1/renders/SHEET-ch1.json` (8 scenes, sample times 2.6 / 7.668 / 10.966 / 16.882 / 20.585 / 27.659 / 32.425 / 37.771)

## 10 · Not done in this mode

Gate-two frame check, VO drift vs `data-start`, peak dBTP, runtime vs
`timing.json` total, and the 1080p master encode all belong to the full-cut
render stage, not the chapter loop.
