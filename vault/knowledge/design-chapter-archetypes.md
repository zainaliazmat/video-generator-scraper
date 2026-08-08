---
summary: The archetype layer — four scene layouts (plate/figure/ledger/band), the declared art window, the ground temperature arc, the photograph rules, and what a drawn layer has to be made of to survive the encode. Sits on top of blockframe-9 and is what every chapter of a MEDIUM/LONG cut is built from. Code homes are tools/scaffold/assets/chapter-design.css and tools/chapter_project.py; this file is the rationale.
updated: 2026-08-06
source: built and rendered across five draft passes on japanese-money-methods ch1 + ch2 (2026-08-05, creator-approved), then across hi ch3-ch8 and the full -en cut on the generator (2026-08-05); gotchas 5-8 come from the creator's first frame review and the eight-chapter -en audit (2026-08-06)
stage: ADOPTED — the standing layout system for chapter-based cuts
---

# The chapter archetype layer

> **Code home:** `tools/scaffold/assets/chapter-design.css` (+ `motion.js` for
> `span` and `plateKen`). Where this prose and the file disagree, **the file
> wins** — it is what renders. Constants: `tools/format.json chapter_design`.
> Supersedes nothing in [[design-finance-blockframe]]; it *extends* it. That note
> still owns the tokens, the grade, the scrim, the type ladder and the watermark.

## Why it exists

`blockframe-9` gives every scene ONE layout — the centred `.stack` over a
full-bleed photograph. That is right for a nine-scene SHORT. Across a
ninety-scene LONG it is what makes the cut read flat, because the photograph was
carrying all of the variance and nothing else ever moved. The vector-only trial
([[design-vector-only-chapter]]) proved it by removing the photograph: eleven
frames of one temperature, and the repetition was the only thing left.

So the centred stack stops being *the* layout and becomes one of four.

## The four archetypes

Assigned by **what the scene does**, never for variety's sake.

| | name | geometry | use |
|---|---|---|---|
| **A** | plate | centred stack, motif full-bleed behind | chapter opens, hand-offs, ceremony |
| **B** | figure | number off-centre, rule at the left margin, art in a top-right plate, measure bar under the type | any scene whose point is a figure |
| **C** | ledger | hard vertical split — type left, artefact full-height right, cropped by the frame edge | evidence: a document, a form, an artefact |
| **D** | band | type compressed under a full-width rule, mechanism owning the bottom two-thirds | scenes where the MOTION is the argument |

Write the sequence out before building and check it reads as a rhythm. ch1 is
`A A C C D D B C D A`; ch2 is `C D B C B B B C D D A`. **Holding one archetype
across consecutive scenes is correct when they are one argument** — ch2 keeps B
across s15/s16/s17 (37.8% → about 1% → thirty times) while the *mechanism*
changes underneath it (table → track → bars). Varying the layout there would
break the only through-line the chapter has.

## The plate — the load-bearing idea

Art lives in a **declared, clipped rect with its own push**, one per archetype,
never in a full-bleed field.

```
.p-a  0,0,1920,1080     .p-b  1120,150,860,610
.p-c  1046,-60,934,1200 .p-d  0,424,1920,656
```

Two things this buys, both learned the hard way:

1. **It kills the ken-window bug class.** The old `.field` was `inset:-8%` and
   `ken` scaled it 1.0↔1.16, so the genuinely-always-visible window was only
   **svg x 247–1673, y 139–941** and nothing computed that. Art outside it was
   cropped silently, at every check. A shipped cut carried an "edge-to-edge
   baseline" that never once appeared on screen. With a plate the window is
   declared, so it cannot recur.
2. **It is what makes a squat motif legible.** ch1's `s11` doorway was
   unbuildable as a centred plate — the stack eats svg y 436–643 and the ken
   window eats the rest, leaving two ~290px bands, and panels forced into that
   read as colour bands rather than cloth. Moved to C it got 130×450 panels with
   36px slits and worked in one pass.

**A plate is a LIFTED PANEL, not a transparent window** — `rgba(30,38,54,.50) →
rgba(13,16,23,.15)`. Ported as a bare `overflow:hidden` rect first and every
motif rendered invisible: dark art on the raw ground has nothing to read
against. The alpha keeps the ground temperature showing through, so the lift
costs no colour.

## The ground temperature arc

`.field` carries a per-scene `--f1` two-stop ground whose warmth tracks the
argument. Role scenes deepen into their role colour; scenes with no role move
only on the **neutral warm↔cool** axis so no frame asserts a colour it has not
earned. One role colour per scene still holds.

