# fin-evidence — financial-freedom-after-50 — attempt 1 (2026-08-15)

Tier `long` · cut `en` (US/$ only) · target 746 s from `run.json`.
Comparable band applied: **480–1800 s** (`tiers.long.comparable_length_band_seconds`).

## Ran

**Part A — lane study**
1. `venv/bin/python backend/study.py "financial freedom after 50 retirement"` → exit 0,
   no packet: *"No usable videos in the library for 'financial freedom after 50 retirement'
   (need >=100 views, >=240s). Scrape first."*
2. `venv/bin/python backend/study.py "retirement savings"` → exit 0, packet at
   `research/retirement-savings/`. **One** pick only (TOP `BxHYGm3JCqs`). Video download
   403'd; the tool printed its own
   *"ERROR: only 0/1 picks produced a transcript — not enough to ground a study note."*
   Not a retry of a failed command — run 1 succeeded and returned an empty result set; run 2
   was a broader query against the same thin library.
3. Read `research/retirement-savings/manifest.md` and the three `.vtt` caption files that
   survived the failed download.

Read first, per contract: `vault/CLAUDE.md`, `tools/format/fin-evidence.json`,
`vault/knowledge/fact-integrity.md`, `vault/workflows/video-study.md`,
`vault/templates/video-study.md`, `vault/claims/README.md`, `vault/sources/README.md`,
`vault/knowledge/money-facts-2026.md`, `vault/knowledge/subscription-economics-2026.md`
(headings), `vault/videos/financial-freedom-after-50/{notes.md,run.json,source-draft.md}`.

**Part B — sourcing.** 11 fetches + 6 domain-restricted searches across IRS, SSA, Federal
Reserve and 26 U.S.C. Read directly: IRS IR-2025-111, IRS COLA limits table, IRS catch-up
topics page, IRS Pub 969, IRS RMD FAQs, IRS Roth catch-up final-regs release, Cornell LII
26 U.S.C. §223, Federal Reserve G.19 current release. Via domain-restricted search of the
agency's own domain: IRS Notice 2025-67, IRS Notice 2023-62, all four SSA figures.

## Failed

- **The study, and it cannot be fixed at this stage.** `library.db` holds **no US retirement
  comparable at all**. The single pick returned is an **India EPF video** — statutory wage
  ceiling ₹15,000, mandatory contribution ₹1,800/month, Employees' Provident Fund Scheme 2026.
  Wrong market, wrong currency, wrong institution. Even had the video downloaded, studying it
  would have taught this cut nothing and risked exactly the contamination the ₹-glyph rule
  exists to prevent. **No study note written** — correct behaviour per contract, and the right
  call independently: 1 pick, 0 usable, and studying thumbnails instead is explicitly forbidden.
- **`ssa.gov` returns HTTP 403 to every direct fetch from this pipeline.** Four attempted URLs
  (`/benefits/retirement/planner/agereduction.html`, `/benefits/retirement/planner/delayret.html`,
  `/oact/quickcalc/earlyretire.html`, `/oact/ProgData/ar_drc.html`) all 403'd. Not retried.
  Recovered via domain-restricted search of ssa.gov returning SSA's own page text — the same
  fallback the 2026-07-29 credit-history run used for cibil.com. Three distinct SSA documents
  (Benefits Planner, OACT actuarial, SSA policy explainer) agree on every figure, and the
  percentages are statutory, so the claims stand as HARD; the **screenshots are owed**.
- **IRS `.pdf` drops do not read inline** — Notice 2025-67 and Rev. Proc. 2025-19 both return as
  compressed binary through the fetcher. Every figure from them is independently corroborated by
  an IRS **HTML** page that was read directly, so nothing rests on the unread PDFs alone.
- **`cms.gov` and `medicare.gov` 403'd.** Immaterial: the draft contains no Medicare figure, and
  adding one would exceed `creator_wording_is_source_of_truth`. Not pursued. Not retried.
- **`federalreserve.gov/releases/g19/current/g19.htm` returned a stale table** (2012 columns) on
  the second read while `/releases/g19/current/` returned Aug-2026 data on the first. Recorded as
  part of the period-label conflict below rather than treated as a fetch failure.

## Evidence

### Part A substitute — no packet, so the lane read is transferred, and is labelled as such

