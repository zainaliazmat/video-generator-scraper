---
summary: Stage log — fin-audit, pay-yourself-first, cut=en, attempt=1. PASS after 3 edits; all load-bearing numbers independently re-fetched and confirmed.
updated: 2026-07-28
source: fin-audit run 2026-07-28
---

# fin-audit — en — attempt 1

- Inputs: slug=pay-yourself-first, cut=en, tier=short (165s), attempt=1.
- Constants: tools/format.json — 15.0 c/s ⇒ budget 2,475 ±10%; layout lints
  (one focal, cue gap 0.8s, cascade ≤5, ≤3 chips/row, ≤22 chars/chip).
- Re-fetch trail: BLS Q2 2026 release text ($1,251, 120.9M, +4.6% vs CPI +3.9%)
  via search after direct 403; Fed press release other20260513a.htm (SHED 2025,
  63% / $400); bea.gov (3.0% May 2026); institute.bankofamerica.com ("nearly a
  quarter", Nov 2025); fdic.gov national rates (0.38% savings, Jul 20 2026) +
  July 2026 HYSA roundups (~3.8–4.2%) for the 10× claim; Wikipedia (Babylon
  1926) + jamesclear.com (quote, 1/10th). Failed fetches: FRED series page 403,
  federalreserve.gov SHED landing URL 404 (correct press-release URL found),
  marcus.com 403, bankrate.com 405 — all routed to official alternates.
- Violations found & fixed by edit: (1) hook payoff at ~16.1s > 15s → en1 VO
  trimmed 24 chars, payoff now ~14.5s; (2) en5 context chip 30 chars → 20;
  (3) en8 chip 25 chars → 16, "even 5%" moved to sub.
- Verdict: PASS → vault/videos/pay-yourself-first/audit-en.md. Script edited —
  downstream voice/build must re-run against the edited script (hash check).
- Untrusted input: no fetched page contained instruction-like content; all
  fetched text treated as data.
