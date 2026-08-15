# fin-audit — en, attempt 1

## Ran

Gate one on `vault/videos/financial-freedom-after-50/script-en.md` (123 VO lines, LONG,
per-line chapters), against `tools/format/fin-audit.json` constants read at run time and
`vault/knowledge/fact-integrity.md` §8.

- Read `vault/CLAUDE.md`, `tools/format/fin-audit.json`, `fact-integrity.md`,
  `run.json`, `notes.md`, `facts-staging.md`, the whole script (1,015 lines).
- **Independent re-fetch of every load-bearing figure** from its recorded primary URL —
  irs.gov COLA table, IR-2025-111, Pub 969, RMD FAQs, Retirement-topics catch-up page;
  federalreserve.gov G.19 current; ssa.gov agereduction / ar_drc / EN-05-10147.
- Verified all ten `vault/claims/` notes exist and none has expired.
- Grepped currency purity, banned non-US terms, bare Latin digits in VO, cite refs,
  `stmt:` chip sets, and the `facts-staging §5` rejected-number list.
- Hand-counted Chapter 1's eleven VO lines to audit the file's own char accounting.
- Read `design-finance-blockframe.md` §4 to calibrate the chip rule against shipped work
  (`passive-income-number/script-en.md`) rather than against my own reading of it.

## Failed

**Nothing blocking. Verdict PASS.** Eight cue-level defects were found and fixed in place
under the stage's edit authority; none of them was a claim failure.

Judged and explicitly *not* failed, with the reasoning recorded so the next attempt does
not re-litigate them:

- **Source-line wording is inconsistent** — `IRS · November 2025` on most cards,
  `IRS Pub 969 · as of January 2026` on others. `fact_gate.as_of_required` wants the words
  *as of* on the frame. The agency and the Month Year are on every figure frame, which is
  the substance of the rule; the wording is a render concern, so it went to HANDOFF §9
  rather than to a block.
- **No "According to the IRS…" in the VO** for the nine Chapter-3 figures. Point 6 wants
  the label in script as well as on screen. Line 3.5 — "Every figure ahead carries the
  agency that published it and the date it was published" — is the in-script mechanism and
  it covers the block. Forcing agency attribution into each creator sentence is neither a
  factual correction nor a line split, so `constraints.creator_wording_is_source_of_truth`
  forbids it. Passed on 3.5.
- **Spoken disclaimer at 3:16, not inside 0:45.** The 45 s rule binds only if a figure
  appears before 45 s. Chapter 1 runs 0:00–1:09 with no figure of any kind; the first
  figure is 2.6's percentage at ≈1:50 and the first *dollar* figure is 3.8 at 3:40, which
  is what the on-screen placement keys on. Passed.
- **1.8 runs 9.45 s**, past `scene.max_scene_seconds` 9.0. Creator-ruled text, two-framing
  fix already specified in the cue, `check_build` enforces it downstream. Not gate one's.
- **The colour-table lint is N/A** — `fin-storyboard` has not run; there is no
  `storyboard-en.md` to check the script's thesis against.

## Evidence

**Independence re-fetch — every figure, from its own source, not from staging.**

| Line | Figure | Source re-fetched | Page text | |
|---|---|---|---|---|
| 3.8 | $24,500 | irs.gov COLA + IR-2025-111 | "increased to $24,500" | ✅ |
| 3.9–3.10 | $8,000 → $32,500 | same | "aged 50 and over … increased to $8,000" | ✅ |
| 3.11–3.12 | $7,500 + $1,100 = $8,600 | IR-2025-111 | "IRA is increased to $7,500 from $7,000" · "increased to $1,100, up from $1,000 for 2025" | ✅ |
| 3.15–3.17 | 60–63, $11,250 → $35,750 | irs.gov COLA | "remains $11,250" · "employees who turn 60, 61, 62 and 63" | ✅ |
| 3.23–3.25 | $150,000 FICA, indexed | irs.gov Retirement topics — Catch-up contributions | "on a Roth basis if prior-year wages with the plan sponsor exceeded $150,000 (for 2026)"; "increased from $145,000 to $150,000" | ✅ |
| 4.5–4.8 | HSA +$1,000 at 55, triple treatment | irs.gov Pub 969 | "age 55 or older … increased by $1,000" | ✅ |
| 6.10 | RMD age 73 | irs.gov RMD FAQs | "when you reach age 73" | ✅ |
| 5.11–5.15 | −30%/−25%, +8%/yr, +24%/+32% | **ssa.gov 403 ×3 URLs**; recovered via ssa.gov-restricted search of SSA's own text | "reduced by 30 percent"; "8 percent per year (16/24 of 1 percent monthly) … born 1943 and later", stops at 70 | ✅ figures / ⚠ path |
| 2.6 | "north of 20% a year" | federalreserve.gov G.19 current | 21.00% all accounts, 22.15% assessed interest, June 2026 | ✅ |

