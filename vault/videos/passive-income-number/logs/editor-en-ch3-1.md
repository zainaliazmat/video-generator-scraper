# editor · passive-income-number · en · chapter 3 · attempt 1
VERDICT: REWORK

Reviewed from the encode (`renders/DRAFT-ch3.mp4`, 2899 frames / 96.601s / s24–s39) plus a
rebuilt sheet. Every luminance figure below is MY OWN measurement off the mp4 (4fps sample,
held window = scene start +0.6 to end −0.55, full-frame luma), not a number I was handed —
the run has missed six predictions and I was told not to trust one more.

## Re-measured, and it reproduces the handoff

| scene | dur | median | p10 | p90 |
|---|---|---|---|---|
| s37 | 7.60 | **22** (last) | **15** (last) | 52 |
| s24 | 3.34 | 23 | 17 | 34 |
| s33 | 4.02 | 28 | 15 | 40 |
| s36 | 6.76 | 28 | 17 | 50 |
| s30 | 7.10 | 30 | 15 | 46 |
| s29 | 6.87 | 33 | 19 | 57 |
| s26 | **8.36 (longest)** | 35 | 20 | 47 |
| s31 | 7.05 | 35 | 24 | 52 |
| s38 | 6.76 | 35 | 20 | 48 |
| s32 | 7.05 | 36 | 21 | 47 |
| s25 | 6.58 | 38 | 27 | 53 |
| s39 | 3.54 | 38 | 19 | 45 |
| s28 | 6.81 | 39 | 24 | 51 |
| s27 | 7.05 | 43 | 31 | 49 |
| **s34 (payoff)** | 7.42 | **45 (#2)** | **36 (#1)** | 55 |
| s35 | 7.05 | 48 (#1) | 17 | 57 |

s31 35 / 24 and s27 43 / 31 — the invariant breach is closed on the encode, confirmed
independently. **s34 passes all four payoff clauses on my numbers**: sound-off pass ·
median #2 with top quartile = ceil(16/4) = 4 · p10 #1 · step-in s33 28 → s34 45 = **+17**.

## THE REFERRED QUESTION: may a verbatim-conclusion beat hold the floor?

**Ruling: s37's floor is NOT a defect, and I agree with the proposed stopping rule.** Two
independent reasons, both measured:

1. **s37 is neither of the two named frames.** The payoff is s34. The **longest-held scene
   is s26 at 8.355s**, not s37 at 7.598s — I checked, because the brief asked me to. So the
   proposed rule (*a relocated floor is a defect only when the new bottom is the PAYOFF frame
   or the LONGEST-HELD frame*) clears s37 on its own terms, and this chapter is not the case
   that breaks it.
2. **The floor is a shoulder, not a cliff.** s37 22 / 15 against s24 23 / 17 and s33 28 / 15 —
   a **one-point** gap to the next darkest, arriving on a **−6** step out of s36. The s31
   breach was median 7.1 / p10 0.0 with the next darkest around 21, i.e. a **3× outlier**
   arriving on **−52.8**. Those are different objects wearing the same word "floor".

⚠ **One sharpening the CEO should fold in, because this chapter exposes the wording.** As
written the rule turns on 0.76s of VO length: s37 lost the "longest-held" title to s26 by
three quarters of a second, and s26's length is set by how long Brian takes to say line 3.3,
not by argumentative weight. That is the same brittleness the CEO already retired once when
it closed the `#1 of N` payoff rank ("flips on a 1.4-point measurement error"). Propose
adding the outlier clause the measurement above supplies: **the new bottom is a defect when
it is the payoff, OR the longest-held, OR an OUTLIER against its own chapter** — operationally
a gap to the second-darkest larger than the gap between the second- and third-darkest, or an
arrival step worse than the chapter's median step by a wide margin. s31 fails all three; s37
fails none. Without that clause, ch4–7 will each argue about a second of runtime instead of
about whether the frame reads.

Also worth recording against the invariant's own text: s37 IS arguably the chapter's most
substantive beat (the verbatim Trinity conclusion, the script's only sourced sentence about
stopping work early). Read literally, `ground_and_payoff_legibility_2026-08-08` — "the darkest
longest-held frame must be the chapter's most substantive beat" — is *satisfied* by s37, not
breached by it. The clause the s21/s31 blockers actually enforced is the opposite one
(a substantive beat must be legible). Whichever way the CEO wants it, the sentence should be
rewritten to say only one of those things, because right now it says both.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s30 | **blocker** | the chapter's ONE drawn layer sits on **birds on a brick parapet at dusk** — I opened `assets-ch3/final/s30.jpg` at full resolution and there is **no roof, no pitch, no chimney, no building form**: a flat brick coping, seven pigeon silhouettes, an orange sky, and a featureless black void across the lower 55% | Line 3.7 is *"that is a third of everything they spent"* — the third being HOUSING. Cover the type and the frame says **"a third of something"** (the bar) plus **"birds at sunset"** (the photo). The subject the whole scene exists to quantify is absent. fin-build's rule-8 defence is *"a dusk roofline says 'housing' and cannot say 'a third'"* — the art half of that is right and the photo half is not true of this photograph; there is no roofline in it. fin-assets and fin-build BOTH flagged it as the chapter's weakest sound-off fit and referred it here, so ruling it acceptable would be waving through the one thing two agents asked me to rule on | **Re-fetch the photograph only.** Keep everything drawn — the `p-b` plate, `.art-lift`, the y150–760 rect, `housing-share` at 0.334, the tick at 275.48, all three cues (1.55 / 1.90 / 2.50). The declared device is *art-forward → route to the calmest subject*, and that device does not require birds: a **dusk roof pitch with a chimney against sky**, or an **apartment-block facade in silhouette**, is equally calm, keeps the near-black lower band `.art-lift` needs, and names the noun. ⚠ Must not duplicate **s29** (wide warm suburban street, houses, dusk) or **s32** (front porch) — different scale and different ground from both, or it becomes the third housing frame that looks like the first. I am naming a subject, not a file: **needs a new fetch**, nothing on disk verified for this slot |
| 2 | s34 | should-fix | the payoff photograph is a **services contract**, and its words are legible at 1080p: *"…insurance. **The Contractor** will…"*, *"…employment…"*, *"…if warranted) relating to any…"*, *"10. Assignment"*, *"the prior written consent of the C…"* | The frame is captioned *"Cooley, Hubbard and Walz, AAII Journal, February 1998 — verbatim, from the study's own methodology"* and the VO says *"the Trinity study states…"*. §10's letter is met (no title, no figure, no agency name) so this is not a fabricated source — but the legible word on the payoff frame of the chapter is **Contractor**, and a viewer who reads it is reading a commercial agreement while being told they are looking at a finance paper. It is also the frame that has to carry the chapter's strongest evidence claim | Cheapest fix is a **tighter crop or a `bgpos` push** that keeps the pen and the raking light but pushes the clause headings out of frame or below the resolve threshold — the frame is 1733×1300 so there is slack, and the beat is *"fine print with a pen"*, which survives losing the words. Only if that collapses the structure, re-fetch: **journal-style two-column body text**, no headings, no clause numbers. Do NOT re-open the German-Bible or 1040-NR-EZ families already killed |
| 3 | s26 | should-fix | an **aerial car park of ~80 vehicles** under *"that is about eleven hundred and ten dollars a month, all of it: payment, insurance, gas, repairs"* | The line is the running cost of **one** car — the viewer's car, the one s24 just parked outside their building. A drone shot of a full lot says "parking", plural and anonymous, and quietly changes the scale of the claim. The four chips carry the enumeration, so it is not false, just the wrong picture: the storyboard's own cue (*four paper slips fanned on a dashboard — payment stub, insurance card, fuel receipt, repair invoice*) says the line exactly, and it is the chapter's longest scene at 8.355s, so it holds the mismatch longest | Re-fetch to the storyboard's own cue, or any single-car interior/close subject with paperwork in it. Keep the `brule` at 400px and the four chip anchors unchanged — they are correct (see below) |

## Verified clean — the things I was told to check, checked

- **s27 resolves to `$332,950`** on the encode at t=23.4. The sheet's `$317,240` is a mid-count-up
  sample, not a defect. `$13,318 / 0.04 = $332,950` ✓, and `$26,266 / 0.04 = $656,650` ✓ on s31.
- **s26's `brule`** at `top:400px` clears the `$1,110` glyphs completely — confirmed on the encode
  at t=16.0, the rule sits well below the foot line. Fixed.
- **s26's cascade is genuinely speech-anchored.** `chipAt [4.37, 5.01, 5.89, 6.71]` against my own
  `tools/tts/clauses.py --line 3.3 --n 5` run: 4.50 / 5.07 / 5.88 for chips 1–3 (0.13s, 0.06s early
  and 0.01s late), chip 4 inside the final clause. All four chips are up by t=16.0 with **1.6s of
  hold** before the cut. Nothing like hi ch1's 5.07s of dead air. The 0.13s early bias is inside the
  tool's own stated precision — do not "correct" it.
- **s30's proportion is true and it reads.** Measured off the frame at t=40.0: fill 234px of a 684px
  track = **0.342**, tick at 0.334 — matches BLS housing 33.4% of $78,535 in `facts-staging.md` §204,
  and the `50.4%` in the foot is `(26,266+13,318)/78,535`. The yellow block against the ghost track
  clears the fill floor at composed size. `33.4%` is a literal string, not a `countUp` — correct call,
  a rounded `33%` would be a different published figure.
- **s27's `bgpos: center top`** improved the frame, not only the numbers: the whole flush handle and
  its recess are inside the frame with clearance, the door shut-line reads down the left. It IS the
  chapter's emptiest photograph and it is carrying the heaviest type stack — that pairing is right.
- **Rate assert, met ON SCREEN, every instance.** s27 and s31 both carry `AT A 4.0% WITHDRAWAL RATE`
  as a first-class 40px `.sub` **above** the figure plus `ILLUSTRATIVE ARITHMETIC` in the foot; s25 /
  s29 carry the BLS release and date; s26 carries `$13,318 divided by 12 — arithmetic, not a separate
  statistic`; s30 carries the BLS foot. `check_vo_frame passive-income-number --cut en --chapter 3`
  re-run by me: **PASS, 16 scenes**. No bare magnitude in any VO line.
- **Both Trinity quotes are verbatim** against `facts-staging.md` A.2 rows 1 and 2, punctuation included.
- **No repeats.** 16 files, 16 distinct md5s, and zero collisions against ch1 and ch2's finals
  (I hashed all three chapters together). The four-car run s24–s27 is four different objects
  (street / nozzle / lot / handle) and the four-document run s33 / s34 / s35 / s37 is four different
  scales and grounds. s37 is the fifth book-or-paper frame in the cut — **ch4 must not add a sixth.**
- **Craft.** Every kicker at +0.30 (inside the 0.5s gate), `cues.py` 24 cues min gap 1.100s, no type
  collision — s30's foot ends at x≈1110 and the plate starts at x≈1120, tight but clean. s39 carries
  its bare 3.543s duration with `data-framings` equal to it, correct for a chapter tail with no successor.
- **s36 lands.** `30 YEARS` is up and the clock dial is fully legible at t=78.5; the late anchor is
  right and the sheet sampling it bare at +2.6 is not a defect, as the build predicted.

## The two declared judgement calls — ruled

- **s35's 1040 dated 2020: ACCEPT.** The date is legible (`2020`, plus the 2020 virtual-currency
  question) but no line in this chapter makes a year claim, the on-screen copy is
  *"Every rung here is a BEFORE-TAX number"*, and the shape is the current 1040. It reads as
  "a tax form", which is the beat. Note only — if a later chapter ever puts a year on screen next
  to a tax frame, revisit.
- **s30's roof ridge with pigeons: REJECT** — finding 1. This is the one place I am overturning a
  declared call, and the reason is that the declaration rests on a description of the photograph
  ("a dusk roofline") that the photograph does not support.

## What is working

- The rung ladder reads as a ladder: the two `--fund` green corpus frames (s27, s31) are the only
  green in 96 seconds, both carry their rate above the figure, and the 156px / 308px measure bar
  makes rung three visibly twice rung two without a word of copy. Do not touch the scale pair.
- The fine-print run is the best-argued stretch in the cut — s33 → s34 → s35 → s36 → s37 steps
  document → clause → consequence → clock → conclusion, and s36's clock breaking the paper run is
  what stops it becoming one texture. Keep that ordering.
- The invariant fix held on the encode, and it held without the grade, the ground or the scrim being
  touched — s31 went 7.1 → 35 on the photograph alone. That is the ch2 ruling working as intended.
