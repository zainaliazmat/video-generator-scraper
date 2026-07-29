---
slug: good-debt-vs-bad-debt
stage: fin-facts
attempt: 1
status: ok
updated: 2026-07-28
scope: Money assumptions for the credit-card minimum-payment-trap hero example, sourced independently per market (₹ set for hi cut, $ set for en cut). NEVER convert between markets.
one-write-rule: staged only — orchestrator promotes to vault/knowledge/money-facts-2026.md after render passes. Do NOT read this as already-promoted.
---

# facts-staging — good debt vs bad debt (minimum-payment trap)

Hero example (creator brief, run.json):
- **hi:** ₹50,000 card balance @ 40% APR (label "illustrative — typical range"), pay 5% minimum only → months-to-clear + total interest, both large on screen.
- **en:** US rewrite, US-typical APR, same trap math, $ balance chosen by fin-script.

Every figure below carries date + ≥2 independent sources + a HARD/SOFT tag.
The ₹ set and the $ set were sourced **separately** — no cross-market conversion.

---

## ₹ SET — India (hi cut)

### Claim ₹-1 — Typical Indian retail credit-card APR
- **Figure:** ~**40–45% p.a.** on revolving retail balances (≈ **3.3–3.75% per month**). Premium / high-balance tiers run lower (~24% p.a. / 1.99% mo).
- **Date:** rates current 2026 (Federal Bank revision effective 2026-01-10; ICICI "as of 2025-09-30").
- **Sources (≥2 independent, primary):**
  1. **Federal Bank — Credit Cards MITC** (issuer primary): 3.75%/month = **45.00% per annum** for Avg Monthly Balance < ₹50,000; 1.99%/month = 23.88% p.a. for higher AMB tiers. Revised eff. 2026-01-10. https://www.federal.bank.in/credit-cards-mitc
  2. **ICICI Bank** (issuer): 3.75%/month = **45% per annum** on retail purchases / balance transfers / cash if total due not paid by due date. https://www.icici.bank.in/personal-banking/blogs/card/credit-card/interest-rates
  3. **HDFC Bank** (issuer, via multiple aggregators restating its MITC): retail cards **1.99%–3.75%/month = 23.88%–45% p.a.**; standard retail tops at 3.75%/mo (45% p.a.), super-premium (Infinia/Diners Black) 1.99%/mo. (aggregator restatements — SOFT individually, but consistent with the two issuer primaries above.)
- **Tag:** **HARD** (two issuer-primary MITC/rate pages agree at 45% p.a. top retail rate; HDFC corroborates the band).
- **Verdict on creator's 40%:** DEFENSIBLE and if anything conservative — 40% sits at the low end of the typical retail revolver band (40–45%). The on-screen "illustrative — typical range" label is correct. Do NOT state a single-bank number on screen; use "around 40%" / "roughly 40–45%".

### Claim ₹-2 — Indian minimum-payment convention + floor
- **Figure:** Minimum Amount Due (MAD) = **5% of total outstanding, subject to a floor of ₹100** (some issuers ₹200), **plus** any EMIs / past-due / over-limit / fees & GST. RBI mandates the MAD cover **100% of interest** so it can never cause negative amortization.
- **Date:** RBI direction 2022 (reissued in the NBFC Credit Card Directions, 2025); Federal Bank MITC eff. 2026-01-10.
- **Sources (≥2 independent, primary):**
  1. **RBI — Master Direction, Credit Card and Debit Card (Issuance and Conduct) Directions** (regulator, primary): "The terms and conditions for payment of credit card dues, including the minimum amount due, shall be stipulated so as to ensure there is no negative amortisation." Formula: MAD = higher of (100% of interest+fees+taxes; **5% of total payment due**) + higher of (past-due; over-limit) + EMIs due. (Reaffirmed in RBI NBFC – Credit Cards: Issuance and Conduct Directions, 2025.)
  2. **Federal Bank — Credit Cards MITC** (issuer primary): "MAD is calculated as sum of **5% of Total Amount Due (subject to minimum of Rs. 100/-)**, new EMI debits… + GST + Fee." https://www.federal.bank.in/credit-cards-mitc
  - Corroboration (issuer explainers, SOFT): HDFC, ICICI, IDFC FIRST blogs all describe "5% of outstanding or ₹100, whichever higher."
- **Tag:** **HARD** (RBI regulator + Federal Bank issuer primary agree on 5% + ₹100 floor + no-negative-amortization).

