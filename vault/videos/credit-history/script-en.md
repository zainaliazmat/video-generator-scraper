---
summary: US/English script for «Your Credit History — the file that decides your loan». 9 VO segments (blockframe-9, ~2:52 vs 165s target), USD, Brian voice, @moneymavens101. US rewrite (not a translation) — hero is the FCRA **seven-year** rule (timeline animation), money beat is the auto-loan tier spread. Every number traces to videos/credit-history/facts-staging.md, USD SET only.
updated: 2026-07-29
source: creator brief (run.json 2026-07-29) + facts-staging.md attempt 2 (USD SET); structure mirrors script-hi.md, register per knowledge/us-english-script-style.md. NO study note exists (fin-research rescued), so retention shape is inherited from the shipped en cuts (pay-yourself-first, good-debt-vs-bad-debt), not from a fresh study.
---

# «Your Credit History» — English / USA edition

**Studio project (to build):** `studio/videos/credit-history-en`
**Language:** US English, en-US. **Voice:** ElevenLabs **Brian** `nPczCjzI2devNBz1zQrb`,
`eleven_multilingual_v2`, style 0.
**On-screen text:** English. **Titles + description:** English.
**Style:** blockframe-9 motion graphics, 16:9, target 165s. Educational only — no host
persona, no first-person expertise, no card/loan/bureau/monitoring-product pick. FICO and
"credit report" appear as **terminology** (the words a viewer will actually see); Experian,
the CFPB and the FCRA appear only as **source evidence in foots**, never as a recommendation.
No lender is named anywhere.

> ### US REWRITE, NOT A TRANSLATION
> (us-english-script-style.md rule zero.) The Hindi script was read for **structure only**.
> Everything here is US-market: dollars, FICO's published weights, the **federal seven-year
> rule**, a used-car auto loan, US institutions in the foots. A rupee sign, "lakh", CIBIL, an
> Indian bank or the India cut's **thirty-six-month** figure anywhere in this file is a hard
> failure — the two markets have structurally different answers to the hero question and
> facts-staging opens with a RED FLAG saying exactly that.
>
> **The mirror of the Hindi cut's guard:** that script may never say "seven years"; **this
> one may never say "thirty-six months".** Same trap, opposite direction.

**Engine rule:** digits are **spelled out** in the VO text below (bare Latin digits are a
coin-flip TTS reading in ElevenLabs). On-screen numerals carry the exact figures,
`Intl.NumberFormat("en-US")` grouping (`$25,000`, `$12,400`).

