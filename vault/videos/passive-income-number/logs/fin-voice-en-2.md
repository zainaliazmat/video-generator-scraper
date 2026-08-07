---
summary: fin-voice for passive-income-number cut en, attempt 2 (style-E restyle, 81 lines). 53 ElevenLabs calls, not 81 — batch.py's .txt sidecar resumed 28 clips whose style-E text is byte-identical to attempt 1's. Zero failures, zero retries. Measured total 527.873s against the 510s target (+3.50%). HOOK GATE MEASURED, not estimated: the promise (1.3) opens at 9.571s and closes at 13.683s, so the 15s gate clears with 5.43s of headroom — fin-audit's pause-loaded 15.5s worst case does not materialise. One scene breaches max_scene_seconds: 2.2 at 10.596s, already flagged in the script's own cue as needing two data-framings.
updated: 2026-08-07
source: tools/tts/batch.py run output + studio/videos/passive-income-number-en/assets/voice/timing.json (ffprobe-measured) + ffprobe/lavfi silencedetect on 1.1-1.4 + tools/format.json cuts.en / tiers.medium / scene.
stage: fin-voice, cut en, attempt 2 — PASS
---

# fin-voice — passive-income-number, cut en, attempt 2 (style-E restyle)

## Gate checks (before spending)

| Guard | Value | Verdict |
|---|---|---|
| `audit-en.md` contains PASS | PASS on the verdict line ("Passed **with two edits**") | **cleared** |
| Char total vs 1.3x budget | 8,017 vs 11,649 (510 x 17.57 x 1.3) | **cleared, 69% of ceiling** |

Voice, model and style all read from `format.json cuts.en` by `batch.py` — nothing
hardcoded. **Brian `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0**, unchanged
for this cut (the hi cut's move to Amrut does not touch it).

## Extraction — 81 lines, by line key

The script was re-read from disk after both changes (the style-E restyle and fin-audit's
in-place edit to **4.8**). Attempt 1's numbering is dead: its 78-line map does not survive
the restyle.

Lines were taken **by the `**<ch>.<n>**` marker**, never by grepping `^> `. The file carries
**176 blockquote lines in total and 100 inside `# THE SCRIPT`**; only the 81 sitting directly
under a line key are narration. A `^> ` sweep would have put 95 non-VO blocks — the SIX
THINGS banner, the chapter preambles, the chapter-4 conflation warning — onto the job as
speech. The backtick `[arch: … ]` line under each VO block is layout and never entered.

**4.8 was voiced from the post-audit text**, verbatim:

> The papers tested how long a tank lasts at each rate, and no advertisement changes that.

Extraction was verified against the script's own per-scene char table before spending
(1.1=49 · 1.2=75 · 1.7=118 · 2.2=155 · 3.3=116 · 4.8=88 · 5.3=73 · 6.7=119, all exact).
Programmatic recount after the run: **8,017 chars against fin-script's 8,014 hand estimate
(+3, 0.04%)** — the table is one char light at 2.11 and 3.5, three heavy at 5.5.

## The run — 53 calls, not 81

`python3 tools/tts/batch.py --project studio/videos/passive-income-number-en --cut en`

- **53 ElevenLabs calls.** Zero failures, zero retries, no `--force`. Every clip written
  first attempt. Cumulative run total: **209 of 350**, not the 237 the ceiling was raised for.
- **28 clips resumed** rather than regenerated. This is not a shortcut and not a stale-audio
  risk: `batch.py` skips a clip only when `<id>.txt` — written immediately before that clip's
  synth call, so it is an exact record of what the mp3 says — matches the new `lines.json`
  text **byte for byte**. The other 53 printed `REGEN (text changed since last take)`, which
  proves the comparison was live rather than silently skipping everything.
- The skips are also a free correctness proof of the extraction: 28 lines I sliced today are
  byte-identical to the 28 attempt 1 sliced independently. One wrong character in any of them
  would have shown up as a REGEN.
