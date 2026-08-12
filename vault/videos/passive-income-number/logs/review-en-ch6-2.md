# review · passive-income-number · en · chapter 6 · attempt 2
VERDICT: PASS
PASS 1: 0 blockers, 0 should-fix, 2 notes
PASS 2: 0 blockers, 0 should-fix, 3 notes

Sheet built once (`tools/chapter_sheet.py` → `renders/SHEET.jpg`) and read once; both
checklists run against it. Every number below was measured on the ENCODED
`renders/DRAFT-ch6.mp4` (86.037s), never on the browser and never taken from the build log.

## The two round-1 blockers — both VERIFIED CLOSED on the encode

### 1 · s77's five reference rungs — FIXED, and the counter-check the brief demanded is discharged

They are on screen. Measured at 59.12s (s77 +7.14, everything up), bar interiors scanned
row by row against the storyboard's own declared scale (920px = $1,963,375 from x=500):

| rung | figure | measured width | true width | err |
|---|---|---|---|---|
| 1 | $254,225 | **120px** | 119.1 | +0.9 |
| 2 | $332,950 | **156px** | 156.0 | 0.0 |
| 3 | $656,650 | **308px** | 307.7 | +0.3 |
| 4 | $1,500,000 | **702px** | 702.9 | −0.9 |
| 5 | $1,963,375 | **918px** | 920.0 | −2.0 |
| overrun | $5,555,556 | x 500→1919, **1420px visible** | 2603px, 1420 visible | exact |

Max error 2px on a 920px scale. The drawing is truthful to `facts-staging.md` and the
`truth_bar` is satisfied on the artifact that ships, not on the generator.

**⚠ The counter-check — did the fix create the defect in the other direction?
No. `no_return_promise` holds, and it holds mechanically.** s77's emitted SVG, comments
stripped, is **exactly six `<rect>`, zero `<text>`, zero `<line>`, zero `fill-opacity`** —
five `.flf` rungs and one `.flw` overrun, nothing else. There is no ghost track behind the
rungs, no axis, no baseline rule, no tick, no gridline and no numeral anywhere in the layer.
What the device states is the comparison the VO makes and only that: five rungs the viewer
just watched the voice enumerate, drawn to one honest scale, and a sixth that runs off it.
Three things stop it reading as a scale or a projection:

- **There is no time dimension.** The rungs are a ranked list of five named line items
  (groceries · car · housing · $5,000/mo · the average household), each spoken in 6.7/6.8,
  each on its own row. Nothing dates them and nothing sequences them.
- **The overrun is not rung 6.** It is the only red object, it is **h64 against the rungs'
  h40**, and the measured gap from rung 5's bottom (y835) to its top (y880) is **44px**
  against the 20px pitch between rungs. It reads as a different category, which is the
  sentence.
- **Both figures in the ratio are printed in this chapter with their rates** — $1,963,375
  at 4.0% on s76, $5,555,556 at 1.08% in frame here from +1.10, with `ILLUSTRATIVE
  ARITHMETIC` under it.

The colour split does the work review asked for: five green sourced, one red that does not
fit. **This is now the best drawn layer in the chapter, and it was the worst one.**

### 2 · s71 — FIXED, re-measured on the encode as instructed

Opened at full size at 15.86s. The antique foxed volume is gone. What ships is a bright
white/cream page block seen **edge-on**, a vertical curtain of page edges, with four neon
plastic index flags — a modern book somebody has gone through and marked up. It no longer
contradicts `Wiley, August 2025` in its own foot; it now agrees with it.

**§10 re-verified on the encode, not assumed.** Zoomed the magenta flag at 3× and the
orange one: illegible cursive squiggle, no legible word, no figure, no title, no spine, no
brand, no seal. Nothing on the frame impersonates a source.

**s71's ground, on the encode:** `45.225 → 50.190`, rank 6 → **rank 9 of 13**. The build
predicted 24.79 → 31.43 on its own chain and told me to treat it as a direction. Direction
was right, value was not — **nine-for-nine on `predictions_missed_a_sixth_time`.** Direction
is the safe one and nothing downstream moves: the floor, the payoff and the CTA are all
untouched.

## The ground table, re-measured on this encode (same instrument as round 1)

```
 1  s79  38.865   ← floor
 2  s75  38.935   sep 0.070  → TIED with s79 (< 1.0, one clause, any member satisfies it)
 3  s76  40.712   sep 1.777  → EXCEEDS 1.0 → s76 is OUT of the floor
 4  s80  43.920 ·  5  s74  44.131 ·  6  s81  47.751 ·  7  s77  48.072 ·  8  s72  48.230
 9  s71  50.190 · 10  s73  51.540 · 11  s70  52.513 · 12  s69  54.628 · 13  s78  55.966
```

**The instrument reproduces round 1 to within 0.01 on all twelve byte-unchanged scenes**
(s79 38.872→38.865, s75 38.928→38.935, s76 40.704→40.712, s77 47.662→48.072, s78
55.973→55.966). That agreement is the evidence that s71's +4.97 is a real move and not a
second instrument's numbers.

