---
summary: fin-audit gate-one verdict for credit-history hi cut, attempt 1. All 8 checks hold after 3 audit edits (two over-length recap chips, one over-tight score-band label). Every load-bearing ₹ figure re-verified independently of facts-staging; the RBI free-annual-report right was confirmed from fetched regulator text, and the 36-month hero survived a two-pass source-domain re-check.
updated: 2026-07-29
source: fin-audit attempt 1 — independent re-fetch/re-check of RBI (CIC) Directions 2025 text, cibil.com source-domain search (2 passes), 9 independent lender restatements of the 36-month DPD window, Bank of India's own CIBIL-band rate card, plus a hand re-derivation of the EMI model
---

# Audit — credit-history / hi / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

**Environment note, recorded because it shapes every row below:** from this
runner, effectively the whole Indian financial web refuses a direct fetch —
`cibil.com` 403, `rbi.org.in` 403, `unionbankofindia.co.in` ECONNREFUSED,
`bankofmaharashtra.in` ECONNREFUSED, `sbi.co.in` empty, `bankofbaroda.in`
ECONNREFUSED, and every `*.bank.in` lender blog 403. This is a bot-block /
network wall, **not** a missing figure. Where the recorded URL could not be
read, the number was re-checked against (a) the source domain via
domain-restricted search, and (b) at least one *independent* primary that this
run had never cited. Nothing below is graded on the staging text alone.

| Number in script | Re-fetch / re-check result |
|---|---|
| CIBIL score = 3-digit, **300–900** (s3 VO + scale) | CONFIRMED. `cibil.com` 403s on direct fetch; two independent domain-restricted passes over cibil.com return "CIBIL Score is a 3 digit numeric summary of your credit history … ranges from 300 to 900" (`/faq/credit-score-and-loan-basics`, `/blog/what-is-cibil-score`). Traces to HARD Claim ₹-1. |
| **700+** generally good (s3 VO + scale) | CONFIRMED. Same source-domain pass: "a score above 700 is generally considered good." Traces to Claim ₹-1. |
| **750–800 = best pricing** (s3, screen only) | **NOT CONFIRMED AS WRITTEN → REWRITTEN to `750+ = best pricing`.** Staging's line is "best pricing *starts around* 750–800". Every lender card re-checked this run puts the *best* band at **800 & above** (Bank of India 800+ = 7.80% vs 750–799 = 7.90%; Union Bank 800+ = EBLR−0.60 vs 750–799 = EBLR−0.45) or at "750 & above" (Bank of Maharashtra). A closed `750–800` label therefore reads as *excluding* the band that actually gets the best price — inverted for the best-off viewer. `750+` is what the cards support. |
| **36 months** month-by-month record, one miss visible 3 years (s5 hero, s9) | CONFIRMED — the strongest survivor in the file. Two independent source-domain passes over cibil.com return the same sentence from `/blog/failed-credit-card-payments`: a missed payment "remain[s] visible on your credit report for 36 months" and "will always be a part of your credit history". Independently corroborated by **nine** lenders' own DPD explainers (Bank of Baroda, Kotak, IndusInd, ICICI, IDFC First, HDFC, Yes, Ujjivan SFB, Axis — each on the RBI-mandated `.bank.in` TLD), all describing a rolling 36-entry DPD grid in the CIBIL report. Staging tagged this SOFT/single-sourced; after this pass it is materially stronger than staging claimed. |
| "will always be a part of your credit history" (s5 quote + foot) | CONFIRMED as CIBIL's own framing via both source-domain passes. ⚠ One residual: a global exact-phrase search does not surface the string (cibil.com is crawl-hostile), and the two passes differ by one article ("a"). Substance is safe; the **exact quotation marks** are the only thing carrying risk, and the VO already paraphrases it ("सिबिल के अपने शब्दों में") rather than quoting. Kept. |
| **~1 percentage point** spread, same loan/same bank, on score alone (s7) | CONFIRMED, and the script is the conservative side of it. Both recorded rate cards are network-unreachable, so the claim was re-checked against a **third lender's own document that this run had never cited** — Bank of India's *CIBIL Based Rate of Interest* card (`bankofindia.bank.in`): 800+ **7.80%**, 750–799 **7.90%**, 700–749 **8.00%**, below 700 **9.45%** (salaried) = a **1.65 pp** top-to-below-700 spread. The script says "क़रीब एक परसेंट", i.e. below what the independent card shows. Staging's 0.75–1.00 pp band holds. |
| **₹30,00,000 · 240 months**, **₹1,390–₹1,860**/mo, **₹3.3–4.5 lakh** interest (s7) | RE-DERIVED BY HAND, all four match. `EMI = P·i·(1+i)^n/((1+i)^n−1)`, P = 30,00,000, n = 240: @7.40% ≈ **₹23,984** (staging 23,986); @8.15% ≈ **₹25,374** (staging 25,373) → Δ **₹1,390**; @8.40% ≈ **₹25,846** → Δ **₹1,862** ≈ 1,860. Total-interest deltas ≈ **₹3.34 lakh** and **₹4.47 lakh** → the on-screen 3.3–4.5 lakh is correct, not rounded up. VO speaks only the round anchor "क़रीब पंद्रह सौ", which sits inside the range. |
| **One free full credit report per calendar year, from each bureau** (s8 VO + block) | CONFIRMED — and this is the one figure whose regulator text was actually **fetched** this run. `rbi.org.in` 403s, but the **RBI (Credit Information Companies) Directions, 2025** text reproduced verbatim on a readable mirror reads: "The CIC shall provide access in an electronic format, upon request and after due authentication of the requester, to one Free Full Credit Report (FFCR) including credit score, once, at any time, during a year (January – December), to individuals whose credit score is available with them." Staging tagged Claim ₹-5 SOFT ("regulator text was never read"); the free-annual-report leg is now read. Per-bureau wording in the script matches "The CIC shall…". |
| Dispute a wrong entry (s8) | Non-numeric; route exists per CIBIL's own CICRA line in staging. No screen number attached. Fine. |

