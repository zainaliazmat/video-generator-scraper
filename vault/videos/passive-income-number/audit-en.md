---
summary: fin-audit gate for passive-income-number cut en, attempt 2 — the style-E restyle, 81 lines, audited from scratch (attempt 1's audit is void; different numbering, different prose). PASS with two edits. Killed 4.8's claim that what Bengen and Trinity tested was "how fast a tank drains" — the analogy was asserting a no-inflow model as the papers' method and contradicting the script's own 95% survival line; and cut scene 1.2's third chip from 27 to 16 chars to clear max_chip_chars 22. Chapters 1–2 confirmed verbatim against the creator-approved style-E draft, all 23 lines. All fourteen corpus lines now speak their rate, including the three attempt 1 caught. Every load-bearing figure re-fetched from its recorded source URL; Trinity 1998 and the Bengen 1994 review read as primary PDFs.
updated: 2026-08-07
source: vault/videos/passive-income-number/script-en.md (attempt 2) + facts-staging.md + run.json constraints/style_decision + studio/voice-tests/passive-income-number/style-E-en-teacher-curiosity.txt + logs/fin-script-en-2.md + tools/format.json. Every source URL was fetched again at this stage; no figure was graded on the staging text alone.
stage: fin-audit, cut en, attempt 2 — STYLE E RESTYLE
---

# audit — passive-income-number, cut `en`, attempt 2 (style-E restyle)

PASS

Passed **with two edits**, one of them a VO line. `script-en.md` was changed at **4.8** (VO +
its cue) and at **1.2** (cue only). **Downstream voice work must re-run against the edited
file — the pipeline hash-checks this.** fin-voice was re-running all 81 clips regardless (the
attempt-1 Brian clips are dead), so both edits land before any TTS spend and cost nothing.

> **Attempt 1's audit is void, not amended.** That document graded a 78-line style-A script
> whose numbering does not survive the restyle: its `5.6` is this file's `5.7`, its `2.11` is
> this file's `2.13`, and its chapters 1–2 no longer exist as prose. Nothing from it is
> carried forward except one recorded ruling I was instructed not to re-litigate and did not:
> **Bengen's `pp. 171–180` is correct and Wikipedia's `pp. 14–24` is the outlier.**

---

## 1. Chapters 1–2 against the creator-approved draft — VERBATIM, all 23 lines

`run.json.style_decision` says fin-script took chapters 1 and 2 from
`studio/voice-tests/passive-income-number/style-E-en-teacher-curiosity.txt` verbatim. Checked
line by line against the reference, not sampled: **1.1–1.8 and 2.1–2.15, twenty-three lines,
match character for character** — same em-dashes, same colon in 1.6, same comma before "and"
in 1.7, no re-wrapping.

**Line 1.7 is present and unchanged**, both against the reference draft and against the
`line_1_7_en_is_untouchable` string in `run.json`:

> *"Everyone asks how much you need invested to live off dividends, and the honest answer
> costs more than the popular one."*

It is the only line in this file I would have failed the run over rather than edited. It is
intact, it is at 0:29, and the loop it opens closes at 5.7. **Neither of my edits touches
chapter 1 or 2's VO** — the 1.2 edit is an on-screen chip string, which is fin-script's own
wording and not part of the creator-approved draft (the draft carries VO lines only).

---

## 2. The independence re-fetch (the point of this stage)

`facts-staging.md` was written by this same run, so no figure below was graded against the
staging text. Every recorded source URL was fetched again here, this attempt.

| Figure, as used in the script (attempt-2 line numbers) | Source re-fetched this stage | Result |
|---|---|---|
| Cooley, Hubbard & Walz · *AAII Journal* · **February 1998** · pp. **16–21** (2.7 `foot:`) | `aaii.com/journal/199802/feature.pdf` — **PDF read as pages, primary** | ✅ byline, title, journal, month and the 16→21 page footers all on the artefact |
| "three Trinity University professors" (2.7) | same PDF, author footnote p. 16 | ✅ *"professors of finance in the Department of Business Administration, Trinity University, San Antonio, Texas"* |
| **95%** at 4.0%, inflation-adjusted, 30-yr payout, at 100% stocks **and** at 50/50 (2.8) | same PDF, **Table 3**, read cell by cell | ✅ both cells read **95**. The `foot:` naming both allocations is correct, not a hedge |
| *"The study did not adjust for taxes or transaction costs."* (3.11) | same PDF, methodology bullets p. 17 | ✅ **verbatim, exact** |
| *"Early retirees who anticipate long payout periods should plan on lower withdrawal rates."* (3.14) | same PDF, **Conclusion** p. 21 | ✅ **verbatim, exact** |
| Payout periods 15/20/25/30 · data **1926–1995** (3.13 `foot:`, 2.8 `foot:`) | same PDF, Tables 1 and 3 | ✅ both |
| Trinity rows the script says it *deliberately did not use* (98% at 75/25, 71% at 25/75, 20% at 100% bonds) | same PDF, Table 3 | ✅ all three correct — the exclusion note is honest, not a cover for a misread |
| Bengen · *"Determining Withdrawal Rates Using Historical Data"* · **JFP, October 1994** (2.5) | `obj.portfolioconstructionforum.edu.au/…pdf` — **PDF read as pages** | ✅ title, author, journal, month |
| **vol. 7 no. 4, pp. 171–180** (2.5 `foot:`) | — | **NOT RE-LITIGATED, per the audit brief.** Attempt 1 established the page range is right and Wikipedia is the outlier; re-opening it is how a correct citation gets wrongly killed on a second pass. Carried unchanged |
| **50/50 stocks-bonds**, retirements starting **1926** (2.6) | same review PDF | ✅ verbatim: *"Using a 50% equity/50% bond portfolio"*, *"he used retirement years from 1926 to 1966"*. The VO says "starting in nineteen twenty-six" — the earliest start year, correct |
| Bengen worst case ≈ **30 years** (3.13 `foot:`) | same review PDF | ✅ *"The worst-case scenario was around 30 years (for a person who retired in 1976)"* |
| S&P 500 dividend yield **1.04%** today · mean **4.21%** · median **4.19%** (4.11 `foot:`, 5.3, 5.4) | `multpl.com/s-p-500-dividend-yield` — **read direct** | ✅ 1.04% as of 6 Aug 2026 · mean 4.21 · median 4.19 |
| **13.84%, June 1932** (4.11, spoken) | same | ✅ *"Maximum: 13.84% (June 1932)"* |
| **Series back to 1871** (4.11, spoken: "Going back to eighteen seventy-one") | `multpl.com/s-p-500-dividend-yield/table/by-month` — **read direct** | ✅ first row **Jan 31, 1871 · 5.86%**. The one spoken date I could not confirm from the summary page, so I fetched the table itself |
| **1.08%, July 2026, all-time minimum** (5.4 `foot:`) — **and the divisor behind $5,555,556 and $7,271,759** | multpl, read direct | ✅ *"Minimum: 1.08% (July 2026)"* |
| **$78,535** · **$26,266** · **$13,318** · **$10,169** · **33.4%** · **50.4%** (2.11, 3.2, 3.6, 3.7, 5.14) | `bls.gov/opub/ted/…` **403** · `bls.gov/news.release/cesan.nr0.htm` **403** · `bls.gov/news.release/pdf/cesan.pdf` **403** → `randalolson.com/2026/03/26/household-spending-2024/` **read direct**, plus BLS's own X post and the bls.gov release surfaced in search | ✅ **all six on an independent surface**: 78,535 · housing 26,266 (~33%) · transportation 13,318 (~17%) · food 10,169 (~13%) · housing+transport ≈50%. The release is named and numbered on screen (USDL-25-1586, 19 Dec 2025) |
| **SCHD 3.11% TTM**, $1.05/share, quarterly → the "about three percent" route (5.10, 5.11) | `stockanalysis.com/etf/schd/dividend/` — **read direct, today** | ⚠ **reads 3.09% today, not 3.11%.** See the drift note below. Not a kill: $1.05/share and quarterly confirm, the `foot:` is dated *6 Aug 2026*, and the VO says only "about three percent" |
| **Morningstar 3.9%** for a **2026 retiree** · 30-yr · 90% success · 30–50% equity · *2025 Edition*, **3 Dec 2025** · up from 3.7% (6.2) | fa-mag **403** → `keilfp.com/blogpodcast/morningstar-safe-withdrawal-rate/` — **read direct** | ✅ every element, including the prior year's 3.7%. **The staged naming trap is obeyed**: screen says "for a 2026 retiree", foot dates the report as the 2025 Edition |
| **Pfau, JFP December 2010** · Japan **0.26%** · 50/50 stocks-bills · zero tolerated failure (6.4) | `retirementresearcher.com/the-shocking-international-experience-of-the-4-rule/` — **read direct** | ✅ title, journal, month/year, Japan 0.26%, and the `foot:`'s "zero tolerated failure" is right: SAFEMAX is defined on the page as *"the maximum sustainable withdrawal rate over 30-years in the worst-case scenario from a country's history"*. Source says *"the 4% rule did not survive in any country"*; the VO says **"did not hold up across most developed markets"** — deliberately **weaker** than the source, and it also survives the page's looser *"even allowing for a 10% failure rate"* framing (4% cleared in only 5 of 19). Understating is the safe direction |
| The Pfau **country-count conflict** (17/109 vs 19/1900–2010) | the fetched page says **19 countries**, 10 of them below 3% | ✅ **staged conflict obeyed** — no count is spoken or shown anywhere in the file, and Japan's 0.26% is the only country decimal used |
| **Bengen 4.7%**, "SAFEMAX", *A Richer Retirement*, **Wiley, August 2025**, ~400 start dates (6.3) | advisorperspectives **403** → `fool.com/…/the-father-of-the-4-rule-says-retirees-can-withdraw-more/` **read direct** + publisher search | ✅ 4.7%, "Safemax", the book title, 55% diversified stocks / 40% intermediate government bonds / 5% T-bills, ~400 start dates; **Wiley** and **5 August 2025** confirmed from the publisher's own listing. Attempt 1 could not reach the publisher and retained this on trust — it is now verified |

**Three things are recorded rather than laundered:**

- ⚠ **SCHD drift: the source reads 3.09% today against the staged 3.11%.** A live TTM yield
  moved 2 basis points in a day, which is what a live TTM yield does. **Not killed**, on
  three grounds: the `foot:` is *dated* (`stockanalysis.com, 6 Aug 2026`) so the screen makes
  a dated claim, not a current one; the VO says only *"about three percent"*, which staging
  tags HARD and which survives either read; and the corpus it feeds is robust — $60,000/0.0309
  = $1,941,748, which the VO's *"near one point nine million"* still describes. **Binding on
  the build:** if the frame's decimal is regenerated at render time it must be re-read and
  re-dated together with `$1,929,260`, never one without the other.
- **`GuruFocus 1.082%`** (on screen at 5.3 and 5.4). gurufocus.com was not reachable this
  stage either. Not load-bearing: the VO says *"one point zero eight"*, and **every
  dividends-only corpus divides by 0.0108**, which multpl confirms direct as its own July 2026
  series minimum. Only the third decimal and its attribution are unverified.
- **The 5.14 `foot:` quintile range `$35,046 → $150,342`** is the one figure in the file I
  could not put on any surface this stage — bls.gov 403'd three ways and it is not carried by
  the independent surface that has the rest of the table. It is screen-only, never spoken,
  attributed to a named and numbered release whose every other figure checked out. **Kept,
  and flagged:** if the build cannot re-confirm it, drop that sentence from the foot — nothing
  in the argument moves.

**Arithmetic re-derived independently, every corpus:** 10,169/12 = 847.4 ✅ · 10,169/.04 =
254,225 ✅ · 13,318/12 = 1,109.8 ✅ · 13,318/.04 = 332,950 ✅ · 26,266/12 = 2,188.8 ✅ ·
26,266/.04 = 656,650 ✅ · 60,000/.04 = 1,500,000 ✅ · 78,535/12 = 6,544.6 ✅ · 78,535/.04 =
1,963,375 ✅ · 60,000/.0108 = 5,555,556 ✅ · 78,535/.0108 = 7,271,759 ✅ · 60,000/.0311 =
1,929,260 ✅ · 26,266/78,535 = 33.44% ✅ · (26,266+13,318)/78,535 = 50.40% ✅ ·
5,555,556/1,500,000 = 3.70 ✅.
**Every figure is exact to the dollar.** The two BLS shares reproducing to the second
decimal off the published totals is itself strong corroboration that the line items are a
real table and not a reconstruction.

**The hero pair is intact and unchanged by the restyle:** **$1,500,000 at 4.0% = $5,000/month**
(spoken whole at 4.3, re-stated at 5.8 and 6.8) **versus $5,555,556 — "five point six million"
— for that same $5,000 from S&P 500 dividends alone at the ~1.08% yield** (5.7, restated at 5.8
and 6.9). Both halves carry their rate in the spoken line *and* in the frame at every
appearance. The 3.7× ratio is shown as `ROUGHLY 4 TIMES` and **never spoken as a decimal**,
exactly as `facts-staging.md` C.3 stages it.

---

## 3. Rate-with-every-corpus, in the SPOKEN line — 14/14, verified one at a time

This is the failure this video exists not to repeat, and attempt 1 caught three of them. I
re-read every line carrying a corpus or a derived income figure against the spoken text, not
against fin-script's table:

| line | figure spoken | the rate, in the same spoken sentence |
|---|---|---|
| 2.13 | $254,225 | *"Divided by four percent"* ✅ |
| 2.14 | $254,225 | *"drawn at four percent a year"* ✅ |
| 3.4 | $332,950 | *"Divided by four percent"* ✅ |
| 3.8 | $656,650 | *"Divided by four percent"* ✅ |
| 4.2 | $1,500,000 | *"divided by four percent"* ✅ |
| 4.3 | $1,500,000 **and** the derived $5,000/mo | *"at a four percent withdrawal rate"* ✅ — the `derived_income_carries_assumption` extension is satisfied in the VO, not just the frame |
| 5.7 | $5,555,556 | *"at about one percent"* ✅ ← **attempt 1's bare 5.6, now fixed** |
| 5.8 | both hero figures | *"at four percent"* **and** *"at about one percent"* ✅ |
| 5.11 | $1,929,260 | *"At about three percent"* opens the line ✅ |
| 5.15 | $1,963,375 + derived $6,545/mo | *"at four percent"* ✅ |
| 5.16 | $7,271,759 | *"at about one percent"* ✅ |
| 6.7 | $254,225 · $332,950 · $656,650 | *"At four percent,"* opens the line ✅ ← **attempt 1's bare 6.7, now fixed** |
| 6.8 | $1,500,000 · $1,963,375 | *"Both at four percent."* opens the line ✅ ← **attempt 1's bare 6.8, now fixed** |
| 6.9 | $5,555,556 | *"at about one percent"* ✅ |

**Fourteen for fourteen, in the VO and in the frame.** The three attempt 1 caught are the
three that now open with their rate — the fix is real, not a re-labelling.

I also checked for a *fifteenth* corpus hiding outside fin-script's own table, since a table
that lists its own passes is not evidence. There is none: the only other money figures spoken
are **bills** (2.11, 3.2, 3.6, 5.14 — BLS statistics, no rate applies), their **÷12 monthly
forms** (2.12, 3.3, 3.7 — expenses, not income from a corpus), and **4.1's chosen $5,000/mo**,
which is an *input* stated before any corpus exists and whose frame says why it was chosen.
Nothing is bare.

**On 6.7's fractions — ruled acceptable, and here is the arithmetic.** *"a quarter of a
million"* = $250,000 against a true $254,225, a **1.7%** round · *"a third of a million"* =
$333,333 against $332,950, **0.1%** · *"two thirds of a million"* = $666,667 against
$656,650, **1.5%**. All
three are canonical fraction phrases, all within 1.7%, all with the **exact digits in the
frame** beside them and `ILLUSTRATIVE ARITHMETIC` in the foot, and all three are governed by
the *"At four percent,"* that opens the line. **It reads as rounding, not as a new figure** —
and the alternative (nine spoken digit-groups in one sentence) is the ASR digit-loss lane this
channel has already been burned by three times. Ruling: keep.

---

## 4. What was rewritten, and why

### EDIT 1 — 4.8, a VO line: the tank analogy was misdescribing the papers

**Shipped:** *"The papers tested how fast a tank drains, and no advertisement changes that."*

The audit brief is explicit that the tank is a teaching device for the withdrawal-rate
question and **not** a model of returns, and that the script must never let it imply a drawn
portfolio is doomed. This line does exactly that, and it is the only line in the tank chain
that does. Two independent problems:

1. **It misstates the method of the two papers the whole video's authority rests on.** I read
   both. Trinity ran portfolio survival across real stock and bond returns, 1926–1995; Bengen
   ran portfolio longevity across real returns from 1926. Neither tested a vessel with no
   inflow. "How fast a tank drains" describes a no-inflow vessel and attributes that model to
   them.
2. **It contradicts the script's own 2.8**, three chapters earlier: *"four percent survived
   ninety-five percent of the periods they tested."* Surviving is the opposite of draining. An
   unqualified "how fast a tank drains" makes draining the only outcome and turns the video's
   own sourced finding into a contradiction the viewer has to resolve.

**Rewritten to:**

> *"The papers tested how long a tank lasts at each rate, and no advertisement changes that."*

`at each rate` is the whole fix: it is true of both papers (that is literally what Tables 1
and 3 are — a rate × horizon grid), it removes the doom implication, and it puts the rate back
at the centre of a warning beat, which is the spine of this cut. The cue's `stmt:` was moved
with it (`How fast a tank drains.` → `How long a tank lasts at each rate.`) so the frame and
the voice do not disagree. 76 → 88 chars; the scene runs 5.0s + 0.8 = 5.8s, well under
`max_scene_seconds` 9.0. The beat, the image brief and the callback are untouched.

**The rest of the tank chain is honest and I left it alone.** 2.2 asks *"how much you can draw
out each year without emptying it"* — emptying is presented as avoidable, so nothing is doomed
— and it is bounded later by 3.13's thirty-year horizon and 3.14's Trinity warning, so nothing
is immortal either. 4.7 (*"twelve percent is a promise about the tap"*), 4.10 and 4.13 (*"a
smaller price is a smaller tank"*) are about the corpus's market value, which is correct. 5.5
(*"you may only take what it hands you"*) implicitly grants the tank an inflow, which is right
for a dividends-only route. **No line says "forever" and no line says the money must run out.**

### EDIT 2 — 1.2, a cue only: a chip 5 characters over the cap

**Shipped:** `stmt: No alarm · No call from work · No reminder of what you owe`, declared as a
3-item cascade. The third chip is **27 characters** against `layout.max_chip_chars` **22**.
Chapter 1 is entirely new in the restyle, so no prior storyboard ever saw this row.

**Rewritten to:** `No alarm · No call from work · No debt reminder` — 16 characters, parallel
with the other two, same meaning as the VO's *"No message reminding you what you owe someone."*

**The VO line is untouched.** The creator-approved draft carries VO lines only; the on-screen
chip wording is fin-script's own, so this edit does not breach the verbatim rule for chapter 1.

### What I did NOT edit, though it was tempting

The **2.13 → "two hundred fifty-four thousand"** truncation of $254,225 and the **3.8 → "about
six hundred fifty-seven thousand"** round of $656,650. Both are creator-approved-verbatim or
sub-0.1%/rounded-with-"about", both carry exact digits in frame. Editing correct text is how a
second audit pass destroys a script.

---

## 5. The rest of the brief's checks

**The 4% rule attributed, never asserted as law — PASS, and it is still the strongest part of
the script.** 2.3 says *"four percent is not a law"* before the number is used for anything;
2.4–2.8 attribute it to two named, dated papers, **both of which I read as primary PDFs this
stage**; 2.9 closes the block with *"a finding with a date, not a promise about your money."*
Four documented criticisms ship, three of them **the papers criticising themselves** —
taxes/costs (3.11, verbatim primary), the thirty-year horizon (3.13), early retirees (3.14,
verbatim primary) — plus Pfau's international failure (6.4) and **the author's own upward
revision** (6.3). The staged instruction to reject the *"4% rule is dead"* headline framing is
obeyed: 6.3 says Bengen moved it **up**. 6.1–6.5 then puts on the record that the rate is not
settled, *before* the recap, and 6.5 ties that back to why the rate sits beside every number.

**No return promise — PASS.** Every corpus is division from a rate named in the same spoken
sentence (§3). No accumulation math exists anywhere in the file, so no growth rate is ever
applied to anything. **"forever" does not appear**, and neither does "the principal keeps
growing" — the trace table records both as deliberately excluded, and I confirmed they are in
fact absent rather than merely disclaimed.

**No corpus-to-age conversion — PASS, clean.** **Zero ages in the file.** `retire*` matches
only *"retirements starting in nineteen twenty-six"* (a start year), *"thirty-year
retirement(s)"* (a horizon, 2.8 and 3.13) and *"early retirees"* at 3.14 — which is Trinity's
own verbatim Conclusion, permitted by `facts-staging.md` PART D, and 3.15 immediately frames
it as *"a warning, not a plan."* Twin A's *"financially free at 50"* has no analogue.
`no_unsourced_retire_early` holds.

**Dollars only — PASS.** Grepped the whole file for `₹`, lakh, crore, SIP, SWP, PPF, POMIS,
SCSS, rupee: **the only hits are inside the rule box that forbids them.** Zero `₹` glyphs. No
Indian instrument, figure, institution or photograph brief anywhere.

**No Latin digits in a VO line — PASS, mechanically.** `^> .*[0-9]` across the file returns
**only** guard blockquotes — the six-item rule box, the timing-budget warnings and the
chapter-4 conflation warning — none of which follows a `**N.M**` key, which is how fin-voice
extracts. **All 81 VO lines are digit-free**, including the ones that had to spell *"one point
zero four"*, *"thirteen point eight four percent"* and *"eighteen seventy-one"*.

**No first person — PASS, and the new register did not smuggle it in.** This was the specific
risk of style E: imperative signposts are one word away from a narrator. Grepped every `> `
line for `I / we / my / our / us / let's` and variants: **zero matches, in VO lines and in
guard prose alike.** Every signpost is an imperative — *Notice this · Think of it this way ·
Now watch what it buys · Work it through · Notice what changed · Say that one slowly · Go back
to the tank · Work it through* — addressed to the viewer, never a claim to teach. No greeting,
no credential, no host.

**No bait-and-switch on the title — PASS, delivered and honest in both directions.** The exact
format-twin phrase is **spoken at 1.7, inside the hook**, so the viewer is never asked to wait
for a different video. 5.1 re-opens it as the viewer's own question including the never-sell
condition; **5.7 pays it in full at the ~70% reward beat** with $5,555,556 at 1.08%; 5.8 sets
it beside $1,500,000 at 4.0% for the identical paycheck. The premise is **not** dismissed —
5.2 calls dividends-only *"a real strategy with a real price tag"* and 5.10–5.12 add a third
rate so the answer is a menu, not a verdict.
*One asymmetry, judged acceptable and unchanged from attempt 1:* the script never states what
dividends-only **buys** (never selling, no sequence risk on principal). No staged fact supports
a benefit claim, and *"the principal keeps growing"* is excluded precisely because it is a
capital-preservation promise the 4% rule does not make. Declining to assert an unsourced upside
is the right failure direction.

**Ladder ordering (housing at rung 3) — APPROVED, carried from attempt 1 and re-checked.**
With BLS housing at $2,189/mo against a $5,000/mo hero, the briefed order produces
$1,500,000 → $656,650 → $1,963,375: **the ladder descends across its own climax.** As shipped
it is strictly monotonic — 254,225 → 332,950 → 656,650 → 1,500,000 → 1,963,375. The wording
risk I re-checked: 3.5 calls housing *"the biggest line in the American budget"* while rungs 4
and 5 are larger. **No contradiction** — rungs 4 and 5 are a chosen paycheck and a whole-year
total, not budget line items.

**Yield purity — PASS.** The frames carry **1.04% · 1.082% · 1.08% · 3.11% · 4.21% · 4.19% ·
13.84%** — staged decimals, not rounded convenience numbers. The dividends-only arithmetic
divides by **0.0108**, never 0.01: $60,000/0.01 would be $6,000,000 and that figure appears
nowhere. Choosing 1.08% over the 1.04% current read produces the **smaller** corpus
($5,555,556 vs $5,769,231), i.e. it **understates** the gap the video is arguing for. Right
direction. And the attempt-1 fix holds: **the 4.21% long-run mean is screen-only at 4.11 and
is not spoken** — a spoken "a little over four percent" fifteen seconds after a spoken four
percent withdrawal rate is the yield/withdrawal-rate conflation the study caught twin B making.
The 4.9–4.10 mechanism (*"a yield is a payout divided by a price"* → *"a yield can double
without one extra dollar being paid out"*) keeps the two concepts apart by construction.

---

## 6. Standing gates

| # | Gate | Result |
|---|---|---|
| 1 | Every number traces to staging **and survives re-fetch** | ✅ — §2. Nothing untraceable; nothing unsupported by its own source. One dated live figure drifted 2bp (SCHD) and one screen-only footnote could not be re-reached; both recorded, neither load-bearing |
| 2 | Char total within ±10% of budget | ✅ **8,014** (8,002 + 12 from my 4.8 edit) against `(510 − 81×0.8) × 17.57 = 7,822` → **+2.5%**. I re-derived the budget formula independently and hand-verified two line counts against the per-scene table (1.1 = 49 ✅, 2.2 = 155 ✅), so the table is trustworthy, not decorative |
| 3 | Hook payoff inside 15s | ✅ **on the model of record, with a flag.** Recomputed, not taken from the script: 1.1 ends 3.59s, 1.2 ends 8.66s, 1.3's VO opens **8.91s**, the clause *"money is deposited into your account"* opens ≈**10.9s** and closes ≈**13.0s**. Inside, ~2s of margin. **⚠ See the hook-gate flag below — this cut's chapter 1 is punctuation-dense and the hi cut landed at 14.9–15.1s on exactly this pattern** |
| 4 | No product or platform recommended | ✅ — **no ticker, no fund name, no AMC, no broker, no account type**, in VO or on screen (grepped SCHD/VYM/Vanguard/Schwab/Fidelity: zero hits outside the off-screen trace table and the exclusion list). 5.10's frame describes an asset class and says so. `multpl.com` / `stockanalysis.com` appear as data attributions in `foot:` — price evidence, the permitted use |
| 5 | Currency purity | ✅ — **zero `₹` in the file.** lakh/crore/SIP/SWP/PPF/POMIS/SCSS occur only inside the rule box that forbids them |
| 6 | No cite refs · no bare Latin digits in VO | ✅ — **`^> .*[0-9]` returns only guard blockquotes, none of which follows a `**N.M**` key. All 81 VO lines are digit-free.** No `(28:4)`-style refs anywhere; the only `(N:NN)` strings are runtime notations in production prose |
| 7 | Persona rules (2026 monetisation carve-out) | ✅ — **no `I`, `we`, `my`, `our`, `us` or `let's` in any `> ` line.** No credential claim, no greeting, no host, no investment pick. The style-E signposts are imperatives throughout — verified individually, since this was the restyle's specific risk |
| 8 | Text-level layout lints | ✅ **after edit 2**, with three build notes below |

**Gate 8 detail.** *Chips:* every `·`-separated row measured. **1.2's third chip was 27 chars —
edited to 16 (§4).** All others clear: 1.6 max 20 · 2.6 max 10 · 3.3 max 9 · 4.6 max 17 · 5.4
max 6 · 5.8 max 19 · 5.12 max 6 · 6.5 max 4 · 6.7 max 16 · 6.8 max 20. *Cascades:* four
declared (1.2 = 3 items, 1.6 = 3, 3.3 = 4, 6.7 = 3), all ≤ `cascade.max_items` 5, all at or
above `cue_min_gap_seconds` 0.8 outside the declared cascades. *One focal element per scene:*
holds — where a cue carries both `num:` and `stmt:`, the `num:` is the focal and the `stmt:`
is subordinate, which is the archetype-B stack. **One exception to bind (below).** *Colour vs
thesis:* the thesis is "the rate is the whole difference, and dividends-only is the expensive
route" — `--warn` sits on the yield trap (4.5–4.13) and on **every** dividends-only corpus
(5.7, 5.16, 6.9), `--fund` on the 4.0% ladder, `--target` on sourced evidence. **The colour
argues *for* the thesis at every load-bearing frame.**

**Four build notes, none of them blocking:**

1. **⚠ HOOK-GATE FLAG, pre-registered — measure it, do not assume it.** The 15s pass above uses
   the flat 17.57 c/s key, which is the model of record and was measured on this very cut's
   attempt-1 audio. But **chapter 1 is punctuation-dense** — 1.2 is three sentences in 75
   chars, roughly one full stop per 25 chars against the script's overall ~1 per 65 — and
   `tts.pause_seconds` says each of those buys 0.55s of real silence the flat key averages
   away. On a pause-loaded reading the promise clause slips to ≈13.4s and the line closes
   ≈15.5s. **This is exactly how `hook_gate_hi` came in at 14.9–15.1s.** 1.1–1.3 are
   creator-approved verbatim, so no script edit is available and none was made.
   **fin-voice must ffprobe the rendered 1.3 clip and report the clause onset against the 15s
   gate before chapter 1 locks**, and record it in `run.json` as `hook_gate_en`, the same way
   the hi cut did.
2. **Scene 2.2 needs its TWO `data-framings` — ruling: adequate mitigation, and now binding.**
   155 chars → 8.8s VO + 0.8 = **9.6s**, over `max_scene_seconds` 9.0. The line is
   creator-approved verbatim and plants the tank, so it is not cut. Two framings (wide on the
   tank, then a push to the tap) mean **no single framing holds past ~4.8s**, which satisfies
   what the constant protects — felt pace and `max_static_hold_seconds` 2.0 — rather than
   evading it. It is declared in three places in the script (the timing warning, the 2.2 cue,
   build handoff 6). **`check_build` will fail this scene if the second framing is missing; do
   not add an exemption, add the framing.**
3. **3.3 is a 4-item cascade and must land as 2 + 2 rows**, not one row of four —
   `max_chips_per_row` is 3 and `.row` has `flex-wrap: wrap`, so four chips silently orphan
   3+1 and no checker flags it. The attempt-1 storyboard already established this house rule
   for its own 4-chip scenes; carry it.
4. **3.7 is the one frame carrying two figures of the same class** (`num: 33.4%` +
   `stmt: $2,189 a month`). Binding on the storyboard: **33.4% is the focal, $2,189 is set at
   sub/foot weight**, never as a second `num:`. Also note 2.14, 5.8, 6.7 and 6.8 use `·` to
   separate **clauses and figure-plus-rate pairs, not chips** — render those as `.sub` lines,
   per the storyboard's own note that "a chip crushes a figure-plus-its-rate".

**One extraction hazard, flagged because it fails silently.** This file carries ~40 guard
blockquotes against 81 VO lines, so a bare `^> ` grep sweeps in junk. **Extract by the
`**N.M**` line key** — 81 keys, verified `1.1 … 6.13` with no gap or duplicate — and run build
handoff item 1's byte-for-byte reconstruction check. Do not skip it.

**The stale storyboard.** `storyboard-en.md` is attempt 1's, built on the 78-line style-A
script, and its scene table is numbered `s1…s78` against a file that no longer exists. It must
be regenerated, not patched. Its two durable findings survive and should be carried:
4-item chip rows go 2+2, and figure-plus-rate pairs are `.sub` lines rather than chips.

---

## 7. Verdict

PASS

Chapters 1–2 are the creator-approved draft to the character, line 1.7 is intact, all fourteen
corpus lines now speak their rate including the three attempt 1 caught, and the fact base got
*stronger* on re-fetch than it was on staging — Trinity and the Bengen review read as primary
PDFs cell by cell, the whole BLS set recovered on an independent surface after three 403s, and
Wiley/August 2025 verified where attempt 1 had to retain it on trust.

Two defects, both fixed rather than failed, because neither changes a fact, a beat or a
structure and a re-run of fin-script would have reproduced the rest of the file verbatim:
**4.8 was letting the tank analogy misdescribe what Bengen and Trinity tested** — the exact
"a drawn portfolio is doomed" reading the brief exists to catch, and one that contradicted the
script's own 95%-survival line three chapters earlier — and **1.2 shipped a 27-character chip
against a 22-character cap** in a chapter that is entirely new and therefore unstoried.

Both edits land **before** any TTS call, and fin-voice was re-running all 81 clips regardless,
so the correction costs nothing. The one thing this gate could not settle from text is the
hook: measure it on the rendered audio, do not assume it.

**Downstream voice work must re-run against the edited `script-en.md` — the file hash has
changed.**
