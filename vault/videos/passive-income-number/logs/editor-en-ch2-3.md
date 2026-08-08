---
summary: fin-editor en ch2 attempt 3 — PASS. Zero blockers. All four changes verified on the ENCODE, not on the claim: s21 reads unmistakably as bread at the tightest ken, s15 says "bound volumes on a library table" sound-off through its whole 1.16x push, s20's kicker is clear of the price-card row, s14's two halves read equal. Two explicit decision-ready recommendations for the CEO: CLOSE the payoff ruling (the 2.7-point #3 closes it, and a rank test is the wrong instrument), and adopt MEDIAN + `p90-p50` + a binary SOUND-OFF QUALIFYING GATE, whose shape and consistency record I set out. One should-fix, carried to ch3+ briefs and explicitly NOT actioned in ch2 — s9, the frame median crowns, is a closed notebook cover with no subject, which is the whole reason the gate has to exist.
updated: 2026-08-08
source: renders/DRAFT-ch2.mp4 (16:44:02) + a freshly rebuilt SHEET.jpg read as a grid before anything else + 13 frames pulled from the encode (s21 85.2/86.5/88.81/90.0 · s15 42.30/43.5/44.34/46.5/48.5 · s20 80.5 · s14 41.0 · s9 2.6 · s13 30.381) · md5 across all 35 finals in en-ch2 plus the en-ch1 and hi-ch2 pools · script-en.md ch2 lines 2.1-2.15 · storyboard cues quoted from the script block · run.json chapters.en.2 read in full + rulings_binding_on_both_cuts.ground_and_payoff_legibility_2026-08-08 + owed.metric_for_most_legible · logs/ceo-en-ch2-1.md · logs/editor-en-ch2-2.md · logs/fin-build-en-ch2-3.md · logs/fin-render-en-ch2-3.md
stage: fin-editor, cut en, chapter 2, attempt 3
---

# editor · passive-income-number · en · chapter 2 · attempt 3
VERDICT: PASS

**BLOCKERS: 0 · SHOULD-FIX: 1 (carried, not actioned here) · NOTES: 2**

Sheet rebuilt from the 16:44 encode and read as a grid, every cell placed beside its VO
line, before any frame was pulled. Thirteen frames then pulled from the **encoded mp4** for
the calls the grid cannot settle. `md5sum` across all 35 finals in `assets-ch2/final/`
**plus** the en-ch1 and hi-ch2 pools: **zero collisions anywhere** — the two new files are
new, and no image is used twice in this chapter or shared with a sibling.

(Note on artifacts: `chapter_sheet.py` writes `SHEET.jpg`; the 16:44 `SHEET-ch2.jpg` named in
the brief is the same 16 cells from the same encode. I read the one I built.)

## The four changes — each confirmed on the frame, none taken on trust

I was told not to assume the third and fourth were as described. I did not assume any of
the four.

**s21, the payoff — CLOSED, and it is the best frame in the chapter now.** Read at 85.2
(the scene's own opening, before the number rises), 86.5, 88.81 and 90.0. Crumb, crust,
flour dust, two cut slices in the foreground, board grain running under them. **Cover the
type and it says food / a loaf / the grocery bill.** The CEO's "green mossy mass … reads as
a rock or a cabbage" is gone at every instant of the ken, including the first. It matches
the storyboard's own written cue (*a single loaf of bread on a bare wooden table, hard side
light, nothing else in frame*) — a cut loaf on a maple board is that cue, delivered.

**s15 — CLOSED, and I am answering the question that was put to me rather than the one the
measurement answers.** Sound-off, THROUGH the ken, not at rest:

- **46.5** — the exact timestamp the CEO called an unidentifiable pale curve — is now an
  open bound volume filling the left half, the recto page curving off the gutter, the text
  block's cut edge visible, and two cracked-spine hardbacks stacked at frame right with the
  frayed page-block edges and a headband readable. Sound-off it says *old bound papers on a
  library table*. That is `PAPER TWO · three Trinity professors published it`.
- **44.34 and 48.5** — same read.
- **42.30, the 1.16× tightest instant** — **it holds, and I agree with fin-render that this
  is its weakest second.** The crop pushes the right-hand stack toward the edge and the pale
  recto dominates; for roughly the first second it reads as *a big pale sheet and something
  stacked beside it* before it resolves to books. **My call: not a defect.** Nothing is
  asserted over it — the statement does not rise until 42.837 and the kicker at 42.30 is
  only `PAPER TWO` — and the frame is unambiguous for 6.5 of its 7.5 seconds. A ken that is
  weakest at its tightest instant and strongest where the claim lands is the ken working.
- Verified against the old failure mode specifically: this is **not** a repeat of s13. s13
  is a bright, symmetric, centred open-book macro that fills the frame; s15 is a dark
  off-centre desk with an open volume left and a stack right. Different scale, different
  light, different composition. Both are in the grid and they do not rhyme.

**s20's kicker — FIXED, and by a different mechanism than the one I prescribed, correctly.**
Read at 80.5. `PER MONTH` now sits on the dark shelf lip with the whole price-card row
**above** it and clear: `REGULAR EGGPLANT $1.99`, `ITALIAN PEPPER $3.99`, `ITALIAN EGGPLANT
$5.99`, `GREEN SQUASH $1.99` all legible, none of them crossing a glyph. **I accept the
correction to my own finding.** I prescribed `.band`; fin-build measured that `.band` starts
at y497 with alpha 0 while the kicker glyphs sit at y438–459, so the mechanism I named could
never have touched the collision I found. The finding was right, the fix was wrong, and it
was caught by measuring before typing rather than after. `background-position: center
bottom` spends cover-slack the composition already had, costs no new layer and no re-fetch,
and the scene still reads as a store. Better than what I asked for.

**s14's bar — FIXED, and here too the reported cause was wrong and the real one is worse.**
Read at 41.0. One track, amber to the midpoint, grey beyond, opaque tick at the split, the
two halves at visibly equal weight with the amber the only chromatic object in the bar. The
frame now says *half, and half* at a glance. **`fade()` had been overwriting the authored
`opacity=".22"` to 1.0 since the layer was drawn** — so my "one opacity line" would have
changed a number that was not in effect, and fin-build proved that by building it and
measuring the identical result. This is the second of the two one-liners to turn out to be a
different defect, and both were found the same way. It is already filed correctly under
`owed.fade_clobbers_authored_opacity` as a scaffold default to fix, not a ch2 workaround to
remember.

## THE PAYOFF RULING — recommendation: CLOSE IT. Do not move s21, s9 or s13.

**The 2.7-point #3 closes the ruling, and not because it is round three.** Four reasons, in
descending order of how much I would fight for them.

**1. The defect the clause was written against is gone and inverted, measurably.** The
clause exists because "light drains off the payoff". s21 was the chapter's floor: last of
fifteen on p10. It is now **#1 on p10 by 3.3 points**, has the **narrowest p90−p50 spread in
the chapter (9.0)** — i.e. it is the most uniformly lit frame here, which is what "legible"
actually means — and **it arrives on a rise**: s20→s21 is **+20.4 median, the largest median
step in the chapter**, where at attempt 2 it was +3, a plateau. That last number is the one
I would put in front of the creator, because it is the only one that describes what a viewer
experiences. A payoff that arrives on the chapter's biggest step up is a payoff that looks
like a payoff.

**2. Sound-off passes decisively, which is the half of the clause I own.** It reads as bread
at the tightest instant of the ken and at rest.

**3. A rank test is the wrong instrument, and this chapter is the proof.** "#1 of N" makes
the payoff frame's compliance a function of **how good the other frames are** — so a chapter
is punished for having two other good pictures, which is the opposite of what anyone wants.
And it is unstable at this resolution: fin-build's composed snapshot and the encode differ
by up to **1.4 points on this very frame**, while the median gaps across the top four are
2.9 / 0.2 / 4.3. **A gate that a 1.4-point measurement error can flip is not a gate.** The
right shape is a band, not a rank.

**4. The two frames above it must not come down — and for different reasons, which is the
answer to the question as it was actually put.**

- **s13 (median 45.2) earns its place and I would defend it.** It is a macro of an open
  journal spread under `PAPER ONE · William Bengen, Journal of Financial Planning`. It is
  the best-matched picture in the entire document run. Darkening it to flatter a rank would
  violate the **first** clause of the same invariant — brightness assigned by argumentative
  weight — in order to satisfy the second. That is not a trade, it is vandalism.
- **s9 (median 45.4) does NOT earn its place, and that is a finding about the metric, not a
  reason to move s21.** See below. Under the qualifying gate I recommend, s9 is not eligible
  to hold #1 at all, which leaves s21 **#2 of the eligible field, 2.7 behind one
  legitimately bright frame.**

**What I recommend the CEO write in place of "#1 of N", binding on ch3–6 (en) / ch3–7 (hi):**

> The payoff frame must (1) **pass sound-off**, (2) rank in the chapter's **top quartile on
> median**, (3) rank **#1 or #2 on p10**, and (4) **arrive on a non-negative median step**
> from the scene before it.

s21 scores **pass · #3 of 15 (top quartile) · #1 · +20.4**. All four, none marginal.
**And this is not a rule written to let en pass:** hi ch2's hero fails (1) and (3) outright
and is being re-sourced, so the reformulation still bites exactly where the defect is.

**Also recommend RETIRING the `≥55 p90` target rather than carrying it as an outstanding
miss.** It is a target on the statistic the CEO is about to rule invalid. In this chapter
p90 crowns s15 at 61.4 — the frame that ranks **#10 of 15 on median** and that both the CEO
and I called a sound-off failure two rounds running. An outstanding miss measured on a
retired statistic is a phantom, and it will read as an unresolved defect in the handover
notes for the next six chapters.

**Concretely: do not re-fetch s21 a third time. Do not darken s9 or s13.**

## THE METRIC — recommendation: MEDIAN + `p90−p50` + a binary SOUND-OFF QUALIFYING GATE

**I endorse fin-render's recommendation in full, including its caveat against itself.** p90
is not merely imprecise here, it is **wrong about the direction of two joints** (s14→s15
reads +18.2 on p90 against +2.3 on median, where one white page enters and nothing
brightens; s15→s16 reads −16.5 against +6.1, where the eye plainly sees the picture get
clearer). A statistic that gets the *sign* of a change wrong cannot rank anything. And p90
structurally penalises evenness, which is exactly what the ruling is asking the payoff frame
to have.

**On the gate — its shape, since that is what was asked of me.** It is binary, it runs
BEFORE the ranking, and it is one question:

> **With the type covered, can a viewer name a concrete object in this frame?**

Not "is it interesting", not "does it match its line" — that is the separate per-line
sound-off test and it is already in my standing rules. Just: **is there a subject.** A
frame that fails is ineligible to be called the most legible, at any median.

**Can I apply it consistently? Yes, and the record is the argument, not my say-so.** It has
produced the same verdict **four times independently, across two cuts, three of them before
anyone asked for a gate**: en s15 at round 1 and again at round 2 (a pale curve — failed),
hi ch2's 11.6s blank-notebook plateau at 59.0 (failed), the old en s21 (failed), and en s9
now. Over the same run, **every purely numerical measure has been overturned at least
once** — p90 by median, source-side mean by composed mean, scdet by everything, and a
composed prediction by the encode. The sound-off read is the only test on this run that has
not been overturned by a measurement. That is the case for making it the qualifier rather
than a tiebreaker.

**The caveat I want on the record with it: the gate is a floor, not a ranker.** It is binary
and it cannot separate two frames that both have subjects — it will never tell you whether
s13 or s21 should be brighter. Do not ask it to. Median ranks; `p90−p50` flags the spiky
frame that median is hiding; the gate only removes the empty ones from contention. Three
instruments, three jobs, and the failure mode of the last three rounds — every measure
eventually crowning an empty frame — is closed by the third.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s9 | should-fix — **carry to ch3+ briefs, do NOT action in ch2** | Read at 2.6 in the encode: a near-featureless dark-amber field, the rounded corner of a **closed** notebook cover, and a pen edge-on at the extreme right. The storyboard cue was *a blank ruled notebook page with a single pencil laid across it* — a ruled page and a pencil are a picture; a cover is a surface. **This is the frame the median metric crowns as the chapter's most legible (45.4, #1 of 15)** | It is the *other* half of the same invariant — "the brightest must not be its emptiest" — and it is only visible now because the metric changed: the CEO's ruling was written on p90, where the two brightest were s16 and s19, both substantive. On median the brightest is a frame with no subject. So this is **new evidence, not moved goalposts**. Graded should-fix, not blocker, for three reasons I want on the record: the CEO measured s9 and explicitly ruled it untouchable in this pass; its p90 57 is the "lighter open" the ch1 gate required, so darkening it would break a live requirement; and line 2.1 (*a number without a rate is a wish*) is a maxim, not a subject, so the sound-off bar is genuinely lower here than on a frame that names a thing | **Nothing in ch2.** The fix is a subject, not a brightness — if it is ever touched it is a re-fetch to the storyboard's own ruled-page-and-pencil, never a grade. What it is actually **for** is the metric ruling: it is the concrete, in-hand demonstration that median alone crowns an empty frame, and therefore the argument for the qualifying gate above |

## Rulings — settled here, do not reopen

- **s15's weakest second (42.19 → ~43.5) is not a defect.** Ruled above, on the frames:
  nothing is asserted over it, and it is unambiguous for 6.5 of its 7.5 seconds.
- **s21's green cast is not "mouldy bread", and I checked rather than assuming.** The frame
  measures R 37.1 / G 41.3 / B 40.9 — a **cool desaturated cast of ~4 luma points**, not a
  saturated green, with B tracking G. It reads as the `--fund` role grade that s18, s22 and
  s23 also carry, which is how a viewer disambiguates it. Not a finding.
- **`Breton 75` at s15 bottom-left is not legible text under §10.** Agreeing with fin-assets,
  fin-build and fin-render, and I looked: ~8% of frame width, below the kicker's own backdrop
  luma.
- **Zero image reuse, verified by md5 across three pools** (en-ch2's 35 finals + en-ch1 +
  hi-ch2), not by filename. Nothing in this chapter repeats and nothing is shared with a
  sibling chapter or the other cut.
- **Drawn art stays at 4, the cap, and all four are untouched** — s14's 0.500 split, s16's
  95/100 grid, s17's two ringed dates, s18's ÷4% = ×25 block. All four still additive under
  rule 8. **Chapters 3–6 must not read four as the new baseline**; §8's budgets (ch3 1, ch4 1,
  ch5 0, ch6 3) stand.
