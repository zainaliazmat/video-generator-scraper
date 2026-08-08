---
summary: Targeted re-voice of en line 7.4 succeeded on the new batch.py --only flag — 1 ElevenLabs call, 91 clips untouched. Found and worked around a real bug in --only (it narrows the timing rebuild too, leaving a 1-entry timing.json); the bare allowlisted re-run repaired it at zero cost. Measured total 626.743s, +0.157s vs attempt 1's 626.586s, LONG 600s floor clears by 26.7s.
updated: 2026-08-01
source: tools/tts/batch.py, tools/pipeline_check.py, tools/format.json, vault/videos/japanese-money-methods/script-en.md, studio/videos/japanese-money-methods-en/assets/voice/timing.json, ffprobe
stage: fin-voice, cut en, attempt 3
status: ok
---

# fin-voice-en attempt 3 — 7.4 re-voiced, timing rebuilt from all 92

## Cost guard (checked before spending — both pass)

| Gate | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | yes (frontmatter + verdict line 10) | pass |
| Char total vs 1.3 × budget | **9,608** vs 660 × 16.1 = 10,626 → cap 13,814 | pass (0.90× budget) |
| `budget.elevenlabs_calls` | 185 of 221 before, **186 after** | pass (35 left) |

Net **−8 chars** on the cut (7.4: 116 → 108), so the guard moved the right way.

## Step 1 — lines.json rebuilt from the current script

Every one of the 92 `>` VO blockquotes in the current `script-en.md` was read and
compared against the on-disk `lines.json`. **Exactly one line differed** — 7.4 — so
that one entry was replaced with the string sliced from the script:

> All four characters share one single part, and that shared part is the emptiness at the centre of the basin.

The other 91 are byte-identical to the script and were left alone. `lines.json` and
the script are now consistent, which is the state attempt 2 deliberately refused to
create while the stale mp3 was still on disk.

## Step 2 — the one API call, and the bug it exposed

```
python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-en --cut en --only 7.4
--only: regenerating 1 clip(s): ['7.4']
=== 7.4 (108 chars) ===
OK: wrote 104,533 bytes -> …/7.4.mp3
timing.json: 1 lines, total 7.30s
  ✗ timing.json ids do not match lines.json ids (1 vs 92 entries)      exit 1
```

**The synthesis half worked perfectly**: one call, one clip, 104,533 bytes, 91 other
clips untouched. The **timing half did not**, and this is a genuine bug in the new
flag, not a misuse:

```python
lines = [l for l in lines if l["id"] in want]      # line 53 — narrows for GENERATION
…
for line in lines:                                  # line 72 — reuses the SAME narrowed list
    dur = pc.ffprobe_duration(…)                    #          to rebuild timing.json
```

`--only` narrows one list that has **two** consumers. The generation loop should see
the subset; the timing loop must always see all 92. So the run clobbered a 92-entry
`timing.json` with a 1-entry one whose `scene_start`s all began at 0.

**The postcondition caught it.** `check_voice_dir`'s id-set comparison is exactly the
check that fires here, it fired, and batch.py exited 1 rather than reporting success —
so the damage was loud and bounded, never silent. That is the control working.

**The fix for `tools/` (this stage may not write it) — one line:** the timing loop must
iterate the full `pc.load_lines(vdir)`, not the filtered `lines`. Keep the filtered list
for generation only:

```python
gen = [l for l in lines if l["id"] in want] if only else lines
for line in gen:  …generate…
for line in lines:  …ffprobe + timing…      # always all 92
```

The selftest passed because it only ever exercised `--only` on a 2-line fixture where
it never checked that the OTHER line survived in timing.json. A one-assert extension —
`run(tmp, "hi", only=["h2"])` then `assert len(timing["lines"]) == 2` — would have
caught this before it cost anything.

## Step 3 — timing.json rebuilt from all 92 clips (zero cost)

The repair needed no new tooling and no shell verb this stage lacks: with all 92 mp3s
now on disk, the **bare allowlisted invocation** regenerates nothing (skip-if-exists on
all 92) and rebuilds timing.json from the full set.

```
python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-en --cut en
… skip (exists) × 92 …
timing.json: 92 lines, total 626.74s                                    exit 0
```

Exit 0, **no `✗` lines** — every postcondition passed: clip size, duration-vs-chars at
±35%, the −50 dB silence floor, the 0.05s ffprobe cross-check, and the scene
arithmetic. **Zero additional API calls.**

