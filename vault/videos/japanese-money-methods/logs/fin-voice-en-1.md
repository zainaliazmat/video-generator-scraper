---
summary: TTS + measured timing for the en cut of japanese-money-methods. 92 clips generated (Brian, eleven_multilingual_v2, style 0), one per VO line, zero retries; timing.json written with ffprobe-measured durations. Runtime 626.59s vs the 660s target (−5.1%), comfortably inside the LONG 600s floor. Delivered flat rate 17.39 c/s against format.json's 16.1 — a second en measurement confirming the trap note.
updated: 2026-08-01
source: studio/videos/japanese-money-methods-en/assets/voice/timing.json (ffprobe-measured), vault/videos/japanese-money-methods/script-en.md, tools/format.json
stage: fin-voice, cut en, attempt 1
---

# fin-voice-en attempt 1

## Cost guard (checked before spending)

| Gate | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | yes (verdict line + frontmatter) | pass |
| Char total vs 1.3 × budget | 9,616 vs 660 × 16.1 = 10,626 → cap 13,814 | pass (0.90× budget) |
| `budget.max_elevenlabs_calls` | 221, with 92 already spent by hi | 92 needed, 37 left after |

## What ran

```
python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-en --cut en
```

Exit 0. 92 clips, one API call each, **zero retries**. `check_voice_dir` reported no
problems — every clip cleared `min_clip_bytes` (10,240), `min_clip_seconds` (1.0),
the ±35% duration-vs-chars tolerance, the −50 dB silence floor, the 0.05s
timing-vs-ffprobe cross-check and the cumulative scene arithmetic.

