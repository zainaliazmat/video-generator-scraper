---
summary: en ch1 fix pass against editor-en-ch1-2. Three edits, all in build.mjs — s4 repointed at s3.jpg with s3's own background-position and the push chained 1.08->1.30 (the §6b hold is now one file by construction), s6's three chips replaced by a drawn count (bag / fuel pump / house, each with a ticking checkbox), and s5 reframed to `center 100%` so the X ring and the arrow clear the stack. One consequence taken with the blocker: the Lottie stage moved to left 815 so the banner stays on the phone the new framing shifted right. Joint measured numerically — hold delta ≤0.81 vs 5.29 at a real boundary. 41 frames across 7 fresh -o dirs, `npm run check` clean, `pipeline_check check build --chapter 1` PASS, every timing byte-identical.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1/ · editor-en-ch1-2.md · fin-build-en-ch1-2.md · passive-income-number-hi-ch1/index.html s5 · tools/format.json chapter_design
stage: fin-build, cut en, chapter 1, attempt 3 (fix pass)
---

# fin-build — en · chapter 1 · attempt 3 (FIX PASS)

`build.mjs` is the generator and the only file I edited inside the project;
`index.html` and `assets/audio.json` are its output. **`assets/audio.json` is
byte-identical to attempts 1 and 2 (`e411096987b8fe28d671687f8eaf2739` before and
after every edit)** — it is derived from the same `sc[]` array the markup is, so
an unmoved hash is mechanical proof that no scene start, no duration and no SFX
cue moved. Nothing was re-timed.

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|
| start | 0 | 3.543 | 9.254 | 14.599 | 21.564 | 25.551 | 31.262 | 38.149 |
| `data-duration` | 3.993 | 6.161 | 5.795 | 7.415 | 4.437 | 6.161 | 7.337 | **8.271** |
| track | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |

Unchanged. Root **46.42s**, seven joints overlapping by exactly 0.450s, s8 bare.

The cold read is closed and I acted on none of it. **No `--bg`, no `--f1`, no
`.has-photo .field` opacity, no per-scene grade override.** The only `.bg`
overrides in the chapter are three `background-position` values, which are
framing, never grade.

---

## 1 · BLOCKER — the s3 → s4 hold. Taken as written, and it is now one file

```
#s4-bg  background-image: url(assets-ch1/final/s3.jpg); background-position: center 70%
        plateKen("#s4-bg", S.s4, D.s4, 1.08, 1.30)
```

`s4.jpg` is unused, left on disk, and its `.src` prompt is untouched. The
generator spec row for 1.4 now carries `img: "s3.jpg"` + `bgPos: "center 70%"` —
the same two values 1.3 carries — so the joint is identical **by construction**
rather than by arithmetic that has to be re-checked every time either file moves.
`plateKen` applies scale only (no `xPercent`), s3 ends at 1.08 and s4 starts at
1.08 at the same instant, and both scenes carry `--f1:#241d15`, so the two `.bg`
layers are the same pixels at the boundary. The 1.30 end is the tighter framing
`crop=1600:900:280:320` existed to reach, taken by zoom instead of by a file.

### Measured, not asserted