- Resumed lines are concentrated where style E left the prose alone: **1.7** (the untouchable
  line), **2.1**, **3.1**, **3.2**, **4.1**, **4.5**, **4.6**, **5.1–5.4**, **5.10–5.13**,
  **5.16**, **6.1–6.10**, **6.12**, **6.13**. Chapters 1–4 regenerated almost entirely; the
  style-E signposts ("Work it through —", "Think of it this way —", "Notice this —") land
  mostly in the front half.
- Postconditions (size, duration-vs-chars at ±35%, silence floor, scene arithmetic):
  **zero problems**. Smallest clip 44,347 bytes against `min_clip_bytes` 10,240; shortest
  2.090s (3.1) against `min_clip_seconds` 1.0.

`gen_vo_en.sh` already existed for this project, with a **relative** `cd` to repo root and
the exact batch line above. Re-read and left unchanged — it is this project's own script, not
a borrowed one with a hard-coded cd elsewhere.

## Measured runtime

| | Seconds |
|---|---|
| VO audio (81 clips, ffprobe) | 463.073 |
| Inter-line padding (81 x 0.8, `tiers.medium` 0.25 + 0.55) | 64.800 |
| **Measured total** | **527.873 (8:47.9)** |
| Target (`tiers.medium.target_seconds`) | 510 |
| **Drift vs target** | **+17.873s, +3.50%** |
| fin-script's projection | 520.9 |
| **Drift vs projection** | **+6.97s, +1.34%** |

Average scene **6.517s** against `target_scene_seconds` 6.5 — effectively on the nose.

## The 17.57 rate key — confirmed within 1.5%, but style E is slower per char

**8,017 chars / 463.073s = 17.313 c/s flat**, including pause silence.

| Cut | Register | Chars | VO seconds | Flat c/s |
|---|---|---|---|---|
| first-lakh-first-thousand-en | style A | 7,657 | 432.00 | 17.73 |
| japanese-money-methods-en (LONG) | style A | 9,619 | 626.59 | 17.39 |
| passive-income-number-en attempt 1 | style A | 7,657 | 435.409 | 17.588 |
| **passive-income-number-en attempt 2 (this)** | **style E** | **8,017** | **463.073** | **17.313** |

The new 17.57 key is **1.5% optimistic** for this cut, which is why the script landed 3.5%
long against a 520.9s projection that assumed it. The cause looks mechanical rather than
noisy, and it is the same mechanic as the documented SHORT caveat: **style E is
punctuation-denser than style A**. The restyle added an em-dash signpost to nine lines and
broke the arithmetic into stepped sentences, so a larger share of each clip is pause rather
than speech, and the flat chars/second comes out lower.

Adding this measurement gives a four-cut mean of **17.505**. That is a 0.4% move on a key
that is 1.5% off for this register — **not worth changing on one cut**, and `tools/` is not
writable from this stage anyway. The honest recommendation is to leave 17.57 and let fin-script
carry a register note: a signpost-heavy script should budget nearer 17.3.

## Largest per-line drift

Against `pipeline_check.expected_seconds` (chars / 17.57 + non-trailing pause charges).

| line | expected | measured | drift |
|---|---|---|---|
| **6.7** | 8.32s | 6.296s | **−2.03s, −24.4%** ← largest, absolute and % |
| 2.11 | 6.72s | 5.747s | −0.97s, −14.4% |
| 2.13 | 6.24s | 5.277s | −0.96s, −15.4% |
| 3.4 / 3.9 | 6.58s | 5.799s | −0.78s, −11.9% |
| 2.15 | 6.39s | 6.949s | +0.56s, +8.7% ← largest positive |
| 2.2 | 9.57s | 9.796s | +0.22s, +2.3% |

All 81 inside `duration_tolerance_pct` 35 — `batch.py` flagged none.

**6.7 is the one to know about.** It is three short sentences, so the model charges it 1.55s
of pause (two non-trailing full stops plus three commas) and Brian takes barely a third of
that. It also carries a 3-item cascade in the frame; at 6.296s of audio the cascade's
`0.6s` gaps and `first_cue_by_seconds` still fit, but there is less slack there than the
script's 6.8s estimate implies.

