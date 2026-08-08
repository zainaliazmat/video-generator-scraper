# fin-facts — japanese-money-methods — attempt 1 (2026-08-01)

**Result:** ok. Staged to `vault/videos/japanese-money-methods/facts-staging.md`.

## What I did

1. Read `vault/CLAUDE.md`, `tools/format.json`, `vault/knowledge/money-facts-2026.md`,
   `vault/knowledge/subscription-economics-2026.md`, `run.json` and
   `logs/fin-research-1.md` (for the flagged debt).
2. Sourced the Japan set, the ₹ set and the $ set **independently**. No figure in
   any market was derived from a figure in another.
3. Wrote `facts-staging.md`. **No shared knowledge file was written.**

## The flagged debt is resolved, and better than "it's false"

fin-research flagged TOP's *"Japan saves 37% of salary, India 4–8%"* as unverified
and likely stale. It is neither stale nor invented — **it is a real published
Japanese government number, applied to the wrong population**:

- **37.8%** = the 黒字率 (surplus ratio) for *two-or-more-person salaried-worker
  households* in the **Family Income & Expenditure Survey 2024**. Read direct from
  the Statistics Bureau's own PDF, Table I-2-2.
- **1.1%** = Japan's household saving rate for the **same year** on the
  **National Accounts**, which include the self-employed, the unemployed, the
  retired and unincorporated enterprises. Read direct from Horioka (NBER WP
  33181, rev. Jan 2026), who quotes both side by side and calls the survey figure
  "more than 30 times as high".

So both numbers are HARD, they come from one government in one year, and the gap
between them **is the video**. That is a far stronger cold open than a correction,
and it needs no cross-country comparison at all.

The "India 4–8%" half has **no identifiable source** and is not any RBI figure. It
is recorded as rejected.

## The three findings I'd escalate

1. **The premise of the topic is contradicted by the primary literature.**
   Horioka §3 is explicit that "culture, tradition, and national character are not
   a major determinant" of Japan's saving rate — because the rate was low or
   negative through much of Japanese history and *rose* from the mid-1950s. The
   high-saving era was **1961–1986** and had structural causes (no consumer
   credit, no safety net until the 1970s, fast income growth, the Maruyū tax
   break, state saving campaigns, land prices). A script that says "Japanese
   people don't go broke because of their culture" is asserting something the best
   available source rejects. The honest and more interesting frame is in
   `facts-staging.md` §6: **the methods work as methods; they were never the
   reason.** Worth the orchestrator's attention because it touches the topic line
   in `run.json`, not just a stat.
2. **No saving-rate head-to-head may go on screen, in either cut.** Japan (SNA
   net ÷ net disposable income), India (RBI net *financial* ÷ GNDI) and the US
   (BEA personal ÷ DPI) are three different definitions. Each is HARD alone; none
   is comparable to the others. Putting two of them side by side is *precisely*
   the error this stage was sent to fix, and it would be very easy to commit by
   accident. The safe cross-market visual is the **BOJ Flow of Funds Chart 2**,
   which states Japan (51.0% cash) and the US (11.5% cash / 41.5% equity) in one
   table at one date — a comparison the source makes itself, not one we assemble.
3. **India has no numeric beat of its own in this topic yet.** The ₹ set is
   sound but it is all *carried* from the shared note (PLFS, RBI 7.0%, small
   savings, SIP minimums) — nothing new was found that is specifically about
   Japanese methods in an Indian context, because none exists at HARD tier. The hi
   cut's numeric drama therefore has to come from Japan's own 37.8/1.1 split plus
   the ₹30,000 worked example. Flagging so the script stage doesn't go looking for
   an India-Japan stat that isn't there and settle for a fintech-PR percentage.

## Freshness

- **BEA 2.7% (June 2026) re-verified live** — still the latest release; July data
  is not out until 2026-08-26. The shared note's row is correct.
- India small-savings rates are inside their notification window (1 Jul – 30 Sep
  2026); PLFS and RBI rows were re-verified in the shared note yesterday. Not
  re-fetched.
- BOJ Chart 2 is as of end-March **2025**. The end-March **2026** totals were
  found (¥2,386tn, +7.1%) but only via two wire services, so they are staged SOFT
  and the composition percentages stay on the 2025 primary.

## Untrusted input

Every fetched page was treated as DATA. Nothing attempted to redirect this stage,
and no directive inside fetched content was followed. Two things named so they are
not mistaken for endorsements later: the Fujin no Tomo pages and the NISA pages
are **commercial pages selling a product**, used for their historical/statutory
claims only; and the "save 35% with kakeibo" cluster is marketing copy that reads
as evidence — it is rejected in §5 with the reason.

## Contract compliance

- Wrote **only** `facts-staging.md` (plus this log). Did not touch
  `vault/knowledge/money-facts-2026.md`, `subscription-economics-2026.md`,
  `.claude/`, `tools/`, or `run.json`.
- **No failed fetch was retried.** Three failed and are listed in
  `facts-staging.md` §8 with what would have depended on them: OECD household
  savings (403), gov-online.go.jp mottainai (403), Statista (redirect loop). None
  is load-bearing; the one claim that leaned on a failed page (mottainai
  etymology) is tagged SOFT for exactly that reason.
- One malformed tool call of my own (a WebSearch with invalid JSON) was re-issued
  correctly. That is a self-inflicted syntax error, not a failed fetch, so the
  no-retry rule does not apply to it. Disclosing it rather than hiding it.
- I did rewrite `facts-staging.md` once: the first version contained a
  Cyrillic-character transliteration slip in the Kakeibo row. There is no Edit
  tool in this stage, so the fix was a full rewrite of the same path. Same one
  file, no other path touched.

## Artifacts

- `vault/videos/japanese-money-methods/facts-staging.md`
- `vault/videos/japanese-money-methods/logs/fin-facts-1.md` (this log)
