---
summary: hi ch3 attempt 3 reviewed from the encode. PASS, 0 blockers. Both changes since attempt 2 verified on the mp4 rather than inherited — s22's stale crop window is gone and all four frame edges carry photograph at both ends of the ken, and s24's granted second drawn layer `divide-by-12` is additive under rule 8, arithmetically exact on width, assembled by +3.30 of 6.05s, and does not break the s23->s24 hold (a 1-D affine fit across the joint gives a straight 0.004-per-0.30s ramp with no step). Three should-fix items carry unchanged and need no ch3 work; two new notes on the strip's drawing conventions, recorded so ch4 reuses the pattern correctly.
updated: 2026-08-09
source: studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4 (rebuilt 9-cell sheet + 13 frames + a scale/shift fit across the s23-s24 joint), index.html, build.mjs, assets-ch3/final/ md5s, tools/format/fin-editor.json, script-hi.md, logs/ceo-hi-ch3-2.md
stage: fin-editor, cut hi, chapter 3, attempt 3
---

# editor · passive-income-number · hi · chapter 3 · attempt 3
VERDICT: PASS

Scenes s22–s30, lines 3.1–3.9. Sheet rebuilt and read as a grid, thirteen frames pulled from
the encode at 1920×1080, and the two changed things measured on the mp4 rather than carried
over from attempt 2. **Zero blockers. Nothing here is unshippable.** Two new items and both
are notes.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s24 | note | the lit cell is exactly 1/12 on **width** and 1.4× the others on **height** | The strip is 12 identical 51px cells and the lit one is 51/612 = 1/12 exactly, which is the assertion and it is true. But the lit rect is `y=238 h=154` against the strip's `y=260 h=110`, i.e. 22px proud top and bottom. Read as a selection marker — which is how it reads on the encode, because every cell is the same width in one continuous strip and only the fill and the proudness change — that is correct. Read as a bar chart, where height is magnitude, it would overstate. I am **not** raising this above a note: the strip has no baseline, no axis and no second bar, so there is no chart grammar for a height read to attach to, and the generator's own assert is on the dimension that carries the claim. | none for ch3. **Binding on any reuse:** if this strip pattern is ever re-cut with the cells at differing widths or with a baseline, the proud-ness must go, because at that point height starts reading as value. Record it in `build.mjs` beside the existing 1/12 assert. |
| 2 | s24 | note | this is the chapter's busiest photograph carrying its most detailed drawn layer | §10 routes the art-forward scenes to the calmest frames and this one could not be moved, because s24's photograph is fixed by the s23→s24 hold. Measured on the encode: grey cell interior ≈ L45, inter-cell gap ≈ L18, so the twelve cells resolve at roughly 2.5:1 against their gaps and a run-detector counts 11 grey + 1 lit cleanly at 1920 — but the bead rods do ghost through the `.5` fill and the cells are not perfectly uniform across the strip. It reads; it is the chapter's least calm drawn layer. | none. **`.art-lift` is load-bearing here and must not be removed** — the build's own snapshot without it had the cells reading as a ghost over the beads. If s24's photograph is ever re-fetched, this layer needs re-checking, not inheriting. |
| 3 | s27 | should-fix | *(carried unchanged from attempts 1 and 2)* the stamp through-line ships two states, not three — s27 is two stamps at rest, not mid-press | §10's arc is s8 at rest → s27 mid-press → s77 five stamped. The middle term is missing. | **Same disposition as both earlier rounds — do not re-fetch on my account.** Brief **s77** to carry the missing change (five freshly stamped receipts, ink wet). The build has already recorded the two-state reality in the s27 comment, which is what the CEO asked for. |
| 4 | s32/s33 | should-fix | *(carried unchanged)* ch2's adding machine and ch3's abacus are two consecutive calculating devices | Not a ch3 defect — a constraint that lands on ch4. If s32/s33's counterfoil is a third calculating device, §10's five-artefact paper spine is gone. | ch4's counterfoil **must be paper**. |
| 5 | — | should-fix | *(carried unchanged)* `storyboard-hi.md` §9c (l.859) and §12 (l.968) still carry the retired five-rung ladder starting at s16, with "two cash boxes" at s22 | `index.html`'s s22 comment and `notes.md` l.870 are now both correct and the storyboard is the stale one — and the storyboard is the artefact an agent reads by path. | Fix both rows to the four-rung ladder (s22 → s31 → s58 → s62) before ch5 briefs assets. |
| 6 | s28 | note | *(carried)* `corpus-doubles` sits at peak luma 87 and is at the low end of readable | Unchanged from attempt 2, still not a defect, still should not be touched in a fix pass. | none. |

## The two things I was asked to verify, verified on the encode

**s22's crop window — closed, and I measured it rather than inheriting my own numbers.**
`#s22-bg` now carries `background-image` and nothing else; the `background-size` /
`background-position` pair is gone from `index.html` and from the generator. On the encode
at **+0.35** (the opening frame, which is what the binary sound-off gate runs on) and at
**+5.10** (the ken at its loosest, which is where the old 79px band was 7.4px from exposure),
all four frame edges carry photograph:

