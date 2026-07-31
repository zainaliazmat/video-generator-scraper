---
summary: fin-audit run log — first-lakh-first-thousand, cut hi, attempt 1. PASS after three direct edits to script-hi.md. Verdict and evidence live in audit-hi.md; this is the trace of what was fetched and in what order.
updated: 2026-07-31
source: this run
stage: fin-audit, cut hi, attempt 1
---

# fin-audit — hi, attempt 1

**Result: PASS, script edited.** Verdict + reasoning: `vault/videos/first-lakh-first-thousand/audit-hi.md`.

## Order of work

1. Read `vault/CLAUDE.md`, `tools/format.json`, `run.json`, `facts-staging.md`,
   `script-hi.md`. Noted the cut is MEDIUM/`swiss-band` per creator pick, so the
   `lines: 9` constant on the swiss-band registry entry does not apply and the
   86-line count is not a violation.
2. Mechanical lints first (cheap, and they decide whether fetching is even worth it):
   grep for `$` → none; grep for Latin digits / `₹` inside VO lines → none;
   grep for `मैं|मेरा|मेरी|मैंने` → none in VO; grep for `(\d+:\d+)` cite refs → none;
   grep for brand names (SBI/HDFC/ICICI/Axis/Kotak/Groww/Zerodha/Paytm) → none on screen.
3. Re-summed the per-scene char table by hand (5,890) against the chapter table
   (~5,958) and the budget (6,375). Both inside ±10%. Recounted 1.1 by character to
   confirm the estimator isn't optimistic: 48 actual vs 47 claimed.
4. **Independence rule — re-fetched every load-bearing source, ignoring the staging
   text as evidence.** Results in audit-hi.md's table. Notes on reachability:
   - businesstoday.in (staging's primary for the rate block): `ECONNRESET`, twice.
     Substituted upstox.com article-196126, which quotes the Finance Ministry release
     verbatim — this is what caught the quarters error, since Business Today was never
     re-read and staging's own hedge was the only signal.
   - business-standard.com "10th-consecutive-quarter" URL: `ECONNRESET`. So the *only*
     source for "ten" remained unread on a re-fetch, while an independent source said
     "ninth" in the Finance Ministry's own words. Resolved downward.
   - pib.gov.in PRID 2246009: HTTP 403 to direct fetch (same as the -en run's BLS
     experience). PLFS figures confirmed through the search index, matched on all four
     numbers including the 2024 base year, so the row survives at HARD.
   - NSE factsheet/whitepaper PDFs: still 403, exactly as staging recorded. The row
     stays SOFT and the script's shape-only handling is what makes it shippable.
5. Re-derived facts-staging §1.3 arithmetically (ordinary monthly annuity, ₹5,000/mo)
   because the whole video hangs on "2 months vs 13 months". First pass looked like a
   systematic off-by-one and nearly became the FAIL; second pass showed the staged
   table is internally consistent under **round-to-nearest**, which is a legitimate
   illustrative convention. Downgraded from a kill to a pinned build warning. Recorded
   here because the next auditor will re-derive it and reach the same false alarm.
6. Made three edits, wrote `audit-hi.md`, wrote this log.

## Edits made to script-hi.md

| Where | Change |
|---|---|
| VO 2.4 | "रख दीजिए" → "मान लीजिए … पड़ा है" — removes an imperative to put money into PPF / post office |
| VO 4.10 + its cue | "दस तिमाही" → "नौ तिमाही"; "unchanged for 10 straight quarters" → "nine straight quarters" |
| swiss-band spec, colour semantics | `--fund` redefined from "returns doing the work" to "the mechanism that works without you once it exists", with the eight scenes that prove it listed |
| Fact-trace row (quarters) | Rewritten to record the re-fetch and the downward correction |
| Build handoff §4 | Added the round-to-nearest pin |

## Consequence

Three of the five touch VO or the fact trace, so the script hash changes. fin-voice
must run against the edited file; nothing has been sent to ElevenLabs yet, so the
correction is free at this point — which is the entire reason this gate sits here.

## For the -en cut's audit

- facts-staging §2.3 uses the same round-to-nearest convention ($800/mo: the first
  $10,000 is $9,799 at month 12 under 4.15%, and the tenth $10k lands at $99,400 at
  month 6 under 10%). Expect the identical false alarm; it is not a defect.
- §2's Munger row is SOFT with no primary reachable. The staging note's own guidance —
  paraphrase, no year, no venue, and lean on the $96,000 crossover arithmetic instead —
  is the only safe shape. Re-fetch it anyway; a quote with seven secondary sources and
  zero primaries is exactly the shape an injected claim takes.
- The BEA 2.7% June-2026 saving rate is the -en cut's load-bearing HARD row and
  supersedes the 3.0% May figure still sitting in `knowledge/money-facts-2026.md`.
