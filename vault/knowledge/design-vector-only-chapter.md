---
summary: A photograph-free finance chapter is buildable and legible — the trial cut of japanese-money-methods ch2 (`index-design.html`, 11 scenes, 73.479s, zero raster). What it wins, what it costs, and the four rules that made it work.
updated: 2026-08-05
source: studio/videos/japanese-money-methods-hi-ch2/index-design.html + renders/DESIGN-ch2-v3.mp4 (three draft passes) and index-claudedesign.html + renders/CD-ch2.mp4 (the restructure, two more passes), 2026-08-05
stage: experiment — NOT shipped. index.html remains the chapter.
---

# The vector-only chapter — what a photograph-free cut actually costs

Creator, 2026-08-05: *"try out this chapter two completely made by Claude Design.
No image, no nothing."* Built and rendered. This note is the finding.

**The Claude Design MCP is not what does this**, and cannot be — full verb-by-verb
evaluation in [[claude-design-mcp]]. The photograph-free cut was built with the
tooling this repo already has: HyperFrames, `assets/js/motion.js`, inline SVG, CSS
gradients, and the chapter's own four Lottie assets. Nothing new was installed.

## What replaced the photograph — three layers per scene

1. **`.rules`** — a 160px editorial grid, ink at 5.5% / 3%, pure CSS. Under `ken` it
   gives the drift something to move; without it a drawn field has no parallax and
   the scene reads as a still.
2. **`.glow`** — one soft radial in the scene's role colour. This is the job the
   graded photo's light did: it says where to look. Six of eleven scenes carry no
   role colour and get plain ink, which is correct.
3. **`.art`** — an oversized SVG motif, bleeding off frame. This is the scene's
   picture and it is what the sound-off rule now judges.

## The four rules the three passes produced

**1. Drawn art needs 2–4× the opacity you first reach for.** Draft 1 set the motifs
at 13–20%, which is right *over a photograph* and wrong over `--bg`. The `.scrim` is
tuned to sit on a graded still and it ate the art — s14's seal, s20's rings and s21's
₹ were invisible in the encode while passing every check. Shipped range is **26–58%**.
The number that matters is not the opacity, it is that `.scrim` + `.grain` are still
in the stack and both cost you contrast the photograph used to absorb.

**2. Frame 0 of a chapter may not be a stroke-draw.** s11 opened on `draw()` and so
opened on an empty field for ~0.4s, arriving off ch1's dark kitchen — the same
retention failure `ceo-hi-ch2-1` killed the rooftop photograph for. The threshold now
exists at frame 0 and only the noren animates. **A `draw()` is a second-beat move, never
the first.**

**3. Motifs collide with the centred stack, and photographs never did.** The `.stack`
sits ~440–640 in a 1080 frame. s11's panels ran 302–632 and passed behind the kicker at
35% ink, halving its contrast — a photograph's own tonality plus the scrim had been
hiding this class of error. **Anything drawn between y≈420 and y≈660 is competing with
the type.** Keep motifs above 410 or below 670.

**4. A declared `data-framings` swap must survive the sheet.** s19's two framings became
a bracket move, which at contact-sheet scale read as the same frame twice — the exact
"cosmetic framings to duck the guard" failure `pipeline_check` cannot see. **If the two
frames are indistinguishable in the sheet, the swap is not real, whatever the attribute
sums to.**
⚠️ **The fix this rule claimed — "fixed by adding an edge-to-edge baseline to framing 2"
— never worked.** The baseline was drawn at svg y1052, which rule 6 shows is outside the
visible window, so it has not appeared in one rendered frame of `DESIGN-ch2-v3.mp4`.
s19's swap in the v3 cut is still cosmetic. Genuinely fixed in `index-claudedesign.html`
by moving both framings inside the window (fence to y916, opened brackets + baseline to
y906/y934).

## Three more rules, from the restructure pass (2026-08-05)

Found by rendering `index-claudedesign.html` and reading the sheet. **All three are
latent in `index-design.html` too** — it renders with them and always has.

**5. `stroke-width="N"` as an SVG attribute is a no-op in this system.** `.art .st`
sets `stroke-width: 3` in CSS and **a CSS rule always beats an SVG presentation
attribute**, so every `stroke-width="9|14|15|22"` in the v3 cut draws as a 3px
hairline — the seal, the tick, the rings and the fence all lost their weight
silently. Write inline `style="stroke-width:N"` instead.

**6. The visible window is smaller than the viewBox, because of `ken`.** `.field` is
`inset:-8%` and `ken` scales 1.0↔1.16, so anything that must stay on screen for a whole
scene has to sit inside **svg x 247–1673, y 139–941**. Outside that it is cropped for
part or all of the scene, silently, at every check. This is what broke rule 4's fix and
what made s11 unsolvable as a centred plate.

