---
slug: credit-history
stage: fin-facts
attempt: 2
status: ok
updated: 2026-07-29
scope: Money + record-retention facts for the "your credit history" short, sourced independently per market (₹ set for hi cut, $ set for en cut). NEVER convert or mirror between markets — see the RED FLAG section, the US 7-year rule has no Indian equivalent.
one-write-rule: staged only — orchestrator promotes to vault/knowledge/money-facts-2026.md after the render passes. Do NOT read this as already-promoted.
---

# facts-staging — credit history (CIBIL / FICO)

Creator brief (run.json): hook "An invisible record decides whether you get a
loan."; beats = what it is / what builds it / what destroys it / why it matters
before you need it. Hero (both cuts): **one missed payment stays visible for
years** — timeline animation. Action step: auto-pay every due date.

Every figure carries date + sources + a HARD/SOFT tag. The ₹ set and the $ set
were sourced **separately**.

---

## ⚠ RED FLAG — THE CROSS-MARKET TRAP IN THIS TOPIC (read before scripting)

The hero beat is "how long does it stay visible". **The two markets have
structurally different answers, and the internet will tell you they are the
same. They are not.**

| | USA | India |
|---|---|---|
| Rule | **7 years**, statutory auto-delete | **No statutory auto-delete exists** |
| Basis | FCRA 15 U.S.C. §1681c(a) | CICRA 2005 sets a *minimum* preservation, no maximum |
| What the report shows | negative item drops off at 7 yr | rolling **36-month** month-by-month payment grid; the account history itself persists |

Dozens of Indian blogs state "under CICRA 2005 the negative entry must be
removed after 7 years." **No primary source was found for that.** The one
industry-press account of the actual law says the opposite: CICRA obliges
bureaus to hold data for *at least* seven years with **no maximum**, which is
why the RBI opened a consultation on capping the preservation period at all.
See Claim ₹-3. **Do not put "7 years" in the Hindi cut.**

Second trap: **FICO publishes percentage weights (35% payment history, 30%
amounts owed). CIBIL does not publish weights.** Do not put "35%" on screen in
the Hindi cut. See Claim ₹-2.

---

## $ SET — USA (en cut)

