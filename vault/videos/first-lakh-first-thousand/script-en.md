---
summary: US/English script for «The first $10,000 is the hardest». MEDIUM tier, per-line chapter architecture — 92 single-sentence VO lines across 9 chapters, ~7,657 chars ≈ 8:19 vs the 510s target. USD only. A US rewrite of the Hindi cut's spine, not a translation. On-screen text English, swiss-band. Every number traces to videos/first-lakh-first-thousand/facts-staging.md §2.
updated: 2026-07-31
source: run.json creator brief (2026-07-31) + facts-staging.md §2 (USA block, attempt 1) + study note knowledge/video-studies/first-lakh-first-thousand.md + knowledge/us-english-script-style.md. Architecture swiss-band per run.json creator pick; layout spec from knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md Direction 1.
stage: fin-script, cut en, attempt 1
---

# «The First $10,000» — US / English edition (MEDIUM, per-line chapters)

**Studio project (to build):** `studio/videos/first-lakh-first-thousand-en`
**Language:** US English. **Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`,
`eleven_multilingual_v2`, style 0.
**On-screen text:** English, US comma grouping (`$10,000`, `$100,000`).
**Architecture:** `swiss-band` (run.json creator pick), **MEDIUM tier → per-line chapters**.
**Tier note:** none of the 9-segment blockframe constants apply here. `lines: 9` on the
`swiss-band` registry entry is a SHORT-tier constant. Scene count is emergent from the
script: **one line = one TTS clip = one scene = one exact timeline anchor.**

**Engine rule:** digits are **spelled out** in every VO line below (bare Latin digits are
a coin-flip reading in ElevenLabs). On-screen numerals carry the exact figures.

**Persona rules (YouTube 2026 AI carve-out):** no host persona, no first-person
expertise, no fund/stock/product pick. The savings-account rate, the high-yield
comparison and the Fed's target range appear **only as price evidence** — "this is what
the rate is" — never as "put your money here". Second person throughout; "I" appears in no VO
line — only in the Chapter 6 title, where it quotes the viewer's objection.

---

> ### ⚠ THE SIX THINGS THAT MUST NOT ENTER THIS CUT
> Numbers 1–5 are named in `facts-staging.md` §2/§4 as the traps for this exact topic.
> 1. **NEVER a rupee, a lakh, or any cross-market equivalence.** `$10,000` is not
>    one lakh and no line may imply it (staging's Currency Firewall). The rupee glyph
>    (U+20B9) appears nowhere in this file — not in a claim ID, and not in this
>    warning, which is why it is named here in words rather than written out.
> 2. **NEVER a specific APY on screen.** The top high-yield figure (~4.15%, Bankrate,
>    SOFT) is **context only, never on screen** and never spoken. The durable claim is
>    "roughly **ten times** a typical savings account" — a ratio, not a rate. The FDIC
>    **national rate** 0.38% is a regulator-published statistic, not a product offer, and
>    is the one rate this cut shows.
> 3. **NEVER a decimal on the market return.** Say "about ten percent a year", show
>    `~10%/yr`. §2.2 tags every cited decimal (10.69 / 10.33 / 10.59 / 10.3) SOFT and
>    conflicting — shape only.
> 4. **NEVER a date or venue on the Munger line.** "In 1994, at the Berkshire meeting…"
>    is folk attribution; no primary was reachable. Paraphrase only, no year on screen,
>    and the profanity is dropped for a monetised cut.
> 5. **NEVER a months-to-milestone figure spoken as a statistic.** Every integer in §2.3
>    is model output. Each spoken figure carries its condition in the same sentence, every
>    math frame carries the `ILLUSTRATIVE · $800/mo · monthly compounding` foot, and 2.8
>    says it out loud in the VO.
> 6. **NEVER "$800 a month is what Americans save."** It is twenty percent of the locked
>    $4,000 worked example — a split, not a statistic. Chapter 6 exists to say so, and
>    the BEA's actual national figure (2.7%) is in the video as the *contrast*.

---

## Title options (English — both cuts, unchanged channel rule)

1. **The First $10,000 Is The Hardest — Here's The Actual Math** *(recommended —
   keyword front-loaded, and the hook figure is the first thing in the title)*
2. $10,000 In 12 Months. $10,000 In 6. Same Person, Same Market.
3. Why Your First $10,000 Has Almost Nothing To Do With The Market

---

## Chapters (ship these as YouTube chapters — study conclusion 7)

| # | Chapter | starts | lines |
|---|---|---|---|
| 1 | The first $10,000 — 12.5 months vs 6 | 0:00 | 10 |
| 2 | Why one hundred percent of it is you | 0:52 | 10 |
| 3 | The tenth $10,000 — the visible sum | 1:47 | 10 |
| 4 | Savings rate beats return rate | 2:40 | 11 |
| 5 | **The crossover — and why Munger said $100,000** | 3:43 | 11 |
| 6 | "But I can't save $800" | 4:41 | 10 |
| 7 | **The fire pit** (the ~70% re-frame) | 5:38 | 8 |
| 8 | How the first $10,000 actually gets built | 6:21 | 12 |
| 9 | Do this today + recap | 7:26 | 10 |

---

## Timing budget

US-English narration ≈ **16.1 chars/s** (`format.json cuts.en.chars_per_second` — the
measured figure across the shipped `-en` cuts, not the retired 15.0 estimate). Char counts
below are the **budget estimate (±10%)**; the build step recounts them programmatically
from the extracted lines file and then ffprobe-measures every clip. Gap model (firaun
`build.py`): **0.2s intra-chapter**, **0.8s at a chapter boundary**.

| Ch | lines | chars | VO | + gaps | chapter runtime |
|---|---|---|---|---|---|
| 1 | 10 | ~789 | 49.0s | 2.6 | 51.6s |
| 2 | 10 | ~848 | 52.7s | 2.6 | 55.3s |
| 3 | 10 | ~818 | 50.8s | 2.6 | 53.4s |
| 4 | 11 | ~960 | 59.6s | 2.8 | 62.4s |
| 5 | 11 | ~896 | 55.7s | 2.8 | 58.5s |
| 6 | 10 | ~874 | 54.3s | 2.8 | 57.1s |
| 7 | 8 | ~657 | 40.8s | 2.2 | 43.0s |
| 8 | 12 | ~1,003 | 62.3s | 3.0 | 65.3s |
| 9 | 10 | ~812 | 50.4s | 1.8 | 52.2s |
| | **92** | **~7,657** | **~475.6s** | **~23.2s** | **~498.8s** |

**Budget check:** 510s × 16.1 = **8,211 char budget**; this draft is **~7,657 (−6.7%)**.
Estimated runtime **~499s (8:19) vs the 510s target — 2.2% under.** Deliberately the same
margin the Hindi cut carries, so the pair ships at matched length; the per-line gap model
is a floor, not a ceiling, and English TTS at 16.1 chars/s is a *measured* rate that has
run slightly slow on one of the two shipped cuts.

**Pace:** ~498s / 92 scenes = **5.4s average scene**, against `scene.target_scene_seconds`
6.5 and `scene.max_scene_seconds` 9.0. Brisker than the Hindi cut's 5.8s — English carries
more information per second, so the same argument needs more frames, which is the correct
direction for a topic the study says died on static holds. The longest line (7.7, 127
chars ≈ 7.9s) is the only scene above 7.5s and is safely under 9.0. The shortest (5.3,
22 chars ≈ 1.4s) is above `tts.min_clip_seconds` 1.0.

**Why 92 lines and not the 78 in `format.json tiers.medium.lines`:** that 78 is 510 ÷ 6.5,
and `format.json scene._scene_seconds_note` is explicit that scene count is **emergent
from the script, never a constant**.

⚠ **ElevenLabs budget.** 86 (hi) + 92 (en) = **178 of the run's 200 calls**, leaving 22
for retries across both cuts. That is tight but sufficient. `fin-voice` must not re-cut a
whole chapter casually; regenerate single failed clips only.

---

## Per-scene timing budget

`ap` = aperture (see the sequence layer below). B = band · C-R/C-L = picture column,
photo right/left · R = reversed field · M = mosaic (major + minor).

| # | chars | est s | ap | | # | chars | est s | ap |
|---|---|---|---|---|---|---|---|---|
| 1.1 | 88 | 5.5 | B | | 5.1 | 69 | 4.3 | B |
| 1.2 | 89 | 5.5 | B | | 5.2 | 86 | 5.3 | B |
| 1.3 | 75 | 4.7 | M | | 5.3 | 22 | 1.4 | B *(hold)* |
| 1.4 | 108 | 6.7 | C-R | | 5.4 | 117 | 7.3 | C-L |
| 1.5 | 82 | 5.1 | R | | 5.5 | 77 | 4.8 | M |
| 1.6 | 52 | 3.2 | B | | 5.6 | 111 | 6.9 | R |
| 1.7 | 79 | 4.9 | B | | 5.7 | 57 | 3.5 | B |
| 1.8 | 66 | 4.1 | C-L | | 5.8 | 121 | 7.5 | B |
| 1.9 | 75 | 4.7 | B | | 5.9 | 76 | 4.7 | C-R |
| 1.10 | 75 | 4.7 | B | | 5.10 | 93 | 5.8 | R |
| 2.1 | 87 | 5.4 | B | | 5.11 | 67 | 4.2 | B |
| 2.2 | 78 | 4.8 | C-R | | 6.1 | 66 | 4.1 | B |
| 2.3 | 80 | 5.0 | B | | 6.2 | 102 | 6.3 | B |
| 2.4 | 118 | 7.3 | B | | 6.3 | 99 | 6.1 | C-L |
| 2.5 | 40 | 2.5 | B | | 6.4 | 76 | 4.7 | B |
| 2.6 | 115 | 7.1 | M | | 6.5 | 100 | 6.2 | B |
| 2.7 | 68 | 4.2 | B | | 6.6 | 98 | 6.1 | B |
| 2.8 | 85 | 5.3 | B | | 6.7 | 84 | 5.2 | M |
| 2.9 | 104 | 6.5 | R | | 6.8 | 84 | 5.2 | B |
| 2.10 | 73 | 4.5 | C-L | | 6.9 | 79 | 4.9 | C-R |
| 3.1 | 87 | 5.4 | B | | 6.10 | 86 | 5.3 | B |
| 3.2 | 89 | 5.5 | M | | 7.1 | 57 | 3.5 | B |
| 3.3 | 56 | 3.5 | B | | 7.2 | 56 | 3.5 | B |
| 3.4 | 81 | 5.0 | C-R | | 7.3 | 94 | 5.8 | C-L |
| 3.5 | 87 | 5.4 | B | | 7.4 | 81 | 5.0 | B |
| 3.6 | 82 | 5.1 | B | | 7.5 | 78 | 4.8 | B |
| 3.7 | 89 | 5.5 | B | | 7.6 | 82 | 5.1 | R |
| 3.8 | 104 | 6.5 | R | | 7.7 | 127 | 7.9 | B |
| 3.9 | 81 | 5.0 | M | | 7.8 | 82 | 5.1 | B |
| 3.10 | 62 | 3.9 | C-L | | 8.1 | 72 | 4.5 | B |
| 4.1 | 74 | 4.6 | B | | 8.2 | 86 | 5.3 | C-R |
| 4.2 | 94 | 5.8 | B | | 8.3 | 87 | 5.4 | B |
| 4.3 | 112 | 7.0 | C-R | | 8.4 | 59 | 3.7 | B |
| 4.4 | 74 | 4.6 | B | | 8.5 | 82 | 5.1 | B |
| 4.5 | 76 | 4.7 | B | | 8.6 | 93 | 5.8 | B |
| 4.6 | 72 | 4.5 | B | | 8.7 | 81 | 5.0 | C-L |
| 4.7 | 82 | 5.1 | C-L | | 8.8 | 118 | 7.3 | B |
| 4.8 | 106 | 6.6 | M | | 8.9 | 73 | 4.5 | B |
| 4.9 | 93 | 5.8 | R | | 8.10 | 65 | 4.0 | B |
| 4.10 | 113 | 7.0 | B | | 8.11 | 89 | 5.5 | C-R |
| 4.11 | 64 | 4.0 | C-R | | 8.12 | 98 | 6.1 | R |
| 9.1 | 47 | 2.9 | B | | 9.6 | 68 | 4.2 | M |
| 9.2 | 93 | 5.8 | C-L | | 9.7 | 99 | 6.1 | B |
| 9.3 | 95 | 5.9 | B | | 9.8 | 94 | 5.8 | R |
| 9.4 | 59 | 3.7 | B | | 9.9 | 51 | 3.2 | B |
| 9.5 | 122 | 7.6 | B | | 9.10 | 84 | 5.2 | B |

---

## The swiss-band spec, as this script uses it

Direction 1 of `knowledge/finance-audit-2026-07-29/11-swiss-vignelli.md`. Load-bearing
constraints the on-screen blocks below already obey:

- **Two type sizes per scene.** Every scene is `bar:` (84px/800, reversed in the black
  title bar) + **one** of `stmt:` (54px/500, hung from the 3px rule at y=780) or `num:`
  (200px/900, tabular, hung from the same rule). A `foot:` (26px/200 `--muted`) is the
  permitted third size and carries the source / the illustrative label.
- **Never a bar + a heading + a subhead in one frame.** No chip rows, no bulleted rows,
  no enumerated lists.
- **Flush left, squared corners, no scrim, no `text-shadow`, no per-scene `--tint`,
  no rotation.**
- **One role colour per scene, ever.** This video's semantics:
  `--warn` red = **the stretch nobody helps you with** (the first $10,000, the 12.5
  months, the half-month the market buys, the 2.7% national rate, the one emergency) ·
  `--fund` green = **the mechanism that works without you once it exists** — the standing
  transfer, the escalator, the habit, the coal bed, the tenth $10,000 ·
  `--target` amber = **a rate or a threshold under examination** (~10%/yr, 0.38%, the
  Fed range, the $96,000 crossover, $100,000) · `--pop` orange = the CTA block, **once**,
  at 9.9.
  ⚠ Same audit note as the Hindi cut: green is **not** "returns doing the work". It marks
  the mechanism the viewer installs. 5.10 exists specifically to deny that returns take
  over at the first milestone; reading green as "returns" would make the palette argue
  against the video's thesis.
- **Ken Burns at half amplitude** inside the band (`1.0 ↔ 1.06`, `xPercent ∓1.2`),
  alternating direction per scene. Boundary = **hard directional wipe, 0.45s** (same
  duration as the dissolve it replaces — `scdet` must be re-measured, §9 of the design note).

### The sequence layer (the anti-sameness engine — mandatory, not optional)

Canon p.84: a fixed system with a **declared cycle of apertures**, never one frame
repeated.

- **BAND (D1) is the default** and carries 57 of 92 scenes (62%).
- **COLUMN (D2)** on 18 scenes, alternating photo side **starting C-R**, so the swap
  reads as a rhythm across the whole video.
- **REVERSED FIELD (D4)** on exactly **9 scenes**, all marked `R` — the hardest-milestone
  line (1.5), the thesis (2.9), the sentence the video is named for (3.8), the
  only-thing-that-moved line (4.9), the ten-times-further line (5.6), the habit correction
  (5.10), the coal bed (7.6), how it actually breaks (8.12) and the closing statement
  (9.8). Reversed type only where the image's left third measures below 25% luminance —
  **measure it, do not assume it**.
- **MOSAIC (D3)** on the 8 scenes carrying a two-figure comparison (1.3, 2.6, 3.2, 3.9,
  4.8, 5.5, 6.7, 9.6). Major rectangle = photo, minor rectangle = the second figure.
- **Cycle offset varies by video.** The Hindi cut opens on `R`; **this cut opens on `B`**
  and its first `R` is scene five. Do not sync the two cuts' aperture cycles — that is
  the one thing that would make the pair read as one template with the language swapped.

---

# THE SCRIPT

> **VO block rule.** Every `>` quoted line **inside a `**N.N**` block** is a VO line,
> verbatim, and is the only thing that goes to TTS. Everything in backticks is a
> production cue and never spoken. Key the extraction off the `**N.N**` headers — a naive
> `grep '^>'` would ship the warning admonition above to ElevenLabs and burn calls
> (the hazard fin-audit found on the Hindi cut). Gate it with a byte-for-byte
> reconstruction check.

---

## Chapter 1 — The first $10,000 (HOOK · cold open on the number)

*Study conclusion 1: the first sentence carries the number, and the payoff figure lands
inside ~8 seconds. No greeting, no title card, no roadmap before the number — the study's
LOW pick opened on a 15-second static title card and did 0.048× subs.*

**1.1**
> Eight hundred dollars a month. The first ten thousand dollars: twelve and a half months.

`[ap B | img: a chipped enamel coffee mug on a kitchen counter, loose quarters and folded bills inside, hard morning window light | bar: THE FIRST $10,000 | num: 12.5 MONTHS | foot: ILLUSTRATIVE · $800/mo · 0% return · monthly compounding | colour: --warn]`

**1.2**
> The same eight hundred a month, from ninety thousand to one hundred thousand: six months.

`[ap B | img: a large glass jar filled to the neck with bills and coins, same counter, later light | bar: THE TENTH $10,000 | num: 6 MONTHS | foot: ILLUSTRATIVE · $800/mo · ~10%/yr · monthly compounding | colour: --fund]`

**1.3**
> Same person, same paycheck, same market. Twelve and a half months, and six.

`[ap M | major: two identical cast-iron weights on a hardware-store scale; minor: a folded pay stub | bar: SAME $800 | stmt: 12.5 months → 6 months | colour: --warn]`

**1.4**
> The only thing that changed is that the second time, ninety thousand dollars was already standing behind it.

`[ap C-R | img: two ledger binders on a shelf, one thin and one thick, spines to camera | bar: WHAT CHANGED | stmt: The second time, $90,000 was already standing behind it | foot: Illustrative model — same monthly amount, same rate]`

**1.5**
> That is why the first ten thousand is the hardest ten thousand you will ever save.

`[ap R | img: a single quarter standing on edge on a bare wood table, raking side light, deep shadow left | bar: THE HARDEST ONE | stmt: The first $10,000 is the hardest money you will ever save | colour: --warn]`

**1.6**
> After that, the money starts doing some of the work.

`[ap B | img: a hand-cranked drill left resting on a workbench, crank still spinning (motion blur) — no face | bar: AFTER THAT | stmt: The money starts doing some of the work]`

**1.7**
> Three questions get answered here. First: when does that help actually show up?

`[ap B | img: three sealed envelopes fanned across a desk blotter | bar: QUESTION ONE | stmt: When does that help actually show up? | colour: --target]`

**1.8**
> Second: how much does picking the right account change the answer?

`[ap C-L | img: a printed rate sheet, macro, one column in focus and the rest falling out of plane | bar: QUESTION TWO | stmt: How much does picking the right account change it? | colour: --target]`

**1.9**
> And third: what if eight hundred a month is nowhere near what you can save?

`[ap B | img: an empty lunch container open on a break-room table, fluorescent light | bar: QUESTION THREE | stmt: And if $800 a month isn't there? | colour: --target]`

**1.10**
> All three get answered. But first, the arithmetic nobody does at the start.

`[ap B | img: longhand arithmetic on a legal pad, pencil resting across it | bar: FIRST, THE ARITHMETIC | stmt: The sum nobody does at the start]`

---

## Chapter 2 — One hundred percent of it is you

*Core beat 1 of the creator brief. The whole thesis, stated as arithmetic rather than as
an opinion.*

**2.1**
> Say you take home four thousand dollars a month, and you set aside eight hundred of it.

`[ap B | img: a paper pay stub, perforated edge, folded once on a kitchen table | bar: THE EXAMPLE | stmt: $4,000 take-home · $800 set aside | foot: Channel worked-example convention — not a national average]`

**2.2**
> That is ninety-six hundred dollars a year, before a single dollar of interest.

`[ap C-R | img: twelve small stacks of coins in a row on a dark surface, side light | bar: PER YEAR | num: $9,600 | foot: $800 × 12 — deposits only, no return]`

**2.3**
> With no return at all, the first ten thousand lands in twelve and a half months.

`[ap B | img: a wall calendar with months crossed off in marker | bar: AT 0% | num: 12.5 MONTHS | foot: ILLUSTRATIVE · $800/mo · 0% · monthly compounding | colour: --warn]`

**2.4**
> Now suppose that same money is sitting in the stock market instead, at its long-run shape of about ten percent a year.

`[ap B | img: a printed newspaper markets page, macro, folded once | bar: AT ~10%/YR | stmt: The long-run shape of the US market | foot: S&P 500 ≈10% nominal / ≈7% after inflation since 1957 — a shape, never a decimal | colour: --target]`

**2.5**
> Twelve and a half months becomes twelve.

`[ap B | img: a single calendar page torn free and falling | bar: AT ~10% | num: 12 MONTHS | foot: ILLUSTRATIVE · $800/mo · ~10%/yr · monthly compounding]`

**2.6**
> The best long-run return most people can get, applied to the whole first ten thousand, buys you about half a month.

`[ap M | major: sand running through the neck of an hourglass, macro; minor: the torn calendar page | bar: WHAT THE MARKET BOUGHT YOU | num: ½ MONTH | foot: 12.5 months → 12 months, on the first $10,000 | colour: --warn]`

**2.7**
> Because the money a return is supposed to act on does not exist yet.

`[ap B | img: an empty white dinner plate on a bare table, raking light | bar: WHY | stmt: There is no balance for a return to act on yet]`

**2.8**
> Both of those are model numbers, not promises, and the assumptions are on the screen.

`[ap B | img: a spreadsheet printed on paper, assumption cells circled in pen | bar: SAY IT PLAINLY | stmt: Model output — not a statistic, not a promise | foot: Every math frame in this video carries its monthly amount and its rate]`

**2.9**
> One hundred percent of the first ten thousand comes out of your paycheck. None of it comes from returns.

`[ap R | img: a hand dropping folded bills into a locked steel cash box — hand only, no face | bar: THE FIRST $10,000 | stmt: 100% savings · 0% returns | colour: --warn]`

**2.10**
> Which is why no account, no fund and no app can rescue this part for you.

`[ap C-L | img: a rack of identical blank forms in a bank lobby, no signage, no logos | bar: NOT AN ACCOUNT PROBLEM | stmt: Nothing you can open fixes this part]`

---

## Chapter 3 — The tenth $10,000 (the visible sum)

*Study conclusion 6: do at least one visible sum on screen — the arithmetic the LOW pick
refused to perform anywhere in ten and a half minutes. This chapter is that sum.*

**3.1**
> Now push the same arithmetic forward. Same eight hundred a month, nothing else changes.

`[ap B | img: a long strip of adding-machine tape running off the edge of a desk | bar: SAME INPUT | stmt: $800 a month · nothing else changes]`

**3.2**
> The second ten thousand: twelve and a half months with no return, eleven with the market.

`[ap M | major: two glass jars side by side, the second noticeably fuller; minor: a printed rate sheet, macro | bar: THE SECOND $10,000 | stmt: 0% → 12.5 months · ~10% → 11 months | foot: ILLUSTRATIVE · $800/mo · monthly compounding]`

**3.3**
> The gap widened. Half a month became a month and a half.

`[ap B | img: two nails of different height driven into a plank, hard side light | bar: THE GAP GROWS | stmt: ½ month → 1½ months]`

**3.4**
> Now skip ahead to the tenth one: ninety thousand dollars to one hundred thousand.

`[ap C-R | img: a heavy toolbox with the lid propped fully open, compartments full | bar: THE TENTH $10,000 | stmt: $90,000 → $100,000]`

**3.5**
> With no return, it is still twelve and a half months. Money never speeds up on its own.

`[ap B | img: a parked handcart on a loading dock, motionless, long shadow | bar: STILL AT 0% | num: 12.5 MONTHS | foot: ILLUSTRATIVE · $800/mo · 0% — the interval never shortens | colour: --warn]`

**3.6**
> With the market doing its long-run thing, that same ten thousand takes six months.

`[ap B | img: a station platform clock, hands mid-sweep, slight motion blur | bar: WITH RETURNS | num: 6 MONTHS | foot: ILLUSTRATIVE · $800/mo · ~10%/yr · monthly compounding | colour: --fund]`

**3.7**
> Not because the market got better. Because there was finally something for it to work on.

`[ap B | img: a wide sail catching wind, low angle, no vessel branding | bar: WHY | stmt: The market didn't change. The balance did.]`

**3.8**
> On the first ten thousand the market bought you half a month. On the tenth it bought you six and a half.

`[ap R | img: two lengths of mooring rope coiled on a dock, one small and one enormous | bar: ½ vs 6½ | num: 6½ MONTHS | foot: The same return, on the tenth $10,000 instead of the first | colour: --fund]`

**3.9**
> Same money, same market, more than ten times the effect. That is the whole video.

`[ap M | major: a page torn out of a bound book, the gap visible; minor: the two ropes | bar: THIS IS THE VIDEO | stmt: ½ month at the start. 6½ at the tenth. | foot: ILLUSTRATIVE — figures rounded to the nearest month]`

**3.10**
> And it is the part nobody tells you when you are starting out.

`[ap C-L | img: a stack of unopened financial mail on a hallway table | bar: THE PART NOBODY SAYS | stmt: Nobody runs this sum for you at the start]`

---

## Chapter 4 — Savings rate beats return rate

*Core beat 3, and the mid-video drop zone (2:40–3:43 ≈ 32–43% of runtime). Per the
retention rule the flat stretch opens on tension, not a transition: the chapter starts by
accusing the viewer's actual behaviour. It also carries the strongest US-specific number
in the whole packet — the BEA saving rate.*

**4.1**
> So what do most people spend the first six months on? Picking the account.

`[ap B | img: a dozen printed comparison sheets spread across a couch | bar: WHERE THE TIME GOES | stmt: What do people spend the first months on?]`

**4.2**
> The right app, the right rate, the right fund. Tabs open, comparisons printed, nothing opened.

`[ap B | img: a laptop closed on a stack of printouts, coffee gone cold beside it | bar: THE SEARCH | stmt: The right app. The right rate. The right fund.]`

**4.3**
> Meanwhile the arithmetic is shouting: on the first ten thousand, the whole rate question was worth half a month.

`[ap C-R | img: a short steel ruler laid against a long plank, macro | bar: WHAT IT WAS WORTH | num: ½ MONTH | foot: ILLUSTRATIVE — the entire gap between 0% and ~10%/yr on the first $10,000]`

**4.4**
> Spend six months finding half a month and you have already lost the trade.

`[ap B | img: an unopened application envelope gathering dust on a windowsill | bar: THE REAL COST | stmt: Six months not starting, to win half of one | colour: --warn]`

**4.5**
> Here is the number that actually decides it, and it is a national statistic.

`[ap B | img: a government statistical release printed and stapled, macro on the header rule | bar: THE DECIDING NUMBER | stmt: And this one is published, not modelled]`

**4.6**
> In June, Americans saved two point seven percent of what they took home.

`[ap B | img: a nearly empty coin tray at a checkout counter | bar: NATIONAL SAVING RATE | num: 2.7% | foot: BEA, Personal Income and Outlays, June 2026 (released 30 Jul 2026) | colour: --warn]`

**4.7**
> On a four thousand dollar paycheck, that is one hundred and eight dollars a month.

`[ap C-L | img: a single small stack of bills next to a much larger envelope | bar: WHAT THAT IS | num: $108/mo | foot: 2.7% of the $4,000 worked example — illustrative arithmetic on a published rate]`

**4.8**
> At that rate the first ten thousand takes almost eight years, and almost six even with the market helping.

`[ap M | major: a long empty highway running to the horizon; minor: the wall calendar | bar: AT 2.7% | stmt: 7.7 years · 5.7 years with the market | foot: ILLUSTRATIVE · $108/mo · monthly compounding | colour: --warn]`

**4.9**
> Same person, same market, same returns. The only thing that moved was the rate they saved at.

`[ap R | img: a kitchen faucet running into a bowl, the water column caught mid-fall, dark background | bar: THE ONLY VARIABLE | stmt: Not the return rate. The savings rate. | colour: --fund]`

**4.10**
> The market does not take requests, and the Fed's target range has not moved since December of twenty twenty-five.

`[ap B | img: the stone facade of a federal building, low angle, no readable signage | bar: NOT WORTH WAITING FOR | stmt: The federal funds target range: unchanged | foot: Federal Reserve, open market operations — 3.50–3.75%, last changed 11 Dec 2025 | colour: --target]`

**4.11**
> And that is the one number in this video that is entirely yours.

`[ap C-R | img: a hand resting on a brass valve wheel — hand only, no face | bar: YOURS | stmt: The only number fully in your control | colour: --fund]`

---

## Chapter 5 — The crossover, and the number Munger named

*Core beat 2 and the answer to loop one. facts-staging §2.3 calls this the video's best
beat, and the reason is that the famous quote is **not** the evidence — the arithmetic
reaches $100,000 on its own, and the quote arrives afterwards as colour.*

**5.1**
> So when does the money actually start helping? That was question one.

`[ap B | img: the first of the three envelopes, now open | bar: QUESTION ONE, ANSWERED | stmt: When does the money start helping?]`

**5.2**
> There is a point where your balance earns as much in a year as you can save in a year.

`[ap B | img: a two-pan balance scale almost level, one coin short on the left | bar: THE POINT | stmt: The year your money earns what you save]`

**5.3**
> That is the crossover.

`[ap B | HOLD 5.2's image — ONE continuous zoom across both scenes into the pivot, never a self-dissolve. Pair total 6.7s, inside max_scene_seconds 9.0 | bar: THE WORD | num: CROSSOVER | colour: --target]`

**5.4**
> You are putting in ninety-six hundred dollars a year, so the question is when the balance earns that much on its own.

`[ap C-L | img: a bank strap around a bundle of bills, macro, no denomination readable | bar: THE TEST | stmt: When does the balance earn $9,600 in a year? | foot: $800/mo × 12 = $9,600 a year in]`

**5.5**
> At a long-run market return, that lands at about ninety-six thousand dollars.

`[ap M | major: a full municipal water tower against flat sky; minor: the balance scale | bar: WHERE IT LANDS | num: ~$96,000 | foot: ILLUSTRATIVE · $9,600/yr contribution · ~10%/yr · monthly compounding | colour: --target]`

**5.6**
> Which is roughly one hundred thousand dollars. Ten times further out than the milestone this video opened with.

`[ap R | img: a weathered highway mile marker at dusk, road running past it | bar: THE REAL TURN | num: ~$100,000 | foot: Not $10,000 — the crossover sits roughly ten times further out | colour: --target]`

**5.7**
> And there is a well-known line about exactly that number.

`[ap B | img: a hardback book face-down and open on a lamp-lit desk, no title readable | bar: THE LINE | stmt: A number a lot of people have heard before]`

**5.8**
> Charlie Munger's famous line was that the first hundred thousand is the hardest, and after that you can ease off the gas.

`[ap B | img: an empty conference-room chair at the head of a long table, house lights up | bar: WIDELY REPORTED | stmt: Munger's line: the first $100,000 is the hardest — after that, ease off the gas | foot: Charlie Munger, as widely reported. PARAPHRASE — no quotation marks, no year, no venue: no primary source is reachable]`

**5.9**
> He was not being poetic. That number is where the arithmetic actually turns.

`[ap C-R | img: longhand arithmetic on a legal pad with one line double-underlined | bar: NOT A SLOGAN | stmt: The quote and the sum land on the same number]`

**5.10**
> So the first ten thousand is not where interest takes over. It is where the habit takes over.

`[ap R | img: a worn wooden stair tread, the centre polished smooth by years of use | bar: THIS | stmt: The first $10,000 is where the HABIT takes over | colour: --fund]`

**5.11**
> And there is no route to one hundred thousand that skips the habit.

`[ap B | img: a long empty staircase in a stairwell, seen from the bottom | bar: THE ONLY ROUTE | stmt: There is no path to $100,000 that skips it]`

---

## Chapter 6 — "But I can't save $800"

*Answer to loop three, and the honesty beat. facts-staging forbids dressing $800 as a
national average; this chapter says out loud that it is a split, that the country's real
saving rate is nowhere near it, and that a smaller amount genuinely takes longer.*

**6.1**
> Question three. What if eight hundred a month is simply not there?

`[ap B | img: the third envelope being opened with a thumb | bar: QUESTION THREE | stmt: And if $800 a month simply isn't there?]`

**6.2**
> Median usual weekly earnings for a full-time worker are about twelve hundred and fifty dollars a week.

`[ap B | img: a crowded bus stop at dawn, shot low — bags and shoes only, no faces | bar: THE REAL SPREAD | num: $1,251/wk | foot: BLS, median usual weekly earnings, full-time wage and salary workers, Q2 2026]`

**6.3**
> And four in ten adults could not cover a four hundred dollar emergency with cash or its equivalent.

`[ap C-L | img: a repair invoice face-up on a car hood, figures out of focus | bar: THE MARGIN | stmt: ~4 in 10 couldn't cover $400 in cash or its equivalent | foot: Federal Reserve, Survey of Household Economics and Decisionmaking 2025 — 63% could, using cash, savings or a card paid in full | colour: --warn]`

**6.4**
> So eight hundred is not an average anybody hit. It is the output of a split.

`[ap B | img: a pie cut into visibly unequal slices on a scratched countertop | bar: NOT AN AVERAGE | stmt: $800 is the output of a split]`

**6.5**
> Twenty percent of a four thousand dollar take-home. That is the one input every figure here runs on.

`[ap B | img: a single squared stack of bills on a bare table, top light | bar: 20% OF $4,000 | num: $800 | foot: Every figure in this video runs on this one input]`

**6.6**
> That twenty percent is a target this channel uses for the arithmetic, not a number anyone measured.

`[ap B | img: a target drawn in pencil on butcher paper, taped to a wall | bar: BE HONEST ABOUT IT | stmt: A target for the math — not a statistic | foot: Compare: the actual national saving rate is 2.7% (BEA, June 2026)]`

**6.7**
> If your twenty percent is two hundred dollars, then you start at two hundred dollars.

`[ap M | major: a small pile of coins beside a far larger one; minor: the pay stub | bar: YOUR 20% | stmt: If yours is $200, you start at $200]`

**6.8**
> And yes, the first ten thousand is further away then. That is worth saying out loud.

`[ap B | img: a straight two-lane road disappearing at the horizon, heat shimmer | bar: HONESTLY | stmt: Then the first $10,000 is further away. That's the truth. | colour: --warn]`

**6.9**
> The blocker was never the amount. It is the start date that keeps not arriving.

`[ap C-R | img: a desk calendar with every square blank | bar: THE REAL BLOCKER | stmt: Not the amount. The date that never arrives. | colour: --warn]`

**6.10**
> A transfer that exists and is small beats a transfer that is perfect and never set up.

`[ap B | img: two paper forms side by side — one signed and dated, one blank | bar: THE COMPARISON THAT MATTERS | stmt: Small and running beats perfect and unbuilt]`

---

## Chapter 7 — The fire pit (THE ~70% RE-FRAME)

*Study conclusion 4 and TOP's move 3: at ~70% the video re-frames what it already proved
with a physical image rather than introducing a new fact. Runs 5:38–6:21 of 8:18; the
punch line (7.7) lands at ~6:07 ≈ **73%**. Nothing here is new information.*
*This analogy is deliberately **not** the Hindi cut's rooftop water tank — a US rewrite
gets a US object. Same structural job, different base.*

**7.1**
> Picture a cold morning and a fire pit with nothing in it.

`[ap B | img: a cold stone fire ring on frosted ground, grey dawn, ash only | bar: PICTURE THIS | stmt: A cold fire pit and a cold morning]`

**7.2**
> You have matches and a bag of kindling, and that is all.

`[ap B | img: a box of matches and a bundle of split kindling on a tailgate | bar: WHAT YOU HAVE | stmt: Matches. Kindling. That's it.]`

**7.3**
> At the start there is exactly one way to get heat: you kneel down and feed it, stick by stick.

`[ap C-L | img: hands feeding a single stick into a small flame — hands only, no face | bar: THE ONLY WAY | stmt: The first heat is you, kneeling, one stick at a time | colour: --warn]`

**7.4**
> The fire gives you nothing back yet, because there is nothing there to hold heat.

`[ap B | img: a thin flame on bare ground, almost out, wind visible in the smoke | bar: WHY IT GIVES NOTHING BACK | stmt: There is nothing there yet to hold heat]`

**7.5**
> Then a bed of coals builds up, and the coals start doing the lighting for you.

`[ap B | img: a shallow bed of glowing coals, macro, orange against grey ash | bar: AS IT BUILDS | stmt: The coals start doing the lighting | colour: --fund]`

**7.6**
> One log on a real coal bed puts out more heat than a whole armful did an hour ago.

`[ap R | img: one heavy log dropped onto a deep coal bed, sparks rising, dark surround | bar: ONE LOG, LATER | stmt: The same log. Far more heat. | colour: --fund]`

**7.7**
> The crossover is the moment the coals put out as much as the wood you are feeding it, and it comes long after the first armful.

`[ap B | img: a wide well-established fire at dusk, the wood pile beside it barely touched | bar: THAT MOMENT IS THE CROSSOVER | stmt: It comes long AFTER the first armful — never in it | colour: --target]`

**7.8**
> Where it breaks: a fire eventually burns out, and a bad market year is a downpour.

`[ap B | img: a rained-out fire ring, wet ash, standing water | bar: WHERE THE ANALOGY BREAKS | stmt: Fires go out. Markets have bad years. | foot: Long-run market returns are a historical shape, not a promise | colour: --warn]`

---

## Chapter 8 — How the first $10,000 actually gets built

*Core beat 4, plus the three-rung ladder the MID study pick gives at 49:42 (emergency
fund → stability → growth), restated product-free. No bank, fund, app or platform is named
anywhere in this chapter — the whole thing is behaviour, and the one rate on screen is the
FDIC's published national average, as price evidence.*

**8.1**
> So how do you fill the fire pit? Three things, and all three are boring.

`[ap B | img: three plain galvanised buckets in a row against a shed wall | bar: THREE THINGS | stmt: All three are boring]`

**8.2**
> One: pick a date, not an intention. An automatic transfer, dated the day after payday.

`[ap C-R | img: a date circled in pen on a paper wall calendar | bar: ONE — PICK A DATE | stmt: A date, not an intention. The day after payday. | colour: --fund]`

**8.3**
> Nobody saves what is left at the end of the month, because what is left is always zero.

`[ap B | img: an open wallet lying flat and empty on a counter | bar: WHY NOT LATER | stmt: What's left at month end is always zero | colour: --warn]`

**8.4**
> Two: every raise goes to the transfer, not to the spending.

`[ap B | img: the cut end of a log showing growth rings, macro | bar: TWO — THE ESCALATOR | stmt: Raise the saving, not the spending]`

**8.5**
> Next time your pay goes up, add the whole increase to that same standing transfer.

`[ap B | img: a measuring cup being topped up to the next printed mark | bar: THE WHOLE RAISE | stmt: Add all of the next raise to the same transfer | colour: --fund]`

**8.6**
> Your life stays exactly as it was yesterday, and your savings rate climbs without a decision.

`[ap B | img: the same kitchen shelf, same items, softer evening light | bar: NOTHING CHANGES | stmt: Your life stays yesterday's. The rate quietly climbs.]`

**8.7**
> Three: make it hard to reach. A different bank, no debit card, a day or two away.

`[ap C-L | img: a padlock hanging on a steel cabinet latch | bar: THREE — MAKE IT HARD | stmt: A different bank. No debit card. A day or two away. | colour: --fund]`

**8.8**
> A typical savings account pays just over a third of one percent, and a high-yield account pays roughly ten times that.

`[ap B | img: a printed rate disclosure sheet on a counter, macro on the fine print, no institution name visible | bar: THE ACCOUNT QUESTION | num: 0.38% | foot: FDIC national rate, savings deposits, as of 20 Jul 2026. Price evidence, not a recommendation — no product APY appears in this video]`

**8.9**
> That is the entire account question, and it takes five minutes to settle.

`[ap B | img: a kitchen timer showing five minutes, on a counter | bar: FIVE MINUTES | stmt: That's the whole account question]`

**8.10**
> And the order matters: safety first, then stability, then growth.

`[ap B | img: three stone steps rising out of frame, morning light | bar: THE ORDER | stmt: Safety → stability → growth | foot: An ordering, not a product pick]`

**8.11**
> A few months of expenses you can reach in a day, before anything you lock away for years.

`[ap C-R | img: a wide-mouth jar open on a low shelf beside a sealed crate | bar: RUNG ONE FIRST | stmt: A few months of expenses, one day away | foot: FDIC-insured, ordinary transfer speed — a category, not a product]`

**8.12**
> Because the first ten thousand usually does not die from under-saving. It dies from one emergency.

`[ap R | img: a cracked ceramic jar on a concrete floor, coins spilled out | bar: HOW IT ACTUALLY BREAKS | stmt: Not by under-saving. By one emergency. | colour: --warn]`

---

## Chapter 9 — Today's one job + recap

*Peak-end: the action first, while attention is still on the argument; the recap second;
the CTA after a payoff; then a loop into the next video for session time.*

**9.1**
> One job today, and it takes about five minutes.

`[ap B | img: a wall clock reading five past the hour | bar: TODAY | stmt: One job. Five minutes.]`

**9.2**
> Open your banking app, create one automatic transfer, and date it the day after you get paid.

`[ap C-L | img: a paper transfer authorisation form and a pen on a desk — NOT a phone screen (the phone-in-hand frame has shipped three times already) | bar: DO THIS | stmt: One automatic transfer, dated the day after payday | colour: --fund]`

**9.3**
> Pick an amount that does not scare you. The size is not the point; the standing instruction is.

`[ap B | img: a small coin and a large coin side by side on grey card | bar: THE AMOUNT | stmt: $200 works. So does less. | foot: $200 = the twenty-percent example from Chapter 6. The size is not the point — the standing instruction is]`

**9.4**
> Once it exists, you never have to make that decision again.

`[ap B | img: a wall switch in the on position, dust on the plate | bar: WHY IT WORKS | stmt: You never make the decision again | colour: --fund]`

**9.5**
> Quick recap. One hundred percent of the first ten thousand is your own saving, and the market buys you about half a month.

`[ap B | img: the enamel mug from 1.1, now noticeably fuller — same object, new crop | bar: RECAP ONE | stmt: The first $10,000: 100% you · the market buys ½ month | colour: --warn]`

**9.6**
> On the tenth ten thousand, that same market buys you six and a half.

`[ap M | major: the full glass jar from 1.2; minor: the two ropes | bar: RECAP TWO | stmt: The tenth $10,000: the same market buys 6½ | colour: --fund]`

**9.7**
> And the point where your money genuinely carries its share sits near one hundred thousand, not ten.

`[ap B | img: the highway mile marker again, later light | bar: RECAP THREE | stmt: The crossover is near $100,000 — not $10,000 | colour: --target]`

**9.8**
> The first ten thousand is hard because all of it is you. After that, the money starts pulling.

`[ap R | img: a settled fire burning steadily at night, wide, nobody tending it | bar: THE WHOLE VIDEO | stmt: Hard because it's all you. After that, the money pulls. | colour: --fund]`

**9.9**
> Subscribe if you want money explained this plainly.

`[ap B | img: a closed ledger and a capped pen laid down, finished | bar: — | num: SUBSCRIBE | colour: --pop (the single --pop block of the video)]`

**9.10**
> Next time: what actually happens after that hundred thousand, and how fast it moves.

`[ap B | img: a highway sign gantry seen from below, distance ahead, no place names legible | bar: NEXT | stmt: Past $100,000 — and the speed after it]`

---

## Fact trace (every number → facts-staging.md §2)

| Number / claim in script | Where | facts-staging.md line | Tag |
|---|---|---|---|
| **$4,000/mo** take-home worked example | 2.1, 4.7, 6.5 | §2.1 "Worked-example take-home — $4,000/mo → 20% = **$800/mo**, channel convention" | CONVENTION (labelled on screen at 2.1 and 6.6) |
| **$800/mo**, **$9,600/yr** | 1.1, 1.2, 2.1, 2.2, 3.1, 5.4, 6.5 | §2.1 same row; §2.3 "$800/mo (the locked 20% example)" | CONVENTION — the VO always frames it as "say you… set aside", never as what Americans do |
| **20%** split | 6.5, 6.6 | §2.1 same row | CONVENTION — 6.6 says on screen and in VO that it is a target, not a measurement |
| **2.7%** national personal saving rate, June 2026 | 4.6, 6.6 | §2.2 "**Personal saving rate — 2.7%** (personal saving $646.1bn), June 2026, released 2026-07-30, BEA — read direct" | **HARD** (supersedes the 3.0% May row) |
| **$108/mo** and **7.7 / 5.7 years** | 4.7, 4.8 | §2.3 "at the BEA's actual national saving rate of 2.7%, a $4,000 take-home saves **$108/mo** → **7.7 years** to the first $10,000 (5.7 years even at 10%)" | COMPUTED from one HARD rate + one CONVENTION — `ILLUSTRATIVE` foot on both frames |
| **$1,251/wk** median usual weekly earnings | 6.2 | §2.1 "Median usual weekly earnings, full-time — $1,251/wk (Q2 2026), BLS + FRED LES1252881600Q" | HARD |
| **~4 in 10** could not cover a **$400** emergency **with cash or its equivalent** | 6.3 | §2.1 "Adults who could cover a $400 emergency with cash — 63% (2025) → ~4 in 10 could not, Fed SHED 2025" | HARD — fin-audit widened "with cash" to the SHED test wording (cash, savings, or a card paid in full); the bare "with cash" attached the 37% to a stricter test than the Fed measured |
| **0.38%** savings-deposit national rate | 8.8 | §2.2 "FDIC **national rate, savings deposits** — **0.38%**, as of 2026-07-20 — read direct" | HARD |
| High-yield ≈ **ten times** a typical savings account | 8.8 | §2.1 "Durable HYSA claim — 'roughly **10×** a typical savings account' — **never an APY on screen**" | RULE — obeyed: a ratio is spoken, no product APY appears |
| Fed target range **unchanged since 11 Dec 2025** | 4.10 | §2.2 "Fed funds target range — **3.50–3.75%**, last *changed* 2025-12-11, federalreserve.gov/monetarypolicy/openmarket.htm — read direct" | HARD — the range shows on screen only in the `foot:`; the VO speaks no decimal |
| **~10%/yr** long-run market shape | 2.4, 2.5, 2.6, 3.2, 3.6, 5.5 | §2.2 "S&P 500 long-run return — **≈10% nominal / ≈7% after inflation** since 1957 … **HARD on the shape ('about ten percent')** · **SOFT on every decimal — never speak one**" | shape only — no decimal spoken or shown anywhere |
| First $10,000: **12.5 / 12 months** | 1.1, 2.3, 2.5 | §2.3 table, "Months to the **first** $10,000 — 12.5 (0%) / 12 (10%)" | COMPUTED — `ILLUSTRATIVE` foot on every frame |
| Second $10,000: **12.5 / 11 months** | 3.2 | §2.3 "Months for the **second** $10k — 12.5 / **11**" | COMPUTED |
| Tenth $10,000: **12.5 / 6 months** | 1.2, 3.5, 3.6 | §2.3 "Months for the **tenth** $10k ($90k→$100k) — 12.5 / **6**" | COMPUTED |
| **½ month vs 6½ months** — the thesis | 2.6, 3.3, 3.8, 3.9, 4.3, 9.5, 9.6 | §2.3 rows above (12.5→12 = ½; 12.5→6 = 6½) | COMPUTED — spoken as "more than ten times", never as an exact multiple, because both inputs are rounded |
| Crossover **≈ $96,000** at a ~10% return | 5.5, 5.6 | §2.3 "**Crossover** ($9,600/yr in): **≈ $96,000** at 10% … **Munger's $100,000 IS the crossover point**" | COMPUTED — the staging note's own framing |
| **$100,000** ≈ the crossover, ten times past the milestone | 5.6, 5.11, 9.7 | §2.3 same row | COMPUTED — presented as *why* the famous number is that number |
| **$200** as "your twenty percent" | 6.7, 9.3 | §2.1 20% convention applied to a smaller take-home — an illustration of the split, not a claim about anyone | CONVENTION (derived) — no source needed, and 6.7 states the condition in the same sentence |
| Munger paraphrase | 5.8 | §2.2 Munger row + the **Munger rule** immediately below it — "Safe: *'Charlie Munger's famous line was that the first hundred thousand is the hardest — after that, you can ease off the gas.'*" | **SOFT** — used verbatim in the sanctioned form. No year, no venue, no profanity, and it is colour, not evidence: 5.5 reaches $96,000 without it |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **Every rupee figure and the whole of facts-staging §1.** That is the other cut's block.
  The rupee glyph and the words "lakh"/"rupee" appear nowhere in this file, not even inside
  a claim ID, and no line compares the two markets' milestones.
- **~4.15% top high-yield APY (Forbright / Newtek 4.20%).** §2.2 tags it SOFT and
  **"context only, never on screen"**; the standing HYSA rule says never an APY. 8.8
  speaks the ratio instead. The 4.15% crossover figure (≈$231,000) is dropped with it —
  it cannot be footed without printing the rate it came from.
- **Any decimal on the market return** (10.69 / 6.81 / 10.33 / 10.59 / 10.3). §2.2:
  four sources, four decimals, no shared methodology. Shape only, spoken and on screen.
- **A date or venue for the Munger quote**, and the profanity in the original wording.
  §2.2 Munger rule.
- **Real median household income $83,730 (2024).** HARD and unused: pairing it with the
  $4,000/mo worked example would imply the example is a national median, which it is not.
- **"The median American has $8,000 saved / $62,410 average", the under-35 $5,400 figure,
  and every "average savings by age" table.** §3 rejects all of them — repackaged SCF 2022,
  four years stale, reached only through blogs.
- **A named bank, brokerage, fund, index fund, app or platform.** Persona rule. The savings
  rate, the high-yield ratio and the Fed range are **price evidence only**, and the 8.8
  foot says so on screen.
- **A 22% APR credit-card number** (suggested as a US shock in `us-english-script-style.md`).
  No sourced line exists for it in this run's facts-staging, and no sourced line means no
  number. The US shocks in this cut (the repair invoice, the emergency) carry no figures
  except the SHED-sourced $400.

---

## Build handoff

1. **`assets/voice/en-lines.json` = 92 entries keyed `1.1 … 9.10`**, containing **only**
   the `>` VO strings above — no markdown, no cue text, no on-screen text. **Key the
   extraction off the `**N.N**` headers**, not off `^>`: the ⚠ admonition near the top of
   this file is also a blockquote and would otherwise be sent to ElevenLabs. **Slice the
   source file; never retype.** Gate the extraction with a byte-for-byte reconstruction
   check against this file before generating audio (`long_form_scripting.md` §1.7).
2. **TTS** via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb` (Brian),
   `eleven_multilingual_v2`, style 0. **92 calls.** With the Hindi cut's 86 that is
   **178 of the run's 200** — 22 spare. Regenerate individual failed clips only; a
   full-chapter re-cut on either side blows the budget.
3. **Timing is by construction.** One line = one clip = one scene. Scene span =
   `probe(clip) + gap_after(line)`, with `GAP_INTRA = 0.20` and `GAP_CHAPTER = 0.80`
   (firaun `build.py` gap model). Never hand-edit a duration; regenerate all four homes of
   the timing numbers from one source.
4. **Recount the characters programmatically** and re-check the total against
   510 × 16.1 = 8,211 before locking. The tables above are budget estimates at ±10%.
   ⚠ **Pin the rounding convention before computing anything.** Every months-to-milestone
   figure in `facts-staging.md` §2.3 is **round to the nearest month**, not the first month
   at or above the target — the same trap fin-audit pinned on the Hindi cut. The VO is
   locked to the staged set (**12.5 / 12 · 12.5 / 11 · 12.5 / 6**). A build that uses
   `ceil` will print an integer the voice contradicts, and the fix at that point costs a
   TTS re-cut. Note that 12.5 is exact by construction ($10,000 ÷ $800) and must render as
   `12.5`, not `13`.
5. **Images: one per line, 92 scenes, zero photo-free frames** (`photo_free_scene_ratio`
   = 0, creator rule 2026-07-28). **Exactly one hold pair — 5.2 + 5.3** — which must run
   **ONE continuous zoom** across both scenes, never a self-dissolve (creator rule, firaun
   2026-07-23). The pair totals ~6.7s, inside `max_scene_seconds` 9.0, so no build-time
   re-crop is needed. Five scenes deliberately re-photograph an earlier object from a new
   crop (9.5 ← 1.1, 9.6 ← 1.2 and 3.8, 9.7 ← 5.6, 5.9 ← 1.10, 8.6 ← 8.5's kitchen);
   those are **separate images**, not holds.
   md5 the asset ledger: no image may repeat across videos or channels, and the shipped
   cuts have already burned `hand tapping phone banking app` and `young indian man … phone`.
6. **US localisation sweep on every photograph** (`us-english-script-style.md`: a
   motorcycle in a workshop, a Swiss franc and a pile of euro coins all shipped in the
   first `-en` cut). Reject any frame with non-US currency, non-US plates, non-US signage,
   right-hand-drive vehicles or foreign-language packaging. US bills and coins only where
   currency is visible at all.
7. **The `.swiss` divergences from `design-finance-blockframe.md` are load-bearing** — see
   §8 of `11-swiss-vignelli.md`: radii → 0, rotation → 0, `text-shadow` off, four-layer
   scrim deleted (hard-edged tone block on a column line instead), per-scene `--tint`
   retired, grade to ~`grayscale(0.85)`, Ken Burns halved inside the band, `back.out` /
   `breathe` / `drift` unused, every scene flush left.
8. **Reversed type is measured, not assumed.** The 9 `ap R` scenes put type on the
   photograph. Measure the left third's mean luminance at fetch time and reject any image
   above 25%; there is no scrim to rescue it.
9. **Do not sync the aperture cycle with the Hindi cut.** The hi cut opens on `R`; this one
   opens on `B` and its first `R` is scene five. If both cuts land on the same aperture at
   the same scene index the pair reads as one template with the language swapped, which is
   the exact sameness failure the sequence layer exists to prevent.
10. **Anchor cues to word-level timings** (faster-whisper), not character-offset
    interpolation.
11. **Chapter-wise production.** Build, proof and re-render chapter by chapter; concat and
    final-render only after all nine chapters are locked.