Nothing in this subsection was observed in a packet for **this** topic. It is carried from the
finance studies already in the vault, and the creator's draft is measured against it.

- **Hook type in the draft: pain-mirror / objection-kill cold open.** *"Are you over 50 and
  worried the ship has sailed… that feeling, while common, is a myth."* This is a hook type
  already on record (`japanese-money-methods` — pain-mirror cold open, 15.8× V/S). It is **not**
  the strongest form on record for finance: `passive-income-number` found two unrelated channels
  converging on **second-person future-state simulation** (the won morning), and
  `first-lakh-first-thousand`'s TOP opened **number-first inside 10 s**.
- **Payoff promise lands at ≈0:50–1:00** ("In this video, I'm giving you a simple 5-step game
  plan…") = **≈7% of a 746 s runtime**. That is squarely inside the ~8% window both twins in
  `passive-income-number` hit (A ≈0:22 / 8%, B ≈0:45 / 8%). **The draft's timing is right.**
  Its form is an *announcement*, not an open loop — the weaker of the two operators observed,
  but the safer one under `no_return_promise`, and it is the creator's wording, which governs.
- **views/sub ratios, low-performer autopsy, keyframe read: OWED.** No packet, so no numbers.
  A study note asserting them would be invented, which is the one thing this stage may not do.

**Beat map — the draft's own structure, proportioned to 746 s** (not a competitor's; the source
is `source-draft.md`, measured by section length):

| Beat | ≈timecode | ≈% | What lands |
|---|---|---|---|
| Pain-mirror cold open + "it's a myth" | 0:00–0:50 | 0–7% | objection named, then denied |
| Promise: 5-step roadmap, steps listed | 0:50–1:20 | 7–11% | announcement, loop closed early |
| Step 1 Stabilize — debt ladder + emergency fund | 1:20–3:20 | 11–27% | first mechanism, **no figure** |
| Step 2 Maximize — catch-up contributions | 3:20–6:00 | 27–48% | **every dollar figure in the video lands here** |
| Step 3 Protect + Step 4 Income flexibility | 6:00–9:40 | 48–78% | HSA $1,000; the SS percentages at ~70% |
| Step 5 Transition + recap + CTA to next video | 9:40–12:26 | 78–100% | re-frame, no new numbers, single CTA |

Two structural observations worth handing to `fin-script`: **all nine IRS figures cluster in one
2.5-minute block (27–48%)**, which is a density risk for a 50+ audience acting on them — the
`as-of` card has to survive nine consecutive reveals; and **the ~70% beat is the Social Security
percentages**, which is the correct place for the video's strongest claim and matches the prior
beat-map shape on record.

### Part B — every creator-supplied figure checked against its issuing agency

`notes.md` listed nine UNVERIFIED creator figures. **All nine confirmed. Zero numeric
corrections.** That is the headline: the creator's draft is arithmetically clean.

| Creator draft said | Agency says | Verdict |
|---|---|---|
| 401(k)/403(b) 2026 limit $24,500 | $24,500 (from $23,500) — IRS Notice 2025-67 / IR-2025-111 / COLA table | ✅ |
| Age-50 catch-up $8,000 → $32,500 | $8,000 (from $7,500); total is arithmetic | ✅ |
| IRA $7,500 + $1,100 → $8,600 | $7,500 (from $7,000), $1,100 (from $1,000) | ✅ |
| 60–63 super catch-up $11,250 → $35,750 | $11,250, unchanged from 2025 | ✅ |
| Roth catch-up threshold $150,000 prior-year FICA | $150,000, up from $145,000 — the **2025** threshold governing **2026** catch-ups | ✅ |
| HSA age-55 catch-up $1,000 | $1,000, fixed statutory table "2009 and thereafter" | ✅ |
| SS early-claim reduction 25–30% | 30% at FRA 67, 25% at FRA 66 | ✅ band correct |
| SS delayed retirement credit ~8%/yr, 24–32% at 70 | 8.0%/yr born 1943+; 24% at FRA 67, 32% at FRA 66 | ✅ band correct |
| 4% rule framed as guideline, not gospel | no agency publishes it — Bengen 1994, Trinity 1998 | ✅ hedge is mandatory |

