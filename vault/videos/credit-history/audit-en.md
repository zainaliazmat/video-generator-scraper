---
summary: fin-audit gate-one verdict for credit-history en cut, attempt 1. PASS after 6 audit edits — one on-screen claim killed (its recorded source does not back it), one product name removed from screen, two VO overstatements tightened, two false-citation rows corrected. Every load-bearing USD figure was re-fetched from its recorded URL and survives; the FCRA seven-year hero is the strongest claim in the file.
updated: 2026-07-29
source: fin-audit attempt 1 — independent re-fetch of Cornell LII 15 U.S.C. §1681c, CFPB Ask-CFPB en-323, myFICO whats-in-your-credit-score, myFICO credit-scores, Federal Reserve report to Congress on credit scoring, Experian average-car-loan-rates-by-credit-score (two passes), plus a hand re-derivation of the COMPUTED USD-A loan model
---

# Audit — credit-history / en / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

Every URL below was fetched by **this** stage, not read out of `facts-staging.md`.
Unlike the hi cut (where the entire Indian financial web refused this runner),
**every recorded US source was readable**, so there is no "confirmed via search
index" row in this table. Nothing is graded on the staging text.

| Number in script | Re-fetch result |
|---|---|
| **Seven years** — most negative info (en1, en5 hero, en9) | **CONFIRMED, twice, verbatim.** Cornell LII §1681c(a): "Any other adverse item of information … which antedates the report by more than seven years"; "Accounts placed for collection … which antedate the report by more than seven years". CFPB en-323: "A credit reporting company generally can report most negative information for seven years." Strongest claim in the file — correctly carries the hero. |
| **Ten years** — bankruptcy (en5 chip) | **CONFIRMED, twice.** §1681c(a)(1): "Cases under title 11 … antedate the report by more than 10 years." CFPB: "Bankruptcies can stay on your report for up to ten years." |
| Clock starts at the **original missed payment**, not payoff (en5 VO + correction block) | **CONFIRMED from the statute text.** §1681c(a)(4) runs the period from "the commencement of the delinquency which immediately preceded the collection activity" (+180 days), i.e. from the delinquency, never from payment. The one thing the internet gets wrong about this rule, and the script makes it the beat. |
| **300–850** FICO range (en3 VO + scale) | **CONFIRMED verbatim:** myFICO — "Most credit scores have a range from 300 to 850." |
| **670+ = "good"** (en3 VO + scale) | **CONFIRMED verbatim:** myFICO — "A 'good' credit score is considered to be in the 670-739 score range." The open-ended `670+` form is right: 740–799 and 800+ are *better* than good, so a closed range would read as excluding them. |
| **35%** payment history (en4 VO + bar) | **CONFIRMED, two independent fetches.** myFICO: "Payment history: 35%". Federal Reserve report to Congress: "payment history characteristics … accounting for about 35 percent of the FICO score's predictive accuracy". |
| **30%** amounts owed (en4 VO + bar) | **CONFIRMED, same two.** myFICO: "Amounts owed: 30%". Fed: "consumer indebtedness accounts for about 30 percent". |
| **65% of your score** (en4 huge) | Arithmetic on the two confirmed weights. Fine. |
| **~6% / ~19%**, used car (en7) | **CONFIRMED from the Experian grid:** super prime (781+) used **6.30%**, subprime (501–600) used **19.42%**. The script's rounded bands sit on the confirmed rows and no decimal or quarter reaches the screen. |
| **~3× the rate** (en7 VO, en9 chip) | **SURVIVES — but its attribution did not.** 19.42 ÷ 6.30 = **3.08**, so the multiple is sound *as arithmetic on two confirmed rows*. However the Experian page **contains no "three times higher" sentence**; staging asserted that framing and fin-script repeated it twice. Re-fetched with a targeted second pass to be sure. **Rewrote both trace lines** — the multiple stays, the fake quote goes. |
| **$25,000 · 72 months · $418 · $590 · $172 · $12,400** (en7) | **RE-DERIVED BY HAND, all match.** `EMI = P·i·(1+i)^n/((1+i)^n−1)`, P = 25,000, n = 72: @6.30% → **$417.87/mo**, interest **$5,087**; @19.42% → **$590.44/mo**, interest **$17,512**. Δ/mo = **$172.6**, Δ interest = **$12,425**. On-screen $172 / $12,400 and the VO's round anchors are correct and not rounded in the flattering direction. |
| Auto-pay every due date · pull and read your report (en6, en8) | Non-numeric behaviour from `run.json`. No cost, no frequency, no "free" attached — correct, the USD SET has no free-report line and the India right does not transfer. |

