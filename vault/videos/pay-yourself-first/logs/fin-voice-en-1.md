---
summary: fin-voice en attempt 1 — 9/9 Brian clips generated, timing.json measured; VO total 165.17s vs 165s target, scene total 177.77s. Largest per-line drift en9 (+2.0s vs char estimate).
updated: 2026-07-28
source: tools/tts/batch.py run 2026-07-28 (9 ElevenLabs calls, eleven_multilingual_v2, voice nPczCjzI2devNBz1zQrb)
---

# fin-voice — pay-yourself-first / en / attempt 1

## Cost guard
- audit-en.md: PASS present ✓
- Char total: 2,544 (batch-counted) vs cap 3,217 (1.3 × 2,475) ✓ — within audit band too (~+2.8%).

## Run
- lines.json: 9 segments (en1..en9) sliced verbatim from script-en.md (audit-edited version).
- batch.py: 9/9 OK, no retries, no skips (fresh project). Postconditions self-verified (size, duration-vs-chars, silence, scene arithmetic).
- timing.json written atomically with measured durations.

## Measured timing
| id | chars | duration | est (c/15) | drift |
|---|---|---|---|---|
| en1 | 297 | 18.63 | 19.80 | −1.18 |
| en2 | 143 | 9.61 | 9.53 | +0.08 |
| en3 | 260 | 19.17 | 17.33 | +1.84 |
| en4 | 195 | 11.96 | 13.00 | −1.04 |
| en5 | 348 | 21.34 | 23.20 | −1.86 |
| en6 | 312 | 19.17 | 20.80 | −1.63 |
| en7 | 456 | 29.07 | 30.40 | −1.33 |
| en8 | 287 | 17.82 | 19.13 | −1.32 |
| en9 | 246 | 18.39 | 16.40 | **+1.99** (largest) |

- VO sum: **165.17s** vs 165s target (+0.17s, +0.1%).
- Scene total (with 0.4s lead-ins + 1.0s tails): **177.77s** — inside the short-tier 60–300s range.

## Artifacts
- studio/videos/pay-yourself-first-en/assets/voice/lines.json
- studio/videos/pay-yourself-first-en/assets/voice/en1..en9.mp3
- studio/videos/pay-yourself-first-en/assets/voice/timing.json
- studio/videos/pay-yourself-first-en/gen_vo_en.sh

## Spend
9 ElevenLabs calls this run; orchestrator budget now 18/30.