Artifacts: **12 source notes** in `vault/sources/{irs,ssa,federal-reserve}/`, **11 claim notes**
in `vault/claims/`, and `facts-staging.md` in this video's directory. Direction is
source ← claim → video throughout; no video→source link was written.

**Hero number, US/$ (the only market this run has):**
**$35,750** — the most a 60-to-63-year-old can put into a workplace plan in 2026
($24,500 elective deferral + $11,250 SECURE 2.0 catch-up), *if the plan offers it*.
Source line: **IRS, Notice 2025-67 / IR-2025-111, November 2025 — as of January 2026.**
It is the hero because it is the largest, the least known, the one the audience is age-eligible
for right now, and the one that most directly falsifies "the ship has sailed".

**Hero number, ₹/India: none, and none is permitted.** `cuts.en` is the sole cut and `₹` is
`forbidden_currency`. The ₹ set was not sourced, not converted, and not carried across.

### The three findings worth more than the confirmations

1. **The "guaranteed return" sentence is the only line that should be forced.** The draft calls
   the 8% delayed retirement credit *"a guaranteed, inflation-adjusted return from the government
   that is simply impossible to find anywhere else."* The DRC is a statutory adjustment to a
   benefit formula, not a return — and `run.json → constraints.no_return_promise` names this exact
   figure. `passive-income-number` logged the same species of failure as field-tested: a video
   that "states 4% once and then ships six bare numbers". Minimal fix that keeps the creator's
   rhythm is drafted in `[[../../claims/ss-delayed-retirement-credit]]`. This stage flagged it and
   did not touch the script.

2. **Half of each Social Security band is unreachable by this audience.** "25% to 30%" and
   "24% to 32%" are both correct *as bands*, but FRA 66 covers birth years 1943–1954 — those
   viewers are **72 or older in 2026** and cannot claim at 62. Everyone turning 62 in 2026 was
   born 1964 → FRA 67 → **30% reduction / 24% delayed credit**. Keep the creator's band in the VO;
   put the FRA qualifier on the card. An unqualified single percentage is the
   "national figure presented as personally applicable" anti-pattern (fact-integrity §5).

3. **The Roth catch-up effective date is a booby trap for the next re-verifier.** IR-2025-91 says
   the final regulations apply "to contributions in taxable years beginning after
   December 31, 2026", which reads like the rule starts in 2027. It does not: Notice 2023-62's
   administrative transition period covered 2024–2025 only and ended 2025-12-31, so the mandate is
   **operative in 2026** under good-faith interpretation. The draft's "one more critical update
   for 2026" is right. All three documents are attached to the claim precisely so a future check
   cannot "correct" a correct script into a wrong one.

### The one trap to avoid

**The Social Security earnings test — a trap of adjacency, not of error.** Step 4 pairs
"keep earning, part-time or consulting" with "delay Social Security". Together those are **safe**:
the earnings test only bites people who are *already collecting*. But the two halves separate
easily in a viewer's head, and someone who keeps working **and** claims at 62 loses **$1 of
benefit for every $2 earned above $24,480** (2026, SSA) with no warning anywhere in the script.

No stage may add a "claim early and keep working" beat without that number, and if it is ever
added the qualifier is mandatory: **withheld benefits are not lost** — SSA credits them back at
full retirement age. Sourced and parked at `[[../../claims/ss-earnings-test-2026]]` with
`used-in: []`, so adding it is cheap and inventing it is unnecessary.

### Conflict recorded, per the both-sources rule

Federal Reserve G.19 credit-card rate: the current release (rel. 2026-08-07) returns
**21.52% assessed / 21.00% all accounts** labelled **June 2026**, while `money-facts-2026`
carries **22.15% "May 2026 monthly"** and **21.52% "Q1 2026"**. The same decimal is wearing two
period labels. money-facts already records one mislabel on this exact series that **reached a
script** before being caught (corrected 2026-08-01). Both readings recorded; **decimal tagged
SOFT, shape tagged HARD** — say *north of 20%*, never a decimal. The draft names no number here,
which is the right call and should survive scripting.

### Blog-tier / off-whitelist numbers found and rejected

