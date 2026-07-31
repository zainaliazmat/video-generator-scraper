---
summary: fin-audit gate one for first-lakh-first-thousand, cut en, attempt 1. PASS with three script edits; every load-bearing figure re-fetched from its recorded source independently of facts-staging.md.
updated: 2026-07-31
source: independent re-fetch of the recorded source URLs (BEA Personal Income and Outlays June 2026, FDIC national-rates-and-rate-caps, federalreserve.gov openmarket.htm, BLS wkyeng Q2 2026 via BLS-owned surfaces, Fed SHED 2025, officialdata.org S&P 500) + re-derivation of every COMPUTED row in facts-staging.md §2.3
stage: fin-audit, cut en, attempt 1
---

# audit-en — first-lakh-first-thousand

PASS

Edited script-en.md. **fin-voice-en and everything downstream must re-run against the
edited file** — one VO-bearing change (6.3), so the pipeline hash will not match.

## What was re-fetched (the independence rule — staging was NOT trusted as evidence)

| Figure in the script | Re-fetched from | Verdict |
|---|---|---|
| **2.7%** national personal saving rate, June 2026 (4.6, 4.7, 4.8, 6.6) | bea.gov/news/2026/personal-income-and-outlays-june-2026 — read direct | **survives**, verbatim: "Personal saving was $646.1 billion in June, and the personal saving rate … was 2.7 percent", released 30 Jul 2026. Script's `foot:` matches the release exactly |
| **0.38%** FDIC national rate, savings deposits (8.8) | fdic.gov/national-rates-and-rate-caps — read direct | **survives** — 0.38% savings, 0.65% money market, 4.38% cap, as of 20 Jul 2026. This was the row most exposed to a plausible-looking injected regulator line; it is real |
| Fed target range **unchanged since 11 Dec 2025** (4.10) | federalreserve.gov/monetarypolicy/openmarket.htm — read direct | **survives** — last change 11 Dec 2025, −25bp to 3.50–3.75%. No later row exists, so "has not moved since December of twenty twenty-five" is correct as of today |
| **$1,251/wk** median usual weekly earnings, Q2 2026 (6.2) | bls.gov/news.release/wkyeng.nr0.htm **403'd to direct fetch** (same as in the pay-yourself-first run); figure confirmed on BLS's own release index ("Usual Weekly Earnings Summary — 2026 Q02 Results") and BLS_gov's own post stating $1,251 for Q2 2026 | **survives** — BLS-owned surfaces only, no aggregator relied on |
| **~4 in 10** could not cover **$400** (6.3) | Fed SHED 2025 (issued 13 May 2026) | figure survives (63% could, unchanged from 2024) — **wording did not.** See kill #1 |
| **~10%/yr** market shape (2.4, 2.5, 2.6, 3.2, 3.6, 5.5) | officialdata.org/us/stocks/s-p-500 (Shiller dataset) — read direct | **survives as shape only** — 10.69% nominal / 6.81% real since 1957. Script speaks "about ten percent a year", shows `~10%/yr` and foots `≈10% nominal / ≈7% after inflation since 1957`. No decimal spoken or shown anywhere. Correct handling of a row that is HARD on shape and SOFT on every decimal |
| Munger, "the first $100,000" (5.8) | no primary reachable, exactly as staging said | quote survives as SOFT colour; **its on-screen presentation did not.** See kill #2 |

### COMPUTED rows re-derived here, not taken from staging

Ordinary monthly annuity, $800/mo, monthly compounding — every staged integer reproduces:

- First $10,000: 12.5 at 0% (exact, $10,000 ÷ $800) · at 10%, month 12 = $10,052 → **12** ✓
- Second $10k: at 10%, month 10 = $19,172, month 11 = $20,131 → **11** ✓
- Tenth $10k ($90k→$100k): at 10%, month 6 = $99,495, month 7 = $101,125 → nearest is **6** ✓
- Crossover: $9,600 ÷ 0.10 = **$96,000** ✓, and $96,000 ÷ $10,000 = 9.6 → "ten times further out" ✓
- 2.7% of $4,000 = **$108/mo**; $10,000 ÷ $108 = 92.6 mo = **7.7 yrs**; at 10%, n = 68.9 mo = **5.7 yrs** ✓
- Thesis ratio: 6.5 ÷ 0.5 = 13× → spoken as "more than ten times", never as an exact multiple ✓