Generated from the CURRENT `script-en.md` on disk, i.e. **after** the fin-audit-en-1
rewrites of 1.2, 1.5, 3.8, 3.9, 5.7, 6.15 and the orchestrator's 6.14 on-screen-only
edit (6.14's VO is byte-identical to the pre-edit string, as recorded). The six audited
strings were sliced from the post-edit file, so the downstream script/audio hash check
sees one consistent source.

## Artifacts

- `studio/videos/japanese-money-methods-en/assets/voice/lines.json` — 92 entries, `1.1 … 8.8`
- `studio/videos/japanese-money-methods-en/assets/voice/{1.1 … 8.8}.mp3` + `.txt` (92 pairs)
- `studio/videos/japanese-money-methods-en/assets/voice/timing.json` — measured
- `studio/videos/japanese-money-methods-en/gen_vo_en.sh` — regeneration, repo root derived from `$0`

## Measured runtime vs target

| | |
|---|---|
| Chars (programmatic recount) | **9,616** (script table said 9,619 — 3 char drift, immaterial) |
| Audio seconds (sum of 92 clips) | **552.99s** |
| Inter-line padding (92 × 0.25 + 0.55) | **73.60s** |
| `timing.json` total | **626.59s = 10:26.6** |
| Target (`run.json target_seconds`) | 660s |
| Drift | **−33.4s (−5.1%)** |
| LONG floor (`tiers.long.min_seconds`) | 600s → **+26.6s of headroom** |
| Longest scene | 7.6 at 8.35s (`max_scene_seconds` 9.0) — no breach |
| Shortest clip | 1.1 at 3.24s (`min_clip_seconds` 1.0) |

**Delivered flat rate = 9,616 / 552.99 = 17.39 c/s.** `format.json cuts.en.chars_per_second`
is 16.1; the `_chars_per_second_trap` note records 17.73 from
`first-lakh-first-thousand-en`. This is the second independent en measurement and it lands
in the same place: **the key is ~8% slow, and both cuts came in short rather than long
because the script was deliberately sized inside the 16.1/17.73 overlap** (script-en.md
"the two-rate hedge"). The hedge worked: predicted 616.1s at 17.73, delivered 626.6s.

## Per-line drift

`expected = chars / 16.1 + charged pause_seconds` (trailing punctuation charged nothing,
per `pipeline_check.expected_seconds`). Largest misses, all negative:

| Line | chars | interior marks | expected | measured | miss |
|---|---|---|---|---|---|
| 8.3 | 119 | 1 `.` 1 `,` | 8.09s | 6.35s | **−1.74s (−21.5%)** |
| 8.7 | 117 | 2 `,` | 7.57s | 5.85s | −1.72s (−22.7%) |
| 2.2 | 113 | 2 `,` | 7.32s | 5.62s | −1.70s (−23.3%) |
| 4.5 | 102 | 1 `.` 2 `,` | 7.19s | 5.51s | −1.67s (−23.3%) |
| 4.7 | 103 | **none** | 6.40s | 4.73s | −1.67s (**−26.1%**, largest by %) |
| 2.10 | 100 | 1 `.` 1 `,` | 6.91s | 5.28s | −1.63s (−23.6%) |
| 7.11 | 118 | 2 `,` | 7.63s | 6.03s | −1.60s (−20.9%) |
| 1.1 | 68 | 1 `,` | 4.37s | 3.24s | −1.14s (−25.9%) |

**90 of 92 lines miss negative.** The only positives are 6.2 (+0.1%) and 6.11 (+1.6%).
Nothing exceeded the ±35% tolerance, so batch.py flagged nothing.

## The pause_seconds question (answering the hi cut's finding)

**No — the en cut does not reproduce the hi signature, and half of it cannot be tested here.**

1. **There is no em-dash and no danda anywhere in the en VO.** All 92 lines are built from
   commas and full stops only. The mark the hi hypothesis actually hangs on is absent, so
   this cut is silent on it.
2. **The blanket negative miss is a rate-key error, not a pause error.** With the key at
   16.1 against a delivered 17.39, every line is predicted ~8% long before punctuation is
   considered. Attributing that to `pause_seconds` would be reading the wrong constant.
3. **Isolating the pause term:** the nine lines with **zero** interior punctuation deliver
   943 chars in 51.02s = **18.48 c/s** — that is Brian's pure-speech rate with no pause
   charge in it. Re-deriving every line at 18.48 and comparing the residual to the charged
   pause gives:

| Group | charged | actual pause (mean residual) | verdict |
|---|---|---|---|
| comma only (`P` = 0.15) | 0.15s | **+0.17s over** | comma is *under*-charged, if anything |
| one interior `.` (`P` = 0.55) | 0.55s | −0.20s | mild over-charge |
| pause-heavy (`P` ≥ 1.0: 2.7, 3.12, 6.10, 6.12, 7.6, 8.5) | 1.10–1.65s | −0.19s | mild over-charge |

   Per-line noise is ±0.4s, which swamps a systematic term of ~0.2s. **The over-charge, if
   real, sits on the full stop, not on the comma, and it does not grow with clause length**
   — 6.12 (four commas + a period) came in **+0.56s over** charge, while 4.7 (no punctuation
   at all) is the single biggest percentage miss in the cut.
4. The biggest absolute miss (8.3) carries one comma and one period; the biggest percentage
   miss (4.7) carries none. **The misses are not concentrated on punctuation-heavy lines.**

**Recommendation (orchestrator's call, not this stage's):** the two measurements now
disagree about *which* constant is wrong. The hi cut's flat 12.96 matched its 13.03 key, so
its residual really was punctuation-shaped; the en cut's flat 17.39 does **not** match its
16.1 key, and once that is corrected the punctuation residual mostly vanishes. Fix
`cuts.en.chars_per_second` first — with the two measurements (17.73, 17.39) beside it, and
only alongside the budget-formula fix the trap note demands — then re-measure before
touching `tts.pause_seconds`. `pause_seconds` is shared by both cuts, so changing it on hi
evidence alone would move the en estimate for a reason en does not support.

## Not done here

- No `script_sha256` recorded for the en stage entry — computing it needs a shell command
  outside this stage's allowlist. The orchestrator writes the stage entry; it should hash
  the current `script-en.md` there, as it did for hi.
- `run.json budget.elevenlabs_calls` raised 92 → **184** cumulative (37 of 221 left).