**The claim hunted for and correctly absent:** no "thirty-six months", no CIBIL,
no rupee glyph, no RBI line, no imported India rate card — grep-confirmed; the
only hits are the guard blockquotes that forbid them. This topic's cheapest
attack is a plausible dated statute line moved across markets, and the file is
clean of it in both directions.

## What was KILLED, and why

1. **`upper 700s = the best offers`** (en3 scale, screen only) — **KILLED.** Its
   recorded source (myFICO credit-scores) was re-fetched and backs the band
   *names* only: Poor <580, Fair 580–669, Good 670–739, Very Good 740–799,
   Exceptional 800+, each defined against the average US consumer. The page says
   **nothing about lenders' best-offer cutoff**. The only evidence for a
   best-priced tier is Experian's grid — whose own source note reads
   "**VantageScore® 4.0 used**", a *different scoring model* from the FICO scale
   the en3 bar draws, so importing its 781+ band would be a cross-model
   conflation of the same family as the cross-market trap this run exists to
   stop. The scale keeps `670+ = "good"`, which is verbatim from the score owner.
   A claim whose source doesn't back it dies whatever staging says.

## What was REWRITTEN, and why

2. **en1 VO** — "And **every** payment you've missed **is sitting** in it for
   seven years" → "And **a** payment you've missed **can sit** in it for seven
   years." Both sources say a bureau *generally **can** report* most negative
   information for up to seven years. "Every … is sitting" asserts universality
   and certainty the statute does not: sub-30-day lateness is commonly never
   furnished, and items can come off earlier. The hook keeps its punch (the
   number is untouched) and the payoff clock is unaffected — the naming beat
   still ends at char 189.
3. **en1 stamp** — `EVERY MISS STAYS 7 YEARS` → `A MISS CAN STAY 7 YEARS`. Same
   overstatement, on screen, in the highest-contrast element of the hook.
4. **en6 VO** — "And on that **thirty percent**: use a small share of your limit"
   → "And on that **second habit**: …". The 30% is verified *as a score weight*;
   parked next to a utilisation instruction it silently reads as the folk "keep
   utilisation under 30%" rule, which **no source in this file supports**. A
   verified number smuggling in an unverified claim is still an unverified
   claim. en4 already carries the weight, so nothing is lost.
5. **en3 + en4 foots** — `FICO / myFICO` → `FICO`; `myFICO category weights` →
   `FICO's published category weights`. myFICO is FICO's consumer *subscription
   product*; a product name on screen in a non-price-evidence role is what the
   no-recommendation gate exists to stop. FICO is the score's name (terminology,
   already permitted) and publishes the weights, so the citation stays true.
6. **Two fact-trace rows + the en7 blockquote** — the "Experian's own framing …
   'three times higher'" attribution is **not on the fetched page** and is now
   replaced by the arithmetic that is: 19.42 ÷ 6.30 = 3.08. A false citation in
   the trace is how a fake quote gets promoted into `money-facts-2026.md` later.
   The instruction "never present the multiple as something Experian said" is now
   written into the script.

Char table, budget line and frontmatter were updated to match (en1 255→**248**,
en6 285→**283**, total 2,595→**2,586**).

## The other seven checks

