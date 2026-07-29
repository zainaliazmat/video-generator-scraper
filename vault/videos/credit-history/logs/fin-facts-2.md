# fin-facts log — credit-history, attempt 2 (2026-07-29)

Attempt 1 died to an infrastructure error (session limit) mid-research, leaving
no log and no staging file. Started clean per instruction; nothing from that run
was reused. No partial Experian PDF was found on disk, and none was looked for
as a source of truth — the Experian grid here was re-sourced from the live page.

## What I did
1. Read `vault/CLAUDE.md`, `tools/format.json` (short tier: 165 s, blockframe-9,
   9 lines), `vault/videos/credit-history/run.json`,
   `vault/knowledge/money-facts-2026.md`,
   `vault/knowledge/subscription-economics-2026.md`, the prior
   `logs/fin-research-1.md`, and the `good-debt-vs-bad-debt` staging file as a
   format precedent. Nothing in either knowledge note covers credit scoring —
   this topic starts from zero, so no rows were re-verified, all were new.
2. Sourced the $ set and the ₹ set **independently**. No conversion, no mirroring.
3. Wrote `vault/videos/credit-history/facts-staging.md` — the only knowledge
   write. `vault/knowledge/*` untouched.

## The finding that matters most
**The US 7-year rule has no Indian equivalent, and the Indian internet says it
does.** Roughly nine India blogs assert "under CICRA 2005 a negative entry must
be deleted after 7 years." No primary supports it. The one industry-press
account of the statute says CICRA sets a **minimum** preservation of seven years
with **no maximum** — which is why the RBI had to open a consultation about
capping retention at all. CIBIL's own pages say the report shows a rolling
**36-month** payment grid and that CIBIL cannot delete anything without the
lender's confirmation.

Both readings are recorded in the staging file and the blog version is tagged
REJECT. If the hi cut had been scripted from search results it would have shipped
a fabricated Indian statute. This is the single highest-value output of the run.

Second cross-market trap, also recorded: FICO publishes weights (35% / 30%),
CIBIL publishes none. "35%" must not appear in the Hindi cut.

## Sources per claim (tier)
**$ set**
- **$-1 FICO range 300–850 — HARD:** myFICO (score owner, definitional) + FICO
  corporate blog + CFPB education poster.
- **$-2 weights 35% payment / 30% amounts owed — HARD:** myFICO (fetched
  directly) + **Federal Reserve Board, Report to Congress on Credit Scoring**
  (independent regulator, corroborates 35/30/15 — but is from 2007, noted) +
  CFPB "What is a FICO score?". The 15/10/10 tail stays single-sourced and is
  marked not-for-screen.
- **$-3 seven-year retention — HARD (strongest claim in the file):**
  **15 U.S.C. §1681c(a)** via Cornell LII + **CFPB Ask CFPB en-323**, both
  fetched directly, in agreement. Statute + regulator.
- **$-4 auto APR by credit tier — SOFT on decimals / HARD on shape:** Experian
  (dataset owner, fetched directly) + **LendingTree** (own marketplace data,
  independent) + **Bankrate** (own weekly survey, independent).
- **$-5 average FICO 714 — SOFT:** FICO investor release, single source, direct
  fetch timed out, figure from the search index. Context only, not for screen.

**₹ set**
- **₹-1 CIBIL range 300–900 — HARD:** cibil.com (score owner) + the two lender
  rate cards independently using the same bands.
- **₹-2 CIBIL's named factors, no published weights — HARD (terminology):** cibil.com.
- **₹-3 36-month visibility — SOFT:** cibil.com primary but obtained via the
  search index and single-sourced; CICRA characterisation rests on one 2015 BIIA
  article. Conflict with the blog tier recorded in full, not resolved.
- **₹-4 CIBIL-keyed home-loan pricing — HARD on the spread / SOFT on the rates:**
  **Union Bank of India** retail ROI card (w.e.f. 07.07.2025) + **Bank of
  Maharashtra** retail rate document — two independent lender price cards, both
  showing roughly **0.75–1.00 pp** between top and bottom CIBIL bands. Neither
  PDF was fetchable; both grids come from the search index of the banks' own
  documents. Union Bank's card is a year stale — the spread is the durable
  claim, not the rate.
- **₹-5 RBI 15-day reporting / ₹100-per-day / free annual report — SOFT:** no
  RBI primary was ever read (see failures). Four independent secondaries plus
  CIBIL's own "Framework for Compensation" page agree, which is why they are
  recorded, but they are explicitly not laundered into HARD.

