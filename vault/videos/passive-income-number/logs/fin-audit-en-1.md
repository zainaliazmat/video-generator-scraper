# fin-audit — passive-income-number, cut `en`, attempt 1

**Result:** ok (PASS **with 3 edits to the script**) · **Date:** 2026-08-07
**Artifacts:** `vault/videos/passive-income-number/audit-en.md` (full evidence) ·
`vault/videos/passive-income-number/script-en.md` (**edited** — 5.6, 6.7, 6.8, plus a
timing note under the budget table and a `stage:` line in the frontmatter)

## What was read

`vault/CLAUDE.md` · `run.json` (constraints block, binding) · `script-en.md` ·
`facts-staging.md` · `knowledge/video-studies/passive-income-number.md` ·
`logs/fin-script-en-1.md` · `tools/format.json`.
`.env` not read. Nothing under `.claude/` or `tools/` written. No Bash, no git.

## Sources re-fetched independently of facts-staging (the independence rule)

Trinity 1998 **primary PDF** (byline, Feb 1998, pp. 16–21, Table 3, both verbatim quotes,
1926–1995, 15/20/25/30) · Bengen 1994 review **PDF** (title, JFP, Oct 1994, 50/50,
1926–1966, ~30-yr worst case) · multpl (1.04% today, mean 4.21, median 4.19, max 13.84%
Jun 1932, min 1.08% Jul 2026) · stockanalysis SCHD (3.11% TTM, $1.05, quarterly) · keilfp
Morningstar (3.9%, 2026 retiree, 30-yr, 90%, 30–50% equity, 2025 Edition 3 Dec 2025, prior
3.7%) · retirementresearcher Pfau (JFP Dec 2010, Japan 0.26%, 19 countries 1900–2010) ·
fool.com Bengen (4.7%, SAFEMAX, *A Richer Retirement*, 55/40/5, ~400 start dates).

**403s worked around, not waved through:** bls.gov, the BLS archive PDF and FRED all 403'd,
so the entire CE 2024 set was confirmed on `randalolson.com/2026/03/26/household-spending-2024/`
— **$78,535 · housing $26,266 (33%) · transport $13,318 (17%) · food $10,169 (13%) ·
housing+transport $39,584 = 50%**, all six matching, plus BLS's own X post carrying $78,535.
advisorperspectives 403'd → Bengen's 4.7% recovered from fool.com. gurufocus 403'd — its
1.082% is on screen but is **not** load-bearing (the VO says 1.08 and every dividends-only
corpus divides by 0.0108, which multpl confirms direct).

**Near-miss worth recording:** Wikipedia — a staged source for the Bengen row — gives
**pp. 14–24**, contradicting the script's **pp. 171–180**. An independent search returns the
standard citation *Vol. 7, Issue 4, pp. 171–180*. **The script is right and Wikipedia is the
outlier.** One keystroke from a wrongful kill; logged so the next run does not re-litigate it.

All 14 corpus quotients re-derived by hand — **every one exact to the dollar**, and both BLS
shares (33.44%, 50.40%) reproduce off the published totals to two decimals.

## What was killed

**fin-script's handoff claim — "all fourteen corpus scenes carry the rate in the VO line and
in the frame" — is false, and its own suggested check pointed the wrong way.** It asked me to
look for a dropped `foot:`. **No `foot:` is missing; all 14 frames are clean and the binding
`withdrawal_rate_on_screen` constraint passes 14/14.** The rate was dropped from the
**spoken** half at **5.6, 6.7, 6.8** — the video's answer to its own title at the 69.9%
reward beat, and the entire recap (five bare corpora in two sentences). That is the study's
Dark Ledger failure reproduced exactly: the rate falls out once repeating it feels redundant.

Rewritten in place, no fact/beat/structure changed, all ≤120 ch, longest scene 8.2s < 9.0:
**5.6** +"at about one percent" · **6.7** +"At four percent," · **6.8** +"Both at four
percent." Net **+34 ch → 7,654** (+0.4%). Derived timing tables deliberately **not**
hand-patched — the build recounts programmatically; a note under the budget table says so.

## Gates

1 ✅ · 2 ✅ (7,654: **+6.2%** vs the padding-corrected 7,206, **−6.8%** vs the naive 8,211 —
inside ±10% on both readings of the disputed rate key) · 3 ✅ (promise recomputed
independently: opens ≈11.9s, closes ≈**14.5s** at the slow key — **~0.5s margin, chapter 1
must not grow**) · 4 ✅ (no ticker/fund/broker/account anywhere) · 5 ✅ (zero `₹`) ·
6 ✅ (all 78 VO lines digit-free; the only `^> .*[0-9]` hits are rule-box prose above
`# THE SCRIPT` that never reaches TTS) · 7 ✅ (no I/we/my/our in any VO line) ·
8 ✅ (zero scenes carry both `num:` and `stmt:`; cascades 4/4/3 ≤ 5; colour argues **for**
the thesis — `--warn` on every dividends-only corpus and the yield trap).

Run-specific: rate-with-every-corpus **fixed** · zero ages in the file · no "forever", no
accumulation math · 4% rule attributed with four documented criticisms, three of them the
papers criticising themselves · title promise spoken at 0:33 and paid at 69.9%, premise not
dismissed · **housing-at-rung-3 deviation approved** (the briefed order would make the ladder
descend across its own climax; as shipped it is strictly monotonic and "biggest line in the
budget" does not contradict rungs 4–5, which are not budget line items).

## Owed / risks for the next stage

1. **Voice work must re-run against the edited script** — the pipeline hash-checks it.
2. **Three non-blocking build notes** (in `audit-en.md` §4): `·` separates clauses at 2.12
   and 4.8 and must not render as chips (36 and 29 ch vs `max_chip_chars` 22); the 4-item
   cascades at 1.6 and 3.3 must stack, not land as one row of four; 3.3 and 6.7 should pin an
   explicit cascade gap.
3. **Extraction hazard:** the rule box uses the same `>` marker as VO lines. `^> [A-Z]`
   excludes it by coincidence of formatting, not by guarantee — **do not skip build handoff
   item 1's byte-for-byte reconstruction check.**
4. **Unverified this run, retained and recorded:** GuruFocus 1.082%; "Wiley, August 2025" and
   "worst case still October 1968" in 6.3's `foot:`. Citation garnish, not load-bearing.
5. **Study debt unchanged** — the visual half is still MISSING, so how a corpus number is
   shown on screen with its rate (literally the binding constraint) is still unobserved.