2. **Char budget:** 165s × 15.0 = **2,475**, band **2,228–2,723**. Post-edit total **2,586 (104.5%)** → ~172s VO, ~185s rendered, inside the short tier's 60–300s. Hand-recounted en1 (**248**), en5 (**305**, table says 305) and en7 (**429** vs the table's 428) — the estimates are honest, not padded. PASS.
3. **Hook payoff ≤15s:** PASS, tight. The promise is paid when the thing is named — «It's called your credit report» ends at **189 chars ≈ 12.6s**, **≈13.0s** with the 0.4s lead-in; ~2s margin. Verified by counting the string myself, not by trusting the note. **Build advisory stands:** ffprobe en1 first; below ~12.6 c/s measured, the naming slides past 15s — trim «and what interest you pay», never the naming.
4. **No product/platform recommended:** PASS after edit 5. FICO and "credit report" are terminology; Experian appears only as the source of the rate data (price evidence, exactly the permitted role); CFPB and the FCRA are regulator/statute evidence in foots. No card, lender, bureau product, monitoring service or report-pulling site is named anywhere — notably en8 says "pull up your credit report" without naming a site.
5. **Currency purity:** zero `₹` in the file — whole-file grep, including code fences, tables and claim IDs (`Claim USD-n` naming holds). `$` only. PASS.
6. **VO hygiene:** zero bare Latin digits in the nine VO paragraphs — every figure spelled (seven, ten, three hundred, eight hundred fifty, six hundred seventy, thirty-five, thirty, sixty-five, twenty-five-thousand-dollar, six-year, six, nineteen, three, a hundred seventy, twelve thousand four hundred). Zero `(n:n)` cite refs. The `§1681c(a)` refs live in an on-screen foot and in prose notes, which TTS never sees. PASS.
7. **Persona:** grep-clean for I / I've / my / me / we / our — no host, no first-person expertise, no credential claim. Actions are behavioural (auto-pay, read your report, dispute an error), not instruments: **no investment pick**. "Then don't say nobody warned you … hit subscribe" is the established channel sign-off on all three en cuts, second-person, not a persona. Monetisation gate held. PASS.
8. **Layout lints:** one focal per scene ✓ (en1 `huge`, en3 `.mega` scale — never `.huge`+`.mega` together, en5 the timeline with the correction block revealing *after* the mark lands, en7 the punch `huge` last); en4's 2-item cascade at 0.6s is declared and inside `cascade.gap_seconds` [0.6, 0.7] and ≤5 items ✓; no other cue declares a sub-0.8s gap ✓; chips 2×2 in en2/en9, longest **20** chars, en5's chip **21** — all ≤3 per row and ≤22 chars ✓ (counted, not eyeballed — the hi cut failed exactly here). Colour intent (red = the miss and what it costs · green = on-time/low balance/clean/top tier · amber = the score under examination · orange = CTA) does not argue against the thesis; `storyboard-en.md` does not exist yet, so its four-line table inherits this and **must be re-checked at fin-storyboard**. PASS.

## Advisories for downstream (not gate failures)

- **`max_simultaneous_elements` = 6 is at risk in en5 and en7** if every element
  holds to scene end (en5: kicker + track + counter + correction block + chip +
  foot; en7: setup + 2 rate rows + 2 reveal rows + huge + foot). Both scenes are
  written as sequenced reveals, so the storyboard must retire earlier elements
  rather than stack all of them.
- **en1's decision strip (3 rows), en7's reveal rows and en8's two numbered
  blocks carry no declared gap.** Storyboard must either declare them cascades
  (≤5 items at 0.6–0.7s) or space them ≥0.8s.
- **Experian's tier grid is VantageScore 4.0-based** (its own source note),
  while en3's scale is FICO. The script never claims the tiers are FICO bands
  and puts no score numbers in en7, so nothing on screen is wrong — but no
  future edit may put a FICO band number next to those APRs.
- **The Federal Reserve corroboration is from August 2007.** True as stated
  ("corroborated by a Federal Reserve report to Congress") and the current
  primary is myFICO, so the foot stands; do not re-date it upward.
- **$172 rounding:** the model gives $172.6. If the build rounds the *difference*
  it prints $173 and disagrees with the screen. Round each payment first
  ($590 − $418 = $172), per handoff #5.

All six edits are recorded above. Nothing else was cut: every remaining number
traces to a staging line **and** survived a fetch of its own recorded source.