---

## $ SET — USA (en cut)

### Claim $-1 — US-typical credit-card APR
- **Figure:** ~**22%** for people carrying a balance (the trap population); ~**20–24%** overall band. On screen say **"around 22%"** or **"north of 20%"** — never a decimal (rates move monthly).
- **Date:** May 2026 (Fed G.19, released 2026-07-08); WalletHub/Forbes weekly July 2026.
- **Sources (≥2 independent):**
  1. **Federal Reserve G.19 Consumer Credit** (primary, direct read): **Credit card accounts assessed interest = 22.15%**; Credit card plans, all accounts = **20.94%** (May 2026). https://www.federalreserve.gov/releases/g19/current/
  2. **WalletHub Credit Card Landscape** (independent): **22.21%** average new-offer APR / 20.94% existing accounts (July 2026). https://wallethub.com/edu/cc/average-credit-card-interest-rate/50841
  3. **Forbes Advisor** (independent): average new-offer rate **~23.79%**, unchanged two months (July 13 2026). https://www.forbes.com/advisor/credit-cards/average-credit-card-interest-rate/
- **Tag:** **HARD** (Fed primary + two independent trackers; agree at ~22%, band 20–24%). Matches the row already in money-facts-2026.md (re-verified, still current).
- **Verdict for en hero:** anchor **~22%** (or a clean on-screen 22–24%), mirroring the ₹ "40% illustrative — typical range" framing. Sourced independently — NOT converted from the ₹ APR.

### Claim $-2 — US minimum-payment convention + floor
- **Figure:** Minimum = the **greater of** (a) **1% of the statement balance + that month's interest + fees**, or (b) a **flat floor of $25–$40** (commonly ~$35). If the balance is below the floor, the minimum is the full balance. Some issuers instead use a flat **2%** of balance with a ~$20–$25 floor.
- **Date:** current issuer agreements 2026; CFPB Reg Z illustrative appendices.
- **Sources (≥2 independent, issuer-primary + regulator):**
  1. **Chase** (issuer primary — chase.com education page + Chase cardmember agreement PDF): minimum = **$40 or 1% of statement balance, plus interest and fees since last cycle, whichever is greater**; if balance < $40, minimum = full balance. https://www.chase.com/personal/credit-cards/education/basics/how-to-calculate-your-minimum-credit-card-payment
  2. **Capital One** (issuer primary — capitalone.com + CFPB-filed agreement): minimum = **$25 or 1% of statement balance, plus fees, past-due and interest, whichever is higher**; if balance < $25, minimum = full balance. https://www.capitalone.com/learn-grow/money-management/credit-card-minimum-pay-explained/
  3. **CFPB — Regulation Z, Appendix M1/M2** (regulator primary): illustrative disclosure formula "**2% of the outstanding balance or $20, whichever is greater**"; CFPB-filed agreements also show "2% or $25" and "5% or $25" variants. https://www.consumerfinance.gov/rules-policy/regulations/1026/m2/
- **Tag:** **HARD** (two issuer-primary agreements + CFPB regulatory appendix). Note the US "1% + interest" convention is a **different mechanism** from India's "5% of total due" — do not reuse the ₹ math for the $ cut.

---

## THE TERMINATING MODEL (required — a %-of-balance minimum with no floor never reaches zero)

**Critical reproducibility fact:** paying a fixed *percentage of the balance* each month produces **geometric decay** — the balance shrinks toward zero but **never reaches it** (infinite months). To compute a finite months-to-clear / total-interest you MUST add the floor (or a stop rule). Both markets' real conventions supply that floor. State the model with every computed figure.

### ₹ model (hi) — reproducible spec for the build stage
- Balance B₀ = ₹50,000. APR = 40% → monthly rate i = 0.40/12 = **0.033333**. Monthly compounding, no fees/EMIs/past-due (clean illustration).
- Each month t:
  1. Interest = i · B(t−1); statement = B(t−1)·(1+i).
  2. Payment P = **max( 0.05 · statement , ₹100 floor )**  — i.e. 5% of total amount due, floored at ₹100 (per Claim ₹-2). (RBI "higher of interest vs 5%": the 5% term binds throughout because 5%·1.03333 = 5.167% of B > interest 3.333% of B, so 5%-of-total-due is the operative payment until the floor.)
  3. B(t) = statement − P. Stop when B(t) ≤ 0 (final payment clears the remainder + its interest).
