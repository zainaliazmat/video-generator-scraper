---
summary: fin-audit gate-one verdict for pay-yourself-first en cut, attempt 1. All 8 checks pass after 3 audit edits (hook trim to land payoff <15s, two over-length chips shortened). Every number survived independent source re-fetch.
updated: 2026-07-28
source: fin-audit attempt 1 — independent re-fetch of BLS/Fed SHED/BEA/BofA/FDIC/Clason sources
---

# Audit — pay-yourself-first / en / attempt 1

PASS

## Independence re-fetch (check 1) — every load-bearing number

| Claim in script | Re-fetch result |
|---|---|
| Median full-time weekly pay $1,251 (en5) | CONFIRMED — the recorded bls.gov release and FRED page both 403 direct fetch, but the BLS Q2 2026 release text surfaced verbatim via search: "$1,251 in the second quarter of 2026… 120.9 million full-time wage and salary workers… 4.6 percent higher… CPI-U 3.9 percent" — exact match on all corroborating details, independent of facts-staging. |
| ~4 in 10 adults can't cover a $400 emergency (en7 echo) | CONFIRMED — Fed press release other20260513a.htm: SHED *Economic Well-Being of U.S. Households in 2025* (rel. May 13, 2026, fielded Oct 2025): 63% would cover $400 with cash or equivalent, unchanged from 2024 ⇒ ~4 in 10 could not. |
| 3¢ of every $1 / personal saving rate 3.0% (en5) | CONFIRMED — bea.gov personal-saving-rate page live: 3.0%, May 2026. |
| 1 in 4 US households nothing left (en1) | CONFIRMED — institute.bankofamerica.com paycheck-to-paycheck (Nov 2025): "in 2025 nearly a quarter of all households are estimated to live paycheck to paycheck." Conservative floor used alone per staging conflict note; PYMNTS 66% correctly kept off screen. |
| HYSA ≈ 10× typical savings, no APY shown (en6) | CONFIRMED as order-of-magnitude — FDIC national rates page live: savings national avg 0.38% (Jul 20, 2026, official); July 2026 top HYSA cards ~3.8–4.2% ⇒ ~10×. Marcus/Bankrate 403/405'd but FDIC (official) + market roundups suffice. No APY on screen ✓ (standing ban). |
| Babylon 1926, Clason, "a part of all you earn is yours to keep", start at 10% (en4) | CONFIRMED — Wikipedia: "a 1926 book by George S. Clason"; jamesclear.com summary carries the quote and the 1/10th rule. Automation twist correctly NOT attributed to Clason. |
| $4,000/mo → $400/mo → $4,800/yr; 5% ladder $200/mo = $2,400/yr | Arithmetic ✓; en-US grouping $4,800 ✓; $400 echo vs SHED $400 is the verified deliberate device. |

The BLS row was the trap-shaped one — staging admits its direct fetch 403'd and
the figure was "quoted from the release text." Independent corroboration
(worker count, YoY %, CPI %) matched exactly, so it stands.

## Other checks

2. Char budget: 165s × 15.0 = 2,475 ±10% (2,228–2,723). Pre-edit ~2,557 (+3%),
   post-edit ~2,533 (+2.3%). Inside band.
3. Hook payoff: VIOLATION found — the promise line ("Today: the hundred-year-old
   rule…") started after ~241 chars ≈ 16.1s. Fixed by trimming en1 (edit 1);
   now ~217 chars ≈ 14.5s. Pass after edit.
4. No product/platform recommended — HYSA/FDIC/ACH generic; DoorDash named only
   as a spending-temptation example, Marcus/Ally never appear in the script. Pass.
5. Currency purity: zero `₹` anywhere in script-en.md (only the meta-note stating
   none appears). Not translation-shaped: DoorDash/BLS/FDIC/HYSA framing is
   natively US, hero math is the US worked example, register per
   us-english-script-style. Pass.
6. VO text: zero bare Latin digits (all figures spelled out: "twelve hundred
   fifty dollars", "nineteen twenty-six"), zero cite-refs. Pass.
7. Persona: no host, no first-person expertise ("as a country, we save" is
   collective, not expert-voice), no investment picks — emergency fund → goals
   only. Pass.
8. Layout lints: one focal per scene ✓ (en1 huge, en3 equation flip, en7 counter
   declared focal; ≤6 elements each); en5 stagger is a 3-item cascade ✓; chips
   ≤3/row ✓ (en2/en9 declared 2×2). VIOLATIONS found: en5 context chip 30 chars,
   en8 third chip 25 chars vs max 22 → fixed by edits 2–3. Colour semantics
   (warn=drain, positive=flipped formula/saved) support the thesis ✓. No
   storyboard-en yet — colour-table check re-runs at storyboard stage.

## Edits made (script-en.md — downstream must re-run against edited script)

1. en1 VO: cut "at the end of the month " (−24 chars) so the payoff promise
   lands ≈14.5s, inside the 15s line. Timing table updated (~2,533 / ~2:49).
2. en5 context chip: `Median full-time pay $1,251/wk` (30) → `Median pay
   $1,251/wk` (20).
3. en8 chip 3: `DAY AFTER PAYDAY, EVEN 5%` (25) → `DAY AFTER PAYDAY` (16);
   "even 5%" moved into the sub (VO already carries it, en9 chip `START AT 5%`
   keeps it on screen at recap).

Nothing killed — every number traced and survived re-fetch. The script's own
discipline held: the brief's 22% APR shock was correctly dropped for lack of a
staging row ("brutal interest", no number).
