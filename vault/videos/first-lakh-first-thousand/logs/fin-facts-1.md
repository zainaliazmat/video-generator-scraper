# fin-facts log — first-lakh-first-thousand, attempt 1 (2026-07-31)

Result: **ok** (after one formatting correction — see the last section).
Artifact: `vault/videos/first-lakh-first-thousand/facts-staging.md`.

## Read first
`vault/CLAUDE.md`, `tools/format.json`, `vault/knowledge/money-facts-2026.md`,
`vault/knowledge/subscription-economics-2026.md`,
`vault/videos/first-lakh-first-thousand/run.json`,
`vault/knowledge/video-studies/first-lakh-first-thousand.md`.

The topic needed two things money-facts did not have: **a return rate for each
market** (to compute months-to-milestone) and **the Munger attribution** the
creator brief asked fin-facts to verify.

## Sources read directly (primary — these are the HARD spine)
- https://www.fdic.gov/national-rates-and-rate-caps — savings 0.38%, MMA 0.65%,
  cap 4.38%, as of **2026-07-20**. Re-verifies the 0.38% already in money-facts.
- https://www.bea.gov/news/2026/personal-income-and-outlays-june-2026 — personal
  saving rate **2.7%**, personal saving $646.1bn, released **2026-07-30**. This
  **supersedes** the 3.0% (May 2026) row in money-facts; the orchestrator should
  update that row on promotion.
- https://www.federalreserve.gov/monetarypolicy/openmarket.htm — fed funds target
  **3.50–3.75%**, last changed 2025-12-11. Note the page lists rate *changes*,
  not meetings, so "unchanged since December" is the correct reading.

## Two-independent-source pairs (HARD without a primary read)
- **India small savings, Q2 FY2026-27**: Business Today (2026-06-30) table +
  two Business Standard pieces (…126063000945, …126063001142), both quoting the
  DEA notification. They independently agree on PPF 7.1%, post office savings
  4.0%, 3-yr TD 7.1%, SSY 8.2%. Rates only Business Today lists are tagged SOFT.
- **Post Office RD 6.7%**: Business Today + Upstox comparison (2026-07-06).

## Failed fetches — reported, NOT retried (per contract)
| URL | Failure |
|---|---|
| http://dea.gov.in/budget-division/475 | DNS timeout (ETIMEOUT) |
| https://sbi.bank.in/web/interest-rates/interest-rates/deposit-rates | empty response |
| https://www.marcus.com/us/en/savings/high-yield-savings | 403 |
| https://www.icicibank.com/personal-banking/deposits/fixed-deposit/fd-interest-rates | 403 |
| https://www.hdfcbank.com/personal/save/deposits/fixed-deposit-interest-rate | 403 |
| https://www.niftyindices.com/Factsheet/ind_nifty50.pdf | 403 |
| https://archives.nseindia.com/content/indices/ind_nifty50.pdf | 403 |
| https://www.indiapost.gov.in/Financial/pages/content/post-office-saving-schemes.aspx | 404 |
| https://www.newsonair.gov.in/interest-rate-on-small-saving-schemes-remains-unchanged-for-next-qrt/?noshow=1 | ECONNRESET |
| https://www.ally.com/bank/online-savings-account/ | fetched, but the page states no APY (only "more than 5x the national average of 0.38%") |

Consequence: **every Indian issuer price card and both NSE PDFs were
unreachable**, so bank RD/FD rates, the SBI savings rate and the Nifty 50 TRI
figure are all **SOFT**. This is the same network pattern the credit-history run
hit (rbi.org.in / cibil.com 403) — it is now three runs in a row, and looks
structural rather than transient. Worth the orchestrator's attention: an India
₹-rate claim can currently only reach HARD via two independent Indian press
outlets quoting a government notification.

## Data anomaly (not an injection)
https://www.capitalone.com/bank/savings-accounts/online-performance-savings-account/
rendered its APY as literally **"NaN APY"** with disclosure "A rate of NaN
Annual Percentage Yield (APY) applies to all account balances… effective as of
7/29/2026". A broken price card, not an attack. No figure taken from it.

## Untrusted-input check
No fetched page contained instructions, role-play, or planted directives. No
page attempted to introduce a dated fake regulator line. Nothing was followed;
every page was treated as data. The only anomaly is the Capital One "NaN" above.

## Conflicts recorded rather than resolved (per contract §3)
- **S&P 500 long-run return**: 10.69% nominal / 6.81% real (officialdata.org,
  Shiller dataset) vs 10.33% / 10.59% / 10.3% (smartasset, sofi, carry, Motley
  Fool). All recorded; staged as **HARD on "about ten percent", SOFT on every
  decimal**. The script may not speak a decimal.
- **Nifty 50 TRI**: 12.41% since inception (factsheet 2026-06-30) vs 12.44%
  20-year (Whitepaper 2026, to 2026-02-27). Both recorded, both SOFT.

## The Munger question the brief asked
Answer: **it does not verify to a primary.** The wording is stable across a
dozen secondary sources and is attributed to a 1990s Berkshire meeting and/or
Janet Lowe's *Damn Right!* (2000), but no transcript, recording or verified page
cite was reachable. Staged **SOFT** with an explicit safe-paraphrase and an
explicit ban on stating a year or venue.

**More useful than the quote:** the computed US crossover at the locked $800/mo
example and a ~10% market is **≈$96,000** — i.e. Munger's $100,000 is
arithmetically the point where returns overtake contributions. The script can
make that its ~70% re-frame beat (the study note calls for exactly one) and the
quote becomes colour instead of evidence.

## The one thing most likely to go wrong downstream
₹1 lakh is the *psychological* milestone; the ₹ **crossover** is ~₹4.8–8.5 lakh
depending on rate. A script that says "after the first lakh, compounding takes
over" is factually wrong. Flagged in facts-staging §1.3 and §4.

## Check failure and correction (formatting only)
Attempt 1 **failed `check_facts`** (`tools/pipeline_check.py:108`), which
requires `re.search(r"https?://", text)`:

```
FAIL facts
  ✗ facts-staging.md contains no source URL — every money claim needs a recorded source
```

Cause was mine and purely presentational: I recorded sources as bare
host+path strings (`bea.gov/news/…`, `fdic.gov/national-rates-and-rate-caps`)
with no scheme, matching the house style in money-facts-2026.md — which the
checker cannot see as URLs.

Corrected by prepending the scheme actually used to every source string in
facts-staging.md, including the rejected-sources table so the record of what was
thrown out stays checkable. **No URL was invented, completed or "improved"** —
every one is a link this stage retrieved or saw returned by search. No figure,
tag, computation or claim changed: HARD stayed HARD, SOFT stayed SOFT, and the
two 403'd niftyindices PDFs plus the unfetched sbi.bank.in page keep their SOFT
tag and their "not fetched / read via search index only" caveats. A resolvable
URL is not a verified fetch, so a scheme is not an upgrade; a new paragraph
under the tag legend now says that explicitly so a later reader does not mistake
a tidy link for a read page.

## Write discipline
Wrote exactly two files: `facts-staging.md` and this log. Did **not** touch
`vault/knowledge/money-facts-2026.md` or any shared knowledge file — the BEA
2.7% supersession and the four HARD India rows are staged for the orchestrator
to promote after the render passes.
