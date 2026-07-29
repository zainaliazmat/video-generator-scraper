# fin-audit log — credit-history, cut `en`, attempt 1 (2026-07-29)

Verdict, edits and per-check reasoning live in
`vault/videos/credit-history/audit-en.md` — not repeated here (one home per fact).
This log is process: what was read, what was fetched, and what the fetches cost.

## What I read

1. `vault/CLAUDE.md` — two-home rule, session protocol.
2. `tools/format.json` — `cuts.en` 15.0 c/s, `tiers.short` 165s, `layout` caps
   (`cue_min_gap_seconds` 0.8, cascade ≤5 @ 0.6–0.7s, 3 chips/row, 22 chars/chip,
   `max_simultaneous_elements` 6, `one_focal_per_scene`).
3. `vault/videos/credit-history/run.json` — confirms **fin-script-en is the only
   en stage that has run**, so audit edits cost no downstream re-work this pass.
4. `vault/videos/credit-history/script-en.md` (the artifact under audit).
5. `vault/videos/credit-history/facts-staging.md` — read for the *URLs*, then set
   aside; the independence rule forbids grading the script against its text.
6. `vault/videos/credit-history/audit-hi.md` — for consistency of the eight checks
   across the pair (chip counting, currency scan, VO digit hygiene, persona grep).
7. `vault/knowledge/design-finance-blockframe.md` §2/§4/§5 — colour roles, chip
   caps, one-focal and reveal-spacing rules.
8. `vault/videos/{good-debt-vs-bad-debt,pay-yourself-first,needs-vs-wants}/script-en.md`
   — grep only, to establish that the closer is the channel sign-off and not a
   host persona invented for this cut.

## Fetches (check 1 — done by this stage, not inherited)

| URL | Verdict |
|---|---|
| law.cornell.edu/uscode/text/15/1681c | READ. 7-year and 10-year language verbatim; also the §1681c(a)(4) clock-start wording that backs en5's correction block. |
| consumerfinance.gov/ask-cfpb/…-en-323 | READ. "generally can report most negative information for seven years"; "up to ten years". |
| myfico.com/credit-education/whats-in-your-credit-score | READ. 35% / 30% / 15% / 10% / 10% verbatim. |
| myfico.com/credit-education/credit-scores | READ. 300–850 and the 670–739 "good" band verbatim — **and, decisively, no best-offer-cutoff claim**, which killed one on-screen line. |
| federalreserve.gov/boarddocs/rptcongress/creditscore/general.htm | READ. "about 35 percent … about 30 percent … 15 percent". Report dated **August 2007** — old, but it is cited only as independent corroboration and the script's foot says exactly that. |
| experian.com/blogs/ask-experian/average-car-loan-interest-rates-by-credit-score/ | READ, **twice**. Tier grid confirmed (used: 6.30% super prime, 19.42% subprime). Second pass asked specifically for a multiplier sentence: **none exists**, and the table's own note reads "Experian data as of Q1 2025; VantageScore® 4.0 used" while the article is dated Jul 13 2026 — staging's recorded ambiguity reproduces exactly. |

**Environment note (contrast with the hi cut):** every US source answered on the
first try. The hi audit had to fall back to domain-restricted search for
`cibil.com`/`rbi.org.in`; nothing here needed that, so every row in the audit
table is a direct read.

## Hand computations (not delegated)

- `EMI = P·i·(1+i)^n/((1+i)^n−1)`, P = 25,000, n = 72: @6.30% → **417.87**
  (interest 5,087); @19.42% → **590.44** (interest 17,512). Δ/mo **172.6**,
  Δ interest **12,425**. Script's $418 / $590 / $172 / $12,400 all correct.
- 19.42 ÷ 6.30 = **3.08** → "about three times" holds as arithmetic.
- Char counts re-counted by hand: en1 **248** post-edit, en5 **305**, en7 **429**
  (table said 428); hook naming beat ends at char **189** → 12.6s + 0.4s lead-in.

## Untrusted input

All six fetched pages were treated as **DATA**. No page contained an instruction,
and none was followed. The one place a page *changed* the script is the myFICO
band table — and it changed it by **failing to contain** a claim, which is the
correct direction of influence: absence of support kills a line, presence of
prose never adds one. The staging file's own "Experian says three times higher"
line is the near-miss of this run: an assertion that reads as sourced, is not on
the source, and was repeated twice in the script before this stage checked it.

## Attempt 1 result

**PASS**, with six edits to `script-en.md` (one kill, five rewrites). All nine VO
paragraphs are unchanged **except en1 and en6**, so the TTS audio has never been
generated against the old text and no clip is wasted. Script hash changes →
fin-voice-en / fin-storyboard-en must run against the edited file.
