# fin-script — japanese-money-methods, cut `en`, attempt 1

**Result:** ok · **Artifact:** `vault/videos/japanese-money-methods/script-en.md`
**Date:** 2026-08-01

## What was read

`vault/CLAUDE.md` · `tools/format.json` (rates, tiers, scene, layout, colors) ·
`vault/videos/japanese-money-methods/facts-staging.md` ·
`vault/knowledge/video-studies/japanese-money-methods.md` ·
`vault/skills/long_form_scripting.md` · `vault/knowledge/us-english-script-style.md` ·
`vault/videos/japanese-money-methods/run.json` · `script-hi.md` (**structure only**) ·
`tools/pipeline_check.py` (to confirm which rate the drift check uses).

`haryanvi-hindi-script-style.md` and `india-finance-market.md` were **not** read — wrong lane
for this cut.

## Output

- **92 lines / 8 chapters / 9,581 chars.** Estimated runtime **668.7s (11:09)** against the
  660s target = **+1.3%**. LONG floor (`tiers.long.min_seconds` 600) cleared by 68.7s at the
  format.json rate and by 14.0s at the measured rate (see below).
- Per-scene timing table included (chars → est s at 16.1 c/s, +0.8s lead-in/tail per line).
- Longest line 128 chars (8.0s VO + 0.8 = 8.8s, under `max_scene_seconds` 9.0). Shortest 61.
  Self-imposed ceiling: **130 chars/line**.

## The one judgement call worth flagging

`format.json` carries two disagreeing truths for this cut: `cuts.en.chars_per_second` = 16.1,
and `cuts.en._chars_per_second_trap` recording a **measured 17.73 c/s flat**, with the
instruction "fix the budget formula FIRST, then the rate" and "DO NOT raise this key on its
own". The formula fix is applied (padding subtracted from the target before the rate). The
key was not changed — `tools/` is not writable from this stage.

Budgeting at 16.1 alone gives 9,441 chars → **606s** at the measured rate, six seconds off
breaching the LONG floor. Budgeting at 17.73 alone gives 10,396 chars → **719s** at the key's
rate, 9% long. **9,581 is the overlap**: 668.7s at 16.1, 614.0s at 17.73. Both readings are
inside spec. The table making this explicit is in the script under "The two-rate hedge", and
build handoff item 5 asks the build stage to measure the real flat rate and, if it lands at
17.73 again, fix the key with the measurement rather than re-padding scripts.

`pipeline_check.expected_seconds` uses the 16.1 key plus `tts.pause_seconds` with a 35%
symmetric tolerance — a line delivered at 17.73 against a 16.1 estimate is ~17% off, so no
clip in this script can self-flag as truncated on rate alone.

## Contract compliance

- **US rewrite, not a translation.** Dollars only. The Indian cut's currency glyph does not
  occur in the file (nor in this log). US shocks and institutions throughout: direct deposit,
  six-month auto-insurance renewal, DoorDash, streaming auto-renewal, closet/fridge/
  subscriptions screen, a repair estimate on a shop lift, a generic FDIC-insured high-yield
  savings account at a different bank, Federal Reserve G.19 and SHED. Japan is confined to
  the story frames; every act-now frame is American (build handoff item 7 lists them).
- **Premise correction honoured.** Opens on the pain-mirror (0:00–0:59, zero stats), then
  Japan's own two numbers — 37.8% FIES vs about 1% SNA, one government, one year, more than
  thirty times apart. Chapter 3 states on screen that culture is **not** a major determinant
  (J7) and gives the real drivers. No "Japan doesn't go broke because of culture" anywhere.
- **No saving-rate head-to-head.** The US personal saving rate (U1 2.7%, U2 3.0%) is used
  **nowhere** — deliberately, by the same adjacency logic the hi cut used to drop India's
  rate; it is documented in "Deliberately NOT used". The only cross-market beat is 3.5, the
  BOJ Chart 2 column pair, and its `foot:` says ASSET MIX ONLY and explicitly "NOT a
  saving-rate comparison".
- **Every number traces.** Fact-trace table maps all 20 figure/claim groups to J1–J8, U4–U7,
  §4 rows, with HARD/SOFT/COMPUTED/CONVENTION tags. The two COMPUTED ratios (3.2) carry an
  `ILLUSTRATIVE` foot and hedged VO ("about" twice). No number is attached to mottainai,
  hara hachi bu or taru wo shiru. No "121 years". No yen conversion.
- **Digits spelled out in VO** ("thirty-seven point eight percent", "nineteen oh four",
  "four thousand dollars", "thirty-two hundred dollars"); on-screen numerals carry the exact
  figures. Acronyms too: VO says "federally insured", the screen says FDIC — an initialism
  is the same coin-flip risk as a bare digit.
- **Persona rules.** No "I", no "we", no credential claim, no fund/stock/account/app/bank
  pick. The card APR and the SHED figure are price/evidence rows with sourced feet; the
  savings account is generic and 5.7's foot says so on screen.
- **VO in the VO block only**; all on-screen text English/romaji, subset-safe (`ABOUT 1%`,
  `ABOUT 22%`, `30 TIMES`, `JPY 197,432` — no tilde, no multiplication sign, no CJK, no yen
  glyph). Kanji appear only inside the photograph at 7.3/7.4.

## Retention architecture

Promise 0:59 · first number 1:15 (16s later) · drop-zone opener 5.11 at 6:45 = 60.5% (the
"this fails in month one, and that is not your fault" honesty beat) · Von Restorff admission
6.7 at 7:44 = **69.3%** (the four categories are a later Western addition) · unpromised
fourth method opens 8:47 = 78.9% · single stacked CTA 8.7–8.8 at 97.8%. Participation beat
(pause the video, three physical checks) at 4.5–4.7. Seven `RAIL OFF` scenes as the
anti-sameness device.

## Owed / risks for the next stage

1. **ElevenLabs budget.** `run.json` caps the run at 30 calls; hi (92) + en (92) = 184.
   Decide before generation, not during.
2. **No US-market competitor study exists** for this topic (study note: the `japan` lane
   returned macro and history). Every packaging decision in this cut is inferred from the
   Hindi cut plus MID's receipts-on-screen finding — flagged, not resolved.
3. **The rate key.** See above; it is a `format.json` edit for the orchestrator or a between-
   runs fix, not something this stage may write.
