---
summary: fin-facts attempt 1 for passive-income-number — OK. Both markets' hero corpus numbers staged with their withdrawal rates; the 4% rule staged with its 1994/1998 origin and five documented criticisms, one of them primary and self-stated. Nothing promoted to shared knowledge.
updated: 2026-08-07
source: See facts-staging.md for every URL and its read/not-read status.
stage: fin-facts, attempt 1
---

# fin-facts — passive-income-number — attempt 1 — OK

## What I read first

`vault/CLAUDE.md` · `vault/videos/passive-income-number/run.json` (constraints
block binding) · `vault/knowledge/money-facts-2026.md` ·
`vault/knowledge/subscription-economics-2026.md` · `tools/format.json` ·
`vault/videos/first-lakh-first-thousand/facts-staging.md` (format reference) ·
`vault/videos/passive-income-number/logs/fin-research-1.md`.

Per the brief, the failed fin-research attempt is context only — **no study
note exists and none is cited.** Nothing in this file came from a transcript.

## The two primaries I actually read, in full

This run's quality rests on two documents that were retrieved and read, not
summarised:

1. **Cooley, Hubbard & Walz, "Retirement Savings: Choosing a Withdrawal Rate
   That Is Sustainable", *AAII Journal*, February 1998, pp. 16–21** — the
   Trinity Study. `https://www.aaii.com/journal/199802/feature.pdf` returned
   binary to the fetch tool, which saved it to disk; I read all six pages
   including Tables 1–4. This gave me the 30-year inflation-adjusted success
   rates at 4%, the 1926–1995 data period, and — the most valuable line in the
   run — the authors' own two limitations, verbatim: *"The study did not adjust
   for taxes or transaction costs"* and *"Early retirees who anticipate long
   payout periods should plan on lower withdrawal rates."*
   A criticism stated by the paper itself is the strongest possible tier, and
   it is what lets the script say "not a law" without editorialising.
2. **The PortfolioConstruction Forum review of Bengen (1994)** — same
   save-to-disk path. Gave the 50/50 allocation, the 1926–1966 start years, the
   worst case of ~30 years for a 1976 retiree, and 3.5%-always-survives.

## Sourcing posture per constraint