**7. A group that scrolls needs a `clipPath`.** s12's feed columns travel upward and
ride out of the mechanism zone into the type band without one.

## Two more, from restoring the photographs (2026-08-05)

**8. Drawn art over a photograph must be ADDITIVE, never depictive.** The moment
`image_per_scene` was restored to the two restructured chapters, the drawn layer
that had been *standing in for* a picture started **doubling** it — a ghost
envelope over a photograph of an envelope, a drawn noren over a photographed
noren, a seal outline over the National Diet Building. That reads as a mistake
rather than as a layer, and it was the single biggest defect of the first photo
pass. What survives the photograph is art that asserts what the picture cannot:
a proportion (ch2 s15/s16/s17's mechanisms), a comparison (ch1 s3's "higher than
last time" bar against a dashed box marking last time), a measurement (ch1 s7's
draining ACCOUNT bar), a count (ch2 s19's household grid over a real crowd).
Nine of ch1's ten scenes and four of ch2's eleven had their drawn layer switched
off outright — `.has-photo.art-off .art { display: none }` in
`tools/scaffold/assets/chapter-design.css`.

**9. Never darken a photograph to make drawn art readable.** Restated because the
photo pass ran straight at it: the base grade is
`grayscale(.32) brightness(.62) contrast(1.05)`, and a per-scene darker override
stacks with it and turns real photographs into grey mush — rejected by the
creator on 2026-08-04 ("it fails to black and white"). So the ground temperature
became a **tint at 38% opacity OVER** the still rather than a darker fill under
it, and anything that genuinely needs a darker field gets `.band` behind it alone.

## What it wins

- **The scenes whose point is a proportion get better.** s16 (`ABOUT 1%`) was a Cabinet
  Office facade — true, and not what the line is about; it is now a 1400px track with a
  15px nub, and it states the figure before a word is read. s19's household grid and
  s17's two bars were always vector and now have nothing to fight.
- **Every sourcing failure class disappears.** This chapter's audit history is almost
  entirely image defects — German newsprint under Japan's accounts, the Tokyo
  *Metropolitan Police* under ONE GOVERNMENT, a demonetised ₹500, four grey exteriors in
  a row, the Hungarian Parliament twelve times from stock. **A drawn frame cannot assert
  a thing it does not mean.** No licence conditions either: `CREDITS.txt` and the two
  CC BY-SA obligations vanish with the photographs.
- **It is cheap and instant.** No stock queries, no candidate rounds, no re-crops.

## What it costs — and this is the finding

**Eleven frames of one temperature.** The photo cut steps warm noren → cool phone →
dark navy → brick colonnade; the vector cut is eleven dark editorial slides with a
centred stack and an outline motif. It is cleaner, more consistent and more
*designed* — and flatter. There is no warmth, no texture and **no human presence
anywhere in 73 seconds**, in a chapter whose subject is households.

So the honest read is **not** "vector replaces photography". It is:

> Scenes whose point is a **number, a proportion or a mechanism** are better drawn.
> Scenes whose point is a **place, a person or a threshold** are worse drawn.

Which is roughly s13 s15 s16 s17 s19 s20 better, s11 s12 s14 s18 s21 worse. A hybrid —
drawn for the argument, photographed for the people — beats either pure form, and is
close to what `image_per_scene` + the Lottie cap were already pushing toward.
This trial suspended `finance-every-frame-has-image` (Claude memory) deliberately; it does not
overturn it.

## Files

- `studio/videos/japanese-money-methods-hi-ch2/index-design.html` — the cut. Scene ids,
  every `data-start` / `data-duration` / `data-framings`, the track 1/2 alternation, the
  type system, every string and the voice rows are **verbatim from `index.html`**, so it
  concatenates frame-exact with ch1/ch3 and the two are directly comparable.
- `renders/DESIGN-ch2-v3.mp4` (20.0 MB, 73.5s) + `renders/SHEET-DESIGN-v3.jpg`.
- `index-claudedesign.html` + `renders/CD-ch2.mp4` + `renders/SHEET-CD.jpg` — the
  **restructure** of this cut (2026-08-05): four layout archetypes instead of one centred
  stack, a per-scene ground temperature, and rules 5–7 above applied. Same verbatim
  contract. It fixes this note's central complaint — eleven frames of one temperature —
  and leaves its central *finding* standing: s12 and s18 are still the weakest frames,
  because a feed and a form are places, not quantities. Evaluation: [[claude-design-mcp]].
- `index.html` is untouched and is still the chapter.