Spot-recount of the char table: 1.1 counts 88 against 88 claimed, 5.3 counts 22 against 22,
7.7 counts 127 against 127. The estimate is honest, not padded.

## Killed / rewritten

**1. `6.3` — a verified figure attached to a test the source did not run. VO rewritten.**
Draft: *"And four in ten adults say they could not cover a four hundred dollar emergency
**with cash**."* The SHED question measures who would cover $400 *"exclusively using cash,
savings, or a credit card paid off at the next statement"* — cash **or its equivalent**.
The 37% complement belongs to that test, not to a cash-only test. Attaching a regulator's
number to a stricter test than the regulator ran is the failure this gate exists for, even
though it happens to understate. Now: *"…could not cover a four hundred dollar emergency
**with cash or its equivalent**."* On-screen `stmt:` and `foot:` widened to match (the foot
now carries the SHED definition). +9 chars. Also dropped "say they" — SHED derives the
share from what respondents would do, it is not a self-report of inability.

**2. `5.8` — a paraphrase presented on screen inside quotation marks. Marks removed.**
Draft `stmt:` was `"The first $100,000 is the hardest — after that you can ease off the
gas."` — quotation marks plus a named attribution reads as verbatim Munger. It is not:
the reported wording is *"the first $100,000 is a bitch"*, the profanity was correctly
dropped for a monetised cut, and **no primary is reachable at all** (no transcript, no
recording, no verified page in *Damn Right!*). Quote marks on a SOFT, primary-unreachable
attribution manufacture a citation. The VO was already clean — it uses indirect speech
("Munger's famous line was that…"), which is the staging-sanctioned form. Only the screen
block changed, so this costs no TTS. Now unquoted, and the foot says **PARAPHRASE — no
quotation marks, no year, no venue**.

**3. `8.10` — an authority appeal with no authority behind it. Deleted.**
`foot:` read "The sequence practitioners describe — an ordering, not a product pick".
No staging line supports "practitioners describe"; it is a source-shaped phrase with no
source, on screen, in a monetised finance video. The disclaimer half of the foot does all
the work on its own. Now just "An ordering, not a product pick".

**Housekeeping in the same pass:** char cells updated for 6.3's +9 (per-scene 90→99,
Ch6 865→874, total 7,648→7,657, budget check −6.9%→−6.7%, frontmatter 8:18→8:19). The
seconds columns are ±10% budget estimates that Build handoff §4 recounts programmatically;
they were not hand-chased beyond the two directly affected cells. Also corrected the
script's own false claim that *"the word 'I' appears nowhere"* — it appears in the
Chapter 6 title, quoting the viewer's objection, which is not a persona breach but was
worth not lying about.

## Checked and clean

- **Char budget.** Per-scene table sums to 7,657 (recounted chapter by chapter and matched
  against the chapter table row for row). Budget is 510 × 16.1 = **8,211**; the draft is
  **−6.7%**, inside ±10%.
- **Hook payoff.** 1.1 promises the 12.5-month figure in the first sentence with no
  greeting and no title card; 1.2 lands the "six months" payoff at ~11.2s on the flat
  16.1 chars/s rate (~13.0s if the en rate is treated as pause-exclusive, which the
  format.json note says it is not). Inside 15s either way.
- **No product or platform.** No bank, brokerage, fund, index fund, app or platform is
  named anywhere. 2.10 explicitly denies that any of them helps at this stage; 8.8's
  0.38% carries "Price evidence, not a recommendation" on screen; 8.11's category note
  says "a category, not a product". Notably 2.4 uses "now **suppose** that same money is
  sitting in the stock market" — the corrected, non-imperative form, i.e. fin-script
  carried forward the exact fix the hi audit had to make by hand.