**Colour intent (thesis-derived — the storyboard formalises this four-line table):**
`--warn` red = **the missed payment and the price it charges** (the seven-year mark, the
subprime row); `--fund` green = **the on-time payment, the low balance, the clean report,
the top tier**; `--target` amber = **the score / the report under examination**; `--pop`
orange = the do-this-today CTA. (design-finance-blockframe §2 — semantics derive from *this*
video's thesis: red is the miss and what it costs, not "credit cards" generally.)

**Per-scene tint ladder** (§2, 0.10–0.13): `en1 red .12 · en2 amber .10 · en3 amber .12 ·
en4 green .10 · en5 red .13 · en6 green .10 · en7 red .12 · en8 orange .12 · en9 green .13`.
**`ken` alternation** (§5 rule 1): `in, out, in, out, in, out, in, out, in`.

## Timing budget

English narration ≈ **15.0 chars/s** (`format.json cuts.en`). Char counts are the budget
estimate only; the build step regenerates + ffprobe-measures each clip and adds the
per-scene **0.4s lead-in / 1.0s tail** before locking scene durations.

| # | Scene | chars | est. VO |
|---|---|---|---|
| en1 | Hook — the file that reads you first | 248 | ~16.5s |
| en2 | Roadmap — four things | 152 | ~10.1s |
| en3 | Concept — the report and the score (300–850) | 302 | ~20.1s |
| en4 | Rule — what builds it (35% + 30% = 65%) | 276 | ~18.4s |
| en5 | Audit — what destroys it: **seven years** (THE HERO) | 305 | ~20.3s |
| en6 | Action — auto-pay every due date | 283 | ~18.9s |
| en7 | The math — same car, about three times the rate | 428 | ~28.5s |
| en8 | Do this today — auto-pay + read the report | 305 | ~20.3s |
| en9 | Recap + CTA | 287 | ~19.1s |
| | **VO total** | **2,586** | **~2:52** |

**Budget check:** 165s × 15.0 = **2,475 char budget**, ±10% band = **2,228–2,723**. This
draft is **2,586 (104.5%)** → **~172s VO**, i.e. ~7s over target. Rendered runtime adds
9 × 1.4s of lead-in/tail = **~185s total**, comfortably inside the short tier's 60–300s
range. If the measured TTS runs long, cut from **en7** (the only scene over 25s) — the
"Same car. Different number." closer is the keeper, "Same car, same price, two different
scores." is the trim.

---

## en1 — HOOK

**VO**
> There's a file on you that you've never read — and it decides whether you get a loan, and what interest you pay. The lender reads it before you ever walk in. It's called your credit report. And a payment you've missed can sit in it for seven years.

**On screen** — the "file you've never read" is the focal shock; the seven-year stamp lands last.
- kicker: `A file you've never read`
- huge (target): `YOUR CREDIT REPORT`
- decision strip (reveals after the huge):
  ```
  THE LOAN?          it decides
  THE RATE?          it decides
  EVER SEEN IT?      probably not
  ```
- stamp (warn): `A MISS CAN STAY 7 YEARS`

**Visuals** — bg keyword: `manila folder tabs in a filing drawer`; cut-in
`unopened mail stacked on a doormat` on «a file on you»; cut-in
`contract and pen on an office desk` on «The lender reads it». 3 bg crossfades,
slow Ken Burns push-**in**.

> **Hook-payoff clock:** the promise is paid off when the thing is named —
> «It's called your credit report» ends at **189 chars ≈ 12.6s** of VO, **≈13.0s** with the
> 0.4s lead-in. Margin to the 15s gate is ~2s. **Build advisory:** ffprobe en1 first; if the
> measured read is slower than 15 c/s, trim «and what interest you pay» from sentence one —
> never the naming.

---

## en2 — ROADMAP

**VO**
> Four things: what that report actually is, what builds it, what destroys it, and why it matters years before you ever need it. Then two moves for today.

**On screen**
- kicker: `By the end you'll know`
- chips (2×2 — max 3 per row, ≤22 chars): `WHAT THE REPORT IS` · `WHAT BUILDS IT` /
  `WHAT DESTROYS IT` · `WHY IT MATTERS EARLY`
- sub: `Then two moves for today`

**Visuals** — bg keyword: `stacked cardboard document boxes in shadow` (calmest — roadmap
rest beat, but it still carries a photo per the every-frame-has-image rule, 2026-07-28).
Ken **out**, slow.

---

## en3 — CONCEPT — the report and the score

**VO**
> First — what it actually is. Every loan, every credit card, every payment gets reported to the credit bureaus. That record is your credit report, and its summary is one three-digit number — your FICO score, from three hundred to eight hundred fifty. Six hundred seventy and up is generally called good.

**On screen** — the 300→850 scale is the single focal element.
- kicker: `First — what it actually is`
- head2: `THE REPORT = the record` → `THE SCORE = the summary`
- scale bar (the focal, `.mega` numerals at each end):
  ```
  300 ├────────────────────────────┤ 850
                 670+ = "good"
  ```
- foot: `FICO — score range 300–850 · CFPB consumer education`

**Visuals** — bg keyword: `analog gauge dial close-up` (the needle-on-a-scale read of a
score); cut-in `odometer digits close-up` on «one three-digit number». Ken **in**.

---

## en4 — RULE — what builds it

**VO**
> So what builds it? Two things do most of the work. Payment history — did you pay on time — is thirty-five percent of your FICO score. How much of your available credit you're using is another thirty percent. That's sixty-five percent of the whole thing, decided by two habits.

**On screen** — two weighted bars, then the sum. **Only 35 and 30 appear** (staging: "Only 35/30 should go on screen").
- kicker: `What builds it`
- two weight rows (cascade, 0.6s apart, fund-bordered):
  ```
  PAYMENT HISTORY    ████████████░░░░░░░░  35%
  AMOUNTS OWED       ██████████░░░░░░░░░░  30%
  ```
- huge (fund, lands on «sixty-five percent»): `65% OF YOUR SCORE`
- sub: `Two habits: pay on time · keep the balance low`
- foot (`--muted`): `FICO's published category weights; the 35% and 30% are corroborated by a Federal Reserve report to Congress. Other factors count too — these two are the biggest.`

**Visuals** — bg keyword: `wall calendar with dates circled` (on-time payments);
cut-in `credit cards fanned out of a wallet` on «your available credit». Ken **out**.

> **Deliberate omission:** no `15%` / `10%` / `10%` tail on screen or in VO. facts-staging
> tags the 15/10/10 split **SOFT-adjacent — single-sourced to myFICO** and says only 35/30
> should go on screen. The foot says "other factors count too" so the bars aren't read as
> the whole score, without asserting a weight the file can't defend.

---

## en5 — AUDIT — what destroys it (THE HERO SCENE)

**VO**
> Now, what destroys it. Under federal law, most negative information can stay on your report for seven years. A bankruptcy, ten. And here's the part people get wrong — the clock doesn't start when you finally pay it off. It starts at the original missed payment. One bad month, seven years of consequences.

**On screen** — **the timeline animation is the hero visual** (creator brief).
- kicker: `What destroys it`
- the timeline (the focal): a horizontal track with seven year-ticks. A `--warn` mark
  **slams down at year zero** and stays lit while the track fills left→right past it;
  the mark only clears as the fill crosses **YEAR 7**.
- counter running under the track: `YEAR 1 → YEAR 7`
- correction block (the thing people get wrong — struck line, then the fix):
  ```
  ~~clock starts when you pay it off~~
  CLOCK STARTS AT THE MISSED PAYMENT
  ```
- chip (warn): `BANKRUPTCY — 10 YEARS`
- foot: `Fair Credit Reporting Act, 15 U.S.C. §1681c(a) · CFPB`

**Visuals** — bg keyword: `hourglass on a dark surface` (calm, thematic — the timeline
carries the scene); cut-in `black ink mark on a white page` on «One bad month». Ken **in**.
The track must keep animating — no static hold past ~2s (§5.2).

> **The rule this scene obeys:** say **seven years**, never "forever", and never "seven
> years from when you pay it off" — the clock runs from the **original delinquency**
> (facts-staging Claim USD-3, §1681c(a)(4)). That correction is not a nicety; it is the one
> thing the internet gets wrong about this rule, so the script makes it the beat.
> **And never "thirty-six months"** — that is the India cut's figure and has no US basis.

---

## en6 — ACTION — auto-pay every due date

**VO**
> The fix is boring, and it works — auto-pay. Put every card and every loan on automatic payment, or set a calendar alert for every single due date. Remembering shouldn't be your job. And on that second habit: use a small share of your limit, and pay the full balance, not the minimum.

**On screen**
- kicker: `The fix`
- huge (fund): `AUTO-PAY` + sub `every single due date`
- flow: `EVERY CARD` → `EVERY LOAN` → `AUTO-PAY or CALENDAR ALERT`
- stamp (fund): `REMEMBERING ISN'T YOUR JOB`
- sub: `Use a small share of the limit · pay the full balance, not the minimum`

**Visuals** — bg keyword: `sticky note reminders on a corkboard`; cut-in
`wall clock in an empty room` on «every single due date». Ken **out**.
**No phone-screen photo as a background** (§7 — this has shipped wrong three times).

---

## en7 — THE MATH — same car, about three times the rate (the ~70% reward beat)

**VO**
> Now the money. Same car, same price, two different scores. Take a twenty-five-thousand-dollar used car on a six-year loan. Top credit tier: the average rate runs around six percent. Subprime: around nineteen — roughly three times the interest on the identical car. That's about a hundred seventy dollars more every month, and around twelve thousand four hundred dollars more in interest over the loan. Same car. Different number.

**On screen** — figures reveal in three anchors, punch on the last. **No decimal APR, no
quarter label, no lender name** (facts-staging Claim USD-4 on-screen rule).
- setup: `$25,000 used car · 72 months · same car, same price`
- the two rows (rounded bands only — never a decimal):
  ```
  TOP CREDIT TIER    ~6%    →   $418/mo
  SUBPRIME          ~19%    →   $590/mo
  ```
- reveal rows (build-calculator locked — see handoff #5):
  ```
  EXTRA EVERY MONTH     $172
  EXTRA INTEREST        $12,400
  ```
- huge (warn, the punch): `SAME CAR. DIFFERENT NUMBER.`
- foot: `Experian tier averages — illustrative band, not a quoted rate · payments are model output`

**Visuals** — bg keyword: `single car key on a dark textured surface` (calmest — densest
scene, §5.3); cut-in `row of used cars on a dealership lot` on «the identical car».
Ken **in**. The numbers carry the scene; keep the background nearly still.
**Sweep both photos for non-US plates, signage and right-hand-drive vehicles** — a foreign
coin shipped in the first en cut (us-english-script-style.md).

> **Why no decimal anywhere:** facts-staging records a **three-way conflict** on the
> super-prime new-car rate (three different values, all attributed to Experian) *and* a
> table whose own label contradicts the article's quarter. Every decimal is tagged SOFT;
> only the **shape** is HARD — "roughly six percent versus roughly nineteen, about three
> times", which is **arithmetic on Experian's own two used-car rows** (19.42 ÷ 6.30 = 3.08),
> **not** a quoted Experian sentence: fin-audit re-fetched the page and it carries no "three
> times higher" line. Never present the multiple as something Experian said. The dollar figures are
> model output, not a sourced statistic (COMPUTED USD-A), and the build stage recomputes them.

---

## en8 — DO THIS TODAY

**VO**
> So, two moves today. One — put every due date on auto-pay before you close this video. Two — pull up your credit report and actually read it; if there's a late mark or an account that isn't yours, dispute it. A score is built over months and years, which is exactly why you start before you need the loan.

**On screen**
- stamp (pop): `DO THIS TODAY`
- two numbered blocks:
  ```
  1  PUT EVERY DUE DATE ON AUTO-PAY
  2  PULL YOUR CREDIT REPORT AND READ IT
  ```
- sub: `A late mark or an account that isn't yours? Dispute it.`
- foot: `A score is built over months and years — start long before you need the loan`

**Visuals** — bg keyword: `desk lamp lighting a stack of printed pages`; cut-in
`hand marking a line with a red pen` on «dispute it». Ken **out**.

> **No frequency or cost claim on the report pull.** The USD SET carries no free-report
> line — the annual-free-report right in the Hindi cut is an *India* regulator claim and is
> not transferable. So the VO says "pull up your credit report", full stop: no "free", no
> "once a year", no "weekly". Contract rule — no sourced line, no number. Add it only after
> a facts pass sources the US right.

---

## en9 — RECAP + CTA

**VO**
> So — straight talk. The lender reads your report before it reads you. On-time payments and a low balance build it. One miss can sit there for seven years. And a weak score charges you triple on the same car. Then don't say nobody warned you. For money talk this straight — hit subscribe.

**On screen**
- recap chips (2×2 — max 3 per row, ≤22 chars): `READ BEFORE YOU ARE` · `ON-TIME BUILDS IT` /
  `ONE MISS = 7 YEARS` · `WEAK SCORE = 3× RATE`
- cta block (pop): `SUBSCRIBE`

**Visuals** — bg keyword: `empty highway at sunrise`. Ken **in**.
*(Not a person — the two shipped en cuts both closed on a young man with a phone; the
no-image-repeat rule §7 bars reusing either, and a face fights the CTA type.)*

---

## Fact trace (every number → facts-staging.md, USD SET)

| Number / claim in script | Where | facts-staging.md line |
|---|---|---|
| **Seven years** — most negative information | en1 stamp, en1 VO, en5 VO + timeline, en9 | Claim USD-3 — "Most negative information, **7 years**", **HARD** (15 U.S.C. §1681c(a) + CFPB, both read directly). Staging: "seven years is safe and exact"; "the strongest claim in the file and should carry the en hero." **Audit wording rule:** the sources say a bureau "generally **can** report" — so VO and stamp say **can stay / can sit**, never "every miss stays". |
| **Ten years** — bankruptcy | en5 chip | Claim USD-3 — "Bankruptcy **10 years**"; CFPB: "up to ten years" |
| Clock starts at the **original missed payment**, not at payoff | en5 VO + correction block | Claim USD-3 on-screen wording — "Do not say '7 years from when you pay it off' — the clock runs from the **original delinquency**" |
| Score is a three-digit number, **300–850** | en3 VO + scale bar | Claim USD-1 — "FICO Score range **300–850**", **HARD** (score owner + CFPB) |
| **670+** = "good" | en3 VO + scale | Claim USD-1 — "'Good' = **670–739**"; the open-ended `670+` form is used because 740+ is *better* than good, so an upper bound would read as excluding it |
| **Payment history 35%** | en4 VO + bar | Claim USD-2 — **HARD**: myFICO (score owner) and the Federal Reserve's report to Congress agree on 35% |
| **Amounts owed / utilization 30%** | en4 VO + bar | Claim USD-2 — **HARD**, same two independent sources ("consumer indebtedness accounts for about 30 percent") |
| **65% of your score** | en4 VO + huge | Claim USD-2 **Script value** — "the two biggest levers are 35% + 30% = **65% of your score**" (staging's own framing, verbatim intent) |
| **~3× the rate**, same car | en7 VO + two rows, en9 chip | Claim USD-4 — **HARD on the shape**, but as *arithmetic on the tier grid, not as a quote*: Experian's used-car rows are super prime **6.30%** and subprime **19.42%**, and 19.42 ÷ 6.30 = **3.08**. (fin-audit re-fetched the page: it contains **no "three times higher" sentence** — staging's attributed phrasing is not on it. The multiple survives because the two rows do.) |
| **~6%** top tier / **~19%** subprime (rounded, screen + VO) | en7 | Claim USD-4 on-screen rule — "say… 'roughly 6% versus roughly 21%'. **Never a decimal, never a quarter.**" Used-car row; ~19 is the rounded subprime band the dollar model is built on |
| **$25,000 · 72 months** model | en7 setup | COMPUTED USD-A — "P = **$25,000** used car, n = **72** months"; used-car row chosen because it is the widest, most relatable spread |
| **$418/mo** (top tier) · **$590/mo** (subprime) | en7 rows | COMPUTED USD-A — "Super prime: payment ≈ **$418/mo**"; "Subprime: payment ≈ **$590/mo**" |
| **$172** more every month | en7 VO + reveal | COMPUTED USD-A — "about **$172 more every month**" |
| **$12,400** more in interest | en7 VO + reveal | COMPUTED USD-A — "roughly **$12,400 more in interest**" ($17,500 − $5,100) |
| Auto-pay / calendar alert on every due date | en6, en8 | run.json `action_step` — "set every due date on auto-pay or calendar alerts" (behaviour, not a figure) |
| Pull and read your report; dispute a wrong entry | en8 | Non-numeric consumer action. **No cost or frequency claim attached** — see the en8 note |

### Deliberately NOT used (so the audit stage doesn't rediscover them)

- **Any decimal APR** — 4.55 / 6.30 / 9.67 / 13.44 / 16.01 / 21.77 and the used-car
  column. Staging tags every decimal **SOFT** and records a **three-way conflict** on the
  super-prime new-car figure (three values, all attributed to Experian) plus a table whose
  label says one quarter and whose article body says another. VO and screen carry rounded
  bands and the "three times" shape only. **No quarter label anywhere.**
- **Average US FICO score 714 / 48.1% at 750+** (Claim USD-5) — **SOFT**, single source,
  and staging's direct fetch of the release timed out. Marked "writer context only — do not
  put on screen." Omitted from VO and screen entirely.
- **The 15% / 10% / 10% weight tail** — SOFT-adjacent, single-sourced to myFICO. Staging:
  "Only 35/30 should go on screen." The en4 foot says other factors count without asserting
  a weight.
- **"upper 700s = the best offers"** — KILLED BY fin-audit (gate one). The recorded source
  (myFICO's credit-scores page) was re-fetched and backs the *band names only* — Poor <580,
  Fair 580–669, **Good 670–739**, Very Good 740–799, Exceptional 800+, each defined against
  the average US consumer. It says **nothing about lenders' best-offer cutoff**. The only
  evidence for a best-priced tier is Experian's grid, whose own note reads "VantageScore 4.0
  used" — a *different* model from the FICO scale on the en3 bar, so importing its 781+ band
  would be a cross-model conflation of the same family as the cross-market one. The scale now
  carries `670+ = "good"` alone, which is verbatim from the score owner.
- **The name "myFICO" on screen** — replaced with **FICO** in the en3 and en4 foots.
  It is FICO's consumer *subscription product*; a product name on screen in a non-price-
  evidence role is exactly what the no-recommendation gate exists to stop. FICO is the
  score's name, i.e. terminology, and publishes the weights — the citation stays true.
- **Any free-credit-report right, frequency or cost** — the USD SET has no such line. The
  India cut's annual-free-report right is a claim about an Indian regulator and does not
  transfer. No sourced line, no number.
- **"Forever" / "it never comes off"** — false under the FCRA and explicitly banned by
  staging's on-screen wording note.
- **"Seven years from when you pay it off"** — the common wrong version; en5 corrects it
  on screen instead.
- **Any named lender, card issuer, bureau product or credit-monitoring service** — Experian
  and the CFPB appear only in foots as the source of the rate data and the statute reading.
- **Blog-tier US aggregators** — capitalcounselor, theglobalstatistics, fool, financewonk,
  supermoney, nerdwallet, cnbc's state map, cars.usnews. All downstream of FICO/Experian,
  listed as rejected in staging. The myFICO Loan Savings Calculator renders client-side and
  yields nothing to a fetch — staging says do not send this stage back to it, and it wasn't.
- **The entire India set** — no rupee sign, no "lakh", no CIBIL, no Indian bank, no RBI
  figure, no home-loan rate card, and above all **not the thirty-six-month window**, which
  is India's answer to the hero question and has no US equivalent. This cut's answer is the
  federal seven-year rule. Nothing was converted, mirrored or scaled between the two sets.

---

## Build handoff

1. `assets/voice/english-lines.json` = `{en1..en9}` with **only** the VO paragraphs above
   (no markdown, no on-screen text). English, verbatim — **slice the source, never retype**.
2. TTS via `tools/tts/elevenlabs_tts.py`, voice `nPczCjzI2devNBz1zQrb` (Brian),
   `eleven_multilingual_v2`, style 0. Budget: **9 calls** of the run's 30.
3. ffprobe-measure each clip → `data-start` / `data-duration`; scene duration =
   `0.4 + clip + 1.0` (design §6). Re-check the total before locking; the four homes of the
   timing numbers must be **generated from one source**, never hand-edited. **ffprobe en1
   first** and confirm the naming beat still lands inside 15s (see the en1 note).
4. Images: keyword-matched bg for **all 9 scenes** (`photo_free_scene_ratio` = 0, creator
   rule 2026-07-28) plus the cut-ins listed per scene. **md5 the asset ledger** — no image
   may repeat across videos or channels (§7); the two shipped en cuts already burned
   `hand tapping phone banking app`, `young man … phone`, `stack of dollar bills flat-lay`,
   `dark desk with calculator and notepad`, and the Hindi credit-history cut burned the
   archive-files / envelope / ruled-statement / red-stamp / calendar-page set. **Sweep every
   photo for non-US currency, plates, signage and right-hand-drive vehicles.**
   No phone-screen photo as a background (§7).
5. **en7 figures are calculator output, not script constants.** Regenerate `$418`, `$590`,
   `$172` and `$12,400` from the USD model (`EMI = P·i·(1+i)^n / ((1+i)^n − 1)`,
   P = $25,000, n = 72, i = APR/12, APRs 6.30% and 19.42% from the Experian used-car tier
   rows) and lock the integers. On-screen numerals must equal that run; the VO stays a round
   anchor ("about a hundred seventy", "around twelve thousand four hundred") regardless.
   `en-US` grouping. **If you change P or n, recompute — do not scale by hand** (staging's
   instruction on COMPUTED USD-A). The on-screen rate labels stay rounded (`~6%`, `~19%`)
   even though the model runs on the decimals.
6. **en5's seven-year timeline is the hero animation** — a track with seven year-ticks, a
   `--warn` mark slammed at year zero that stays lit while the fill sweeps past it and only
   clears at YEAR 7, with the `YEAR 1 → YEAR 7` counter beneath. It must still be moving at
   every point in the scene (§5.2, no static hold > ~2s). The struck-through correction line
   reveals after the mark lands, not with it (one focal at a time, §5.4).
7. Anchor cues to **word-level timings** (faster-whisper), not character-offset
   interpolation (§6). The cut-ins above name the exact VO word they land on.
