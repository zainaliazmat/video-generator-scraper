---
summary: fin-voice for passive-income-number, cut hi, attempt 1. 78 ElevenLabs calls, one per VO line, zero retries and zero waste. timing.json measured at 488.222s against a 510s target (-4.3%). Two thin margins re-measured: 5.14 cleared its hold ceiling with 0.49s to spare, but the 15-second hook gate landed at ≈15.0s, not the ≈13.9s the audit predicted.
updated: 2026-08-07
source: vault/videos/passive-income-number/script-hi.md as on disk 2026-08-07 (post fin-audit edits to 5.9, 5.14, 7.6); tools/format.json cuts.hi + tiers.medium; tools/tts/batch.py output; ffprobe.
stage: fin-voice, cut hi, attempt 1
---

# fin-voice-hi-1 — passive-income-number

STATUS: ok

## Gate checks before spending

| Guard | Value | Verdict |
|---|---|---|
| `audit-hi.md` contains PASS | yes (PASS, "passing with edits") | cleared |
| Char total vs 1.3× budget | 5,565 measured vs 1.3 × (510 × 13.03) = 8,639 | cleared, 36% under |
| Line count vs `tiers.medium.lines` | 78 vs 78 | exact |
| Voice | `HTUuC7OeeEt6OL5fViVe` (Harsh), `eleven_multilingual_v2`, style 0 — read from `format.json cuts.hi`, not hardcoded | correct |

## Extraction

Extracted **by line key**, `1.1 … 7.8` — never by grepping `^> `. The script carries ~33
guard/rationale blockquote lines (the SIX THINGS block, chapter preambles, the retention
notes); a `^> ` sweep would have put every one of them into the job and turned a 78-call
run into ~111 calls of which a third would be English prose read in a Hindi voice. The
extraction anchors on the `**N.M**` marker and takes the single `> ` line that follows it.

Text sliced from the file as it exists on disk **after** the fin-audit rewrites — 5.9,
5.14 and 7.6 are the audited strings, not fin-script's originals. No hash from an earlier
stage was trusted. `batch.py` writes an `<id>.txt` sidecar next to every clip immediately
before the call, so the pairing of text→audio is now recorded per clip and a later edit
re-voices only the line it touched.

Written to `studio/videos/passive-income-number-hi/assets/voice/lines.json` as the
canonical ordered `[{"id","text"}]` array. (The script's Build-handoff §1 names the file
`hindi-lines.json`; `pipeline_check.load_lines` only reads `lines.json`, so the tool's
name wins.)

## Spend

**78 ElevenLabs calls. Zero retries, zero failures, zero regenerations.** Every call
returned 200 and a non-trivial mp3 (smallest 28,465 bytes on 1.3, largest 127,939 on
6.13). Run budget moves 0 → 78 of 188; 110 remain, of which the en cut needs ~78.

## Measured timing

`timing.json` written by `batch.py` with ffprobe durations — not hand-written, not
estimated. MEDIUM padding 0.25 lead + 0.55 tail per line (`tiers.medium`), 62.4s total.

- **Total runtime 488.222s (8:08) vs the 510s target — −21.8s, −4.3%.**
- The script's own table predicted 513.4s. The whole gap is a char over-count: the budget
  table assumed 5,876 chars, the extracted text measures **5,565** (−5.3%). The estimate
  was per-line and eyeballed; these are the real counts.
- **Delivered rate: 5,565 chars ÷ (488.222 − 62.4) = 13.07 chars/s flat.** That is a
  fourth independent confirmation of `cuts.hi.chars_per_second` = 13.03, to within 0.3%.
  The hi key is sound and needs no change. (Contrast the en key, which `format.json`
  records as measured wrong three times running.)
- `check_voice_dir` returned **zero problems**: no clip under 10,240 bytes, none under
  1.0s, none silent, every `duration` within 0.05s of ffprobe, scene arithmetic exact on
  all 78, total matching the sum of scenes.

## The two thin margins the audit flagged — both re-measured

### 1. The 15-second hook gate: AT THE WIRE, not clear

The audit predicted the withheld number is named at **≈13.9s**. Measured, it is
**≈15.0s** — right on the line, with no margin.

The preamble is not the cause; it ran slightly fast. Measured scene spans:
1.1 = 3.961s · 1.2 = 5.816s · 1.3 = 2.550s → 1.4's scene starts at **12.327s**, audio at
**12.577s** (the estimate was 12.5s, so 1.1–1.3 are 0.17s *ahead*).

The drift is inside 1.4 itself. Silence detection on `1.4.mp3` (ffprobe + silencedetect,
−40 dB / 0.12s):

```
silence_start: 1.14893   silence_end: 1.61807   (0.469s — the em-dash)
silence_start: 3.63696   silence_end: 3.97245   (trailing)
```

