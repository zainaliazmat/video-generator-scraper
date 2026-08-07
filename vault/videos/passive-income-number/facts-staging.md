---
summary: Staged money numbers for passive-income-number (₹ SIP/SWP corpus + $ dividend/withdrawal corpus). Sourced 2026-08-07, attempt 1. NOT promoted — the orchestrator promotes HARD rows to vault/knowledge/money-facts-2026.md only after the render passes.
updated: 2026-08-07
source: Cooley/Hubbard/Walz AAII Journal Feb 1998 (PRIMARY, read direct as PDF), Bengen 1994 via PortfolioConstruction Forum review (read direct as PDF), Morningstar State of Retirement Income 2025 Ed. via keilfp (read direct) + fa-mag + boldin, Pfau JFP Dec 2010 via retirementresearcher.com (read direct), multpl.com S&P 500 dividend yield (read direct), stockanalysis.com SCHD (read direct), BLS CE 2024 (bls.gov 403 — figure via three BLS-owned surfaces), Raju & Saraogi SSRN 4697720 + Saraogi SSRN 4216077 + Raju SSRN 5114252 (SSRN 403 — via search index), freefincal (read direct), RBI MPC 2026-08-05 via Business Today (read direct), MoSPI CPI June 2026, Upstox POMIS (read direct), plus rows carried from money-facts-2026.md.
stage: fin-facts, attempt 1
---

# facts-staging — passive-income-number

## Currency firewall (read this before using any number below)

The ₹ set and the $ set were sourced **independently and are not convertible.**
They differ on *three* axes at once, not one:

1. **Different withdrawal rates.** India's published research lands at **3.0–3.5%**;
   the US anchors at **3.9–4.7%**. Using one market's rate on the other market's
   corpus is a fabricated number.
2. **Different inflation.** RBI projects **5.0% for FY27**; the US safe-rate
   literature is built on US CPI history. This is *why* the rates differ — it is
   the mechanism, not a coincidence.
3. **Different living costs.** ₹25,000/mo and $5,000/mo are both "an ordinary
   monthly income" in their own market and neither is the other.

₹1 crore is **not** $1.5 million and no line, frame or chart may imply it.

## Tags

**HARD** = primary/regulator/peer-reviewed/published price card, or two
independent top-tier sources agreeing · **SOFT** = single source, survey,
opinion, or primary unreachable · **COMPUTED** = arithmetic done here from
tagged inputs; label "illustrative" on screen, never speak as a statistic ·
**CONVENTION** = a channel choice, not a fact.

**On the URLs.** "read direct" = this stage retrieved the page. "via search
index" = the URL is recorded for checkability only and the row's tag reflects
that. No URL was constructed or guessed.

---

# PART A — The withdrawal rate itself (both markets need this staged as a fact)

`run.json.constraints.withdrawal_rate_on_screen` requires every corpus figure to
carry its rate **in the same frame**. So the rate is a sourced fact in its own
right, listed first, before any corpus number exists.

## A.1 The 4% rule — origin (HARD, primary read direct)

| Claim | Detail | Source | Tag |
|---|---|---|---|
| Who invented it | **William P. Bengen**, "Determining Withdrawal Rates Using Historical Data", ***Journal of Financial Planning*, October 1994**, vol. 7 no. 4, pp. 171–180 | https://obj.portfolioconstructionforum.edu.au/articles_perspectives/Determining-withdrawal-rates-using-historical-data.pdf — **read direct** (PortfolioConstruction Forum review of the paper, Angela Ashton, 2014-02-06) + https://en.wikipedia.org/wiki/William_Bengen (read direct) + https://www.financialplanningassociation.org/learning/publications/journal/NOV23-revisiting-william-bengens-safemax-portfolio-withdrawal-rate-OPEN (via search index) | **HARD** on author/journal/date · the 1994 paper itself was NOT read (FPA PDF 403'd) |
| What Bengen actually tested | **50% equity / 50% bond**, retirement start years **1926–1966**, withdrawals inflation-linked after year one | PortfolioConstruction Forum review, read direct | HARD |
| What he found | 4% initial → portfolio lasted **≥50 years in most cases**; **worst case ≈30 years** (a 1976 retiree). **5% → as short as 20 years.** **3.5% → always ≥50 years** | same | HARD |
| Who made it famous | **Cooley, Hubbard & Walz** (professors of finance, Trinity University, San Antonio) — "Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable", ***AAII Journal*, February 1998, pp. 16–21** — the "Trinity Study" | https://www.aaii.com/journal/199802/feature.pdf — **READ DIRECT, full paper, all 4 tables** | **HARD (primary)** |
| Trinity's data | **1926–1995**, Ibbotson SBBI 1996 Yearbook. Stocks = S&P 500 (10.5% compound), bonds = long-term high-grade corporates (5.7% compound). Payout periods 15/20/25/30 yrs; 5 allocations | Trinity paper, read direct | HARD |
| Trinity's headline result (Table 3 — **inflation-adjusted** withdrawals, 30-yr payout) | 4% survived **95%** of periods at 100% stocks · **98%** at 75/25 · **95%** at 50/50 · **71%** at 25/75 · **20%** at 100% bonds | Trinity Table 3, read direct | HARD |