**The floor is the same TWO-member tie it was in round 1** — {s79, s75} at 0.070, s76 out at
1.777. Not reopened, and the forbidden trade (brightening s75, stranding s79 alone) is still
forbidden.

**The invariant is discharged, in the one direction it runs.** The payoff **s77 sits at
48.072, +9.21 above the floor**, and the CTA **s81 at 47.751, +8.89 above it**. Neither beat
this chapter is bound to protect is anywhere near the bottom. s77's figure measures
**4.26:1** at 59.5s at 112px `.huge` — the AA floor for large text is 3.0 — and the rungs
sit 150px below the figure's baseline, so the changed layer cannot and does not touch it.
The payoff-legibility clause passes on the same three limbs it passed on in round 1: rank 7
of 13, unchanged; figure well clear; `countUp` settling 1.215s before the dissolve.

## THE RULING the build routed to me — §4, the s76→s77 ladder stagger

**Ruled: a NOTE, not a defect. Do not fix it. The build was right to leave it and right to
route it.** Sampled at both `qa.dissolve_sample_offsets`, 52.209 (+0.225) and 52.364 (+0.38),
and profiled every green row between y520 and y900 in each.

- At **+0.38 the ladder is already a single clean set** at s77's rows (560/620/680/740/800)
  with no second set at all. The stagger does not survive to the back half of the dissolve.
- At **+0.225** both sets are present. But they share the **same fill, the same left edge
  (x=500) and the same five widths** — the only difference is a 24–64px vertical offset. The
  eye does not read two misregistered ladders; it reads **one ladder settling upward** as the
  camera leaves the barn and arrives at the container. On a device whose whole job is to be
  continuous across three scenes, that is closer to an asset than a defect.
- The visible window is roughly +0.15 to +0.30 — about **four to five frames at 30fps**,
  inside a dissolve where the photograph, the type and the ground are all cross-fading anyway.

**And both available fixes cost more than the thing they fix, which is what settles it.**
Aligning s77's rows to s76's pushes the overrun into y≥920 and through the watermark keep-out
box — a structural violation, not a trade. The 24px half-measure collapses the measured
rung5→overrun gap from **44px to 16px**, which would put the red bar at the same pitch as the
rungs and make it read as **rung 6 of the same series** — and that is precisely the
`no_return_promise` failure the brief told me to guard hardest on this layer. **I will not
trade four frames of a cosmetic vertical settle for a payoff frame where the overrun joins
the series it is supposed to escape.** Left as shipped, deliberately, on the numbers.

## Findings

