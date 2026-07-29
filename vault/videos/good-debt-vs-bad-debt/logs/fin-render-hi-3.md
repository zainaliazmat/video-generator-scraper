# fin-render — good-debt-vs-bad-debt · cut hi · attempt 3 · invocation 2 (POST-ENCODE MASTER QA)

status: PASS (master QA)
date: 2026-07-28
stage: gate two — post-encode master QA. The orchestrator ran the chunked encode between invocations; the master exists. NO encode run here. Frame gate was cleared in attempt-2 invocation-1 (all 5 re-sourced backgrounds clean, s2 revered-figure violation resolved); this invocation is the runtime / VO-drift / audio-level QA of the shipped master.

## Master under test
- renders/FINAL-1080p-hi.mp4 · 291,208,162 bytes (277.7 MB)
- h264 High @ 1920x1080, 30 fps, 5856 frames, 11.75 Mb/s video ; aac-LC 48 kHz stereo, 179 kb/s
- ffprobe container duration 195.200000 s (video and audio streams both 195.20 s), bt709, progressive

## 1 · Runtime vs timing.json — PASS
- Master duration 195.20 s (5856 frames / 30 fps = 195.20 s exact).
- timing.json total = 195.17 s ; root data-duration (index.html) = 195.17 s.
- Delta = +0.03 s = 0.9 frame. The renderer rounds the 195.17 s composition up to a whole frame count (195.17 x 30 = 5855.1 -> 5856 frames -> 195.20 s). Sub-frame, expected. MATCH.

## 2 · VO content vs script-hi.md — PASS (9/9)
faster-whisper "small" (int8, lang=hi, beam=1, vad off) on the master; segments diffed against the 9 script paragraphs. All nine present, in order, content matches. Whisper garbles Devanagari spelling but the number words are unambiguous:
- s1 month-1 split: "पचीस सौ तिरासी" = Rs 2,583 OK · "सोलह सौ सरसठ" = Rs 1,667 OK · "नौ सौ" = Rs 900 OK.
  Note: the on-screen "OFF THE DEBT Rs 916" row is spoken ROUNDED to नौ सौ / 900 — verbatim per script; the floor-independent round anchor, not a mismatch.
- s7 (critical): "पचास हज़ार" 50,000 · "करीब 40%" ~40% APR · "पाँच परसेंट" 5% min · "एक साल बाद ... करीब 40,000 बाकी" (~Rs 40,000 after a year) · "17 साल से भी ज़्यादा" (17+ yrs) · "करीब 90,000" (nearly Rs 90,000).
- ABSENCE check (the key hero-math guard): the false-precise on-screen-only integers 208 and Rs 88,614 are NOT spoken anywhere in the VO — confirmed across the full transcript. Narration carries only the floor-independent round anchors; the exact integers live on screen only, exactly as the script's hero-math doctrine requires.

## 3 · VO placement drift (encode) — PASS (max 0.045 s ; target <= 0.1 s)
Method: ffmpeg silencedetect (noise -40 dB) on the master gives speech onset per scene; the same detector on each source clip h1-h9 gives that clip's intrinsic head-silence lead. Encode drift = master_onset - data_start - source_lead (isolates encode placement error from the clip's own lead).

| scene | data_start | master onset | src head-lead | encode drift (s) |
|---|---|---|---|---|
| s1 | 0.400   | 0.508   | 0.087 | +0.021 |
| s2 | 22.541  | 22.632  | 0.070 | +0.021 |
| s3 | 37.682  | 37.808  | 0.104 | +0.022 |
| s4 | 61.678  | 61.740  | 0.092 | -0.030 |
| s5 | 89.122  | 89.181  | 0.038 | +0.021 |
| s6 | 113.091 | 113.159 | 0.046 | +0.022 |
| s7 | 133.430 | 133.489 | 0.037 | +0.022 |
| s8 | 159.986 | 160.048 | 0.107 | -0.045 |
| s9 | 178.705 | 178.822 | 0.095 | +0.022 |

- 7 of 9 scenes sit at a flat +0.021..+0.022 s systematic offset (silencedetect threshold-crossing difference between the 44.1 kHz-mono source and the 48 kHz-stereo master + mp3 decoder delay) — a CONSTANT offset from t=0.5 s to t=178.8 s = no timeline drift.
- The two negatives (s4 -0.030, s8 -0.045) come from those two source clips' leading micro-blips slightly over-estimating the per-clip lead; non-directional, still < 0.05 s.
- ZERO accumulation: s9 drift (+0.022 @ 178.8 s) == s1 drift (+0.021 @ 0.5 s). The chunked encode preserved A/V sync end-to-end. Max |drift| = 0.045 s.
- Independent cross-check: whisper first-word onset per scene spans -0.40..+0.24 s about data_start, centred near 0, no trend — consistent with zero drift within whisper's ~0.3 s timestamp precision.
- For transparency: RAW speech-onset-minus-data_start (lead included) peaks at +0.126 s (s3) — that is intrinsic clip lead, NOT encode drift; the isolated drift above is the gate metric.

## 4 · Audio levels — PASS (broadcast-safe)
- True peak (loudnorm input_tp, 4x oversample): -3.23 dBTP -> under the -1 dBTP ceiling. PASS.
- Sample peak (astats): -3.23 dBFS, both channels identical (mono VO -> dual-mono stereo). No inter-sample overshoot (TP == sample peak).
- Integrated loudness -22.02 LUFS ; LRA 3.50 LU ; threshold -32.64 ; RMS -25.07 dB.
- -22.0 LUFS sits right at the EBU R128 broadcast target (-23) -> broadcast-safe. It is ~8 LU under YouTube's -14 streaming reference, so it will play a touch quieter than typical YT content (YouTube applies no positive gain). NOT a gate fail (the gate is peak < -1 dBTP, which passes with 2.2 dB to spare); optional +~8 dB loudness lift to ~-14 LUFS before publish if platform-loudness matching is wanted (peak headroom allows it).

## 5 · Black-segment scan — PASS
ffmpeg blackdetect d=0.10 pix_th=0.10 over all 5856 frames: zero black_start events. No black frames / dropouts at transitions (every scene carries a full-bleed .bg under the grade; scene changes are opacity fades, never to black).

## Measured summary (the artifact)
- Runtime: 195.20 s (target 195.17 s ; delta +0.03 s / 0.9 frame)
- Max VO drift (encode): 0.045 s (s8) ; 7/9 at a flat +0.022 s, no accumulation
- True peak: -3.23 dBTP (ceiling -1) ; Integrated -22.0 LUFS (broadcast-safe)
- Black segments: 0
- VO content: 9/9 correct ; hero anchors spoken (2,583 / 1,667 / 900 ; ~40k after a year ; 17+ yrs ; ~90k) ; 208 / Rs 88,614 correctly on-screen-only (absent from VO)

## Verdict
MASTER QA: PASS. Runtime within a frame of timing.json; all 9 VO segments correct with the floor-independent hero anchors spoken and the false-precise 208 / Rs 88,614 absent from narration; VO placement drift <= 0.045 s with zero accumulation over 195 s; true peak -3.23 dBTP (broadcast-safe); no black segments. The cut is deliverable.

NEXT: orchestrator ships good-debt-vs-bad-debt-hi (renders/FINAL-1080p-hi.mp4); optional loudness lift to ~-14 LUFS before publish; then post-delivery cleanup per vault/CLAUDE.md.