**The claim that was hunted for and is correctly absent:** no "7 years", no
CICRA auto-delete, no FICO percentage weight, no RBI ₹100/day or fortnightly
line appears anywhere in the script — grep-confirmed (the only hits are the
guard blockquotes that forbid them). This is the injected-plausible-RBI-line
attack surface for this topic and the script is clean of it. Incidentally, the
same fetched Directions text **does** support the ₹100/day compensation and the
15th/last-day fortnightly reporting that staging omitted for lack of a primary —
recorded for a future cut, deliberately **not** added here (it would rewrite VO
and re-time the scene for no gate).

## Other checks

2. **Char budget:** 165s × 12.5 c/s = **2,063 ±10% (1,856–2,269)**. Script table totals **~2,110 (+2.3%)**. Independently re-counted s1 (≈211 vs the table's 212) and s7 (≈306 vs 310) — the table's estimates are honest, not padded. Inside the band. Build still ffprobe-measures before lock.
3. **Hook payoff ≤15s:** PASS, tight. The promise ("a report you've never seen decides your loan and your rate") is paid off when the thing is named — «नाम है — क्रेडिट रिपोर्ट» ends at **≈13.4s** of VO (168 chars @ 12.5 c/s), **≈13.8s** with the 0.4s lead-in. The on-screen focal `YOUR CREDIT REPORT` reveals earlier still. Margin is ~1.2s: at a measured 11.5 c/s it slides to ≈15.2s. **Mandatory build advisory** — ffprobe s1 and keep the naming inside 15s; if TTS runs slow, trim the first sentence's «पर वो तय करती है कि» clause, never the naming.
4. **No product/platform recommended:** CIBIL / TransUnion CIBIL appear only as terminology and as source evidence in foots; **no bank is named anywhere** in VO or on screen (the three lender cards live only in the staging file and in this audit). No card, loan, app or bureau subscription is picked. Pass.
5. **Currency purity:** zero `$` in the whole file — grep-confirmed, including code fences, tables and claim IDs (attempt 2's `Claim US-n` rename holds). ₹ only. Pass.
6. **VO text hygiene:** zero Latin or Devanagari digits inside the nine VO paragraphs (every figure spelled out: छत्तीस, तीन सौ, नौ सौ, पंद्रह सौ, तीस लाख); zero `(n:n)` cite refs. The `§` refs and digits that exist are in prose/visual notes, which TTS never sees. Pass.
7. **Persona:** grep-clean for मैं / मैंने / मेरा / मेरी / मेरे — no host, no first-person expertise. No investment pick: the actions are auto-pay and pull-your-report, i.e. behaviour, not an instrument. Subscribe is the channel CTA. Pass (monetisation gate held).
8. **Layout lints:** one focal per scene ✓ (s5's `huge` lands sequentially on «छत्तीस महीने», it does not compete with the grid); s4's 4-row cascade ≤5 items at 0.6s, inside `cascade.gap_seconds` ✓; no other cue declares a sub-0.8s gap ✓; ≤3 chips per row ✓. **VIOLATIONS:** two s9 recap chips at **23 chars** > `max_chip_chars` 22 → fixed by edit. Colour intent (red = the miss and its price, green = on-time/clean/top band, amber = the score under examination, orange = CTA) does not argue against the thesis; the storyboard does not exist yet, so its table inherits this and must be re-checked at fin-storyboard.

## Edits made (script-hi.md — downstream must re-run against the edited script)

1. **s9 chip:** `THE BANK READS IT FIRST` (23) → `BANK READS IT FIRST` (19). Over `max_chip_chars`.
2. **s9 chip:** `A LOW SCORE COSTS LAKHS` (23) → `LOW SCORE COSTS LAKHS` (21). Over `max_chip_chars`.
3. **s3 scale label:** `750–800 = best pricing` → `750+ = best pricing`, plus the matching fact-trace row now records why. The closed range contradicted every lender card re-checked this run, all of which price 800+ best or equal-best.

All three are **on-screen text only — the nine VO paragraphs are byte-identical**, so the TTS audio is unaffected. The script hash changes, so the pipeline gate must re-acknowledge and storyboard/build must pick up the corrected strings.

Nothing was killed: every number traced to a staging line and survived an independent re-check, one was narrowed to the form its sources actually support.
