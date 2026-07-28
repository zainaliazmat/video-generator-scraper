---
summary: "fin-render QA of FINAL-1080p-en.mp4 — frame check 9/9 pass, VO drift 0.021s (xcorr), peak -3.91 dBTP, runtime +0.041s vs timing.json. PASS."
updated: 2026-07-28
source: fin-render agent, attempt 1 (encode run by orchestrator)
---

# fin-render — pay-yourself-first · en · attempt 1

Master: `studio/videos/pay-yourself-first-en/renders/FINAL-1080p-en.mp4`
285,625,246 B (272 MB) · h264 1920x1080 30fps · AAC 48 kHz stereo · 12.85 Mb/s

## Gate two — frame check (from master, one frame per scene at last cue)

| scene | t (s) | verdict |
|---|---|---|
| s1 | 15.3 | pass — dollar-bill bg, EMPTY BY THE 20TH?, 1-IN-4 statstrip, BofA Nov 2025 foot, EVERY MONTH stamp |
| s2 | 29.9 | pass — 4 roadmap chips + "Works even at 5%", photo-free navy |
| s3 | 46.8 | pass — old formula struck red, INCOME − SAVINGS = EXPENSES green, FLIP THE FORMULA |
| s4 | 63.5 | pass — Babylon 1926 chip + quote, START WITH 10% chip; candle grade override reads fine |
| s5 | 83.6 | pass — DOORDASH/THE SALE/CARD BALANCE chips, MEDIAN PAY $1,251/WK, $1.00 EARNED → 3¢ SAVED (¢ renders), BLS+BEA foot |
| s6 | 105.7 | pass — HIGH-YIELD SAVINGS / DIFFERENT BANK / FDIC INSURED rails, 10x sub (ASCII x), clock bg |
| s7 | 135.5 | pass — $4,800 en-US grouping, 12/12 green ticks, $400 auto-save card, START AT 5% $200/MO + IN A YEAR $2,400, Fed SHED foot |
| s7 mid | 118.9 | pass — mid-count reads $2,400 / 6 ticks, clean multiple |
| s8 | 149.8 | pass — OPEN BANKING APP → SCHEDULE THE TRANSFER → DAY AFTER PAYDAY chip flow, 5% sub, dollar-fan bg (no grade override, correct for en) |
| s9 | 176.4 | pass — 4 recap chips, "the 20th won't scare you" sub, SUBSCRIBE CTA, city-window bg |

No safe-area violations, no brand logos in imagery, US-dollar imagery only (correct
currency for the en cut), no phone screens.

## QA numbers

- **Runtime:** 177.813 s (container) vs timing.json total 177.772 s → **+0.041 s** (AAC priming/padding; pass)
- **True peak:** loudnorm input_tp **−3.91 dBTP** (limit < −1 dBTP → pass); input_i −21.13 LUFS, LRA 3.2
- **VO drift (cross-correlation of each en*.mp3 vs master, authoritative):** all nine
  lines at **+0.021 s** uniform (AAC priming delay) → max abs drift **0.021 s** ≤ 0.1 s (pass).
  The long en7 clip (29.074 s) flagged by fin-build sits at the same +0.021 s — no accumulation.
- **VO drift (faster-whisper `small`, en, word timestamps):** onsets −0.02…−0.51 s,
  mean −0.35 s — the known systematic whisper onset bias (breath lead-in), same as
  the hi cut; per-line first words all match the script order (Quick/Four/Most/The/
  So/The/Now/So/So). Cross-correlation is the authoritative number.
- **blackdetect (d=0.3, pix_th=0.10):** two windows — 20.03–24.07 s (s2) and
  108.30–117.00 s (s7). Both are the photo-free dark-navy scenes; frames at 22.0 s
  ("BY THE END YOU'LL KNOW" + first chip) and 112.0 s ("NOW THE MATH" + take-home
  sub) show live text. False positives of the dark design, no dead air.

## Verdict

**PASS** — master approved for delivery.