The chapter is not rendered yet (that is fin-render's stage), so I measured the
same quantity `scdet` measures — consecutive-frame delta — on the composition's
own rendered frames, in a region carrying **only photograph** in both scenes
(x1650–1900, y60–380: outside s4's left-aligned stack, above its `brule`, and
outside s3's centred stack). Two batches, identical relative offsets: the hold,
and the next real boundary as a control.

| pair offset | **s3 → s4** (the hold) | s4 → s5 (a real cut) |
|---|---|---|
| −0.05 → +0.05 (before the dissolve) | 0.547 | 0.564 |
| +0.05 → +0.15 | 0.095 | **2.654** |
| +0.15 → +0.25 | 0.811 | **5.294** |
| +0.25 → +0.30 | 0.569 | **1.905** |
| +0.30 → +0.35 | 0.339 | **2.857** |
| +0.35 → +0.45 (dissolve end) | 0.755 | **2.100** |
| +0.45 → +0.55 (after) | 0.653 | 0.528 |

The hold's peak pair-delta is **0.81**, flat across the joint and
indistinguishable from the ambient in-scene push either side of it (0.55 / 0.65).
The real boundary peaks at **5.29 — 6.5× higher** against the same ambient. There
is no photographic transition at 14.599 any more; the only thing crossfading is
type.

Eyes agree with the number. At **14.90**, the instant the editor measured two
phones, two mugs and two vases: **one phone, one mug, one vase**, with s3's
statement ghosting out and s4's `brule` fading in. The whole 14.549–15.15 sheet
shows one unchanging composition under a continuous push.

⚠ **The mechanism, not just this joint.** The editor's warning that s41/s42 and
s75/s76 will ghost the same way is correct and the rule that prevents it is now
in the spec table, not in prose: a hold pair is **one `img` and one `bgPos`, with
chained `plateKen` endpoints**. A derived crop is only safe when both files are
the same aspect ratio AND neither carries a `background-position`, which is
exactly the pair of conditions nobody checks. Storyboard §6b should say "same
file" outright.

### The one consequence I had to take with it

Repointing s4 moved the phone. On `s4.jpg` (an exact-16:9 crop) the phone's
centre sat at frame x≈1035; on `s3.jpg` at `center 70%` it sits at
960 + 231·scale = **x1218–1236 across the Lottie's play window**. Left where it
was, the 820px banner would have hung mostly on bare terrazzo with the phone
under its right edge — losing the one thing the editor said explicitly not to
lose. `.v-lstage` therefore moves `left: 550px → 815px` (card centre 1225, right
edge 1635, inside the 1810 safe line). Verified in frames: at **16.449** — the
`buzz` SFX cue — the card is mid-build and the phone runs down the middle of it.
The Lottie's own timing (`+1.13`, 2.50s) and the `buzz` cue at `+1.85` are
untouched.

## 2 · SHOULD-FIX 1 — s6 is a drawn count now, and there is no sixth sheet

`#s6-chips` (three chips, no motion) → `#s6-ticks`, the component hi ch1's 1.5
already ships: `.v-ticks` / `.v-tickcell`, three inline `<svg class="icon">` cells
with a `draw()`n checkbox under each. Copy is unchanged — the three chips are
still on screen, now as the label inside their cell, because ladder C's copy is
the script's and not the layout's.

| cell | glyph | why that glyph |
|---|---|---|
| Groceries | **`assets/icons/grocery-bag.svg`** (new) | a carried shopping bag, not the white cloth tote in the frame — same reason hi's ration mark is a sack and not a jar |
| Gas and the car | **`assets/icons/fuel-pump.svg`** (new) | the whole point of the finding: the doorstep photograph has no car and no fuel in it |
| Rent or the mortgage | `assets/icons/house-door.svg` | reused verbatim from the library |
| every tick | `assets/icons/checkbox-tick.svg` | reused; only the tick path carries a per-scene id |

Both new icons are **written back to `assets/icons/`** — colourless, classless,
`i-*` ids — and a script verifies every path in all four library files appears
verbatim in `index.html`, so the library and the cut cannot drift. My first bag
(cuffed top, knob handle) rendered as a salt shaker at 220px; the shipped one is a
straight-sided body under one big semicircular handle, and the library file
carries that note so the next build does not redraw the mistake.

Cues ride the cascade the chips already rode: cells `popEach` at +1.10 / +1.70 /
+2.30, each tick draws 0.50s after its own cell (+1.60 / +2.20 / +2.80, 0.45s),
last mark complete at **+3.25** — inside `chapter_design`'s "assemble by about
+3.3", and settled for 2.5s of the scene's 5.711s hold. Six sampled states, four
of them partial (one tick + empty box; two ticks + empty box; …), so it animates
rather than merely appearing.

Rule 8 holds for the reason hi's ruling gave: **a count being paid** is not
something the photograph shows. Rule 9 holds too — the scene gained a `.band`
(the generator now emits it for `art: "ticks"` as well as `art: "lottie"`), which
darkens *behind* the drawn layer inside archetype D's own band and never touches
the photograph. No Lottie was added: the chapter still spends 1 of its cap of 4.
No re-fetch, no sixth contact sheet.

## 3 · SHOULD-FIX 2 — s5 reframed, and the handoff value was backwards again

`#s5-bg { background-position: center 100% }`. No re-fetch, no re-crop, no
`.centred` change, and the arrow is untouched — the editor's ruling on it stands.

**`center 32%` is the wrong direction**, and it is the identical trap `#s3-bg`
hit at attempt 2 (where the handoff proposed 40% and 70% was correct). On a
`cover` image that overflows vertically, a *smaller* percentage aligns nearer the
source's TOP, which pushes the subject **down** the frame — i.e. further onto the
type, not off it. Rendered rather than argued: at 32% the bullseye moves ~42px
*into* the kicker.

The file's entire vertical slack is 231.6 box px ≈ 126 frame px at the scene's
mid-scale, so `center 100%` is the far end of it and it is what the frame needs.
At **22.35s** (bare, the editor's own sample instant) the X ring and the arrow's
point sit clear above the stack and "NOT RICH" lands on empty gold beside the
shaft; at **23.364s** (max density) the focal line runs across bare gold and lower
red with the mark well above it. The gold/arrow cluster is ~340px tall against
~180px of stack, so the fletching's tail still grazes the focal line's top-right —
that is the residue of a subject that fills the frame, and it is the best the
declared levers reach without moving the stack or re-cropping. Checked at both ken
extremes (scale 1.16 and 1.00) — the mark stays above the kicker for the whole
scene, and the image's bottom edge never reaches the frame (86px of margin at
scale 1.0), so nothing exposes.

---

## The frame pass — 41 frames, 7 batches, one `-o` dir each

`hyperframes snapshot` wipes its `-o` directory per invocation, so every batch has
its own. A retry loop wrapped all seven invocations; no `Navigation timeout` flake
occurred this pass.

| batch | frames | what | how many I actually looked at |
|---|---|---|---|
| `s5-100` | 2 | s5 at `center 100%`, bare + max density | **2 of 2 full res** |
| `c2-hold` | 8 | 14.549 → 15.15 across the s3→s4 hold | **8 of 8 measured numerically** + 14.90 full res + contact sheet (8) |
| `c3-cut` | 8 | 21.514 → 22.115, the s4→s5 boundary, control | **8 of 8 measured numerically** |
| `c4-density` | 10 | each scene's LAST cue + t=0.05 + t=46.41 | 3 full res + both contact sheets (**10 of 10**) |
| `c5-lottie` | 6 | the banner's build on the new framing | 1 full res + contact sheet (**6 of 6**) |
| `c6-ticks` | 6 | s6's cascade, four partial states | 3 full res + contact sheet (**6 of 6**) |
| `c7-joints` | 7 | all seven joints at +0.38 | contact sheet (**7 of 7**) |

**9 read at full resolution, 32 more on five contact sheets, 16 of them also
measured pixel-wise.** An earlier working batch (`c1`, 9 frames) was shot against
an intermediate build and is superseded by `c4-density`; I am not counting it.

- **All 8 scenes paint their photograph.** Eight distinct graded stills in
  `c4-density`; s3 and s4 are now deliberately the same file, which is the fix.
- **All 7 dissolves fire against a live frame.** At +0.38 every joint shows the
  outgoing type ghosted over the *incoming* photograph, never against black. The
  hold is the one that looks different, correctly: only the type changes.
- **t=0.05** shows s1's photograph already painted with no type; **t=46.41** shows
  s8 fully painted and not fading, so the assembled cut takes no black flash.
- **No rail.** Every occurrence of "rail" / "chapter" / "slide" in `index.html` is
  in a comment, the `<title>` or the stylesheet filename. No frame of the 41
  carries a title, counter, slide number or progress mark. The `cut-en` watermark
  rides `#root::after` bottom-right in all 41.

## Gates

**`npm run check` → PASS**, identical in shape to attempts 1 and 2 — no new
finding from any of the three edits.

```
Lint      0 error(s), 3 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 9 info(s)
Motion    0 errors, 0 warnings
Contrast  10/10 text checks pass WCAG AA
```

The 3 warnings are `composition_file_too_large` (337 lines) and
`timeline_track_too_dense` ×2 — the shape every one-file-per-chapter build here
has. The 9 layout infos are all `container_overflow` on `#sN-bg`, which IS the ken
scaling the background past the section that clips it. `known_benign` is `[]` and I
added nothing to it. **No design token was touched** — no colour, no size, no
weight; the three `background-position` values and the stage's `left` are
geometry.

**`pipeline_check check build --slug passive-income-number --cut en --chapter 1`
→ PASS build-en.**

## Result

**8 scenes · s1–s8 · 46.420s.** Chapter 1 of six, chapter offset 0.000s, so it
concatenates frame-exact as-is. Three design edits plus one forced consequence
(the Lottie stage), zero timing changes, two icons added to the permanent library.
Ready for a fresh draft render.
