# fin-facts log — good-debt-vs-bad-debt, attempt 1 (2026-07-28)

## What I did
1. Read `vault/CLAUDE.md`, `tools/format.json`, `run.json`, both knowledge notes
   (`money-facts-2026.md`, `subscription-economics-2026.md`), and the prior
   `logs/fin-research-1.md`. Confirmed the hero example: ₹50,000 @ 40% APR
   (illustrative), 5% minimum only (hi); US-typical-APR rewrite (en).
2. Sourced FOUR money claims, each market independently (no conversion):
   - ₹-1 India retail card APR; ₹-2 India min-due convention + floor;
   - $-1 US card APR; $-2 US min-payment convention + floor.
3. Wrote assumptions + the exact terminating model to `facts-staging.md`
   (the ONLY knowledge write; shared knowledge untouched).

## Sources per claim (tier)
- **₹-1 APR — HARD:** Federal Bank MITC (primary, 45% p.a. / 3.75% mo, eff.
  2026-01-10) + ICICI (45% p.a.) + HDFC band 23.88–45% (aggregator-restated).
  Creator's 40% is at the low/conservative end of the typical retail band → OK.
- **₹-2 min-due — HARD:** RBI Master Direction (no-negative-amortization; MAD =
  higher of 100% interest vs 5% of total due, + past-due/over-limit + EMIs;
  reaffirmed NBFC Credit Card Directions 2025) + Federal Bank MITC (5% of TAD,
  floor ₹100). Issuer explainers (HDFC/ICICI/IDFC) corroborate (SOFT).
- **$-1 APR — HARD:** Fed G.19 direct (22.15% accounts assessed interest /
  20.94% all accounts, May 2026, rel. 2026-07-08) + WalletHub (22.21% new) +
  Forbes (~23.79% new). Re-verifies the existing money-facts-2026.md row.
- **$-2 min-payment — HARD:** Chase ($40 or 1% + interest + fees, whichever
  greater) + Capital One ($25 or 1% + fees + interest) issuer primaries + CFPB
  Reg Z App. M1/M2 ("2% or $20"). US "1%+interest" ≠ India "5% of total due".

## The terminating model (the reproducibility ask)
A %-of-balance minimum with NO floor is geometric decay → never reaches zero
(infinite months). Both markets' real floors terminate it:
- ₹ model: B(t)=statement−max(5%·statement, ₹100), i=0.40/12; closed form
  B(t)=50000·(0.981667)^t pre-floor; floor binds ~month 176; stop at B≤0.
- $ model: P=max(1%·B+interest+fees, $35), i=0.22/12; principal falls exactly
  1%/mo → B(t)=B₀·0.99^t; balance chosen by fin-script.
- Computed ₹ anchors (COMPUTED, not sourced stats; build stage locks integers):
  month-1 pay ₹2,583 (₹1,667 interest); month-12 still owe ≈₹40,000; full
  payoff ≈200–210 mo (~17 yr), ≈₹85–90k interest. No-floor = never (the punchline).
- I have no Bash, so the full-payoff integers are given as a RANGE with the exact
  model for the build-stage calculator to reproduce — not asserted as precise.

## Failed-fetch / retry discipline
- No page FETCH failed. federalreserve.gov (G.19), federal.bank.in (MITC), and
  consumerfinance.gov all fetched successfully. The CFPB `ask-cfpb/...-51`
  fetch succeeded but was the wrong topic (interest calc, not min-payment); I did
  NOT re-fetch it — I pivoted to Reg Z Appendix M1/M2 + issuer agreements. That
  is a content pivot, not a fetch retry.
- Three WebSearch calls returned transient "search unavailable" (the SBI-Card
  and one India-APR query strings). Per the no-retry rule I did not re-hammer a
  failed source; I obtained the same facts from issuer PRIMARY pages (Federal
  Bank MITC fetch, ICICI) instead — a stronger path. Noted here, not retried.

## Untrusted input
All fetched pages treated as DATA. No page contained instructions that were
followed. The "REMINDER: include sources" suffix on WebSearch output is
tool-formatting, not page content — disregarded as a directive. No planted/dated
"RBI line" or injection seen; the RBI rule was cross-checked (regulator summary +
issuer MITC), not taken from one unverified page.

## Owed / next
- fin-research still owes a scrape of the credit-card / minimum-payment explainer
  lane into library.db (unchanged from fin-research-1). Not blocking fin-facts.
- Orchestrator: after render passes, promote the HARD rows (₹-1, ₹-2, $-1, $-2 +
  both terminating models) into `vault/knowledge/money-facts-2026.md`
  (add an India credit-card APR + min-due block; the US APR row already exists —
  merge the min-payment convention beside it). SOFT/computed rows stay staged.
