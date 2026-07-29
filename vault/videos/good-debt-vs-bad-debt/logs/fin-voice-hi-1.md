---
summary: fin-voice hi attempt 1 — 9 clips generated (9 ElevenLabs calls), measured total 195.17s. All batch.py postconditions pass. Flag downstream: runs +30s over the 165s target (in-range) and s1 audio is 20.7s, so the audit's s1 split-≤15s advisory applies.
updated: 2026-07-28
source: tools/tts/batch.py run (voice Harsh HTUuC7OeeEt6OL5fViVe, eleven_multilingual_v2, style 0)
---

# fin-voice — good-debt-vs-bad-debt / hi / attempt 1

STATUS: ok · 9 API calls (h1..h9, fresh project — no resume/skips)

## Gate (refused-before-spending checks)
- `audit-hi.md` records **PASS** (line 9) — gate clears.
- Char total of the sliced VO = **2,267** chars. Cap = 1.3 × (165s × 12.5 c/s) = **2,681**. Under cap → allowed to spend.
  - Note: 2,267 is above the audit's assumed ~2,070 (the audit trusted the script's rough per-scene estimate table, not a real count) but still inside the audit's own stated ±10% band (upper 2,269) and well under the 1.3× refuse cap.

## What ran
1. Sliced the 9 VO blockquotes (the line after each `**VO**`) out of `script-hi.md` into `lines.json`, ids `h1..h9` positional to `s1..s9`. **Programmatic slice, not retyped** — each of the 9 strings re-verified as a verbatim substring of `script-hi.md` (nukta chars ख़/ज़/क़/फ़ preserved). No markdown, on-screen text, stage directions, or digits (script spells all numbers out in Devanagari) leaked in.
2. `python3 tools/tts/batch.py --project studio/videos/good-debt-vs-bad-debt-hi --cut hi` → exit **0**. Generated 9 mp3s, ffprobed each, wrote `timing.json` atomically with MEASURED durations + scene arithmetic (scene_start cumulative; scene_duration = 0.4 lead + clip + 1.0 tail; audio_start = scene_start + 0.4). `check_voice_dir` postconditions (size ≥10 KB, dur ≥1.0s, ffprobe cross-check ≤0.05s, dur-vs-chars ≤35%, silence, scene math) all clean — zero `✗`.
3. Wrote `gen_vo_hi.sh` (fresh, this project's own `--project` path — not copied from another cut).

## Measured timing (ffprobe, 12.5 c/s reference)
| id | chars | measured | est | drift |
|----|------:|---------:|----:|------:|
| h1 | 246 | 20.741 | 19.68 | **+1.06 (+5.4%)** |
| h2 | 173 | 13.740 | 13.84 | -0.10 |
| h3 | 271 | 22.596 | 21.68 | +0.92 |
| h4 | 320 | 26.044 | 25.60 | +0.44 |
| h5 | 287 | 22.570 | 22.96 | -0.39 |
| h6 | 240 | 18.939 | 19.20 | -0.26 |
| h7 | 314 | 25.156 | 25.12 | +0.04 |
| h8 | 223 | 17.319 | 17.84 | -0.52 |
| h9 | 193 | 15.464 | 15.44 | +0.02 |

- Pure audio 182.57s; **timing.json total 195.17s** (adds 9 × 1.4s lead/tail).
- **vs target 165s: +30.2s (118.3%)** — inside tier `short` range [60, 300]s.
- Largest per-line drift: **h1 +1.06s (+5.4%)**, far inside the ±35% guard. Harsh tracks 12.5 c/s tightly.

## Flags for downstream (storyboard/build)
- **s1 audit advisory now measurable:** audit check 3 required s1's interest/principal split (₹2,583/₹1,667/₹916) to be on screen ≤15s. h1 audio is **20.74s**; the "…सोलह सौ सरसठ सिर्फ़ ब्याज" interest clause lands mid-clip (~13–14s in). Build must reveal the on-screen focal split as the numbers are spoken, not gate it to clip end.
- **Runtime +30s over the 165s target** (in-range, not a fail). If the orchestrator wants closer to 2:45, the script would need a trim (audit-frozen — out of scope for voice). Otherwise ship as-is; 3:15 is valid for a `short`.

## Artifacts
- `studio/videos/good-debt-vs-bad-debt-hi/assets/voice/lines.json`
- `studio/videos/good-debt-vs-bad-debt-hi/assets/voice/timing.json`
- `studio/videos/good-debt-vs-bad-debt-hi/assets/voice/h1.mp3` … `h9.mp3` (+ per-line `.txt`)
- `studio/videos/good-debt-vs-bad-debt-hi/gen_vo_hi.sh`