### Claim $-1 — FICO score range and bands
- **Figure:** FICO Score range **300–850**. "Good" = **670–739**; **800+** = "exceptional"; lenders' best-offer cutoff sits in the **upper 700s**.
- **Date:** current, July 2026.
- **Sources:**
  1. **myFICO / FICO** (primary — the score's owner defines its own range): https://www.myfico.com/credit-education/credit-scores — "Most credit scores have a 300-850 score range."
  2. **FICO corporate blog** on the 850 ceiling: https://www.fico.com/blogs/perfect-credit-score-understanding-850-fico-score
  3. **CFPB** consumer education poster "Understanding credit scores" (regulator): https://files.consumerfinance.gov/f/documents/cfpb_building_blocks_activities_understanding-credit-scores_poster.pdf
- **Tag:** **HARD** (definitional, from the score's owner, plus regulator corroboration).

### Claim $-2 — What the FICO score is made of
- **Figure:** **Payment history 35%** · **Amounts owed (utilisation) 30%** · Length of credit history 15% · Credit mix 10% · New credit 10%.
- **Date:** current, July 2026 (myFICO read 2026-07-29). Weights unchanged for two decades.
- **Sources (two independent):**
  1. **myFICO** (primary, fetched directly): https://www.myfico.com/credit-education/whats-in-your-credit-score — verbatim category weights above.
  2. **Federal Reserve Board, *Report to the Congress on Credit Scoring and Its Effects on the Availability and Affordability of Credit*** (regulator, independent of FICO): https://www.federalreserve.gov/boarddocs/rptcongress/creditscore/general.htm — "Payment history accounts for about **35 percent** of the FICO score's predictive accuracy, consumer indebtedness accounts for about **30 percent**, and length of credit history accounts for **15 percent**." ⚠ the report is from **2007** — it corroborates the top three weights, not the 10/10 split, and is old. It is cited as independent confirmation of the two load-bearing numbers only.
  3. **CFPB, "What is a FICO score?"** (regulator): https://www.consumerfinance.gov/ask-cfpb/what-is-a-fico-score-en-1883/
- **Tag:** **HARD** for the 35% and 30% figures (score owner + Federal Reserve agree). **SOFT-adjacent** for the 15/10/10 tail — single-sourced to myFICO. Only 35/30 should go on screen.
- **Script value:** "the two biggest levers are 35% + 30% = **65% of your score**" — pay on time, keep the balance low. That single line covers the whole "what builds it" beat.

### Claim $-3 — How long a missed payment stays (THE HERO CLAIM)
- **Figure:** Most negative information, **7 years**. Bankruptcy **10 years**. Civil judgments: 7 years *or* until the statute of limitations expires, **whichever is longer**. Collections: 7 years from the delinquency that led to collection.
- **Date:** statute current 2026 (FCRA as amended; FTC republished text March 2026).
- **Sources (two independent primaries, both read directly):**
  1. **15 U.S.C. § 1681c(a)** — the statute itself, via Cornell LII: https://www.law.cornell.edu/uscode/text/15/1681c — "Any other adverse item of information, other than records of convictions of crimes which antedates the report by more than seven years"; "Cases under title 11 … antedate the report by more than 10 years."
  2. **CFPB, Ask CFPB** (regulator): https://www.consumerfinance.gov/ask-cfpb/how-long-does-negative-information-stay-on-my-credit-report-en-323/ — "A credit reporting company generally can report most negative information for seven years"; "Bankruptcies can stay on your report for up to ten years."
- **Tag:** **HARD** — statute + regulator, read directly, in agreement. **This is the strongest claim in the file and should carry the en hero.**
- **On-screen wording:** "**seven years**" is safe and exact. Do not say "forever". Do not say "7 years from when you pay it off" — the clock runs from the **original delinquency**, not from payment (per §1681c(a)(4) collections language).

### Claim $-4 — What bad credit costs: auto loan APR by credit tier (THE MONEY)
- **Figure (Experian tier grid, new / used vehicle APR):**

  | FICO band | Tier | New | Used |
  |---|---|---|---|
  | 781–850 | Super prime | **4.55%** | **6.30%** |
  | 661–780 | Prime | 6.23% | 8.77% |
  | 601–660 | Near prime | 9.67% | 14.03% |
  | 501–600 | Subprime | 13.44% | 19.42% |
  | 300–500 | Deep subprime | **16.01%** | **21.77%** |

- **Date:** ⚠ **AMBIGUOUS.** The Experian article body says "in the first quarter (Q1) of 2026" and is dated 2026-07-13, but the table's own label reads "as of Q1 2025". **Do not put a quarter label on screen.**
- **Sources:**
  1. **Experian, "Average Car Loan Interest Rates by Credit Score"** (fetched directly), restating **Experian State of the Automotive Finance Market** — Experian *is* the primary owner of this dataset: https://www.experian.com/blogs/ask-experian/average-car-loan-interest-rates-by-credit-score/
  2. **LendingTree** (independent — its own marketplace loan-request data, not Experian's): https://www.lendingtree.com/auto/refinance/rates-by-credit-score/ — average auto rate at a **700 credit score = 8.22% new / 10.75% used**. Sits in the same place as Experian's prime band (661–780: 6.23% / 8.77%), a little higher; **corroborates the shape, not the decimals.**
  3. **Bankrate** (independent weekly rate survey): https://www.bankrate.com/loans/auto-loans/average-car-loan-interest-rates-by-credit-score/ and https://www.bankrate.com/data-center/auto-loan/ — 60-month new-car average **6.96%** as of **2026-07-23**.
- ⚠ **RECORDED CONFLICT (all kept, none picked):** three different values for super-prime / "excellent credit" new-car APR are in circulation, **all attributed to Experian**: **4.55%** (Experian's own page), **4.66%** (search-surfaced restatement), **4.88%** (via Bankrate). This is exactly why no decimal goes on screen.
- **Tag:** **SOFT on any exact decimal** (date ambiguity + a three-way conflict). **HARD on the shape**: super-prime used-car money costs roughly **6%** and deep-subprime roughly **22%** — Experian's own framing is that deep-subprime used rates are "**three times higher**" than super prime, and LendingTree/Bankrate independently land in the same band structure.
- **On-screen rule:** say "**about three times the interest rate for the same car**" or "roughly 6% versus roughly 21%". Never a decimal, never a quarter.

### Claim $-5 — Average US FICO score (context only, not for screen)
- **Figure:** **714** (down 2 points YoY); record **48.1%** of consumers at 750+.
- **Date:** FICO Score Credit Insights, **Spring '26 edition, released 2026-03-24**. Decline attributed mainly to resumed federal student-loan delinquency reporting.
- **Sources:** FICO investor relations release: https://investors.fico.com/news-releases/news-release-details/ficor-score-credit-insights-report-average-fico-score-dips-714/ — **direct fetch timed out; figures are from the search index of that release, not read.**
- **Tag:** **SOFT** (single source, not read directly). Writer context only — do not put on screen.

### COMPUTED $-A — the en money translation
Tagged **COMPUTED**, not a sourced statistic. Derived from Claim $-4 rates.
- **Model:** standard amortising loan, `EMI = P·i·(1+i)^n / ((1+i)^n − 1)`, P = **$25,000** used car, n = **72** months, i = APR/12. Used-car row chosen because it is the widest, most relatable spread.
- **Super prime @ 6.30%:** payment ≈ **$418/mo**, total interest ≈ **$5,100**.
- **Subprime @ 19.42%:** payment ≈ **$590/mo**, total interest ≈ **$17,500**.
- **The line:** same car, same price — **about $172 more every month and roughly $12,400 more in interest.**
- Build stage must recompute with code and lock exact integers; figures here are model-anchored, not false-precise. If fin-script changes P or n, recompute — do not scale by hand.

---

## ₹ SET — India (hi cut)

### Claim ₹-1 — CIBIL score range
- **Figure:** TransUnion CIBIL Score = a three-digit number from **300 to 900**. Above ~**700** is generally treated as good; lenders' best pricing starts around **750–800**.
- **Date:** current, July 2026.
- **Sources:**
  1. **TransUnion CIBIL** (primary — the score's owner): https://www.cibil.com/blog/what-is-cibil-score and https://www.cibil.com/faq/credit-score-and-loan-basics — "ranges from 300 to 900". *cibil.com blocks direct fetch (HTTP 403); text obtained via domain-restricted search of cibil.com itself.*
  2. **Union Bank of India** and **Bank of Maharashtra** published rate cards (Claim ₹-4) price loans in bands running from below-600 up to 800+, independently confirming the same scale in commercial use.
- **Tag:** **HARD** (definitional primary + two lenders' price cards using the scale).

### Claim ₹-2 — What CIBIL says drives the score
- **Figure:** Four named factors, **no published percentage weights**: **payment history**, **credit utilisation**, **age of credit**, **credit enquiries** — plus **credit mix** (secured loans viewed more favourably than a large number of unsecured ones).
- **Date:** current, July 2026.
- **Sources:** TransUnion CIBIL (primary, via domain-restricted search of cibil.com): https://www.cibil.com/blog/all-you-need-to-know-about-cibil-score · https://www.cibil.com/faq/understand-your-credit-score-and-report
- **Tag:** **HARD (terminology).**
- **DO NOT:** put **35% / 30%** (or any percentage weight) on screen in the Hindi cut. Those are **FICO's published weights for FICO's score** (Claim $-2). CIBIL does not publish weights. Reusing them is exactly the cross-market conversion this stage forbids. The hi cut says *which* factors, ranked, without numbers.

### Claim ₹-3 — How long a missed payment stays visible (THE HERO CLAIM — and the correction)
- **Figure:** A missed payment remains **visible on the CIBIL report for 36 months (3 years)** of month-by-month payment history. CIBIL's own wording adds that it "will always be a part of your credit history" even after that window. **There is no statutory auto-delete.**
- **Date:** current, July 2026.
- **Sources:**
  1. **TransUnion CIBIL** (primary, via domain-restricted search of cibil.com): 36-month visibility of missed payments; and — separately — "as per the Credit Information Companies (Regulation) Act 2005, no correction, deletion or addition to any information in the database can be made by CIBIL without confirmation from the concerned bank/financial institution." https://www.cibil.com/blog/failed-credit-card-payments · https://www.cibil.com/credit-score-repair · https://www.cibil.com/faq/credit-score-and-loan-basics
  2. **BIIA (Business Information Industry Association)**, industry press, on the actual statutory position: under **CICRA 2005 bureaus must report loan data for at least seven years, with no maximum limit specified**, which "resulted in some agencies reporting data up to 25 years old"; RBI wrote to bureaus and banks seeking views on a maximum preservation period and **no conclusion had been reached**. https://www.biia.com/india-retention-period-of-loan-information-held-at-credit-bureaus-under-discussion/ — ⚠ **dated 2015-09-08.** Recorded as the only account found of what the Act actually says; the 7-year *minimum, no maximum* reading is the load-bearing part.
  3. **CICRA 2005 primary text** — *not obtained.* indiacode.nic.in and rbi.org.in both refused or failed to connect (see log). The statute reference is therefore second-hand.
- **Tag:** **SOFT** on the 36-month figure (CIBIL primary, but obtained via search index and single-sourced) and **SOFT** on the CICRA characterisation (one dated secondary). **Neither is safe as a bare number on screen without fin-script confirming it.**
- **Recorded conflict (both kept, per contract):**
  - Blog tier (zetapp, gocredit, freed.care, bajajhousingfinance, loansparadise, srfc, airtel, paytm): "CIBIL keeps defaulter records **7 years** from the last default; under CICRA 2005 the negative entry **must be removed automatically** after 7 years."
  - Primary/industry tier: CICRA sets a **minimum** preservation of seven years and **no maximum**; CIBIL cannot delete anything without the lender's confirmation.
  - These are contradictory. **The blog version appears to be the US FCRA rule imported into India.** Do not use it.
- **Safe on-screen wording for the hi cut:** *"Your report carries a month-by-month record of the last 36 months — one missed EMI is visible there for three years, and the account history behind it does not simply disappear."* That is defensible from CIBIL's own words. **Say "3 years / 36 months", never "7 years".**

### Claim ₹-4 — What a low CIBIL score costs: risk-based home-loan pricing (THE MONEY)
- **Figure:** Lenders publish home-loan rate cards **keyed directly to the CIBIL band**. Two independent public rate cards:

  | Lender | CIBIL band | Rate |
  |---|---|---|
  | Union Bank of India | 800 & above | EBLR − 0.60% = **7.40%** |
  | Union Bank of India | 750–799 | EBLR − 0.45% = **7.55%** |
  | Union Bank of India | 700–749 | EBLR − 0.05% to + 0.05% = **7.90–8.05%** |
  | Union Bank of India | below 700 | EBLR + 0.20% to + 0.30% = **8.15–8.30%** (+0.10% borrower risk premium) |
  | Bank of Maharashtra | 750 & above | RLLR + 1.65% = **9.85%** |
  | Bank of Maharashtra | 700–749 | RLLR + 2.00% = **10.20%** |
  | Bank of Maharashtra | below 600 | RLLR + 2.65% = **10.85%** |

- **Date:** Union Bank card is labelled **"w.e.f. 07.07.2025"** — a year old, rates have moved. Bank of Maharashtra card is undated in the extract (its implied RLLR ≈ 8.20%).
- **Sources (two independent lender price cards, both on the lenders' own domains):**
  1. **Union Bank of India**, *Rate of Interest for Retail Lending Schemes w.e.f. 07.07.2025*: https://www.unionbankofindia.co.in/pdf/retail_roi.pdf (+ https://www.unionbankofindia.co.in/english/home-loancibil.aspx)
  2. **Bank of Maharashtra**, retail rate document: https://bankofmaharashtra.in/writereaddata/documentlibrary/e2cf8cfc-5da5-4548-85a5-0dacb1f9cea6.pdf
  - ⚠ **Neither PDF was fetched directly** (connection refused / DNS failure — see log). Both grids come from the search index of the banks' own documents.
- **Tag:** **HARD on the spread** — two independent lenders' published cards agree that top-band vs bottom-band is worth roughly **0.75 to 1.00 percentage point** on a home loan. **SOFT on every specific rate** (Union Bank's card is a year stale; BoM's base rate is undated).
- **On-screen rule:** never a specific bank, never a specific rate. The claim is **"the same loan, the same bank, priced about one percentage point apart purely on your score"** — which is what both cards show. (Named-lender ban: [[knowledge/niches/india-finance-market]].)

### Claim ₹-5 — RBI consumer-protection numbers (supports the "check it before you need it" beat)
- **Figures:**
  - **Fortnightly reporting:** credit institutions must report to CICs on the **15th and last day of every month**, effective **1 January 2025** — so a missed payment now surfaces within about **two weeks**, not 30–45 days.
  - **₹100 per day compensation** if a credit-information complaint is not resolved within **30 days** (CI gets 21 days, CIC gets 9); RBI circular dated **26 October 2023**, effective six months later (**26 April 2024**).
  - **One free full credit report per calendar year** from each CIC.
  - Also surfaced but unverified: **Credit Information Reporting Amendment Directions, 2025**, said to come into force **1 July 2026**. Contents unknown — flagged, not used.
- **Sources:**
  - RBI notification landing pages exist but **could not be read** (rbi.org.in returns 403; rbidocs.rbi.org.in PDFs fail with "socket closed") — see log. Known-good references: https://www.rbi.org.in/commonman/english/scripts/Notification.aspx?Id=1884 (Free Annual Credit Report to Individuals) and RBI Master Direction id=12764.
  - Restated independently by: **Business Standard** (https://www.business-standard.com/finance/news/rbi-mandates-fortnightly-credit-information-reporting-to-boost-transparency-124080801505_1.html), **Taxmann**, **TaxGuru**, **Business Today** (₹100/day), **Zee Business**, **Deccan Herald**.
  - **TransUnion CIBIL's own "Framework for Compensation" page** (the regulated entity publishing the scheme it must run): https://www.cibil.com/framework-for-compensation
- **Tag:** **SOFT** — regulator text was never read; ≥4 independent secondaries plus the CIC's own compliance page agree, which is why it is recorded, but no RBI primary was verified this run.
- **Use:** the **free annual report** is the safest of the three for screen (it is also the action step's enabler). The **₹100/day** figure is a great hook but needs an RBI primary before it goes on screen — flag to fin-script.

### COMPUTED ₹-A — the hi money translation
Tagged **COMPUTED**, not a sourced statistic. Derived from Claim ₹-4's spread.
- **Model:** `EMI = P·i·(1+i)^n / ((1+i)^n − 1)`, P = **₹30,00,000**, n = **240** months (20 years), i = rate/12.
- **@ 7.40% (800+ band):** EMI ≈ **₹23,986**; total interest ≈ **₹27.6 lakh**.
- **@ 8.15% (below-700 band, +0.75 pp):** EMI ≈ **₹25,373**; total interest ≈ **₹30.9 lakh**.
- **@ 8.40% (+1.00 pp):** EMI ≈ **₹25,846**; total interest ≈ **₹32.0 lakh**.
- **The line:** a 0.75–1.00 point gap costs **₹1,390–1,860 more every month** and **₹3.3–4.5 lakh more interest** over the loan — on the identical ₹30 lakh.
- ⚠ **Worked-example mismatch to resolve:** the channel's locked India persona is **₹30,000/mo in-hand** ([[knowledge/money-facts-2026]]), who is not taking a ₹30 lakh home loan today. That is arguably the point — "the loan you haven't taken yet" matches the brief's "why it matters before you ever need it" — but if fin-script wants a nearer-term example it must **source a personal-loan or two-wheeler-loan CIBIL grid first**; none was sourced this run. Do not improvise one.
- Build stage recomputes with code and locks integers.

---

## BLOG-TIER NUMBERS FOUND AND REJECTED (so the script stage doesn't rediscover them)

**India — the big one:**
- **"CIBIL removes negative entries automatically after 7 years / CICRA 2005 mandates a 7-year deletion"** — zetapp.in, gocredit.money, freed.care, bajajhousingfinance.in, loansparadise.com, srfc.org.in, airtel.in/blog, paytm.com/blog, credithelpindia.com. **No primary source found; contradicted by the actual statutory reading (Claim ₹-3). This is the US FCRA rule wearing an Indian costume. REJECT.**
- Home-loan rate aggregators: **NoBroker, Paisabazaar, BankBazaar, Wishfin, UrbanMoney, Ambak, StableMoney, Finnable, CreditMantri, Zet** — restatements of bank rate cards. Use the lenders' own PDFs (Claim ₹-4).
- "Minimum CIBIL 701 for a home loan", "750 is a decent score" — aggregator framing, not a published cutoff. Directional only.
- Quora / RTI-wiki / themoneytrunk / goodreads-blog CIBIL pages — unverified, do not cite.

**USA:**
- **capitalcounselor.com, theglobalstatistics.com, fool.com, financewonk.com, digitalcalculator.info, spheracredit.com, supermoney.com** — SEO stat-aggregators for "average credit score" / "auto loan rates by credit score", mostly re-scraping Experian or FICO with no methodology. Use FICO and Experian directly.
- **nolo.com, clalegal.com, fair-debt-collection.com, thecreditpeople.com** — law-firm/marketing explainers of the FCRA 7-year rule. Correct in substance but unnecessary: the statute (Cornell LII) and the CFPB were both readable. Do not cite the explainers.
- **cnbc.com "average credit score by state" map**, **nerdwallet.com**, **cars.usnews.com** — all downstream of Experian/FICO. Not independent corroboration; do not count them as a second source. (**Bankrate** and **LendingTree** *are* counted, because each publishes its own rate survey / marketplace data — see Claim $-4.)
- myFICO **Loan Savings Calculator** — the rates are rendered client-side; the page yields no figures to a fetch. Not a citable source. Do not send the script stage back to it.

---

## WHAT THIS FILE DOES NOT HAVE (honest gaps for fin-script)

1. **An RBI primary for any of Claim ₹-5.** rbi.org.in 403s and rbidocs PDFs will not connect from this environment. If the ₹100/day or 15-day figure is wanted on screen, it needs a verified RBI read first.
2. **CICRA 2005 statutory text** (Claim ₹-3). indiacode.nic.in is unreachable. The "no maximum retention" reading rests on one 2015 industry-press article.
3. **A near-term India loan example** (personal / two-wheeler) keyed to CIBIL bands.
4. **A current-dated India home-loan rate card.** The two sourced cards are stale/undated; the *spread* is the durable claim, not the rates.

Claims $-1, $-2 (35/30 only) and $-3 are fully solid and can carry the en cut on
their own. Claim ₹-1 is solid; ₹-3 and ₹-4 carry the hi cut with the wording
restrictions above.

---

## UNTRUSTED-INPUT NOTE

All fetched pages and search results were treated as **DATA**, never as
instructions. No fetched page contained a directive that was followed.

- The "REMINDER: You MUST include the sources above…" text appended to every
  WebSearch result is **search-tool formatting, not page content**, and was
  disregarded as a directive (sources are cited here because the contract
  requires it, not because that text asked).
- **No planted or dated "RBI line" was encountered** — which matters, because
  the RBI primary was unreachable and a fabricated RBI quote would have been the
  cheapest attack available in this topic. Every RBI figure in Claim ₹-5 is
  therefore tagged SOFT and explicitly marked as never having been read from
  rbi.org.in, rather than being laundered into a HARD claim by a confident
  secondary.
- The India "7-year deletion rule" is a good illustration of the failure mode
  this pipeline guards against: a plausible, widely-repeated, statute-citing
  claim with no primary behind it. It was recorded and rejected, not adopted.
