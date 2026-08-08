---
summary: TTS + measured timing for japanese-money-methods-hi. 92 clips generated in one batch.py pass (92 ElevenLabs calls, zero retries); measured total 659.71s against the 660s target, −0.04%. All batch.py postconditions passed.
updated: 2026-08-01
source: vault/videos/japanese-money-methods/script-hi.md (post-fin-audit-hi-1), tools/format.json cuts.hi + tiers.long
stage: fin-voice, cut hi, attempt 1
---

# fin-voice-hi — attempt 1

STATUS: ok

## Cost guard — cleared before any spend

| Gate | Result |
|---|---|
| `audit-hi.md` contains PASS | ✅ line 10, "PASS", after four direct edits |
| Char total vs 1.3× budget | ✅ 7,596 measured vs 11,180 ceiling (660 × 13.03 × 1.3) — 68% of the cap |

Char total is `timing.json`'s own programmatic recount (sum of `chars`), not the
script's estimate: **7,596** against the script's stated 7,598. The two-character
gap is the script table's ±5% budget estimate landing almost exactly.

## What ran

```
python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-hi --cut hi
```

- Voice `HTUuC7OeeEt6OL5fViVe` (Harsh), `eleven_multilingual_v2`, style 0 — all read
  from `tools/format.json`, nothing hardcoded.
- **92 API calls, 92 clips, zero failures, zero retries.** No clip pre-existed, so
  nothing was skipped and nothing was re-spent.
- `run.json budget.elevenlabs_calls` 0 → **92**; 129 of 221 remain for the -en cut.
- Exit 0. batch.py's own postconditions (min bytes, min seconds, duration-vs-chars
  within ±35%, silent-clip guard, scene arithmetic) all passed — the run printed no
  `✗` lines.

## Extraction

`assets/voice/lines.json` — ordered `[{"id","text"}]`, **92 entries `1.1 … 8.8`**,
matching the chapter counts in the script's own table (10 · 11 · 12 · 13 · 12 · 14 ·
12 · 8 = 92). VO strings only: no markdown, no `head:`/`stmt:`/`foot:` cue text, no
`[AUDIT …]` notes. The warning blockquote above `# THE SCRIPT` (build-handoff hazard
§1) was **not** swept in — extraction keyed off the `**N.N**` markers, so the
English/Latin-digit box never entered the VO set.

Generated from the **current** file on disk, so the four fin-audit-hi-1 rewrites are
in the audio as edited:

| Line | chars | measured | Carries the audit edit |
|---|---|---|---|
| 1.2 | 93 | 6.400s | the 15-second promise clause ("जापान के तीन तरीक़े हैं") |
| 3.8 | 88 | 6.165s | the "युद्ध के बाद" postwar qualifier |
| 3.9 | 98 | 7.602s | "शायद ही कभी" (softened from "कभी … नहीं") |
| 6.14 | 97 | 7.523s | placement disclaimed; PPF rate as scale only |

## Runtime vs target

| | |
|---|---|
| Measured total (`timing.json.total`) | **659.709s** (10:59.7) |
| Target (`run.json target_seconds`) | 660s |
| Drift | **−0.291s, −0.04%** |
| LONG `min_seconds` 600 | clear by 59.7s |
| Padding charged | 0.25 lead-in + 0.55 tail per line = 73.6s (`tiers.long`, **not** the `scene.*` 0.4/1.0 SHORT defaults) |
| Pure audio | 586.1s |
| Mean scene | 7.17s (`target_scene_seconds` 6.5) |
| Longest scene | 3.11 at **9.760s** ⚠ see below |

The script's estimate was 656.7s; delivery came in 3.0s longer — a **0.46% modelling
error over eleven minutes**. `cuts.hi.chars_per_second` 13.03 is confirmed again, this
time on a LONG cut: 7,596 / 586.1 = **12.96 c/s** flat delivered.

## Largest per-line drift

Measured against `pipeline_check.expected_seconds` (flat chars/13.03 **plus**
`tts.pause_seconds` for each non-trailing mark), which is the check that actually
gates. Tolerance is ±35%; nothing came close.

| Line | chars | expected | measured | drift |
|---|---|---|---|---|
| **2.10** | 88 | 7.45s | 5.878s | **−21.1%** ← largest |
| 5.8 | 99 | 8.30s | 6.818s | −17.8% |
| 7.5 | 79 | 6.61s | 5.433s | −17.8% |
| 4.4 | 84 | 6.60s | 5.381s | −18.4% |
| 4.7 | 78 | 6.14s | 5.094s | −17.0% |
| 4.12 | 99 | 8.20s | 6.818s | −16.8% |
| 3.11 | 102 | 8.43s | 8.960s | +6.3% ← largest positive |
| 7.1 | 57 | 5.08s | 5.564s | +9.6% |

Every one of the six biggest misses is **negative** and every one is a line whose
expected value is inflated by a mid-sentence danda or em-dash. Harsh reads those marks
shorter than `tts.pause_seconds` models them when the clause on either side is long —
the tabled pauses were tuned on the cold-open hook, which is short punched clauses. Not
a defect and not worth a constant change on one cut's evidence: the total lands −0.04%
off target, so the model is right in aggregate and only its *distribution* is slightly
off. Worth re-checking after the -en cut measures.

## For fin-build-hi

1. **`timing.json` is the single source.** 92 entries with MEASURED durations,
   `scene_start` / `scene_duration` / `audio_start` already computed. Derive all four
   timing copies from it; never hand-edit a duration (the ffprobe cross-check will
   catch it).
2. ⚠ **3.11 is 9.760s of scene, over `scene.max_scene_seconds` 9.0.** 3.4 (9.002s) and
   2.9 (9.185s) sit on the line too. `check_build` fails a scene that holds **one photo**
   past 9.0 — so these three need a cut-in or a second framing inside the scene, not a
   re-record. The script's own budget flagged 3.11 at 7.8s; the five-item comma list
   (`वजह थी उधार … अभियान।`) delivered 1.1s longer than the flat rate predicted.
   This is a build-side fix, not a voice-side one: the audio is correct.
3. Three continuous-zoom holds — **1.1→1.2 (11.6s), 6.7→6.8 (14.3s), 7.4→7.5 (14.4s)** —
   each needs ONE continuous zoom across both scenes with a tighter crop on the second,
   never a self-dissolve (creator rule, firaun 2026-07-23).
4. `gen_vo_hi.sh` derives the repo root from its own path rather than hardcoding an
   absolute `cd` — the archive gotcha in `vault/CLAUDE.md` §5. It resumes per clip, so
   re-running it after a single deleted mp3 costs one call, not 92.
