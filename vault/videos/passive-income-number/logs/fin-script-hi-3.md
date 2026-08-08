---
summary: fin-script hi attempt 3 — TARGETED EXPANSION of script-hi.md from 5,919 to 6,422 chars (+503) across exactly ten lines in chapters 3–7, to cross YouTube's 8:00 mid-roll threshold that attempt 2 missed by 0.741s. No new lines, no new scenes, no new facts, no new numbers, no register change. 45 of 81 VO lines re-verified byte-for-byte against their voice sidecars; currency purity clean.
updated: 2026-08-08
source: creator brief (attempt 3, 2026-08-08) · tools/format.json cuts.hi.chars_per_second 14.281 · studio/videos/passive-income-number-hi/assets/voice/timing.json (81 measured clip durations) + the 81 <id>.txt sidecars · vault/videos/passive-income-number/facts-staging.md · vault/knowledge/video-studies/passive-income-number.md · vault/knowledge/niches/india-finance-market.md · vault/skills/long_form_scripting.md · vault/CLAUDE.md
stage: fin-script, cut hi, attempt 3
---

# fin-script — passive-income-number, cut hi, attempt 3

**STATUS: ok.** `vault/videos/passive-income-number/script-hi.md` rewritten.

## The problem, restated in one line

The cut was budgeted at **13.03 c/s — a key measured on Harsh, the retired voice.** The voice
is Amrut, measured 2026-08-08 at **14.281 c/s** across all 81 rendered clips. At the true key
the MEDIUM budget is `(510 − 81×0.8) × 14.281 = 6,357` chars; the script held **5,919**. The
voiced cut therefore measured **479.259 s = 7:59.259**, and YouTube places mid-roll only at
**8:00 or longer**. MEDIUM tier exists in this pipeline to earn mid-roll. It was being
forfeited by **0.741 s**.

## What was done

**+503 characters across exactly ten lines. Nothing else changed.** 71 of 81 VO lines are
byte-identical to what is already voiced on disk.

| line | before | after | Δ | modelled scene s | headroom to 9.0 | the content added |
|---|---|---|---|---|---|---|
| **3.5** | 65 | 110 | +45 | 8.078 | 0.92 | The bill did not shrink — only the pocket changed |
| **3.6** | 65 | 117 | +52 | 8.203 | 0.80 | The rate is one stamp on every rung; only the corpus moves |
| **4.4** | 61 | 119 | +58 | 8.152 | 0.85 | Speaks the 3.0% rate inside a derived-income line + "a need, not a nicety" |
| **4.9** | 63 | 117 | +54 | 8.055 | 0.95 | Tax: the hand gets a little less than the ledger — **still zero figures** |
| **5.3** | 57 | 113 | +56 | 7.542 | 1.46 | The division still comes out right; the tank is the question |
| **5.12** | 61 | 105 | +44 | 7.956 | 1.04 | Why 4% dominates — repeated until a paper sounds like a law |
| **5.17** | 73 | 121 | +48 | 8.419 | 0.58 | The inflation MECHANISM: next year's ration costs more, so the draw must rise |
| **6.4** | 53 | 105 | +52 | 7.811 | 1.19 | Closes chapter 1's withheld-number loop out loud |
| **6.8** | 55 | 104 | +49 | 7.948 | 1.05 | A number alone says nothing; meaning comes from comparison |
| **6.11** | 66 | 111 | +45 | 7.948 | 1.05 | Hardens the guard rail — no date, no promise, only a sum and a rate |
| | **619** | **1,122** | **+503** | | | |

**Result: 81 lines · 6,422 chars · 449.7 s VO · +64.8 s padding · 514.5 s = 8:34.5.**
+1.0% over the 6,357-char budget, +0.9% over the 510 s target, **34.5 s past the 8:00 gate.**

## How each constraint was held

| constraint | how |
|---|---|
| No new lines / no new scenes | 81 in, 81 out. No image brief changed. The storyboard does not get more expensive. |
| ≤ ~10 lines touched | Exactly 10. ElevenLabs 290 → **300 of 350**. |
| `max_scene_seconds` 9.0 | All ten modelled 7.54–8.42 s. Tightest is 5.17 at 0.58 s of margin. |
| **6.13 not touched** | Correct — it is the cut's **only** measured breach (9.812 s). Left alone, and now carries the two-`data-framings` instruction. |
| Chapters 1–2 untouched | Zero edits. The 8.682 s hook gate on 1.3 is undisturbed. |
| No return promise | Zero numbers added anywhere. |
| Rate in the same line | **Improved**: 4.4 now speaks «उसी तीन परसेंट पर». The unrated-line count drops 4 → 3 (2.10/2.11/2.12, all locked chapter-2 copy). |
| No corpus → age | 6.11 strengthened: now refuses a date and a promise as well as an age. |
| Banned payout word | Absent, in every form. |
| ₹ only | **Verified by grep: 0 occurrences of the forbidden glyph in the whole file**, prose and notes included. |
| No Latin digits in VO | None added. |
| No first person | No मैं / हम. Every addition is second person or impersonal. |

## The two judgement calls, stated rather than buried

