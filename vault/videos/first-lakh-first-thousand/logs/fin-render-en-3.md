---
summary: fin-render MASTER QA on the en master — PASS. Runtime +0.018 s vs timing.json, 92/92 VO lines at a uniform +0.0213 s with sd 0.0000, PUBLISH -1.05 dBTP with flat factor 0.000000 and 2 peak samples of 24,268,800, zero black segments in 15,167 frames. All four scene-specific carry-overs (s59 minor panel, s91 suppressed bar, s21 mid-tone, s90 grade override) survived the encode intact and were re-measured on delivered pixels.
updated: 2026-07-31
source: own ffprobe + ffmpeg loudnorm/astats/blackdetect/blackframe/silencedetect/signalstats on renders/{FINAL,MIXED,PUBLISH}-1080p-en.mp4 - FFT cross-correlation of the 92 assets/voice/*.mp3 against both masters - faster-whisper small int8 (venv) single pass - assets/voice/timing.json (92 lines) - index.html data-start table (92 audio rows)
stage: fin-render, cut en, attempt 3 - invocation 2 of 2, master QA only (no encode, no re-mix, no frame check)
---

# fin-render - «The First $10,000 Is The Hardest» en, attempt 3 - MASTER QA: PASS

**Nothing was encoded, mixed or re-rendered by this stage.** The encode and the audio finish are
the orchestrator's. This stage measured the delivered files only.

Deliberately reported in the same four slots as the hi cut so the pair is comparable.

## Side by side - hi cut vs this en cut

| # | Measurement | hi (attempt 4) | **en (this cut)** |
|---|---|---|---|
| 1 | Runtime vs timing.json | +0.027 s | **+0.018 s** |
| 1 | Frames | 15,444 @ 30/1 | **15,167 @ 30/1** |
| 2 | VO lines matched | 86 / 86 | **92 / 92** |
| 2 | Drift mean / sd | +0.0213 / 0.0000 | **+0.0213 / 0.0000** |
| 2 | Drift max | +0.0214 | **+0.0214** |
| 3 | PUBLISH true peak | -1.26 dBTP | **-1.05 dBTP** |
| 3 | Flat factor | 0.000000 | **0.000000** |
| 3 | Peak count | 2 of 24,711,168 | **2 of 24,268,800** |
| 4 | Black segments | 0 in 15,444 f | **0 in 15,167 f** |

The two cuts carry the *identical* placement signature (+21.3 ms, zero spread) and the *identical*
clipping signature (flat factor 0, 2 peak samples, abs peak count 1).

## 1. Runtime - PASS, +0.018 s

| file | video stream | audio stream | container | size | vs timing.json 505.561 |
|---|---|---|---|---|---|
| FINAL   | 505.566667 (15,167 f, 11,789,166 bit/s) | 505.578667 (aac 48 kHz stereo, 165,924 bit/s, 23,699 f) | 505.578667 | 755,950,002 B | **+0.018 s** |
| MIXED   | 505.566667 (15,167 f, 11,789,166 bit/s) | 505.579000 (193,109 bit/s, 23,701 f) | 505.579000 | 757,668,545 B | +0.018 s |
| PUBLISH | 505.566667 (15,167 f, 11,789,166 bit/s) | 505.600000 (194,602 bit/s, 23,701 f) | 505.600000 | 757,763,422 B | +0.039 s |

15,167 / 30 = 505.5667 exactly. Video stream identical across all three (stream-copied through mix
+ loudnorm). Last VO (9.10) ends 505.011 s; the +0.018 / +0.039 s tails are AAC padding after the
last word, same mechanism as hi.

## 2. VO placement - PASS, max drift +0.0214 s (target <= 0.1 s)

Method identical to the hi cut: normalised FFT cross-correlation of each source
`assets/voice/<id>.mp3` (first <= 3 s) against a +/-0.8 s window of the master, both decoded to mono
16 kHz. **Each master's audio was decoded once in full (505 s -> 16 MB) and windowed in memory**
rather than seeking per line, so seek accuracy cannot contribute to the measured offset.

| master | matched | min | max | mean | sd | corr min | corr mean |
|---|---|---|---|---|---|---|---|
| **FINAL**   | **92 / 92** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.983 | 0.989 |
| **PUBLISH** | **92 / 92** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.936 | 0.977 |

Uniform +21.3 ms AAC priming delay on every line, zero spread, zero accumulation across 505 s.
**0 outliers in 184 measurements** (test: `corr < 0.9` or `|lag| > 0.05`). PUBLISH's lower corr
floor (0.936 on 5.6, 0.939 on 4.6) is the bed + 23 SFX sitting under the voice, not displacement -
every one of those rows still lands at +0.0213.

Build integrity: all 92 `data-start` / `data-duration` values match `timing.json`
`audio_start` / `duration` to **0.0000 ms - 0 mismatches**, 92 audio tags in the html.

## 3. Levels - PASS

| file | input_i (LUFS) | **input_tp (dBTP)** | LRA |
|---|---|---|---|
| FINAL   | -21.13 | -1.75 | 3.20 |
| MIXED   | -21.19 | -1.86 | 3.10 |
| **PUBLISH** | **-14.14** | **-1.05** | 3.00 |

`astats` on PUBLISH (the upload file):

- sample peak **-1.344036 dB** (L) / **-1.157258 dB** (R)
- **Peak count 2** per channel of **24,268,800** samples, **Abs peak count 1**
- **Flat factor 0.000000** both channels - no flat-topped run anywhere
- RMS -17.7162 / -17.7256 dB, bit depth 31/32

**On the 0.21 dB the orchestrator flagged:** en's PUBLISH is hotter than hi's (-1.05 vs -1.26), and
the question was whether that bought any clipping. It did not. Flat factor, peak count and abs peak
count are *identical* to hi's to the digit; worst-channel sample peak is -1.16 dBFS vs hi's -1.29.
The extra level produced zero additional limiter activity.

**Recorded honestly:** -1.05 dBTP leaves **0.05 dB** of margin under the -1 dBTP limit. It passes,
but it is a tenth of hi's 0.26 dB margin. Worth a slightly lower loudnorm target on the next en cut.

## 4. Content - PASS, voice confirmed present end to end

faster-whisper `small` int8, `language=en`, `beam_size=1`, VAD off, word timestamps, single pass on
FINAL: **122 segments spanning 0.00 -> 504.52 s**, and **zero gaps > 3 s**. The hi cut needed seven
isolated `clip_timestamps` re-runs to close whisper dropouts; this cut needed none - the transcript
is continuous on the first pass.

Per-line coverage, computed independently of the cross-correlation: **0 of 92 lines** have less than
50 % of their duration covered by transcribed speech. So the voice is *measured* present across the
whole cut by two independent methods, not assumed.

Transcript is US-market as intended - opens «$800 a month, the first $10,000 12 and a half months»,
closes «Next time what actually happens after that 100,000 and how fast it moves».

`silencedetect n=-45dB:d=0.4` on FINAL: **136 silences, min 0.417 s, max 1.324 s** - every one a
designed inter-line pause. No silence anywhere near long enough to be a dropout.

## 5. Black-frame scan - PASS, zero segments

| pass | result |
|---|---|
| `blackdetect=d=0.3:pix_th=0.10` | **0 segments**, `frame=15167` full decode |
| `blackdetect=d=0.2:pix_th=0.20` | **0 segments**, `frame=15167` full decode |
| `blackframe=amount=95:threshold=48` | **109 frames** - all one contiguous run, investigated below |

### The 109 blackframe hits - investigated, not a defect

hi returned 0 frames here, so this was chased down rather than waved through. All 109 are
**contiguous, frames 7679-7787, t 255.967 -> 259.567 s** = the whole post-dissolve body of
**scene 48 (line 5.7, 255.487-259.526)**. `pblack` peaks at 96 % and never rises further; the
actual black-segment test (`blackdetect`) finds nothing at either threshold.

Frames pulled from the delivered master at 256.10 / 257.50 / 259.30 and read at 1:1: s48 is a
genuine low-key photograph - a wicker basket on a stand, warm rim light, weave texture fully
resolving, ken burns visibly working across the three samples. All four system elements are present
and high-contrast: bar `THE LINE`, rule, focal `A number a lot of people have heard before`, foot
`CH 5 - 48 / 92`. The 95-96 % pblack is the large intentional black field around the subject.
**Deliberate chiaroscuro, not a black or missing frame.**

**Design note for the next cut (not a blocker on this one):** measured in the 1920x600 aperture,
s48 is the darkest scene in the video - **YAVG 5.3-5.7, p90 24, YMAX 133-136** - i.e. *darker than
s90*, the one scene that was judged to need a grade override, and with no highlight at all
(YMAX 133 vs s90's 255). It passed gate two at attempt 1 on a 1:1 read and it is legible, so it is
not re-litigated on a cut that has spent its fix pass. But if a per-scene grade allowance is ever
widened, s48 is the stronger candidate than the scene that actually got it.

## 6. The four carry-overs - all re-measured on delivered pixels

Every attempt-2 aperture number reproduces on the encoded master, which is the point: the encode
changed no grade.

| frame | attempt 2 (pre-encode) | **delivered master** | verdict |
|---|---|---|---|
| s21 @ 109.10 (worst frame) | YAVG 30.80 / p90 92 / max 161 | **30.81 / 92 / 163** | match |
| s21 @ 114.25 (ken max 1.16) | YAVG 38.67 / p90 96 / max 161 | **38.72 / 97 / 161** | match |
| s90 @ 494.30 (the one override) | YAVG 13.79 / p90 33 / max 255 | **13.79 / 33 / 255** | exact |
| s63 @ 342.26 (ordinary dark) | 70.01 / 123 | **70.03 / 123** | match |
| s10 @ 48.40 (bright ref) | 117.33 / 144 | **117.41 / 144** | match |

- **s21 - no crushed region.** Confirmed. The delivered scene holds 30.81 -> 38.72 YAVG through its
  1.00 -> 1.16 ken (the push *brightens*, so the first frame is the worst), with p90 92 -> 97. That
  is **2.2x s90's mean and 2.8x s90's p90** on delivered pixels. No second `filter:` override needed.
- **s90 - the one per-scene grade override survived the encode**, reproducing to 2 decimals
  (13.79 / 33 / 255). This remains the video's only per-scene grade.
- **s59 minor panel - still illegible.** The minor is `s11.jpg` at `left:1290px, top:180, 630x600`,
  no ken. Sampled at 323.50 s and zoomed to **4x and 12x nearest-neighbour** on the two most
  text-dense regions. At 12x the chart labels are 2 px-tall grey smudges with no resolvable glyph
  structure - the treemap is a flat block, the category axis is an unreadable stack. **No currency
  symbol and no digit group resolves anywhere in the panel; `£10,000,000` cannot be read.** The
  legible currency in the panel is US $1 / $2 / $5 / $10 / $20 notes, correct for a $ cut. Cleared.
- **s91 - reads as a deliberate quiet close.** Measured the top 180 px band where the bar would be:
  **YMIN 10, YAVG 15.997, p90 16, YMAX 20** at 497.86 and **YMIN 12, YAVG 16.000, YMAX 22** at
  499.30 - a flat uniform field of `--bg`. For contrast, s90's same band reads **YMIN 0, YMAX 252**,
  which is what a band containing a real title looks like. So on the delivered pixels there is no
  text, no black strip and no empty container box. Read at 1:1: the rule is drawn, the orange
  `SUBSCRIBE` pop block is present and high-contrast, the foot `CH 9 - 91 / 92` is present, the pen
  is unmarked. Confirmed as designed.

(s91's 21 px foot bottom margin, recorded at attempt 2 as a pre-existing `pop`-variant layout note,
is unchanged in the master. Still a note for the next cut, still not a blocker.)

## Numbers

| | |
|---|---|
| Runtime (FINAL) | **505.578667 s** vs timing.json 505.561 -> **+0.018 s** |
| Frames | **15,167** @ 30/1, full decode both black passes |
| VO lines verified present | **92 / 92** FINAL, **92 / 92** PUBLISH, + **92 / 92** by transcription |
| Max VO drift | **+0.0214 s**, mean +0.0213, sd 0.0000, 0 outliers / 184 |
| Peak (PUBLISH, the upload file) | **-1.05 dBTP**, -1.1573 dBFS sample, flat factor 0.000000, 2 peak samples |
| Peak (FINAL / MIXED) | -1.75 / -1.86 dBTP |
| Loudness (PUBLISH) | -14.14 LUFS, LRA 3.00 |
| Black segments | **0** in 15,167 frames, two thresholds |
| Encode / mix run by this stage | **none** |

## Verdict

**PASS.** `renders/PUBLISH-1080p-en.mp4` (757,763,422 B) is approved as the upload file for
@moneymavens101. Placement, levels, runtime and black content all match or beat the hi cut; the
only two things worth carrying forward are notes for the *next* cut, not defects in this one:
the 0.05 dB true-peak margin, and s48 being darker than the scene that got the grade override.
Both cuts can ship.
