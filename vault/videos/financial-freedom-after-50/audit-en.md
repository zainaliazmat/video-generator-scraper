---
summary: fin-audit gate one for financial-freedom-after-50, cut en, attempt 1. Every load-bearing figure was re-fetched from its recorded primary URL independently of facts-staging; all nine IRS/SSA/Fed figures survived. Eight cue-level edits made (seven chip-length violations, one missing source line, one bare-year source line). Verdict PASS.
updated: 2026-08-15
source: independent re-fetch of irs.gov (COLA table, IR-2025-111, Pub 969, RMD FAQ, catch-up topic page), federalreserve.gov G.19, ssa.gov (403 — recovered by domain-restricted search, as facts-staging §6 predicted) · tools/format/fin-audit.json · vault/knowledge/fact-integrity.md §8 · vault/knowledge/design-finance-blockframe.md §4 · vault/claims/*
stage: fin-audit, cut en, attempt 1
---

# fin-audit — financial-freedom-after-50 (en), attempt 1

PASS

Edited in place: **8 cues**. No VO line was touched, so the spoken text is byte-identical
to what fin-script handed over — but the file hash changed, so voice work runs against
**this** version.

---

## 1. The independence re-fetch — every number, from its own source, not from staging

`facts-staging.md` was written by this run, so it was treated as a list of URLs to check,
not as evidence. Each figure below was pulled from the recorded primary URL by this stage.

| Script line | Figure | Re-fetched from | What the page said | Verdict |
|---|---|---|---|---|
| 3.8 | $24,500 | irs.gov COLA table + IR-2025-111 | "increased to $24,500" | ✅ |
| 3.9–3.10 | $8,000 → $32,500 | same | "catch-up … aged 50 and over … increased to $8,000" | ✅ arithmetic checks |
| 3.11–3.12 | $7,500 + $1,100 = $8,600 | IR-2025-111 | "IRA is increased to $7,500 from $7,000" · "catch-up … increased to $1,100, up from $1,000 for 2025" | ✅ |
| 3.13 | 401(k)/403(b)/457/TSP | IR-2025-111 | "401(k), 403(b), governmental 457 plans, and the federal government's Thrift Savings Plan" | ✅ card is more complete than the VO, which is fine |
| 3.15–3.17 | ages 60–63, $11,250 → $35,750 | IRS COLA table | "higher catch-up … remains $11,250" · "employees who turn 60, 61, 62 and 63" | ✅ |
| 3.23–3.25 | $150,000 prior-year FICA wages, indexed | irs.gov Retirement topics — Catch-up contributions | "must make catch-up contributions on a Roth basis if prior-year wages with the plan sponsor exceeded $150,000 (for 2026)"; threshold "increased from $145,000 to $150,000" | ✅ indexation confirmed, so 3.25 stands |
| 4.5–4.8 | HSA triple treatment, +$1,000 at 55 | irs.gov Pub 969 | "age 55 or older … your contribution limit is increased by $1,000"; deductible in / tax-free growth / tax-free qualified withdrawals | ✅ |
| 6.10 | RMDs begin at 73 | irs.gov RMD FAQs | "must start taking withdrawals … when you reach age 73" | ✅ |
| 5.11–5.15 | −30%/−25% at 62 · +8%/yr · +24%/+32% | ssa.gov **HTTP 403 on every direct fetch** (agereduction, ar_drc, EN-05-10147) — recovered by ssa.gov-restricted search returning SSA's own text | "reduced by 30 percent" for FRA 67 at 62 · "8 percent per year (16/24 of 1 percent monthly) for those born 1943 and later", stops at 70 | ✅ figures confirmed, **retrieval path still degraded** |
| 2.6 | "north of 20% a year" | federalreserve.gov G.19 current | 21.00% all accounts, 22.15% accounts assessed interest, June 2026 data | ✅ the shape holds with room; the shape-only rule is the right call |

**Nothing untraceable, nothing killed.** No figure in the script is absent from
`facts-staging §1/§2`, and no staged figure was contradicted by its own source. The
failure mode this rule exists to catch — a plausible dated agency line that the page
does not actually contain — did not occur in this cut.

**Claim-note coverage:** all ten referenced notes exist in `vault/claims/` and every
`expires:` is in the future against today, 2026-08-15. The nearest is
`credit-card-apr-shape-2026` at **2026-09-15** (`monthly`) — verified this month, and it
is the one that will expire first. Nothing stale.

---

## 2. What was changed, and why

### Killed: nothing. No claim failed its source.

### Rewritten: 8 cues (production text only — zero VO characters)

**Seven chip-length violations.** `layout.max_chip_chars` is 22 and
`design-finance-blockframe §4` names the exact silent failure: "`.row` has `flex-wrap:
wrap`, so four long chips silently wrap 3+1 into a ragged orphan that **no checker
flags**." Text-level is the only place this is catchable, which is why it is gate one's
job. Measured before → after:

| Line | Chip that broke it | was | now |
|---|---|---|---|
| 4.7 | "3 Qualified medical withdrawals tax-free" | 40 / 26 / 17 | 17 / 16 / 22 — `1 Deduct going in · 2 Grows tax-free · 3 Tax-free for medical` |
| 5.5 | "1 More years of contributions" | 29 / 22 | 20 / 22 |
| 5.12 | "−30% if your full retirement age is 67 (born 1960 or later)" | 59 / 42 | 17 / 17 — `−30% if FRA is 67 · −25% if FRA is 66` |
| 5.14 | "+24% if your full retirement age is 67 (born 1960 or later)" | 59 / 20 | 17 / 17 |
| 5.15 | "FRA 66 (born 1943–1954) → +32%" | 26 / 30 | 20 / 22 |
| 7.2 | "Kill high-interest debt" | 23 / 16 | 19 / 16 |
| 7.3 | "2026 catch-ups: $8,000 at 50+" | 29 / 16 | 14 / 13 / 17 (three chips, one row) |

The compliance content survived every one of these. `facts-staging §3.2` requires a full
retirement age on the SS percentage cards — **it is still on both chips of 5.12 and
5.14**, and the birth-year mapping that makes it actionable now lives where it belongs,
on 5.15, its own dedicated frame, which is flagged as un-cuttable.

**One missing source line — 3.15.** The frame shows the ages **60 · 61 · 62 · 63** as a
bracket and carried no agency line. `fact_gate` point 1 asks whether *every number on
screen* has a named source **in frame**, and the script's own HANDOFF §3 says a card may
not inherit its agency line from the frame before it — yet 3.15 was doing exactly that,
leaning on 3.16. Added `src: IRS · November 2025 | label: VERIFIED`, which the IRS COLA
page supports verbatim.

**One bare-year source line — 3.24.** Read `src: IRS · 2026`. `fact_gate.as_of_required`
wants Month Year. Set to `IRS Notice 2025-67 · November 2025`, matching 3.23 beside it.

**Two HANDOFF items added (now §9 and §10)** so the storyboard cannot undo either fix:
normalise every source line to `AGENCY · as of MONTH YEAR` using the source's
*publication* month, and do not re-lengthen the chips.

---

## 3. Every gate, and how it was decided

**1. Traceability + source survival** — PASS. §1 above.

**2. Length band** — PASS, and this one needed the constant read rather than re-derived.
`script.char_budget_formula` says to use "the tier's target seconds, per
`tiers._tier_seconds_note`", and that note is explicit that LONG's `min_seconds` (600) is
**a floor, not a target**. The run's declared target is `run.json.target_seconds` = **746**,
and `notes.md` lines 11–18 record the creator's `y` on that override with its arithmetic.
So:

```
chars = (746 − 123 × 0.8) × 17.57 = 647.6 × 17.57 = 11,378
band at length_tolerance_pct 10 = 10,240 … 12,516
script = 12,287 → +8.0%   INSIDE
runtime 797.7 s vs 746 s → +6.9%   INSIDE, and clears the 600 s floor by 197.7 s
```

The 12,287 figure was spot-audited rather than trusted: Chapter 1's eleven VO lines were
counted by hand at 79 / 90 / 91 / 94 / 120 / 84 / 72 / 152 / 97 / 135 / 44 = **1,058**,
against the file's claimed **1,058**, and line 1.8 came out at exactly the declared 152.
The accounting is sound to the character, so the total is taken as measured.

**3. Hook payoff inside 15 s** — PASS on the model. Line 1.3 starts after 1.1 (79) + 1.2
(90) = 169 chars → 169 / 17.57 = 9.62 s + 2 × 0.8 s padding = **11.2 s**, matching the
file. Pause-loaded ≈12.5 s. Clears 15 s on both models — which is the bar that matters,
because on `passive-income-number` the two models sat 4.6 s apart. Still owed:
`hook_gate_en` measured on the render with silencedetect.

**4. No product or platform recommended** — PASS. Long-term care appears as two
*categories* (traditional / hybrid) plus self-funding; 4.15's cue already forbids naming an
insurer. No bank, fund, card, security or app anywhere. 2.15 explicitly bans a bank name
and an APY on the high-yield-savings frame. "Wall Street wizard" (1.6) is a figure of
speech arguing *against* stock picking.

**5. Currency purity** — PASS. Zero `₹`. Grepped `lakh · crore · cheque · flat · queue ·
colour/favour/behaviour/labour · -ise verbs · ISA/SIPP/RRSP/TFSA/PPF/EPF/SIP/NPS`. Three
`flat` hits, all US-correct and none in VO: "the flat model" ×2 (a pacing model) and "a
hand flat on the page" (5.16 cue). `SIMPLE IRA` is not an `ISA`/`SIP` hit. Script spells
`maximize`, `stabilize`, `organizing` — US throughout.

**6. Ten-point fact gate** — PASS, all ten, in order:

1. *Named source in frame* — every figure card carries one, **after** the 3.15 fix. Frames
   deliberately without one (2.9, 2.14, 3.19, 3.20, 4.4, 4.11, 4.13, 6.5, 6.7, 6.9,
   6.12, 6.13, 7.2) are `opinion`/`convention` labelled, which is what `fact-integrity §3`
   prescribes — an opinion gets *no* source line, and giving one would be the worse error.
2. *"as of [Month Year]"* — present on every figure frame. The IRS cards use the
   publication month (November 2025 = Notice 2025-67 / IR-2025-111; January 2026 = Pub 969
   revision), the Fed card August 2026 (the current G.19 release, carrying June data —
   correct, and the card carries **no period label**, exactly as `facts-staging` row 11
   demands), SSA August 2026 for statutory percentages. Wording was inconsistent
   (`IRS · November 2025` vs `IRS Pub 969 · as of January 2026`); HANDOFF §9 now normalises
   it. Not a block: the month and the agency are on every frame, which is the substance.
3. *Whitelist* — IRS, SSA, Federal Reserve. All three on `fact-integrity §1`. The one
   non-whitelisted claim, the 4% rule, carries no agency card, no "verified", and is
   labelled convention with "a 1994 study" in the VO. `facts-staging §5`'s rejected tier
   (Genworth, Fidelity, EBRI/Gallup, HHS/ACL 70%, recordkeeper averages, any HYSA APY) —
   **grepped for; not one of them reappeared in the script.** The rediscovery risk that
   §5 exists to prevent did not materialise.
4. *Annual figures re-verified since last January* — every IRS 2026 limit re-read today,
   2026-08-15, from irs.gov. ✅
5. *Monthly figures re-verified this month* — G.19 re-fetched today; the claim note expires
   2026-09-15. ✅
6. *verified/estimate/opinion, on screen AND in script* — on screen, every cue carries a
   label. In script, the load-bearing ones are spoken: 3.5 ("Every figure ahead carries the
   agency that published it and the date it was published") verbally tags the whole figure
   block, 3.15 names the SECURE 2.0 Act, 5.16–5.17 explicitly de-label the DRC as *not* a
   return, and 6.5's "a starting guideline, not gospel" is the opinion label spoken aloud.
   No label drifts mid-sentence. Note deliberately **not** forced: rewriting the creator's
   sentences into "According to the IRS, …" is neither a factual correction nor a line
   split, so `constraints.creator_wording_is_source_of_truth` forbids it; 3.5 is the
   sanctioned mechanism and it covers the block.
7. *No model output without inputs visible* — there is no model in this cut. Every total is
   shown as arithmetic on its own frame (3.10 `$24,500 + $8,000`, 3.12 `$7,500 + $1,100`
   with COMBINED made legible, 3.17 `$24,500 + $11,250`). 3.21 and 5.5 both carry an
   explicit ⚠ banning a growth curve, a rate or a projection. 6.9's "tens, even hundreds of
   thousands" stays a shape in the VO and is barred from reaching a frame.
8. *Title promises what the video delivers* — the recommended title, "The 5-Step Retirement
   Catch-Up Plan For Anyone Over 50 (2026 Limits)", promises five steps (delivered,
   Chapters 2–6) and 2026 limits (delivered, nine of them in Chapter 3). No return, no
   guarantee, no number the viewer is told they will hit.
9. *No product/fund/bank/security as a recommendation* — see gate 4.
10. *Disclaimer in four places* — spoken at 3.4–3.5 (condensed, which §6 permits) ahead of
    the first dollar figure; on-screen lower third on 3.8 plus a full card over the last 4 s
    of 7.16; description and pinned are declared in the script's disclaimer table and owned
    by `fin-package`. Checked and judged **not** a failure: the 45-second spoken rule binds
    only "if any figure appears before then", and Chapter 1 (0:00–1:09) carries no figure at
    all — the first figure of any kind is 2.6's percentage at ≈1:50, and the first *dollar*
    figure is 3.8 at 3:40, which is what §6's on-screen placement keys on.

**7. Claim-note coverage / expiry** — PASS. Ten claims, ten notes, ten future expiries.

**8. No cite refs, no bare digits in VO** — PASS. Grepped every `>` line under `# THE
SCRIPT`: not one bare Latin digit. Every number is spelled ("twenty-four thousand five
hundred dollars", "four oh one k", "I.R.A.", "R.M.D.s", "SECURE two point oh"). No `(28:4)`
pattern anywhere in the file.

**9. Persona** — PASS, and this was the attempt-1 flag that got resolved properly. No host
persona, no credential, no "as a financial advisor", no years-of-experience claim: the
draft's "fifteen years in the trenches" pair is gone, replaced by creator ruling on
2026-08-15 with 1.8's third-person sentence, and `run.json → no_advice_framing` was updated
to match rather than left contradicting the script. The surviving first-person uses — "In
this video, I'm giving you…" (1.3), "I'm here to tell you" (1.4), "hear me out" (5.3), "I
know, it's not the sexiest part of finance" (4.10) — are all narrator-of-the-video, never
practitioner. No investment pick anywhere.

**10. Layout lints** — PASS after the seven chip fixes. One focal element or one declared
cascade per scene; every cascade ≤5 items (largest is 4, at 3.13, 6.1); all 4-item cascades
sit within `cascade.rows: 2` at `max_chips_per_row: 3`; no scene stacks two independent
focal groups. Consecutive cues are single reveals or declared sequences, so
`cue_min_gap_seconds` 0.8 is not at risk. The colour-table check is **N/A this attempt** —
`fin-storyboard` has not run and `storyboard-en.md` does not exist yet.

---

## 4. Not blocked, but the next stage owns these

1. **Eleven source screenshots are owed** (`facts-staging §6`). `fact_gate` point 1 and
   `fact-integrity §4` cannot be closed by any text stage — the frames have to exist.
2. **ssa.gov 403s from this pipeline.** It 403'd me too, on three different SSA URLs, so
   this is a stable property of the network path and not a transient. The percentages are
   statutory and cross-agree across three SSA documents, so the claims stand — but 5.11 and
   5.13 need a real capture from a path that reaches ssa.gov, and it cannot be mocked up.
3. **Line 1.8 runs 9.45 s**, past `scene.max_scene_seconds` 9.0. The text is creator-ruled
   and stays; the two-framing fix is already specified in its cue and `check_build` will
   fail the scene if the storyboard ignores it.
4. **`hook_gate_en` is modelled, not measured.** Record the silencedetect number in
   `run.json` at the voice stage.
5. **Chapter start times are modelled.** Regenerate from ffprobe before they ship.
6. **The lane is unmeasured** — the beat placements are carried from three 20–35-audience
   studies. Continuity, not evidence, and the script says so.
