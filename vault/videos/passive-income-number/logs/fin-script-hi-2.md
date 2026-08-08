# fin-script — passive-income-number, cut `hi`, attempt 2 (STYLE E RESTYLE)

**Result:** ok · **Artifact:** `vault/videos/passive-income-number/script-hi.md` (overwritten in place)
**Date:** 2026-08-07

## What this attempt was

**A restyle, not a rewrite.** Attempt 1 passed `fin-audit`. The creator then picked style E for
both cuts after a listening test and changed this cut's voice to Amrut Deshmukh
(`run.json.style_decision`, 2026-08-07). Facts, chapter boundaries, beat order, the rung ladder
and every number are attempt 1's, unchanged. **Only the register changed** — plus the two line
counts the creator-approved reference itself dictates.

## What was read, in the ordered sequence the brief gave

1. `vault/CLAUDE.md` (first, per contract)
2. `run.json` — `style_decision`, all seven `constraints`, `hook_gate_hi`, `hook_gate_en`,
   `rate_key_en_followup`, `budget`, `chapters.hi`, `owed`
3. `studio/voice-tests/passive-income-number/style-E-teacher-curiosity.txt` — **chapters 1 and
   2 taken verbatim, not one character altered**; chapters 3–7 restyled to match
4. `script-en.md` (the finished style-E en cut) — **register model only, never a source**
5. `script-hi.md` attempt 1 — facts, structure, chapter boundaries, rung ladder, cues
6. `facts-staging.md` — every number still traces here; **nothing new introduced**
7. `tools/format.json` (cuts.hi, tiers.medium, scene, chapter_design, layout, tts) ·
   `knowledge/video-studies/passive-income-number.md` · `knowledge/niches/india-finance-market.md`
   · `skills/long_form_scripting.md` · `logs/fin-script-hi-1.md` · `logs/fin-script-en-2.md`

`haryanvi-hindi-script-style.md` was **not** read — retired for finance by the 2026-07-28
creator decision, and the contract names the same date.

## Output

- **81 lines / 7 chapters / 5,908 chars.** Estimated runtime **518.2 s (8:38)** against the
  510 s target = **+1.6%**.
- Chapters 1+2 = **21 lines / 1,545 chars** (the approved style-E draft, verbatim).
  Chapters 3–7 = **60 lines / 4,363 chars** (restyled).
- Line count moved 78 → 81 for two reasons only: the approved reference is 8+13 where style A
  was 7+12 (+2), and the stepped arithmetic splits one compressed sum line into two on the
  rung-three block (+1, in ch4). Chapter boundaries and the five-rung ladder are untouched.
- Per-scene timing table included (chars → est s at 13.03 c/s, +0.8 s lead-in/tail per line),
  with the archetype per scene.

## The budget — the SPEECH formula, as the brief instructed

```
(510 − lines × (lead_in + tail)) × chars_per_second
(510 − 81 × 0.8) × 13.03 = 445.2 × 13.03 = 5,801 chars
```

Draft is **5,908 = +1.8% over the char budget, +1.6% over the runtime target.** `510 × 13.03 =
6,645` was **not** used; at 81 lines it would have run 575 s, **12.7% long**. The script states
the formula, the wrong figure and why, so the next stage cannot re-derive the bad one.

## The rate key — first evidence on Amrut, and it holds

The creator-approved reference read (chapters 1+2, Amrut, **118.0 s** of audio) carries **1,545
chars** by this stage's count → **≈13.09 c/s flat**, i.e. **within ~0.5% of the 13.03 key**, on
the new voice and on this exact register. So **13.03 STANDS and nothing was re-padded.** A
register note for fin-voice is carried in the script, the way attempt 2 of the en script did:
re-measure off the full 81-clip batch, correct `format.json` with the measurement beside it,
and **watch the SHAPE of the drift** — one-sided means a wrong key, two-sided means a right one.
Caveats stated in the note: one sample, hand-counted (±1%), and a continuous read, so per-line
clip boundaries will add their own onset and decay. `rate_key_en_followup` says style E ran
~1.5% pause-heavier than the en key predicted; the same mechanic should be expected here.

## ⚠ The hook gate — the brief's target was not met literally, and here is the trade

`hook_gate_hi` records style A's **number-naming clause at 14.9–15.1 s with zero margin** and
names it the first thing to re-test. The brief asked for the naming clause **well inside 15 s**.
**With chapters 1–2 taken verbatim that is arithmetically impossible:** lines 1.1–1.4 are 253
chars, so 1.5 — the naming clause — cannot open before ≈22.9 s. The only way to buy it is to cut
creator-approved copy.

What style E does instead is **split the two objects style A had fused**:

| | style A | style E |
|---|---|---|
| the payoff promise (money arrives, before noon, in your account) | fused into 1.4 | **1.3, opens ≈10.4 s, closes ≈14.7 s** |
| the number, named and withheld | 1.4, measured 14.9–15.1 s | 1.5, ≈22.9 s |

**The en cut's gate was measured on exactly this object, not on its naming clause.**
`hook_gate_en.measured_onset_seconds` 9.571 is *"money is deposited into your account"* (en 1.3);
en's naming clause sits at ≈20 s and was never the gate. So the hi cut now matches the en cut's
shape, and the promise gains **4.6 s of onset margin where style A had none** — the improvement
the brief asked for, on the object the gate is actually measured on.

**Recorded rather than swallowed:** the promise *closes* only ~0.3 s inside 15 s, so this is
owed as a measurement. Build handoff item 6 tells fin-voice to run `silencedetect` on **clip
1.3, not 1.5**, and to overwrite the style-A `hook_gate_hi` entry with both numbers. The flat
model that produced 10.4 s predicted the en cut's onset at 8.9 s against a measured 8.7 s, so it
is good to ~0.2 s — but it is still a model. If the creator wants the naming clause itself
inside 15 s, that is a change to the approved chapter-1 copy and belongs in the voice-test file.

## The four style-E moves, and where each lives

1. **What-if open** (1.1–1.4): the phone's silence is the promise, its single buzz the payoff.
2. **Signposts — 12 across 81 lines**, all imperatives so no first person enters:
   *यहाँ ध्यान दीजिए* (1.4, 3.6, 5.13, 6.11, 7.4) · *इसे ऐसे समझिए* (2.3, 5.4) ·
   *हिसाब सामने कीजिए* (2.9, 3.2, 4.2, 5.10, 6.6) · *अब देखिए कि … क्या आता है* (2.11, 3.4, 4.4,
   6.3, 6.12) · *यह मानिए* (2.13) · *वापस उसी टंकी पर चलिए* (4.7).
3. **The tank pays off twice.** 2.3–2.4 plant it (one tap in = SIP, one tap out = SWP).
   **4.7–4.8 is the first callback** — the money comes out of *your own* tank, which is why the
   outgoing tap is kept narrow; this converts attempt 1's honesty beat from a new idea into a
   return. **5.4–5.5 is the second**, and because 5.6 lands at **4:43** the callback is what
   **opens the 55–65% mid-video drop zone** — the strongest available form of "never a flat
   transition". Style A's water-tank images at 4.6/5.4/5.5 were already there; style E just
   names the analogy up front so they read as one object instead of three unrelated stills.
4. **Stepped arithmetic.** Every rung is corpus-and-rate → yearly → monthly, on separate lines:
   2.8/2.9/2.10 · 3.1/3.2/3.3 · 4.1/4.2/4.3 · 6.5/6.6/6.7. Rung four (6.2) stays compressed
   because chapter 6 has to carry the hero as well and the method is established by then.

## The accuracy trap style E created here, and how it was closed

The stepped arithmetic **manufactures a line whose figure has no rate in its own sentence** —
the monthly line. In the creator-approved chapter 2 that is 2.10, and it cannot be edited. For
every line this stage wrote, the rate was **put back into the VO of the monthly line**: 3.3 and
4.3 say «उसी तीन परसेंट पर», 6.7 says «तीन परसेंट पर». That is +51 chars spent deliberately.

The script carries a **line-by-line rate table (29 rows)** so `fin-audit` can check one at a
time. **Four lines carry a figure whose rate is not spoken in the same sentence — 2.10, 2.11,
2.12 (all creator-approved verbatim) and the "what X buys" shape at 3.4 / 4.4 / 4.5 / 6.3.** In
all of them the rate is in the frame with an `ILLUSTRATIVE` marker and is spoken in the
immediately preceding clip. **fin-audit must rule** on whether a preceding-clip rate satisfies
"the same VO breath" for the verbatim three; if it does not, the fix is a change to the approved
copy, not a silent edit here. Flagged rather than papered over.

## Judgement calls worth flagging

1. **One beat was cut to hold the line budget** — attempt 1's 6.4, *"the amount that leaves
   first each month is no longer leaving your pocket"*. No fact left with it; 6.3 names the bill
   and 7.6 carries the ownership close. It is the only beat dropped from the whole cut.
2. **Line 2.4 is 107 chars → a 9.01 s scene, 0.01 s over `max_scene_seconds`.** Creator-approved
   verbatim and the line that plants the two taps, so not cut. **Build handoff item 7 requires
   TWO `data-framings`** on that scene — the identical exception, for the identical reason, that
   the en cut carries on its own tank line.
3. **Ch5 grew to 17 lines and ch6 to 16** with the same beat count as attempt 1; ch4 grew to 10
   because rung three's arithmetic is now stepped. Every chapter boundary is unchanged.