ch2's arc is the reference: warm promise → cool screen-light → amber under
examination → neutral paper → amber deeper → **the coldest frame in the chapter
where the claim collapses to about 1%** → red at the correction → neutral → cool
opening → red radiating → warm resolve. *The drop is a temperature event before
it is a number.*

**Push it harder than looks right.** At document scale the arc reads almost flat;
in the encode it is exactly right. Same lesson as drawn-art opacity.

We do **not** re-implement the ground cross-fade the Claude Design animatics use.
They hard-cut and melt the ground inside the incoming scene; we cross-dissolve
whole sections for 0.45s, which blends both grounds already. Adding both
double-fades.

## Photographs — `image_per_scene` is the standing rule

The vector-only chapters were a deliberate, temporary exception. Every shipped
frame carries a graded still, using blockframe's own `.bg` and the **locked**
`grayscale(.32) brightness(.62) contrast(1.05)`.

- **`.has-photo`** — the ground drops to a 38% tint, `.rules` to 28%, the plate
  becomes an aperture (no panel lift), the hatch is hidden.
- **`.art-off`** — the scene's drawn layer is redundant; hide it entirely.
- **`.art-forward`** — buy the drawn layer back to 52% for scenes whose point is
  a PROPORTION, where the mechanism still wins and the photograph is only there
  to satisfy the rule.
- **`.centred`** — see below.

**Rule 8 (the big one): drawn art over a photograph must be ADDITIVE, never
depictive.** A ghost envelope over a photograph of an envelope, a drawn noren
over a photographed noren, a seal outline over a government building — all read
as a mistake, not a layer. What survives is art that asserts what the picture
cannot: a proportion, a comparison (*"higher than last time"* against a dashed
box marking last time), a measurement (a draining ACCOUNT bar), a count (a
household grid over a real crowd). On the first photo pass **nine of ch1's ten
scenes and four of ch2's eleven** had their drawn layer switched off.

**Rule 9: never darken a photograph to make drawn art readable.** A per-scene
darker override stacks with the base grade and turns real photographs into grey
mush — rejected by the creator 2026-08-04 (*"it fails to black and white"*). If
something drawn needs a darker field, darken **behind it** with `.band`.

## `.centred` — a split with nothing on the other side is a hole

B and C put type on one side because the ART was on the other. Once `.art-off`
retires a scene's drawn layer, the other side is empty and the split is no
longer a layout. Such a scene re-centres, and loses its plate, its `crule`, its
`vrule` and its `brule` — a divider between two bands is meaningless when there
is only one.

Creator, 2026-08-05: *"place the text in the center of the screen, so the right
side of the screen won't feel empty."*

Consequence to accept, not fight: on a photo-led chapter most scenes end up
centred, and the archetypes then vary the *art*, not the type. That is correct.
**If a chapter reads flat, the fix is giving two or three scenes something real
to put on the other side — never adding layouts for their own sake.**

## No rail

An earlier pass carried a top rail with the chapter title and a `1.3 / 1.10`
scene counter. **Removed at creator request 2026-08-05 and not to be
reintroduced:** the viewer must not be shown that the video is chapter-based or
slide-numbered. It reads as courseware, not as a film. The orientation problem it
answered is the edit's job.

## Building a chapter is a GENERATOR job, not a copying job

`tools/chapter_project.py <slug> --cut hi --chapter 3` builds the whole project
from the shipped `index.html` plus a hand-authored `chapter.json`. The split is
the point:

| the generator owns | the spec owns |
|---|---|
| every `data-start` / `data-duration` / `data-framings` / `data-track-index`, every on-screen string, every `.bg`, every `<audio>` row, every shipped motion call — lifted verbatim and rebased by ONE constant | the archetype, the ground `--f1`, whether the drawn layer survives, the art itself, the measure bar |

Chapter membership comes from the VO line id (`vo-<chapter>-<line>`), so there is
no second map to drift. **That is how the -en chapter map was caught: it is not
the -hi one.** `-en` ch6 runs s59–s73 and ch7 s74–s84, because the US rewrite has
two extra lines in KAKEIBO and its promise break sits one scene later. Deriving
the map by hand from the -hi row would have mis-cut two chapters.

The generator re-reads what it wrote and asserts the rebase — GAPS, not totals,
because a correct total is exactly what the re-timing failure produces. It also
reports the two shipped boundaries that are 1 ms out against their successor
(hi ch6/ch7) instead of silently absorbing them.

