# editor · passive-income-number · en · chapter 3 · attempt 2
VERDICT: REWORK

Reviewed from the current encode (`renders/DRAFT-ch3.mp4`, 03:35, 96.601s, s24–s39) plus a
rebuilt sheet, with the two changed photographs re-opened at full resolution and the s30
composite measured pixel-by-pixel off the mp4. `npm run check` re-run by me: **0 errors,
0 warnings, 14/14 AA, motion 0 errors.** 16 files, 16 distinct md5s — still no repeat.

## The three attempt-1 findings, ruled

**Finding 1 (s30, blocker) — the SUBJECT is fixed. The COMPOSITE is not.**
The incoming photograph is what I asked for and it closes the sound-off failure: a slate
roof running across the lower half, three brick chimneys, a clapboard gable — cover the type
and the frame says HOUSING. It is also not a duplicate of s29 (wide dusk street, houses at
distance) or s32 (white porch and steps): three different scales, three different subjects,
confirmed on the sheet and by hash. **That half of the finding is closed.**

But the fix moved the defect rather than removing it, and it moved it into the drawn layer —
see finding 1 below. This is the failure mode I was explicitly asked to check for and it
reproduces.

**Finding 2 (s34, should-fix) — the build attempted it, measured it, and stopped with cause.**
I read the whole rationale and re-checked its load-bearing claim: the sharp band carrying
every legible word occupies rows ~430–900 of 1300, i.e. dead centre, so a 16:9 full-width
`bgpos` window contains it at both extremes and is a genuine no-op. Only a zoom crop excludes
the words, and the pen lies in the same plane. The (b)-family crop that loses the words is a
soft grey field with no nameable object — the exact shape the CEO's rationale of record kills.
**The refusal is correct and I am not re-asking for it.** Kept as a should-fix below because
the words are still legible on the payoff frame, but it does **not** block this attempt and I
am not requesting action on it this pass.

**Finding 3 (s26, should-fix) — closed.** The aerial car park is gone; the frame is now a
tread-and-sidewall macro of a single tyre. One car, not eighty, so the scale no longer argues
with "the running cost of one car", and the four chips still carry the enumeration. Legible
at t=16.0, `$1,110` clean, `brule` clear. Note only, below.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s30 | **blocker** | `.art-lift`'s panel now renders as a **visible hard-edged grey rectangle floating in the sky**. Measured on the encode at t=41.0: left edge at **x=1120**, luma **47 → 31** across one pixel; top edge at **y=150**, **35.3 → 25.5**; bottom edge at **y=760** cutting across the roof. The panel is 860×610 and the bar inside it is 720×120, so ~80% of the box is empty grey | `.art-lift` is `linear-gradient(140deg, rgba(13,16,23,.66), rgba(13,16,23,.34))` on `.plate-in` with **no feather on any edge**. It was invisible over the outgoing near-black dusk frame; over the incoming daylight sky it is a translucent grey card with hard corners parked in frame right for **7.1 seconds**, on the chapter's only drawn moment. That is `chapter-design.css`'s own disqualifier in its own words — *"reads as a mistake, not as a layer"* — and I saw it on the first full frame I opened, before I measured anything. It was introduced by the attempt-1 fix, so it is squarely this pass's to close | **Feather the panel edge** — add transparent stops (or a `mask-image`) to `.has-photo.art-lift .plate-in` so the darkening falls off instead of terminating on a line. ⚠ `art-lift` has exactly **three users**: this scene, `en-ch2` s16, and `hi-ch3` s28 (I grepped). Over ch2 s16's dark ground a feather should be a **no-op**, so fix it at the class and it also lands on hi-ch3 before that ships — but **re-sheet ch2 and confirm s16 is unchanged**; if it moves, scope the softening to `#s30-pin`. ⚠ **`bgpos` cannot fix this and must not be spent on it:** the source is 1880×1253, cover scale 1.0213, so there is **0px of horizontal slack** and 199.7px of vertical — sliding the photograph changes what the box sits over, never that the box has edges. ⚠ **Do not re-fetch the photograph.** It is the right picture and it is the second fetch on this slot |
| 2 | s34 | should-fix | payoff photograph still resolves `9. Insurance`, `The Contractor`, `10. Assignment`, `the prior written consent of the` at 1080p, under a foot citing *Cooley, Hubbard and Walz, AAII Journal, February 1998* | A viewer who reads the frame is reading a **services agreement** while being told they are looking at a finance paper. §10's letter is met (no title, no figure, no agency name), so it is not a fabricated source — it is a mismatch on the frame carrying the chapter's strongest evidence claim | **No action required this attempt.** The crop lever is measured dead (see above) and the only remaining lever is a re-fetch — journal-style two-column body text, no headings, no clause numbers, and it must land at **p10 ≥ 80** to keep payoff clause 3, against today's 92.1. Worth one fetch if fin-assets is opening the pool anyway; not worth a dedicated pass. Do NOT re-open the German-Bible or 1040-NR-EZ families |
| 3 | s30 | note | the ghost track's 100% end lands at **x=1910 of 1920** — 10px from the frame edge | It does terminate visibly (luma 52 → 21 at x=1910, verified), so the denominator IS bounded and the proportion reads. But 10px is inside any safe margin and on a phone it will read as running off, which weakens "a third of **everything**" | **Leave it.** `.p-b` is the shared archetype rect and moving it moves every B scene in every chapter for 10px. Recorded so the next reviewer does not re-derive it. The check's `panel_out_of_canvas #s30-pin right 60px` is this same declared geometry, not a new defect |
| 4 | s26 | note | the frame is now an extreme tread macro — a **surface**, where the storyboard cue was four paper slips on a dashboard (an object that enumerates) | Not a defect: it says "car", it says "one car", and the chips do the enumerating. But it is a texture on the chapter's longest scene (8.355s), and ch2's CEO carry-forward asked this chapter to open on subjects rather than surfaces | Accept for this cut. Flag only so ch4 does not add a second texture-macro at length |

