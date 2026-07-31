---
summary: fin-render MASTER QA on the RE-ENCODED hi master (after the s85 empty-bar deletion) — PASS, zero regression. All four attempt-3 numbers reproduce: runtime +0.027 s vs timing.json, 86/86 VO lines at a uniform +0.0213 s with sd 0.0000, PUBLISH −1.26 dBTP with flat factor 0.000000, zero black segments in 15,444 frames.
updated: 2026-07-31
source: own ffprobe + ffmpeg loudnorm/astats/blackdetect/blackframe/silencedetect on renders/{FINAL,MIXED,PUBLISH}-1080p-hi.mp4 · FFT cross-correlation of the 86 assets/voice/*.mp3 against both masters · faster-whisper small int8 (venv) single pass + 3 isolated clip_timestamps passes · assets/voice/timing.json (86 lines) · index.html data-start table (86 audio rows)
stage: fin-render, cut hi, attempt 4 — master QA only (no encode, no re-mix, no frame check)
---

# fin-render — «पहला एक लाख» hi, attempt 4 — RE-ENCODE REGRESSION QA: PASS

Scope set by the orchestrator: the cut was re-encoded after fin-build deleted two lines from
`index.html` (the s85 `bar: "—"` div and its cue). The visual fix was already confirmed by the
orchestrator at 506.5 s, so nothing was re-litigated visually here. This stage re-measured the
four attempt-3 numbers on the NEW files. **Nothing was encoded, mixed or re-rendered here.**

## Side by side — attempt 3 vs attempt 4

| # | Measurement | attempt 3 | **attempt 4 (new files)** | moved? |
|---|---|---|---|---|
| 1 | Runtime FINAL (audio/container) | 514.816 s | **514.816 s** | no |
| 1 | Runtime FINAL video stream | 514.800 s, 15,444 f @ 30/1 | **514.800 s, 15,444 f @ 30/1** | no |
| 1 | vs `timing.json` total 514.789 | +0.027 s | **+0.027 s** | no |
| 1 | MIXED / PUBLISH container | 514.816 / 514.900 | **514.816 / 514.900** | no |
| 2 | VO lines matched (FINAL / PUBLISH) | 86/86 · 86/86 | **86/86 · 86/86** | no |
| 2 | Drift min … max | +0.0213 … +0.0214 | **+0.0213 … +0.0214** | no |
| 2 | Drift mean / sd | +0.0213 / 0.0000 | **+0.0213 / 0.0000** | no |
| 2 | Corr min (FINAL / PUBLISH) | 0.995 / 0.945 | **0.995 / 0.942** | −0.003 on PUBLISH only |
| 3 | PUBLISH true peak | −1.26 dBTP | **−1.26 dBTP** | no |
| 3 | PUBLISH loudness / LRA | −14.07 LUFS / 3.00 | **−14.07 LUFS / 3.00** | no |
| 3 | PUBLISH flat factor | 0.000000 | **0.000000** | no |
| 3 | PUBLISH peak count / samples | 2 of 24,711,168 | **2 of 24,711,168** | no |
| 4 | Black segments (2 thresholds) | 0 in 15,444 f | **0 in 15,444 f** | no |

The only number that moved at all: the **video bitrate, 11,979,252 → 11,978,672 bit/s (−580 bit/s,
−0.005 %)** — two fewer DOM elements on one 3.961 s scene is exactly what that looks like. It is
the intended change, not a regression.

## 1. Runtime — PASS, +0.027 s

| file | video stream | audio stream | container | size | vs timing.json 514.789 |
|---|---|---|---|---|---|
| FINAL   | 514.800 (15,444 f, 11,978,672 bit/s) | 514.816 (aac 48 kHz stereo, 167,200 bit/s, 24,132 pkt) | 514.816 | 782,033,033 B | **+0.027 s** |
| MIXED   | 514.800 (15,444 f, 11,978,672 bit/s) | 514.816 (192,607 bit/s, 24,133 pkt) | 514.816 | 783,668,590 B | +0.027 s |
| PUBLISH | 514.800 (15,444 f, 11,978,672 bit/s) | 514.900 (194,397 bit/s, 24,133 pkt) | 514.900 | 783,785,801 B | +0.111 s |

Video stream byte-for-byte identical across the three (stream-copied through mix + loudnorm).
Frame count unchanged at 15,444 — **the deletion cost zero frames**, so no shift is even
representable at the container level. The +0.027 / +0.111 s tails are AAC padding after the last
word (last VO 9.10 ends 514.238 s), same as attempt 3.

## 2. VO placement — PASS, max drift **+0.0214 s** (target ≤ 0.1 s)

Method unchanged from attempt 3: normalised FFT cross-correlation of each source
`assets/voice/<id>.mp3` (first ≤3 s) against a ±0.8 s window of the master, both decoded to mono
16 kHz. Whisper word onsets cannot resolve 0.1 s on this audio (§4), so this is the placement number.

| master | matched | min | max | mean | sd | corr min | corr mean |
|---|---|---|---|---|---|---|---|
| **FINAL**   | **86 / 86** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.995 | 0.997 |
| **PUBLISH** | **86 / 86** | +0.0213 | **+0.0214** | +0.0213 | 0.0000 | 0.942 | 0.987 |

Uniform +21.3 ms AAC priming delay on every line, zero spread, zero accumulation. Corr min on
PUBLISH 0.942 vs 0.945 (bed + SFX under the voice); no row is an outlier by either test
(`corr < 0.9` or `|lag| > 0.05`): **0 outliers in 172 measurements**.

**The s85 question — nothing after it shifted.** s85 is line 9.9 (`scene_start` 504.647,
`audio_start` 504.897, 3.161 s), 10.1 s from the end. Everything downstream carries the identical
offset:

| line | audio_start | drift FINAL | corr | drift PUBLISH | corr |
|---|---|---|---|---|---|
| 9.8  | 498.167 | +0.0213 | 0.996 | +0.0213 | 0.990 |
| **9.9 (s85)** | **504.897** | **+0.0213** | 0.996 | **+0.0213** | 0.977 |
| 9.10 | 508.857 | +0.0213 | 0.996 | +0.0213 | 0.989 |

Build integrity: all 86 `data-start` / `data-duration` values still match `timing.json`
`audio_start` / `duration` to < 0.5 ms — **0 mismatches**, 86 audio tags in the rebuilt html.

## 3. Levels — PASS

| file | input_i (LUFS) | **input_tp (dBTP)** | LRA |
|---|---|---|---|
| FINAL   | −21.98 | −3.23 | 3.20 |
| MIXED   | −22.01 | −3.21 | 3.00 |
| **PUBLISH** | **−14.07** | **−1.26** | 3.00 |

Every figure identical to attempt 3 to the reported precision. PUBLISH sits 0.26 dB under the
−1 dBTP limit. `astats` on PUBLISH:

- sample peak **−1.288898 dB** (L) / **−1.309510 dB** (R) — same to 6 decimals as attempt 3
- **Peak count 2** of **24,711,168** samples (Abs peak count 1) — limiter ceiling, not clipping
- **Flat factor 0.000000** both channels — no flat-topped run anywhere
- RMS −17.0882 / −17.0990 dB, bit depth 31/32

## 4. Content — PASS

faster-whisper `small` int8, `language=hi`, `beam_size=1`, VAD off, word timestamps, single pass on
FINAL: **132 segments spanning 0.00 → 513.82 s** (attempt 3: 120 segments, 0.00 → 513.80 s —
segmentation is run-to-run nondeterministic in block merging; span is the same cut).

Seven windows > 3 s returned no segment in the single pass. Cross-correlation had already placed
every line inside them at corr ≥ 0.99; the three largest were re-run with isolated
`clip_timestamps` as an independent second witness, and **all three returned verbatim speech**:

| window | lines it covers | isolated re-run | verdict |
|---|---|---|---|
| 224.84 – 254.84 s (30.0 s) | 5.1 – 5.6 | 2 segments, «…एक बिंदु आता है जहाँ आपका पैसा साल भर में उतना कमा लेता है…क्रॉसओवर…» | whisper dropout |
| 356.98 – 366.12 s (9.1 s) | 7.4, 7.5 | 3 segments, «…क्योंकि टंकी की सतह छोटी है» / «पर जैसे जैसे टंकी भरती है» / «पानी की चौड़ी सतह बारिश को पकड़ने लगती है» | whisper dropout |
| 23.12 – 35.78 s (12.7 s) | 1.4 – 1.6 | 4 segments, «…पहला एक लाख आपकी ज़िन्दगी का सबसे मुश्किल एक लाख होता है…» | whisper dropout |

Remaining four windows (196.22–202.64 → 4.6–4.7; 376.52–383.16 → 7.7–7.8; 405.68–409.44 → 8.3;
482.60–486.02 → 9.5) are the same class; all covered lines sit at corr 0.995–1.000 in §2.

Tail transcript is continuous through the edited scene — 498.20–501.12, 501.12–503.74,
**504.72–507.66 («पैसे की ऐसी सीधी बात के लिए, सब्सक्राइब…» = line 9.9, the s85 scene)**,
508.54–513.82.

`silencedetect n=-45dB:d=0.4` on FINAL: **136 silences**, all designed inter-line pauses
(0.42 – 1.28 s). Around s85: 503.748 → 504.945 (1.197 s designed gap), then speech; last silence
513.853 → 514.816 is the AAC tail. No silence long enough to be a dropout, and no *new* silence
where the bar used to be.

## 5. Black-frame scan — PASS, zero segments

| pass | result |
|---|---|
| `blackdetect=d=0.3:pix_th=0.10` | **0 segments**, `frame=15444` full decode |
| `blackdetect=d=0.2:pix_th=0.20` + `blackframe=amount=95:threshold=48` | **0 segments, 0 frames**, `frame=15444` |

Relevant because the defect being fixed was a *black* bar: at the loosest threshold the scan still
finds nothing, and s85 is no darker than any other scene.

## Numbers

| | |
|---|---|
| Runtime (FINAL) | **514.816 s** vs timing.json 514.789 → **+0.027 s** (unchanged) |
| VO lines verified present | **86 / 86** FINAL, **86 / 86** PUBLISH (unchanged) |
| Max VO drift | **+0.0214 s**, sd 0.0000, 0 outliers/172 (unchanged) |
| Peak (PUBLISH, the upload file) | **−1.26 dBTP**, −1.2889 dBFS sample, flat factor 0 (unchanged) |
| Peak (FINAL / MIXED) | −3.23 / −3.21 dBTP (unchanged) |
| Black segments | **0** in 15,444 frames, two thresholds (unchanged) |
| Only delta vs attempt 3 | video bitrate −580 bit/s (−0.005 %), i.e. the deleted bar |
| Encode / mix run by this stage | **none** |

## Verdict

**PASS — no regression.** The two-line deletion changed runtime, VO placement, levels and black
content by exactly nothing. `renders/PUBLISH-1080p-hi.mp4` (783,785,801 B) is re-approved as the
upload file; the en cut is not blocked by this one.