## Contract compliance

- **Currency purity, grep-verified across the WHOLE file:** the other cut's glyph occurs
  **zero** times — prose, cue text, foots, claim IDs and this log included. Commentary says
  "the rupee's counterpart glyph". PART C of the staging file contributed nothing.
- **The banned payout word: zero occurrences in any form** — English, inline English, and the
  Devanagari transliterations, grep-checked case-insensitively. The live trap is closed at the
  root: the index's total-return measure is **never explained, named or abbreviated anywhere**,
  so no line can force the word. 6.16 quotes only «क़रीब बारह परसेंट».
- **`script-en.md` was read for register, not content.** No US figure, institution, bill or
  photograph crossed over; no conversion, no shared axis, no "which is about".
- **81 line keys verified by grep.** **Zero digits — Latin or Devanagari — in any VO line**
  (the only digit-bearing `>` lines in the file are guard blockquotes). On-screen numerals carry
  the exact figures with `en-IN` grouping.
- **Persona.** No host persona, no first-person expertise; **मैं** and **हम** appear in no VO
  line (the single occurrence in the file is the rule statement itself, in prose). No fund, AMC,
  bank, app or platform named. The post-office scheme, 7.4% and 7.1% appear as published price
  evidence and the frames say so. Second person throughout.
- **No age anywhere in the cut**, narrative or implied. 6.11 states the refusal on the record.
- **Font subset obeyed** in every on-screen string: `TO` not an arrow, `AT`/`IS` not an equals,
  `DIVIDED BY` not a solidus, `·` as separator, `12%` not a tilde, **no question mark on screen**
  (5.2's line is set as a statement for exactly that reason).
- **≈₹5,550, not ₹5,500** — PART E's rounding correction, pinned in handoff item 9.

## ⚠ pipeline_check was NOT run — no Bash in this context

The brief's closing command
`python3 tools/pipeline_check.py check script --slug passive-income-number --cut hi --tier medium`
**could not be executed**: this stage has no shell. **The orchestrator must run it.** What
`check_script` asserts (read from `tools/pipeline_check.py:133`) was verified by hand instead:

| assertion | status |
|---|---|
| `script-hi.md` exists | ✅ written |
| `len(text) >= 500` bytes | ✅ ~40 KB |
| `cuts.hi.forbidden_currency` absent from the file | ✅ grep returns zero |

So the check is expected to pass, but that is a prediction, not a result. Run it.

## Owed / risks for the next stage

1. **`fin-audit-hi` must run in full.** `audit-hi.md` is attempt 1's and is stale — 81 lines
   against 78, new numbering from 1.5 onward, chapters 1–2 entirely new prose. Its first job is
   the rate table above, specifically the four verbatim lines.
2. **`fin-voice-hi` must run: 81 calls, all new.** The 78 attempt-1 clips are dead **twice
   over** — wrong voice AND wrong script — so nothing resumes off a sidecar.
   `budget.elevenlabs_calls` reads 209 against a 350 ceiling → **290 after this run**. Bump the
   counter; it has already been missed once on this slug.
3. **`fin-storyboard-hi` must run.** Line numbering shifted everywhere, and the **tank is a new
   recurring subject needing six distinct frames** (2.3, 2.4, 4.7, 4.8, 5.4, 5.5).
4. **⚠ Every `sNN` in `run.json.chapters.hi` is now wrong.** Under style E ch1 is s1–s8 and ch2
   is s9–s21. Handoff item 11 re-maps the recorded blockers **by subject**, and records that
   `_carry_forward_from_ch1_assets` is **partly void**: style E's chapter 1 has no chai glass and
   no window, so 7.7's callback now rhymes with the **1.3 kitchen counter and its steel glass**;
   and because 1.8 uses a stamp rather than a balance scale, 3.7's brass weights no longer risk
   reading as a reuse — though they must still be visibly ON the balance.
5. **The comma defect recurs on every lakh/crore rung** (2.8, 3.1, 3.7, 4.1, 4.10, 6.1, 6.5,
   6.12, 6.13, 7.3, 7.6). It was fixed system-side; verify the fix holds before judging any
   chapter.
6. **The visual half of the study is still MISSING, not faked** — no keyframes, no hook frames,
   no on-screen-text read, no LOW autopsy. `study.py --ids JiuVKaO2a6c Jn3N9OzSY1c` once cookies
   exist would answer the question that is literally this cut's binding constraint: how a corpus
   number is shown on screen with its rate.
7. **vidIQ: 13 credits remain** against a ~35-credit close-out packaging budget. The three title
   options are unverified candidates, keyword-front-loaded so a title lock can be deferred
   without touching the script.
