# fin-facts log — pay-yourself-first, attempt 1 (2026-07-28)

## What was read
- vault/CLAUDE.md, tools/format.json
- vault/knowledge/money-facts-2026.md — salary anchors, SHED, BEA, FDIC,
  HYSA no-APY rule already sourced; used verify-only, not re-fetched.
- vault/knowledge/subscription-economics-2026.md — NPCI UPI Autopay already
  HARD; worked-example anchors (₹30,000 in-hand / $4,000 take-home).

## Searches/fetches run
1. WebSearch: India salaried month-end broke surveys → only blog prose + one
   YouGov report lead.
2. WebSearch: US paycheck-to-paycheck primary sources → BofA Institute +
   PYMNTS identified as the two primaries; CareerBuilder 78% confirmed zombie.
3. WebSearch: BLS median usual weekly earnings Q2 2026 → $1,251 (release text
   in results + FRED series).
4. WebSearch: HYSA rates Jul 2026 → Marcus 3.40 / Ally 3.00 / top ~4.00–4.15 /
   natl avg 0.38.
5. WebFetch bls.gov release → **403, not retried** (contract). Figure kept via
   release text quoted in search + FRED as second source.
6. WebFetch BofA Institute paycheck-to-paycheck → ~25% of households, Nov 2025,
   internal data.
7. WebSearch: Clason provenance → 1926, multiple concurring book sources.
8. WebSearch + WebFetch YouGov India 2026 report page → 34% keeping up / 19%
   falling behind (summary page only, full report gated) — SOFT.
9. WebSearch: India standing-instruction terminology → HDFC "Standing
   Instruction" product page; SBI auto debit. Terminology only.
10. WebSearch: India emergency-savings surveys → Stable Money (fintech PR,
    SOFT) + Business Standard survey piece.
11. WebFetch business-standard.com survey article → **403, not retried**.
    Headline figures staged as SOFT with conductor-unverified caveat.

## Outcome
- Staged 6 India rows (2 HARD verify-only, 3 SOFT, terminology block) and
  6 US rows (4 HARD, 1 HARD-leaning, 1 SOFT) + provenance + rejected list.
- Key finding: **no HARD "% of Indians who save first" stat exists** — RBI 7.0%
  net financial savings is the honest anchor; staged the plausibility flag on
  the ₹12,000 hero number vs PLFS ₹24,217 average.
- US paycheck-to-paycheck conflict (25% BofA vs 66% PYMNTS) recorded BOTH per
  contract.

## Untrusted input
No instruction-like content encountered in any fetched page. Nothing followed
from page content beyond data extraction.
