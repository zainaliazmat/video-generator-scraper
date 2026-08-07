# fin-script — passive-income-number, cut `en`, attempt 2 (STYLE E RESTYLE)

**Result:** ok · **Artifact:** `vault/videos/passive-income-number/script-en.md`
**Date:** 2026-08-07

## What this attempt was

**A restyle, not a rewrite.** Attempt 1 passed `fin-audit` (with three VO edits). The creator
then picked style E for both cuts after a listening test
(`run.json.style_decision`, 2026-08-07). Facts, chapter boundaries, beat order, the ladder and
every number are attempt 1's, unchanged. **Only the voice of the writing changed.**

## What was read, in the ordered sequence the brief gave

1. `studio/voice-tests/passive-income-number/style-E-en-teacher-curiosity.txt` — chapters 1
   and 2, creator-approved, **taken verbatim as chapters 1 and 2 and not altered by one
   character**. Chapters 3–6 restyled to match their register.
2. `vault/videos/passive-income-number/script-en.md` (attempt 1) — facts, chapter structure,
   beat order, numbers, cues.
3. `vault/videos/passive-income-number/run.json` — `constraints` + `style_decision`.
4. `vault/videos/passive-income-number/facts-staging.md` — every number still traces here;
   **nothing new was introduced.**

Also: `vault/CLAUDE.md` · `tools/format.json` (cuts.en, tiers.medium, scene, chapter_design,
layout) · `vault/knowledge/video-studies/passive-income-number.md` ·
`vault/knowledge/us-english-script-style.md` · `vault/skills/long_form_scripting.md` ·
`logs/fin-script-en-1.md`.

**`script-hi.md` was NOT read, NOT waited for, and is not mirrored.**
`haryanvi-hindi-script-style.md` and `india-finance-market.md` were not read — wrong lane.

## Output

- **81 lines / 6 chapters / 8,002 chars.** Estimated runtime **520.2s (8:40)** against the
  510s target = **+2.0%**.
- Chapters 1+2 = 23 lines / 2,311 chars (the approved style-E draft, verbatim).
  Chapters 3–6 = 58 lines / 5,691 chars (restyled).
- Per-scene timing table included (chars → est s at 17.57 c/s, +0.8s lead-in/tail per line).
- Every VO line numbered `<chapter>.<n>` under a `## Chapter <N>` heading — verified 81 line
  keys, and **zero bare Latin digits in any VO line** (the only digit-bearing `>` lines in
  the file are guard blockquotes).

## The budget, and the formula that changed today

```
(510 − lines × (lead_in + tail)) × chars_per_second
(510 − 81 × 0.8) × 17.57 = 445.2 × 17.57 = 7,822 chars
```

`cuts.en.chars_per_second` **changed to 17.57 today** (was 16.1), and the corrected formula
was used — not `target × rate`, which would have licensed 8,961 chars, ~17% long. The draft
is 8,002, **+2.3% over the char budget and +2.0% over the runtime target**, inside ±5%.