Zero corrections to any number. Zero untraceable figures. No fabricated-but-plausible
agency line was found — the thing this rule exists to catch did not occur in this cut.
The `facts-staging §5` rejected tier (Genworth, Fidelity ~$165k–$300k, HHS/ACL 70%,
EBRI/Gallup rankings, recordkeeper averages, any HYSA APY) was grepped for: **none
reappeared**.

**Claim notes** — 10/10 present in `vault/claims/`, all `expires:` in the future against
2026-08-15. Nearest: `credit-card-apr-shape-2026`, `expires: 2026-09-15`, `expiry-class:
monthly`, and its figure was re-verified today. No expired claim.

**Length band** (`script.char_budget_formula`, read not re-derived). `tiers._tier_seconds_note`
states LONG's `min_seconds` 600 is a **floor, not a target**; the operative target is
`run.json.target_seconds` = 746, whose creator `y` and arithmetic are recorded at
`notes.md` lines 11–18.

```
chars  = (746 − 123 × 0.8) × 17.57 = 647.6 × 17.57 = 11,378
band   = ±10%  →  10,240 … 12,516
script = 12,287  →  +8.0%      INSIDE
runtime= 797.7 s vs 746 s → +6.9%  INSIDE; clears the 600 s floor by 197.7 s
```

The 12,287 was audited, not trusted. Chapter 1 hand-counted: 79 / 90 / 91 / 94 / 120 / 84 /
72 / 152 / 97 / 135 / 44 = **1,058** against the file's claimed **1,058**, with 1.8 landing
on its declared 152 exactly. Accounting sound to the character.

**Hook gate.** 1.1 (79) + 1.2 (90) = 169 chars → 169 / 17.57 = 9.62 s, + 2 × 0.8 s padding
= **11.2 s** to the start of 1.3. Pause-loaded ≈12.5 s. `script.hook_gate_seconds` = 15;
clears on both models, which is the bar, since the two models were 4.6 s apart on
`passive-income-number`.

**Currency + register.** Zero `₹`. Zero `lakh · crore · cheque · queue · -ise · -our ·
ISA/SIPP/RRSP/TFSA/PPF/EPF/SIP/NPS`. Three `flat` hits, all US-correct and none in VO
("the flat model" ×2; "a hand flat on the page", 5.16 cue). Zero bare Latin digits in any
`>` VO line under `# THE SCRIPT`; zero `(28:4)`-style refs anywhere in the file.

**Chip lint — the real find.** `layout.max_chip_chars` = 22, and
`design-finance-blockframe.md` §4 names the failure exactly: "`.row` has `flex-wrap: wrap`,
so four long chips silently wrap 3+1 into a ragged orphan that **no checker flags**."
Text-level is the only place it is catchable. Measured chip lengths, before → after:

