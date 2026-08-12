# review · passive-income-number · en · chapter 6 · attempt 1
VERDICT: REWORK
PASS 1: 2 blockers, 0 should-fix, 2 notes
PASS 2: 0 blockers, 0 should-fix, 2 notes

Sheet built once (`tools/chapter_sheet.py`) and read once; both checklists run against it.
Everything below that carries a number was measured on the ENCODED
`renders/DRAFT-ch6.mp4`, never on the browser and never from the build's rank table.

## Findings

| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | s77 | blocker | the five reference rungs of `ladder-overrun` are invisible on the encode | The overrun bar reads (mean RGB `(61,30,31)` against a `(22,20,28)` ground — ΔRGB ≈ 40, and it does run off the right edge: sampled at x=1900, y=890 it is still bar). The five rungs it must be measured against do NOT: `.fl` at `fill-opacity .2` under `.has-photo.art-forward .art{opacity:.52}` is ≈ 0.10 effective alpha of `--ink`, measured ΔRGB 6–10 against the gap immediately above each bar (contrast 1.07–1.09:1). A viewer sees one red band with nothing to compare it to. Rule 8 is the additive test: with no visible reference, the layer asserts no proportion and no comparison — and this is the chapter's payoff frame and the third of the three forward-referenced ladder layers `container_ladder_2026-08-09` builds toward. | Give the five reference rungs on s77 the SAME fund-green `.flf` fill they carried on s75/s76 — they are literally the same five bars the viewer just watched fill in, and the colour split then also encodes "five sourced, one that does not fit". Re-measure on a rendered frame; target a bar-vs-gap ΔRGB comparable to the overrun bar's ≈40, not a contrast ratio (on a dark field the ratio sits near 1.0 even for the green bars that plainly read on s76). ⚠ Do NOT reach for `.art-lift` here: the overrun bar reaches x=1900, so s77's plate spans the frame and `art-lift` would be the forbidden whole-frame darkening wearing a plate-scoped name. |
| 2 | P1 | s71 | blocker | the photograph is an antique, foxed, hand-bound volume with browned deckled pages, under a foot in the same frame reading `Wiley, August 2025` | The picture contradicts the text beside it, in one frame, at full size (sampled 17.5s). The beat's whole content is that Bengen revised his number UP, recently; a 19th-century-looking book says "old book, old rule" and inverts it. **This escaped `fin-assets`** — it is a selection defect, not a build defect, and worth recording as evidence that the early gate missed one. | Needs a NEW fetch: a modern hardback with a dust jacket and clean white pages, on a table, warm lamp — a book that could plausibly have been printed last year. I have not opened a replacement candidate, so I am naming no file. |
| 3 | P1 | s77 | note | the foot (`roughly four times the total-return figure` / `ILLUSTRATIVE ARITHMETIC`) lands at +6.39 and holds 1.52s before the dissolve | Not a `derived_income_carries_assumption` failure — the binding assumption `AT A 1.08% DIVIDEND YIELD` is in frame from +1.10 and holds the whole scene, verified at 58.2s (mid-countUp, figure reading `$4,523,986`) and at 59.5s. But it is the thinnest-held string in the chapter, on the payoff frame. | If finding 1 touches this scene's ladder anyway, pull `fade("#s77-foot", …)` from +6.39 to ≈ +5.0. Do not move the anchor at +5.59; it is measured. |
| 4 | P1 | s70 | note | ~40 words of legible corporate-governance body prose on the stand-in document, carried forward by `fin-build` as this stage's call | **Settled here: keep as shipped, no action.** Zoomed on the encode at 8.0s and 12.0s the legible fragments are "…an evolving area", "restore investor confidence", "proactive in seeking reform", "qualified independent…" — generic prose with no agency name, no seal, no title, no brand and no figure, so it impersonates no source and trips no clause of the invented-source rule. The offered free re-pick's only text-free alternative would have made s70 a near-twin of s81's closed notebook, which trades a non-defect for a real repetition finding. | none |
| 5 | P2 | s70–s72 | note | three consecutive `arch-C` frames — a photographed document, a centred figure, the same register — running 6.5s to 26.4s | This is the pass-2 flat-stretch signature, and it is where I would leave. It is NOT raised higher because it is the storyboard's own declared `ONE ANSWER / ANOTHER ANSWER / A THIRD ANSWER` device: the parallelism is the argument, s72 already breaks it on colour (`--warn`) and shape (a statement, not a number), and s73 pays all three off side by side. Asking for a different archetype here would be a finding about the review. | none required. Fixing finding 2 (a modern book against s70's paper-on-wood) already widens the visual gap inside the run. |
| 6 | P2 | s77 | note | cross-chapter, for assembly only — NOT a defect of this chapter | ch6's payoff object is a steel shipping container in a yard; s75/s76 are wooden crates in a barn. ch5's s61 (`ROUGHLY 4 TIMES`) is being re-fetched right now toward four-crates-against-one. If s61 lands as wooden crates, the ch6 rhyme partner is metal, not wood, and the rhyme lands on scale rather than material. | Information for whoever locks s61. If it is cheap there, prefer a re-fetch whose object family carries to a large steel container. Nothing to change in ch6. |