**Say it this way:** "the four percent rule" is a **1994 paper and a 1998 paper**,
not a law. Both are named, dated and quotable. That framing satisfies
`no_return_promise` by construction.

## A.2 The 4% rule — documented criticisms (HARD; the paper criticises itself)

| # | Criticism | Evidence | Source | Tag |
|---|---|---|---|---|
| 1 | **It ignores taxes and costs — the authors say so themselves** | Trinity, verbatim in its methodology bullets: *"The study did not adjust for taxes or transaction costs."* | https://www.aaii.com/journal/199802/feature.pdf — **read direct** | **HARD (primary, self-stated)** |
| 2 | **It was built for a 30-year retirement, not a 50-year one** | Trinity, Conclusion, verbatim: *"Early retirees who anticipate long payout periods should plan on lower withdrawal rates."* Bengen's own worst case was a 30-year horizon | same, read direct + PortfolioConstruction review | **HARD (primary)** |
| 3 | **Today's forward-looking number is lower than 4%** | **Morningstar: 3.9%** for a 2026 retiree — 30-year horizon, **90% success probability**, **30–50% equity**, fixed inflation-adjusted spending. Up from **3.7%** for 2025 | https://keilfp.com/blogpodcast/morningstar-safe-withdrawal-rate/ — **read direct** (pub. 2025-12-03) + https://www.fa-mag.com/news/morningstar-safe-retirement-withdrawal-rate-for-2026-is-3-9-85940.html + https://www.boldin.com/retirement/safe-withdrawal-rate-morningstar/ + https://www.morningstar.com/business/insights/research/the-state-of-retirement-income (all via search index; morningstar.com 403'd to direct fetch) | **HARD** (three independent agree on 3.9%) |
| 4 | **It is a US-history artefact — it fails almost everywhere else** | Pfau, *"An International Perspective on Safe Withdrawal Rates: The Demise of the 4 Percent Rule?"*, **Journal of Financial Planning, December 2010**. At a 50/50 stocks-bills allocation with zero tolerated failure, **the 4% rule did not survive in ANY country**. SAFEMAX below 3% in **10 of 19** countries. **Japan 0.26%**, Italy 0.8%, France 0.82%, Germany 1.01% | https://retirementresearcher.com/the-shocking-international-experience-of-the-4-rule/ — **read direct (Pfau's own site)** + https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1699526 + https://www.financialplanningassociation.org/article/journal/DEC10-international-perspective-safe-withdrawal-rates-demise-4-percent-rule (both via search index; SSRN and FPA 403'd) | **HARD on the shape** · see conflict below |
| 5 | **Even its author has moved it — twice** | Bengen now says **4.7%** ("Universal SAFEMAX"), in *A Richer Retirement* (Wiley, **August 2025**). New model adds mid/small/micro-cap, international equity and T-bills; tested allocation ≈55% diversified stocks / 40% intermediate Treasuries / 5% T-bills; ~400 historical start dates. Worst case still **October 1968**. He suggests ~**5–5.5%** under normal conditions | https://www.advisorperspectives.com/articles/2025/08/29/bill-bengen-boosts-the-4-rule-to-4-7 + https://www.forbes.com/sites/jlange/2025/10/23/bill-bengens-new-safe-withdrawal-rate-a-175-raise-for-retirees/ + https://www.cnbc.com/2025/09/03/4percent-rule-inflation-retirement.html + https://www.fool.com/investing/2026/08/05/the-father-of-the-4-rule-says-retirees-can-withdraw-more/ (all via search index) | **HARD** (four independent outlets, consistent) |