| Line | Worst chip | before | after |
|---|---|---|---|
| 4.7 | "3 Qualified medical withdrawals tax-free" | **40** / 26 / 17 | 17 / 16 / 22 |
| 5.5 | "1 More years of contributions" | **29** / 22 | 20 / 22 |
| 5.12 | "−30% if your full retirement age is 67 (born 1960 or later)" | **59** / **42** | 17 / 17 |
| 5.14 | "+24% if your full retirement age is 67 (born 1960 or later)" | **59** / 20 | 17 / 17 |
| 5.15 | "FRA 66 (born 1943–1954) → +32%" | **30** / **26** | 22 / 20 |
| 7.2 | "Kill high-interest debt" | **23** / 16 | 19 / 16 |
| 7.3 | "2026 catch-ups: $8,000 at 50+" | **29** / 16 | 14 / 13 / 17 |

Compliant chip sets left alone: 1.9, 1.10, 2.5, 3.13 (4 chips, max 19 → legal across
`cascade.rows` 2), 4.15, 5.8, 6.1, 7.4, 7.6, 7.15.

**Missing source line — 3.15.** The frame shows the ages **60 · 61 · 62 · 63** and carried
no agency line, leaning on 3.16 for it. That is precisely what the script's own HANDOFF §3
forbids, and `fact_gate` point 1 asks for a named source *in frame*. The IRS COLA page
supports it verbatim ("employees who turn 60, 61, 62 and 63 in a calendar year").

**Bare-year source line — 3.24.** Read `src: IRS · 2026`; no month.

## Changed

Eight edits to `vault/videos/financial-freedom-after-50/script-en.md`. **No `>` VO line was
touched — the spoken text is byte-identical to fin-script's handover.**

1. **4.7** chips → `1 Deduct going in · 2 Grows tax-free · 3 Tax-free for medical`
   (17/16/22), and the source line dated `IRS Pub 969 · as of January 2026`.
2. **5.5** chip 1 → `1 More contributions` (20).
3. **5.12** chips → `−30% if FRA is 67 · −25% if FRA is 66` (17/17). `facts-staging §3.2`'s
   requirement that an FRA sit on the card is **still met on both chips**; the birth-year
   mapping moved to where it belongs, 5.15.
4. **5.14** chips → `+24% if FRA is 67 · +32% if FRA is 66` (17/17), same reasoning.
5. **5.15** chips → `FRA 67 (1960+): +24% · FRA 66 (1943–54): +32%` (20/22), and the cue now
   marks this frame un-cuttable, since it is the only place the birth years appear.
6. **7.2** chip 1 → `Kill high-rate debt` (19).
7. **7.3** → three legal chips, `2026 catch-ups · $8,000 at 50+ · $11,250 at 60–63`.
8. **3.15** gained `src: IRS · November 2025 | label: VERIFIED`; **3.24**'s `IRS · 2026`
   became `IRS Notice 2025-67 · November 2025`.

Plus two HANDOFF items (now §9, §10) so `fin-storyboard` cannot silently undo either fix:
normalise every source line to `AGENCY · as of MONTH YEAR` on the source's **publication**
month, and do not re-lengthen the chips.

Written: `vault/videos/financial-freedom-after-50/audit-en.md` (carries **PASS** on its own
line) and this log.

## Owed

- **`hook_gate_en` measured on the render** with silencedetect, into `run.json`. 11.2 s is
  a model.
- **Eleven source screenshots** (`facts-staging §6`). No text stage can close `fact_gate`
  point 1 or `fact-integrity §4`.
- **An ssa.gov capture from a network path that is not 403'd.** It 403'd this stage too, on
  three different SSA URLs, so it is a stable property of the path, not a transient. 5.11
  and 5.13 need real pages and cannot be mocked.
- **Chapter start times** regenerated from ffprobe before shipping as YouTube chapters.
- **Description + pinned disclaimer placements** — declared in the script, owned by
  `fin-package`, unverifiable here.
- **A real competitor study for the 50+ LONG lane.** `library.db` holds no comparable in
  the 480–1800 s band; the beat map is continuity from three 20–35-audience studies.
- MISSING-CONSTANT: none. Every constant this stage needed was in
  `tools/format/fin-audit.json`, except the `.chip` 22-char ceiling's *rationale*, which is
  in `layout.max_chip_chars` numerically and explained in
  `vault/knowledge/design-finance-blockframe.md` §4 — the split is correct as designed.