- Carried and re-confirmed on this encode: `s23` carries its bare `7.749`, 16 `data-framings`
  present, the four figure frames carry their four assumptions, `AT A 4.0% WITHDRAWAL RATE`
  and `ILLUSTRATIVE ARITHMETIC` are both legible under `$254,225`, and s20 still has no
  person, no ₹ and no brand mark.
- Not re-reported, per the brief: `.mega`/comma clearance, scdet, dissolve residual, cue
  ladder, `s20→s21` deltas.

## What is working — the next pass must not break these

- **Two rounds running, the fix pass has been cheaper and more honest than the finding.**
  Both one-liners turned out to be different defects than reported, and both were caught by
  measuring the mechanism *before* editing rather than shipping the prescription. `.band`
  could never have reached s20's kicker; s14's `.22` had never been in effect. I got both
  diagnoses wrong and both were corrected on the frame. That habit is worth more to the next
  six chapters than either fix.
- **The payoff now arrives on the chapter's largest step up.** +20.4 median at s20→s21,
  against +3 at attempt 2. Whatever ch3 does to its own hero, do not lose the shape of
  arriving on a rise — it is the thing a viewer feels and no static rank captures it.
- **The rate discipline and the four drawn layers are untouched and remain the standard.**
  Four figure frames, four assumptions in frame; four layers each asserting something its
  photograph structurally cannot. Do not weaken a foot or add a fifth layer to make room for
  anything.
