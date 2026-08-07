---
summary: Process log for fin-audit, passive-income-number cut hi attempt 1. Result PASS with five in-place edits. Records what was re-fetched, what the fetches returned, what was found, and the two judgement calls that could have gone the other way.
updated: 2026-08-07
source: script-hi.md, facts-staging.md, knowledge/video-studies/passive-income-number.md, run.json, tools/format.json. Live re-fetches performed by this stage 2026-08-07.
stage: fin-audit, cut hi, attempt 1
---

# fin-audit-hi-1 — process log

**Result: PASS with edits.** Findings and evidence live in `../audit-hi.md`; this file
records method, fetch outcomes and judgement calls.

## Order of work

1. `run.json` constraints block → `vault/CLAUDE.md` → `tools/format.json` constants.
2. `script-hi.md`, `facts-staging.md`, the study note, `knowledge/money-facts-2026.md`.
3. **Re-fetched every load-bearing source before grading any claim** — the independence
   rule. Staging was treated as a list of URLs to check, not as evidence.
4. Mechanical lints by grep (currency, banned word, Latin digits in VO, persona, ages).
5. Re-derived all rung arithmetic and both SIP figures by hand.
6. Five edits, then reconciled the char/timing tables to match.

## Re-fetch outcomes

| Source | Outcome |
|---|---|
| Business Today, RBI MPC 2026-08-05 | **read direct** — 5.0% FY27, quarterly split, repo 5.25%, all exact. The highest-risk row in the file; genuine |
| Upstox POMIS | **read direct** — 7.4%, ₹9 lakh / ₹15 lakh, monthly |
| freefincal SWR bands | **read direct** — 3.5% / 4.5% thresholds confirmed; **no backtest disclosed** → drove D4 |
| AAII Journal Feb 1998 (Trinity) | **read direct, full PDF, all tables** — the verbatim tax/costs bullet and the payout-period range confirmed at source |
| Bengen 1994 via PortfolioConstruction | PDF retrieved, **not text-extractable** this run; origin corroborated on the other staged surfaces. Contents still unread → drove D3 |
| SSRN 4697720 (Raju & Saraogi) | **403'd to me, same as fin-facts.** Recovered title/authors/date/3.0–3.5%/2.6%/3.75% via search index |
| PIB PLFS Annual Report 2025 | ₹24,217 / ₹18,353 confirmed, with the 2024 → 2025 rise |

Two sources that facts-staging marked "read direct" were re-read and matched exactly; one
("practitioner backtest") did **not** match its description, which is the whole reason the
independence rule exists.

## Judgement calls worth recording

**1. The char budget — accepted the corrected formula, rejected the naive one.**
`13.03 × 510 = 6,645` puts the script at −11.9%, i.e. an automatic FAIL on the ±10% gate.
Accepted fin-script's `(510 − 62.4) × 13.03 = 5,832` instead, because `format.json`
documents 13.03 as chars per second **of audio** and charges 0.8 s/line of non-audio
padding, and `cuts.en._chars_per_second_trap` explicitly instructs "Fix the budget formula
FIRST". Failing this script for length would have forced ~800 characters of padding into a
correctly-budgeted cut. **This is the single most likely way a future attempt gets this
wrong**; it is written into `audit-hi.md` §3 so a later stage cannot re-break it.

**2. Fix vs FAIL on D1/D2.** Both were genuine breaches of a binding constraint and of the
script's own build assert. Chose to edit rather than bounce: each was a one-token
correction that touched no argument, and a FAIL here spends an attempt against the ×2 stop
without improving the script. The authority to edit exists precisely for this shape of
defect. Had the rungs themselves been bare — the Dark Ledger pattern — that would have been
a FAIL, because it would mean the ladder was built wrong.

**3. 6.15/6.16's 20-year horizon is not an age conversion.** Considered and rejected as a
violation: the horizon is an input to a cost-per-month calculation (framed by 6.14 as "what
it costs per month"), not an achievement date. PART D permits this form by name and forbids
"you'll be free by 2046", which does not appear. A viewer can chain the numbers themselves;
the script never does it for them, and 6.11 refuses on the record.

**4. Did not touch** the 2.6/2.7 hold-ceiling breach (a build fix, already prescribed and
caught by `check_build`), the fact-trace's mis-filing of 6.13 under the 3.0% row (harmless
— the line does carry a rate), or the chapter start estimates beyond the two that moved
(the build recomputes all timing from ffprobe by construction).

## Edits made (5)

VO rewritten: **5.9**, **5.14**, **7.6**. On-screen text rewritten: **5.9** stmt, **5.15**
foot, **7.6** stmt. Non-VO: the role-colour legend rebuilt from the cues; char/timing tables
and frontmatter reconciled (5,851 → 5,876; 511.4 s → 513.4 s).

**Three VO strings changed → the TTS input changed.** Voice work must re-run against the
edited file, and the extraction must be keyed (`1.1 … 7.8`), never a `^> ` grep — the file's
guard blockquotes are also `>`-quoted and would add ~33 junk lines to an 78-line job.

## Untrusted input handling

All fetched pages were treated as DATA. No fetched page altered a command, a path or a
decision; no page contained an instruction directed at this stage. Recording the negative,
per the convention in the study note.

## Owed / carried

- A primary read of SSRN 4697720 before 3.0% is promoted to `money-facts-2026.md`.
- The 1994 Bengen paper's contents remain unread — D3 scoped the VO around this rather than
  asserting it. If a later run retrieves it, 5.14 can be tightened back.
- Nothing in this audit unblocks the `run.json.owed` items (study packet, vidIQ pass).
