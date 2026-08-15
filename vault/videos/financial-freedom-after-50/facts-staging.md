---
summary: Sourced money figures for financial-freedom-after-50 (en/$ only). Every row carries its primary source URL inline AND links to a claim note in vault/claims/, which links to a source note in vault/sources/<agency>/. HARD rows are promotable by tools/close_out.py after both renders pass; SOFT rows never are.
updated: 2026-08-15
source: fin-evidence attempts 1-2, 2026-08-15. IRS Notice 2025-67 / IR-2025-111 / COLA table / Pub 969 / RMD FAQ / Roth catch-up final regs / Notice 2023-62; SSA planner + OACT + 2026 COLA fact sheet; Federal Reserve G.19; 26 U.S.C. §223.
stage: STAGING — not promoted, not shared knowledge
---

# facts-staging — financial-freedom-after-50 (en, US/$)

**Market: US / $ only.** No ₹ figure appears in this run and none may. The topic is US tax and
Social Security law; there is no second market to source and nothing to convert.

Every creator-supplied figure listed as UNVERIFIED in `notes.md` has been checked against its
issuing agency. **All nine survived. Zero corrections to any number.** The corrections this run
recommends are to *framing*, not arithmetic — see §3.

> **On the two layers of sourcing in this file.** Each row below carries its **primary source URL
> inline**, and also links to a claim note that links to a full source note. The inline URL is not
> a duplicate for convenience — `tools/close_out.py` promotes HARD rows *out of this file* into
> `money-facts-2026.md`, so a row that cannot show its own source is a row that would land in
> shared knowledge unsourced. The vault-note layer carries the retrieval caveats, the expiry
> mechanics and the "what this is NOT authoritative for" column; the URL layer travels with the
> row. Both are required.

---

## 1. HARD — verified, primary, promotable

| # | Claim | Figure | Primary source URL | Claim note | Expiry |
|---|---|---|---|---|---|
| 1 | 401(k)/403(b)/457/TSP elective deferral, 2026 | **$24,500** | https://www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions | [[../../claims/401k-elective-deferral-2026]] | annual, 2027-01-31 |
| 2 | Age-50 catch-up, 2026 | **$8,000** → total **$32,500** | https://www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions | [[../../claims/401k-catchup-age50-2026]] | annual, 2027-01-31 |
| 3 | SECURE 2.0 catch-up, ages 60–63, 2026 | **$11,250** → total **$35,750** | https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500 | [[../../claims/401k-supercatchup-60-63-2026]] | annual, 2027-01-31 |
| 4 | IRA limit + catch-up, 2026 | **$7,500 + $1,100 = $8,600** | https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500 | [[../../claims/ira-limit-2026]] | annual, 2027-01-31 |
| 5 | Roth-mandated catch-up wage threshold | **$150,000** prior-year (2025) FICA wages | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | [[../../claims/roth-catchup-threshold-2026]] | annual, 2027-01-31 |
| 6 | HSA additional contribution, age 55+ | **$1,000** | https://www.irs.gov/publications/p969 | [[../../claims/hsa-catchup-age55]] | **stable**, 2027-08-15 |
| 7 | Early-claim reduction at 62 | **30%** (FRA 67) · 25% (FRA 66) | https://www.ssa.gov/benefits/retirement/planner/agereduction.html | [[../../claims/ss-early-claim-reduction-62]] | stable, 2027-08-15 |
| 8 | Delayed retirement credit | **8%/yr to age 70** → **24%** (FRA 67) · 32% (FRA 66) | https://www.ssa.gov/benefits/retirement/planner/delayret.html | [[../../claims/ss-delayed-retirement-credit]] | stable, 2027-08-15 |
| 9 | RMD beginning age | **73** | https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs | [[../../claims/rmd-beginning-age-73]] | stable, 2027-08-15 |
| 10 | Earnings test, 2026 (**held in reserve — see §4**) | **$24,480** / **$65,160** | https://www.ssa.gov/news/en/cola/factsheets/2026.html | [[../../claims/ss-earnings-test-2026]] | annual, 2027-01-31 |
| 11 | Credit card interest, shape only | **north of 20%/yr** | https://www.federalreserve.gov/releases/g19/current/ | [[../../claims/credit-card-apr-shape-2026]] | **monthly**, 2026-09-15 |

### Corroborating URLs (the second and third source behind each row)

The table above shows **one** URL per row — the one best suited to the on-screen source shot.
Every row is multi-sourced; these are the rest.

- **Rows 1–4 (all 2026 IRS contribution limits)** are triple-sourced. All three read this run:
  - IRS Notice 2025-67 (the notice itself) — https://www.irs.gov/pub/irs-drop/n-25-67.pdf
  - IR-2025-111 (the newsroom release) — https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500
  - COLA limits table (the standing page, shows 2026 beside 2025 in one row — **best screen-record target**) — https://www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions
- **Row 5** needs all three of these together, and the reason is in §4's runner-up trap:
  - Notice 2025-67 (the $150,000 amount) — https://www.irs.gov/pub/irs-drop/n-25-67.pdf
  - Notice 2023-62 (the transition period that ended 2025-12-31, i.e. **why the rule bites in 2026**) — https://www.irs.gov/pub/irs-drop/n-23-62.pdf
  - IR-2025-91 final regulations — https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-on-new-roth-catch-up-rule-other-secure-2point0-act-provisions
- **Row 6** — 26 U.S.C. §223(b)(3), the statute fixing $1,000 for "2009 and thereafter" with no
  COLA clause (this is why the class is `stable`, not `annual`) —
  https://www.law.cornell.edu/uscode/text/26/223
- **Row 7** — SSA OACT actuarial page — https://www.ssa.gov/oact/quickcalc/earlyretire.html ·
  FRA 67 for birth years 1960+ — https://www.ssa.gov/news/en/cola/factsheets/2026.html
- **Row 8** — SSA OACT delayed-retirement-credit table — https://www.ssa.gov/oact/ProgData/ar_drc.html
- **Row 11** — conflicting prior readings of the same series are recorded in
  [[../../knowledge/money-facts-2026]] (22.15% "May 2026 monthly"; 21.52% "Q1 2026") against this
  release's 21.52% "June 2026". See the warning below.

⚠️ **Rows 7, 8 and 10 (all SSA):** the URLs above are the correct, citable primary documents, but
**ssa.gov returned HTTP 403 to every direct fetch from this pipeline.** The figures were recovered
via domain-restricted search of ssa.gov returning SSA's own page text, corroborated across three
distinct SSA documents. The percentages are statutory and cross-agree, so the rows stand HARD —
but the screenshot must be captured from a network path that can actually reach ssa.gov. See §6.

⚠️ **Row 5's URL is a PDF that does not read inline** through this pipeline's fetcher (returns
compressed binary). Its figures are corroborated by the IRS **HTML** pages listed above, all of
which were read directly. Nothing in rows 1–5 rests on an unread PDF alone.

**Row 11 is HARD on the shape and SOFT on every decimal.** The same 21.52% is carrying three
different period labels across reads of the same series. Say *north of 20%*. Never a decimal,
never a period label.

**Row 9 is single-sourced** (one IRS page). HARD because the IRS is the sole authority and the
age is statutory, but attach Pub 590-B before any future video leads on RMDs.

### Already HARD in the vault — reuse, do not re-source
Both live in [[../../knowledge/money-facts-2026]] with their sources; not re-fetched this run, so
no URL is asserted here that this run did not itself retrieve.
- **$400 emergency**: 63% of US adults could cover it with cash (→ ~4 in 10 could not).
  Federal Reserve SHED, *Economic Well-Being of U.S. Households in 2025*, rel. May 2026.
  The strongest available opener for Step 1.
- **FDIC insurance limit $250,000** per depositor / bank / ownership category — if the
  "separate high-yield savings account" beat wants a card.

---

## 2. SOFT / convention — never promoted, label on screen

| Claim | Status | Handling |
|---|---|---|
| **The 4% rule** | **Not a government figure and never will be.** Origin: William P. Bengen, "Determining Withdrawal Rates Using Historical Data," *Journal of Financial Planning* 7(4), October 1994; popularised by the Trinity study (Cooley/Hubbard/Walz, 1998). No whitelisted agency publishes it, so **no primary URL exists to give it** — that absence is the finding. | The draft already frames it as "a starting guideline, not gospel" — **that hedge is the only thing making this sentence publishable. Do not let any stage remove or soften it.** On screen: no source card, label **opinion/convention**, never "verified". Provenance itself is secondary-sourced this run — say "a 1994 study", not a citation you have not read. |
| **Emergency fund of 3–6 months of essential expenses** | US convention, not a statistic. Same class as the "$1,000 starter fund" row already in money-facts. | Frame as "the standard advice", no source card, no agency name. |
| **"Healthcare costs are the number one financial fear for retirees"** | **Unsourced superlative.** No whitelisted agency publishes a ranked fear list; the surveys that do (EBRI, Gallup) are not on the §1 whitelist. | Two options: (a) label **opinion** — "in my experience it is the fear I hear most" — which fits the creator's first-person voice, or (b) cut the ranking and keep "healthcare costs are a real risk to the plan". **Do not cite anyone for the #1 ranking.** |
| **"Long-term care can be astronomical"** | No figure in the draft, and that is correct. | Keep it numberless. The commonly-quoted cost tables (Genworth) and the "70% chance of needing care" statistic (HHS/ACL) are **not on the whitelist**. Rejected — see §5. |
| **"Fifteen years in the trenches"** | Creator's own first-person credibility claim, supplied deliberately. | `run.json → no_advice_framing` already rules: keep as written, never extend into credentials. Not a money claim; no source needed. |

---

## 3. Framing corrections recommended (numbers are all correct)

1. **The delayed-retirement-credit "return" line — the one real finding.**
   Draft: *"That's a guaranteed, inflation-adjusted return from the government that is simply
   impossible to find anywhere else."*
   The 8% DRC is a statutory benefit-formula adjustment, not a return. This sentence collides
   directly with `run.json → constraints.no_return_promise`, which names this exact figure.
   Suggested minimal rewrite preserving voice and rhythm:
   > "That's a permanent, inflation-adjusted increase written into the benefit formula — not a
   > market return, and not something you have to earn by taking risk."
   Detail in [[../../claims/ss-delayed-retirement-credit]].

