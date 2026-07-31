---
summary: fin-voice for first-lakh-first-thousand cut en, attempt 1. All 92 clips generated (one API call each) and timing.json written with measured durations; batch.py exited 1 on two duration-vs-chars flags (1.6, 5.1) that the evidence says are estimator artifacts, not truncated audio.
updated: 2026-07-31
source: tools/tts/batch.py run output + ffprobe of the flagged clips; rates/voice from tools/format.json.
stage: fin-voice, cut en, attempt 1
---

# fin-voice — first-lakh-first-thousand / en / attempt 1

## Gates before spending

| Gate | Result |
|---|---|
| `audit-en.md` contains PASS | yes (line 10, attempt 1) |
| Char total vs 1.3× budget | 7,659 chars vs budget 510 × 16.1 = **8,211**; cap 1.3× = **10,674**. 6.7% *under* budget. PASS |

## Extraction

92 VO lines → `studio/videos/first-lakh-first-thousand-en/assets/voice/lines.json`,
ids `1.1 … 9.10` in script order (10/10/10/11/11/10/8/12/10 per chapter).

The script (line 235) warns that a naive `grep '^>'` would ship the "SIX THINGS
THAT MUST NOT ENTER THIS CUT" admonition (lines 30–53) to ElevenLabs and burn
calls — that hazard was found on the Hindi cut. Extraction was keyed off the
`**N.M**` headers instead, and gated with the byte-for-byte reconstruction check
the script asks for: **92 patterns sliced from the source matched 92/92 lines in
`lines.json`** (`grep -F -f`). No production cue (backticked `[ap … ]` blocks)
entered the file.

## Generation

`python3 tools/tts/batch.py --project studio/videos/first-lakh-first-thousand-en --cut en`

- Voice **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0 —
  all read from `tools/format.json`, nothing hardcoded.
- 92 clips written, 0 skipped (fresh project), **92 API calls**. With the Hindi
  cut's 86, the run has spent 178 of 200; 22 left.
- `timing.json` written by batch.py with MEASURED durations. Padding is the
  MEDIUM-tier 0.25 lead + 0.55 tail (`tiers.medium`), 73.6s across 92 lines.

## Result

| Metric | Value |
|---|---|
| Measured total | **505.56s** (8:25.6) |
| Target | 510s → **−0.9%** |
| Audio only (total − 73.6s padding) | 431.96s |
| Delivered rate | 7,659 / 431.96 = **17.73 chars/s** |
| Mean scene | 505.56 / 92 = **5.49s** (target 6.5, max 9.0 — no scene near the cap) |
| Longest clip | 7.7 → well under `max_scene_seconds` |
| Shortest clip | 5.3 at 1.384s (above `tts.min_clip_seconds` 1.0) |

Exit code **1** — postcondition failure, two lines:

```
✗ 1.6: duration 2.51s is >35% off chars/rate estimate 3.93s
✗ 5.1: duration 3.37s is >35% off chars/rate estimate 5.39s
```

Largest per-line drift: **5.1 at −37.5%**; 1.6 at −36.1%. Both marginal against
the 35% tolerance, both on the SHORT side.

## Why these two are almost certainly not truncated clips

ffprobed the flagged clips against their un-flagged short-line siblings:

| id | chars | dur | chars/s | words/min | flagged |
|---|---|---|---|---|---|
| 7.1 | 57 | 2.952 | 19.3 | **244** | no |
| 1.6 | 52 | 2.508 | 20.7 | **239** | **yes** |
| 5.1 | 69 | 3.370 | 20.5 | 214 | **yes** |
| 9.9 | 51 | 2.691 | 19.0 | 178 | no |
| 3.3 | 56 | 3.161 | 17.7 | — | no |
| 5.3 | 22 | 1.384 | 15.9 | — | no |

**7.1 delivers faster than 1.6 (244 vs 239 wpm) and passes.** A truncated clip
would land near half its estimate, not 3% off a sibling that passed. The flags
track punctuation, not audio: `expected_seconds` adds the full
`tts.pause_seconds` budget on top of a flat rate that *already includes*
delivered pause silence, and ElevenLabs trims the trailing sentence-final
silence — so a short line with a `.` plus a `?` or a `,` (exactly 1.6 and 5.1)
over-estimates by ~0.7s on a ~3s clip, which is 20+ percentage points of a 35%
tolerance.

Root cause is the check's model, not the audio or the script. Two honest fixes,
in the order the "fix defaults, not gates" rule ranks them — **neither is
fin-voice's to make** (`tools/` is out of this stage's write scope):

1. Do not charge a sentence-final pause on the LAST mark of a line — the voice
   never renders it, because the clip ends there. This is the actual physics and
   it fixes every short line at once.
2. Failing that, scale the tolerance with clip length (a 0.7s model error is
   noise on a 7s clip and 25% on a 2.5s one).

Blind `--force` regeneration of 1.6 and 5.1 would spend 2 of the 22 remaining
calls on a re-roll of the same tolerance dice and is not recommended.

## Cross-cut note (calibration)

`cuts.en.chars_per_second` is 16.1; this cut delivered **17.73** (+10%). That
figure is itself a measured average over two shipped `-en` cuts, so this is a
third data point rather than an error — worth folding in after the cut ships,
which would also shrink the drift on short lines. Not changed here.

## Artifacts

- `studio/videos/first-lakh-first-thousand-en/assets/voice/lines.json` (92 lines)
- `studio/videos/first-lakh-first-thousand-en/assets/voice/{1.1 … 9.10}.mp3` + `.txt` (92 each)
- `studio/videos/first-lakh-first-thousand-en/assets/voice/timing.json` (measured, 505.561s)
- `studio/videos/first-lakh-first-thousand-en/gen_vo_en.sh` (relative `cd`, not a hardcoded studio path)