## Verified clean this pass

- **The drawn layer still tells the truth against the new ground, and it still reads.** Measured
  in the bar band y405–505: fill RGB **(89, 63, 22)** amber vs ghost **(64, 61, 58)** neutral —
  +25 R of hue separation, so fill and remainder separate on colour even though they are only
  5 luma apart. Fill 1190→1430 of a 1190→1910 track = **0.334**, tick at 275.48. BLS CE 2024
  housing 33.4% of $78,535 confirmed against `facts-staging.md` §204. `33.4%` still a literal
  string, not a `countUp` — correct, a rounded `33%` would be a different published figure.
- **s30 is not a duplicate of s29 or s32** — checked on the sheet, at full resolution, and by md5.
  The chapter does run four consecutive residential exteriors (s29 street / s30 roof / s31 door /
  s32 porch), but they are four different objects at four different scales, the same device the
  s24–s27 car run uses. Not a finding; ch4 should not extend the run to five.
- **s26 resolves the scale error without breaking anything it was carrying** — `brule` still clears
  the `$1,110` glyphs, all four chips up with hold before the cut, AA unaffected.
- **No regression anywhere else.** s27 `$332,950` and s31 `$656,650` both resolve; the two `--fund`
  greens are still the only green in 96 seconds; both Trinity quotes still verbatim; s39 still
  carries its bare 3.543s tail duration.

## What is working

- The rung ladder still reads as a ladder — s27 and s31 are the only green frames, both carry
  `AT A 4.0% WITHDRAWAL RATE` above the figure, and the 156px/308px measure bar makes rung three
  visibly twice rung two without copy. Do not touch the scale pair.
- The fine-print run (s33 → s34 → s35 → s36 → s37) is still the best-argued stretch in the cut,
  and s36's clock breaking the paper run is what stops it becoming one texture. Keep the ordering.
- s30's photograph is now the right photograph. The fix below is to the panel behind the bar,
  **not** to the picture — the next pass must not swap this file.