**The drift is now two-sided.** On attempt 1 all 78 lines drifted negative, which is what
established the old 16.1 key was wrong rather than noisy. Here the scatter runs both ways
(−24% to +9%), which is the signature of a key that is roughly right per line.

## HOOK GATE — measured, not modelled

fin-audit could not settle this from text: a flat-rate model put the promise at 10.9–13.0s,
a pause-loaded reading at ~15.5s against a 15s gate, and lines 1.1–1.3 are creator-approved
verbatim so an overshoot would have had no script fix. So it was measured off the rendered
audio with `silencedetect` and the timeline in `timing.json`.

Method: onset = `timing.json audio_start` + the leading silence inside the clip, both measured.
`silencedetect=noise=-50dB:d=0.03` via `ffprobe -f lavfi -i "amovie=…"`.

| clip | audio_start | speech in-clip | **speech on the timeline** |
|---|---|---|---|
| 1.1 | 0.250 | 0.070 → 2.407 | 0.320 → 2.657 |
| 1.2 | 3.793 | 0.000 → 4.573 | 3.793 → 8.366 |
| **1.3 (the promise)** | **9.504** | **0.067 → 4.179** | **9.571 → 13.683** |
| 1.4 (the payoff buzz) | 14.849 | 0.000 → 5.839 | 14.849 → 20.688 |

**`hook_gate_en` = 9.571s** — the onset of "And on that same day, before noon, money is
deposited into your account." It **closes at 13.683s**.

- **Gate 15s: CLEARED.** 5.43s of headroom at the open, 1.32s at the close.
- **Threshold-insensitive.** Re-run at `-40dB` the leading silence moves from 0.0669 to
  0.0673 and the last speech from 4.179 to 4.167 — a 4ms change in the onset. This is not a
  measurement sitting on a detector setting.
- **fin-audit's 15.5s worst case does not happen.** The pause-loaded model over-charges
  chapter 1 by ~1.5s: it bills 1.2 two full stops at 0.55s each, and Brian delivers the whole
  line 0.46s *faster* than chars/17.57 alone.
- fin-script's cue estimate (opens 8.7s, closes 12.8s) is the right shape but **0.87s early**
  on both ends. If the cue text matters downstream it should read 9.6 / 13.7.
- Dead air between 1.2's last word and 1.3's first is **1.205s** (1.2's own 0.338s tail +
  0.55 tail + 0.25 lead-in + 1.3's 0.067s head). That is the largest silence in the cold open
  and it sits immediately before the promise, which is the right place for it.

No script fix is needed, so the creator-approved verbatim block is untouched.

## Scene budget — one breach of `max_scene_seconds` (9.0)

| line | audio | scene (audio + 0.8) | verdict |
|---|---|---|---|
| **2.2** | **9.796s** | **10.596s** | **BREACH, +1.596s** |
| 5.15 | 7.706s | 8.506s | clear |
| 6.8 | 7.523s | 8.323s | clear |
| 1.8 | 7.471s | 8.271s | clear |
| 2.3 | 7.367s | 8.167s | clear |

Only **2.2** breaches, and the script's own cue predicted it:

> `⚠ 155 chars = 9.6s — THIS SCENE NEEDS TWO data-framings: wide on the tank, then a push to the tap`

Measured 9.796s, so the estimate was right and slightly light. `check_build` fails a scene
holding **one photo** past `max_scene_seconds`, so this is solvable in the storyboard with the
second data-framings crop the cue already specifies — **no re-time and no re-voice**. 2.2 is
the tank plant, load-bearing at 4.7, 4.8 and 5.5; shortening it would cost three callbacks.

## For run.json

- `budget.elevenlabs_calls`: 156 → **209** (53 this stage). The `_spend_log` should record that
  the restyle cost 53 rather than the projected 81, because 28 style-E lines survived the
  restyle unchanged and resumed off their `.txt` sidecars.
- `hook_gate_en`: **9.571s onset / 13.683s close**, measured, 15s gate cleared.
