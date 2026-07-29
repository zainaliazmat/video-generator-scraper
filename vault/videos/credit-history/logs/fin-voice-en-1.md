---
summary: fin-voice for credit-history en, attempt 1. 9 ElevenLabs calls (2,587 chars, Brian nPczCjzI2devNBz1zQrb) produced a measured 160.63s VO / 173.23s rendered against a 165s target. batch.py exit 0, all postconditions clean; every line read FASTER than the 15.0 c/s estimate, largest drift en5 at −2.94s (−14.4%). The audit's hook-payoff advisory clears with ~3.4s margin — no trim needed.
updated: 2026-07-29
source: tools/tts/batch.py run + independent ffprobe of all 9 clips; script vault/videos/credit-history/script-en.md (post-audit-edit, read fresh off disk); rates/voice from tools/format.json
---

# fin-voice — credit-history / en / attempt 1

STATUS: ok

## Cost guard (checked before spending)

| Gate | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | PASS at line 9 | clear |
| Char total vs 1.3× budget | 2,587 vs 3,217.5 (165s × 15.0 c/s = 2,475) | clear — **+4.5%** over target, 20% under the ceiling |

## The post-edit warning was honoured

fin-audit flagged that `script-en.md` was edited after writing (6 changes, `en1`
and `en6` VO among them). `studio/videos/credit-history-en/` **did not exist**
before this stage — it was created here — so there was no cached clip, no stale
`lines.json` and nothing for batch.py's skip-if-exists path to resume from. All
nine clips are first-generation from the current on-disk text.

Both edited lines were sliced in their post-edit form and verified by hand-count
against the audit's own recount:

- **en1** = 248 chars — "a payment you've missed **can sit**", stamp wording is
  screen-only so it never reaches TTS. (Audit recount: 248. ✓)
- **en6** = 283 chars — "And on that **second habit**", the "thirty percent"
  phrasing is gone. (Post-edit table: 283. ✓)
- **en5** = 305 chars, matching the audit's independent recount. ✓

## What ran

`python3 tools/tts/batch.py --project studio/videos/credit-history-en --cut en`
→ **exit 0**, no postcondition problems printed.

- 9 calls, exactly the 9 the script's handoff #2 predicted.
- Voice `nPczCjzI2devNBz1zQrb` (Brian), `eleven_multilingual_v2`, style 0 — all
  read from `tools/format.json` by the tool, nothing hardcoded in this stage.
- VO text sliced verbatim from the nine `**VO**` blockquotes of `script-en.md`
  (en1→en1 … en9→en9). No markdown, no on-screen text, no stage directions, no
  foots, no blockquote guards. Digits stay spelled out exactly as the script
  wrote them (the engine rule) — nothing was normalised or re-typed.

**One char-count correction:** en7 slices to **429** chars, not the 428 in the
script's budget table. fin-audit's hand recount also said 429, so the slice is
right and the table's estimate is the stale figure. Total is **2,587**, not
2,586. Cosmetic — no gate moves.

## Measured timing

VO total **160.627s** vs the 165s target — **−4.37s (−2.6%)**. Rendered runtime
with the per-scene 0.4s lead-in + 1.0s tail (9 × 1.4s = 12.6s) is **173.227s**,
comfortably inside the short tier's 60–300s range.

| id | chars | est @15.0 c/s | measured | drift |
|---|---|---|---|---|
| en1 | 248 | 16.53s | 14.707s | −1.83s (−11.0%) |
| en2 | 152 | 10.13s | 9.326s | −0.81s (−8.0%) |
| en3 | 302 | 20.13s | 20.062s | −0.07s (−0.4%) |
| en4 | 276 | 18.40s | 16.300s | −2.10s (−11.4%) |
| en5 | 305 | 20.33s | 17.398s | **−2.94s (−14.4%)** |
| en6 | 283 | 18.87s | 18.704s | −0.16s (−0.9%) |
| en7 | 429 | 28.60s | 26.749s | −1.85s (−6.5%) |
| en8 | 305 | 20.33s | 19.174s | −1.16s (−5.7%) |
| en9 | 287 | 19.13s | 18.207s | −0.93s (−4.8%) |

**Largest per-line drift: en5, −2.94s (−14.4%)** — inside the 35% tolerance in
`format.json tts.duration_tolerance_pct`, and batch.py's own check agreed.

