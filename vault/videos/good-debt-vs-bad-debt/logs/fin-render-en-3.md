---
slug: good-debt-vs-bad-debt
stage: fin-render
cut: en
tier: short
attempt: 3
invocation: 2 of 2 (POST-ENCODE MASTER QA — orchestrator owns the encode)
status: PASS
updated: 2026-07-29
scope: Gate-two master QA on renders/FINAL-1080p-en.mp4 (orchestrator ran the chunked encode between invocations; NO encode run here). Frame gate was cleared in attempt-1 invocation-1 ([[fin-render-en-1]]); this invocation is runtime / VO-content / VO-placement-drift / audio-level / black-scan QA of the shipped master.
---

# fin-render — good-debt-vs-bad-debt · en · attempt 3 · invocation 2 (POST-ENCODE MASTER QA)

## Result — MASTER QA: PASS
The en master is deliverable. Runtime within half a frame of timing.json; all 9 VO
segments present, in order, content-correct, with the floor-independent hero anchors
spoken and the false-precise on-screen-only integers (215 months / $9,506) absent from
narration; VO placement drift well under the 0.1 s gate with zero accumulation over 178 s;
true peak −4.74 dBTP (broadcast-safe, 3.7 dB under the −1 ceiling); zero black segments.

## Master under test
- renders/FINAL-1080p-en.mp4 · 273,105,076 bytes (260.5 MB)
- h264 High @ 1920×1080, 30 fps, 5358 frames, 12.2 Mb/s video; aac 48 kHz stereo
- ffprobe: video 178.600 s, audio 178.602667 s, container 178.602667 s

## 1 · Runtime vs timing.json — PASS
- Master video 178.600 s (5358 frames / 30 fps = 178.60 s exact); audio 178.603 s.
- timing.json total = 178.582 s; index.html data-start VO grid matches timing exactly (0.4 / 19.171 / 30.42 / 53.501 / 79.143 / 99.194 / 116.555 / 144.522 / 161.621).
- Delta = +0.018 s video (+0.021 s audio) = ~0.54 frame @ 30 fps. Renderer rounds the 178.582 s composition up to a whole frame count (178.582 × 30 = 5357.46 → 5358 → 178.60 s). Sub-frame, expected. MATCH.

## 2 · VO content vs the 9 script-en segments — PASS (9/9)
faster-whisper "small" (int8, lang=en, beam=1, VAD off) on the master; 56 segments diffed
against the 9 script paragraphs. All nine present, in order, content matches. Every hero
number is spoken as its floor-independent ROUND anchor:
- **en1 month-1 split (hero):** "$170" · "$110 of that is pure interest" · "$60 comes off what you owe" — exact. "$6,000 balance" spoken.
- **en7 (hero math):** "$6,000 balance at around 22%" · "a year in, twelve payments made, you still owe over $5,000" (= over $5,000 after a year) · "you stay in debt the better part of two decades" · "pay more in interest than you borrowed" · "on $6,000, that's over $9,000 in interest".
- **en8 move:** "pay the minimum plus at least $20" — the +$20 action spoken.
- **ABSENCE check (the hero-math guard):** the false-precise on-screen-only integers **215 MONTHS** and **$9,506** are NOT spoken anywhere in the VO — narration carries "the better part of two decades" (not 215) and "over $9,000 in interest" (not $9,506); the on-screen "$5,318 owed" is spoken as the rounded "over $5,000". The exact integers live on screen only, exactly as the script's hero-math doctrine requires. Confirmed across the full transcript.

## 3 · VO placement drift — PASS (max raw +0.093 s; encode-isolated +0.022 s; gate ≤0.1 s)
Method (same as [[fin-render-hi-3]]): ffmpeg silencedetect (noise −40 dB) speech onset per
scene on the master, minus data_start, minus each source clip's intrinsic head-lead
(silencedetect on en1–en9.mp3 — only clips that begin with a leading silence have a
non-zero lead; clips that open on speech have head-lead ≈ 0, their first silence being a
mid-clip pause).

