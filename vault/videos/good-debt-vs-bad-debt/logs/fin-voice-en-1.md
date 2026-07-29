---
summary: fin-voice en (US, Brian) attempt 1 — 9 VO clips generated, timing.json measured. Spoken 165.98s (≈ on the 165s target); scene timeline 178.58s incl. 0.4/1.0 padding. All batch.py postconditions passed; 9 ElevenLabs calls made.
updated: 2026-07-28
source: tools/tts/batch.py run (exit 0) + independent ffprobe; inputs script-en.md + audit-en.md (PASS) + format.json cuts.en
---

# fin-voice — good-debt-vs-bad-debt / en / attempt 1

STATUS: ok · 9 ElevenLabs API calls (en1..en9, all fresh — none skipped).

## Cost guard (both cleared before spend)
- audit-en.md records **PASS** (line 9).
- Script chars 2,528 (batch-counted) vs ceiling 1.3 × (165s × 15 c/s = 2,475) = **3,217.5**. Well under. Also inside the plain ±10% band 2,228–2,722.

## What ran
- Sliced the 9 `**VO**` blockquotes from script-en.md **verbatim** into `assets/voice/lines.json` (ids `en1..en9`, matching the en script's section titles + build-handoff #1). Verified byte-exact: all 9 text values found verbatim in script-en.md (grep -F, 0 drift). Glyph convention confirmed straight apostrophes (0x27) + em-dash (U+2014); no digits in VO (numbers spelled out).
- `python3 tools/tts/batch.py --project studio/videos/good-debt-vs-bad-debt-en --cut en` → exit 0. Voice Brian `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0 (all from format.json — nothing hardcoded). batch.py wrote each `enN.txt` + `enN.mp3`, ffprobed, wrote `timing.json` atomically, and self-verified postconditions (size ≥10KB, dur ≥1s, timing==ffprobe ±0.05, ±35% char/rate, non-silent, scene arithmetic, total). No `✗`.
- Independent ffprobe re-measure of all 9 matches timing.json to the millisecond.

## Measured timing (rate 15 c/s; drift = measured − chars/15)
| id | chars | est s | measured s | drift s | drift % |
|----|------:|------:|-----------:|--------:|--------:|
| en1 | 289 | 19.27 | 17.371 | -1.90 | -9.8 |
| en2 | 152 | 10.13 | 9.848 | -0.28 | -2.8 |
| en3 | 287 | 19.13 | 21.682 | +2.55 | +13.3 |
| en4 | 327 | 21.80 | 24.242 | +2.44 | +11.2 |
| en5 | 331 | 22.07 | 18.651 | **-3.42** | **-15.5** |
| en6 | 260 | 17.33 | 15.961 | -1.37 | -7.9 |
| en7 | 410 | 27.33 | 26.567 | -0.77 | -2.8 |
| en8 | 243 | 16.20 | 15.700 | -0.50 | -3.1 |
| en9 | 229 | 15.27 | 15.961 | +0.69 | +4.5 |

- **Spoken VO total = 165.98s** vs 165s target → **+0.98s (+0.6%)**, essentially on target.
- **Scene timeline total = 178.58s** (timing.json `total`; each scene = 0.4 lead + clip + 1.0 tail → 9×1.4 = 12.6s padding). This is the runtime the build/render will produce (2:58.6) — inside the "short" tier band [60,300]s.
- **Largest per-line drift: en5 −3.42s (−15.5%)** — Brian read en5 at 17.75 c/s (fast); largest positive en3 +2.55s (+13.3%). All inside the ±35% postcondition tolerance.

## Audit advisory (check 3 — hook payoff ≤15s)
en1 measured 17.371s for 289 chars = **16.64 c/s (faster than 15)**. Interest-reveal clause ("…a hundred ten of that is pure interest") lands ~13.2s from scene start (incl. 0.4s lead-in) — inside 15s. Advisory said trim only if slower than 15 c/s; Brian ran faster, so **no trim of en1 needed**.

## Artifacts
- studio/videos/good-debt-vs-bad-debt-en/assets/voice/lines.json
- studio/videos/good-debt-vs-bad-debt-en/assets/voice/timing.json
- studio/videos/good-debt-vs-bad-debt-en/assets/voice/en1.mp3 … en9.mp3 (+ en1.txt … en9.txt)
- studio/videos/good-debt-vs-bad-debt-en/gen_vo_en.sh

## Next
Hand to fin-storyboard-en (scenes en1..en9; scene timings locked in timing.json, total 178.58s). Orchestrator marks fin-voice-en done (freezes script_sha256).
