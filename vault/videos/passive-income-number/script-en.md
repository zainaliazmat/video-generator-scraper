---
summary: US/English script for «The Passive-Income Number». MEDIUM tier, per-line chapter architecture — 81 single-sentence VO lines across 6 chapters, 8,014 chars ≈ 8:41 at the corrected budget formula and the 17.57 en rate. RESTYLED to style E (teacher + curiosity) on 2026-08-07; chapters 1 and 2 are the creator-approved style-E draft verbatim, chapters 3–6 restyled to match. Facts, chapter boundaries, beat order and every number are unchanged from attempt 1. A US REWRITE, not a translation of script-hi.md, which was NOT read. Dollars only. The hero pair is $1.5M at a 4.0% withdrawal rate = $5,000/month versus about $5.6M for the same $5,000 from S&P 500 dividends alone at today's ~1% yield.
updated: 2026-08-07
source: run.json creator brief + constraints + style_decision block · studio/voice-tests/passive-income-number/style-E-en-teacher-curiosity.txt (ch1+ch2, creator-approved, taken verbatim) · script-en.md attempt 1 (facts, structure, cues) · facts-staging.md attempt 1 (Parts A, C, D, F) · study note knowledge/video-studies/passive-income-number.md · knowledge/us-english-script-style.md · skills/long_form_scripting.md. Architecture per tools/format.json tiers.medium + chapter_design.
stage: fin-script, cut en, attempt 2 — STYLE E RESTYLE (register only; facts, structure, chapter boundaries and argument unchanged from attempt 1, which passed fin-audit with 3 VO edits)
---

# «The Passive-Income Number» — US / English edition (MEDIUM, per-line chapters)

**Studio project (to build):** `studio/videos/passive-income-number-en`
**Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`, style 0.
**On-screen text:** English. **Title + description:** English.
**Architecture:** `blockframe-9` base (`format.json architecture_lock`) + the **chapter
archetype layer** (`format.json chapter_design`, A/B/C/D). **MEDIUM tier → per-line
chapters** — none of the 9-segment blockframe constants apply. **One line = one TTS clip =
one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line (bare Latin digits are a
coin-flip reading in ElevenLabs); initialisms too — the VO says "the S and P five hundred",
the screen says `S&P 500`. On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-US")` grouping.

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person expertise,
no fund/stock/index/account pick. **I** and **we** appear nowhere in the VO — the style-E
teaching signposts are **imperatives**, never a narrator claiming to teach. Funds, indexes
and yields appear **only as price evidence**.

---

## What style E is, and what it did NOT change

The creator picked style E for both cuts after a listening test (`run.json.style_decision`,
2026-08-07). **This is a restyle, not a rewrite.** Every fact, every chapter boundary, every
beat order and every number is attempt 1's, which passed `fin-audit`. Four moves changed the
writing:

1. **The open is a what-if, not a statement.** The phone's *silence* is the promise; its
   *single buzz* is the payoff. (Was: "You wake up, and there is no alarm.")
2. **Signposted teaching throughout** — *Notice this · Think of it this way · understand
   where it comes from · Now watch what it buys · Work it through · Notice what changed ·
   Go back to the tank.* One per beat at most; they mark structure, never fill space.
3. **The tank analogy is load-bearing and pays off twice.** 2.2 establishes it — you filled
   a tank slowly over years, and the only question that matters is how much you can draw
   each year without emptying it. **4.7–4.8 is its callback**, so the yield-trap warning at
   the halfway mark is a return to a picture the viewer already holds, not a new idea. **5.5
   is the second callback**: same tank, but the dividends-only route may only take what the
   tank hands you.
4. **Stepped arithmetic.** Yearly figure → monthly figure → the division, each on its own
   line. No calculation is compressed into one mouthful.

**Chapters 1 and 2 are `studio/voice-tests/passive-income-number/style-E-en-teacher-curiosity.txt`
verbatim** — 23 lines, creator-approved, not one character altered. Chapters 3–6 are restyled
to match. **Line 1.7 is untouchable** and is unchanged from attempt 1 as well.

---

> ### ⚠ THE SIX THINGS THAT MUST NOT ENTER THIS CUT
> 1. **This is a US rewrite, not a translation.** The Indian cut's currency glyph, lakh,
>    crore, SIP, SWP, PPF, POMIS, SCSS, a post office, an Indian bank passbook — none may
>    appear in this file, in a cue, or in a photograph. `script-hi.md` was **not read**.
> 2. **No corpus figure without its rate in the same breath AND the same frame.** This is
>    `run.json.constraints.withdrawal_rate_on_screen`, and it is the exact failure the study
>    observed in both format twins — Dark Ledger states 4% once, then ships six bare numbers.
>    Every rung below re-speaks its rate. **fin-audit caught three lines on attempt 1 where
>    the frame carried the rate and the VO did not** — all three are fixed here, and all
>    fourteen corpus lines were re-checked one at a time (list at the end of the fact trace).
> 3. **Never convert a corpus into an age.** No "financially free at fifty", no "start at
>    twenty-eight", no age on any rung. Twin A's *"Start at 28 and you are financially free
>    at 50"* is the sentence `no_unsourced_retire_early` exists to ban.
> 4. **No return promise.** Every number here is division from a stated assumption. The four
>    percent rule is cited as a 1994 paper and a 1998 paper **with their documented limits**,
>    never as a law. `no_return_promise`.
> 5. **No bait and switch on the title.** The video is packaged on the dividend question and
>    it answers the dividend question, in full, at 5.7 (70.7% — the reward beat). The honest
>    answer is that dividends-only costs roughly four times the corpus. Deliver it, then
>    price it. Do not withhold it past the reward beat and do not soften it.
> 6. **No cross-market arithmetic, ever.** No conversion, no shared axis, no "which is
>    about". The Indian numbers are a different video sourced from different literature at
>    different rates.

---

## Title options (English)

1. **How Much You Need Invested To Live Off Dividends ($5,000/Month)**
   *(recommended — the exact format-twin phrase, keyword-front-loaded, with the payoff in
   the parenthetical. Six clones of this title, six breakouts, per `run.json.source_note`)*
2. Live Off Dividends: The $5.6 Million Problem Nobody Mentions
3. $5,000 A Month From Investments: The Real Number, At Four Percent

---

## Chapters (ship as YouTube chapters)

| # | Chapter | starts | % | lines | chars |
|---|---|---|---|---|---|
| 1 | The day | 0:00 | 0.0% | 8 | 669 |
| 2 | Rung one: the grocery bill | 0:44 | 8.5% | 15 | 1,642 |
| 3 | Rung two, rung three, and the fine print | 2:30 | 28.8% | 16 | 1,496 |
| 4 | Rung four, and the number that is a warning | 4:08 | 47.6% | 13 | 1,288 |
| 5 | What dividends alone actually cost | 5:31 | 63.6% | 16 | 1,580 |
| 6 | The day, again | 7:14 | 83.4% | 13 | 1,339 |

---

## Timing budget