| # | pass | scene/span | severity | what | why it is not more than this | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s77 | note | the shipped frame departs from the storyboard's §9a wording, which declares the five rungs *"ghosted at ~.2"* | **Recorded so gate two and the creator do not read this as drift.** The `.2` ghost was the storyboard's chosen mechanism for a hierarchy — rungs subordinate, overrun dominant. Under `.has-photo.art-forward .art{opacity:.52}` it delivered ≈0.10 effective alpha and the rungs were absent on the encode, so the mechanism failed its own intent. The shipped frame keeps the **intent** and changes the **mechanism**: hierarchy is now carried by colour (one red among five green) and size (h64 vs h40), and the overrun is still plainly the dominant object. This is the review's own round-1 instruction being honoured, not the build going off-plan. | none |
| 2 | P1 | s75/s76 vs s77 | note | s75 and s76 each carry a 920px `.fl` ghost track behind every rung; s77 carries none | Not an inconsistency that costs anything. On s75/s76 the track states "each rung is a fraction of $1,963,375" — a per-row denominator. On s77 the comparison is rung-set vs overrun, and rung 5 *is* the 920px denominator, so a track would be redundant and (the build's call) closer to an axis. Both readings are true and neither frame asserts a scale. | none |
| 3 | P2 | s70 / s71 | note | `fin-assets` claimed separation on four axes; **three hold on the encode, one does not** | Checked, not assumed, as the brief required. Vertical curtain vs horizontal sweeping spread — **holds.** Textless vs ~40 words of legible prose — **holds.** Edge-on page block vs flat macro of a spread — **holds.** *Cool vs warm ground* — **does not hold**: both are warm cream/amber (encode YAVG 52.513 and 50.190, both under an amber tint). Three axes is ample; the two frames do not twin, and the run is the storyboard's own declared `ONE ANSWER / ANOTHER ANSWER / A THIRD ANSWER` parallelism, which round 1 already settled. Raising it would be a finding about the review. | none |
| 4 | P2 | s71 | note | the amber `4.7%` measures **6.31:1** mean / **3.24:1** worst-5% ground on the encode, against the build's browser prediction of 6.68 / 4.17 | Clears the AA large-text floor of 3.0 (it is 112px `.huge`), and plainly legible at full size — the scrim's centre pull lands it on the page block's shadowed third. Worth logging for two reasons: it is the **ninth consecutive** encode that came in under a build-chain prediction, and **its already-accepted neighbour s70 measures thinner still at 2.53:1 worst-5%** and was never raised in round 1. s70 is not what changed and I am not reopening it — but if a later pass ever tightens this metric, s70 is the frame that fails first, not s71. | none |
| 5 | P2 | s76→s77 boundary | note, **for gate two only** | at +0.38 the incoming `THE DIVIDENDS-ONLY PRICE` kicker paints on the same rows as the outgoing `RUNGS FOUR AND FIVE` / `BOTH AT A 4.0% WITHDRAWAL RATE` | **This is NOT the `japanese-money-methods-hi` stacking-context bug.** Both are clearly partial — outgoing fading, incoming rising at start+0.30 — which is what a 0.45s cross-dissolve is supposed to look like. Logged only so the gate-two sweep has a known-good reading of this boundary to compare against. | none |

## Would I keep watching?

Yes, and the chapter now closes the video the way it was designed to.

**The risk point round 1 named has actually moved.** At ~15s s71 was the second consecutive
book-on-a-table with a coloured percentage over it, and an antique one arguing with its own
line. It is now a bright, high-contrast vertical curtain of marked-up pages — a different
object doing a different thing — and the opening run's luma strip went from a dip-and-recover
(54.6 → 52.5 → **45.2** → 48.2) to a clean monotonic descent (54.6 → 52.5 → **50.2** → 48.2)
into the s73 verdict. That is a better-shaped four scenes than round 1 had.

**I cannot find a timestamp I would leave at, and I am saying that plainly rather than
inventing one.** The nearest thing to a soft spot is still the s70–s72 document run, and it
is the storyboard's declared device, broken on colour and shape by s72 and paid off side by
side at s73.

**The chapter's best 20 seconds are now s74→s77**, and that is the change. The ladder
assembles under the voice across the hold, carries across the dissolve as one settling
object, and then s77 finally does the thing it was drawn to do: five green rungs that fit,
one red bar that leaves the frame. In round 1 that beat arrived as a red smear with nothing
to measure it against. It now lands.

## Regressions vs my last pass

**None.** Checked, not assumed:

- Twelve byte-unchanged scenes reproduce round 1's ground within **0.01 YAVG** — the strongest
  available evidence that nothing outside s71 and s77's rung fill moved.
- The floor's shape, membership and separations are identical (tie at 0.070, s76 out at 1.777).
- s77's figure, band, `vrule`, anchor (+5.59), `countUp` (1.10s) and 1.215s settle are untouched.
- s75/s76 markup is unchanged: same three/five `.flf` rungs, same ghost tracks, `plateKen`
  1.16→1.08→1.00 across the hold, no self-dissolve.
- **NO RAIL** anywhere — thirteen scenes swept, no chapter title, no counter, no slide number.
- s81 is still the cut's one terminal CTA: one `--pop` block, CSS triangle, the sub-line is the
  spoken reason and not an invented promise. It carries its bare duration (7.566, no +0.45).
- `npm run check`: 0 errors, 0 warnings, **15/15 text checks pass WCAG AA**; the nine infos are
  the `.bg inset:-8%` ken window and `known_benign` is still `[]`.

**Round-1 finding 3 (pulling `s77-foot` from +6.39 to ≈+5.0) was declined by the build with
arithmetic, and the decline is correct.** +5.0 leaves 0.59s to the +5.59 anchor and +5.59
leaves 0.00 — both under `layout.cue_min_gap_seconds` 0.8. +6.39 *is* the floor. It was a note,
the binding assumption is in frame from +1.10 and holds the whole scene, and I withdraw it.

## What is working — the next pass must not break these

- **The drawn layer is now the chapter's strongest asset and it is honest.** Five rung widths
  truthful to within 2px of the real figures, six rects, no text, no axis, no track, no tick,
  no numeral. Do not add a label to it, do not add a track to it, and do not align it to s76.
- **The rate discipline is complete and survived the rebuild.** Every figure carries its
  assumption in frame — `EACH AT A 4.0%` (s75), `BOTH AT A 4.0%` (s76), `AT A 1.08% DIVIDEND
  YIELD` (s77) — each with `ILLUSTRATIVE ARITHMETIC`, and s70/s71/s72 each carry a full
  provenance foot.
- **Ground temperature moves and the moves land on the turns**: warm-red admission (s69) →
  amber evidence (s70/s71) → red verdict (s73) → green ladder (s74–s76) → red payoff (s77) →
  the chapter's one neutral immediately after it (s78) → warmest frame in the video for the
  callback (s79) → green meaning (s80) → orange CTA (s81). Not a flat strip.
- **The s75/s76 HOLD is correct and is not a repeat** — s75 is a derived 1.469× crop of s76,
  one continuous pull-back across 15.4s.
