---
summary: fin-voice stage for first-lakh-first-thousand, cut hi, attempt 1. All 86 clips generated and ffprobe-measured; batch.py postcondition FAILED on one line (1.1 runs 53% over its chars/rate estimate). Measured runtime 566.39s vs the 510s target (+11.1%).
updated: 2026-07-31
source: tools/tts/batch.py run output + studio/videos/first-lakh-first-thousand-hi/assets/voice/timing.json
stage: fin-voice, cut hi, attempt 1
---

# fin-voice — first-lakh-first-thousand / hi / attempt 1

## Cost guard (checked before spending)

| Gate | Result |
|---|---|
| `vault/videos/first-lakh-first-thousand/audit-hi.md` contains PASS | yes (line 10) |
| char total vs 1.3 × (510 × 12.5 = 6,375) = 8,287 | **5,812 chars** — 91% of budget, 70% of the ceiling |

Both passed, so the run proceeded. 86 ElevenLabs calls spent (of the run's 200 ceiling;
the `-en` cut needs a comparable number, leaving ~28 calls of headroom).

## What was produced

- `assets/voice/lines.json` — 86 entries, ids `1.1 … 9.10` matching the script's own
  numbering (dotted ids are the shipped MEDIUM convention: firaun uses `seg-07.4`).
  Text sliced from the `>` VO blocks of `script-hi.md`, verbatim Devanagari, no
  markdown / cue text / on-screen text.
- 86 `<id>.mp3` + 86 `<id>.txt` (the exact string sent to the API, written by batch.py).
- `assets/voice/timing.json` — written atomically by batch.py, MEASURED durations.
- `gen_vo_hi.sh` — regeneration script. Root is `${YTS_ROOT:-…}` rather than a hardcoded
  `cd`, so it survives `archive_cut.py` (the gotcha named in `vault/CLAUDE.md`).

Voice/model came from `tools/format.json` (`cuts.hi.voice_id` Harsh
`HTUuC7OeeEt6OL5fViVe`, `tts.model` `eleven_multilingual_v2`, `tts.style` 0) — nothing
hardcoded here.

## Measured timing

| | value |
|---|---|
| target (`tiers.medium.target_seconds`) | 510.00s (8:30) |
| **measured total (timing.json)** | **566.39s (9:26)** — **+56.39s, +11.1%** |
| VO audio only (total − 86 × (lead 0.4 + tail 1.0)) | 445.99s (7:26) |
| scene padding (`scene.lead_in_seconds` + `scene.tail_seconds`) | 120.40s |
| measured Hindi rate | 5,812 / 445.99 = **13.03 chars/s** (format.json assumes 12.5 — the voice runs 4% fast) |

**The overshoot is not the script.** The VO itself came in at 446s against a ~477s
budget — the script under-ran. The 510s target is blown by batch.py's scene arithmetic:
`lead_in 0.4 + tail 1.0` per line is a per-scene constant, and at 86 lines that is 120s
of padding, where `script-hi.md` planned on the firaun gap model (0.2s intra-chapter /
0.8s at a chapter boundary ≈ 22s). At SHORT tier's 9 lines the same constants cost only
12.6s, which is why this has not surfaced before. This is a tier-scaling question for
`format.json`, not something fin-voice may hand-edit — `timing.json` is generated.

## Postcondition failure (exit code 1)

```
✗ 1.1: duration 5.88s is >35% off chars/rate estimate 3.84s — wrong text or truncated clip
```

Only one of 86 lines breached; it is therefore also the largest per-line drift.

| id | text | chars | expected @12.5 | measured | drift |
|---|---|---|---|---|---|
| 1.1 | `पाँच हज़ार रुपये महीना। पहला एक लाख — बीस महीने।` | 48 | 3.84s | 5.878s | **+53.1%** |

Diagnosis (ffprobe only — `ffmpeg` is outside this stage's allowlist):

- Not truncated: 5.877551s of mp3, 94,502 bytes at 128 kbps, stream duration == format
  duration. Truncation would read short, not long.
- Not silent: batch.py's `mean_volume_db` guard (−50 dB) did not fire.
- It is genuinely slow delivery. 1.1 runs at 8.2 chars/s where its neighbours run
  12.0 (1.2), 14.5 (1.6) and 12.2 (5.3). The line is the cold-open hook and contains
  three stops in 48 chars — a danda plus an em-dash — and the voice takes a long beat at
  each. Its bytes-per-char is ~2× the file next to it, consistent with added pause.
- Slow is arguably *right* for a hook line, but `tts.duration_tolerance_pct` 35 cannot
  tell "deliberate pause" from "wrong text", so the gate fires. No retry was attempted:
  the orchestrator owns retries.

Two ways forward, both the orchestrator's call:

1. **Re-cut 1.1 only** — one API call: delete `assets/voice/1.1.mp3` and re-run
   `gen_vo_hi.sh` (skip-if-exists means the other 85 are free). A different take will
   likely land inside tolerance, but the pauses are a property of the punctuation, so it
   may reproduce.
2. **Accept it** — the clip is real, audible, correct-length-for-its-content speech, and
   the 35% band is a truncation heuristic, not an editorial one. Accepting means the
   `known_benign` list in `format.json` is the honest place to record it, so the next
   `check` run does not re-flag a decision that was already made.

## Notes for fin-build

- `timing.json` `total` is **566.39s** — the root `data-duration` and every scene span
  must derive from it, not from the script's `~498s` budget table.
- Scene 5.2 + 5.3 hold one photograph for 7.86 + 3.20 = 11.06s of scene time (audio
  4.83 + 1.80). `script-hi.md` §5 of the build handoff already flags this pair as a
  `max_scene_seconds` 9.0 breach and requires a second, tighter crop for 5.3 — the
  measured numbers make it worse than the ~9.2s the script predicted, not better.
- The other two `hold` pairs measure 1.1+1.2 = 12.94s and 1.5+1.6 = 10.17s of scene
  time, so all three continuous-zoom pairs now exceed 9.0s and each needs a second crop.
