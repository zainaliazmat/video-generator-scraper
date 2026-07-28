---
summary: fin-audit gate-one verdict for pay-yourself-first hi cut, attempt 1. All 8 checks pass after 2 audit edits (PLFS gender qualifier on s7 foot, chip row-breaks in s2/s9).
updated: 2026-07-28
source: fin-audit attempt 1 — independent re-fetch of PLFS/RBI/Clason/HDFC sources
---

# Audit — pay-yourself-first / hi / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

| Claim in script | Re-fetch result |
|---|---|
| PLFS 2025 avg salaried earnings ₹24,217 | CONFIRMED — PIB release PRID 2246009 (PLFS Annual Report 2025, Jan–Dec 2025): men ₹22,891→₹24,217, women ₹17,126→₹18,353. Note: ₹24,217 is the MEN's figure → edit below. |
| RBI net household financial savings 7.0% of GNDI FY25 | CONFIRMED — RBI Annual Report via business-standard.com (126052901658, May 2026): 7.0% FY25 up from 5.8%; gross 11.8%, liabilities 4.8%. Script's ₹100→₹7 framing carries the precise "net household financial savings, 7% of GNDI" foot on screen, per the staging blessing. Nuance logged: excludes physical savings (gold/property) — foot qualifier is what keeps it honest. |
| Richest Man in Babylon, Clason, 1926, "a part of all you earn is yours to keep", 10% | CONFIRMED — Wikipedia + multiple 1926-edition listings for the year; jamesclear.com summary carries the quote and the 1/10th fraction. Automation twist correctly NOT attributed to Clason. |
| Standing Instruction / UPI Autopay terminology | CONFIRMED — recorded HDFC page fetched live, title "Standing Instruction Facility on Debit Cards | HDFC Bank". Terminology only, no money claim. |
| ₹12,000 × 12 = ₹1,44,000 | Arithmetic ✓; en-IN grouping ₹1,44,000 ✓ (and ₹14,400 for the ladder ✓). |
| 5% of ₹24,000 = ₹1,200/mo = ₹14,400/yr | Arithmetic ✓, anchored to the verified PLFS row. |

Plausibility flag honored: ₹12,000/mo is framed as the ₹60–70k in-hand
higher-earner example; the ladder (₹1,200/mo) is the ask. No SOFT row used on
screen. No fabricated "X% save first" stat present.

## Other checks

2. Char budget: budget 165s × 12.5 = 2,062 ±10% (1,856–2,269). Script's own
   table ~2,060; independent word-count estimate ~2,150. Inside band. Build
   stage ffprobe-measures before locking (script already mandates this).
3. Hook payoff: question at 0s, answer ("क्योंकि आप बचत सबसे आख़िर में करते हैं")
   lands ~6s in. Pass.
4. No product/platform recommended — no bank/fund/app named in script; book is
   provenance, SI/UPI Autopay are generic feature names. Pass.
5. Currency purity: zero `$` anywhere in script-hi.md. Pass.
6. VO text: zero Latin digits, zero cite-refs — all figures spelled out in
   Devanagari. Pass.
7. Persona: no host, no first person, no investment picks (emergency fund →
   goals only). Pass.
8. Layout lints: one focal per scene ✓ (s7 counter declared focal, 5 elements
   ≤ 6); s5 stagger is a 3-item cascade ✓; all chips ≤22 chars (max 21) ✓;
   colour usage (warn=problem, positive=solution) supports the thesis ✓.
   VIOLATION found: s2 and s9 each listed 4 chips with no row break vs
   `max_chips_per_row: 3` → fixed by edit.

## Edits made (script-hi.md — downstream must re-run against edited script)

1. s7 foot: `avg salaried earnings ≈ ₹24,217/mo` → `avg salaried earnings (men)
   ₹24,217/mo · (women) ₹18,353`. Why: ₹24,217 is PLFS's MEN's average;
   presenting it unqualified as "the average salary" misstates the source.
2. s2 chips: declared 2×2 rows (was 4 chips, no row break — lint violation).
3. s9 recap chips: declared 2×2 rows (same violation).

Nothing killed — every number traced and survived.
