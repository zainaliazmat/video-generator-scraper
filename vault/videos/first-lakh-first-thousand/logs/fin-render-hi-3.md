---
summary: fin-render MASTER QA, hi cut, attempt 3 — PASS. Runtime +0.027 s vs timing.json; all 86 VO lines present in FINAL at a uniform +0.0213 s AAC-priming offset (max drift 0.0214 s, corr 0.995–1.000), and all 86 still present in PUBLISH after the mix + 7.94 dB lift; PUBLISH true peak −1.26 dBTP with zero clipped samples; zero black segments in 15,444 frames. No encode or re-mix was run by this stage.
updated: 2026-07-31
source: own ffprobe + ffmpeg loudnorm/astats/silencedetect/blackdetect/blackframe/edgedetect on renders/{FINAL,MIXED,PUBLISH}-1080p-hi.mp4 · faster-whisper small int8 (venv) single pass + 3 isolated clip_timestamps passes · assets/voice/timing.json (86 lines) · index.html data-start table (86 audio rows)
stage: fin-render, cut hi, attempt 3 — invocation 2 of 2 (master QA only)
---

# fin-render — «पहला एक लाख» hi, attempt 3 — MASTER QA: PASS

Gate two passed at attempt 2 (frame check, 86/86 scenes). This invocation measured the
three files the orchestrator produced. **Nothing was encoded, re-mixed or re-rendered here.**

## 1. Runtime — PASS

| file | video stream | audio stream | container | vs timing.json 514.789 |
|---|---|---|---|---|
| FINAL   | 514.800 (15,444 f @ 30 fps, exact) | 514.816 | 514.816 | **+0.027 s** |
| MIXED   | 514.800 (15,444 f) | 514.816 | 514.816 | +0.027 s |
| PUBLISH | 514.800 (15,444 f) | 514.900 | 514.900 | +0.111 s |

Video is identical across all three (h264, 1920×1080, 30/1, nb_frames 15,444,
bit_rate 11,979,252 bit/s to the bit → stream-copied, not re-encoded).
The +0.027 s on FINAL and the extra +0.084 s on PUBLISH are AAC tail padding from the
mix and the loudnorm re-encode. Last VO (9.10) ends at 514.238 s, so **nothing is
truncated** — the pad is silence after the last word.

## 2. VO placement — PASS, max drift **+0.0214 s** (target ≤ 0.1 s)

Method: normalised FFT cross-correlation of each source `assets/voice/<id>.mp3`
(first ≤3 s) against a ±0.8 s window of the master, both decoded to mono 16 kHz.
This is the authoritative measure; whisper word timestamps cannot resolve 0.1 s on this
audio (carried finding from credit-history and pay-yourself-first, re-confirmed in §4).

| master | lines matched | drift min | drift max | mean | sd | corr min | corr mean |
|---|---|---|---|---|---|---|---|
| **FINAL**   | **86 / 86** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.995 | 0.998 |
| **PUBLISH** | **86 / 86** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.945 | 0.988 |

The offset is a constant +21.3 ms on every one of the 86 lines — the AAC encoder priming
delay, the same number measured on credit-history hi. Zero spread, zero accumulation
across 8.5 minutes: line 1.1 and line 9.10 carry the identical offset.

**The `preload="none"` question — answered by measurement, not assumption.** A correlation
peak of 0.995–1.000 means the source waveform is literally present at that timecode.
All 86 rows clear it; the weakest is 0.945 (in PUBLISH, where the bed and SFX sit under the
voice). No line is missing, silent, doubled or shifted. `preload="none"` cost nothing.

Build integrity: all 86 `data-start` / `data-duration` values match `timing.json`
`audio_start` / `duration` to < 0.5 ms — 0 mismatches.

## 3. Levels — PASS

| file | input_i (LUFS) | **input_tp (dBTP)** | LRA |
|---|---|---|---|
| FINAL   | −21.98 | −3.23 | 3.20 |
| MIXED   | −22.01 | −3.21 | 3.00 |
| **PUBLISH** | **−14.07** | **−1.26** | 3.00 |