## Measured runtime vs target

| | attempt 1 | **attempt 3** |
|---|---|---|
| Chars | 9,616 | **9,608** |
| Audio seconds (sum of 92 clips) | 552.99s | **553.14s** |
| Inter-line padding (92 × 0.25 + 0.55) | 73.60s | 73.60s |
| `timing.json` total | 626.586s | **626.743s = 10:26.7** |
| Target (`run.json target_seconds`) | 660s | 660s |
| Drift vs target | −33.4s (−5.1%) | **−33.3s (−5.0%)** |
| LONG floor (`tiers.long.min_seconds` 600s) | +26.6s | **+26.7s headroom — clears** |

**The total went UP by +0.157s, not down.** My attempt-2 projection was ≈626.2s
(≈ −0.4s) and it was wrong in sign: I priced the new 7.4 at the *old* line's delivered
18.27 c/s, but 8 fewer characters did not buy 8 characters of time. "emptiness at the
centre" is slower in the mouth than "empty square hole" — measured **6.504s against the
old 6.348s**, a delivered **16.6 c/s** for this line. A −7% char cut produced a +2.5%
duration rise. Worth remembering: **character count does not predict a single line's
duration well enough to project from; only ffprobe settles it.** The floor was never at
risk either way.

### 7.4 and the lines it shifts

| | |
|---|---|
| 7.4 `scene_start` | **517.368s — unchanged**, as required |
| 7.4 duration | 6.504s (was 6.348s), `scene_duration` 7.304s |
| Lines shifted | **7.5 … 8.8** (21 lines), each **+0.157s** |
| 7.5 `scene_start` | 524.673s |
| 8.8 `scene_start` | 620.849s, ends 626.743s |

## Per-line drift

Unchanged from attempt 1 apart from 7.4, since 91 clips are the same audio.

| | |
|---|---|
| Largest drift by absolute seconds | **8.3 — −1.74s** (expected 8.09s, measured 6.35s) |
| Largest drift by percent | **4.7 — −26.1%** (expected 6.40s, measured 4.73s) |
| New 7.4 | expected 108/16.1 + 0.70 pause = 7.408s, measured 6.504s → **−0.90s (−12.2%)** |
| Tolerance | ±35% — nothing breached, batch.py flagged nothing |

7.4's drift got *smaller* (attempt 1: −1.19s / −15.8%), because the new line is slower
per character. 90 of 92 lines still miss negative; the only positives remain 6.2 and 6.11.

## For the owed format.json fix — carried forward verbatim

Recording as instructed, third measurement, unchanged by this 8-char edit:

- **17.39 c/s flat** for this cut (9,619 chars / 626.59s at the time of measurement;
  9,608 / 553.14s of pure audio recomputes to **17.37 c/s** — same place).
- **18.48 c/s on the nine zero-punctuation lines** = pure speech, no pause charge.
- Against `cuts.en.chars_per_second` = **16.1**. With `first-lakh-first-thousand-en`'s
  17.73, that is **two independent flat measurements above 17.3 against a 16.1 key**.

**It stays BOTH-OR-NEITHER.** fin-script budgets `target_seconds × rate`, which ignores
the scene padding that is not audio — 73.6s of 660s here. The true char budget is
`(660 − 73.6) × 17.39 = 10,197`; `16.1 × 660 = 10,626` only lands because two errors
cancel. **Fix fin-script's budget formula to `(target_seconds − scene_padding) × rate`
FIRST, then raise the key.** Raising the key alone ships every en script ~17% long.
Owed, not done.

## Artifacts

- `studio/videos/japanese-money-methods-en/assets/voice/lines.json` — 92 lines, 7.4 updated
- `studio/videos/japanese-money-methods-en/assets/voice/7.4.mp3` + `7.4.txt` — new take
- `studio/videos/japanese-money-methods-en/assets/voice/timing.json` — 92 entries, total 626.743s
- `studio/videos/japanese-money-methods-en/gen_vo_en.sh` — now documents the `--only`
  route and its known bug (the delete-an-mp3 advice it used to carry is what blocked
  attempt 2)

## Notes for the rebuild

- The composition is being rebuilt from scratch on **blockframe-9**; the existing
  `index.html` was not read and not touched by this stage.
- Every downstream copy of the timing must be re-derived from this `timing.json` — 21
  `scene_start`s moved by +0.157s and any stale copy will drift the whole tail.