**One root `.html` per chapter project, and it is `index.html`.** `hyperframes
check` only looks for that name, `chapter_sheet.py` hardcodes it, and the
linter's `multiple_root_compositions` is an ERROR on two root files carrying
`data-composition-id` — so ch1/ch2's `index.html` + `index-claudedesign.html`
pair cannot pass a check. In a *chapter* project `index.html` is not the shipped
cut; the shipped cut lives in `<slug>-<cut>/` and is never touched.

## What a drawn layer has to look like to survive the encode

Rule 8 says what art may ASSERT. This says what it must be made of, and it cost
two full draft rounds across chapters 3 to 8 to learn:

1. **Solid fills and heavy strokes only.** `.has-photo .art` is 30% and
   `.art-forward` 52%; a 2–3px stroke at 0.4 alpha inside that is simply not on
   screen. Every outline "track", tick row and dashed leader drawn in the first
   ch3 pass vanished, and every solid filled rect survived. Draw a ghost track as
   a filled rect at ~.2, never as an outline; nothing thinner than 9px.
2. **Those two opacities are `!important`, so a per-scene inline opacity on the
   `<svg>` is a no-op.** The only levers that reach the screen are the weight and
   alpha of the elements inside it. (The `opacity` key in a chapter spec is
   therefore decorative; ignore it.)
3. **`.art-lift`** — a new modifier. `.has-photo` turns the plate into an
   aperture, which is right over a dark still and makes ink art light-on-light
   over a pale one (ruled paper, banknotes, a white wardrobe, a sunlit page).
   `.art-lift` gives that scene its panel back. It is the plate-scoped form of
   rule 9: it darkens BEHIND the art and cannot reach the photograph outside the
   plate rect, so the whole-frame lever stays forbidden.
4. **`.measure-lab.under` / `.measure.under`** — the bar's position is declared
   in the stylesheet now, at y 868/910. At the old per-scene y742 it landed on
   the icon that variant-A scenes carry *inside* their stack and struck its own
   label through on three consecutive ch4 frames.
5. **The contact sheet samples at +2.6s.** A mechanism that finishes at +4.4
   sheets as a half-built frame and reads as a defect that is not one. Assemble
   by about +3.3, or judge that scene from the mp4. Scenes whose line really is
   an enumeration keep their spread — their second declared framing gives the
   sheet a late cell anyway.

**Density calibration, from the approved chapters:** ch1 ships ONE drawn scene
and one measure bar out of ten. Three or four drawn layers in a twelve-to-
fourteen scene chapter is the top of the range, not the target.

## The gotchas that cost renders

1. **`stroke-width="N"` as an SVG attribute is a no-op.** `.art .st` sets it in
   CSS and a CSS rule always beats a presentation attribute. Write inline
   `style="stroke-width:N"`.
2. **The ken window is smaller than the viewBox** — see the plate section.
3. **A group that scrolls needs a `clipPath`**, or it rides out of its band into
   the type.
4. **`breathe(dur)` rounds UP as often as down.** 4.5 yields 6.0s, which can run
   past the root duration and leave an element mid-swell on the last frame. Ask
   for a whole multiple of 3.
5. **An absolutely-positioned `<p>` keeps its UA margin.** `.measure-lab` shipped
   without `margin: 0`, so its 1em top margin pushed every measure label 22px
   down onto its own track, in both cuts, on every chapter that carries a bar —
   invisible in source, obvious on the encode, and the creator caught it before
   we did (2026-08-06). Every other text class in `blockframe.css` sets
   `margin: 0`; a new absolutely-positioned text component must too, and should
   pin `line-height` so a font swap cannot re-close the gap.
6. **A Lottie stage needs PIXEL dimensions.** lottie-web sizes its `<svg>` from
   the container's box at `loadAnimation()` time. A stage declared `inset: -8%`
   with no width/height renders the artwork at its **native size pinned
   top-left** — a 640×420 phone in the corner of an otherwise empty frame, with
   `hyperframes check` passing clean. Declare `left/top/width/height` in px and
   force `.stage svg { width: 100% !important; height: 100% !important }`.
7. **A drawn proportion's numerator and denominator are a PAIR.** A build copied
   a 16px nub from one chapter into another without the 1480px track it was a
   fraction of, landing it in a 600px track: 2.67% printed under a focal reading
   "ABOUT 1%", 2.4× off a published figure. Never move one without the other,
   and state the arithmetic in the scene comment at the point of edit.
8. **`.p-b` maps viewBox x 1:1 to screen x.** The plate is `left: 1120px;
   width: 860px` on a 1920 frame, so anything past **vx=800 is off-canvas** and
   simply does not exist on the encode. One chapter lost the X of a decision
   fork this way — the entire point of the frame — and every check passed.

## Putting the chapters back together — `tools/cut_assemble.py`