| Constraint | How it is satisfied in facts-staging.md |
|---|---|
| `no_return_promise` | Every corpus row is `annual income ÷ rate`, with the formula printed. The two return rates (~12% India, ~10% US) are tagged SOFT-on-decimal and marked "shape only". Part F forbids speaking either as an expectation |
| `withdrawal_rate_on_screen` | **Part A exists solely for this.** The rate is staged as a fact *before* any corpus figure, with its own sources — Bengen 1994, Trinity 1998, Morningstar 3.9% for 2026, Bengen's own 4.7% revision, and India's 3.0–3.5%. Every hero line in B.3/C.3 is written as "₹1 crore **at 3%**", never bare |
| `no_unsourced_retire_early` | Part D. Exactly one sourced early-retirement statement exists and it is a *limit* (Trinity's conclusion, read direct). Everything else is explicitly forbidden with the reason |
| `hi_currency_framing` | Part B is SIP/SWP/POMIS/passive-income vocabulary throughout. **I found and flagged one live trap the script would otherwise walk into:** "Total Return Index" is defined as price return **plus dividend return** — explaining Nifty TRI in the hi cut forces the banned word. Fix staged in B.1: never explain TRI in hi, quote the number only |

## The two conflicts I recorded instead of resolving

Per the contract, both sides are in the file and both rows are tagged SOFT:

1. **Pfau's country count.** SSRN and the FPA abstract say **17 countries /
   109 years**; Pfau's own retirementresearcher.com says **19 countries /
   1900–2010**. Both recorded. On-screen instruction: say "most developed
   markets", never a count.
2. **The SCHD yield.** stockanalysis.com 3.11% TTM (read direct) vs Motley Fool
   3.3% vs a 3.41% 30-day SEC yield — three methodologies, three numbers, and
   the Schwab issuer price card 403'd. Recorded all three; on screen "about
   three percent".

## One naming trap that nearly produced a wrong on-screen line

My first two searches returned **"Morningstar 2025 = 3.9%"** and
**"Morningstar 2026 = 3.9%, up from 3.7% in 2025"** — apparently contradictory.
They are not. Morningstar's report titled ***The State of Retirement Income:
2025 Edition*** (published 2025-12-03) sets the rate for a **2026** retiree.
Report year ≠ retiree year, and secondary coverage mixes them constantly. Had I
taken the first result, the video would have put a mislabelled year beside a
withdrawal rate. Resolved with three independent sources and written into
facts-staging.md as an explicit warning, because the next stage will hit the
same search results. This is the same failure mode as the G.19 "Q2 2026 vs May
2026 monthly" mislabel already recorded in money-facts-2026.

## Fetch failures (recorded, not retried — the orchestrator owns retries)

Every one of these is marked in facts-staging.md at the row it affects, and the
row's tag reflects it. **No figure below was upgraded past what its actual read
supports.**

| Domain | Result | Consequence |
|---|---|---|
| `niftyindices.com`, `archives.nseindia.com`, `nsearchives.nseindia.com` | 403 (all three) | Nifty 50 TRI 12.41% stays **SOFT** — second consecutive run, same as 2026-07-31 |
| `papers.ssrn.com` | 403 | All three India SWR papers are **via search index**; the band is HARD only because freefincal corroborates independently |
| `actuariesindia.org` | TLS: unable to verify first certificate | The Institute of Actuaries presentation not read |
| `bls.gov` (news release, PDF, and TED) + `fred.stlouisfed.org` | 403 | $78,535 tagged HARD on the strength of **three BLS-owned surfaces agreeing** via search index — same posture money-facts-2026 already uses for the BLS weekly-earnings row |
| `morningstar.com`, `financialplanningassociation.org` | 403 | Morningstar 3.9% via three independent secondaries; Bengen's 1994 PDF never read (the review was) |
| `schwab.com` | authorization error, ref 0915-82LR | **Nothing is attributed to Schwab.** Listed in Part E as rejected |
| `amfiindia.com` | ECONNREFUSED | SWP definition rests on four AMC (issuer) pages instead; SIP/AUM figures stay SOFT context |
| `pib.gov.in`, `mospi.gov.in` | 403 / not fetched | India CPI 4.38% June 2026 tagged **SOFT** — no government surface read |
| `indiapost.gov.in` | 404 | POMIS caps rest on unanimous secondary agreement, not the issuer |
| `cleartax.in`, `business-standard.com`, `schwabassetmanagement.com`, `investor.vanguard.com` | 403 / DNS / no data | LTCG row **SOFT**; **VYM yield marked NOT USABLE** rather than guessed |

`business-standard.com` failed DNS resolution this session, which is worth
flagging: it is a load-bearing source for the small-savings rows already banked
in money-facts-2026. Those rows were carried forward as previously verified, not
re-verified this run.

## An arithmetic error in the sources, caught

Every secondary states POMIS pays **₹5,500/month** on the ₹9 lakh maximum.
₹9,00,000 × 7.4% ÷ 12 = **₹5,550**. Their figure is a rounding, not the rate's
output. Staged as ₹5,550 COMPUTED with the discrepancy noted, so a later stage
does not "correct" it back to the wrong number. (The joint-account ₹9,250 *is*
exact.)

## Untrusted input

Roughly forty pages were fetched or search-indexed this run. **No page contained
an instruction directed at me** — no "ignore previous instructions", no planted
directive, no fake dated regulator line. The nearest thing to a manipulation
risk was structural rather than adversarial and is worth naming:

- **A manufactured consensus.** Five India personal-finance blogs
  (basunivesh, hisabhkaro, fincalculator, 1finance, vrid) all state "India's SWR
  is 3–3.5%" as though independently established. They are all repackaging the
  **same two Raju/Saraogi papers**. Counting them as corroboration would have
  produced a fake five-source HARD tag on a one-author-group finding. They are
  listed in Part E as rejected, and the band is HARD only because **freefincal
  (Pattabiraman) reaches the same range from a different practitioner
  backtest**. This is the same disease as the fabricated "CICRA 2005 seven-year
  rule" already recorded in money-facts-2026: many Indian blogs, one origin.
- Headline inversion: several outlets frame Bengen's revision as "the 4% rule no
  longer works". He moved it **up**, to 4.7%. Rejected in Part E.

## The one write rule

Written this run: `vault/videos/passive-income-number/facts-staging.md` and this
log. **`vault/knowledge/money-facts-2026.md` was read and NOT modified**, nor was
any other shared knowledge file. Promotion is the orchestrator's, after render.

Candidates worth promoting if the render passes: the Trinity/Bengen provenance
block (A.1–A.2, primary, durable, market-independent), the S&P 500 dividend
yield ≈1% row, the BLS $78,535 row, and the India 3.0–3.5% SWR band. The Nifty
TRI row should **not** be promoted until someone reaches an NSE host.

## Owed

1. **An NSE-reachable network path.** Three hosts, two runs, six 403s. The Nifty
   long-run return is load-bearing for any India investing video and is stuck at
   SOFT purely on retrieval.
2. **An Income Tax Department primary for §112A.** The 12.5%/₹1.25 lakh figures
   are consistent across four tax-content sites but unread at source; any future
   India video touching capital gains needs this properly.
3. **AMFI's July 2026 monthly note** (lands ~2026-08-08). Not needed by this
   script; flagged so a later stage does not invent one.
