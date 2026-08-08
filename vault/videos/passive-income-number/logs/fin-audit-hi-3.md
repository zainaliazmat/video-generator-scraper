---
summary: fin-audit hi attempt 3 — SCOPED audit of the ten expanded lines (3.5 · 3.6 · 4.4 · 4.9 · 5.3 · 5.12 · 5.17 · 6.4 · 6.8 · 6.11) added to reach the 510s target at the corrected 14.281 c/s key. Verdict PASS after two in-place edits. Full reasoning in ../audit-hi.md.
updated: 2026-08-08
source: script-hi.md (fin-script hi attempt 3, targeted expansion) audited against facts-staging.md, run.json.constraints, tools/format.json. Every load-bearing figure inside the ten re-fetched live 2026-08-08 by this stage, not trusted from the staging file.
stage: fin-audit, cut hi, attempt 3
---
# fin-audit-hi-3

VERDICT: PASS (with edits) — see vault/videos/passive-income-number/audit-hi.md

Scope as briefed: the ten expanded lines only. Hook gate not re-litigated (measured 8.682s
on 1.3, ruled and recorded). Chapters 1-2 not re-opened. The other 71 lines carry attempt 2's
PASS.

## Edited script-hi.md (2 edits, 0 extra ElevenLabs calls)

- **4.9 VO** «...हाथ में उससे थोड़ा कम **आता है।**» -> «...हाथ में उससे थोड़ा कम **आ सकता है।**»
  (117 -> 120 ch), and its frame `stmt: ... the hand **gets a little less than** the ledger`
  -> `... the hand **may get less than** the ledger`.
  WHY: the expansion's new clause asserted an unconditional net reduction. B.2's LTCG row is
  SOFT and the script correctly put no number on it, but the re-fetched §112A surface carries
  the condition the claim needs and lacks — LTCG applies only **above ₹1.25 lakh of gains per
  financial year**, on the gain portion only. At this cut's own rungs the tax is zero at
  ₹10L/₹20L/₹40L (4.9 sits immediately after the ₹40L rung, where ₹1,20,000 a year is below
  the exemption even if the whole withdrawal were gain) and zero-to-small at ₹1cr. Hedged, not
  killed: certainty -> possibility. Still zero tax figures spoken or shown. The replaced span
  carries no nukta and no chandrabindu, so the edit cannot silently swap a character.
- **6.8 frame** gains `foot: AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE`. VO untouched.
  WHY: 6.8 speaks «इस पच्चीस हज़ार» — a derived income figure — on a frame that carried neither
  its rate nor an ILLUSTRATIVE marker. `derived_income_carries_assumption` binds on the figure;
  the build assert (handoff §8) keys on ON-SCREEN tokens and 6.8 renders none, so it would have
  stayed silent. The script's rate-in-the-line table claims to re-read "every derived-income
  line" and **omits 6.8** — the table's completeness was the untested claim, which is why
  attempt 2 (which graded the seven declared exceptions, all sound) did not reach it. Sentence
  one of 6.8 is byte-identical attempt-2 text, so the gap is inherited; attempt 3 rewrote that
  frame, which made it the moment to close it for free.

Consequential file edits, same commit: the change table's 4.9 row (117/+54/8.06 -> 120/+57/8.27),
the fact-trace 4.9 row, a new 6.8 row in the rate-in-the-line table, and its "THREE lines"
tally corrected to FOUR. Aggregate timing columns deliberately NOT hand-recomputed — handoff §4
already orders a programmatic recount. **Budget the build against 6,425 chars, not 6,422.**

## Verified TRUE — the one closure the expansion claimed

4.4 «अब देखिए कि उसी तीन परसेंट पर दस हज़ार महीने में क्या आता है…» — the rate is now spoken
inside the same sentence as the derived figure, not merely in the neighbouring clip and the
frame. Arithmetic re-derived: ₹40,00,000 x 3% / 12 = ₹10,000, matching 4.3. Frame keeps
`AT A 3.0% WITHDRAWAL RATE · ILLUSTRATIVE`. Both limbs of the constraint hold. Real closure.

## Independence re-fetch (figures inside the ten)

- **RBI FY27 CPI ~5%** (5.17): staging's businesstoday.in AND business-standard.com are both
  DNS-dead from this host (`EREFUSED`). Recovered on **Forbes India**, also recorded in staging:
  "lowered its CPI inflation projection to 5 percent from 5.1 percent", repo 5.25%, MPC
  3-5 Aug 2026, announced 5 Aug 2026. CONFIRMED, matching the frame's foot exactly.
- **5.17's added MECHANISM** (next year's ration costs more, so the draw rises): confirmed
  **PRIMARY** — Trinity 1998 PDF read this run, p.19: *"To counteract the effect of inflation,
  the dollar withdrawal in a given year must be increased by the inflation rate for that year."*
  The most at-risk added sentence turned out to be the best-sourced one.
- **4%** (5.12): Trinity PDF read direct, Tables 1-3 carry the 3%-12% grid; the added clause
  claims only that repetition made it *sound like* a rule, which is staging A.1's own framing.
- **3.0%** (3.6, 4.4): SSRN 403'd for the fourth stage running. freefincal re-read direct and
  independent — "IWR < 3.5% … the corpus is likely adequate". CONFIRMED on the band.
- **Tax exists** (4.9): all four AMC SWP pages 403'd; §112A surface read — 12.5% above
  ₹1.25 lakh/FY, holding period over 12 months. Confirmed that tax exists, and it is exactly
  what killed the unconditional form of the claim.

**No new number, decimal, date or rate entered the cut.** 3.5, 5.3, 6.4 and 6.11 speak no
figure at all; every figure in the other six was already spoken elsewhere and already traced.

## Gate checks

1 numbers trace + survive re-fetch **PASS after E1** · 2 char budget **PASS +1.07%** (6,425
against `(510 − 81 × 0.8) × 14.281 = 6,357`; 4.4 hand-counted at exactly 119 codepoints, so the
table is trustworthy) · 3 hook **PASS, not re-litigated** · 4 no product/platform **PASS** ·
5 currency purity **PASS** (`$` and the banned word grep to zero, re-verified) · 6 no cite refs,
no bare Latin digits in VO **PASS** · 7 persona **PASS** (all signposts imperative; 3.5's «मई»
is the month, not «मैं») · 8 layout lints **PASS** (no chip rows in the ten; only chapter 1
declares cascades; red never on India's 3.0%, amber never on the imported 4%; the hi storyboard
does not exist yet, so there is no colour table to argue with).

## Carried forward

1. Both recorded RBI hosts are now unreachable. Repoint the staging row before promotion.
2. SSRN 403'd for the fourth stage running — primary read still owed on the 3.0-3.5% band.
3. All four AMC SWP pages now 403. Re-source first if 2.2 or 4.9 is ever strengthened.
4. Char total 6,422 -> 6,425. Programmatic recount owed at build (handoff §4).
5. Re-voice is still **exactly ten clips**. E1 changes 4.9, already on the list; E2 is a cue.
   No eleventh call. Cost stays 290 -> 300 of 350.
6. Cannot run `pipeline_check` — no Bash by contract. The orchestrator runs it and owns `mark`.
