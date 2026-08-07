# fin-script — passive-income-number, cut `en`, attempt 1

**Result:** ok · **Artifact:** `vault/videos/passive-income-number/script-en.md`
**Date:** 2026-08-07

## What was read

`vault/CLAUDE.md` · `vault/videos/passive-income-number/run.json` (constraints block, binding) ·
`vault/videos/passive-income-number/facts-staging.md` ·
`vault/knowledge/video-studies/passive-income-number.md` ·
`vault/knowledge/us-english-script-style.md` · `vault/skills/long_form_scripting.md` ·
`tools/format.json` (cuts.en, tiers.medium, scene, chapter_design, layout, colors) ·
`vault/knowledge/design-chapter-archetypes.md` (archetype vocabulary) ·
`vault/videos/japanese-money-methods/script-en.md` (**deliverable shape only**) ·
`tools/pipeline_check.py` (which rate the drift check uses).

**`script-hi.md` was NOT read, NOT waited for, and is not mirrored.**
`haryanvi-hindi-script-style.md` and `india-finance-market.md` were not read — wrong lane.

## Output

- **78 lines / 6 chapters / 7,620 chars.** Estimated runtime **535.7s (8:56)** against the
  510s target = **+5.0%** at the `format.json` key, **492.2s (−3.5%)** at the measured rate.
- Per-scene timing table included (chars → est s at 16.1 c/s, +0.8s lead-in/tail per line).
- Longest line 119 chars (7.4s VO + 0.8 = 8.2s, under `max_scene_seconds` 9.0). Shortest 41.
  Self-imposed ceiling **120 chars/line**. Average scene 6.87s vs `target_scene_seconds` 6.5.
- Every VO line numbered `<chapter>.<n>` under a `## Chapter <N>` heading — verified 78
  matches on `^> [A-Z]`, zero VO lines over 120 chars, zero bare Latin digits in any VO line.

## The hero pair, and the anti-bait-and-switch construction

The title promise is the dividend framing; the honest answer is that dividends-only is the
expensive way to buy the same paycheck. Both are delivered, in that order:

- **1.7 (0:33)** speaks the exact format-twin phrase, so the packaging promise is confirmed
  inside the hook and the viewer is never asked to wait for a different video.
- **4.2–4.3 (4:15–4:30 = 47.6–50.4%)** — $1,500,000 at a 4.0% withdrawal rate = $5,000/month.
- **5.6 (6:07 = 69.9%)** — the same $5,000/month from index dividends alone, at the ~1.08%
  yield, needs about $5,555,556. This is the ~70% reward beat, and it is the video's answer
  to its own title rather than a twist away from it.
- **5.8** — "roughly four times", shown rounded and never spoken as "three point seven",
  because 3.7 is a quotient of two SOFT decimals (staged instruction, obeyed).
- **5.10–5.11** gives the third route (a high-dividend asset class at about three percent,
  $1,929,260) so the answer is a menu of three rates, not a single verdict.

## The rate discipline — where both twins failed

The study's central finding is that Dark Ledger states 4% once and then ships **six bare
numbers**, and that twin A states 5% well and then projects at 7% into "financially free at
50". This script re-speaks the rate in the **VO line** and puts it in the **frame** on all
fourteen corpus scenes: 2.11, 2.12, 3.4, 3.9, 4.2, 4.3, 5.6, 5.7, 5.11, 5.15, 5.16, 6.7,
6.8, 6.9. Build handoff item 9 names them so a dropped `foot:` cannot pass silently.

**Zero ages anywhere.** No rung carries one, no line converts a corpus into one, and the only
sentence in the file about stopping work early is Trinity's own verbatim warning to withdraw
**less** (3.15–3.16, `facts-staging.md` PART D).

**No return promise.** 2.7 marks 4.0% as "a finding with a date, not a promise about your
money"; 4.4 says the operation out loud ("It is division… No forecast, no market call, no
promise"); 6.1–6.5 states on the record that the rate is **not settled** and gives three
sourced answers (Morningstar 3.9% for a 2026 retiree, Bengen's own 4.7%, Pfau's international
result) before the recap. That admission is the Von Restorff beat.

## The one judgement call worth flagging

**The brief puts rent/mortgage at rungs 4–5 in the 50–85% band. BLS housing is $2,189/month,
which is below the $5,000/month hero** — placing it after the hero makes the ladder descend,
and a descending ladder kills the only escalation this format has. Housing is therefore
**rung 3** at 3:22 (37.4%), and the 50–85% band carries rungs 4 and 5, the two rungs that
actually sit above it ($1,500,000 and $1,963,375). Flagged in the script under "The ladder,
and why it ascends in this order". Every other beat is in its briefed band.