**1. The 117-character flat ceiling is exceeded on two lines, deliberately.** At 14.281 c/s,
9.0 s minus 0.8 s of padding is 117 chars. **4.4 lands at 119 and 5.17 at 121.** They were
allowed because the flat ceiling is a text-only proxy and this cut has 81 *measurements* that
prove it is loose in both directions: **2.4 is 107 chars and measured 7.053 s** (the flat model
over-charged it by a second), while **6.13 is 103 chars and measured 9.012 s** (the flat model
under-charged it into a real breach). Both expanded lines have measured base rates of 17–19 c/s
and were modelled as `measured base + added chars ÷ 14.281 + 0.8`, i.e. the known measurement
for the existing text plus the *cut mean* — deliberately the conservative half — for the new.
**The arbiter is `probe()` after TTS, and the script says so.**

**2. The mid-video drop zone now opens on a reveal, not on the warning.** Attempt 2 had
«बारह परसेंट चेतावनी है» opening the 55–65% window at 54.5%. The expansion pushes 5.6 to
**4:36.3 (53.7%)**, about 1.5 s before the window opens, so the window now opens on **5.8** —
the government's own scheme, and its ₹9 lakh cap two clips later. That is still tension rather
than a flat transition, which is what the retention rule actually asks for, but it is a
0.8-percentage-point trade taken to buy mid-roll and it is recorded in the script rather than
smoothed over.

## Corrections this attempt hands forward (both found in the measured data, neither asked for)

1. **The two-framings scene is 6.13, not 2.4.** Attempt 2 predicted 2.4 at 9.01 s from the flat
   model and ordered two `data-framings` there. **2.4 measured 7.853 s and needs one.** 6.13
   measured **9.812 s** and is the cut's only breach. The storyboard would otherwise have been
   handed the instruction backwards, on the exact scene that carries the video's best beat.
2. **The attempt-2 register note was wrong by 9.6%, and the reason is now recorded.** It
   reasoned from a 118.0 s *continuous* reference read that Amrut ran ≈13.09 c/s. A continuous
   read carries inter-sentence pause inside the audio; per-line clips push that pause out into
   `lead_in + tail` where it stops counting as speech. Same 21 lines: 118.0 s continuous vs
   107.20 s as clips.

## Verification performed (no Bash available to this stage)

- **Currency purity — the one thing `check_script` actually tests:** grepped the whole file for
  the forbidden glyph. **0 occurrences.** File is far over the 500-byte floor. Both `check_script`
  assertions therefore pass by inspection; the orchestrator runs the command itself.
- **Devanagari fidelity.** `Edit` was not available to this stage, so the change could only be
  delivered as a whole-file `Write` — which puts all 81 VO lines through a rewrite and risks a
  silent nukta / chandrabindu swap that is inaudible until the render. Mitigation, in two parts:
  - **45 of 81 lines re-verified byte-for-byte** by grepping the script for the exact contents
    of their `assets/voice/<id>.txt` sidecars — deliberately weighted to every nukta-,
    chandrabindu- and conjunct-heavy line in the cut (फ़ोन · ऑफ़िस · ख़बर · तनख़्वाह · सब्ज़ी ·
    ख़त्म · ख़तरा · तेज़ी · ख़ुद · जाँच · थोड़ा-थोड़ा · वक़्त · रक़म · ख़र्चे · डेढ़ · साढ़े · एक-चौथाई ·
    ईंट · सीढ़ियाँ · आख़िरी · क़रीब · ख़ास · पहुँचे · साफ़ · ज़्यादातर · ख़ाली · आँकड़ों). **Zero drift.**
  - **All ten touched lines confirmed to preserve their original text exactly** — nine append
    after the existing danda, and 4.4 takes a mid-line insertion whose two surrounding fragments
    both matched their sidecar.
  - **The remaining 36 are covered by a free mechanical gate**, written into build handoff item
    2: `tools/tts/batch.py` compares every line to its sidecar on resume and prints REGEN per
    changed line. **Exactly ten REGENs are expected. Eleven or more means this rewrite drifted a
    character and the run must stop, restore from the sidecar, and not spend the call.** That
    converts an unverifiable risk into a detectable one at zero cost — and it protects the call
    budget, since a false REGEN both wastes a call and ships a subtly different reading.

## Owed / next

1. **Re-voice exactly ten clips** — 3.5 · 3.6 · 4.4 · 4.9 · 5.3 · 5.12 · 5.17 · 6.4 · 6.8 ·
   6.11. **Run the resume, not `--force`.** Cost 290 → 300 of 350.
2. **Re-probe those ten and rebuild `timing.json`.** Any scene landing over 9.0 s takes the
   two-`data-framings` treatment. 5.17 is the one to check first.
3. **Re-measure the flat rate on the ten new clips** and record it beside 14.281. These are the
   first Amrut clips of *newly written* style-E text; a ~1.5% negative drift is expected
   (`rate_key_en_followup`) and is not a defect. Do not re-key `format.json` off ten lines.
4. **fin-audit hi attempt 3** — re-audit the ten changed lines only. Everything else is the
   artifact that already passed.
5. **Verify the deliverable at the end.** The point of this attempt is a runtime. `ffprobe` the
   final encode: **if it lands under 480 s the expansion failed**, and nothing downstream of it
   matters.
6. **Update `run.json`** — `stages.fin-script-hi` to attempt 3, `budget.elevenlabs_calls` to 300
   after the re-voice, and replace the `chapters.hi` two-framings note (it currently implies
   2.4). The `_carry_forward_to_storyboard_hi` tint note on 5.2 / 6.13 still stands and is
   restated in the script's cues.
