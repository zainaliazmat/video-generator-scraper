---
summary: fin-voice hi attempt 1 — 9/9 ElevenLabs clips generated (Harsh, eleven_multilingual_v2), timing.json measured, postconditions pass. VO 166.3s vs 165s target.
updated: 2026-07-28
source: tools/tts/batch.py run 2026-07-28
---

# fin-voice — pay-yourself-first / hi / attempt 1

STATUS: ok

## Cost guard (verified before spending)
- audit-hi.md read directly: contains PASS (all 8 checks).
- Char total (from batch.py, exact): 2,097 vs budget 2,062 (165s × 12.5) —
  1.02×, well under the 1.3× refuse line (2,681).

## Run
- lines.json: h1..h9 sliced verbatim from script-hi.md VO blocks (no markdown,
  no on-screen text). Voice HTUuC7OeeEt6OL5fViVe (Harsh), model
  eleven_multilingual_v2, style 0 — all from tools/format.json.
- batch.py: 9 API calls, 9 clips written, ffprobed, timing.json atomic,
  postconditions all pass (exit 0).

## Measured vs estimate (12.5 c/s)
| id | chars | est s | meas s | drift |
|---|---|---|---|---|
| h1 | 188 | 15.04 | 14.34 | −0.70 |
| h2 | 148 | 11.84 | 10.53 | −1.31 (−11.1%, largest %) |
| h3 | 275 | 22.00 | 23.72 | +1.72 (largest abs) |
| h4 | 189 | 15.12 | 14.66 | −0.46 |
| h5 | 263 | 21.04 | 20.32 | −0.72 |
| h6 | 240 | 19.20 | 20.32 | +1.12 |
| h7 | 314 | 25.12 | 25.91 | +0.79 |
| h8 | 234 | 18.72 | 17.32 | −1.40 |
| h9 | 246 | 19.68 | 19.17 | −0.51 |

- VO total (sum of clip durations): **166.29s** vs 165s target (+0.8%).
- Scene total incl. 0.4s lead + 1.0s tail per scene: **178.90s**.
- All lines inside the 35% duration-vs-chars tolerance.

## Flag for proof stage
h5 and h6 report identical size (325,634 B) and duration (20.323s) despite
different texts — almost certainly CBR-mp3 coincidence (silence check passed on
both), but listen to h6 during chapter proofing to confirm it is not a
duplicated take.