Second, smaller call: the rungs are priced from **published BLS Consumer Expenditures 2024
line items** (food $10,169 · transportation $13,318 · housing $26,266 · total $78,535) rather
than from the twins' invented bill sizes. Each rung is therefore `a sourced annual bill ÷ a
sourced rate`, which closes the twins' weakest link and lets the one staged US survey do the
work of five separate claims.

## The rate-key hedge

`format.json` carries two disagreeing truths: `cuts.en.chars_per_second` = 16.1, and
`cuts.en._chars_per_second_trap` recording **two** independent flat measurements above 17.3
(17.73 and 17.39), with "fix the budget formula FIRST, then the rate" and "DO NOT raise this
key on its own". The formula fix is applied (padding subtracted from the target before the
rate: `(510 − 62.4) × 16.1 = 7,206`). The key was not changed — `tools/` is not writable here.

Budgeting at 16.1 alone gives 7,206 chars → **469s** at the measured rate, 8% short.
Budgeting at 17.73 alone gives 7,936 chars → **555s** at the key's rate, 9% long.
**7,620 is the overlap**: 535.7s at 16.1, 492.2s at 17.73 — under ±5.1% either way. The table
making this explicit is in the script under "The two-rate hedge"; build handoff item 5 asks
the build stage to measure the real flat rate and, if it lands near 17.7 a third time, fix
the key with the measurement rather than re-padding scripts.

## Contract compliance

- **US rewrite, not a translation.** Dollars only; the Indian cut's currency glyph does not
  occur in the file, nor in this log. US throughout: BLS Consumer Expenditures, the Labor
  Department, a US grocery checkout, a fuel pump, US mailboxes, a suburban street, twenty-
  dollar bills, 1930s US archival frames. `script-hi.md` was not opened.
- **Every number traces.** Fact-trace table maps all 24 figure/claim groups to
  `facts-staging.md` A.1, A.2, C.2, C.3 and PART D, with HARD/SOFT/COMPUTED/CONVENTION tags.
  Every computed corpus carries `ILLUSTRATIVE ARITHMETIC` plus its rate in the same frame.
- **Staged traps obeyed, individually.** The Morningstar naming trap (report year ≠ retiree
  year) — screen says "for a 2026 retiree", foot dates the 2025 Edition to 3 Dec 2025. The
  Pfau conflict — **no country count spoken or shown**, and Japan's 0.26% is the only country
  decimal used, because it is the only one both surfaces agree on. The SCHD/VYM decimals —
  "about three percent", VYM absent entirely (staged NOT USABLE). The 3.7× ratio — shown, not
  spoken.
- **Persona rules.** No "I", no "we", no credential claim, no fund/index/account pick —
  verified by grep across all 78 VO lines. Twin A's otherwise-reusable assumption sentence
  ("we will use X as our conservative working number") is rewritten to "four percent is the
  working number here". No ticker appears on screen or in VO; the high-dividend row is
  described as an asset class with its data source in the `foot:`, per the japanese-money-
  methods audit precedent that a disclaimer under a recommendation is still a recommendation.
- **Digits spelled out in VO**, initialisms too — the VO says "the S and P five hundred" and
  "the Labor Department"; the screen says `S&P 500` and `BLS`. `AAII` is screen-only.
  On-screen numerals carry the exact figures.
- **VO in the VO block only.** All on-screen text English, subset-safe: `ROUGHLY 4 TIMES`,
  `ABOUT 1%`, `ABOUT 3%`, `DIVIDED BY`, `·` — no multiplication sign, no tilde, no arrow.
- **One terminal CTA at 6.13 (98.5%), zero mid-roll** — third independent confirmation of
  that line; twin B, the higher-reach video, has zero CTAs at all.

## Retention architecture

Promise inside 1.3 (opens 12.0s, closes 15.1s — inside gate 3, and both twins are outside
it) · packaging promise confirmed 1.7 at 0:33 · first number 2.3 at 0:53 (an origin, not a
corpus) · rung one 2.11 at 1:57 = 21.9% · hero pair 4.2–4.3 straddling halfway · **yield trap
4.8 straddling 5:00**, the absolute minute both twins independently chose · drop zone 55–65%
opens on the yield mechanism and the Depression frame, not a flat transition · ~70% reward
5.6 at 6:07 = 69.9% · callback 6.11 at 96.0% · single CTA 6.13 at 98.5%.

## Owed / risks for the next stage

1. **The visual half of the study is still MISSING, not faked.** No keyframes, no hook
   frames, no on-screen-text read, no thumbnail read, no LOW autopsy. Every framing decision
   in the cues above is inferred from transcripts plus our own shipped design system.
   `study.py --ids JiuVKaO2a6c Jn3N9OzSY1c` once cookies exist would answer the one question
   that is literally our binding constraint: **how a corpus number is shown on screen with
   its rate.**
2. **6.7 speaks the rungs as fractions** ("a quarter of a million", "a third of a million",
   "two thirds of a million") while the frame carries the exact figures. Deliberate — the
   digit-soup alternative is unlistenable and this is the third recorded ASR digit-loss
   lane — but fin-audit should confirm the rounding reads as rounding, not as a new claim.
3. **BLS CE 2024 was never read direct** (bls.gov 403'd; the figure is consistent across
   three BLS-owned surfaces via search index). It is the denominator of four of the five
   rungs. Same posture as the BLS weekly-earnings row already banked, and flagged here
   because this script leans on it harder than any prior cut.
4. **vidIQ credits: 13 remain** until the 2026-08-29 reset, against a ~35-credit close-out
   packaging budget. The title options above are written keyword-front-loaded so a title lock
   can be deferred without re-writing the script.