| | top row | bottom row | left col | right col |
|---|---|---|---|---|
| +0.35 | 27.6 / σ7.0 | 22.6 / σ5.7 | 20.8 / σ8.2 | 29.9 / σ7.4 |
| +5.10 | 26.4 / σ7.2 | 21.7 / σ5.7 | 18.2 / σ5.3 | 25.9 / σ8.3 |

Texture on every edge at both ends. **The uncovered band is 0px and the frame that ships is
now the frame fin-assets gated.** The gullaks still read: coin slits countable, no text, no
coin, no hand, no face. Attempt 2's second s22 finding is cleared too — the composition
comment now describes the terracotta gullak yard and carries the many-small-containers
declaration, so the archived artefact is true.

**s24's `divide-by-12` — it earns its place.**

*Rule 8 / additive.* It passes on the merits, not on the grant. The photograph is a soroban
with the beads at no value; an abacus is a device **for** calculating and what it cannot do
at any bead setting is assert that **one whole divides into twelve equal parts and one part
is taken**. That is a proportion, and there is no proportion in the photograph for the
drawing to duplicate. This is not the ghost-envelope case — an outlined envelope over a
photographed envelope re-draws the subject; a 1/12 strip over an unset abacus asserts what no
frame of that abacus contains. **This is the finding I raised in round 1, and the built answer
is the one I asked for: the operation, not the number.**

*Truth.* Geometry read off `index.html`, not off the account: 12 cells × 51px + 11 gaps ×
9px = 711, the notches step exactly 60px from x=91 to x=691, the lit cell is `x=40 w=51`
sitting **inside** the twelve rather than added beside them, and 51/612 = 1/12 exactly.
Measured on the encode at +3.30 the strip spans 1161→1870 with eleven 50px grey cells on a
10px pitch gap plus the lit one — twelve, uniform, countable. ₹60,000 ÷ 12 = ₹5,000 is real
arithmetic on the chapter's own figures at its own 3.0%, the frame carries `ILLUSTRATIVE
ARITHMETIC` in the foot and `AT A 3.0% WITHDRAWAL RATE` as a first-class 40px sub, and
nothing in the drawing reads as a published statistic. No invented source, no seal, no agency.

*fin-render's two open judgements, settled on the mp4.* **Legibility at speed:** the three
beats separate cleanly — +2.40 shows one bar cut into twelve equal cells with the notches in
and nothing lit, +3.30 shows cell 1 green and proud with `ONE MONTH` under it and `TWELVE
EQUAL MONTHS` right-aligned. A viewer never has to count, because the label states the
twelve. **`fill-opacity` .5 under h.264:** survives. Cell interiors sit ≈27 luma points above
their gaps and no cell drops out anywhere in the strip; the bead rods ghost through but do
not break a cell. Both confirmed.

*Timing.* Assembly beats at +1.70 / +2.25 / +2.80 with 0.5s fades, complete at **+3.30**
inside s24's 6.051s framing — 2.75s of settled frame before the cut, and the ₹5,000 countUp
lands after the art at +4.15. The art ladder is **byte-identical in shape to s28's**
(band +1.40, a1 +1.70, a2 +2.25, a3 +2.80), which this chapter already passed, so the
sub-0.8s spacing inside the layer is the same one-focal-group-assembling exemption s28 ships
under and not a new cue-ladder breach. Root is `data-duration="61.143"` and the scene table
sums to it exactly (55.484 + 5.659); the encode is 1835 frames.

*The hold.* I did not take this on report. Fitting a 1-D scale+shift on the photograph-only
band (y 820–1040, x < 1100, i.e. below all type and left of the plate) against t=10.60:

| t | 10.60 | 10.90 | 11.20 | 11.50 | 11.80 | 12.10 | 12.40 | 12.70 |
|---|---|---|---|---|---|---|---|---|
| scale | 1.000 | 1.004 | 1.008 | 1.012 | 1.016 | 1.020 | 1.024 | 1.028 |

A straight 0.004-per-0.30s ramp straight through the 11.552 joint and the 11.552–12.002
dissolve, with no step, no stall and no reversal. **One continuous push.** The `.centred` →
archetype-B move relocated the type only.

## What is working

- **`divide-by-12` is the second model layer in this chapter, and for the same reason as the
  first.** Both assert something their photograph cannot — s28 a ratio over an empty balance,
  s24 a proportion over an unset abacus — both compute from the real figures, both put the
  shape in the drawing and the numbers in the type, and neither re-draws its subject. That is
  the pattern ch4 should copy. Do not touch either.
- **s22's fix is complete and the archived record now matches the frame.** Plain `cover`, no
  window, no band, and a comment that describes the photograph that actually ships.
- **The rate discipline, the hold, and the craft ladder are unchanged and must stay so** —
  every corpus and derived figure carries its 3.0% or its ILLUSTRATIVE marker in frame across
  all nine scenes, nine md5-distinct files with no reuse, s30 alone on a bare 5.659s, first
  cue up before +0.40.