- **Currency purity.** Zero `₹` glyphs (U+20B9) in the file. The words "rupee"/"lakh"
  appear only in the meta warning and the "deliberately not used" section, never in a VO
  line or an on-screen block, and no line draws a cross-market equivalence.
- **VO hygiene.** Zero bare Latin digits across all 92 VO strings — every figure is
  spelled out ("twelve and a half", "two point seven percent", "twenty twenty-five").
  The only `(N:N)`-shaped string in the file is the runtime "(8:19)" in prose, not a cite
  ref and not in VO.
- **Persona.** No host persona, no first-person expertise, no stock/fund/product pick.
  Second person throughout. The "growth" rung at 8.10 is an ordering, not an allocation.
- **Layout lints.** 92 cue blocks against 92 VO lines. Zero scenes carry both `stmt:` and
  `num:` — one focal element per scene by construction, with `foot:` as the permitted third
  size. swiss-band forbids chip rows outright and none appear, so `max_chips_per_row` /
  `max_chip_chars` cannot be breached. Tightest cue spacing: 5.3 at 1.4s with two cues
  (0.5s + 0.8s = 1.3s, fits with 0.1s to spare) and 2.5 at 2.5s with three cues (2.1s,
  fits). No cascades declared, none needed.
- **Colour table vs thesis.** `--fund` green is defined as "the mechanism that works
  without you once it exists" — **not** "returns doing the work", which is the definition
  the hi cut had to have corrected. Every green scene fits that reading, including the
  tenth-$10,000 scenes (3.6, 3.8, 9.6) where the mechanism genuinely is compounding, and
  5.10 whose whole job is to deny that returns take over at the first milestone. The
  palette argues *for* the thesis. Minor looseness: 1.7/1.8/1.9 are `--target` amber while
  the declared amber list names only rates and thresholds; the three are the rate/threshold
  *questions*, so it reads, and nothing recolours.
- **Aperture sequence.** B 57 · C 18 · R 9 · M 8 = 92. The C-R/C-L alternation is perfect
  across all 18 column scenes starting C-R. The cut opens on B with its first R at scene
  five, so it does not sync with the hi cut's cycle.
- **Chapter start times.** The nine chapter runtimes sum forward to exactly the stated
  starts (0:00 → 8:18 pre-edit); internally consistent.
- **The trap facts-staging §4 flagged** ("do not call the first milestone the crossover")
  is stated out loud and corrected four times — 5.6, 5.10, 5.11, 9.7 — with ~$96,000 /
  $100,000 on screen against $10,000.
- **Rejected rows stayed rejected.** No 4.15% APY anywhere on screen or in VO, no market
  decimal, no Munger year or venue, no SCF-2022 "average savings by age" figure, no 22%
  APR, and $83,730 median household income is correctly left out so the $4,000 worked
  example cannot read as a national median.

## Carried forward for fin-build (not script defects)

1. **Rounding is NEAREST month, not `ceil`.** Re-derived above: the tenth $10k at 10% is
   $99,495 at month 6 and $101,125 at month 7 — staging takes 6, the nearer one, and a
   `ceil` build would print 7 against a voice saying "six". Same trap the hi audit pinned.
   12.5 is exact by construction ($10,000 ÷ $800) and must render `12.5`, never `13`.
2. **Extraction hazard.** The ⚠ admonition near the top of script-en.md is a `>`
   blockquote; a naive `grep '^>'` would ship "NEVER a rupee, a lakh…" to ElevenLabs and
   burn calls. Key off the `**N.N**` headers, as Build handoff §1 specifies, and keep the
   byte-for-byte reconstruction gate.
3. **ElevenLabs budget.** 86 (hi, spent) + 92 (en) = 178 of 200. 22 spare. Single failed
   clips only; a full-chapter re-cut on either side blows the run.