PUBLISH sits 0.26 dB under the −1 dBTP limit. Clipping check on PUBLISH (`astats`):

- sample peak **−1.2889 dB** (L) / **−1.3095 dB** (R) — below the true-peak reading, as expected
- **Peak count 2** samples of 24,711,168 (Abs peak count 1) — two samples touch the maximum, which is what a limiter ceiling looks like, not clipping
- **Flat factor 0.000000** on both channels — **no flat-topped runs anywhere**, i.e. the +7.94 dB lift introduced no clipped segment
- RMS −17.09 dB, bit depth 31/32

## 4. Content — PASS

faster-whisper `small` int8, `language=hi`, `beam_size=1`, VAD off, word timestamps, single
pass on FINAL: **120 segments spanning 0.00 → 513.80 s**, continuous speech across the cut.

Two apparent holes in the single pass, **both model dropouts, both disproved**:

| window | single pass | isolated `clip_timestamps` re-run | verdict |
|---|---|---|---|
| 127.22 – 149.54 s | no segments | returns 3.3 «अंतर बढ़ने लगा — दो महीने से पाँच महीने», 3.4, 3.5, 3.6 verbatim | whisper dropout |
| 415.58 – 421.86 s | no segments | returns 8.5 «अगली बार तनख़्वाह बढ़े…», 8.6 verbatim | whisper dropout |

Cross-correlation had already put 3.3–3.6 (corr 0.995–0.998) and 8.5–8.6 (corr 0.997–1.000)
at their exact slots; the isolated passes are the independent second witness.

Whisper first-word onsets vs `data-start` (81 of 86 lines resolvable): −1.13 … +0.07 s,
mean **−0.27 s**, sd 0.22 — the known whisper onset bias (breath lead-in + block merging),
not placement error. Cross-correlation stands as the placement number.

`silencedetect n=-45dB:d=0.4` on FINAL: gaps are the designed inter-line pauses
(0.43 – 1.25 s in the opening block); no silence long enough to be a dropout.

## 5. Black-frame scan — PASS, zero segments

| pass | result |
|---|---|
| `blackdetect=d=0.3:pix_th=0.10` | **0 segments** |
| `blackdetect=d=0.2:pix_th=0.20` + `blackframe=amount=95:threshold=48` | **0 segments, 0 frames** |

Full decode both times, `frame=15444` — the whole cut was scanned, not sampled.

## 6. The two accepted cosmetics — re-confirmed cosmetic, NOT re-opened

- **1280 px sources / ~1.6× upscale on the s1–s2 zoom.** Confirmed as a source-resolution
  fact, not an encode defect: edge energy (`edgedetect,signalstats` YAVG) on the master reads
  **4.49 at 1.20 s** (zoom start) and **6.28 at 10.87 s** (zoom end) — detail *increases* into
  the zoom, so the encoder is not smearing or macroblocking the soft paper. Note: 1280 px is
  the norm for this cut's library (s12, s17, s33, s34, s50, s79, s81 all 1280; only s84 is
  1880), so this is an asset-sourcing standard to raise next cut, not a defect of the six
  replacements.
- **s34 pre-2016 ₹500 design** — authentic Indian currency, dated. Nothing in the master QA
  touches it. Still cosmetic.

## Numbers

| | |
|---|---|
| Runtime (FINAL) | **514.816 s** vs timing.json 514.789 → **+0.027 s** |
| VO lines verified present | **86 / 86** in FINAL, **86 / 86** in PUBLISH |
| Max VO drift | **+0.0214 s** (uniform +21.3 ms AAC priming) |
| Peak (PUBLISH, the upload file) | **−1.26 dBTP** true peak, −1.29 dBFS sample, flat factor 0 |
| Peak (FINAL / MIXED) | −3.23 / −3.21 dBTP |
| Black segments | **0** in 15,444 frames (two thresholds) |
| Whisper segments | 120, 0.00 – 513.80 s, 2 dropouts disproved by isolated passes |
| Encode / mix run by this stage | **none** |

## Verdict

**PASS** — `renders/PUBLISH-1080p-hi.mp4` is approved as the upload file.
