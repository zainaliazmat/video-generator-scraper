---
summary: Master render + audio finishing + QA for passive-income-number en. All four QA thresholds measured; three pass, VO drift fails by 39 ms on one line of 81 and is RESCUED with the evidence that it is pre-existing in the locked chapter, not introduced by assembly.
updated: 2026-08-15
source: tools/cut_assemble.py, hyperframes render 0.7.66, tools/audio/mix.py, tools/loudnorm.py, tools/transcript.py, tools/pipeline_check.py check render
stage: render, cut en, attempt 1
---

# render-en attempt 1

## What was produced

| File | Size | Notes |
|---|---|---|
| `renders/FINAL-1080p-en.mp4` | 566.6 MB | the archive master. 15,837/15,837 frames, 8m 47.9s, 1920×1080 @30fps, rendered in **29m 36.7s** |
| `renders/MIXED-1080p-en.mp4` | — | bed `bed-resolve.mp3` + **128 SFX** cues laid under the voice |
| `renders/PUBLISH-1080p-en.mp4` | — | **the upload**. −19.67 → **−14.20 LUFS**, **−1.64 dBTP**, LRA 3.20 |
| `renders/captions-en.srt` | — | **149 cues** |
| `vault/videos/passive-income-number/narration-en.md` | — | narration, joined not retyped |

Render command (both env vars load-bearing at this length):

```
FFMPEG_ENCODE_TIMEOUT_MS=10800000 PRODUCER_ENABLE_CHUNKED_ENCODE=true \
  npx hyperframes render . -q high -f 30 --video-bitrate 12M \
  -o ../passive-income-number-en/renders/FINAL-1080p-en.mp4
```

## QA — three of four pass

```
vo drift : max +0.139s at line 4.8 over 81 clips   (target ±0.1s)   ✗
true peak: -1.64 dBTP                              (ceiling -1.0)   ✓
black    : no black segments                                        ✓
runtime  : 527.9s against timing.json's 527.873s                    ✓
```

## The VO drift failure, investigated to root cause rather than retried

**VERDICT: pre-existing in the locked chapter, NOT introduced by assembly. Rescued, not fixed.**

Three measurements, in the order they narrow it:

1. **Placement is exact.** All **81** `<audio>` rows in the assembled master sit on their
   `timing.json` `audio_start` to within 1e-6 s — checked row by row, none misplaced. `vo-4-8`
   is at `data-start="294.8"`, which is exactly what timing.json declares. So the assembler did
   not move this clip.
2. **The clip is not an acoustic outlier.** True speech onset measured directly on all 81 mp3s
   (16 kHz mono, 10 ms windows, first window over 2% peak): **4.8 begins at 0.090 s** against a
   median of 0.050 s and a maximum of 0.100 s (5.12). It is at the top of the normal band, not
   outside it.
3. ⚠ **The same drift is in ch4's own draft, which was reviewed and LOCKED.** Running the
   identical Silero VAD path over `…-en-ch4/renders/DRAFT-ch4.mp4` at the chapter-local
   placement (46.261 s = 294.8 − 248.539) measures **+0.134 s** on 4.8. The master's +0.139 s
   reproduces that to **5 ms**. Nothing about assembly caused it.

**Why it surfaced only now:** `check render` is a CUT-level gate — `--chapter` is explicitly not
implemented for `render` — so it had never once run against ch4. The chapter gates are
`hyperframes check` plus the draft render, neither of which measures VO drift.

**Why it ships.** 0.139 s against a 0.100 s target is **39 ms over, about 1.2 frames at 30fps**,
on one line of 81, in a format with no lip sync and no on-screen mouth. The gate's real job —
catching a dropped or displaced clip — is governed by `vo_drift_match_window_seconds: 0.5`, and
**zero clips were lost**. The failure is the difference between a single global
`vad_onset_latency_seconds: 0.101` constant and this clip's genuine +0.040 s later onset, plus
VAD's own conservatism on the opening phoneme.

**What was deliberately NOT done, and why.** Re-cutting 4.8 is one ElevenLabs call, but the
audio is already baked into a 29-minute render, so it would cost a full re-render to move a
sound 39 ms that no listener can locate. Nudging the placement 40 ms earlier would desync the
clip from its scene's visual timing to satisfy a measurement. **Neither buys anything a viewer
can perceive.** Tuning `vo_drift_target_seconds` to pass this run was rejected outright — that
is the bottom rung of `fix-defaults-not-gates` and it is threshold-fitting to one's own output.

**Owed, not done here:** the gate models onset with ONE global latency constant while real
per-clip onset variance on this voice spans 0.050–0.100 s. A drift measured against each clip's
own measured onset would separate "the clip starts late" from "the clip is placed wrong", which
is the distinction the gate actually wants. Not changed mid-run — same reasoning as
`owed.cue_rung_5_does_two_jobs`: this alters the verdict for every chapter of every video, and a
cut in flight is the wrong place to re-model it. Raised as
`owed.vo_drift_uses_one_global_onset_constant`.

---

## Attempt 2 — the same file, re-rendered with motion (2026-08-15)

Gate two found that attempt 1's master carried **no motion at all** (see
`incidents.the_master_rendered_with_NO_MOTION_AT_ALL_2026-08-15`). `tools/cut_assemble.py` was
fixed, `verify_motion()` added, and the cut re-rendered.

| | attempt 1 (static) | attempt 2 (correct) |
|---|---|---|
| size | 566.6 MB | **759.9 MB** |
| render time | 29m 36.7s | **57m 19.2s** |
| frames | 15,837 | 15,837 |
| runtime | 8m 47.9s | 8m 47.9s |

⚠ **The +34% size and +94% render time are themselves corroboration**: 81 animating scenes cost
far more to capture and encode than 81 stills that cross-dissolve. Assembly reports
**382 motion calls carried / 382 declared**.

Audio is byte-identical (the mix reads the same VO clips and the same 128-cue list), so the
finishing chain reproduced exactly: **−19.67 → −14.20 LUFS, −1.64 dBTP**. Captions were NOT
regenerated — they are a join of `script-en.md` and the composition's `<audio data-start>`
values, neither of which changed.

**QA reproduced exactly, including the failure:** VO drift **+0.139s at 4.8** again, true peak
−1.64 dBTP, no black, runtime on target. That the drift is bit-identical across two independent
renders is further confirmation of the attempt-1 diagnosis — it is a property of the clip and
its placement, not of anything the renderer does. **RESCUED again, on the same reasoning.**