2. **Attach a full retirement age to every SS percentage.** "25% to 30%" and "24% to 32%" are both
   correct bands, but only the **30%** and **24%** ends are reachable by anyone who can act on
   this video: FRA 66 belongs to birth years 1943–1954, who are 72+ in 2026. Keep the creator's
   band in the VO if `creator_wording_is_source_of_truth` is read strictly; put
   *"30% if your full retirement age is 67 — born 1960 or later"* on the card.

3. **Keep two hedges the draft already has.** They are doing compliance work and read as style:
   "If your plan allows it" (the 60–63 catch-up is plan-optional) and "assuming your plan has a
   Roth option". Neither is padding.

---

## 4. The trap to avoid

**The earnings test, and it is a trap of adjacency, not of error.** Step 4 says "keep earning,
part-time or consulting" and Step 4 says "delay Social Security". Together they are safe — the
earnings test only bites people who are *already collecting*. But a viewer who takes the
"keep working" half and separately claims at 62 loses **$1 of benefit for every $2 earned above
$24,480** (2026, SSA — https://www.ssa.gov/news/en/cola/factsheets/2026.html), and nothing in the
script warns them.

The script as written does not need the number. But **no stage may add a "claim early and keep
working" beat without it**, and if it is ever added the recalculation qualifier is mandatory:
withheld benefits are **not lost** — SSA credits them back at full retirement age. Sourced and
parked at [[../../claims/ss-earnings-test-2026]] so that adding it is cheap and inventing it is
unnecessary.

Runner-up trap: **reading the Roth catch-up final regs' "after December 31, 2026" as the start of
the rule.** It is the *regulations'* applicability date
(https://www.irs.gov/newsroom/treasury-irs-issue-final-regulations-on-new-roth-catch-up-rule-other-secure-2point0-act-provisions).
The mandate is operative in **2026** because the Notice 2023-62 transition period ended
2025-12-31 (https://www.irs.gov/pub/irs-drop/n-23-62.pdf). A later re-verification that consults
only the final-regs page will "correct" a correct script into a wrong one.

---

## 5. Blog-tier and off-whitelist numbers found and REJECTED — do not rediscover these

Listed so `fin-script` does not go looking and find them fresh. **No URLs are given for these on
purpose** — a rejected source does not get a citation in a staging file that feeds promotion.

| Number seen | Where it comes from | Why rejected |
|---|---|---|
| "70% chance of needing long-term care after 65" | HHS/ACL LongTermCare.gov | HHS/ACL is **not** on the fact-integrity §1 whitelist. Real-looking, widely repeated, unusable here. |
| Genworth Cost of Care survey figures (nursing home / assisted living annual costs) | Private insurer marketing research | Not whitelisted; an insurer publishing the cost of the risk it sells is the definition of an interested source. Draft says "astronomical" with no number — correct, keep it. |
| Fidelity "retiree health care cost estimate" (the ~$165k–$300k couple figure) | Fidelity | Aggregator/vendor, not an agency. Also a projection presented as a number. |
| "Average 401(k) balance for people in their 50s/60s" (Fidelity/Vanguard *How America Saves*) | Recordkeeper data | Not whitelisted **and** it is the "national average presented as personally applicable" anti-pattern (§5) — the exact thing this video's premise argues against. Using it would undercut the hook. |
| EBRI / Gallup "top retirement fear" rankings | Survey houses | Not whitelisted. See §2. |
| NerdWallet / Bankrate / Investopedia 2026 contribution-limit tables | Aggregators | Leads only. Followed back to IRS Notice 2025-67 and the IRS COLA table, which are what is cited in §1. |
| Any specific HYSA APY for the emergency-fund beat | Bank price cards | `money-facts-2026` "Do not claim" already forbids it — a rate dates the video. The durable form is "roughly 10× a typical savings account". |
| SSA $1,000/mo-style example benefit amounts | SSA illustration | Fine as SSA's own illustration, but it is an **example**, not a statistic. If shown, the word "example" must be in frame (§3). Not needed — the script uses percentages only. |

---

## 6. Owed

- **Every screenshot.** This stage has no browser or capture tool in its allowlist, so
  `vault/screenshots/` gained nothing. Eleven captures are owed; filenames are recorded in each
  source note's `screenshot:` field, and the URL to capture is in §1 above.
  Fact-gate point 1 and §4 of the standard cannot be satisfied by this run alone.
- **ssa.gov read from a network path that is not 403'd.** All four SSA figures came via
  domain-restricted search of ssa.gov, not a direct read. The percentages are statutory and
  cross-agree across three SSA documents, but the capture must be a real page.
- **The competitor study.** The lane is unmeasured — see
  [[../../knowledge/video-studies/financial-freedom-after-50]] (empty-lane finding) and the
  stage log. `library.db` holds no US retirement comparable in the LONG band (480–1800 s).