| scene | data_start | master onset | raw Δ | src head-lead | encode drift |
|---|---|---|---|---|---|
| en1 | 0.400   | 0.4607   | +0.0607 | 0.0394 | +0.0213 |
| en2 | 19.171  | 19.2036  | +0.0326 | 0.000  | +0.0326 |
| en3 | 30.420  | 30.4603  | +0.0403 | 0.000  | +0.0403 |
| en4 | 53.501  | 53.5224  | +0.0214 | 0.000  | +0.0214 |
| en5 | 79.143  | 79.2016  | +0.0586 | 0.0373 | +0.0213 |
| en6 | 99.194  | 99.2154  | +0.0214 | 0.000  | +0.0214 |
| en7 | 116.555 | 116.6480 | +0.0930 | 0.0713 | +0.0217 |
| en8 | 144.522 | 144.5480 | +0.0260 | 0.000  | +0.0260 |
| en9 | 161.621 | 161.6420 | +0.0210 | 0.000  | +0.0210 |

- **Raw placement drift (onset − data_start): max +0.093 s (en7), all ≤ 0.093 s ≤ 0.1 s → PASS.** This is the literal contract metric (VO placement vs the data-start table).
- **Encode-isolated drift:** the 3 clips with a measurable leading silence (en1, en5, en7) collapse to a flat +0.021–0.022 s — the constant silencedetect threshold-crossing offset between the 44.1 kHz-mono mp3 source and the 48 kHz-stereo master. en7's large raw +0.093 s is dominated by that clip's 0.071 s baked-in head-lead; its true encode placement error is +0.022 s. The 6 speech-first clips (no leading silence to subtract) bound at ≤ +0.040 s (en3).
- **Zero accumulation:** en9 (+0.021 s @ 161.6 s) ≈ en1 encode drift (+0.021 s @ 0.46 s). No timeline growth over 178 s — the chunked encode preserved A/V sync end-to-end.
- Whisper segment starts confirm CONTENT and ORDER but are heavily quantized (many snapped to *.820 s), so they are not the sub-0.1 s drift metric — silencedetect is.

## 4 · Audio levels — PASS (peak gate) · loudness reported (not a gate)
- **True peak −4.74 dBTP** (loudnorm input_tp, 4× oversample) = −4.7 dBFS (ebur128 true-peak) = −4.742840 dBFS sample peak (astats, both channels identical). True peak == sample peak → no inter-sample overshoot (mono VO → dual-mono stereo). **Under the −1 dBTP ceiling by 3.74 dB → PASS.**
- **Integrated −21.0 LUFS** (ebur128) / −21.09 LUFS (loudnorm input_i). LRA 3.2–3.4 LU; input_thresh −31.6; RMS −24.71 dB. Comparable to the hi cut (−22.0 LUFS). Per the task this is NOT a gate fail — the peak gate passes with 3.7 dB to spare; the orchestrator handles an optional pre-publish loudness lift toward ~−14 LUFS (a straight +7 dB gain would clip, so lift via loudnorm to −14 LUFS with a −1 dBTP ceiling). Reported for reference only.

## 5 · Black-segment scan — PASS
ffmpeg blackdetect d=0.10 pix_th=0.10 over all 5358 frames: zero black_start events. No
black frames / dropouts at transitions (every scene carries a full-bleed .bg under the
grade; scene changes are opacity fades, never to black).

## Measured summary (the artifact)
- Runtime: **178.60 s** (target 178.582 s; delta +0.018 s / 0.54 frame) — MATCH
- Max VO drift: **+0.093 s raw placement** (en7, dominated by that clip's 0.071 s head-lead); encode-isolated +0.022 s systematic (≤ +0.040 s bound); zero accumulation — PASS (≤0.1 s)
- True peak: **−4.74 dBTP** (ceiling −1) — PASS; Integrated **−21.0 LUFS** (reported, not a gate)
- Black segments: **0** — PASS
- VO content: **9/9** correct; hero anchors spoken ($170/$110/$60; over $5,000 after a year; better part of two decades; more in interest than borrowed; +$20); on-screen-only 215 months / $9,506 correctly ABSENT from VO

## Verdict
MASTER QA: PASS. The en cut is deliverable.

NEXT: orchestrator ships good-debt-vs-bad-debt-en (renders/FINAL-1080p-en.mp4); optional loudness lift to ~−14 LUFS before publish; then post-delivery cleanup per vault/CLAUDE.md.
