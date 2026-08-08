---
summary: Targeted re-voice of en line 7.4 (Ryoan-ji "square hole" dropped, creator option A 2026-08-01). BLOCKED before spending — batch.py can only regenerate a clip that is ABSENT from disk, and this stage's bash allowlist has no verb that can remove the stale 7.4.mp3. Zero API calls made; budget still 184/221. Cost guards both pass, so the run is cleared to spend the moment the stale clip is gone.
updated: 2026-08-01
source: tools/tts/batch.py, tools/pipeline_check.py, tools/format.json, vault/videos/japanese-money-methods/script-en.md, studio/videos/japanese-money-methods-en/assets/voice/timing.json
stage: fin-voice, cut en, attempt 2
status: fail (blocked, nothing spent, nothing mutated)
---

# fin-voice-en attempt 2 — targeted re-voice of 7.4

## Cost guard (checked first, both pass)

| Gate | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | yes (frontmatter + verdict line 10) | pass |
| Char total vs 1.3 × budget | 9,608 after the edit vs 660 × 16.1 = 10,626 → cap 13,814 | pass (0.90× budget) |
| `budget.elevenlabs_calls` | 184 of 221 spent; this job needs **1** | pass (36 left after) |

The edit is a net **−8 chars** (7.4 goes 116 → 108), so the guard moves the right way.

## The text (verified, not retyped)

Sliced verbatim from the orchestrator's current `script-en.md`; a substring check
confirms the exact string is present in the file:

> All four characters share one single part, and that shared part is the emptiness at the centre of the basin.

On disk, `assets/voice/7.4.txt` and `lines.json` still carry the **old** string
("…the empty square hole in the middle of the basin."), and `7.4.mp3` is the old
take. All three are consistent with each other — see "State left on disk" below.

## Why this is blocked

`tools/tts/batch.py` has exactly one skip rule (line 45):

```python
if os.path.exists(out) and os.path.getsize(out) > 0 and not force:
```

That is a **binary** choice at the whole-cut level:

- no flag → 7.4.mp3 exists and is non-empty → **skipped**, the old take survives;
- `--force` → **all 92** clips regenerate → 92 calls against 37 remaining. Terminal,
  and explicitly ruled out by the task ("do not regenerate the other 91 clips").

There is no `--only <id>`. The single-clip path the tooling actually intends is
documented in this cut's own `gen_vo_en.sh` — *"delete an mp3 to redo just that
line"* — i.e. it depends on an out-of-band `rm`. This stage's bash allowlist is
`batch.py` and `ffprobe` only, so it has no verb that can remove a file, and the
Write tool refuses to truncate an existing binary it cannot Read first. Both
escape hatches I checked were rejected on merit, not on permissions:

1. **`--force`** — 92 calls, over budget, destroys 91 correct takes.
2. **Renaming 7.4's id in `lines.json`** (e.g. `7.4b`, so `7.4b.mp3` is absent and
   gets generated) — this *would* cost one call and *would* pass `check_voice_dir`,
   which only compares `lines.json` ids to `timing.json` ids and never flags orphan
   mp3s. Rejected anyway: it puts an id into `timing.json` that does not exist in
   `script-en.md`, and the blockframe-9 rebuild maps scenes to audio **by id**. That
   is a silent mismatch bought to save one `rm`.

## The unblock (one command, then re-invoke)

```bash
rm studio/videos/japanese-money-methods-en/assets/voice/7.4.mp3 \
   studio/videos/japanese-money-methods-en/assets/voice/7.4.txt
```

Then attempt 3 writes the new 7.4 into `lines.json` and runs the single allowed
line; batch.py regenerates the one absent clip, re-ffprobes all 92, and rewrites
`timing.json` with the shifted `scene_start`s from 7.4 onward. Cost: 1 call.

## State left on disk (deliberately unchanged)

**`lines.json` was NOT updated.** Writing the new text while the old mp3 is still
present would create exactly the failure mode `check_voice_dir` cannot see: a later
naive `batch.py` run skips 7.4, pairs the **new** text with the **old** audio, and
writes a `timing.json` that passes every postcondition — 108 chars against 6.348s is
well inside the ±35% tolerance, so nothing fires. Leaving `lines.json`, `7.4.txt`
and `7.4.mp3` all consistently *stale* keeps a premature re-run a harmless no-op
instead of a silent corruption. Per the fix-defaults-not-gates rule, the wrong state
is unrepresentable rather than merely warned about.

`gen_vo_en.sh` needs no change — it already derives the repo root from `$0`
(`cd "$(dirname "$(readlink -f "$0")")/../../.."`), carries no hardcoded studio
path, and its comment documents the delete-one-mp3 path.

## Projected runtime after the re-voice

Nothing here is written to `timing.json` — these are estimates for the floor check
only; the real numbers come from ffprobe on attempt 3.

| | |
|---|---|
| Current measured total (attempt 1) | **626.586s** |
| Old 7.4 | 116 chars → 6.348s (delivered 18.27 c/s; one interior comma) |
| New 7.4 | 108 chars → **≈5.9s** at the same delivered rate |
| Expected delta | **≈ −0.4s** |
| Projected new total | **≈ 626.2s = 10:26.2** |
| LONG floor (`tiers.long.min_seconds`) | 600s → **≈ +26s headroom** |

The floor is not at risk under any plausible take: even if the new 7.4 came in at
the bottom of its ±35% tolerance (≈4.4s), the total lands ≈624.6s, still +24.6s
clear. Only 7.4 and the 20 lines after it (7.5 … 8.8) shift; `scene_start` for
7.4 stays 517.368s and everything downstream moves by the same ≈−0.4s.

## For the owed format.json fix — third measurement

Recording as instructed: this cut measured **17.39 c/s flat** (9,616 chars /
552.99s of audio) against `cuts.en.chars_per_second` = **16.1**, and **18.48 c/s**
on the nine zero-punctuation lines (pure speech, no pause charge). With
`first-lakh-first-thousand-en`'s 17.73, that is **three independent en measurements,
two of them flat, all above 17.3 against a 16.1 key**.

The fix remains BOTH-OR-NEITHER, per the `_chars_per_second_trap` note: fin-script
budgets `target_seconds × rate`, which ignores scene padding that is not audio. At
LONG here that padding is 73.6s of 660s, so the true char budget is
`(660 − 73.6) × 17.39 = 10,197`, while `16.1 × 660 = 10,626` only lands because two
errors cancel. **Change the budget formula to `(target_seconds − scene_padding) × rate`
first, then raise the key.** Raising the key alone ships every en script ~17% long.
This edit does not change that verdict — it is 8 chars.

## Not done here

- No API call, no mp3 written, no `timing.json` write, no `lines.json` write.
- `run.json budget.elevenlabs_calls` unchanged at **184**.
- Durable fix, for whoever owns `tools/` (this stage may not write it): give
  `batch.py` an `--only <id>` (repeatable) flag. It is a two-line change to the
  loop guard and it removes the only reason this stage ever needs a shell verb it
  does not have. Targeted re-voices are not rare — a single audited line moving is
  the normal outcome of gate-one.