English narration = **17.57 chars/s** (`format.json cuts.en.chars_per_second`, **raised from
16.1 on 2026-08-07** — the mean of three flat measurements on shipped MEDIUM/LONG cuts,
17.588 of them from this very cut's attempt-1 audio). MEDIUM charges **0.25s lead-in + 0.55s
tail per line** (`tiers.medium`) = **0.8 × 81 = 64.8s** of inter-line padding.

**Budget formula — the corrected one.** Padding is not audio, so it comes out of the target
*before* the rate is applied:

```
(510 − lines × (lead_in + tail)) × chars_per_second
(510 − 81 × 0.8) × 17.57 = 445.2 × 17.57 = 7,822 chars
```

This draft is **8,014 chars — +2.5% over budget, landing at 520.9s (8:41) against the 510s
target, +2.1%.** Inside the ±5% band. *(8,002 → 8,014 at fin-audit: the 4.8 rewrite below
adds 12 chars. Chapter starts after ch4 shift ≈ +0.7s — regenerate them from measured audio,
per build handoff 3.)*

> ⚠ **Do NOT use `target_seconds × rate`.** That formula ignores per-line padding and
> inflates a MEDIUM script by ~17% (510 × 17.57 = 8,961). `cuts.en._chars_per_second_trap`
> records why it survived so long: a wrong rate and a wrong formula cancelled, and the
> ordering rule — fix the formula first, raise the key second — is what finally let the key
> be corrected. **The trap is RESOLVED for `en`. It still applies to `cuts.hi`, whose 13.03
> was measured on the retired voice.**

| Ch | lines | chars | VO | + padding | runtime | starts |
|---|---|---|---|---|---|---|
| 1 | 8 | 669 | 38.1s | 6.4 | 44.5s | 0:00 |
| 2 | 15 | 1,642 | 93.5s | 12.0 | 105.5s | 0:44 |
| 3 | 16 | 1,496 | 85.1s | 12.8 | 97.9s | 2:30 |
| 4 | 13 | 1,288 | 73.3s | 10.4 | 83.7s | 4:08 |
| 5 | 16 | 1,580 | 89.9s | 12.8 | 102.7s | 5:31 |
| 6 | 13 | 1,339 | 76.2s | 10.4 | 86.6s | 7:14 |
| | **81** | **8,014** | **456.1s** | **64.8s** | **520.9s** | |

**Pace:** 520.9 / 81 = **6.43s average scene** (`target_scene_seconds` 6.5, bang on).

**The line-length ceiling is 144 characters**, not attempt 1's 120: at 17.57 c/s,
`max_scene_seconds` 9.0 minus 0.8s padding = 8.2s of VO = 144 chars. Shortest line 41 chars
→ 3.1s, well over `tts.min_clip_seconds` 1.0.

> ⚠ **ONE LINE EXCEEDS IT, deliberately: 2.2 at 155 chars → 8.8s VO + 0.8 = 9.6s.** It is a
> creator-approved verbatim line and the one that plants the tank, so it is not cut. **That
> scene must carry TWO `data-framings`** — wide on the tank, then a push to the tap — so no
> single framing holds past 9.0s. Same mechanism as a continuous zoom, applied inside one
> scene instead of across two. Build handoff item 6.

### Where the retention beats land

- **The promise lands inside the fifteen-second gate at 1.3** — *"money is deposited into
  your account"* opens **8.7s** and closes **12.8s**; 1.4 reinforces it at 13.6s. Both twins
  are outside the gate (A ≈0:22, B ≈0:45); **the gate still wins.** Style E buys this for
  free: the silence in 1.1–1.2 is the setup, so the deposit reads as a payoff rather than an
  announcement.
- **The packaging promise is confirmed at 1.7 (28.9s, 0:29)** — four seconds earlier than
  attempt 1. The loop it opens closes at 5.7.
- **First figure at 2.3 (1:00)**: four percent, marked *not a law* in the same line. The
  first *corpus* does not exist until 2.13.
- **Rung one lands at 2.13 = 2:09 (24.8%)** — inside the 8–25% band, but at its edge, which
  is the one real cost of style E's longer chapter 2. Flagged and accepted: the tank is what
  makes every later rung legible, and 24.8% still pays out earlier than either twin does in
  runtime-equivalent terms.
- **The hero pair straddles halfway**: 4.2 at **4:15 = 49.1%**, 4.3 at **4:22 = 50.4%**.
- **The tank callback opens the mid-video drop zone.** 55–65% = 4:46–5:38, and 4.7 lands at
  **4:47**. The drop zone opens on a *return to a familiar picture*, which is the strongest
  available form of "never a flat transition".
- **The yield trap straddles 5:00**: 4.6 at 4:40, the mechanism at 4.9 = **4:57**. Both
  twins place their 10–12% warning within about half a minute of that absolute mark, on two
  different runtimes.
- **The ~70% reward is 5.7 at 6:08 = 70.7%**: the $5.6M answer to the title.
- **The close is the callback, not the recap** (study conclusion 11): 6.11 returns to the
  day at 96.3%.
- **One CTA, terminal, at 6.13 = 98.6%. Zero mid-roll CTA** — third independent confirmation
  of that line, and B (the higher-reach twin) has zero CTAs at all.

---

## The ladder, and why it ascends in this order

Both twins price income in **named household bills**, never in "wealth". This cut does the
same, except every bill is a **published BLS figure** rather than a vibe — so each rung is
`a sourced annual bill ÷ a sourced rate`, and the twins' weakest link (invented bill sizes)
is closed.

| rung | the bill | annual (BLS CE 2024) | monthly | ÷ 4.0% | lands |
|---|---|---|---|---|---|
| 1 | food | $10,169 | $847 | **$254,225** | 2.13 · 2:09 |
| 2 | transportation | $13,318 | $1,110 | **$332,950** | 3.4 · 2:47 |
| 3 | housing (rent or mortgage) | $26,266 | $2,189 | **$656,650** | 3.8 · 3:14 |
| 4 | **the worked paycheck** | $60,000 | **$5,000** | **$1,500,000** | 4.2 · 4:15 |
| 5 | the whole average household | $78,535 | $6,545 | **$1,963,375** | 5.15 · 6:59 |

⚠ **Deviation from the brief, deliberate and flagged (carried unchanged from attempt 1).**
The brief places rent/mortgage at rungs 4–5, in the 50–85% band. **BLS housing is
$2,189/month, which is less than the $5,000/month hero** — putting it after the hero makes
the ladder descend, and a descending ladder kills the only escalation this format has.
Housing is therefore rung **3** (3:14, 37.3%), and the 50–85% band carries rungs 4 and 5,
the two rungs that actually sit above it.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line below is a VO line, verbatim, and is the only
> thing that goes to TTS. Everything in backticks is a production cue and never spoken.
> **Slice these strings — never retype them.**
>
> `arch:` names the chapter archetype (`format.json chapter_design.archetypes`) —
> **A** plate (opens, hand-offs) · **B** figure (the point is a number) · **C** ledger
> (evidence: a document, a form, an artefact) · **D** band (the motion is the argument).

---

## Chapter 1 — The day (WHAT-IF COLD OPEN · second person · no number, no greeting)

*The twins open on the **won morning** — wake → no alarm → coffee → window → phone → money
that arrived while you slept. Style E keeps the payload and changes the grammar: it is a
**what-if**, the phone's **silence** is the promise, and its **single buzz** is the payoff.
The number is named and withheld (twin B's move), never announced (twin A's), because an
open loop commits to nothing and `no_return_promise` allows nothing else. Every frame is
American.* **⚠ Creator-approved verbatim — do not edit any VO line in this chapter.**

**1.1**
> Imagine a day when your phone does not ring once.

`[arch: A | img: a phone lying face-down on a nightstand in a quiet bedroom, screen dark, first light through a blind, no people | head: IMAGINE ONE DAY | stmt: The phone does not ring once.]`

**1.2**
> No alarm. No call from work. No message reminding you what you owe someone.

`[arch: D | img: an unlit bedside clock face-down beside the bed, hard morning shadow, nothing switched on | head: NOTHING ASKS FOR YOU | stmt: No alarm · No call from work · No debt reminder | cascade 3 items, 0.6s gap]`

**1.3**
> And on that same day, before noon, money is deposited into your account.

`[arch: A | img: a US kitchen counter in late-morning light, a mug and a folded newspaper, nobody in frame — ONE continuous zoom across 1.3 and 1.4 | head: BEFORE NOON | stmt: Money is deposited. | PROMISE — opens 8.7s, closes 12.8s, inside the fifteen-second gate]`

**1.4**
> Notice this — the phone buzzes exactly once that day, and that one buzz is the money arriving.

`[arch: D | img: the same counter, tighter — the phone now face-up beside the mug, notification glow, screen text illegible, no face | head: ONE BUZZ | stmt: That one buzz is the money arriving. | lottie candidate: phone-notify-credit (already in the library) — re-tint, and the notification card carries NO figure: the beat is the buzz, not an amount]`

**1.5**
> You did not get rich. You reached one specific number.

`[arch: A | img: a single blank index card centred on a bare wooden table, hard side light | head: NOT RICH | stmt: One specific number.]`

**1.6**
> That number has one job: to quietly pay your groceries, your gas, and your rent.

`[arch: D | img: a paper grocery bag, car keys and a set of house keys laid in a row on wood, top-down | head: ITS ONE JOB | stmt: Groceries · Gas and the car · Rent or the mortgage | cascade 3 items, 0.6s gap]`

**1.7**
> Everyone asks how much you need invested to live off dividends, and the honest answer costs more than the popular one.

`[arch: A | img: a laptop on a kitchen table showing a blurred search results page, hands only, text illegible | head: THE QUESTION | stmt: The honest answer costs more than the popular one. | colour: --warn | PACKAGING PROMISE CONFIRMED at 0:29 — the loop this opens closes at 5.7 | ⚠ UNTOUCHABLE LINE, run.json.style_decision]`

**1.8**
> In this video that number is built one rung at a time, starting with the smallest, and one condition rides along on every rung.

`[arch: A | img: the lowest rungs of a wooden ladder against a plain exterior wall, the top out of frame | head: ONE RUNG AT A TIME | stmt: Smallest first. One condition on every rung.]`

---

## Chapter 2 — Rung one: the grocery bill (THE TANK, THE RATE, THEN THE FIRST CORPUS)

*The rate is staged as a **fact in its own right** (`facts-staging.md` A.1) and is spoken
before any corpus exists, because `withdrawal_rate_on_screen` makes a bare number a
fabricated promise. **2.2 plants the tank**, which is what turns "safe withdrawal rate" from
jargon into a picture, and it is load-bearing again at 4.7 and 5.5. The arithmetic is
stepped: yearly (2.11) → monthly (2.12) → the division (2.13). Rung one lands at **2:09
(24.8%)**.* **⚠ Creator-approved verbatim — do not edit any VO line in this chapter.**

**2.1**
> Start with the rate, because a number without a rate is a wish with a comma in it.

`[arch: A | img: a blank ruled notebook page with a single pencil laid across it | head: START WITH THE RATE | stmt: A number without a rate is a wish. | colour: --target]`

**2.2**
> Think of it this way — you filled a tank slowly, over years, and the only question that matters is how much you can draw out each year without emptying it.

`[arch: D | img: a plain steel water tank with one tap low on its side, workshop light, no branding, no legible gauge | head: THE TANK | stmt: How much can you draw each year without emptying it | colour: --target | ⚠ 155 chars = 9.6s — THIS SCENE NEEDS TWO data-framings: wide on the tank, then a push to the tap | lottie candidate: a tank with a level line and one tap; search the library first, and the level is decorative, never a measurement]`

**2.3**
> That question has a number, and the number is four percent — but understand where it comes from, because four percent is not a law.

`[arch: A | img: a plain wall with one nail and no picture hanging on it, hard shadow | head: NOT A LAW | stmt: Four percent is a finding. Not a law. | colour: --target]`

**2.4**
> It is two papers, and both of them have names and dates.

`[arch: C | img: two stapled academic papers squared on a desk under a lamp | head: TWO PAPERS | stmt: Both have names and dates.]`

**2.5**
> William Bengen published the first one in the Journal of Financial Planning, in October nineteen ninety-four.

`[arch: C | img: an open journal page, macro, one title line in focus, body text illegible | head: PAPER ONE | stmt: William Bengen, Journal of Financial Planning | foot: "Determining Withdrawal Rates Using Historical Data", October 1994, vol. 7 no. 4, pp. 171-180 | colour: --target]`

**2.6**
> He tested a portfolio split half in stocks and half in bonds, across retirements starting in nineteen twenty-six.

`[arch: C | img: a printed table of historical returns, columns of figures, one row lit | head: WHAT HE TESTED | stmt: 50% stocks · 50% bonds | foot: Retirement start years 1926-1966, withdrawals inflation-linked after year one]`

**2.7**
> Four years later, three Trinity University professors ran it again and published it in February nineteen ninety-eight.

`[arch: C | img: a bound journal volume open flat, spine cracked, on a library table | head: PAPER TWO | stmt: Three Trinity University professors. | foot: Cooley, Hubbard and Walz, "Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable", AAII Journal, February 1998, pp. 16-21 — the Trinity Study | colour: --target]`

**2.8**
> Across thirty-year retirements, four percent survived ninety-five percent of the periods they tested.

`[arch: B | img: a grid of small squares printed on paper, most inked, a few blank, macro | head: WHAT THEY FOUND | num: 95% | foot: 4.0%, inflation-adjusted withdrawals, 30-year payout: 95% of periods at 100% stocks and at 50/50 — Trinity Table 3, data 1926-1995 | colour: --target]`

**2.9**
> So four percent is the working number here, and it is a finding with a date, not a promise about your money.

`[arch: A | img: a calendar page from an old desk diary, one date circled in pencil | head: THE WORKING NUMBER | stmt: 4.0% — a finding with a date. Not a promise. | colour: --target]`

**2.10**
> Now watch what it buys. Take a yearly bill, divide it by four percent, and that is the money the bill needs behind it.

`[arch: D | img: a hand writing a short division on a paper napkin, hand only, figures illegible | head: THE WHOLE METHOD | stmt: annual bill DIVIDED BY 4.0% = the money behind it | colour: --fund]`

**2.11**
> The Labor Department says the average household spent ten thousand one hundred sixty-nine dollars on food in one year.

`[arch: B | img: a full US grocery cart at a checkout lane, no faces, no readable brand marks | head: FOOD, ONE YEAR | num: $10,169 | foot: Average annual food spending per consumer unit, 2024 — BLS Consumer Expenditures, released 19 Dec 2025, USDL-25-1586 | colour: --target]`

**2.12**
> Work it through — that is about eight hundred and forty-seven dollars a month, walked out of a store in bags.

`[arch: B | img: two paper grocery bags on a car's back seat, daylight, no plates visible | head: PER MONTH | num: $847 | foot: $10,169 divided by 12 — arithmetic, not a separate statistic]`

**2.13**
> Divided by four percent, the grocery bill needs two hundred fifty-four thousand dollars standing behind it.

`[arch: B | img: a single loaf of bread on a bare wooden table, hard side light, nothing else in frame | head: RUNG ONE | num: $254,225 | foot: AT A 4.0% WITHDRAWAL RATE · $10,169 divided by 0.04 · ILLUSTRATIVE ARITHMETIC | colour: --fund | RATE IS IN THE FRAME AND IN THE LINE — non-negotiable, every rung]`

**2.14**
> Two hundred fifty-four thousand dollars, drawn at four percent a year, and the grocery bill stops costing you hours.

`[arch: B | img: a punched paper time card in a rack, hours illegible | head: WHAT IT REPLACES | stmt: $254,225 at 4.0% · the grocery bill stops costing hours | colour: --fund]`

**2.15**
> That is rung one. Notice what changed: the bill is the same, but your hours are no longer paying it.

`[arch: A | img: the bottom rung of a wooden ladder against a wall, shallow depth | head: RUNG ONE | stmt: Same bill. Your hours are free. | colour: --fund]`

---

## Chapter 3 — Rung two, rung three, and the fine print (28.8% → 47.6%)

*Rungs two and three, each corpus re-stamped with its rate in the VO line **and** in the
frame, and each stepped the same way chapter 2 established — yearly, monthly, then the
division. Then the two criticisms the papers make **of themselves** (`facts-staging.md` A.2
rows 1 and 2, both HARD primary, both verbatim), placed here, where the rule is being used,
rather than saved for a disclaimer nobody hears. 3.14–3.15 is the only sourced sentence
about stopping work early in this file, and it is a warning to withdraw **less**.*

**3.1**
> Rung two is parked outside your building.

`[arch: A | img: a used sedan at a kerb outside a US apartment block, evening, no plates legible | head: RUNG TWO | stmt: It is parked outside.]`

**3.2**
> The same survey puts transportation at thirteen thousand three hundred eighteen dollars a year.

`[arch: B | img: a fuel pump nozzle in a car's filler neck, price display illegible | head: TRANSPORTATION, ONE YEAR | num: $13,318 | foot: Average annual transportation spending per consumer unit, 2024 — BLS Consumer Expenditures, 19 Dec 2025 | colour: --target]`

**3.3**
> Work it through — that is about eleven hundred and ten dollars a month, all of it: payment, insurance, gas, repairs.

`[arch: D | img: four small paper slips fanned on a car's dashboard — a payment stub, an insurance card, a fuel receipt, a repair invoice, all illegible | head: PER MONTH | num: $1,110 | stmt: Payment · Insurance · Fuel · Repairs | foot: $13,318 divided by 12 — arithmetic, not a separate statistic | cascade 4 items]`

**3.4**
> Divided by four percent, the car and everything it costs needs about three hundred thirty-three thousand dollars.

`[arch: B | img: a single car key on a bare concrete floor, hard overhead light | head: RUNG TWO | num: $332,950 | foot: AT A 4.0% WITHDRAWAL RATE · $13,318 divided by 0.04 · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**3.5**
> Rung three is the biggest line in the American budget, and it has a landlord or a bank attached to it.

`[arch: A | img: a row of US mailboxes in an apartment lobby, one open | head: RUNG THREE | stmt: The biggest line in the budget. | colour: --warn]`

**3.6**
> Housing came to twenty-six thousand two hundred sixty-six dollars for the average household that year.

`[arch: B | img: a suburban US street of two-storey houses at dusk, wide, no people | head: HOUSING, ONE YEAR | num: $26,266 | foot: Average annual housing spending per consumer unit, 2024 — BLS Consumer Expenditures, 19 Dec 2025 | colour: --target]`

**3.7**
> That is a third of everything they spent, and about two thousand one hundred eighty-nine dollars a month.

`[arch: B | img: a printed pie-slice diagram on a statistical release page, macro, one wedge in focus | head: SHARE OF THE BUDGET | num: 33.4% | stmt: $2,189 a month | foot: Housing was 33.4% of total household spending in 2024; housing and transportation together were 50.4% — BLS | colour: --target]`

**3.8**
> Divided by four percent, rent or the mortgage needs about six hundred fifty-seven thousand dollars behind it.

`[arch: B | img: a single house key on a plain paper envelope, top-down, hard light | head: RUNG THREE | num: $656,650 | foot: AT A 4.0% WITHDRAWAL RATE · $26,266 divided by 0.04 · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**3.9**
> Say that one slowly, because it is where the number stops sounding like savings and starts sounding like a house.

`[arch: A | img: an empty front porch with two steps, late afternoon shadow | head: SAY IT SLOWLY | stmt: It stopped sounding like savings.]`

**3.10**
> Now understand what those papers say about themselves.

`[arch: C | img: a paper open at a methodology section, one paragraph in focus, a thumb holding the page | head: THEIR OWN FINE PRINT | stmt: The papers say this themselves. | colour: --warn]`

**3.11**
> The Trinity study states in one sentence that it did not adjust for taxes or for transaction costs.

`[arch: C | img: a single printed line of text under a magnifier on a desk | head: LIMIT ONE | stmt: "The study did not adjust for taxes or transaction costs." | foot: Cooley, Hubbard and Walz, AAII Journal, February 1998 — verbatim, from the study's own methodology | colour: --warn]`

**3.12**
> So every rung on this ladder is a before-tax number, and your real one is bigger than the arithmetic.

`[arch: D | img: a tax form corner and a pen on a kitchen table, figures illegible | head: WHAT THAT MEANS | stmt: Every rung here is a BEFORE-TAX number. | colour: --warn]`

**3.13**
> The second limit is the clock, because both papers were built for a thirty-year retirement.

`[arch: C | img: a wall clock with a plain white face in an empty hallway | head: LIMIT TWO | num: 30 YEARS | foot: Bengen's worst case was a 30-year horizon; Trinity's payout periods ran 15, 20, 25 and 30 years | colour: --warn]`

**3.14**
> Trinity's own conclusion says early retirees who expect long payouts should plan on lower withdrawal rates.

`[arch: C | img: the last page of a paper, a conclusion heading visible, body text illegible | head: THEIR CONCLUSION | stmt: "Early retirees who anticipate long payout periods should plan on lower withdrawal rates." | foot: Cooley, Hubbard and Walz, AAII Journal, February 1998, Conclusion — verbatim | colour: --warn]`

**3.15**
> That is the only sourced sentence about stopping work early in this video, and it is a warning.

`[arch: A | img: a long empty road running to the horizon, flat light | head: THE ONLY ONE | stmt: And it is a warning, not a plan. | colour: --warn]`

**3.16**
> Which brings up the number you actually came here for.

`[arch: A | img: a closed laptop on a table, one lamp behind it | head: NOW THE ONE YOU CAME FOR | stmt: — ]`

---

## Chapter 4 — Rung four, and the number that is a warning (47.6% → 63.6%)

*The hero corpus straddles halfway (4:15–4:22 = 49.1–50.4%), where twin A lands its number
and where the prior beat-map shape puts it. Then **the trap**, and this is where style E
earns its keep: **4.7–4.8 is the tank callback**, so the 10–12% warning arrives as a return
to a picture from 2.2 rather than as a new idea at the halfway mark — and it opens the
mid-video drop zone (55–65% = 4:46–5:38) on a familiar image instead of a flat transition.
The mechanism then lands at 4.9, straddling **5:00**, the absolute minute both twins
independently chose. Our version is better sourced than theirs: they assert that a big yield
is suspicious, this one shows the mechanism and then shows the only time the index actually
paid double digits.*

> ⚠ **Do not let the callback conflate a yield with a withdrawal rate.** The study caught
> twin B doing exactly that (*"This is the famous 4% rule"* said over a 4% dividend yield).
> The tank lines below are careful: an advertised twelve percent is *a promise about the
> tap*, and the reason it is a warning is that **the tank shrank** — a yield rises when the
> price falls. Nothing here says a high yield is a high withdrawal rate.

**4.1**
> Five thousand dollars a month is sixty thousand dollars a year, and it sits deliberately below the average household.

`[arch: B | img: a plain grey card on a table with five twenty-dollar bills laid in a fan, top-down | head: THE WORKED FIGURE | num: $5,000 / MONTH | foot: $60,000 a year, chosen below the BLS average of $6,545 a month so the figure is conservative and cannot be read as a promise | colour: --target]`

**4.2**
> Work it through — sixty thousand dollars a year, divided by four percent, is one and a half million dollars.

`[arch: B | img: a bank vault door, closed, wide, no signage | head: RUNG FOUR | num: $1,500,000 | foot: AT A 4.0% WITHDRAWAL RATE · $60,000 divided by 0.04 · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**4.3**
> One and a half million dollars, at a four percent withdrawal rate, is five thousand dollars a month.

`[arch: B | img: the same vault door, tighter on the dial — ONE continuous zoom from 4.2 | head: BOTH HALVES, TOGETHER | stmt: $1,500,000 AT 4.0% = $5,000 a month | colour: --fund]`

**4.4**
> Notice what that is. It is division — not a forecast, not a market call, not a promise.

`[arch: D | img: a pocket calculator on a desk, display illegible, a pencil beside it | head: WHAT THIS IS | stmt: Division. Not a forecast. | foot: corpus = annual income DIVIDED BY the withdrawal rate]`

**4.5**
> Now the warning, and it is the reason most people never reach any of these rungs.

`[arch: A | img: a rain-slick road at night with a single amber hazard light | head: NOW THE WARNING | stmt: This is where the ladder breaks. | colour: --warn]`

**4.6**
> Somewhere on your feed there is a payout advertised at ten percent, or twelve, and it looks like a shortcut.

`[arch: C | img: a phone held up showing a blurred short-video feed, hand only, no readable text or handle | head: ON YOUR FEED | stmt: 10% · 12% · "monthly income" | colour: --warn]`

**4.7**
> Go back to the tank, because twelve percent is a promise about the tap.

`[arch: D | img: the 2.2 tank re-photographed from a different angle, the tap now wide open, water running out | head: A PROMISE ABOUT THE TAP | stmt: 12% is a wider tap. | colour: --warn | TANK CALLBACK — the drop zone opens here, 4:47 | lottie candidate: the 2.2 tank with the tap opening and the level dropping]`

**4.8**
> The papers tested how long a tank lasts at each rate, and no advertisement changes that.

`[arch: A | img: the same tank, level low, tap still open, hard shadow | head: WHAT THE PAPERS TESTED | stmt: How long a tank lasts at each rate. | colour: --warn]`

**4.9**
> The number on the screen is usually real, because a yield is a payout divided by a price.

`[arch: D | img: a two-pan balance where the right pan has dropped, one pan empty | head: WHAT A YIELD IS | stmt: payout DIVIDED BY price | colour: --warn | THE 5:00 BEAT — both twins land their 10-12% warning within half a minute of this mark]`

**4.10**
> So a yield can double without one extra dollar being paid out, because the price fell and the tank shrank with it.

`[arch: D | img: a price sticker peeled half off a plain box, the box itself dented | head: THE PRICE FELL | stmt: Same payout. Smaller price. Smaller tank. | colour: --warn]`

**4.11**
> Going back to eighteen seventy-one, the highest reading ever was thirteen point eight four percent, in June nineteen thirty-two.

`[arch: B | img: a 1930s US newspaper financial page, archival grain, headline out of focus | head: THE ALL-TIME HIGH | num: 13.84% | foot: S&P 500 dividend yield, series from 1871 — maximum 13.84% in June 1932; long-run mean 4.21%, median 4.19% · multpl.com, read 5 Aug 2026 | colour: --warn]`

**4.12**
> That was the bottom of the Great Depression, and the yield was enormous because the prices had collapsed.

`[arch: C | img: a 1930s US breadline photograph, archival, wide, faces indistinct | head: WHAT WAS HAPPENING | stmt: The yield was enormous because the price had collapsed. | colour: --warn]`

**4.13**
> So a very big yield is very often a very small price, and a smaller price is a smaller tank.

`[arch: D | img: a discount tag hanging off a cracked item on a shelf, no brand visible | head: THE RULE | stmt: A very big yield is very often a very small price. | colour: --warn]`

---

## Chapter 5 — What dividends alone actually cost (63.6% → 83.4%)

*The title's promise, paid in full. **5.7 lands at 6:08 = 70.7%** — the reward beat, exactly
where the skill says to plant it. This is the honest answer to the phrase six channels built
breakouts on: the index pays about one percent, so dividends-only costs roughly four times
the corpus a total-return withdrawal needs. **5.5 is the second tank callback** and it is
honest: the tank is the same size, but this route may only spend what the tank hands you.
Then rung five, the whole BLS household.*

**5.1**
> Which leaves the question in the title. What if you only spend what the portfolio pays you, and never sell a share?

`[arch: A | img: a hand resting on a closed folder on a desk, hand only | head: THE TITLE QUESTION | stmt: Spend only what it pays. Never sell a share. | colour: --target]`

**5.2**
> That is the dividends-only route, and it is a real strategy with a real price tag.

`[arch: A | img: a paper price tag tied with string, blank face, on a plain surface | head: DIVIDENDS ONLY | stmt: A real strategy. With a real price tag.]`

**5.3**
> Right now the S and P five hundred's dividend yield is about one percent.

`[arch: B | img: a market data screen photographed at a shallow angle, figures illegible | head: TODAY | num: ABOUT 1% | foot: S&P 500 dividend yield, 5 Aug 2026 — multpl 1.04%, GuruFocus 1.082% · two reads, so the VO says "about one percent" | colour: --target]`

**5.4**
> One tracker reads one point zero four, another reads one point zero eight, and July was the lowest on record.

`[arch: C | img: two printed data tables side by side on a desk, different layouts, one row lit on each | head: TWO READS | stmt: 1.04% · 1.082% | foot: multpl.com's own series records 1.08% in July 2026 as the all-time minimum of the 1871 series | colour: --target]`

**5.5**
> Think of it this way — same tank, but now you may only take what it hands you, and that is about one percent.

`[arch: D | img: the 2.2 tank once more, tap barely cracked, a single thin stream into a cup | head: SAME TANK, SMALLER TAP | stmt: Take only what it hands you. About 1%. | colour: --warn | SECOND TANK CALLBACK]`

**5.6**
> So run the same division at one percent, and watch what happens to the number.

`[arch: D | img: a hand turning a single dial on a plain instrument panel, hand only | head: SAME DIVISION | stmt: Change only the rate. | colour: --warn]`

**5.7**
> That same five thousand a month, from index dividends alone at about one percent, needs five point six million dollars.

`[arch: B | img: a bare warehouse floor with a single pallet in the middle of it, wide, hard light | head: THE ANSWER | num: $5,555,556 | foot: AT A 1.08% DIVIDEND YIELD · $60,000 divided by 0.0108 · ILLUSTRATIVE ARITHMETIC | colour: --warn | THE ~70% REWARD BEAT — 6:08 = 70.7%]`

**5.8**
> One and a half million at four percent, or five point six million at about one percent, for the identical paycheck.

`[arch: B | img: two identical envelopes on a table, one thin and one thick, top-down | head: SAME PAYCHECK | stmt: $1,500,000 AT 4.0% · $5,555,556 AT 1.08% | colour: --target]`

**5.9**
> Notice what changed: nothing but the rate, and the same paycheck now costs roughly four times the money.

`[arch: B | img: four identical crates stacked beside one crate, plain wood, hard side light | head: THE GAP | num: ROUGHLY 4 TIMES | foot: The exact ratio is a quotient of two soft decimals, so it is shown rounded and never spoken as a decimal | colour: --warn]`

**5.10**
> Funds built around high-dividend stocks pay more than the index does, at roughly three percent today.

`[arch: B | img: a printed fund factsheet on a desk, corner lifted, all figures out of focus, no logo | head: THE MIDDLE ROUTE | num: ABOUT 3% | foot: A broad US high-dividend-equity ETF, 3.11% trailing-twelve-month yield, stockanalysis.com, 6 Aug 2026 · three published reads span 3.11-3.41%, so the VO says "about three percent" · price evidence for an asset class, not a recommendation | colour: --target]`

**5.11**
> At about three percent, that five thousand a month lands near one point nine million dollars.

`[arch: B | img: a single storage-unit door, roller shutter closed, plain | head: THE MIDDLE PRICE | num: $1,929,260 | foot: AT A 3.11% YIELD · $60,000 divided by 0.0311 · ILLUSTRATIVE ARITHMETIC | colour: --target]`

**5.12**
> Three routes, three rates, one paycheck, and the rate you assume is the entire difference between them.

`[arch: D | img: three parallel painted lanes on asphalt converging at the top of frame | head: THREE ROUTES | stmt: 4.0% · 3.11% · 1.08% | colour: --target]`

**5.13**
> Rung five is the whole month, not one slice of it.

`[arch: A | img: a full month page of a wall calendar, nothing written on it | head: RUNG FIVE | stmt: The whole month.]`

**5.14**
> The average American household spent seventy-eight thousand five hundred thirty-five dollars that year.

`[arch: C | img: a thick statistical release stapled at the corner on a desk, cover page in focus, body illegible | head: THE WHOLE HOUSEHOLD | num: $78,535 | foot: Average annual expenditures per consumer unit, 2024 — BLS Consumer Expenditures, released 19 Dec 2025, USDL-25-1586. Range $35,046 lowest quintile to $150,342 highest | colour: --target]`

**5.15**
> Work it through — that is six thousand five hundred forty-five a month, and at four percent it needs one point nine six million.

`[arch: B | img: a suburban US house seen from the street at dusk, lights on inside, no people | head: RUNG FIVE | num: $1,963,375 | foot: AT A 4.0% WITHDRAWAL RATE · $78,535 divided by 0.04 · ILLUSTRATIVE ARITHMETIC · $6,545 a month | colour: --fund]`

**5.16**
> The same whole month from index dividends alone, at about one percent, is over seven million dollars.

`[arch: B | img: an empty commercial lot behind a chain fence, wide, flat light | head: THE SAME MONTH, DIVIDENDS ONLY | num: $7,271,759 | foot: AT A 1.08% DIVIDEND YIELD · $78,535 divided by 0.0108 · ILLUSTRATIVE ARITHMETIC | colour: --warn]`

---

## Chapter 6 — The day, again (83.4% → 100% · PEAK-END · ONE terminal CTA)

*The rate is not settled and the video says so before it recaps — that admission is the
Von Restorff beat, and it is what stops the ladder reading as a promise. Then the ladder in
one breath, then **the callback** (study conclusion 11: both twins close on the morning, and
B, the higher-reach twin, never recaps at all). 6.11 returns to chapter 1's images — the
silent phone and the single buzz — not to the coffee-and-window version the twins use. One
CTA, at 98.6%, and nothing before it.*

**6.1**
> One more thing about the four percent, because it is not a settled number and nobody should pretend it is.

`[arch: A | img: a single chair in an empty room, hard window light | head: ONE MORE THING | stmt: It is not a settled number. | colour: --warn]`

**6.2**
> Morningstar puts the safe starting rate at three point nine percent for someone retiring in twenty twenty-six.

`[arch: C | img: a research report cover on a desk, title out of focus, a pen across it | head: ONE ANSWER | num: 3.9% | foot: "The State of Retirement Income: 2025 Edition", published 3 Dec 2025, sets the rate for a 2026 retiree — 30-year horizon, 90% success probability, 30-50% equity. Report year is NOT retiree year | colour: --target]`

**6.3**
> Bengen himself moved his own number up to four point seven percent, in a book published in August twenty twenty-five.

`[arch: C | img: a hardback book lying face-down and open on a table, spine up, title not legible | head: ANOTHER ANSWER | num: 4.7% | foot: Bengen's "Universal SAFEMAX", A Richer Retirement, Wiley, August 2025 — a wider asset mix, roughly 400 historical start dates, worst case still October 1968 | colour: --target]`

**6.4**
> And a two thousand ten study found the four percent rule did not hold up across most developed markets.

`[arch: C | img: a folded world map on a desk with one corner turned back, no country legible | head: A THIRD ANSWER | stmt: It did not hold up across most developed markets. | foot: Pfau, "An International Perspective on Safe Withdrawal Rates", Journal of Financial Planning, December 2010 — 50/50 stocks and bills, zero tolerated failure. Japan's sustainable rate was 0.26% | colour: --warn]`

**6.5**
> Same rule, three answers, which is exactly why the rate belongs next to the number every single time.

`[arch: D | img: three price stickers of different sizes on one plain box | head: WHY THE RATE IS ALWAYS SHOWN | stmt: 3.9% · 4.0% · 4.7% | colour: --warn]`

**6.6**
> So here is the ladder in order, all of it at four percent.

`[arch: A | img: a wooden ladder standing against a plain exterior wall, full height, hard shadow | head: THE LADDER | stmt: All of it AT 4.0%. | colour: --fund]`

**6.7**
> At four percent, groceries are a quarter of a million. The car, a third of a million. Housing, two thirds of a million.

`[arch: D | img: three unmarked wooden crates of increasing size in a line on a concrete floor | head: RUNGS ONE TO THREE | stmt: Food $254,225 · Car $332,950 · Housing $656,650 | foot: EACH AT A 4.0% WITHDRAWAL RATE · ILLUSTRATIVE ARITHMETIC | cascade 3 items | colour: --fund]`

**6.8**
> Both at four percent. Five thousand a month, one and a half million. The average household, one point nine six million.

`[arch: D | img: two larger crates continuing the same line, same floor — ONE continuous zoom from 6.7 | head: RUNGS FOUR AND FIVE | stmt: $5,000/mo $1,500,000 · $6,545/mo $1,963,375 | foot: BOTH AT A 4.0% WITHDRAWAL RATE · ILLUSTRATIVE ARITHMETIC | colour: --fund]`

**6.9**
> And that same five thousand a month from index dividends alone, at about one percent, near five point six million.

`[arch: B | img: one crate far larger than all the others, alone in a wide empty bay | head: THE DIVIDENDS-ONLY PRICE | num: $5,555,556 | foot: AT A 1.08% DIVIDEND YIELD · roughly four times the total-return figure · ILLUSTRATIVE ARITHMETIC | colour: --warn]`

**6.10**
> Every one of those is a division, and every one is only as good as the rate sitting beside it.

`[arch: D | img: a pencil resting on a page of handwritten division, figures illegible | head: WHAT THEY ALL ARE | stmt: A division. Only as good as its rate.]`

**6.11**
> Now go back to the day this started on. No alarm, no call from work, and one buzz before noon.

`[arch: A | img: the 1.1 nightstand and the 1.4 phone re-photographed in late-afternoon light, phone face-down again, the day over — a distinct frame, NOT a reuse | head: BACK TO THE DAY | stmt: No alarm. No call. One buzz. | CALLBACK — 96.3%]`

**6.12**
> That number does not buy a lifestyle. It buys back the hours that used to go to the bills.

`[arch: A | img: an empty chair facing a window at first light, wide | head: WHAT IT BUYS | stmt: Not a lifestyle. The hours. | colour: --fund]`

**6.13**
> If the number is less mysterious now, subscribe, because the next one prices the rungs nobody puts on a thumbnail.

`[arch: A | img: a closed notebook and a capped pen on the same table, finished | head: — | num: SUBSCRIBE | foot: The only CTA in the video, at 98.6% | colour: --cta]`

---

## Per-scene timing budget

`chars` → `est s` at **17.57 chars/s** (`format.json cuts.en.chars_per_second`). Add **0.8s
per line** (0.25 lead-in + 0.55 tail, `tiers.medium`) to get scene duration.

| # | chars | est s | | # | chars | est s | | # | chars | est s |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 49 | 2.8 | | 3.1 | 41 | 2.3 | | 5.1 | 115 | 6.5 |
| 1.2 | 75 | 4.3 | | 3.2 | 95 | 5.4 | | 5.2 | 82 | 4.7 |
| 1.3 | 72 | 4.1 | | 3.3 | 116 | 6.6 | | 5.3 | 73 | 4.2 |
| 1.4 | 94 | 5.4 | | 3.4 | 113 | 6.4 | | 5.4 | 109 | 6.2 |
| 1.5 | 54 | 3.1 | | 3.5 | 101 | 5.7 | | 5.5 | 106 | 6.0 |
| 1.6 | 80 | 4.6 | | 3.6 | 102 | 5.8 | | 5.6 | 78 | 4.4 |
| 1.7 | 118 | 6.7 | | 3.7 | 105 | 6.0 | | 5.7 | 119 | 6.8 |
| 1.8 | 127 | 7.2 | | 3.8 | 109 | 6.2 | | 5.8 | 115 | 6.5 |
| 2.1 | 82 | 4.7 | | 3.9 | 113 | 6.4 | | 5.9 | 104 | 5.9 |
| 2.2 | **155** | **8.8** | | 3.10 | 54 | 3.1 | | 5.10 | 101 | 5.7 |
| 2.3 | 131 | 7.5 | | 3.11 | 99 | 5.6 | | 5.11 | 93 | 5.3 |
| 2.4 | 56 | 3.2 | | 3.12 | 101 | 5.7 | | 5.12 | 103 | 5.9 |
| 2.5 | 109 | 6.2 | | 3.13 | 91 | 5.2 | | 5.13 | 50 | 2.8 |
| 2.6 | 113 | 6.4 | | 3.14 | 107 | 6.1 | | 5.14 | 103 | 5.9 |
| 2.7 | 118 | 6.7 | | 3.15 | 95 | 5.4 | | 5.15 | 128 | 7.3 |
| 2.8 | 101 | 5.7 | | 3.16 | 54 | 3.1 | | 5.16 | 101 | 5.7 |
| 2.9 | 108 | 6.1 | | 4.1 | 117 | 6.7 | | 6.1 | 106 | 6.0 |
| 2.10 | 118 | 6.7 | | 4.2 | 108 | 6.1 | | 6.2 | 110 | 6.3 |
| 2.11 | 119 | 6.8 | | 4.3 | 100 | 5.7 | | 6.3 | 117 | 6.7 |
| 2.12 | 109 | 6.2 | | 4.4 | 87 | 5.0 | | 6.4 | 103 | 5.9 |
| 2.13 | 107 | 6.1 | | 4.5 | 81 | 4.6 | | 6.5 | 101 | 5.7 |
| 2.14 | 116 | 6.6 | | 4.6 | 108 | 6.1 | | 6.6 | 58 | 3.3 |
| 2.15 | 100 | 5.7 | | 4.7 | 71 | 4.0 | | 6.7 | 119 | 6.8 |
| | | | | 4.8 | 88 | 5.0 | | 6.8 | 119 | 6.8 |
| | | | | 4.9 | 89 | 5.1 | | 6.9 | 114 | 6.5 |
| | | | | 4.10 | 114 | 6.5 | | 6.10 | 94 | 5.4 |
| | | | | 4.11 | 128 | 7.3 | | 6.11 | 94 | 5.4 |
| | | | | 4.12 | 105 | 6.0 | | 6.12 | 90 | 5.1 |
| | | | | 4.13 | 92 | 5.2 | | 6.13 | 114 | 6.5 |

**81 lines · 8,014 chars · 456.1s VO · +64.8s padding · 520.9s (8:41).**
Char counts are a hand-budget estimate (±2%); the build step recounts them programmatically
from the extracted lines file, then ffprobe-measures every clip.

---

## Fact trace (every number → facts-staging.md)

| Number / claim in script | Where | facts-staging.md row | Tag |
|---|---|---|---|
| **Bengen 1994** — author, journal, month, volume, pages | 2.5 | **A.1** row 1 | **HARD** on author/journal/date. The 1994 paper itself was NOT read (FPA PDF 403'd); the VO claims only what the review establishes. |
| **50/50 stocks and bonds**, start years from 1926 | 2.6 | **A.1** row 2 | **HARD** |
| **Trinity 1998** — three professors, February 1998 | 2.7 | **A.1** row 4 | **HARD (primary, read direct)**. The **AAII** initialism is on screen only — an initialism is the same coin-flip TTS risk as a bare digit. |
| **95%** survival, 4.0%, inflation-adjusted, 30-year payout | 2.8 | **A.1** row 6 — Trinity Table 3 | **HARD.** 95% is the figure at 100% stocks *and* at 50/50; the foot names both so the number is not floating free of an allocation. |
| **4.0%** as the working rate | 2.3, 2.9 and every rung | **A.1** | **HARD.** Framed as "a finding with a date, not a promise" — this is what satisfies `no_return_promise` by construction. |
| **$10,169** food · **$847**/mo · **$254,225** at 4.0% | 2.11, 2.12, 2.13, 2.14 | **C.2** BLS CE 2024 row ÷ **A.1** rate | numerator **HARD** (BLS's own figure on three BLS surfaces; not read direct — same posture as the BLS weekly-earnings row already banked). Quotient **COMPUTED**, labelled ILLUSTRATIVE on screen, rate in frame and in the line. |
| **$13,318** transportation · **$1,110**/mo · **$332,950** at 4.0% | 3.2, 3.3, 3.4 | same | same |
| **$26,266** housing · **33.4%** share · **$2,189**/mo · **$656,650** at 4.0% | 3.6, 3.7, 3.8 | same | same. 50.4% (housing + transport) is on screen only. |
| **"did not adjust for taxes or transaction costs"** | 3.11 | **A.2** row 1 | **HARD (primary, self-stated)** — verbatim from Trinity's own methodology. |
| **Built for 30 years** · payout periods 15/20/25/30 | 3.13 | **A.2** row 2 + **A.1** row 5 | **HARD (primary)** |
| **"Early retirees… should plan on lower withdrawal rates"** | 3.14, 3.15 | **PART D** — the only sourced early-retirement statement that exists, and it is a limit | **HARD (primary)**. Verbatim, attributed on screen. |
| **$5,000/mo = $60,000/yr** worked figure | 4.1 | **C.3** preamble — chosen deliberately *below* the BLS $6,545/mo average | **CONVENTION**, and the foot says why on screen. |
| **$1,500,000** at 4.0% | 4.2, 4.3, 5.8, 6.8 | **C.3** row 1 | **COMPUTED** from a HARD rate. "$1.5M at 4%" is arithmetic; "$1.5M" alone would be a fabricated promise. |
| **Yield = payout ÷ price** | 4.9, 4.10 | definitional, no figure attached | — |
| **13.84%**, June 1932 · long-run mean **4.21%** / median **4.19%** since 1871 | 4.11 (13.84% spoken; the mean and median are **screen-only**, in the foot), 4.12 | **C.2** row 2 | **HARD** (multpl, read direct). The 4.21% mean was spoken on attempt 1 and is now screen-only: two different "four percents" in one chapter is exactly the yield/withdrawal-rate conflation the study caught twin B making. The fact is not dropped, it is moved to the frame. |
| **About 1%** today · 1.04% / 1.082% · July 2026 all-time minimum | 5.3, 5.4 | **C.2** row 1 | **HARD on "about one percent"** · SOFT on the decimal → VO says "about", the screen carries both reads and names both sources. |
| **$5,555,556** at 1.08% | 5.7, 5.8, 6.9 | **C.3** row 5 | **COMPUTED**, ILLUSTRATIVE on screen, yield in frame and in the line. **This is the video's answer to its own title.** |
| **Roughly four times** | 5.9 | **C.3** closing note — $5.6M ÷ $1.5M = 3.7× | **COMPUTED from two SOFT decimals**, so it is *shown* rounded and **never spoken as "three point seven"**, exactly as staged. The multiplication glyph is absent from the font subset, so the screen reads `ROUGHLY 4 TIMES`. |
| **About 3%** dividend-fund yield · **$1,929,260** | 5.10, 5.11 | **C.2** row 3 + **C.3** row 4 | **HARD on "about three percent"** (three reads span 3.11–3.41%) · SOFT on the decimal. The ticker is **not** on screen and **not** in the VO — the foot describes the asset class and names the data source. |
| **$78,535** · **$6,545**/mo · **$1,963,375** at 4.0% · **$7,271,759** at 1.08% | 5.14, 5.15, 5.16, 6.8 | **C.2** BLS row + **C.3** rows 1 and 5, right-hand column | numerator **HARD**, quotients **COMPUTED**, both labelled |
| **3.9%**, Morningstar, for a **2026 retiree** | 6.2 | **A.2** row 3 | **HARD** (three independent agree). ⚠ The staged naming trap is obeyed: the screen says "for a 2026 retiree" and the foot says the report is the *2025 Edition*, published 3 Dec 2025. Never "Morningstar 2025 says 3.9%". |
| **4.7%**, Bengen's own revision, August 2025 | 6.3 | **A.2** row 5 | **HARD** (four independent outlets). The revision moved the rate **up**; the "4% rule is dead" headline framing is rejected in **PART E** and is not used. |
| **Did not hold up across most developed markets** · **Japan 0.26%** (screen only) | 6.4 | **A.2** row 4 + the ⚠ CONFLICT note | **HARD on the shape.** The staged conflict is obeyed exactly: **no country count is spoken or shown** (17/109 vs 19/1900–2010 disagree across surfaces), and Japan's 0.26% is the only country decimal used, because it is the only one both surfaces agree on. |
| **The tank** (2.2, 4.7, 4.8, 5.5, 4.13) | — | **not a fact — an analogy** | It carries no figure and asserts no measurement. Its one claim is definitional: the safe-withdrawal question *is* "how much can be drawn per year without exhausting the portfolio". Where a tank image appears beside a figure, the figure and its rate come from the rows above. |

### The rate-in-the-VO check, line by line (attempt 1's three misses are fixed)

fin-audit found three lines where the *frame* carried the rate and the *spoken sentence* did
not — old 5.6, 6.7, 6.8. Every corpus and derived-income line in this draft was re-read one
at a time against `withdrawal_rate_on_screen` and its 2026-08-07 `derived_income_carries_assumption`
extension:

| line | the figure | the rate, spoken in the same line |
|---|---|---|
| 2.13 | $254,225 | "Divided by four percent" |
| 2.14 | $254,225 | "drawn at four percent a year" |
| 3.4 | $332,950 | "Divided by four percent" |
| 3.8 | $656,650 | "Divided by four percent" |
| 4.2 | $1,500,000 | "divided by four percent" |
| 4.3 | $1,500,000 → $5,000/mo | "at a four percent withdrawal rate" — **the derived income too** |
| 5.7 | $5,555,556 | "at about one percent" ← *old 5.6, was bare* |
| 5.8 | $1,500,000 and $5,555,556 | "at four percent" and "at about one percent" |
| 5.11 | $1,929,260 | "At about three percent" |
| 5.15 | $1,963,375 | "at four percent" |
| 5.16 | $7,271,759 | "at about one percent" |
| 6.7 | $254,225 · $332,950 · $656,650 | "At four percent" opens the line ← *old 6.7, was bare* |
| 6.8 | $1,500,000 · $1,963,375 | "Both at four percent" opens the line ← *old 6.8, was bare* |
| 6.9 | $5,555,556 | "at about one percent" |

Fourteen lines, fourteen rates. 6.7 speaks its rungs as fractions ("a quarter of a million")
while the frame carries the exact figures — deliberate, because the digit-soup alternative is
unlistenable and this is the third recorded ASR digit-loss lane; fin-audit should confirm the
rounding reads as rounding and not as a new claim.

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **Every figure in PART B.** This is the US cut. The Indian instruments, schemes, rates,
  research and currency appear nowhere — not in a VO line, not in a cue, not in a
  photograph. **PART F forbids cross-market arithmetic**, so there is no conversion, no
  shared axis and no "which is about" anywhere in this file.
- **India's 3.0–3.5% withdrawal band (A.3).** Correct for the other cut, wrong here; the
  currency firewall says the two rate sets "differ on three axes at once" and are not
  transferable.
- **The 4.21% long-run mean yield, spoken.** Kept on screen at 4.11, cut from the VO. See
  the fact-trace row: a spoken "a little over four percent" fifteen seconds after a spoken
  four percent withdrawal rate is the conflation twin B shipped.
- **The 5% and 3.5% Bengen outcomes** (5% → as short as 20 years; 3.5% → always ≥50 years).
  Real, HARD, and cut for time — the 30-year-horizon limit at 3.13 makes the same point with
  a primary quotation attached, and stacking a third rate before 6.2 would blunt the "three
  answers" beat.
- **Trinity's other allocation rows** (98% at 75/25, 71% at 25/75, 20% at 100% bonds). Using
  only the strongest row would be cherry-picking, and using all five needs a chart this
  runtime cannot afford. 2.8 states the row it uses and the foot names the allocation.
- **A VYM yield.** `facts-staging.md` marks the row **NOT USABLE — do not put a VYM yield on
  screen** (Vanguard returned no fund data). It is absent.
- **Any ticker on screen or in the VO.** SCHD is the source of the "about three percent" row
  and is recorded in this trace table, which is not on screen. The frame describes the asset
  class. Per the japanese-money-methods audit precedent, a disclaimer under a recommendation
  is still a recommendation — so there is no recommendation to disclaim.
- **Northwestern Mutual's "$1.46 million".** Twin B's only citation, at ~90% of its runtime.
  It is a **competitor's claim**, not a staged fact, and the study note says it must be
  re-sourced from Northwestern Mutual directly or dropped. It was not staged, so it is
  dropped.
- **Twin B's "under $50,000 in dividends, the IRS takes nothing"** and twin A's US/UK
  withholding-tax claims. All flagged in the study as needing independent sourcing; none was
  staged. No tax rate appears in this script — 3.12 says only that every rung is a
  before-tax number, which is what Trinity itself says.
- **"The principal keeps growing" / "forever" / "without selling a single share" as a
  promise.** Both twins say some version; it is a capital-preservation promise the 4% rule
  does not make. 5.1 states the never-sell condition as *the viewer's question*, and 5.7
  prices it — it is never asserted as an outcome.
- **US personal saving rate (2.7%), median household income ($83,730), median weekly
  earnings ($1,251), the Fed funds range.** All staged, all HARD, none needed — the argument
  is a division, and every extra macro figure competes with the five rungs for the same
  attention.
- **Any age, anywhere.** No rung carries one, no line converts a corpus into one, and twin
  A's *"financially free at 50"* has no analogue in this file.

---

## Build handoff

1. **`assets/voice/english-lines.json` = 81 entries keyed `1.1 … 6.13`**, containing **only**
   the `>` VO strings above — no markdown, no cue text, no on-screen text. **Slice the
   source file; never retype.** Gate the extraction with a byte-for-byte reconstruction check
   against this file before generating audio (`long_form_scripting.md` §1.7). ⚠ This file
   carries ~40 guard blockquotes against 81 VO lines, so a bare `^> ` grep sweeps in junk —
   extract by the `**N.M**` line key, exactly as the hi cut's fin-voice did.
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb` (Brian),
   `eleven_multilingual_v2`, style 0. **81 clips.** `run.json budget.max_elevenlabs_calls`
   is 350 and `elevenlabs_calls` stands at 156 — the attempt-1 Brian clips are dead (right
   voice, wrong script) and must be regenerated, not reused. Bump the counter after the run.
3. **Timing is by construction.** One line = one clip = one scene. MEDIUM charges
   `lead_in_seconds 0.25` + `tail_seconds 0.55` per line (`format.json tiers.medium`) — **not**
   the `scene.*` 0.4/1.0 defaults, which are tuned for SHORT's nine lines. Never hand-edit a
   duration; regenerate all four homes of the timing numbers from one source.
4. **Recount the characters programmatically** before reacting to any drift. Budget formula:
   `(510 − lines × 0.8) × 17.57`. **No line may exceed 144 characters** except 2.2 — see 6.
5. **Measure the delivered flat rate after TTS** (total chars ÷ total audio seconds) and put
   it in the build log. `cuts.en.chars_per_second` is now 17.57, a mean of three measurements
   including this cut's own attempt-1 audio at 17.588; a fourth measurement belongs in the
   key **with the measurement beside it**, not in a re-padded script.
6. **⚠ Scene 2.2 runs 9.6s and needs TWO `data-framings`** — wide on the tank, then a push to
   the tap. It is the only scene over `max_scene_seconds` 9.0, it is a creator-approved
   verbatim line, and a single framing there will fail `check_build`. The 2.2 tank is
   re-photographed at **4.7, 4.8 and 5.5** — those are *different frames of the same object*
   (tap closed / tap wide open / tap barely cracked), never the same file re-used, and the
   sound-off test is what they have to pass: tap position alone must say the beat.
7. **Images: one per line, 81 scenes, zero photo-free frames** (`photo_free_scene_ratio` = 0,
   creator rule 2026-07-28), and each must pass the **sound-off test per line**. Two pairs
   are holds — **1.3→1.4** and **6.7→6.8** — and each must run **ONE continuous zoom across
   both scenes**, never a self-dissolve (creator rule, firaun 2026-07-23); give the second
   scene a tighter crop of the same source so no framing holds past 9.0s. **6.11 deliberately
   re-photographs the 1.1 nightstand and 1.4 phone in later light** — a callback, not a
   reuse; shoot/source it as a distinct frame.
8. **Localisation sweep.** Every frame is American. Sweep every photo for non-US currency,
   signage, plugs, licence plates and vehicles — a euro coin and a Swiss franc shipped in the
   first `-en` cut. The 1930s archival frames (4.11, 4.12) must be US archival. md5 the asset
   ledger: no image may repeat across videos or channels.
9. **⚠ THE FONT SUBSET.** `tools/scaffold/assets/fonts/NotoSansFinance-var.woff2` carries
   **97 codepoints**: `>` `→` `▶` `×` `≈` `~` are absent. Already obeyed in every cue above —
   `ROUGHLY 4 TIMES` not a multiplication glyph, `ABOUT 1%` not a tilde, `DIVIDED BY` not a
   solidus, `·` as the separator, and **no question mark in any on-screen string** (2.2's
   tank line is set as a statement for exactly this reason). Verify every on-screen string
   against a dumped `subset.txt` before render.
10. **The rate is in the frame on every corpus scene.** 2.13, 2.14, 3.4, 3.8, 4.2, 4.3, 5.7,
    5.8, 5.11, 5.15, 5.16, 6.7, 6.8, 6.9 — fourteen frames, and a build that drops the
    `foot:` from any one of them breaks `run.json.constraints.withdrawal_rate_on_screen`.
    4.3 also carries a **derived income** ($5,000/mo) and is covered by the same assert per
    the 2026-08-07 `derived_income_carries_assumption` extension. This is the one thing
    `fin-audit` hard-fails.
11. **Anchor cues to word-level timings** (faster-whisper), not character-offset
    interpolation. `first_cue_by_seconds` 0.5, `cue_min_gap_seconds` 0.8,
    `max_simultaneous_elements` 6, `max_chips_per_row` 3, `max_chip_chars` 22.
12. **Lottie candidates** (`vector_art.reach_for_it_when` — a beat a photograph cannot state;
    cap 4 per chapter): **1.4** one notification arriving, no figure on the card · **2.2 /
    4.7 / 5.5** the tank at three tap positions, which is the cut's spine and worth drawing
    once and re-cutting three times · **4.10** payout over price with the price falling on
    its own · **5.9** four crates against one · **5.12** three lanes at three rates ·
    **6.7/6.8** the five-rung ladder assembling. Search the library first
    (`tools/lottie/search.py`) — `phone-notify-credit`, `two-rates-30x` and `stats-table-row`
    already exist and may re-cut. Tint is required. **Nothing drawn may read as a
    measurement**: the tank's level line is decorative and carries no figure.
13. **Chapter-wise production.** Build, proof and re-render chapter by chapter; concat and
    final-render only after all six chapters are locked. Encode with an explicit
    `-o renders/FINAL-1080p-en.mp4`.
14. **Captions.** Narration MD + `.srt` per cut via `tools/transcript.py` — join, never
    retype (creator rule 2026-08-06). Burn subtitles into every frame.
