---
summary: US/English script for «The Never Too Late Guide to Financial Freedom After 50». LONG tier, per-line chapter architecture — 123 single-sentence VO lines across 7 chapters, 12,287 VO chars ≈ 13:18 at the 17.57 c/s Brian rate with 0.8 s per-line padding, against the run's 746 s target (+6.9%, inside the 10% tolerance). This is a REFORMAT of the creator's finished draft (source-draft.md), not an authored script: every sentence is the creator's except three compliance inserts, two forced factual corrections, and one line replaced by creator ruling 2026-08-15, all listed below. US/$ only — no second market exists for this topic and none was consulted.
updated: 2026-08-15
source: vault/videos/financial-freedom-after-50/source-draft.md (creator, verbatim wording) · creator rulings 2026-08-15 (line 1.8 replacement, hoist approved) · facts-staging.md §1-§5 · run.json constraints · vault/claims/* (eleven claim notes) · knowledge/us-english-script-style.md · knowledge/fact-integrity.md §1/§3/§6 · skills/long_form_scripting.md · workflows/voiceover-tts.md Rule 0 · tools/format/fin-script.json
stage: fin-script, cut en, attempt 2 — creator-ruled amendment to the attempt-1 reformat (mark script PASSED at attempt 1)
---

# «The Never Too Late Guide to Financial Freedom After 50» — US / English (LONG, per-line chapters)

**Studio project (to build):** `studio/videos/financial-freedom-after-50-en`
**Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0.
**Architecture:** `per-line-chapters` (`fin-script.json tiers.long`). **None of the 9-segment
SHORT constants apply.** One VO line = one TTS clip = one scene = one exact timeline anchor.
**On-screen text, title and description:** English. **Currency: $ only.**

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only thing
> that goes to TTS. Everything in backticks is a production cue and is never spoken.
> **Slice these strings — never retype them.**

> **Engine rule.** Digits are **spelled out in every VO line** (bare Latin digits are a
> coin-flip reading in ElevenLabs), and so are initialisms — the VO says "four oh one k",
> "I.R.A.", "H.S.A.", "R.M.D.s", "T.S.P."; the **screen** carries `401(k)`, `IRA`, `HSA`,
> `RMD`, `TSP` and the exact figures with US comma grouping.

> **Cues name what the frame must SHOW, never a layout.** No archetype letter, no ground,
> no plate, no modifier appears in this file — `fin-storyboard` owns those and will assign
> them. A cue here says: the object, the comparison, and the number that has to be legible.

> **Persona rules (YouTube 2026 AI carve-out).** No claimed credentials, no
> "as a financial advisor", no fund/bank/card/security named as a recommendation. Products
> and platforms appear only as evidence of a rule or a price. **There is no first-person
> expertise claim anywhere in this cut** — the draft's "fifteen years in the trenches" line
> was replaced by creator ruling on 2026-08-15 (see §D below). The VO uses "I" only as the
> narrator of the video itself ("In this video, I'm giving you…"), never as a practitioner.

> **Photography rule.** Where people appear at all, they read **50 and older** and the
> frame is unmistakably American. Sweep every photo for non-US currency, signage, plugs and
> vehicles, and for stock that skews 25–35 — a thirty-year-old's hand under a Social
> Security card is the same defect class as a non-US banknote in a US cut.

---

## What this stage did to the creator's draft — the complete list

`run.json → constraints.creator_wording_is_source_of_truth` permits exactly two edits:
factual corrections forced by evidence, and splitting a sentence too long for one VO line.
**Everything below is either one of those two, or a change the creator has since ruled on
directly.** Nothing else in the draft was touched: no rewritten voice, no new examples, no
resequenced argument, no trimmed sentences. **Nothing in this section is open.**

### A. Forced factual corrections (2) — both required by `facts-staging.md`

| # | Draft said | Now says | Why |
|---|---|---|---|
| 1 | "That's a guaranteed, inflation-adjusted **return from the government** that is simply impossible to find anywhere else." | **5.16 + 5.17:** "That's a permanent, inflation-adjusted increase written into the benefit formula." / "It is not a market return, and not something you have to earn by taking risk." | `facts-staging §3.1` + `run.json → no_return_promise`, which names this exact figure. The delayed retirement credit is a statutory benefit-formula adjustment, not a return. Wording is the one `facts-staging` supplied, so the correction is sourced, not invented. |
| 2 | "**The number one financial fear for retirees is** healthcare costs, and for good reason." | **4.4:** "Healthcare costs are a real risk to the plan, and for good reason." | `facts-staging §2` — the #1 ranking is an **unsourced superlative**; the survey houses that publish ranked fear lists (EBRI, Gallup) are not on the `fact-integrity §1` whitelist. Option (b) was taken over option (a) because option (a) ("the fear I hear most") is a first-person expertise claim. The consequence the sentence was carrying survives intact. |

### B. Sentence splits forced by the line ceiling (14)

The ceiling is **144 characters**: at 17.57 c/s, `scene.max_scene_seconds` 9.0 minus 0.8 s of
padding = 8.2 s of VO = 144 chars. Fourteen draft sentences ran past it and were split at
their own comma or clause boundary, with the minimum connective needed to make each half a
sentence: 1.9/1.10 · 2.12/2.13 · 3.9→3.10 · 3.11/3.12 · 3.13/3.14 · 3.23/3.24 · 4.5/4.6 ·
4.6/4.7 · 4.15/4.16 · 5.14/5.15 · 5.18/5.19 · 6.11 · 6.12/6.13 · 6.15/6.16. **No split
dropped a word or an idea.** Conversely, twenty-three pairs of short adjacent draft
sentences were joined into one line where they are one breath (`Rule 0`: a line is one
sentence *or clause*, ~2–8 s) — this is what holds the scene average at 6.49 s and the clip
count under `budget.max_elevenlabs_calls`.

**One line exceeds the ceiling deliberately: 1.8, at 152 chars.** It is the creator's own
ruled replacement text and is not cut. See its cue for the required two-framing treatment.

### C. Compliance inserts — three, each flagged in place

1. **A spoken disclaimer was inserted (lines 3.4–3.5, 196 chars).** `fact_gate`
   requires the disclaimer in **all four** placements and the draft has none. It sits at
   **3:16**, twenty-four seconds before the first dollar figure at 3:40, which satisfies
   "spoken, before any figure appears".
2. **A physical CTA action was inserted (lines 7.10–7.12, 257 chars).**
   `us-english-script-style` §"Script architecture" makes the CTA **one physical action,
   doable today, under five minutes, needing nothing they lack** — mandatory, and the draft's
   only CTA is "watch the next video". The inserted action is *log in, find your contribution
   rate, write it down*, which is the one act that Step 2 is about and needs no branch visit,
   no form and no phone call. The draft's next-video push is untouched and still closes the
   video.
3. **A plain subscribe ask was folded into 7.15** (+61 chars), once, at the end, per the CTA
   rule in `us-english-script-style`.

### D. Creator rulings — both resolved 2026-08-15, neither open

1. **Line 1.8, the "fifteen years in the trenches" claim: REPLACED.** The draft read *"For
   the past fifteen years, I've been in the trenches with people just like you, folks in their
   fifties and sixties who felt hopelessly behind."* followed by *"And I've seen them build
   futures they are excited about using the exact roadmap I'm about to share with you."*
   Attempt 1 carried both verbatim and raised the first as a persona flag: it is a first-person
   experience claim in a YMYL finance video, and the standing persona rule bans first-person
   expertise. **The creator confirmed on 2026-08-15 that it is not a literal biographical
   claim and ruled REPLACE.** The two lines are now one:

   > *"People in their fifties and sixties who felt hopelessly behind have been building
   > futures they are excited about, using the exact roadmap in this video."*

   This supersedes `run.json → constraints.no_advice_framing`'s intake instruction to keep the
   sentence; the constraint is being updated to match and its old wording is **not** binding.
   Effect: chapter 1 drops from 12 lines to 11, the file from 124 to 123, and every downstream
   id, count and timing in this file is recomputed below. **No credential claim of any kind
   remains anywhere in the cut.**
2. **The hook-gate hoist: KEPT, and now CREATOR-APPROVED.** *"In this video, I'm giving you a
   simple five-step game plan that proves it's never too late."* was the draft's third
   paragraph and is now **line 1.3**, moved verbatim, ~45 seconds earlier.
   **Why it was moved:** `script.hook_gate_seconds` = **15**, and the gate is on the payoff
   PROMISE. In the draft's order that sentence starts at **≈55 s** — the gate fails by forty
   seconds. Hoisted, it starts at **11.2 s** on the flat model and **≈12.5 s** with
   `tts.pause_seconds` loaded; it clears on *both*, which matters because the two models
   bracketed reality by 4.6 s on `passive-income-number`. Zero words changed; the paragraph it
   left still reads, because "We'll walk through how to…" is a complete opening (now 1.9).
   **Creator-approved 2026-08-15 — this is authorized structure, not a deviation.
   `fin-audit` should not re-litigate it as an unpermitted structure change.**

---

## Title options (English)

1. **The 5-Step Retirement Catch-Up Plan For Anyone Over 50 (2026 Limits)**
   *(recommended — keyword front-loaded on the search phrase this audience types, the age in
   the first five words, and the parenthetical promises the dated figures the video actually
   shows. Delivers exactly what the script delivers.)*
2. Behind On Retirement At 55? Here Is What 2026 Actually Lets You Save
3. Over 50 With Not Enough Saved: The Catch-Up Contributions Most People Miss

**Not used, and why:** any title with "never too late" alone (no keyword, no specificity),
and anything implying a return, a guarantee or a number the viewer will hit.

---

## Chapters (ship as YouTube chapters)

| # | Chapter | starts | % | lines | chars |
|---|---|---|---|---|---|
| 1 | Feeling behind is a feeling, not a fact | 0:00 | 0.0% | 11 | 1,058 |
| 2 | Step one — stabilize and stop the leaks | 1:09 | 8.6% | 17 | 1,678 |
| 3 | Step two — your catch-up years, and the 2026 numbers | 2:58 | 22.3% | 26 | 2,633 |
| 4 | Step three — protect the base you have built | 5:49 | 43.7% | 18 | 1,731 |
| 5 | Step four — income flexibility, and when to claim | 7:42 | 57.9% | 19 | 1,926 |
| 6 | Step five — the deliberate transition | 9:46 | 73.5% | 16 | 1,777 |
| 7 | The roadmap, and today's one job | 11:40 | 87.8% | 16 | 1,484 |

---

## Timing budget

Rate = **17.57 chars/s** (`fin-script.json cuts.en.chars_per_second`). LONG charges
**0.25 s lead-in + 0.55 s tail per line** (`tiers.long`) = **0.8 × 123 = 98.4 s** of
inter-line padding, which is **not audio**.

Target is **746 s**, the run's overridden LONG target (`run.json.target_seconds`), not the
600 s floor — `tiers._tier_seconds_note` says `min_seconds` is a floor, and `notes.md`
records the creator-approved override with its arithmetic. Budget, computed from
`script.char_budget_formula` with the padding subtracted first, per
`script.word_budget_formula`:

```
chars = (target_seconds − lines × (lead_in + tail)) × chars_per_second
      = (746 − 123 × 0.8) × 17.57
      = 647.6 × 17.57
      = 11,378 chars   (tolerance ±10% → 10,240 … 12,516)
```

**This draft is 12,287 VO chars = +8.0% of budget**, and lands at **797.7 s (13:18) against
the 746 s target, +6.9%** — inside `script.length_tolerance_pct`. It is deliberately on the
high side of the band: the run target was itself derived from the draft's natural length, and
spelling the digits out for TTS ("twenty-four thousand five hundred dollars" for `$24,500`)
adds roughly 430 chars that the draft's own char count never carried.

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 11 | 1,058 | 60.2 s | 8.8 s | 69.0 s | 0:00 |
| 2 | 17 | 1,678 | 95.5 s | 13.6 s | 109.1 s | 1:09 |
| 3 | 26 | 2,633 | 149.9 s | 20.8 s | 170.7 s | 2:58 |
| 4 | 18 | 1,731 | 98.5 s | 14.4 s | 112.9 s | 5:49 |
| 5 | 19 | 1,926 | 109.6 s | 15.2 s | 124.8 s | 7:42 |
| 6 | 16 | 1,777 | 101.1 s | 12.8 s | 113.9 s | 9:46 |
| 7 | 16 | 1,484 | 84.5 s | 12.8 s | 97.3 s | 11:40 |
| | **123** | **12,287** | **699.3 s** | **98.4 s** | **797.7 s** | |

**Pace:** 797.7 / 123 = **6.49 s average scene** against `scene.target_scene_seconds` 6.5.
**Longest line 152 chars (1.8) → 8.65 s + 0.8 = 9.45 s**, over `max_scene_seconds` 9.0 —
deliberate, creator-ruled text, and its cue carries the mandatory two-framing fix. Longest
line after that is 143 chars → 8.94 s, under the ceiling.
**Shortest line 43 chars → 2.4 s**, well over `tts.min_clip_seconds` 1.0 — no line is short
enough to trip the truncation check.
**Clip count 123 against `budget.max_elevenlabs_calls` 154** — 31 re-rolls of margin.

⚠ **Chapter start times above are modelled, not measured.** Regenerate them from the ffprobe
durations of the real clips before they ship as YouTube chapters; `tts.pause_seconds` will
push everything later than this table by a few seconds per chapter.

---

## Where the retention beats land

- **Payoff promise: line 1.3, starting 11.2 s** (flat) / **≈12.5 s** (pause-loaded), inside
  `script.hook_gate_seconds` 15 on both models. Unaffected by the 1.8 replacement, which sits
  five lines later. **Measure it on the rendered clip with silencedetect and record
  `hook_gate_en` in run.json** — this number is a model and models have been 4.6 s apart on
  this exact question before.
- **No greeting, no channel name, no "in today's video"** — 1.1 opens on the viewer's own
  question and the first four lines are the pain-mirror the study logged as a working type.
- **First dollar figure: 3.8 at 3:40**, twenty-four seconds after the spoken disclaimer at
  3:16. The on-screen lower-third disclaimer fires on this same frame (`fact_gate
  _disclaimer_note`: onscreen = the FIRST dollar figure).
- **Nine IRS figures land inside one 2.5-minute block, 3:40–5:14.** This is the structural
  risk the study named: the as-of treatment has to survive nine consecutive reveals for an
  audience that will act on them. Every one of the nine carries its own agency + date card;
  none inherits one from the card before it.
- **Screenshot-the-source moment: 3.8, held 3+ seconds** on the IRS COLA limits page, which
  shows 2026 beside 2025 in one row (`facts-staging §1`, named as the best screen-record
  target). This is the video's `fact-integrity §4` obligation and it is not optional.
- **Mid-video drop zone (55–65% = 7:19–8:39) opens on Chapter 5 at 7:42**, and 5.1 opens it
  on a reframe with tension in it — *the most powerful lever is not saving more* — never a
  flat "now let's talk about".
- **The ~70% reward beat is 5.14 at 9:12 = 69.2%**: the twenty-four to thirty-two percent
  figure, the strongest claim in the video, in the exact place the prior beat maps put it.
  5.13 (the eight percent a year) sets it up at 9:03 = 68.1%.
- **One CTA, terminal, at 7.10–7.12 (12:38 = 95.0%).** Zero mid-roll CTA — three prior finance
  cuts converged on that and the higher-reach twin in `passive-income-number` carried none at
  all.
- **The close returns to the opening claim** (7.7 at 12:19: "it's a feeling, not a fact")
  before the action, so the last emotional beat is the hook paid off, not a list.

---

# THE SCRIPT

---

## Chapter 1 — Feeling behind is a feeling, not a fact

*Pain-mirror cold open, second person, no number and no greeting. The promise is hoisted to
1.3 to clear the fifteen-second gate (creator-approved 2026-08-15); everything else is the
draft's order. 1.8 is the creator's ruled replacement for the draft's "fifteen years in the
trenches" pair.*

**1.1**
> Are you over fifty and worried the ship has sailed on a comfortable retirement?

`[img: a man in his early sixties at a kitchen table in a US home, morning light, a bank statement face-up in front of him, looking at it rather than at camera | head: OVER FIFTY? | stmt: The ship has not sailed. | no figure on this frame]`

**1.2**
> Do you ever look at your savings and get that sinking feeling of, I'm just too far behind?

`[img: a laptop on the same table showing a blurred retirement account balance page, figures illegible, a reading-glasses case beside it | head: TOO FAR BEHIND? | stmt: That feeling has a name, and it is not a number.]`

**1.3**
> In this video, I'm giving you a simple five-step game plan that proves it's never too late.

`[img: five plain numbered index cards laid in a row on a wooden table, top-down, unwritten | head: FIVE STEPS | stmt: A five-step plan, in order. | PAYOFF PROMISE — must START by 15.0 s (script.hook_gate_seconds); modelled 11.2 s flat / 12.5 s pause-loaded. MEASURE ON THE RENDER. Position creator-approved 2026-08-15.]`

**1.4**
> Believe me, you are not alone. But I'm here to tell you that feeling, while common, is a myth.

`[img: a quiet US suburban street at dawn, several houses, no people | head: NOT ALONE | stmt: Common — and still a myth.]`

**1.5**
> The truth? It's not about starting over from scratch. It's about making a few smart, strategic moves in the right order.

`[img: a hand placing the third card in a row of five on the table, the earlier two already down | head: NOT FROM SCRATCH | stmt: A few moves. In the right order.]`

**1.6**
> Forget the idea of needing a magic bullet or suddenly becoming a Wall Street wizard.

`[img: a closed newspaper business section on a table, the market page folded under, a coffee mug on top of it | head: NO MAGIC BULLET | stmt: No stock picking. No wizardry.]`

**1.7**
> This is about taking back control with a straightforward, proven system.

`[img: a plain ruled notebook open to a blank page beside a pen, hard side light | head: TAKE BACK CONTROL | stmt: A system, not a bet.]`

**1.8**
> People in their fifties and sixties who felt hopelessly behind have been building futures they are excited about, using the exact roadmap in this video.

`[img: an older couple walking away from camera on a US beach boardwalk, unhurried, no faces | head: THE SAME ROADMAP | stmt: Felt behind. Built anyway. | CREATOR-RULED REPLACEMENT 2026-08-15 — replaces the draft's "fifteen years in the trenches" line and the one after it. No credential claim remains. | ⚠ 152 chars → 8.65 s VO + 0.8 = 9.45 s, past scene.max_scene_seconds 9.0. THIS SCENE MUST CARRY TWO FRAMINGS — wide on the boardwalk, then a push to the couple — so no single framing holds past 9.0 s. Same mechanism as a continuous zoom, applied inside one scene; precedent is passive-income-number line 2.2 (155 chars), which shipped this way.]`

**1.9**
> We'll walk through how to stabilize your finances, and crank up your most powerful savings years.

`[img: cards one and two of the five now lettered STABILIZE and MAXIMIZE, the other three still blank | head: STEPS ONE AND TWO | stmt: 1 Stabilize · 2 Maximize | reveal the two cards in sequence]`

**1.10**
> Then build a fortress around what you've earned, create new income options, and finally, design a confident transition into retirement.

`[img: cards three, four and five now lettered PROTECT, INCOME, TRANSITION, completing the row of five | head: THREE, FOUR, FIVE | stmt: 3 Protect · 4 Income · 5 Transition | cascade 3 items]`

**1.11**
> Let's start building that future, right now.

`[img: a hand squaring up the row of five cards on the table | head: START HERE | stmt: Step one.]`

---

## Chapter 2 — Step one: stabilize and stop the leaks

*No figure in this chapter, by design. The draft leads with mechanism, and the one number
available here — credit card interest north of twenty percent, `facts-staging` row 11 — is
**deliberately not spoken**: the draft says "high-interest debt" and the row is HARD on the
shape and SOFT on every decimal. It appears on ONE card, as a shape, with its agency and
month, and never as a decimal or a period label.*

**2.1**
> First things first: our roadmap doesn't start with some risky investment or chasing a hot stock. It starts by building a rock-solid foundation.

`[img: a poured concrete foundation slab on a US residential lot, rebar visible, no building on it yet | head: FOUNDATION FIRST | stmt: Not a hot stock. A foundation.]`

**2.2**
> You can't build a skyscraper on shaky ground, right? Your finances are no different.

`[img: a steel high-rise frame under construction seen from street level in a US city | head: SHAKY GROUND | stmt: The building is only as good as what is under it.]`

**2.3**
> This first step is all about getting stable. Think of your financial life like a bucket.

`[img: a galvanized bucket on a workbench, plain background | head: THE BUCKET | stmt: Step one: get stable.]`

**2.4**
> It doesn't matter how much water you pour in if there are holes in the bottom. Our first job is to plug those holes.

`[img: the same bucket, water running from a hose into it and visibly draining out of two holes near the base | head: TWO HOLES | stmt: Pouring faster does not fix a leak. | the leak must be legible, not implied]`

**2.5**
> For most people, the two biggest leaks are high-interest debt and not having a real emergency fund.

`[img: the bucket again, the two holes now labelled on the frame | head: THE TWO LEAKS | stmt: 1 High-interest debt · 2 No emergency fund | cascade 2 items]`

**2.6**
> High-interest debt, especially from credit cards, is a silent wealth-killer. It's actively working against you, twenty-four seven.

`[img: a stack of unopened credit card statements on a US kitchen counter, envelopes only, no issuer marks or logos visible | head: WORKING AGAINST YOU | stmt: Credit card interest: north of 20% a year | src: Federal Reserve G.19 · as of August 2026 | label: VERIFIED | ⚠ SHAPE ONLY — never a decimal and never a period label on this card (facts-staging row 11). "north of 20%" is the whole permitted claim.]`

**2.7**
> That interest is a guaranteed negative return on your money.

`[img: a plain arrow graphic pointing down on a neutral card, no ticker, no market chart | head: NEGATIVE, GUARANTEED | stmt: Interest paid is the one rate you know in advance. | no figure on this frame]`

**2.8**
> So, before you get aggressive with investing, you need a plan to wipe this out.

`[img: a hand writing the word PLAN at the top of a ruled notebook page | head: A PLAN FIRST | stmt: Wipe it out before you go on offense.]`

**2.9**
> List your debts from the highest interest rate to the lowest and attack the one at the top with every spare dollar.

`[img: a handwritten list on a legal pad — four rows, a rate column, the top row circled, amounts illegible | head: HIGHEST RATE FIRST | stmt: Order by rate. Attack the top. | label: OPINION (this is a widely used method, not an agency rule) — no source card]`

**2.10**
> Once it's gone, you roll that entire payment onto the next one.

`[img: the same legal pad with the top row struck through and an arrow drawn to the second row | head: ROLL IT DOWN | stmt: The freed payment goes to the next line.]`

**2.11**
> This creates a debt-crushing snowball that not only clears your slate faster but also delivers a massive psychological win.

`[img: a snowball part-way down a snowy slope in a US winter landscape, its track widening behind it | head: THE SNOWBALL | stmt: Faster payoff, and a win you can feel. | analogy — the frame must show the track, not just the ball]`

**2.12**
> At the same time, you need a cash cushion. A surprise car repair or a leaky roof shouldn't be a catastrophe that sends you deeper into debt.

`[img: a US driveway, hood of a sedan up, an older man looking at the engine | head: THE SURPRISE | stmt: A repair should be an expense, not a catastrophe.]`

**2.13**
> Or, even worse, forces you to raid your retirement accounts.

`[img: a retirement account statement on a table with a pen resting on a withdrawal form, figures illegible | head: THE WORST OPTION | stmt: Never the retirement account.]`

**2.14**
> Your first goal is to build an emergency fund that covers at least three to six months of your essential expenses.

`[img: six identical envelopes in a row on a table, three of them thicker | head: THREE TO SIX MONTHS | stmt: 3–6 months of ESSENTIAL expenses | label: OPINION / CONVENTION — the standard advice, not a statistic. NO agency card, NO source line on this frame (facts-staging §2).]`

**2.15**
> Keep this money in a separate, high-yield savings account, easy to access, but not mixed in with your coffee money.

`[img: two plain unbranded passbook-style folders side by side on a desk, one labelled EVERYDAY and one labelled EMERGENCY | head: KEEP IT SEPARATE | stmt: Separate account. Easy to reach. | ⚠ NO bank name, NO app, NO APY on this frame — a rate dates the video (facts-staging §5)]`

**2.16**
> This fund is your financial shock absorber.

`[img: a cutaway or close view of a car shock absorber on a workbench | head: SHOCK ABSORBER | stmt: It absorbs the hit so the plan does not.]`

**2.17**
> It's what gives you the peace of mind to focus on the next steps without worrying about life's curveballs.

`[img: a woman in her late fifties on a porch in the US, coffee in hand, relaxed, looking out | head: PEACE OF MIND | stmt: Now you can go on offense.]`

---

## Chapter 3 — Step two: your catch-up years, and the 2026 numbers

*The dense chapter. Nine IRS figures in one block. **Every figure card carries its own
agency and its own publication date** — none inherits from the card before it, because the
viewer who screenshots frame six must be able to read that frame alone. The spoken
disclaimer sits at 3.4–3.5, before the first figure.*

**3.1**
> Okay, foundation stable? Now we go on offense. Your fifties and early sixties are often your highest-earning years.

`[img: a US workplace mid-shift — a woman in her fifties at a desk in an open office, no screen text legible | head: ON OFFENSE | stmt: Your highest-earning years are now.]`

**3.2**
> And the government gives you some seriously powerful tools to accelerate your savings.

`[img: the front of an IRS publication on a desk, cover legible, no figures shown yet | head: THE TOOLS EXIST | stmt: Written into the tax code, on purpose.]`

**3.3**
> This is your catch-up phase, and you have to treat it with a sense of urgency.

`[img: a wall calendar in a US kitchen turned to a month, no dates marked | head: THE CATCH-UP PHASE | stmt: A window, not a phase you drift through.]`

**3.4**
> Quick note before the numbers start: this is general financial education, not financial, tax, or legal advice.

`[img: a plain card on a neutral ground, the disclaimer set as the only element | head: BEFORE THE NUMBERS | stmt: General financial education. Not financial, tax, or legal advice. | SPOKEN DISCLAIMER — fact_gate.disclaimer_placements, placement 1 of 4, at 3:16, before the first figure at 3:40]`

**3.5**
> Every figure ahead carries the agency that published it and the date it was published.

`[img: the same plain card, now showing a specimen source line — AGENCY · MONTH YEAR — as the example it describes | head: EVERY FIGURE, SOURCED | stmt: Agency + publication date, on the frame.]`

**3.6**
> The most valuable tool in your arsenal is the catch-up contribution.

`[img: a single form on a desk with the words CATCH-UP CONTRIBUTION legible on it | head: THE CATCH-UP | stmt: The one tool that only exists after fifty.]`

**3.7**
> If you're fifty or older, you're allowed to contribute way more to your retirement accounts.

`[img: two clear jars side by side, the right one visibly taller, both empty | head: AFTER FIFTY | stmt: The ceiling moves up. | no figure yet — the numbers start on the next frame]`

**3.8**
> In twenty twenty-six, the standard four oh one k or four oh three b contribution limit is twenty-four thousand five hundred dollars.

`[img: SCREEN RECORDING of the IRS COLA limits page, the 2026 column beside 2025, the elective deferral row highlighted — irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions | head: 2026 401(k) / 403(b) LIMIT | stmt: $24,500 | src: IRS · November 2025 | label: VERIFIED | ⚠ SCREENSHOT-THE-SOURCE MOMENT — hold this frame 3+ seconds, URL bar legible (fact-integrity §4). FIRST DOLLAR FIGURE → the on-screen lower-third disclaimer fires here (placement 2 of 4). | claim: 401k-elective-deferral-2026]`

**3.9**
> But being fifty or over lets you add an extra eight thousand dollars as a catch-up.

`[img: the same IRS page scrolled to the catch-up row, that row highlighted | head: AGE 50+ CATCH-UP | stmt: + $8,000 | src: IRS · November 2025 | label: VERIFIED | claim: 401k-catchup-age50-2026]`

**3.10**
> That's a total of thirty-two thousand five hundred dollars for the year.

`[img: a two-line sum set as arithmetic — $24,500 + $8,000 — with the total under a rule | head: THE TOTAL | stmt: $24,500 + $8,000 = $32,500 | src: IRS · November 2025 | label: VERIFIED | the addition must be legible as arithmetic, not as a headline]`

**3.11**
> For an I.R.A., the twenty twenty-six limit is seven thousand five hundred dollars, with an extra one thousand one hundred dollar catch-up.

`[img: the IRS newsroom release IR-2025-111 on screen, the IRA paragraph highlighted | head: 2026 IRA LIMIT | stmt: $7,500 + $1,100 catch-up | src: IRS · November 2025 | label: VERIFIED | claim: ira-limit-2026]`

**3.12**
> That's a combined total of eight thousand six hundred dollars across all your Traditional and Roth I.R.A.s.

`[img: the sum set as arithmetic — $7,500 + $1,100 — total under a rule, with the words ACROSS ALL IRAS COMBINED beneath | head: COMBINED, NOT EACH | stmt: $7,500 + $1,100 = $8,600 total | src: IRS · November 2025 | label: VERIFIED | the word COMBINED must be legible — this is the line viewers most often misread]`

**3.13**
> It's important to note these limits apply to most employer plans, like the four oh one k, the four oh three b, and the government's T.S.P.

`[img: three plain labelled tabs in a row — 401(k) · 403(b) · TSP | head: WHICH PLANS | stmt: 401(k) · 403(b) · governmental 457(b) · TSP | cascade 4 items]`

**3.14**
> But other plans, like SIMPLE I.R.A.s, have different rules.

`[img: a fourth tab set apart from the other three, labelled SIMPLE IRA, visibly separated | head: DIFFERENT RULES | stmt: SIMPLE IRA — different limits. Check your plan. | label: VERIFIED (the exclusion is in the same IRS notice) | src: IRS · November 2025]`

**3.15**
> And it gets better: thanks to the SECURE two point oh Act, there's a special super catch-up for those between sixty and sixty-three.

`[img: a US calendar or age band graphic showing 60 · 61 · 62 · 63 as four consecutive years, bracketed | head: AGES 60 TO 63 | stmt: A four-year window. | src: IRS · November 2025 | label: VERIFIED | the four ages must be legible as a bracket, not a list | fin-audit 2026-08-15: the ages 60·61·62·63 are numbers ON SCREEN and had no agency line — fact_gate point 1 requires one on THIS frame, not inherited from 3.16. IRS COLA page: "employees who turn 60, 61, 62 and 63 in a calendar year".]`

**3.16**
> If your plan allows it, your total catch-up for those years is eleven thousand two hundred fifty dollars.

`[img: the IRS newsroom release on screen, the 60–63 paragraph highlighted | head: SUPER CATCH-UP | stmt: $11,250 (if your plan offers it) | src: IRS · November 2025 | label: VERIFIED | claim: 401k-supercatchup-60-63-2026 | ⚠ the words IF YOUR PLAN OFFERS IT are compliance, not decoration — it is plan-optional]`

**3.17**
> That lets you potentially save a grand total of thirty-five thousand seven hundred fifty dollars in your workplace plan for twenty twenty-six.

`[img: the arithmetic — $24,500 + $11,250 — total under a rule, the words WORKPLACE PLAN ONLY beneath | head: THE 60–63 TOTAL | stmt: $24,500 + $11,250 = $35,750 | src: IRS · November 2025 | label: VERIFIED]`

**3.18**
> Every dollar you put away now has an outsized impact. It's like giving your money a final, powerful sprint before the retirement finish line.

`[img: a US high school running track, the final straight, empty lanes, late afternoon light | head: THE FINAL SPRINT | stmt: The last stretch counts double. | analogy frame — no figure]`

**3.19**
> If you're not contributing enough to get your full employer match, you're literally turning down free money.

`[img: a plain benefits-enrollment screen mock with an EMPLOYER MATCH row, the percentage blanked | head: THE MATCH | stmt: An unclaimed match is money you were offered and declined. | label: OPINION on the phrase "free money" — no agency publishes a match rate; NO source card]`

**3.20**
> Start there, then automate a one percent increase to your contribution every few months.

`[img: a contribution-rate field on a plain form, a hand adjusting it up by one | head: ONE PERCENT AT A TIME | stmt: +1% every few months, automatic. | label: OPINION — a method, not a rule; no source card]`

**3.21**
> You probably won't even feel it, but the long-term impact on your nest egg will be massive.

`[img: a bird's nest on a branch with several eggs, US woodland, natural light | head: YOU WON'T FEEL IT | stmt: The paycheck barely moves. The balance does. | ⚠ no projected number, no growth curve, no rate — no_return_promise]`

**3.22**
> One more critical update for twenty twenty-six: there's a new rule for high earners.

`[img: an IRS notice PDF on screen, first page, title legible | head: NEW FOR 2026 | stmt: One rule changed for higher earners.]`

**3.23**
> If your FICA wages from your employer in the previous year were over one hundred fifty thousand dollars,

`[img: a W-2 form on a desk, the Social Security wages box circled, the amount illegible | head: PRIOR-YEAR FICA WAGES | stmt: Over $150,000 in the prior year | src: IRS Notice 2025-67 · November 2025 | label: VERIFIED | claim: roth-catchup-threshold-2026 | the box on the W-2 must be the one the rule actually reads]`

**3.24**
> then any catch-up contributions you make must be made on a Roth, after-tax, basis, assuming your plan has a Roth option.

`[img: two labelled paths from one box — PRE-TAX greyed out, ROTH highlighted | head: CATCH-UP MUST BE ROTH | stmt: Catch-up goes Roth (after-tax) | src: IRS Notice 2025-67 · November 2025 | label: VERIFIED | ⚠ the hedge "assuming your plan has a Roth option" is compliance and stays (facts-staging §3.3) | fin-audit 2026-08-15: src was "IRS · 2026", a bare year — every source line in this cut carries Month Year.]`

**3.25**
> And that one hundred fifty thousand dollar threshold will be indexed for inflation.

`[img: the $150,000 figure on a card with a small upward step beside it and the word INDEXED | head: INDEXED | stmt: $150,000 is the 2025 wage figure governing 2026 — it moves | src: IRS · November 2025 | label: VERIFIED | ⚠ do NOT show a future threshold — none is published]`

**3.26**
> This is a big shift, so check your plan's rules and tweak your strategy.

`[img: a summary plan description booklet on a desk, a hand turning to a tabbed page | head: CHECK YOUR PLAN | stmt: Plan rules decide what you can actually elect.]`

---

## Chapter 4 — Step three: protect the base you have built

*The chapter where the draft's one unsourced superlative lived. It is gone (correction 2).
The long-term-care beat stays **numberless on purpose**: every cost table in circulation
comes from an insurer or an off-whitelist agency (`facts-staging §5`), and "astronomical"
with no figure is the honest form.*

**4.1**
> With your savings engine roaring, it's time to build a fortress around what you have.

`[img: a stone fort wall in the US, low angle, solid and plain | head: BUILD THE FORTRESS | stmt: Now protect what you just built.]`

**4.2**
> A single unexpected disaster, especially a health crisis, can wipe out decades of hard work.

`[img: a US hospital corridor, empty, daylight, no people identifiable | head: ONE EVENT | stmt: Decades of saving, one event.]`

**4.3**
> This step is all about managing risk so your plan doesn't get blown off course.

`[img: a sailboat on open US coastal water heeled hard over in wind | head: OFF COURSE | stmt: Risk management is steering, not fear.]`

**4.4**
> Healthcare costs are a real risk to the plan, and for good reason. Your plan has to account for this.

`[img: a stack of medical billing envelopes on a kitchen counter, no provider names legible | head: HEALTHCARE | stmt: A real risk to the plan. | label: OPINION — no ranked "number one fear" claim, no survey, NO source card. ⚠ Do not restore a ranking to this frame (facts-staging §2).]`

**4.5**
> If you are enrolled in a high-deductible health plan, you may have access to a Health Savings Account, or H.S.A.

`[img: an insurance card and a plan summary on a desk, HIGH DEDUCTIBLE legible on the summary, no insurer name | head: HSA ELIGIBILITY | stmt: High-deductible health plan → HSA eligible | src: IRS Pub 969 | label: VERIFIED]`

**4.6**
> It's one of the most incredible long-term savings tools out there. It's got a triple tax advantage.

`[img: three stacked bands on a plain card, unlabelled, waiting to be filled | head: TRIPLE ADVANTAGE | stmt: Three tax breaks in one account. | label: OPINION on "most incredible"; the three mechanics on the next frame are VERIFIED]`

**4.7**
> Contributions are tax-deductible, the money grows tax-free, and withdrawals for qualified medical expenses are also tax-free.

`[img: the same three bands now labelled | head: THE THREE | stmt: 1 Deduct going in · 2 Grows tax-free · 3 Tax-free for medical | src: IRS Pub 969 · as of January 2026 | label: VERIFIED | cascade 3 items | fin-audit 2026-08-15: chips shortened from 26/17/40 chars to 17/16/22 — layout.max_chip_chars is 22]`

**4.8**
> People fifty-five and older can even make an additional one thousand dollar catch-up contribution.

`[img: IRS Publication 969 on screen, the age-55 catch-up sentence highlighted | head: HSA CATCH-UP, AGE 55+ | stmt: + $1,000 | src: IRS Pub 969 · as of January 2026 | label: VERIFIED | claim: hsa-catchup-age55 | note: fixed by statute, NOT indexed — do not show it rising]`

**4.9**
> An H.S.A. can become your dedicated war chest for medical costs in retirement.

`[img: a plain lockbox on a shelf, closed, a small label reading MEDICAL | head: THE WAR CHEST | stmt: Earmarked, not general savings.]`

**4.10**
> Beyond the H.S.A., you have to review your insurance. I know, it's not the sexiest part of finance, but it is one of the most critical.

`[img: a folder of policy documents on a table, tabs visible, no insurer names | head: REVIEW THE POLICIES | stmt: Dull, and load-bearing.]`

**4.11**
> Do you have enough life insurance to protect your spouse?

`[img: two wedding bands on a nightstand beside a folded policy document | head: LIFE INSURANCE | stmt: Enough for the person left behind? | label: OPINION — "enough" is personal; no figure, no source card]`

**4.12**
> Is your disability insurance solid enough to cover your income during these final, crucial earning years?

`[img: an empty office chair at an occupied US desk, jacket over the back, mid-day | head: DISABILITY COVER | stmt: The years you cannot afford to lose income.]`

**4.13**
> And then there's the elephant in the room: long-term care. The cost of assisted living or in-home care can be astronomical.

`[img: a US assisted-living residence corridor with a handrail, daylight, no people | head: LONG-TERM CARE | stmt: The cost can be astronomical. | ⚠ NO FIGURE ON THIS FRAME AND NONE ANYWHERE IN THIS BEAT. Every circulating cost table is insurer-published or off-whitelist (facts-staging §5). Numberless is the correct form.]`

**4.14**
> Pretending it can't happen to you is not a strategy.

`[img: a plain closed door in a US home hallway | head: NOT A STRATEGY | stmt: Not planning is a plan with one outcome.]`

**4.15**
> It's time to investigate your options, whether that's traditional long-term care insurance or a hybrid life and long-term care policy.

`[img: two labelled document stacks side by side on a table — TRADITIONAL LTC and HYBRID LIFE + LTC | head: TWO OPTIONS | stmt: Traditional LTC · Hybrid life + LTC | ⚠ categories only, never a named insurer or product]`

**4.16**
> Or a plan to self-fund by earmarking specific assets. You have to have a plan before you need one.

`[img: a third stack labelled SELF-FUND beside the other two, a hand setting it down | head: OR SELF-FUND | stmt: A named asset, set aside in advance.]`

**4.17**
> Protecting your base is about shifting from a pure growth mindset to one of wealth preservation.

`[img: a young tree with a stake and a tie in a US yard, the support in focus | head: GROWTH → PRESERVATION | stmt: The job changes from growing to keeping.]`

**4.18**
> You've worked too hard to let one surprise put it all at risk.

`[img: a worn pair of work boots by a US back door | head: TOO HARD FOR THAT | stmt: Protect the work.]`

---

## Chapter 5 — Step four: income flexibility, and when to claim

*The Social Security block, and the ~70% reward beat. Two things are load-bearing here: the
percentages **each carry a full retirement age on the card** (`facts-staging §3.2` — only the
30% and 24% ends are reachable by anyone who can act on this video), and the delayed
retirement credit is described as a **benefit-formula increase, never a return**
(correction 1). The earnings test is deliberately absent: `facts-staging §4` shows the script
is safe without it, and no stage may add a "claim early and keep working" beat without it.*

**5.1**
> For many people over fifty, the most powerful lever you can pull to change your financial future isn't just saving more.

`[img: a long steel lever on a plain machine, a hand on the end of it | head: THE BIGGEST LEVER | stmt: It is not saving more. | opens the mid-video drop zone on a reframe, not a transition]`

**5.2**
> It's earning more, and for longer. This step is all about expanding your horizons and giving yourself options.

`[img: a man in his early sixties in a US workshop, working, unhurried | head: EARN LONGER | stmt: More years of income. More options.]`

**5.3**
> The idea of working longer isn't always popular, but hear me out.

`[img: a plain wall clock in a US office, hands past the hour | head: NOT POPULAR | stmt: Hear the arithmetic first.]`

**5.4**
> Even one or two extra years of income can have a monumental impact. It does three things at once.

`[img: three empty numbered rows on a plain card | head: THREE THINGS AT ONCE | stmt: One or two years does three jobs.]`

**5.5**
> It gives you more time to pour money into your retirement accounts, and it gives your existing investments more time to grow.

`[img: rows one and two of the card now filled | head: ONE AND TWO | stmt: 1 More contributions · 2 More years of growth | ⚠ no rate, no projection, no curve — no_return_promise]`

**5.6**
> And most importantly, it shortens the number of years your nest egg needs to support you.

`[img: row three filled, and a horizontal band beside it visibly shortened at the left end | head: AND THREE | stmt: 3 Fewer years the money has to last | the shortening must be the visual argument]`

**5.7**
> This doesn't mean being chained to a high-stress desk job until you're seventy. This is about creating flexibility.

`[img: an empty corporate cubicle in the US, lights on, nobody in it | head: NOT THAT | stmt: Flexibility, not endurance.]`

**5.8**
> Could you shift to a part-time role? Could you turn a lifetime of experience into a consulting gig?

`[img: a woman in her sixties at a small home desk in the US, laptop open, a notepad beside it, working part of a day | head: TWO ROUTES | stmt: Part-time · Consulting | cascade 2 items]`

**5.9**
> Earning even a little bit of income in early retirement can dramatically reduce the strain on your portfolio.

`[img: the shortened band from 5.6 with a smaller draw arrow beneath it, no figures | head: LESS STRAIN | stmt: Every earned dollar is a dollar not withdrawn. | label: OPINION on "dramatically" — mechanism, no figure, no source card]`

**5.10**
> This flexibility is directly tied to the biggest retirement decision you'll make: when to claim Social Security.

`[img: a Social Security card in a plain document sleeve on a table, number obscured | head: THE BIGGEST DECISION | stmt: When you claim.]`

**5.11**
> You can claim as early as age sixty-two, but that comes with a permanent haircut on your monthly benefit.

`[img: the SSA retirement-age reduction planner page on screen, ssa.gov URL legible | head: CLAIM AT 62 | stmt: A permanent reduction | src: SSA · as of August 2026 | label: VERIFIED | claim: ss-early-claim-reduction-62 | ⚠ ssa.gov 403'd every fetch from the pipeline — this capture must come from a network path that can actually reach ssa.gov (facts-staging §6)]`

**5.12**
> It's a reduction of roughly twenty-five to thirty percent compared to what you'd get at your full retirement age.

`[img: two benefit bars side by side, the 62 bar visibly shorter, no dollar amounts | head: THE REDUCTION | stmt: −30% if FRA is 67 · −25% if FRA is 66 | src: SSA · as of August 2026 | label: VERIFIED | ⚠ the FRA MUST be on this card — it is, in both chips; the birth-year mapping is its own frame at 5.15. (fin-audit 2026-08-15: chips were 59/42 chars, over layout.max_chip_chars 22; shortened without dropping the FRA.) Only the 30% end is reachable by anyone who can act on this video — an FRA of 66 belongs to birth years 1943–1954, who are 72+ in 2026 (facts-staging §3.2).]`

**5.13**
> However, for every year you delay claiming past your full retirement age, up to age seventy, your benefit increases by about eight percent.

`[img: the SSA delayed-retirement-credit planner page on screen, ssa.gov URL legible | head: DELAY PAST FRA | stmt: +8% a year, up to age 70 | src: SSA · as of August 2026 | label: VERIFIED | claim: ss-delayed-retirement-credit | sets up the reward beat on the next line]`

**5.14**
> By waiting until age seventy, you can lock in a monthly check that's twenty-four to thirty-two percent higher than at your full retirement age.

`[img: three benefit bars — 62, full retirement age, 70 — ascending, no dollar amounts, the 70 bar tallest | head: WAITING UNTIL 70 | stmt: +24% if FRA is 67 · +32% if FRA is 66 | src: SSA · as of August 2026 | label: VERIFIED | ⚠ THE ~70% REWARD BEAT (9:12 = 69.2%). Hold it. The FRA belongs on this card for the same reason as 5.12. (fin-audit 2026-08-15: chips were 59/20 chars; shortened to 17/17.)]`

**5.15**
> Exactly how much higher depends on what that full retirement age is.

`[img: a plain two-row card — FRA 67 → +24% · FRA 66 → +32% — with birth-year ranges beside each | head: IT DEPENDS ON YOUR FRA | stmt: FRA 67 (1960+): +24% · FRA 66 (1943–54): +32% | src: SSA · as of August 2026 | label: VERIFIED | this is the frame that carries the birth-year mapping for 5.12 and 5.14 — it must not be cut. (fin-audit 2026-08-15: chips were 26/30 chars; shortened to 20/22.)]`

**5.16**
> That's a permanent, inflation-adjusted increase written into the benefit formula.

`[img: a printed benefit-formula excerpt on a desk, a hand flat on the page | head: WRITTEN INTO THE FORMULA | stmt: Statutory, permanent, inflation-adjusted. | ⚠ FORCED CORRECTION 1 — the draft said "guaranteed return from the government". Never restore that phrasing (run.json no_return_promise, facts-staging §3.1).]`

**5.17**
> It is not a market return, and not something you have to earn by taking risk.

`[img: a plain card with a market chart shape struck through | head: NOT A RETURN | stmt: No market. No risk taken. | no ticker, no index, no fund]`

**5.18**
> Having other sources of income, even part-time, gives you the power to delay Social Security.

`[img: a hand holding a claim form, unsigned, pen down beside it | head: THE POWER TO WAIT | stmt: Other income is what buys the delay.]`

**5.19**
> And to lock in that much larger payment for the rest of your life.

`[img: the tallest of the three bars from 5.14, alone, extending off the right edge of frame | head: FOR LIFE | stmt: The higher check does not expire.]`

---

## Chapter 6 — Step five: the deliberate transition

*The 4% rule appears here and is the one claim in the video with **no primary source and no
agency card**, by design: no whitelisted agency publishes it, it is a 1994 study
(`facts-staging §2`), and the draft's own hedge — "a starting guideline, not gospel" — is
what makes the sentence publishable. **No stage may remove or soften that hedge.***

**6.1**
> Alright, you've stabilized your finances, you're maxing out your savings, you've protected your assets, and you've built income flexibility.

`[img: the row of five cards from Chapter 1, the first four turned face-up | head: FOUR DOWN | stmt: 1 Stabilize · 2 Maximize · 3 Protect · 4 Income | cascade 4 items]`

**6.2**
> The final step is to bring it all together and plan your transition from accumulating wealth to distributing it.

`[img: the fifth card turned face-up, lettered TRANSITION | head: STEP FIVE | stmt: From accumulating to distributing.]`

**6.3**
> Retirement isn't a finish line you stumble across. It's a new phase that requires a whole new playbook.

`[img: a race finish line on a US track with the tape already broken, the track continuing past it | head: NOT A FINISH LINE | stmt: The road keeps going past the tape.]`

**6.4**
> The central question is no longer, how much can I save, but, how much can I safely spend? This means creating a smart withdrawal strategy.

`[img: two questions set on one card, the first struck through | head: THE QUESTION CHANGES | stmt: Not "how much can I save" — "how much can I safely spend"]`

**6.5**
> You may have heard of the four percent rule, but think of it as a starting guideline, not gospel. Your own strategy needs to be more nuanced.

`[img: a 1994 journal article on a desk, plain, no agency seal anywhere in frame | head: THE 4% RULE | stmt: A 1994 study. A starting guideline, not a rule. | label: OPINION / CONVENTION — ⚠ NO AGENCY CARD, NO SOURCE LINE, NEVER the word "verified" on this frame. No whitelisted agency publishes this figure and that absence is the finding (facts-staging §2). The hedge in the VO is load-bearing and must not be softened.]`

**6.6**
> You need a game plan for which accounts to draw from first.

`[img: three labelled account folders in a row on a desk — TAXABLE · TAX-DEFERRED · ROTH | head: WHICH ACCOUNT FIRST | stmt: The order is the strategy.]`

**6.7**
> Do you spend down your taxable brokerage accounts before touching your tax-deferred I.R.A.s and four oh one k plans?

`[img: a hand moving the TAXABLE folder to the front of the row | head: TAXABLE FIRST? | stmt: Taxable → tax-deferred → ? | label: OPINION — sequencing is a planning question, not an agency rule; no source card]`

**6.8**
> Where do your tax-free Roth accounts fit in?

`[img: the ROTH folder held apart from the other two, unplaced | head: AND ROTH? | stmt: The one account with no tax bill on the way out.]`

**6.9**
> Smart coordination here can save you tens, even hundreds, of thousands of dollars in taxes over your retirement.

`[img: the three folders arranged in a deliberate order, a hand squaring them | head: COORDINATION | stmt: Order changes the tax bill. | label: OPINION on the size of the saving — ⚠ NO figure on this frame; "tens, even hundreds of thousands" stays a shape in the VO and never becomes a number on screen]`

**6.10**
> This is also when you have to get smart about Required Minimum Distributions, or R.M.D.s.

`[img: an IRS RMD FAQ page on screen, the beginning-age line highlighted | head: RMDs | stmt: Required Minimum Distributions generally begin at age 73 | src: IRS · January 2026 | label: VERIFIED | claim: rmd-beginning-age-73 | the age is on the card, not in the VO — the draft says "later in life" and the creator's wording stands]`

**6.11**
> Those are the withdrawals the government forces you to start taking from your traditional retirement accounts later in life.

`[img: a withdrawal form on a desk with a date circled on a wall calendar behind it | head: NOT OPTIONAL | stmt: The IRS sets the date, not you. | src: IRS · January 2026]`

**6.12**
> A series of strategic Roth conversions in your early retirement years can potentially lower your taxable income in the long run.

`[img: a hand moving a portion from the TAX-DEFERRED folder to the ROTH folder | head: ROTH CONVERSIONS | stmt: Move it early, on purpose. | label: OPINION — a strategy, not an agency rule; no source card, and the word "potentially" stays]`

**6.13**
> Done before Social Security and R.M.D.s both kick in, it can even reduce the taxes you'll owe on your Social Security benefits.

`[img: a timeline band with two markers — SOCIAL SECURITY and RMDs — and the window before both shaded | head: THE WINDOW | stmt: The years before both start. | label: OPINION on the outcome; the fact that benefits can be taxable is VERIFIED (IRS) — do not put a percentage on this frame]`

**6.14**
> This final step is about shifting from financial autopilot to being a deliberate, hands-on C.E.O. of your own retirement.

`[img: a plain desk with a single nameplate reading YOUR RETIREMENT, nobody seated | head: HANDS ON | stmt: Autopilot off.]`

**6.15**
> It's about orchestrating all your income streams into a smooth, tax-efficient, and sustainable paycheck.

`[img: three labelled inflow arrows converging into one outflow on a plain card — SOCIAL SECURITY · WITHDRAWALS · EARNED INCOME → ONE PAYCHECK | head: ONE PAYCHECK | stmt: Several sources, one steady paycheck. | no dollar amounts]`

**6.16**
> One that will last the rest of your life. It's the final piece that turns a pile of assets into true financial freedom.

`[img: an older couple on a US porch at dusk, seen from behind, unhurried | head: THE FINAL PIECE | stmt: A pile of assets becomes a paycheck.]`

---

## Chapter 7 — The roadmap, and today's one job

*Recap, the callback to the opening claim, then ONE physical action. The action is the
insert; everything around it is the draft.*

**7.1**
> So there you have it: a five-step roadmap to prove it's never, ever too late.

`[img: all five cards face-up in a row on the table, complete | head: THE FIVE STEPS | stmt: The whole roadmap, in one frame.]`

**7.2**
> One: stabilize your foundation. Plug the leaks by killing high-interest debt and building your emergency fund.

`[img: card one alone, lettered STABILIZE, the bucket from 2.3 behind it | head: ONE — STABILIZE | stmt: Kill high-rate debt · Build 3–6 months | label: the 3–6 months is OPINION / CONVENTION — no source card here either]`

**7.3**
> Two: maximize your savings. Go on offense and take full advantage of those powerful catch-up contributions.

`[img: card two, lettered MAXIMIZE | head: TWO — MAXIMIZE | stmt: 2026 catch-ups · $8,000 at 50+ · $11,250 at 60–63 | src: IRS · November 2025 | label: VERIFIED | the recap card repeats the figures, so it repeats the source line — a recap frame is still a frame]`

**7.4**
> Three: protect your base. Build a fortress with the right insurance and a solid plan for healthcare costs.

`[img: card three, lettered PROTECT | head: THREE — PROTECT | stmt: Insurance reviewed · HSA if eligible · A long-term-care plan | no figure]`

**7.5**
> Four: create income flexibility. Give yourself the power to delay Social Security and own your timeline.

`[img: card four, lettered INCOME | head: FOUR — INCOME | stmt: Delay past full retirement age → +8% a year to 70 | src: SSA · as of August 2026 | label: VERIFIED]`

**7.6**
> And five: plan a deliberate transition with a smart, tax-efficient withdrawal strategy.

`[img: card five, lettered TRANSITION | head: FIVE — TRANSITION | stmt: Withdrawal order · Roth conversions · RMDs at 73 | src: IRS · January 2026 | label: VERIFIED for the age 73; the rest is strategy]`

**7.7**
> Feeling behind in your fifties is stressful, but it's a feeling, not a fact.

`[img: the same man from 1.1 at the same kitchen table, the statement now set aside, looking out the window | head: A FEELING, NOT A FACT | stmt: The opening question, answered. | CALLBACK to 1.1 — same set, same light, statement moved]`

**7.8**
> You are not powerless. This isn't about some impossible standard of perfection; it's about making a few high-impact choices in the right order.

`[img: the five cards again, a hand resting on the first one | head: NOT POWERLESS | stmt: A few choices. In order.]`

**7.9**
> You have far more control than you think. You just needed a system.

`[img: the notebook from 1.7, now written on, closed with a pen on top | head: A SYSTEM | stmt: You had the control. You needed the order.]`

**7.10**
> Here's the one thing to do today, and it takes about five minutes.

`[img: a laptop on a US kitchen table, a plain login screen, a cell phone beside it | head: TODAY, FIVE MINUTES | stmt: One thing. Today. | CTA — the only one in the video]`

**7.11**
> Log in to your workplace retirement plan account and find the page that shows your contribution rate.

`[img: a plain retirement-plan account screen with a CONTRIBUTION RATE row, the percentage blanked | head: FIND THIS ONE NUMBER | stmt: Your current contribution rate. | needs nothing the viewer does not already have — no branch, no form, no phone call]`

**7.12**
> Write that number down, because that single number is the one step two is going to change.

`[img: a hand writing a percentage onto a sticky note and pressing it to the edge of the laptop, the figure itself illegible | head: WRITE IT DOWN | stmt: That number is where step two starts.]`

**7.13**
> Now that you have the roadmap, your next move is to figure out your target.

`[img: a blank card with a question mark set beside the completed row of five | head: WHAT'S YOUR NUMBER? | stmt: The roadmap is set. The target is not.]`

**7.14**
> To help with that, be sure to watch our next video, How to Calculate Your True Retirement Number, right here.

`[img: an end-card region held clear for the next-video thumbnail, plain ground | head: NEXT: YOUR RETIREMENT NUMBER | stmt: How to Calculate Your True Retirement Number | leave the right third of frame empty for the YouTube end screen]`

**7.15**
> It's the perfect next step on this journey. And if this was useful, subscribe, so the next one finds you.

`[img: the same end-card ground, subscribe affordance area kept clear | head: NEXT STEP | stmt: Subscribe · Next video | one subscribe ask, plainly, once]`

**7.16**
> Thanks for watching, and go start building that future today.

`[img: the older couple from 6.16 walking a US neighborhood sidewalk in evening light, seen from behind | head: START TODAY | stmt: Step one is today. | FULL DISCLAIMER CARD holds over the last 4 s — see below]`

---

# FACT TRACE — every figure in the script, and where it comes from

**No figure appears in this script that is not below.** Each row's claim note points at a
source note in `vault/sources/<agency>/`; the video links to CLAIMS, never to sources
(`fact_gate._indirection_note`).

| Line | Figure | Label | Agency + date on frame | Claim note | Expiry |
|---|---|---|---|---|---|
| 2.6 | credit card interest **north of 20% a year** | verified (shape only) | Federal Reserve G.19 · August 2026 | `credit-card-apr-shape-2026` | **monthly, 2026-09-15** |
| 3.8 | 401(k)/403(b) limit **$24,500** | verified | IRS · November 2025 | `401k-elective-deferral-2026` | annual, 2027-01-31 |
| 3.9–3.10 | age-50 catch-up **$8,000** → total **$32,500** | verified | IRS · November 2025 | `401k-catchup-age50-2026` | annual, 2027-01-31 |
| 3.11–3.12 | IRA **$7,500 + $1,100 = $8,600** | verified | IRS · November 2025 | `ira-limit-2026` | annual, 2027-01-31 |
| 3.16–3.17 | ages 60–63 catch-up **$11,250** → total **$35,750** | verified | IRS · November 2025 | `401k-supercatchup-60-63-2026` | annual, 2027-01-31 |
| 3.23–3.25 | Roth catch-up threshold **$150,000** prior-year FICA wages, indexed | verified | IRS Notice 2025-67 · November 2025 | `roth-catchup-threshold-2026` | annual, 2027-01-31 |
| 4.8 | HSA age-55 catch-up **$1,000** (statutory, not indexed) | verified | IRS Pub 969 · January 2026 | `hsa-catchup-age55` | stable, 2027-08-15 |
| 5.11–5.12 | claim at 62 → **−30%** (FRA 67) / **−25%** (FRA 66) | verified | SSA · as of August 2026 | `ss-early-claim-reduction-62` | stable, 2027-08-15 |
| 5.13–5.15 | delayed retirement credit **+8%/yr** → **+24%** (FRA 67) / **+32%** (FRA 66) | verified | SSA · as of August 2026 | `ss-delayed-retirement-credit` | stable, 2027-08-15 |
| 6.10 (card only) | RMDs generally begin at **age 73** | verified | IRS · January 2026 | `rmd-beginning-age-73` | stable, 2027-08-15 |

**Unsourced by design — labelled, no agency card, and that is correct:**

| Line | Claim | Label | Why no source |
|---|---|---|---|
| 2.9 | highest-rate-first payoff order | opinion | A method, not an agency rule. |
| 2.14 / 7.2 | emergency fund of **3–6 months** of essential expenses | opinion / convention | US convention, not a statistic (`facts-staging §2`). Frame as "the standard advice". |
| 3.19–3.20 | "free money" on the match · +1% every few months | opinion | No agency publishes a match rate or this method. |
| 4.4 | healthcare costs are a real risk to the plan | opinion | The **ranking** was cut — no whitelisted agency publishes a ranked fear list. |
| 4.6 | "one of the most incredible savings tools" | opinion | A judgement; the three tax mechanics beside it are verified. |
| 4.11 | "enough" life insurance | opinion | Personal, unquantifiable here. |
| 4.13 | long-term care "astronomical" | opinion | **Numberless on purpose** — every circulating cost table is insurer-published or off-whitelist. |
| 6.5 | the **4% rule** | opinion / convention | 1994 study, popularised 1998. No whitelisted agency publishes it and no primary URL exists to give it. The hedge stays. |
| 6.7 / 6.9 / 6.12–6.13 | withdrawal sequencing · "tens, even hundreds of thousands" · Roth conversions | opinion | Planning strategy, not published rule. No figure reaches a frame. |

**Available, sourced, and deliberately NOT used:**

- **The earnings test ($24,480 / $65,160, SSA 2026, `ss-earnings-test-2026`).** `facts-staging
  §4`: the script is safe without it because the "keep working" and "delay claiming" beats
  never combine into "claim early and keep working". **If any later stage adds that beat, the
  number and the recalculation qualifier — withheld benefits are credited back at full
  retirement age — become mandatory in the same breath.**
- **Fed SHED "$400 emergency, 63% could cover it" and the FDIC $250,000 limit.** Both are
  HARD in `money-facts-2026` and `facts-staging` names the SHED figure as the strongest
  available opener for Step 1. Not used: the draft has no figure in Step 1, and adding one
  would be this stage authoring, which `creator_wording_is_source_of_truth` forbids.
  **Available if fin-audit or the creator wants Step 1 to carry proof.**
- **Every figure in `facts-staging §5`** (the 70%-need-care statistic, Genworth cost tables,
  the Fidelity retiree-healthcare estimate, average balances by age, EBRI/Gallup fear
  rankings, any HYSA APY). Rejected at evidence stage. **Do not rediscover them.**

---

# DISCLAIMER — all four placements (`fact_gate.disclaimer_placements`)

Text, verbatim from `fin-script.json fact_gate.disclaimer`:

> This video is general financial education, not financial, tax, or legal advice. No specific
> product, fund, bank, or provider is recommended. Figures are current as of the date shown on
> screen and change over time. Confirm anything that affects your own decision with the issuing
> agency or a licensed professional.

| Placement | Where, in this cut |
|---|---|
| **spoken** | Lines **3.4–3.5** at 3:16, before the first dollar figure at 3:40. |
| **onscreen** | Lower third on **3.8**, the frame carrying the first dollar figure. Full card holds over the last 4 s of **7.16**. |
| **description** | Above the fold, before the chapter list. `fin-package` owns this. |
| **pinned** | Required — this video touches **taxes and Social Security claiming**. Add "Confirm with a tax professional". |

---

# HANDOFF — what the next stages must not undo

1. **`fin-storyboard` assigns every layout.** No cue in this file names an archetype, a
   ground, a plate or a modifier, and none should be added here.
2. **Line 1.8 needs TWO framings inside its one scene.** At 152 chars it runs 9.45 s, past
   `scene.max_scene_seconds` 9.0, and `check_build` fails a scene holding one photo that long.
   The text is creator-ruled and is not cut, so the fix is on the frame: wide, then a push.
   Precedent: `passive-income-number` line 2.2, 155 chars, shipped this way.
3. **Nine consecutive IRS reveals in Chapter 3 each need their own source card.** A card that
   inherits its agency line from the frame before it fails `fact_gate.as_of_required`, because
   the viewer screenshots one frame, not the sequence.
4. **The `ssa.gov` captures (5.11, 5.13) are still owed and cannot be faked.** Every direct
   fetch from this pipeline returned HTTP 403; the figures are statutory and cross-agree
   across three SSA documents, but the *screenshot* must be a real page from a network path
   that reaches ssa.gov (`facts-staging §6`).
5. **Eleven screenshots are owed in total.** Filenames live in each source note's
   `screenshot:` field, URLs in `facts-staging §1`. `fact-integrity §4` and gate point 1
   cannot be satisfied without them.
6. **Three hedges are compliance, not style, and stay word for word:** "If your plan allows
   it" (3.16), "assuming your plan has a Roth option" (3.24), "a starting guideline, not
   gospel" (6.5).
7. **Measure `hook_gate_en` on the rendered clip** with silencedetect and record it in
   run.json. The 11.2 s in this file is a model.
8. **Regenerate the chapter start times from ffprobe durations** before they ship as YouTube
   chapters — `tts.pause_seconds` will push every chapter later than the table above.
9. **Every source line renders as `AGENCY · as of MONTH YEAR`.** `fact_gate.as_of_required`
   wants the words *as of* on the frame carrying the figure. This file writes some cards
   `IRS · November 2025` and others `IRS Pub 969 · as of January 2026`; the storyboard
   normalises all of them to the `as of` form. The month is the source's **publication**
   month (IRS Notice 2025-67 = November 2025; G.19 current release = August 2026), never
   the month the video ships.
10. **Chip texts in this file are already at the 22-char ceiling** (`layout.max_chip_chars`,
   `design-finance-blockframe §4`). Seven `stmt:` chip sets were shortened by fin-audit on
   2026-08-15 — 4.7, 5.5, 5.12, 5.14, 5.15, 7.2, 7.3. Do not re-lengthen them: `.row` has
   `flex-wrap`, so an over-long fourth chip wraps 3+1 into an orphan and **no build checker
   catches it**.
11. **The lane is unmeasured.** `knowledge/video-studies/financial-freedom-after-50.md` is an
   empty-lane finding, not a study: `library.db` holds no US retirement comparable in the
   LONG band. The beat placements in this file are carried from three studies of a **20–35**
   audience and are continuity, not evidence. A real scrape + study is owed before the next
   50+ topic.