⚠ **CONFLICT — record both, never pick one.** Pfau's country count is reported as
**17 countries / 109 years** by the SSRN + FPA abstracts and as **19 countries /
1900–2010** on Pfau's own retirementresearcher.com. Both are recorded. **On
screen say "most developed markets", never a country count**, and never a
decimal for a country's SAFEMAX except Japan's 0.26% (which both surfaces agree
on and which is the only one worth showing).

⚠ **NAMING TRAP that broke two of my own searches.** Morningstar's report titled
***The State of Retirement Income: 2025 Edition*** (published **2025-12-03**)
sets the rate for **2026** retirees. Report year ≠ retiree year. Search results
mix them constantly. **On screen: "3.9%, Morningstar, for a 2026 retiree."**
Never "Morningstar 2025 says 3.9%".

## A.3 India's own withdrawal-rate research (the ₹ cut must NOT use 4%)

| Claim | Figure | Source | Tag |
|---|---|---|---|
| India SWR, peer-reviewed | **3.0–3.5%**; best SWR **3.0% at a 40% equity allocation**; failure risk rises sharply **above 3.75%**. Data **2000–2023**, India asset returns + India inflation | Raju & Saraogi, *"Balancing Acts: Safe Withdrawal Rates in the Indian Context"*, **2024-01-17** — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4697720 (**SSRN 403'd, via search index**). **First Prize, 1st International Research Conference on Pension (IRCP 2025), New Delhi, 3–4 Apr 2025**; presented at the Institute of Actuaries of India 12th TechTalk (https://www.actuariesindia.org/sites/default/files/2024-11/Presentation%20for%2012th%20Techtalk%20on%20Employee%20Benefits.pdf — **TLS cert failure, not fetched**) | **HARD on the 3.0–3.5% band** · SOFT on any single decimal |
| India SWR, second paper | **3% for an average investor; no more than 2.6% for a risk-conservative investor.** Explicitly finds *"limited applicability of the 4 percent SWR in India"* | Ravi Saraogi, *"Computing the Safe Withdrawal Rate for a Retirement Portfolio in India"* — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4216077 (**SSRN 403'd, via search index**) | **SOFT** — same author group as above, so **not independent** |
| India SWR, third paper | Moderate equity (**20–50%**) gives the highest SWRs; 4% "too generic" for India. Data **1992–2024** | Rajan Raju, *"Safe Withdrawal Rates in India: Balancing Portfolio Sustainability and Flexibility (1992–2024)"* — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5114252 (via search index) | **SOFT** — same author group |
| **Independent India practitioner corroboration** | Initial withdrawal rate **under 3.5% → corpus likely adequate**; **3.5–4.5% → grey area**; **above 4.5% → corpus likely inadequate** | Dr. M. Pattabiraman, freefincal — https://freefincal.com/using-safe-withdrawal-rates-to-judge-retirement-corpus-health/ — **read direct** (pub. 2026-02-08). Stated as decade-long backtesting opinion; **no backtest data disclosed in the article** | **SOFT**, but **independent of Raju/Saraogi** — this is what makes the band usable |
| Why India's rate is lower | **RBI projects CPI inflation at 5.0% for FY27** (Q1 5.3 / Q2 4.7 / Q3 5.9 / Q4 5.5). MPC 2026-08-05, repo held at **5.25%**, neutral stance | https://www.businesstoday.in/latest/economy/story/rbi-mpc-2026-central-bank-trims-fy27-inflation-outlook-to-5-signals-price-stability-focus-547265-2026-08-05 — **read direct** + https://www.forbesindia.com/article/news/rbi-mpc-live-updates-august-2026-repo-rate-sanjay-malhotra-policy-announcement-liveblog/2996705/1 (via search index) | **HARD** |
| Actual latest India CPI | **4.38% y/y, June 2026** (provisional; base 2024=100). Rural 4.74% / urban 3.92%; food (CFPI) **5.32%** | MoSPI/NSO via https://www.pib.gov.in/PressReleasePage.aspx?PRID=2284125 (**PIB 403'd**) and https://www.mospi.gov.in/uploads/latestReleases/latest_release_1783937698596_1013f1a1-3400-41aa-b4f4-5bbff10db7b7_Press_Release_of_CPI_for_June_2026.pdf (**not fetched**); figures via search index of both government surfaces + https://tradingeconomics.com/india/inflation-cpi | **SOFT** (no government surface read direct this run) |

**The load-bearing India insight of this whole video:** the 4% rule is an
imported American number, and India's own published research says **3%**. Using
4% makes an Indian's target corpus look **25% smaller than it is**
(₹75 lakh vs ₹1 crore for the same ₹25,000/month). That is the differentiator,
and both halves are sourced.

---

# PART B — India (₹). SIP / SWP / passive income. The word "dividend" is BANNED.

## B.1 Carried forward from [[knowledge/money-facts-2026]] — already sourced, still current

| Claim | Figure | Source | Tag |
|---|---|---|---|
| Regular wage/salaried avg monthly earnings | **₹24,217 men / ₹18,353 women** | PLFS Annual Report 2025 (Jan–Dec 2025), PIB | HARD |
| SIP minimum | **₹500/mo; ₹250 "Chhoti SIP"** | AMFI | HARD |
| Net household financial savings | 7.0% of GNDI, FY25 | RBI Annual Report, May 2026 | HARD |
| **PPF** | **7.1% p.a.**, Q2 FY2026-27 (1 Jul – 30 Sep 2026) | DEA notification 2026-06-30 via Business Today + Business Standard | HARD |
| Post Office **3-yr Time Deposit** | 7.1% p.a., same quarter | same | HARD |
| Small-savings rates unchanged — **ninth** consecutive quarter (say nine, not ten) | — | same | HARD |
| Nifty 50 **TRI since inception** (base 1995-11-03) | **12.41% p.a.** (factsheet 2026-06-30); price-only 10.90%; 20-yr TRI 12.44% | niftyindices.com + archives.nseindia.com + nsearchives.nseindia.com — **all three 403'd again this run**, same as 2026-07-31 | **SOFT — shape only, never a decimal** |

⚠ **The TRI vocabulary trap (hi cut).** "Total Return Index" is *defined* as
price return **plus dividend return, reinvested**. Explaining TRI in the hi cut
would force the banned word. **Fix: in the hi cut never explain TRI at all** —
say "index ka long-run return, roughly twelve percent" and show `~12%/yr`.
The word and the concept both stay in the en cut only.

## B.2 New this run — the India passive-income products that actually publish a monthly figure

| Claim | Figure | Date | Sources | Tag |
|---|---|---|---|---|
| **POMIS** (Post Office Monthly Income Scheme) rate | **7.4% p.a., paid monthly** | Q1 FY27 (Apr–Jun 2026) confirmed; Q2 FY27 unchanged per the DEA notification | https://upstox.com/news/personal-finance/investing/post-office-monthly-income-scheme-pomis-interest-rate-april-june-2026-calculation/article-191478/ — **read direct** (2026-03-31) + the Business Today Q2 FY27 rate table already banked in money-facts-2026 + https://cleartax.in/s/post-office-monthly-income-scheme-pomis (via search index) | **HARD** on the rate (two independent + the "unchanged" notification) |
| POMIS **deposit ceiling** | **₹9 lakh single · ₹15 lakh joint**, 5-year term, sovereign-backed | 2026 | Upstox (read direct) + cleartax + bankbazaar + policybazaar — **every source agrees**; indiapost.gov.in 404'd | **HARD** (unanimous across sources; issuer page not reached) |
| **SCSS** rate + ceiling | **8.2% p.a., paid quarterly**, ceiling **₹30 lakh**, 5-yr term, **age 60+ only** | Jul–Sep 2026 quarter | Business Today Q2 FY27 table (banked in money-facts-2026, SOFT there) + https://cleartax.in/c/senior-citizen-savings-scheme-scss + https://www.policybazaar.com/life-insurance/investment-plans/articles/post-office-senior-citizen-saving-scheme/ (via search index) | **SOFT** — no primary read; **age-gated, so use only if the script needs a 60+ beat** |
| **SWP** = what it is | A facility to withdraw a **fixed amount at a fixed interval by redeeming units**; the reverse of a SIP. Withdrawals come out of **capital + appreciation**, and are subject to capital-gains tax | 2026 | amfiindia.com **connection refused** this run. Definition is unanimous across https://mf.nipponindiaim.com/investoreducation/systematic-withdrawal-plan · https://www.tatamutualfund.com/blogs/systematic-withdrawal-plan-how-start-swp-mutual-funds · https://mutualfund.adityabirlacapital.com/blog/systematic-withdrawal-plan-in-mutual-fund · https://www.franklintempletonindia.com/investor/swp-calculator — four AMC (issuer) pages (via search index) | **HARD (terminology)** — four fund houses, identical definition. **No AMFI primary read this run.** |
| **LTCG on equity MF / SWP redemptions** | **12.5%** above a **₹1.25 lakh** per-financial-year exemption, holding period **>12 months**, **no indexation**, no §87A rebate. Union Budget 2026 made **no change** for FY2026-27 | FY2026-27 | cleartax.in/s/long-term-capital-gains-on-shares (**403'd**) · https://www.angelone.in/knowledge-center/income-tax/section-112a · https://www.bajajamc.com/knowledge-centre/common-things-to-know-about-ltcg-on-mutual-funds · https://tax2win.in/guide/section-112a-income-tax-ltcg-exemption — all via search index; **incometaxindia.gov.in not reached** | **SOFT** — consistent across four tax-content sites but **no statute or ITD page read**. Use as "roughly twelve and a half percent above ~1.25 lakh a year", never as a precise tax claim |
| Mutual fund industry AUM | **₹82.22 lakh crore** as on 2026-06-30; SIP monthly inflow record **₹32,087 crore** (Mar 2026) | Jun 2026 | AMFI via https://www.outlookmoney.com/invest/amfi-data-june-2026-equity-mutual-fund-inflows-aum-etf-sip (via search index); amfiindia.com **connection refused** | **SOFT** — context colour only, not a claim the video needs |

**The POMIS beat is the strongest sourced reality-check the ₹ cut has, and it
needs no forbidden vocabulary:** India's *government's own* monthly-income
scheme pays 7.4% and **caps you at ₹9 lakh**. Maximum monthly income from one
account: **₹5,550**. Even a joint account tops out at **₹9,250/month**. That is
the honest ceiling on "guaranteed monthly income" in India — and it is exactly
why the SIP→SWP route exists.

## B.3 COMPUTED — the ₹ hero math (illustrative; compute in build code, label it)

**Every figure below is division, not a forecast.** Formula stated on screen:
`corpus = annual withdrawal ÷ withdrawal rate`.

### Corpus needed, by withdrawal rate

| Monthly income wanted | at **3.0%** (India research) | at **3.5%** (India research, upper) | at **4.0%** (the imported US rule) |
|---|---|---|---|
| **₹25,000/mo** (₹3,00,000/yr) | **₹1,00,00,000 = ₹1 crore** | ₹85,71,429 ≈ **₹85.7 lakh** | ₹75,00,000 = ₹75 lakh |
| ₹50,000/mo (₹6,00,000/yr) | **₹2,00,00,000 = ₹2 crore** | ₹1,71,42,857 ≈ ₹1.71 crore | ₹1,50,00,000 = ₹1.5 crore |
| ₹24,217/mo (the PLFS average) | ₹96,86,800 ≈ **₹96.9 lakh** | ₹83,03,000 ≈ ₹83 lakh | ₹72,65,100 ≈ ₹72.7 lakh |

**★ THE ₹ HERO NUMBER: ₹1 crore, at a 3% withdrawal rate, is ₹25,000 a month.**
It is chosen because ₹25,000/mo sits right on the PLFS regular-salaried average
of ₹24,217 — so the number means "your current salary, without the job", and the
corpus lands on a round crore by arithmetic rather than by rounding. The
withdrawal rate **3%** must be in the same frame (`withdrawal_rate_on_screen`).

**The rule-import cost:** believe the American 4% and you aim at **₹75 lakh**.
India's own research says **₹1 crore**. The imported rule under-states an Indian
target by **25%** — the single best beat in the ₹ cut.

### Getting there — SIP required per month (monthly compounding, end-of-period)

| Horizon | at **7.1%** (PPF/3-yr TD — HARD) | at **~12%** (Nifty TRI shape — SOFT) |
|---|---|---|
| 15 years | ₹32,000/mo *(approx)* | **≈ ₹20,000/mo** |
| **20 years** | **≈ ₹19,000/mo** | **≈ ₹10,000/mo** |
| 25 years | ≈ ₹12,150/mo | ≈ ₹5,300/mo |

- ⚠ Every cell is model-dependent (compounding frequency, end- vs
  beginning-of-period, and a **rate assumption that is not a promise**). On
  screen only, labelled illustrative, **with the rate visible in the frame**.
- The honest framing: at ~12% the ₹1 crore costs **₹10,000/month for 20 years**;
  at the HARD 7.1% it costs **₹19,000/month** — **nearly double**. Show both
  columns. Showing only the 12% column is the promise this run must not make.
- **₹5,300/month for 25 years** is the "start young" beat, and it is *ten times*
  AMFI's ₹500 SIP minimum — a clean bridge from the audience's actual starting
  point.

---

# PART C — USA ($). Dividends + withdrawal rate. This is the format-twin phrase.

## C.1 Carried forward from [[knowledge/money-facts-2026]]

| Claim | Figure | Source | Tag |
|---|---|---|---|
| Real median household income | $83,730 (2024) | US Census P60-286 | HARD |
| Personal saving rate | 2.7% (June 2026) | BEA, rel. 2026-07-30 | HARD |
| Median usual weekly earnings, full-time | $1,251/wk (Q2 2026) | BLS + FRED | HARD |
| S&P 500 long-run return | **≈10% nominal / ≈7% real** — **shape only, never a decimal** | cited decimals conflict across sources | HARD on shape |
| Fed funds target range | 3.50–3.75%, last changed 2025-12-11 | federalreserve.gov | HARD |

## C.2 New this run — what a US portfolio actually pays

| Claim | Figure | Date | Sources | Tag |
|---|---|---|---|---|
| **S&P 500 dividend yield** ← the whole en cut hangs on this | **≈1.0–1.1%.** multpl: **1.04%**; GuruFocus: **1.082%**. multpl's own series records **1.08% (July 2026) as the all-time minimum** | 2026-08-05 / Jul 2026 | https://www.multpl.com/s-p-500-dividend-yield — **read direct** + https://www.gurufocus.com/economic_indicators/150/sp-500-dividend-yield (via search index) | **HARD on "about one percent"** · SOFT on the decimal |
| S&P 500 dividend yield, **long-run mean/median** | **mean 4.21% · median 4.19%** (series from 1871); max 13.84% (Jun 1932) | 2026-08-05 | multpl.com — read direct | **HARD** |
| **SCHD** (Schwab US Dividend Equity ETF) yield | **3.11%** TTM, $1.05/share annual, quarterly. Other reads: **3.3%** (Motley Fool, late Jul 2026), **3.41%** 30-day SEC yield (Apr 2026) | 2026-08-06 | https://stockanalysis.com/etf/schd/dividend/ — **read direct** + https://www.fool.com/investing/2026/07/27/schd-yields-33-and-could-finish-its-15th-year-of-c/ (via search index). **schwabassetmanagement.com 403'd — issuer price card NOT read** | **SOFT on the decimal** (three reads, three numbers) · **HARD on "about three percent"** |
| **VYM** (Vanguard High Dividend Yield ETF) | expense ratio 0.04%, net assets $81.6bn, tracks FTSE High Dividend Yield Index. **Yield not obtained** — investor.vanguard.com returned no fund data, advisors.vanguard.com not fetched | 2026 | https://investor.vanguard.com/investment-products/etfs/profile/vym (fetched, no data) | **NOT USABLE — do not put a VYM yield on screen** |
| **US household spending** ← the $ denominator | **$78,535** average annual expenditures per consumer unit, **2024** (= **$6,545/month**). Housing $26,266 (33.4%) · transport $13,318 (17.0%) · food $10,169. Range $35,046 (lowest quintile) → $150,342 (highest). Avg income before taxes $104,207 | rel. **2025-12-19**, USDL-25-1586 | BLS Consumer Expenditures—2024: https://www.bls.gov/news.release/cesan.nr0.htm · https://www.bls.gov/opub/ted/2026/housing-and-transportation-accounted-for-50-percent-of-household-spending-in-2024.htm · https://x.com/BLS_gov/status/2002031438787760616 · https://fred.stlouisfed.org/series/CXUTOTALEXPLB0101M — **all four 403'd or not fetched; figure is consistent across three BLS-owned surfaces via search index** | **HARD** (BLS's own figure on three BLS surfaces; not read direct — same posture as the BLS weekly-earnings row already in money-facts-2026) |

## C.3 COMPUTED — the $ hero math (illustrative; compute in build code, label it)

Worked example **$5,000/month = $60,000/year**, chosen deliberately *below* the
BLS $6,545/mo average so the number is conservative and cannot be read as a
promise. `corpus = annual income ÷ rate`.

| Route | Rate | Corpus for **$5,000/mo** | Corpus for the BLS avg **$6,545/mo** |
|---|---|---|---|
| Bengen 1994 / Trinity 1998 | **4.0%** | **$1,500,000** | $1,963,375 |
| Morningstar, for a 2026 retiree | **3.9%** | $1,538,462 | $2,013,718 |
| Bengen's own 2025 revision | **4.7%** | $1,276,596 | $1,670,957 |
| Live on a **dividend fund's** payout only | **3.11%** (SCHD) | $1,929,260 | $2,525,241 |
| **Live on S&P 500 dividends only** | **1.08%** | **$5,555,556** | **$7,271,759** |

**★ THE $ HERO NUMBER: $1.5 million at a 4% withdrawal rate is $5,000 a month —
but if you insist on living on S&P 500 *dividends* alone, the same $5,000 a
month needs about $5.6 million.**

That gap **is the video**, and it is the honest answer to the format-twin phrase
"how much you need invested to live off dividends": **the S&P 500 pays about 1%,
so dividends-only costs you roughly 3.7× the corpus** that a total-return
withdrawal plan needs. Every input is sourced; the output is division.

- Both numbers must appear **with their rate in the same frame**
  (`withdrawal_rate_on_screen`). "$1.5M" alone is a fabricated promise;
  "$1.5M at 4%" is arithmetic.
- $5.6M ÷ $1.5M = **3.7×**. Safe to show as "roughly four times". Do not speak
  "3.7" — it is a ratio of two SOFT decimals.

---

# PART D — Retire-early / financial-freedom claims (constraint `no_unsourced_retire_early`)

**There is exactly one sourced statement available about early retirement, and
it is a limit, not a promise:**

> *"Early retirees who anticipate long payout periods should plan on lower
> withdrawal rates."*
> — Cooley, Hubbard & Walz, *AAII Journal*, February 1998, Conclusion.
> https://www.aaii.com/journal/199802/feature.pdf — **read direct**

Corroborated by: Bengen's worst case being a **30-year** horizon (1994), and
Pfau (JFP Dec 2010) finding longer horizons and non-US markets both push the
sustainable rate down.

**Therefore, permitted and forbidden:**

- ✅ Permitted: "the four percent rule was built for a thirty-year retirement —
  its own authors say that if you stop working early, you have to withdraw
  less." Dated, sourced, primary.
- ❌ Forbidden, no source exists in this file: any "retire at 40/45/50", "quit
  your job in N years", "financial freedom by age X", or "this corpus means you
  never work again" claim, in either cut.
- ❌ Forbidden: presenting any corpus figure as an *achievement date*. The SIP
  tables in B.3 are "what it costs per month", never "you'll be free by 2046".

---

# PART E — Blog-tier numbers found and REJECTED (do not rediscover)

| Number / claim | Where it came from | Why rejected |
|---|---|---|
| "Safe withdrawal rate India is 3.5%, better than the 4% rule" as a standalone figure | https://www.basunivesh.com/safe-withdrawal-rate-india/ · https://hisabhkaro.com/learn/safe-retirement-withdrawal-rate-india/ · https://fincalculator.in/blog/safe-withdrawal-rate-explained · https://1finance.co.in/blog/what-is-safe-withdrawal-rate/ · https://blog.vrid.in/2025/11/11/indias-safe-withdrawal-rate-what-the-new-research-says/ | All repackage the **same Raju/Saraogi papers**. Cite the papers, not the blogs. Treating these as independent corroboration would fake a consensus that is one author group |
| "SWR 3.5–4.2% for the sub-₹12-lakh tax bracket, 2.7–3.2% at 30%" | surfaced in search summaries of the India SWR blogs | Tax-bracket-specific SWRs are a **model output**, not a published headline; no primary read. Would put a false-precision tax claim on screen |
| Post-office / SCSS / POMIS rate tables | https://www.bankbazaar.com/life-insurance/postal-life-insurance/post-office-monthly-income-scheme.html · https://www.policybazaar.com/... · https://scripbox.com/plan/post-office-monthly-income-scheme-calculator/ · https://www.bajajfinserv.in/investments/post-office-monthly-income-scheme · https://groww.in/calculators/... · https://schemesinindia.in/... · https://indiapolicyhub.in/... · https://calcwise.finance/... | Affiliate/SEO rate pages. Used Upstox (read direct) + the DEA notification coverage already banked in money-facts-2026 instead |
| POMIS "₹5,500/month on ₹9 lakh" | Upstox and every secondary | **Their rounding is wrong-ish.** ₹9,00,000 × 7.4% ÷ 12 = **₹5,550**, not ₹5,500. Use ₹5,550 as COMPUTED, or say "about fifty-five hundred". The joint figure ₹9,250 *is* exact |
| Nifty 50 return tables | https://www.bajajamc.com/knowledge-centre/nifty-50-historical-returns · https://www.multibagg.ai/... · https://primeinvestor.in/nifty-50-returns/ · https://premium.capitalmind.in/nifty-50-returns/ | Aggregators. NSE's own factsheet figures used instead — still SOFT, all three NSE hosts 403'd for the second run running |
| "S&P 500 average return 10.33% / 10.59% / 10.3%" | smartasset · sofi · carry · fool | Already killed in money-facts-2026. Four sources, four decimals, no shared methodology |
| Any single VYM / SCHD yield decimal presented as *the* yield | stockanalysis 3.11% vs Motley Fool 3.3% vs Schwab 30-day SEC 3.41% | Three reads, three numbers, three methodologies (TTM vs 30-day SEC). **Say "about three percent"** |
| "4% rule is dead / no longer works" headlines | https://money.usnews.com/money/retirement/articles/the-4-rule-no-longer-works-for-retirees-says-the-man-who-invented-it · https://quantflowlab.com/4-rule/ · https://www.compoundladder.com/guides/4-percent-rule · https://www.bullseyeretirement.com/articles/bengen-new-5-percent-rule | Headline framing, and it inverts the actual news — Bengen revised the rate **up** to 4.7%, not down. Cite the revision, never the headline |
| Schwab's "fatal flaw" framing | https://www.thestreet.com/personal-finance/schwab-exposes-a-fatal-flaw-in-retirement-spending | Third-party summary of Schwab; **schwab.com itself returned an authorization error** (ref 0915-82LR). No Schwab primary was read — do not attribute anything to Schwab |
| AMFI July 2026 data | — | **Does not exist yet.** AMFI publishes within the first 10 business days of the following month; the July note lands ~2026-08-08 to 08-12. June 2026 is the latest. Do not let a later stage "find" a July figure |

# PART F — Do not claim (this topic)

- **Any return rate spoken as an expectation.** ~12% (India) and ~10% (US) are
  *historical shapes* and both are SOFT on the decimal. Every use is
  "if it returned X" — never "it returns X". (`no_return_promise`)
- **A corpus figure without its withdrawal rate in the same frame.** This is the
  one thing `fin-audit` will hard-fail. (`withdrawal_rate_on_screen`)
- **The word "dividend" or any Devanagari transliteration in the hi cut** — in
  script, on-screen text, title, tags, or file names. Including inside any
  explanation of Total Return Index (see the B.1 trap).
- **4% in the ₹ cut as advice.** It appears only as *the imported rule this
  video corrects*, always beside India's 3%.
- **Any retire-early / freedom-by-age claim.** See Part D — the only sourced
  early-retirement line is a warning to withdraw *less*.
- **Cross-market arithmetic.** ₹1 crore is not $1.5M. Never a conversion, never a
  shared chart axis, never "which is about".
- **A specific fund, AMC, bank, ETF or product as a recommendation.** SCHD and
  VYM appear as *yield evidence for an asset class*, and only in the $ cut.
  POMIS/SCSS/PPF appear as *published government rates*. Never "buy this".
- **A precise India tax number.** The 12.5%/₹1.25 lakh row is SOFT — no statute
  or Income Tax Department page was read this run.
- **Attributing anything to Schwab, AMFI, NSE, PIB, MoSPI, SSRN or the FPA as
  "read"** — every one of those domains failed this run. The log lists them.
