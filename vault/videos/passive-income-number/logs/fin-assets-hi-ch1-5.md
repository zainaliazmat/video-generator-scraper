---
summary: s5 (ch1, hi) — the storyboard's "three household bills" spec queried properly for the first time, twice, 12 candidates. Zero cleared. INCUMBENT JARS KEPT (YHIGH 160, R−B +61.8); route B drawn art is the fix.
updated: 2026-08-07
source: fin-assets attempt 5, chapter 1, hi cut. One slot, no promotion.
---

# fin-assets — passive-income-number / hi / chapter 1 / attempt 5

**Scope: s5 only, and nothing was promoted.** s1–s4, s6, s7 not read, not
re-fetched, not re-picked. `manifest.json` was edited twice to drive the two
sheets and **restored to its incumbent value**; it is byte-identical to how
attempt 4 left it. `s5.jpg`, `s5.jpg.src` and `CREDITS.txt` were never touched.

## Decision

**KEEP the jars photograph.** Two sheets, 12 candidates, **0 accepted.** This
is not a "ran out of attempts" keep — every candidate has a named, measured or
visible reason, and the two that cleared both numeric gates were the worst of
the twelve on meaning.

## The gates, and the incumbent's own numbers

Measured with `ffprobe signalstats` (YHIGH) + a 32×32 downsample mean (R−B).
The method reproduces fin-editor's ch1 figures exactly — s5 **+61.8** (editor
+61.7), s7 **+43.6** (+43.6), s2 **+14.6** (+14.6) — so the two stages are
reading the same instrument.

| | YHIGH (≥110) | R−B (≥ ~+40) | width |
|---|---|---|---|
| **incumbent `s5.jpg`** | **160** ✓ | **+61.8** ✓ | 1880 px ✓ |

The incumbent is the **warmest raw in the chapter** and passes both gates with
room. Whatever it fails to say, it does not fail either measurable thing, and
it is the second-brightest-ceiling warm frame ch1 has.

## Sheet A — `electricity bill and rent receipt on a wooden table@pexels`

The editor's literal first suggestion. 6 of 6 cells rendered.

| cell | what it is | YHIGH | R−B | call |
|---|---|---|---|---|
| 1 | woman face-down on a desk, laptop, calculator, US notes | 230 | **+12.9** | reject — warmth, **US $**, identifiable face under a money claim |
| 2 | hands, calculator, **$5 + $1 bills**, orange receipts | 210 | **+31.0** | reject — warmth, **US $** |
| 3 | a **US $20 bill** and receipts on white | 218 | **+5.8** | reject — warmth, **US $** |
| 4 | pink calculator on white ledger paper | 227 | **+29.3** | reject — warmth; sound-off says "doing sums", not "quietly paid" |
| 5 | laptop + scattered receipts, grey office | 217 | **+0.5** | reject — dead neutral, institutional |
| 6 | woman at an office desk reading a slip | 198 | **+12.9** | reject — warmth, face, office |

**0/6.** Every cell clears YHIGH trivially (white paper always does) and
**every cell fails R−B** — best was +31.0 against a +40 gate. Three of six
carry US dollars on a ₹ video.

## Sheet B — `utility bills and envelopes on a wooden table warm light@pexels`

The editor's second variant, plus the chapter's warmth adjectives (standing
instruction #2). 6 of 6 cells rendered.

| cell | what it is | YHIGH | R−B | call |
|---|---|---|---|---|
| 1 | hand sliding **US $100 notes** into a black envelope, on wood | 159 | +39.6 | reject — **US $**; and "cash into an envelope" is not a household bill |
| 2 | man holding a sheet stamped **`PAST DUE`** in red, crumpled paper | 222 | +32.9 | reject — warmth, and it **contradicts the line** |
| 3 | same shoot: man on a sofa, beer can, `PAST DUE` on the table | 223 | **+49.4** ✓ | **reject — contradiction.** Passes both gates and says the opposite of the VO |
| 4 | white marble flatlay, **US coins**, envelopes, green calculator | 228 | +0.8 | reject — warmth, **US $** |
| 5 | same shoot again: crumpled bills, beer can, red `PAST DUE` | 222 | **+56.7** ✓ | **reject — contradiction.** Warmest cell of all twelve |
| 6 | hands holding a black envelope stuffed with **US $100s** | 169 | +32.6 | reject — warmth, **US $** |

**0/6.** Cells 2, 3 and 5 are one Nicola Barts photoshoot (Pexels 7926672 /
7926641 / sibling) returned three times. It is a *can't-pay-the-bills* shoot:
a red `PAST DUE` stamp, crumpled paper, a beer can. VO 1.5 says a corpus
**चुपचाप भरता रहता है** — quietly keeps paying them. A `PAST DUE` stamp under
"Electricity. Ration. Rent." is the sound-off test's gate 2 in its purest
form: **a contradicting frame is worse than a bland one**, and this one would
have passed both numeric gates. Promoting cell 5 would have looked decisive
and shipped the chapter's worst frame.

## The structural finding — why this slot is not photographable

Worth carrying forward, because it is the reason a third attempt would also fail:

1. **Neither pool indexes "a bill" as an object. Both index it as an emotion.**
   Twelve candidates across two distinct queries returned exactly three
   scenes: *stressed at a desk with a calculator*, *`PAST DUE` on the sofa*,
   and *cash going into an envelope*. The storyboard's actual spec — three
   household bills fanned on a table, no person, no verdict — is a styled prop
   shot that does not exist in these libraries. Round 1's "paper stack" and
   round 2's jars were not lazy queries; they were the two nearest things that
   do exist.
2. **White paper cannot clear a warmth gate.** Paper is the most neutral
   surface in stock photography, so any frame it dominates collapses toward
   R−B 0 — 9 of 12 cells landed under +33 regardless of how warm the wood or
   the lamp was. The only two cells that cleared +40 did so because a *sofa
   and a person* filled the frame, not the bills. The R−B gate and the
   "bills on a table" spec are close to mutually exclusive on stock.
3. **"bills" is a currency magnet.** 5 of 12 cells carried US dollars from
   queries that never mention money — the same failure mode as
   first-lakh-first-thousand's bitcoin props. Naming the denomination is the
   documented fix, but here there is no ₹ denomination to name: the subject is
   an *invoice*, not a note.

So the reach-for-it condition in `format.json vector_art.lottie` is met on the
merits, not as a consolation: **1.5 is a COUNT of three obligations and a
PROCESS**, and no photograph of it exists to be found.

## Handoff

- **Nothing changed on disk.** `manifest.json` restored; `s5.jpg` (md5
  `ebc3f7deece1f8617296d466b2164221`) is the same file the last render used, so
  no re-fetch, no re-encode of anything upstream is implied by this attempt.
- `python3 tools/pipeline_check.py check assets --slug passive-income-number
  --cut hi --chapter 1` → **PASS assets-hi**. All 7 slots present, every one
  with its CREDITS row; 7 distinct md5s, none colliding anywhere in `studio/`.
- **Route B is now the fix, not the fallback.** fin-build should amend §7's
  `art` column for scene 5 from `off` to the drawn layer the editor specified:
  three marks (bulb / jar-or-sack / house-or-key) taking a tick in sequence on
  the statement beat, inline `<svg class="icon">` + `draw()` per
  `vector_art.icon_first`, using the existing `assets/icons/checkbox-tick.svg`.
  The jars carry *ration* and the warmth; the drawn layer carries the **count
  of three** and the **verb**, which is precisely what no cell in twelve could.
- The `_cand/s5.jpg` sheet on disk is **sheet B** (sheet A was overwritten by
  the second run); both are described above in full.