The attempt-1 "two-rate hedge" section is **deleted**, not carried: the trap is RESOLVED for
`en` (one of the three measurements in the new key is this cut's own attempt-1 audio, 17.588).
The file keeps one line noting the ordering rule still applies to `cuts.hi`, whose 13.03 was
measured on the retired voice.

**The line ceiling moved from 120 to 144 chars** — at 17.57 c/s, `max_scene_seconds` 9.0
minus 0.8s padding is 8.2s of VO = 144 chars. The 120 was correct at 16.1 and is now
needlessly tight.

## The four style-E moves, and where each one lives

1. **What-if open.** 1.1–1.4: the phone's silence is the promise, its single buzz the payoff.
   Side effect worth recording — **it fixed the fifteen-second gate for free**: the deposit
   at 1.3 opens 8.7s and closes 12.8s, where attempt 1's promise closed at 15.1s and was
   accepted at its boundary (`run.json.hook_gate_hi` records the equivalent hi decision).
2. **Signposts** — 15 across 81 lines, ~1 per 5 lines, all imperatives so no first person
   enters: *Notice this* (1.4) · *Think of it this way* (2.2, 5.5) · *understand where it
   comes from* (2.3) · *Now watch what it buys* (2.10) · *Work it through* (2.12, 3.3, 4.2,
   5.15) · *Notice what changed* (2.15, 5.9) · *Now understand* (3.10) · *Notice what that
   is* (4.4) · *Go back to the tank* (4.7) · *Now go back to the day* (6.11).
3. **The tank pays off twice.** 2.2 plants it. **4.7–4.8 is the callback**, so the yield-trap
   warning arrives as a return to a picture the viewer already holds — and because 4.7 lands
   at **4:47**, the callback is what opens the 55–65% mid-video drop zone, which is the
   strongest available form of "never a flat transition". **5.5 is the second callback**
   (same tank, but this route may only take what the tank hands you). 4.13's closing rule
   was re-pointed at the tank too ("a smaller price is a smaller tank").
4. **Stepped arithmetic.** Every rung is yearly → monthly → division, each on its own line:
   2.11/2.12/2.13 · 3.2/3.3/3.4 · 3.6/3.7/3.8 · 4.1/4.2/4.3 · 5.14/5.15.

## The one accuracy trap the tank created, and how it was closed

The study's sharpest finding is that twin B **conflates a 4% dividend yield with the 4%
safe-withdrawal rule**. A careless tank callback would repeat that error — "twelve percent
empties the tank" reads as *a yield is a withdrawal rate*. The lines are written to avoid it:
an advertised twelve percent is **"a promise about the tap"** (4.7), the papers **"tested how
fast a tank drains"** (4.8), and the reason a big yield is a warning is that **the tank
shrank** because the price fell (4.10, 4.13). Nothing says a high yield *is* a high
withdrawal rate. A guard blockquote above chapter 4 states this so a later edit cannot undo
it silently.

**Consequence, and the one fact that moved:** attempt 1 spoke the S&P's long-run **4.21%**
mean dividend yield at old 4.9 — a second spoken "four percent" fifteen seconds from the
withdrawal rate, which is the conflation in audible form. It is now **screen-only**, in the
foot of 4.11 alongside the 13.84% maximum. The fact is not dropped; it moved to the frame.

## The binding constraint: every corpus figure speaks its rate

fin-audit caught **three lines on attempt 1** where the frame carried the rate and the VO did
not — old 5.6, 6.7, 6.8. All three are fixed, and all fourteen corpus lines were re-read one
at a time. The script carries a line-by-line table of the check (2.13, 2.14, 3.4, 3.8, 4.2,
4.3, 5.7, 5.8, 5.11, 5.15, 5.16, 6.7, 6.8, 6.9). **4.3 also carries the derived income**
($5,000/month) with the rate in the same line, per the 2026-08-07
`derived_income_carries_assumption` extension.

## Retention beats, re-measured on the new line lengths

Promise 1.3 at 8.7–12.8s (inside gate 3) · packaging promise 1.7 at **0:29** (was 0:33) ·
first figure 2.3 at 1:00 · **rung one 2.13 at 2:09 = 24.8%** · hero pair 4.2/4.3 straddling
halfway at 49.1–50.4% · **tank callback 4.7 at 4:47 opens the drop zone** · yield mechanism
4.9 at **4:57**, straddling the 5:00 mark both twins independently chose · **~70% reward 5.7
at 6:08 = 70.7%** · rung five 5.15 at 6:59 · callback 6.11 at 96.3% · single terminal CTA
6.13 at 98.6%, zero mid-roll.

## Three judgement calls worth flagging to fin-audit

1. **Rung one now lands at 24.8%, at the edge of the 8–25% band** (was 21.9%). That is the
   real cost of style E's chapter 2, which runs 15 lines against 13 because the tank and the
   stepped arithmetic both live there. Accepted rather than trimmed: the tank is what makes
   every later rung legible, and the first corpus still arrives far earlier than either twin
   does in runtime-equivalent terms.
2. **Line 2.2 is 155 chars → a 9.6s scene, over `max_scene_seconds` 9.0.** It is
   creator-approved verbatim and it is the line that plants the tank, so it was not cut.
   **Build handoff item 6 requires TWO `data-framings` on that scene** (wide on the tank,
   then a push to the tap) — the continuous-zoom mechanism applied inside one scene. It is
   the only line over the 144-char ceiling.
3. **Two lines were dropped from attempt 1's chapters 3 and 5 to hold the budget** — old 3.5
   ("A car normally takes money out of the month…", the rung-two *what changed* beat, whose
   work 2.15 and 3.9 already do) and old 5.9 ("Neither number is wrong…", covered by the new
   5.9 and 5.12). No fact left with either. Old 4.7 ("The number on the screen is usually
   real…") was folded into 4.9 rather than cut.

## Contract compliance

- **US rewrite, not a translation.** Dollars only; **the Indian cut's currency glyph does not
  occur anywhere in the file** (grep-verified) and does not occur in this log. US throughout:
  BLS Consumer Expenditures, the Labor Department, a US grocery checkout, a fuel pump, US
  mailboxes, a suburban street, twenty-dollar bills, 1930s US archival frames.
  `script-hi.md` was not opened.
- **Every number traces.** The fact-trace table maps all 23 figure/claim groups to
  `facts-staging.md` A.1, A.2, C.2, C.3 and PART D, with HARD/SOFT/COMPUTED/CONVENTION tags,
  plus a row stating that the tank carries **no figure and asserts no measurement**.
- **Staged traps obeyed, individually.** Morningstar naming trap (report year ≠ retiree
  year) · the Pfau conflict (no country count spoken or shown; Japan's 0.26% only) · the
  SCHD/VYM decimals ("about three percent"; VYM absent) · the 3.7× ratio shown, never spoken.
- **Persona rules.** No "I", no "we", no credential claim, no fund/stock/index/account pick.
  The style-E signposts are imperatives precisely so the teaching register does not smuggle
  in a host persona. No ticker on screen or in VO.
- **Digits spelled out in VO**, initialisms too ("the S and P five hundred", "the Labor
  Department"); `S&P 500`, `BLS`, `AAII` are screen-only.
- **VO in the VO block only.** All on-screen text English and subset-safe: `ROUGHLY 4 TIMES`,
  `ABOUT 1%`, `DIVIDED BY`, `·` — no multiplication glyph, tilde or arrow, **and no question
  mark** (2.2's tank line is set on screen as a statement for exactly that reason).

## Owed / risks for the next stage

1. **fin-audit must be re-run in full.** `audit-en.md` is attempt 1's and is now stale — 81
   lines against its 78, new numbering throughout, and chapters 1–2 are entirely new prose.
2. **fin-voice-en must re-run: 81 calls.** The 78 attempt-1 Brian clips are dead (right
   voice, wrong script). `budget.elevenlabs_calls` reads 156 against a 350 ceiling; bump it
   after the run — the counter was already missed once on this slug.
3. **fin-storyboard-en must re-run.** Line numbering shifted everywhere from 2.2 onward, the
   tank is a new recurring subject needing four distinct frames (2.2, 4.7, 4.8, 5.5), and
   6.11's callback now points at the 1.1 nightstand and 1.4 phone rather than a coffee maker.
4. **The visual half of the study is still MISSING, not faked.** No keyframes, no hook
   frames, no on-screen-text read, no LOW autopsy. `study.py --ids JiuVKaO2a6c Jn3N9OzSY1c`
   once cookies exist would answer the question that is literally our binding constraint:
   how a corpus number is shown on screen with its rate.
5. **BLS CE 2024 was never read direct** (bls.gov 403'd; consistent across three BLS-owned
   surfaces via search index). It is the denominator of four of the five rungs.
6. **vidIQ credits: 13 remain** until the 2026-08-29 reset, against a ~35-credit close-out
   packaging budget. The title options are keyword-front-loaded so a title lock can be
   deferred without re-writing the script.