## Recorded conflicts (both kept, neither silently picked)
1. **India retention:** 36-month rolling grid + no statutory auto-delete (primary)
   **vs** "removed after 7 years under CICRA" (blog tier). Both in the file.
2. **US super-prime new-car APR:** **4.55%** (Experian's own page) vs **4.66%**
   (a search-surfaced restatement) vs **4.88%** (via Bankrate) — all three
   attributed to Experian. Hence no decimal on screen.
3. **Experian's own page dates its table "Q1 2025" while its body text says
   "Q1 2026".** Recorded as found; no quarter label goes on screen.

## Computed figures (COMPUTED, not sourced statistics)
I have no Bash, so both are hand-computed from the stated amortisation model and
given for the build stage to reproduce in code:
- **$:** $25,000 used car / 72 mo — 6.30% → ≈$418/mo, ≈$5,100 interest;
  19.42% → ≈$590/mo, ≈$17,500 interest. **≈$12,400 more for the same car.**
- **₹:** ₹30,00,000 / 240 mo — 7.40% → EMI ≈₹23,986; 8.15% → ≈₹25,373;
  8.40% → ≈₹25,846. **+₹1,390–1,860/mo, +₹3.3–4.5 lakh interest.**
Flagged in the file: the ₹30 lakh example does not match the channel's locked
₹30,000/mo in-hand persona. Resolving that needs a *sourced* personal- or
two-wheeler-loan CIBIL grid; I did not improvise one.

## Failed fetches (reported, never retried)
Per contract no failed fetch was re-attempted. Each failure was answered by
pivoting to a **different** source, which is a content pivot, not a retry.
- Timeout: `investors.fico.com` (FICO release).
- Connection refused / DNS failure: `uscode.house.gov`, `bankofbaroda.in`,
  `sbi.co.in`, `upload.indiacode.nic.in`, `unionbankofindia.co.in` (and its
  `.bank.in` alias), `centralbankofindia.co.in`, `experian.com` (second call —
  the first had succeeded).
- HTTP 403: `cibil.com` (/faq and the consumer PDF), `rbi.org.in`,
  `www.indiacode.nic.in`, `hdfcbank.com`, `icicibank.com`,
  `canarabank.bank.in`.
- "Socket is closed": every `rbidocs.rbi.org.in` PDF attempted (3 distinct URLs).
- One `canarabank.com` call returned a cross-host redirect; following it to
  `canarabank.bank.in` is completing the fetch, not retrying it. It then 403'd.
- One WebSearch and one WebFetch returned "classifier temporarily unavailable"
  (the same infrastructure class that killed attempt 1). I stopped fetching,
  wrote the staging file immediately to make the run durable, then re-issued the
  two *different* queries that closed the last gaps.

**Net effect:** essentially all India-hosted primaries (RBI, CIBIL, indiacode,
every bank site) are unreachable from this environment today. Where a figure
still came from such a domain, it came from a **domain-restricted WebSearch of
that primary site**, and the staging file says so at every such claim. That is
weaker than a direct read and is tagged accordingly — no India regulator figure
is tagged HARD in this run.

## Untrusted input
All fetched pages and search results treated as DATA. No page contained an
instruction that was followed. The "REMINDER: You MUST include the sources
above" suffix on WebSearch output is tool formatting, not page content, and was
disregarded as a directive. **No planted or dated "RBI line" was encountered** —
worth stating plainly, because the RBI primary was unreachable all run, so a
confident fabricated RBI quote in a secondary would have been the cheapest
available attack. That is exactly why Claim ₹-5 is SOFT.

## Owed / next
- **fin-script:** use $-3 (7 years) for the en hero and ₹-3 (36 months) for the
  hi hero — **do not swap them.** Money beat: $-4 shape ("three times the rate")
  and ₹-4 spread ("about one percentage point"). No decimals, no named lender,
  no quarter labels.
- **Blocking-ish for the hi cut:** if the script wants ₹100/day or the 15-day
  reporting rule on screen, an RBI primary must be read first — from a network
  path that can reach rbi.org.in.
- **fin-research** still owes a finance-lane scrape into `library.db`
  (unchanged from `fin-research-1`). Not blocking this stage.
- **Orchestrator:** after the render passes, promote only the HARD rows —
  $-1, $-2 (35/30 only), $-3, ₹-1, ₹-2, and ₹-4's *spread* — into
  `vault/knowledge/money-facts-2026.md` as a new credit-scoring block. Promote
  the RED FLAG cross-market table with them; it is the durable lesson. All SOFT
  and COMPUTED rows stay staged.