## The two things the build handed forward — both settled here, on the encode

**1 · s77's payoff-legibility clause — MEASURED PASS, no action.**
The build predicted median rank 5 of 13, 1.21 behind the quartile cut, and declared two of
four limbs failing. Measured on the encode (mean `YAVG`, three samples per scene at 0.35 /
0.55 / 0.75 of each scene's own duration), s77's ground is **47.662, rank 7 of 13**, above the
chapter median (45.225) and **8.79 above the floor**. The figure itself measures **4.86:1**
against its own local background at 59.5s — above AA for normal text, let alone at 112px —
and `countUp` settles it 1.22s before the cross-dissolve. The rank did not reproduce and the
legibility limb it was standing in for is not in trouble. **Eight-for-eight on
`predictions_missed_a_sixth_time_2026-08-10`.**

**2 · The s75/s76/s79 floor — MEASURED, and it is a TWO-member tie, not a three-member cluster.**

```
s79  38.872   ← floor
s75  38.928   separation 0.057  → TIED (< 1.0, one clause, any member satisfies it)
s76  40.704   separation 1.775  → EXCEEDS 1.0 → s76 is NOT in the floor
s80  43.923 · s74 44.125 · s71 45.225 · s77 47.662 · s81 47.736 · s72 48.217
s73  51.553 · s70 52.466 · s69 54.633 · s78 55.973
```

Under `separation_not_rank_2026-08-09` the shape here is neither of the two the brief named:
it is a **two-member tie {s79, s75} at 0.057**, and the third frame the build clustered with
them separates by 1.775 and is out. The invariant —
`outlier_limb_is_subordinate_to_the_invariant_2026-08-10`, one direction only, no
satisfied-by-construction — is discharged on the numbers above: **the payoff (s77, 47.662)
and the CTA (s81, 47.736) are both ~8.8 points above the floor and both above the median.**
Neither of the two beats this chapter is bound to protect is anywhere near the bottom.

No fix, and a fix would be forbidden anyway: brightening s75 strands **s79 alone** at the
floor, and s79 is the callback that pays chapter 1 — moving a beat that carries the video's
emotional close to the bottom to relieve a tie is exactly the trade
`outlier_limb_is_subordinate_to_the_invariant` forbids. Both floor frames were opened at full
size and both read: s79's white focal measures 17.4:1 against its own field; s75's green subs
are the highest-chroma type in the chapter.

## Would I keep watching?

Yes, and the chapter closes the video properly. It opens on its strongest move — a
weathervane under *"It is not a settled number"* is the rare final-chapter open that reopens a
loop instead of closing one, and the VO earns the next minute by conceding the argument before
recapping it. The ladder assembling under the voice on s75→s76 is the best 15 seconds in the
chapter; the pull-back is one continuous move, the tight frame really is a crop of the wide
one, and it never self-dissolves. s81 is a clean terminal CTA — one `--pop` element, a CSS
triangle not a font glyph, and the sub-line is the spoken reason rather than an invented
promise.

**Where attention is at risk: chapter-local ≈ 15s (cut-absolute ≈ 457s), s71.** It is the
second consecutive book-on-a-table with a coloured percentage over it, and the antique book of
finding 2 makes the beat feel like more of the same rather than a fresh answer. Fixing that
photograph is the cheapest retention win in the chapter.

The other risk is s77 at chapter-local ≈ 57s: the number lands hard, but the picture's
argument — *this one does not fit on the same scale* — currently arrives only as a red smear
across the bottom third. Finding 1 is what turns the frame's best idea back on.

## Regressions vs my last pass

n/a, attempt 1.

## What is working — do not break these

- **The rate discipline is complete.** Every figure in the chapter carries its assumption in
  frame: `EACH AT A 4.0% WITHDRAWAL RATE` (s75), `BOTH AT A 4.0% WITHDRAWAL RATE` (s76),
  `AT A 1.08% DIVIDEND YIELD` (s77), each with `ILLUSTRATIVE ARITHMETIC`, and s70/s71/s72 each
  carry a full provenance foot. Nothing on screen reads as a forecast and `no_return_promise`
  is clean — the overrun bar has no axis, no tick and no numeral, and both figures in its
  ratio are on screen in this chapter with their rates.
- **§3c holds: NO RAIL anywhere.** Thirteen frames swept, no chapter title, no scene counter,
  no slide number.
- **Ground temperature actually moves and the moves land on the turns** — warm-red admission
  (s69) → amber evidence (s70/s71) → red verdict (s73) → green ladder (s74–s76) → red payoff
  (s77) → the chapter's one neutral at s78, immediately after the payoff → warm callback (s79)
  → green meaning (s80) → orange CTA (s81). This is not a flat strip.
- **The s75/s76 HOLD is correct and must not be "fixed" as a repeat** — s75 is a derived
  1.469× crop of s76, `plateKen` 1.16→1.08→1.00, one continuous pull-back across 15.4s.
