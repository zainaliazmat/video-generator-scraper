---
summary: fin-voice for passive-income-number cut en, attempt 1. 78 ElevenLabs calls (Brian), zero failures, zero retries. Measured total 497.809s against the 510s target (-2.39%), inside the two-rate hedge fin-script sized for. Flat delivered rate measured 17.588 c/s — the THIRD independent en measurement above 17.3 against the 16.1 key. No scene breaches max_scene_seconds.
updated: 2026-08-07
source: tools/tts/batch.py run output + studio/videos/passive-income-number-en/assets/voice/timing.json (ffprobe-measured) + tools/format.json cuts.en / tiers.medium / scene.
stage: fin-voice, cut en, attempt 1 — PASS
---

# fin-voice — passive-income-number, cut en, attempt 1

## Gate checks (before spending)

| Guard | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | PASS at both the verdict line and the close | **cleared** |
| Char total vs 1.3x budget | 7,657 vs 10,674 (510 x 16.1 x 1.3) | **cleared, 72% of ceiling** |

## Extraction

78 VO lines pulled **by line key**, not by grepping `^> `. The script carries 113
blockquote lines — 78 VO plus 35 guard/annotation blockquotes (the SIX THINGS
banner, the fin-audit edit note, the two-rate hedge). A `^> ` sweep would have
put 35 wasted calls on the job. The key is the `**<ch>.<n>**` marker immediately
above each VO blockquote; the ``[arch: …]`` backtick line below it is layout, never
narration, and never entered the job.

Post-audit text was voiced verbatim — **5.6, 6.7 and 6.8** carry the rewritten
rate-bearing sentences. Their measured char counts are 119 / 119 / 119 against the
audit note's hand-estimate of 117 / 117 / 119; the note declares itself an estimate
and `batch.py` recounts programmatically, so nothing was hand-patched.

## The run

`python3 tools/tts/batch.py --project studio/videos/passive-income-number-en --cut en`

- **78 ElevenLabs calls.** No resume, no skips, no `--force`, no retry. Every clip
  written first-attempt. Run total after this stage: **156 of 188**.
- Voice `nPczCjzI2devNBz1zQrb` (Brian), `eleven_multilingual_v2`, style 0 — all from
  `format.json cuts.en`, none hardcoded.
- Postconditions (size, duration-vs-chars, silence, scene arithmetic): **zero problems**.
  Smallest clip 33,898 bytes (3.1) against `min_clip_bytes` 10,240; shortest 2.090s
  against `min_clip_seconds` 1.0.

## Measured runtime

| | Seconds |
|---|---|
| VO audio (78 clips, ffprobe) | 435.409 |
| Inter-line padding (78 x 0.8, `tiers.medium` 0.25 + 0.55) | 62.400 |
| **Measured total** | **497.809 (8:17.8)** |
| Target (`tiers.medium.target_seconds`) | 510 |
| **Drift** | **-12.19s, -2.39%** |

Average scene 6.382s against `target_scene_seconds` 6.5 — marginally brisker than
target, which is the right side to miss on.

### The rate key — third measurement, and it agrees with the other two

**7,657 chars / 435.409s = 17.588 c/s flat**, including pause silence.

| Cut | Chars | VO seconds | Flat c/s |
|---|---|---|---|
| first-lakh-first-thousand-en | 7,657 | 432.00 | 17.73 |
| japanese-money-methods-en (LONG) | 9,619 | 626.59 | 17.39 |
| **passive-income-number-en (this)** | **7,657** | **435.409** | **17.588** |

Three independent flat measurements — 17.73, 17.39, 17.588 — spread 0.34 c/s, mean
**17.57**, against a `cuts.en.chars_per_second` key of **16.1**. The key under-predicts
delivery by 9.1%.

`_chars_per_second_trap` said the fix is BOTH-OR-NEITHER: the budget formula first,
then the key. **fin-script applied the formula fix on this cut** — its Timing budget
section computes `(510 - 62.4) x 16.1 = 7,206` and states it explicitly, rather than
the old `510 x 16.1 = 8,211`. So the precondition the trap named is now met, and this
is the third measurement that was owed. The remaining question is only which rate to
write, and 17.57 is the mean of three cuts spanning MEDIUM and LONG.

Corroborating detail: **every one of the 78 lines drifted negative** against
`expected_seconds` (chars/16.1 + non-trailing pause charges) — not one came in slow.
A key that is merely noisy produces a two-sided scatter; a key that is wrong produces
this. `tools/` is not writable from this stage, so the key is untouched.

### fin-script's hedge held

It sized the script to survive both readings: 492.2s at 17.73, 535.7s at 16.1.
Measured **497.809s** — inside the band, 5.6s off the fast edge, 2.4% under target.
Had it budgeted at 16.1 alone (7,206 chars) this cut would have run ~470s, 8% short.

## Per-line drift (against the 16.1 key + pause model)

Largest deviations, all negative, all inside the `duration_tolerance_pct` 35 band:

| Line | Chars | Expected | Measured | Drift |
|---|---|---|---|---|
| **6.7** | 119 | 8.941s | 6.296s | **-2.645s (-29.6%)** |
| 1.6 | 87 | 7.204s | 5.146s | -2.058s (-28.6%) |
| 4.7 | 105 | 7.072s | 5.512s | -1.560s (-22.1%) |
| 2.3 | 109 | 6.920s | 5.381s | -1.539s (-22.2%) |
| 2.11 | 107 | 6.796s | 5.277s | -1.519s (-22.4%) |
| 3.10 | 113 | 7.169s | 5.460s | -1.709s (-23.8%) |

The two worst are the pause-heaviest lines in the file — 6.7 charges three commas
and two non-trailing periods (1.55s), 1.6 charges three periods and a comma (1.80s).
On those, the over-charge from `tts.pause_seconds` stacks on the under-prediction from
the 16.1 rate, which is how a line reaches -29.6% with only 5.4 points of headroom left.
Raising the rate key to ~17.57 collapses 6.7's drift to about -7%, so the rate fix also
buys back the tolerance margin. No action needed on the script.

Effective delivery spread: slowest **4.4 at 13.81 c/s** (three sentences, four marks —
"It is division. Sixty thousand divided by four percent. …"), fastest **3.10 at
20.70 c/s** (one long unbroken clause). Ratio 1.5x, which is why the pause model exists.

## Scene hold ceiling — no breaches

`scene.max_scene_seconds` is 9.0. Longest measured scene is **6.8 at 8.323s**
(7.523s audio + 0.8 padding), then 5.6 at 7.931s and 5.15 / 6.9 at 7.905s.
**Nothing for fin-storyboard to crop** — the script's self-imposed 120-char line
ceiling did its job, and it did it with 0.68s to spare on the worst scene.

## Artifacts

- `studio/videos/passive-income-number-en/assets/voice/lines.json` — 78 ordered lines
- `studio/videos/passive-income-number-en/assets/voice/{1.1..6.13}.mp3` + `.txt` sidecars
- `studio/videos/passive-income-number-en/assets/voice/timing.json` — ffprobe-measured
- `studio/videos/passive-income-number-en/gen_vo_en.sh` — relative `cd`, survives archival
