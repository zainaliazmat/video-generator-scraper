# fin-research log — good-debt-vs-bad-debt, attempt 1 (2026-07-28)

## What I did
1. Read `vault/CLAUDE.md`, `vault/workflows/video-study.md`,
   `vault/templates/video-study.md`, `tools/format.json`, and
   `vault/videos/good-debt-vs-bad-debt/run.json`. Creator brief: style "signal";
   locked hook — "The minimum payment is a trap. Here's the actual math."; core
   beats debt-is-renting-money → good vs bad debt (education/business vs
   consumption) → how minimum payments work → compounding working against you;
   hero-math ₹50,000 @ 40% APR (illustrative) / US-$ rewrite sourced separately;
   action step "pay more than the minimum". Short tier, 165s target.
2. Ran the study packet build with the run.json topic:
   `venv/bin/python backend/study.py "good debt vs bad debt"` → exit 1:
   "No usable videos in the library for 'good debt vs bad debt'
   (need >=100 views, >=240s). Scrape first."
   Per contract I ran the topic query once and did NOT retry or try alternate
   query strings — the orchestrator owns retries.

## What failed
`library.db` has zero comparable long-form matches for the good-debt/bad-debt /
credit-card-interest / minimum-payment topic space — the same empty-lane result
the pay-yourself-first run hit, i.e. the personal-finance-explainer lane has not
been scraped into the library. study.py could not pick TOP/MID/LOW, so no packet
exists. Per contract no study note was written —
`vault/knowledge/video-studies/good-debt-vs-bad-debt.md` was intentionally NOT
created (never degrade a study into a study of thumbnails).

## Evidence
- study.py run above, exit code 1, "Scrape first" message (needs ≥100 views,
  ≥240s; found none).
- Existing studies in `vault/knowledge/video-studies/` are only
  `claude-video-editing-launch` and `pompeii-last-day` — neither covers debt or
  personal finance.
- Precedent for this exact failure + handling:
  `vault/videos/pay-yourself-first/logs/fin-research-1.md` (EmptyStudyPacket →
  rescued, run continued on vault knowledge, scrape recorded as owed).

## Untrusted input
No transcripts, titles, or descriptions were fetched (no packet was built), so no
attacker-controllable DATA was read and nothing instruction-like was encountered.

## Owed
Scrape the good-debt-vs-bad-debt / credit-card-interest / minimum-payment /
"debt explained" competitor lane (Hindi + US personal-finance creators, long-form
≥240s) into `library.db`, then re-run this stage. One scrape of the broader
personal-finance-explainer lane clears this debt for this topic and its siblings
(emergency-fund, pay-yourself-first).

Until then the run continues on vault knowledge only:
- the creator's locked hook + beats + hero-math from `run.json`;
- `vault/knowledge/best-practices.md` (hook/packaging rules);
- `vault/knowledge/us-english-script-style.md` + `haryanvi-hindi-script-style.md`
  (per-cut voice/register);
- `vault/knowledge/money-facts-2026.md` for any APR/number — verify + source,
  never invent.
