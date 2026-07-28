---
summary: "fin-render QA of FINAL-1080p-hi.mp4 — frame check 9/9 pass, VO drift 0.021s, peak -3.27 dBTP, runtime +0.005s vs timing.json. PASS."
updated: 2026-07-28
source: fin-render agent, attempt 1 (encode run by orchestrator)
---

# fin-render — pay-yourself-first · hi · attempt 1

Master: `studio/videos/pay-yourself-first-hi/renders/FINAL-1080p-hi.mp4`
275 MB · h264 1920x1080 30fps · AAC 48 kHz stereo · 12.89 Mb/s

## Gate two — frame check (from master, one frame per scene at last cue)

| scene | t (s) | verdict |
|---|---|---|
| s1 | 14.5 | pass — rupee-note bg, EVERY MONTH stamp, drained month bar |
| s2 | 26.5 | pass — 4 roadmap chips + "Works even at 5%", photo-free |
| s3 | 51.1 | pass — old formula struck red, new formula green, FLIP stamp |
| s4 | 65.3 | pass — Babylon chip + quote, safe area OK |
| s5 | 87.2 | pass — Indian market bg, ₹100→₹7, RBI FY25 foot |
| s6 | 108.8 | pass — SALARY IN → AUTO-TRANSFER → SAVED BY 9 AM flow |
| s7 | 136.7 | pass — ₹1,44,000 (en-IN lakh grouping), 12-step bar, ladder card, PLFS foot |
| s8 | 153.9 | pass — barn-wood grade override reads fine, 3-chip flow + payoff |
| s9 | 177.9 | pass — 4 recap chips, sub, SUBSCRIBE CTA (Mumbai skyline bg) |

No safe-area violations, no brand marks, no wrong-currency imagery, no phone screens.

## QA numbers

- **Runtime:** 178.901 s vs timing.json total 178.896 s → **+0.005 s** (pass)
- **True peak:** loudnorm input_tp **−3.27 dBTP** (limit < −1 dBTP → pass); input_i −22.24 LUFS, LRA 3.3
- **VO drift (cross-correlation of each h*.mp3 vs master):** all nine lines at **+21.3 ms** uniform (AAC priming delay) → max abs drift **0.021 s** ≤ 0.1 s (pass)
- **VO drift (faster-whisper `small`, hi, word timestamps):** onsets −0.26…−0.51 s, mean −0.36 s — systematic whisper onset bias (breath lead-in), not placement error; per-line spread ±0.12 s. Cross-correlation is the authoritative number.
- **blackdetect (d=0.3, pix_th=0.10):** two windows — 15.77–19.57 s (s2) and 112.30–122.43 s (s7). Both are the photo-free dark-navy scenes; frames at 18.0 s and 118.0 s show live text (kicker/chip, kicker+sub). False positives of the dark design, no dead air.

## Verdict

**PASS** — master approved for delivery.
