---
summary: fin-audit log, cut en, attempt 1 — PASS with three edits to script-en.md. Six sources re-fetched independently of facts-staging; two claims killed on presentation, one authority appeal deleted.
updated: 2026-07-31
stage: fin-audit, cut en, attempt 1
---

# fin-audit — first-lakh-first-thousand, cut en, attempt 1

**Verdict: PASS.** Report: `vault/videos/first-lakh-first-thousand/audit-en.md`.

## Inputs read

- `vault/CLAUDE.md` (session protocol, two-home rule)
- `tools/format.json` (en rate 16.1 chars/s, layout lints, tier constants)
- `vault/videos/first-lakh-first-thousand/run.json` (tier medium, 510s, swiss-band)
- `vault/videos/first-lakh-first-thousand/script-en.md` (the artifact under audit)
- `vault/videos/first-lakh-first-thousand/facts-staging.md` (§2 USA block — read as a
  *map of URLs to re-fetch*, never as evidence)
- `vault/videos/first-lakh-first-thousand/audit-hi.md` (what the sibling cut's gate caught)

## Re-fetches performed (independence rule)

| Source | Method | Result |
|---|---|---|
| bea.gov personal-income-and-outlays-june-2026 | direct | 2.7%, $646.1bn, rel. 30 Jul 2026 — confirms |
| fdic.gov/national-rates-and-rate-caps | direct | 0.38% savings / 0.65% MMDA / 4.38% cap, as of 20 Jul 2026 — confirms |
| federalreserve.gov/monetarypolicy/openmarket.htm | direct | last change 11 Dec 2025 → 3.50–3.75% — confirms |
| fred.stlouisfed.org LES1252881600Q | direct | **403** — fell back to BLS-owned surfaces |
| bls.gov/news.release/wkyeng.nr0.htm | direct | **403** — figure confirmed via BLS's own release index + BLS_gov post: $1,251, Q2 2026 |
| federalreserve.gov SHED (+ 2025 report coverage) | direct + index | 63% could cover $400 using cash **or its equivalent** — figure confirms, script wording did not |
| officialdata.org/us/stocks/s-p-500 | direct | 10.69% nominal / 6.81% real since 1957 — confirms the *shape* claim only |
| Munger primary | — | none reachable, as staging said. Kept SOFT, kept as colour |

Every COMPUTED figure (12.5/12, 12.5/11, 12.5/6, ~$96,000, $108/mo, 7.7yr, 5.7yr, ½ vs 6½)
was re-derived from an ordinary monthly annuity rather than trusted from §2.3. All reproduce.

## Edits made to script-en.md (downstream must re-run)

1. **6.3 VO + stmt + foot** — "with cash" → "with cash or its equivalent"; dropped
   "say they". The SHED 37% belongs to a cash-*or-equivalent* test. VO-bearing → hash break.
2. **5.8 stmt** — removed the quotation marks around a Munger paraphrase with no reachable
   primary; foot now says PARAPHRASE explicitly. Screen-only, no TTS cost.
3. **8.10 foot** — deleted "The sequence practitioners describe" (unsourced authority
   appeal). Screen-only.
4. Housekeeping: char cells for 6.3's +9 chars (total 7,648 → 7,657, −6.7% of the 8,211
   budget); corrected the script's own false claim that the word "I" appears nowhere.

## Checks: result

| # | Check | Result |
|---|---|---|
| 1 | Numbers trace to staging AND survive re-fetch | pass after edit #1 |
| 2 | Char total within ±10% of 510 × 16.1 = 8,211 | pass — 7,657, −6.7% |
| 3 | Hook payoff inside 15s | pass — ~11.2s |
| 4 | No product/platform recommended | pass — none named; 2.4 already uses the non-imperative "suppose" form |
| 5 | Currency purity (no ₹ in -en) | pass — zero U+20B9 in the file |
| 6 | No cite refs, no bare Latin digits in VO | pass — 0 digits across 92 VO strings |
| 7 | Persona rules | pass |
| 8 | Layout lints from format.json | pass — 92 cue blocks, 0 dual-focal scenes, no chip rows, tightest cue spacing 5.3 at 1.4s/2 cues fits |

## Note for the next run

Two of the three kills were **presentation**, not arithmetic: a real number bound to the
wrong test, and a real paraphrase dressed as a verbatim quote. The hi cut's kills were an
unsourced integer and a product imperative. fin-script has stopped making the hi cut's
mistakes — worth adding "quotation marks on screen require a reachable primary" and "a
figure's sentence must match the source's test, not just its value" to fin-script.md's
rules, so gate one stops finding them by hand.
