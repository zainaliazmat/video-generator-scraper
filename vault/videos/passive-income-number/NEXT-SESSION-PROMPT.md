---
summary: Handover for resuming the passive-income-number run (rewritten 2026-08-08 after a session-limit stop). Session file — delete once folded into the milestone note.
updated: 2026-08-08
source: this run's run.json, stage logs and chapter reviews.
---

Resume the `passive-income-number` finance video run:

```
/finance-video --resume passive-income-number
```

`vault/videos/passive-income-number/run.json` is authoritative. Read it first — it now
carries a complete per-chapter map, the creator's `constraints`, both measured hook
gates, the budget, and **eight root-cause tool fixes** made on 2026-08-08.

## Stopped by a session limit, not by a failure

Two agents were killed mid-flight (limit reset 9:10am Asia/Karachi). **Neither wrote a
log, so neither stage is done**, and nothing in `run.json` claims otherwise — every
stage marked `done` was re-verified against disk after the stop.

## The two next actions

1. **`fin-ceo` on en chapter 1.** The chapter has `fin-editor` PASS (round 3, 0 blockers,
   0 should-fix) and is waiting only on the CEO gate. The dispatched agent died before
   writing anything, so the gate has **not** been attempted. Artifacts are on disk:
   `renders/DRAFT-ch1.mp4` (1393 frames / 46.433s / 0 black segments) and a regenerated
   `renders/SHEET-ch1.jpg`.
2. **`fin-build` on hi chapter 1.** ⚠ **Do not trust `index.html` in that project.**
   `build.mjs` and `package-lock.json` are new and possibly incomplete; `index.html` is
   still the **old style-A build from 2026-08-07**. The style-E rotation re-keyed the
   image filenames, so the old composition now points at the *new* photographs and would
   render the right slots with the wrong pictures, every check green. Regenerate
   `index.html` from `build.mjs` before anything else.

## Where each cut stands

**en (6 chapters).** script · audit · voice · storyboard all done. ch1: assets ×3,
build ×3, draft ×3, editor PASS — awaiting CEO. ch2: assets PASS (16 accepted, 128
rejected), build not started. ch3–6 not started.

**hi (7 chapters).** script · audit · voice · storyboard all done and measured. The cut
runs **519.331s = 8:39.331**, clearing YouTube's 8:00 mid-roll floor by 39.3s — it was
7:59.259 before a deliberate expansion (see `hi_length_decision`). ch1: assets PASS,
build half-written. ch2: not started, but its style-A photographs are reusable. ch3–7 not
started.

**Budget: ElevenLabs 300 / 350.** Enough for ~50 more clips. vidIQ **13 credits** against
a ~35-credit close-out packaging pass, resetting 2026-08-29 — still unresolved: ration
it, defer the title lock, or run one market only.

## Uncommitted code

`vault_commit.py` only touches vault paths by design, so these are **still uncommitted**
and will be lost if the tree is reset:

- `tools/pipeline_check.py` — chapter-aware `check_build`, comment stripping, the
  duration band
- `tools/tts/batch.py` — the `.voice` stamp
- `tools/chapter_sheet.py` — settle on all drawn art, plus a new `--selftest`
- `.claude/agents/fin-audit.md` — gained `Write`
- `studio/videos/passive-income-number-hi/gen_vo_hi.sh` — the corrected `--force` note

## What this session learned (all recorded in run.json / the vault)

Seven of the eight fixes are one bug wearing different clothes: **a check reporting green
over the exact thing it existed to catch.** The eighth is its inverse — a grep that
reports a false blocker.

- `check_build` refused `--chapter`, so the whole chapter loop had **no build
  postcondition**; the Lottie guard fired on the comment explaining the trap it prevents.
- The duration check **double-counted pause silence** the rate key already contained —
  proven general by measuring both cuts, then fixed by making the estimate a *range*,
  since a pause mark is a request the engine honours variably.
- The TTS resume **could not see a voice change**. 17 lines were byte-identical across
  the Harsh→Amrut switch and would have shipped chapter 5 half in the retired voice, with
  every check green — nothing downstream tests timbre.
- `fin-audit` **had no tool that could create its own required log**, so it correctly
  reported failure on a passing audit.
- **`R−B ≥ +40` was unreachable.** Only ~9% of a photograph's warmth survives to the
  encoded frame (`encoded = 0.0927 × source − 6.43`); a source of ~+500 would be needed.
  Warmth is chrome, not photograph. Retired — it had cost four fetch rounds.
- `chapter_sheet.py` sheeted a **tick cascade one third built** — third occurrence of
  that failure, third kind of art. Now keyed off the whole `v-` family.
- A **grep for `₹` on the notification Lottie returns 0 and always will** — the generator
  draws the mark as five round-capped strokes, not text. Verify from the generator or the
  encode, never the artefact.

Two gaps recorded as **owed** rather than built mid-run, both with reasons in `run.json`:
the derived-income assert is frame-only and cannot see a VO line speaking money over a
bare frame; and md5 dedupe cannot catch a photograph that lives in both stock pools at
different resolutions (Pexels has ingested part of Pixabay — the tell is a "by Pixabay"
credit).

## Two questions still open for `fin-editor`, both deliberately unruled

- **hi 1.3→1.4** is a dissolve, not the script's declared continuous zoom, because the
  reused chai-glass counter has no phone in it. The en cut's equivalent joint was an
  editor blocker when it read as two pictures, and its fix — point both scenes at one
  file — is unavailable here.
- **en s10 could not source "the tank"** (6 sheets, 36 candidates). It resolves as a
  brass tap on a plain steel body. This matters beyond one frame: the tank-and-two-taps
  analogy is style E's load-bearing device, the mid-video yield-trap beat is written as
  its callback, and s46/s47/s57 inherit the object family. If the image cannot say TANK,
  the callback lands on an object the viewer was never shown.

## Still owed

A real study packet (`study.py --ids JiuVKaO2a6c Jn3N9OzSY1c`) once yt-dlp cookies exist —
`YTAUTO_COOKIES` / `YTAUTO_COOKIES_BROWSER` were added to `study.py`. The current study
was built from two bought vidIQ transcripts, so its visual half is recorded MISSING, not
faked.