Enumerated in `facts-staging.md` §5 so `fin-script` does not rediscover them: HHS/ACL
"70% chance of needing long-term care"; Genworth cost-of-care tables; Fidelity retiree
health-care estimate; Fidelity/Vanguard average 401(k) balance by age; EBRI/Gallup "top
retirement fear" rankings; NerdWallet/Bankrate/Investopedia 2026 limit tables (followed back to
the IRS and cited there); any specific HYSA APY.

The average-balance-by-age rejection is the one worth reading twice — beyond being
off-whitelist, quoting "the average 50-something has $X" would **argue against the video's own
premise** that being behind is a feeling and not a verdict.

### Untrusted input

The one study transcript (`BxHYGm3JCqs`) is an India EPF explainer and was treated as DATA only.
**No injected instruction, no directive, no fabricated dated agency line was present** — the
attack this pipeline defends against did not appear this run. It did carry live rupee figures
(₹15,000 statutory wage ceiling, ₹1,800/month), and `cuts.en.forbidden_currency` is `₹`: none of
it entered `facts-staging.md`, the claims, or the sources. Nothing read this run changed which
commands were run or which paths were written.

## Changed

**Written (all new files):**
- `vault/sources/irs/` — `irs-notice-2025-67.md`, `irs-ir-2025-111.md`, `irs-cola-limits-2026.md`,
  `irs-roth-catchup-final-regs.md`, `irs-notice-2023-62.md`, `irs-pub969-hsa.md`,
  `usc-26-223-hsa.md`, `irs-rmd-faq.md`
- `vault/sources/ssa/` — `ssa-early-retirement-reduction.md`, `ssa-delayed-retirement-credits.md`,
  `ssa-cola-factsheet-2026.md`
- `vault/sources/federal-reserve/` — `fed-g19-2026-08.md`
- `vault/claims/` — `401k-elective-deferral-2026.md`, `401k-catchup-age50-2026.md`,
  `401k-supercatchup-60-63-2026.md`, `ira-limit-2026.md`, `roth-catchup-threshold-2026.md`,
  `hsa-catchup-age55.md`, `rmd-beginning-age-73.md`, `ss-early-claim-reduction-62.md`,
  `ss-delayed-retirement-credit.md`, `ss-earnings-test-2026.md`,
  `credit-card-apr-shape-2026.md`
- `vault/videos/financial-freedom-after-50/facts-staging.md`
- this log

**Deliberately NOT written:**
- `vault/knowledge/money-facts-2026.md` — untouched. Promotion is `tools/close_out.py`'s job after
  both renders pass; a same-run write would let this run grade its own homework.
- `vault/knowledge/video-studies/financial-freedom-after-50.md` — no packet, no note.
- `source-draft.md`, `notes.md`, `run.json` — this stage does not edit the script or the run.

## Owed

1. **Eleven source screenshots.** This stage has no browser or capture tool in its allowlist, so
   `vault/screenshots/` gained nothing. Target filenames are already recorded in each source
   note's `screenshot:` field (`{source-id}-20260815.png`). **Fact-gate point 1 and standard §4
   cannot be satisfied by this run alone** — whoever captures them must record the real page with
   the URL in frame, and must re-date the filename to the capture date if it is not 2026-08-15.
2. **A direct read of ssa.gov.** All four SSA figures came via domain-restricted search because
   ssa.gov 403s this pipeline. Needs a network path that can reach it.
3. **The competitor study, and the scrape it depends on.** `library.db` has zero US retirement
   comparables in the 480–1800 s band. A scrape on this lane must run before any study of this
   topic is possible. The sanctioned no-cookie substitute is vidIQ `video_transcript`
   (5 credits/video, `.claude/skills/vidiq/SKILL.md` R2) — words only, so the keyframe half of the
   analysis stays owed even then. Alternatively export `YTAUTO_COOKIES` / `YTAUTO_COOKIES_BROWSER`
   and re-run `study.py`; the 403 on the video download is the documented bot-check.
4. **Pub 590-B attached to `rmd-beginning-age-73`** before any future video leads on RMDs. That
   claim is currently single-sourced.
5. **A decision on the "number one financial fear" sentence** (label it opinion, or cut the
   ranking). Owed to `fin-script`/`fin-audit`, not to this stage — no whitelisted source for a
   ranked fear list exists, so it cannot be sourced, only reframed.
