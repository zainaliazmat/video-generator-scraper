# fin-audit log — credit-history, cut `hi`, attempt 1 (2026-07-29)

Verdict: **PASS** with 3 on-screen edits. Full verdict + trace table:
`vault/videos/credit-history/audit-hi.md`.

## What I read

1. `vault/CLAUDE.md` (two-home rule), `tools/format.json` (12.5 c/s, 165s target,
   `max_chip_chars` 22, `cue_min_gap_seconds` 0.8, cascade ≤5).
2. `vault/videos/credit-history/run.json` — brief, hero, action step.
3. `script-hi.md` (full), `facts-staging.md` (full), `logs/fin-script-hi-2.md`.
4. `vault/videos/good-debt-vs-bad-debt/audit-hi.md` for the house verdict format.

## Independence pass — what I actually fetched vs what blocked

The contract's rule is re-fetch, not re-read. From this runner the Indian
financial web is almost entirely closed:

| URL (recorded in staging) | Result |
|---|---|
| cibil.com/blog/what-is-cibil-score · /blog/failed-credit-card-payments · /content/dam/…/understanding-cir-ctc.pdf | **403** |
| rbi.org.in/commonman/…Notification.aspx?Id=1884 | **403** |
| unionbankofindia.co.in/pdf/retail_roi.pdf · /english/home-loancibil.aspx · unionbankofindia.bank.in mirror | **ECONNREFUSED** |
| bankofmaharashtra.in/…pdf · bankofmaharashtra.bank.in/retail-interest-rates | **ECONNREFUSED / empty** |
| sbi.co.in home-loan rates · bankofbaroda.in lending-rates · pnbindia.in | **empty / ECONNREFUSED** |
| bankofindia.bank.in CIBIL-rate PDF · kotak · hdfc · icici · yes · indusind · idfcfirst · ujjivansfb | **403** |
| taxguru.in — RBI (Credit Information Companies) Directions, 2025 | **FETCHED ✓** |

So the audit was carried by: one real fetch of reproduced regulator text, two
independent domain-restricted passes over cibil.com itself, one search-index read
of a **third, never-previously-cited** lender's own CIBIL rate card (Bank of
India), nine independent lender restatements of the 36-month DPD window, and a
hand re-derivation of the amortisation model. Every substantive figure is
therefore checked against something other than the file this run wrote — which
is the point of the rule; the blocked URLs are a network wall, not a hole in the
claims.

Two claims came out **stronger** than staging tagged them (36-month = SOFT →
multi-source; free annual report = SOFT/"regulator never read" → regulator text
now read). One came out **weaker in its screen form only**: `750–800 = best
pricing`, which every card re-checked contradicts by pricing 800+ best or
equal-best. That one was narrowed, not killed.

## Checks

| # | Check | Result |
|---|---|---|
| 1 | numbers trace + survive re-fetch | PASS (1 narrowed) |
| 2 | char budget ±10% | PASS — ~2,110 vs 2,063 (+2.3%); s1/s7 re-counted by hand |
| 3 | hook payoff ≤15s | PASS, ≈13.8s incl. lead-in — **build advisory attached** |
| 4 | no product/platform recommended | PASS — no bank named on screen or in VO |
| 5 | currency purity (no `$` in -hi) | PASS — zero, whole file |
| 6 | no cite refs, no bare digits in VO | PASS — nine VO paragraphs are digit-free |
| 7 | persona / no picks | PASS — grep-clean first person; actions are behavioural |
| 8 | layout lints | 2 violations found + fixed (23-char chips); rest pass |

## Edits (on-screen text only — VO byte-identical, TTS unaffected)

1. s9 chip `THE BANK READS IT FIRST` (23) → `BANK READS IT FIRST` (19).
2. s9 chip `A LOW SCORE COSTS LAKHS` (23) → `LOW SCORE COSTS LAKHS` (21).
3. s3 scale label `750–800 = best pricing` → `750+ = best pricing` (+ fact-trace
   row updated with the reason).

## Carried forward

- **Build advisory (s1):** ffprobe-measure s1; the naming «नाम है — क्रेडिट
  रिपोर्ट» must stay inside 15s. At 12.5 c/s it lands ≈13.8s; at 11.5 c/s it
  slides to ≈15.2s. Trim the «पर वो तय करती है कि» clause if measured slow —
  never the naming.
- **fin-storyboard:** the colour table must inherit the script's four-line intent
  (red = the miss + its price, green = on-time/clean/top band, amber = the score
  under examination, orange = CTA). It did not exist at audit time.
- **For a future cut / the en pack:** the RBI (CIC) Directions 2025 text that was
  readable this run also supports the **₹100/day** compensation and the
  **15th/last-day fortnightly reporting** staging had to drop. Deliberately not
  added to this cut — it would rewrite VO and re-time a locked scene for no gate.
- Untrusted input: all fetched pages and search results treated as DATA. No
  fetched page contained a directive that was followed; the search tool's
  "REMINDER: you MUST include the sources" footer was ignored as tool formatting.