**Every one of the nine lines came in SHORT.** That is a one-sided error, not
noise: the effective measured rate is **16.11 chars/s** (2,587 / 160.627), i.e.
Brian reads **7.4% faster** than the 15.0 c/s `format.json` records for the en
cut. The hi cut's Harsh calibrated to within 0.9% in the same run, so this looks
like a per-voice constant that is slightly low rather than a bad estimate.
**Not changing it here** — `tools/` is out of this stage's write scope, and one
video is one sample. Worth a cross-check against the two shipped en cuts before
anyone touches `cuts.en.chars_per_second`.

The script's "if the measured TTS runs long, cut from en7" contingency is **not
needed** — en7 measured 26.75s against its own 28.6s estimate, and nothing ran
long.

## The audit's mandatory advisory — hook payoff ≤15s

`audit-en.md` check 3 made this a build gate and required an ffprobe of en1
before anything else, with a prescribed trim if the read came in slower than
15 c/s.

en1 measured **14.707s** for 248 chars = **16.86 c/s — faster than 15**, so the
trim condition is not met. **No trim. «and what interest you pay» stays.**

Where the naming lands, by two independent methods:

- Char-offset: «It's called your credit report» closes at char **189 of 248**
  (76.2%) → 0.762 × 14.707 = **≈11.2s of VO, ≈11.6s on the timeline** with the
  0.4s lead-in.
- Backwards from the tail: the sentence *after* the naming is 58 chars, ≈3.6s at
  the measured rate → naming ends at 14.707 − 3.6 = **≈11.1s VO, ≈11.5s** on the
  timeline.

Both agree at **≈11.5s. Margin to the 15s gate ≈3.4s**, better than the ~2.0s the
audit projected. Still an interpolation, so handoff #7 stands: confirm it off the
word-level (faster-whisper) timings when cues are anchored. There is now enough
slack that a re-check is a formality rather than a risk.

## Postconditions verified

`check_voice_dir` passed silently inside batch.py (exit 0 = zero problems),
covering: clip size ≥10,240 bytes, duration ≥1.0s, timing-vs-ffprobe within
0.05s, duration-vs-chars within 35%, mean volume above −50 dB, and the full
scene-arithmetic chain (`scene_start` cumulative, `scene_duration` = 0.4 + clip
+ 1.0, `audio_start` = `scene_start` + 0.4, `total` = sum of scenes).

Cross-checked independently: ffprobe on all 9 mp3s returns durations identical
to `timing.json` at 3 decimal places. `timing.json` was generated by batch.py
and was not hand-edited.

## Artifacts

- `studio/videos/credit-history-en/assets/voice/lines.json` — 9 ordered `{id,text}`
- `studio/videos/credit-history-en/assets/voice/en1.mp3` … `en9.mp3` + matching `.txt`
- `studio/videos/credit-history-en/assets/voice/timing.json` — measured, atomic
- `studio/videos/credit-history-en/gen_vo_en.sh` — manual regeneration. Written
  fresh for this project; the `cd` is derived from the script's own location
  (`dirname "$0"/../../..`), not hardcoded to another project's path.

## Notes for the next stage

- `timing.json` is the single source for the composition's four timing copies —
  derive, never retype. A fabricated duration fails the ffprobe cross-check.
- **en5, the hero scene, is the tightest fit.** It measured 17.40s of VO (scene
  18.80s), nearly 3s less than the script's 20.33s estimate. The seven-year
  timeline has to slam the mark, sweep YEAR 1 → YEAR 7, reveal the struck
  correction block *after* the mark, and never hold static past ~2s (§5.2) —
  all inside 18.80s, not the ~21.7s the script was pacing against. Re-derive the
  keyframes from `timing.json`, don't scale the script's numbers.
- Same caution, smaller, for **en1 (16.11s scene)** and **en4 (17.70s scene)** —
  both ~11% shorter than planned, and en4 carries a declared 0.6s two-item
  cascade plus the `65% OF YOUR SCORE` punch.
- Re-running `gen_vo_en.sh` costs nothing: batch.py skips clips that already
  exist. Only `--force` re-spends credits.
- The studio project is otherwise empty — `credit-history-en` was created by this
  stage. No `index.html`, `package.json`, images or `manifest.json` exist yet.
- Untouched by this stage and still owed downstream: `storyboard-en.md` does not
  exist, so the audit's colour-intent table and its `max_simultaneous_elements`
  advisories for en5/en7 are still open.