So "आप अमीर नहीं हुए" occupies 0 → 1.149s, the em-dash costs a measured 0.469s, and the
clause that actually names the number — "आप बस एक ख़ास नंबर तक पहुँच गए।" — does not begin
until **1.618s** into the clip. The word नंबर sits at 45% of that clause by character and
36% by syllable, so its onset is 2.35–2.53s into the clip:

**timeline onset of नंबर ≈ 14.9 – 15.1s.** Line 1.4 ends at 16.574s.

The audit's 13.9s assumed the number arrives about 1.15s into 1.4. It arrives about 2.4s
in, because four words plus a half-second em-dash pause precede it. The gate is met or
missed by about a tenth of a second depending on how it is scored.

**This is not fixable here and was not fudged here.** The audio is correct for the text;
timing.json reports what was measured. If the gate must hold with real margin, the fix is
in the script and is small — either drop the em-dash clause from 1.4 so the number leads
the line, or trim 1.2 (5.816s, the longest of the three preamble scenes) by ~1s. Both are
fin-script edits; re-voicing would then cost 1 or 2 calls via `--only`.

### 2. Line 5.14 vs the 9.0s hold ceiling: CLEARED

Predicted 8.70s against `scene.max_scene_seconds` 9.0. Measured **7.706s of audio →
8.506s of scene**, i.e. **0.494s of margin** — nearly double the predicted 0.30s. Harsh
delivered the longest line in the cut faster than the flat rate (0.975× expected). No
script change needed, and the script's "no line may exceed 105 characters" rule holds.

The tightest scene in the cut is not 5.14 — it is **6.13 at 8.767s** (0.233s under the
ceiling), 100 chars. Also passing, but it is the one to watch if anything is re-voiced.

### 3. A hold that DOES breach — already known, belongs to build

2.6 (5.998s) + 2.7 (8.036s) = **14.034s on one photograph**, because 2.7 holds 2.6's
image. That is a `max_scene_seconds` breach by construction, and the script's Build-handoff
§7 already calls it and prescribes the fix: give 2.7 a second, tighter crop of the same
source and run the pair as one continuous zoom, never a self-dissolve. Measured 14.034s
against the script's predicted 14.1s. Flagging it forward to fin-storyboard/fin-build.

## Per-line drift

Against the flat 13.03 c/s budget model (measured ÷ chars/13.03):

| | line | chars | measured | flat estimate | drift |
|---|---|---|---|---|---|
| slowest | **4.4** | 71 | 6.766s | 5.449s | **+1.317s (+24.2%)** |
| | 4.3 | 38 | 3.527s | 2.916s | +0.611s (+20.9%) |
| | 5.10 | 82 | 7.523s | 6.293s | +1.230s (+19.5%) |
| fastest | **7.6** | 94 | 6.034s | 7.214s | **−1.180s (−16.4%)** |
| | 4.8 | 63 | 4.075s | 4.834s | −0.759s (−15.7%) |
| | 6.14 | 94 | 6.165s | 7.214s | −1.049s (−14.5%) |

Largest per-line drift = **+24.2% on 4.4**, and it is explained rather than anomalous:
"आटा, दाल, चावल, तेल, दूध, सब्ज़ी — हर महीने, बिना आपकी तनख़्वाह को छुए।" carries six commas,
an em-dash and a danda = 1.90s of scored pause under `tts.pause_seconds`. Against
`pipeline_check.expected_seconds` (chars/rate **plus** those pauses) it reads as −8%, well
inside the ±35% band. Nothing in the cut approached the tolerance; `check_voice_dir` flagged
zero lines.

## Files written

- `studio/videos/passive-income-number-hi/assets/voice/lines.json` — 78 entries
- `studio/videos/passive-income-number-hi/assets/voice/{1.1…7.8}.mp3` + `.txt` sidecars
- `studio/videos/passive-income-number-hi/assets/voice/timing.json` — measured
- `studio/videos/passive-income-number-hi/gen_vo_hi.sh` — regeneration script, `cd`s to the
  repo root via `$(dirname "$0")/../../..` rather than hardcoding an absolute studio path
  (the archive gotcha in `vault/CLAUDE.md` §5: every previous `gen_vo_*.sh` hardcoded a `cd`
  into a directory `archive_cut.py` later deletes, so it cannot be run after archiving)

## Notes for the next stage

1. The hook-gate finding above is the one decision the orchestrator owns. Voicing is
   complete either way; a script fix costs 1–2 `--only` calls, not a re-run.
2. Runtime is 21.8s short of target. If that matters, it is head-room, not a defect — the
   pace is 6.26s/scene against `target_scene_seconds` 6.5, so scenes are marginally brisk
   rather than dead. No scene exceeds 9.0s.
3. `timing.json` is now the single source for the composition's four timing copies. Do not
   re-derive durations anywhere; ffprobe cross-checks downstream will catch it.