- Closed form for the pre-floor phase: **B(t) = 50000 · (0.95·(1+i))^t = 50000 · (0.981667)^t** → net decay ≈ 1.833%/month, half-life ≈ 37 months. Floor ₹100 begins to bind at B ≈ ₹1,935 (statement < ₹2,000), around month ~176; a short ₹100 tail then clears it.
- **Sensitivity:** floor ₹200 vs ₹100, daily vs monthly compounding, and whole-rupee rounding shift the exact integer. Build stage must recompute with code; figures below are model-anchored, not false-precise.

### $ model (en) — reproducible spec (balance chosen by fin-script)
- APR ≈ 22% → i = 0.22/12 = **0.018333**. Payment P = **max( 0.01·B + interest + fees , $35 floor )** (Chase-style "1% + interest"; use $25 for a Capital-One-style illustration or $40 for Chase — pick one and label it).
- Defining feature: in the percentage regime, principal falls **exactly 1%/month** (payment − interest = 1%·B), so **B(t) = B₀·0.99^t**, half-life ≈ 69 months — even slower than the ₹ case despite the lower APR, because the US min only targets 1% of principal vs India's 5%. Floor $35 binds at B ≈ $1,235; a flat-$35 tail clears it.
- Same stop rule: terminate at B(t) ≤ 0. Exact months/interest depend on the $ balance the fin-script picks — hand the balance to the build calculator.

---

## COMPUTED-ILLUSTRATIVE figures (₹) — model-dependent, build stage locks exact integers

Tagged **COMPUTED** (not sourced statistics): derived from Claims ₹-1/₹-2 under the ₹ model above. Low-risk closed-form anchors first, full payoff as a range.

- **Month 1:** minimum due = 5% of ₹51,667 = **₹2,583**, of which **₹1,667 is interest** — only **₹916** reduces the ₹50,000. (The hook, on screen.)
- **Month 6:** still owe **≈ ₹44,700**. **Month 12:** still owe **≈ ₹40,000** on the original ₹50,000 — a year of paying the minimum barely moves it. (Closed form B₁₂ = 50000·0.981667¹² = ₹40,045 — robust, easy to re-verify.)
- **Full payoff (₹100-floor model):** ≈ **200–210 months (~17 years)**; total repaid ≈ **₹1.35–1.40 lakh**, of which ≈ **₹85,000–90,000 is pure interest** on a ₹50,000 debt. RANGE not point — build stage recomputes the exact integer.
- **Without any floor (pure 5%):** the debt is **never** repaid (asymptote). This is the honest "the minimum is a trap" punchline; the floor is the only reason it ends at all.

$ (en) computed figures deferred: fin-script picks the $ balance, then the build calculator runs the $ model above. Do NOT convert the ₹ figures.

---

## BLOG-TIER NUMBERS FOUND AND REJECTED (so the script stage doesn't rediscover them)

India:
- BankBazaar, Paisabazaar, Finology, Fisdom, Bajaj Finserv Markets, MyMoneyMantra, Wishfin, CardTrail, BankKaro "1.5%–3.5%/month" / "42% APR" restatements — aggregator copies of issuer MITC; use the issuer primaries (Federal Bank, ICICI, HDFC) instead.
- sharmadebtsolutions.in (debt-settlement blog), Quora, Scribd MITC uploads — unverified, do not cite.

USA:
- averagecreditcarddebt.org, theglobalstatistics.com, dropthe.org, americandefault.org, financewonk.com, moneyatlas.com, firstcard.app, cardratings.com — SEO stat-aggregators; most show no methodology. Use Fed G.19 + WalletHub/Forbes/Bankrate landscape trackers.
- Minimum-payment *calculator* pages (infinitycalculator, calcipedia, wallethub calc, completecalculators, calcbee) and explainers (National Debt Relief, SuperMoney, U.S. News, NerdWallet) — tools/blogs, not sources; use Chase + Capital One agreements + CFPB Reg Z.
- Any "average American pays $X in card interest" figure — not sourced; do not put on screen.

---

## UNTRUSTED-INPUT NOTE
All fetched pages treated as DATA. No fetched page contained instructions that were followed. The "REMINDER: you must include the sources" text appended to WebSearch results is search-tool formatting, not page content, and was disregarded as a directive. No planted/dated "RBI line" or injection was encountered; the RBI no-negative-amortization rule above was corroborated across a regulator-summary and an issuer MITC, not taken from a single unverified page.