A chapter project is for BUILDING and REVIEWING. It is never the deliverable.
`tools/chapter_preview.py` stream-concats the eight drafts, so its seven joints
are hard cuts and up to eight frames of independent rounding accumulate;
`pipeline_check check_render` wants one file whose duration matches
`timing.json` to within a second. So the approved chapter designs are folded
back into ONE composition and rendered once.

`tools/cut_assemble.py <slug> --cut hi` writes
`studio/videos/<slug>-<cut>-full/index.html` and the merged full-cut
`audio.json`. It is the exact inverse of the generator's two rebases: offsets
are added back to every `data-start`, `<audio data-start>` and absolute motion
time, and **each chapter's last scene gets its `+0.45` cross-dissolve overlap
back** — the generator strips it because a chapter has no successor to dissolve
into. Each chapter's own `sceneTransitions` / `register()` / `var S` / `var D` /
`var IDS` are dropped and replaced by one of each over all 92 scenes.

The shipped `index.html` is never touched: it stays the one home of every
timing, on-screen string and `.bg`, and the assembler reads it as the authority
it verifies against.

Four things this taught, all of which would have shipped silently:

1. **A hand-built chapter's `<style>` must be SCOPED.** `-hi` ch2 deliberately
   redeclares `.field` as the legacy `inset:-8%` full-bleed field and overrides
   `.arch-b/.arch-c/.arch-d .stack` — correct for its eleven vector scenes,
   catastrophic across the other 81, which are plate-first. Merged unscoped it
   would have re-styled six creator-approved chapters, including undoing the
   `padding-left: 62px` the creator asked for on every B scene.
2. **Strip CSS comments BEFORE splitting a selector list on `,`.** These files
   put `/* C · LEDGER — type in a left column, artefact on the right */` above
   the rule it describes; the comma inside the prose becomes a selector
   boundary, and `.arch-c .stack` comes out as `.ch2 .arch-c .stack` — a
   descendant of the section instead of the section itself, matching nothing.
   The rule silently disappears and every check still passes.
3. **Verify attribute-by-attribute against the shipped cut, not by total.** The
   failure this project keeps hitting produces a correct total with every
   internal cut drifted. The assembler asserts each scene's `data-start`,
   `data-duration`, `data-track-index` and framings sum individually, plus
   monotonicity and all 92 voice rows verbatim. Independently: every scene's
   inner HTML must be byte-identical to its chapter project's — 0 differences
   across both cuts is the check that says nothing was redesigned in transit.
4. **The shipped script's tail rides along with the last scene's motion.**
   `motion_lines()` splits on `/* sN · … */`, so the final chunk carries
   `window.__timelines = …; register();`. Harmless in a chapter project; a
   second registration in a merged file is not. Both the assembler and any
   future merge must strip it (ch8 of both cuts had the duplicate).

**`FFMPEG_ENCODE_TIMEOUT_MS` is not optional at full length.** A 92-scene 1080p
cut is ~18,800 frames; capture takes ~26 minutes and the ffmpeg encode then runs
alone at about 0.17× — roughly 72 minutes. The default encode timeout is 41.8
minutes, so it is killed at about frame 11,000 with no mp4 written and the log
line buried thousands of lines deep. Ninety minutes lost, twice over if the
watcher only looks for the output file. Set
`FFMPEG_ENCODE_TIMEOUT_MS=10800000` (or `PRODUCER_ENABLE_CHUNKED_ENCODE=true`,
which is what `.claude/agents/fin-render.md` already carries), and make any
wait-loop break when the render process exits, not only when the file appears.

## Timing is never a design decision

Every `data-start` / `data-duration` / `data-framings` comes from `timing.json`,
which is measured from the voice. A layout pass may not touch one.
[[claude-design-mcp]] §3b records what happens when something re-times a chapter
by eye: durations that sum to exactly the right total while every internal cut
drifts up to 1.86s, with the last scene back-solved to close the books.

## Files

- `tools/scaffold/assets/chapter-design.css` — the layer.
- `tools/scaffold/assets/js/motion.js` — `span` (rail/measure fills) and
  `plateKen` (a push with explicit endpoints, so a zoom can continue across a
  cut on the same image).
- `tools/chapter_project.py` — the generator (see above). `chapter.json` in each
  chapter dir is that chapter's design spec and the only file to hand-edit.
- `studio/videos/japanese-money-methods-hi-ch1/index-claudedesign.html` and
  `…-ch2/index-claudedesign.html` — the two reference chapters, creator-approved
  2026-08-05. Chapters 3–8 and the whole -en cut are generated, and write
  `index.html` instead (see the one-root-html rule).
