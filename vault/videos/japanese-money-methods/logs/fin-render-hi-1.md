---
summary: Gate-two frame check for japanese-money-methods-hi, attempt 1. All 92 per-scene frames are correct in isolation, but every cross-dissolve boundary paints the OUTGOING scene's rail number and headline on top of the INCOMING scene — a stacking-context leak in the shared scaffold. FAIL, no encode.
updated: 2026-08-01
source: hyperframes snapshot v0.7.66 against studio/videos/japanese-money-methods-hi/index.html
---

# fin-render — hi — attempt 1 (GATE TWO, frame check only)

Invocation 1 of 2. **No encode was run** (orchestrator owns the encode).
`renders/FINAL-1080p-hi.mp4` does not exist yet; audio/VO/loudness QA is deferred
to invocation 2.

## Verdict

**STATUS: fail.** Not because of any single scene — all 92 per-scene frames are
clean — but because of a boundary defect that reproduces on the real 30 fps
frame grid at all 91 cross-dissolves.

## What was sampled

Render frame rate is **30 fps** (no `data-fps` on `#root`; `hyperframes render`
defaults to 30), so frame index = `round(t x 30)`.

### Pass 1 — one frame per scene, at that scene's settled last cue
Sample point per scene n = `S[n+1] - 0.20s`, i.e. after every cue in the scene
has landed (no `exit()` anywhere in this cut, so nothing is hidden by then) and
before scene n+1's dissolve opens. 92 frames.

| Batch | Scenes | Times (s) | Frames | Output |
|---|---|---|---|---|
| gate2a | s1–s46 | 4.205 … 316.92 | 126 … 9507 | `snapshots/gate2a/` |
| gate2b | s47–s68 | 325.74 … 484.411 | 9772 … 14532 | `snapshots/gate2b/` |
| gate2c | s69–s92 | 491.14 … 659.2 | 14734 … 19776 | `snapshots/gate2c/` |

### Pass 2 — the six flagged items
`snapshots/gate2x/` — 108.5, 111.8, 147.4, 155.5, 157.3, 208.0, 210.0, 243.5,
245.6, 464.10, 464.32, 464.66, 470.10
(frames 3255, 3354, 4422, 4665, 4719, 6240, 6300, 7305, 7368, 13923, 13930,
13940, 14103).

### Pass 3 — boundary forensics
`snapshots/gate2y/` — 17.95, 18.05, 18.15, 18.25, 18.3 (dissolve interior)
`snapshots/gate2z/` — 18.333333, 18.366667, 18.4 → **frames 550, 551, 552**,
three consecutive real render frames across the s3→s4 boundary.

## The six flagged items — all PASS

| # | Check | Result |
|---|---|---|
| 1 | s24 icon RED, not white (`.warnc`) | **PASS** — frame 4422 (t=147.4, draw ends 147.21): padlock renders solid red `--warn`, stroke fully drawn, sits below the statement inside the content column. |
| 2 | s65/s66 hold pair, one continuous zoom | **PASS on framing** — 13923 (s65 full-bleed, whole ₹500 spread) → 13940/14103 (s66 panel). No self-dissolve flicker: the two use different framings of `s65.jpg`, so the boundary reads as a punch-in, not a same-image dissolve. |
| 3 | s66 push-in lands on the note's printed panel | **PASS** — frame 14103 (t=470.1): `background-position:86% 8%` lands the ₹500 numeral **and** serial **6UW 643492** in the panel, with the "MONTH 1…12" ruled band legible under it. Exactly the rung-3 crop target. |
| 4 | s19/s25/s32 second framing appears, swap visible | **PASS ×3** — s19: 3255 crowd crossing → 3354 blossom/shrine. s25: 4665 blue bar chart → 4719 open book. s32: 6240 pale ochre plaster → 6300 dark green board. All three swaps land and are distinguishable. *Soft note:* s32's pair are both low-information abstract textures and s32b is the darkest panel in the cut — the swap reads as a colour shift, not a new subject. Legal, just weak. |
| 5 | s36c not crushed to black | **PASS** — frame 7368 (t=245.6): the inline `filter: grayscale(.32) brightness(1.35)` holds. Truck reads as a clean silhouette against a graded red sky; sky retains tonal separation, no black clipping. Runs hotter/more saturated than the rest of the grade but is legible and on-subject. |
| 6 | `cut-hi` watermark in frame | **PASS** — the @cashguruguides mark is present bottom-right (`right:64px bottom:40px`, 84px, opacity .5) in **every one of the 105 frames** sampled, including the seven `v-bleed` scenes and mid-dissolve frames. `#root::after` hangs off root, so it survives the boundaries. |

## Sweep findings — 92/92 scenes clean in isolation

- **Layout / safe area:** no overflow, no clipped descender, no collision. Rail
  column (300px) and content column (`padding-right:860px` → 760px usable) hold
  on every scene. Longest statement (s32, 5 clauses) wraps to 3 lines and stays
  inside. Footnotes never touch the panel edge.
- **Contrast:** type sits on flat `--bg` on all 85 rail scenes (nothing over a
  photo), and the 7 `v-bleed` scenes carry the scrim + text-shadow. Consistent
  with the 17-of-17 WCAG AA already reported by `npm run check`.
- **Currency:** every money image is INR — ₹500 notes (s21, s51, s56, s65/s66,
  s86), ₹ coins, Gandhi portrait. No yen imagery anywhere against a ₹ statement.
- **Phone screens:** s1/s2 use a powered-off handset on a desk; no readable UI,
  no third-party app, no brand mark. Nothing else shows a screen.
- **Brand marks:** none visible in any stock frame.
- **Closing frame (s92):** the stall is a chai/juice vendor's wire glass carriers
  — not alcohol. Fine for @cashguruguides.

## The failure — outgoing scene's text and rail paint OVER the incoming scene

Reproduced on three consecutive real render frames at the s3→s4 boundary
(`snapshots/gate2z/`), and again at s65→s66 (`gate2x` frame 13940):

| Frame | t (s) | Rail no. | Headline / statement | Photo panel |
|---|---|---|---|---|
| 550 | 18.3333 | **03** | s3's "THEN RENT / Then the power bill…" | ~87% s4 (pen) |
| 551 | 18.3667 | **04** | **still s3's** "THEN RENT / Then the power bill…" | 100% s4 |
| 552 | 18.4 | 04 | *none* (s4's head has not risen yet) | 100% s4 |

So for the whole 0.45s dissolve the viewer sees the **previous** line's headline
and rail number sitting at 100% opacity on top of the **next** scene's photo;
one frame in, the rail number flips to the new scene while the old headline is
still solid; then the old text vanishes with a hard cut. Frame 551 is
unambiguously a wrong frame — scene 04's identity with scene 03's words.

**Root cause (mechanism verified, not guessed).** `.scene` is
`position:absolute` with **no `z-index` and no `isolation`**, so it is not a
stacking context once its opacity reaches 1. Its children are:
`.bg` z-index 0 · `.scrim`/`.grain` z-index 1 · `.stack` **z-index 2** ·
`.rail .railcol` **z-index 3**. Those escape into the **root** stacking context
and are sorted globally by z-index, not per scene.

During a dissolve the incoming section has `opacity < 1`, which *does* force a
stacking context — but one with `z-index:auto`, so the entire incoming scene
paints in the z-index-0 band, **below** every outgoing `.stack` (2) and
`.railcol` (3) that already leaked to root. Hence the outgoing type floats above
the incoming photo. The moment the tween reaches opacity 1 the incoming section
stops being a stacking context, its own `.railcol` rejoins the z-3 band later in
tree order and wins the rail number — while the outgoing `.stack` still outranks
the incoming `.bg`, which is frame 551 exactly.

The arithmetic confirms it: measured photo blend at t=18.05 / 18.15 / 18.25 /
18.3 is ~7% / ~40% / ~75% / ~87% incoming, matching
`dissolve(0.45, power1.inOut) x fade("#sN-panel", 0.55, power1.out)` to within
read error — so the section tween *is* running; only its paint order is wrong.

**Scope.** All 91 boundaries, both architectures (rail and `v-bleed`), and it is
a property of the shared `assets/blockframe.css`, so every cut built on this
scaffold has it. `hyperframes check` cannot see it: lint is static, and the
layout/WCAG passes sample settled mid-scene frames, never the overlap window.

**Fix — one declaration, in the scaffold, not this cut:**

```css
.scene { isolation: isolate; }   /* or: z-index: 0 */
```

Either confines `.bg`/`.scrim`/`.stack`/`.railcol` to their own scene and makes
each section composite atomically, which is what `sceneTransitions()` has always
documented itself as doing. `isolation` is preferable — it creates the stacking
context without also pinning the sections into the z-0 band, so DOM order keeps
deciding paint order exactly as motion.js's comment claims.

Because the scaffold is the one home for this, the change belongs in
`tools/scaffold/assets/css/blockframe.css` and then in the cut's copy; the
`-en` cut and every future cut need it too. Per the fix-defaults-not-gates rule
this is a **correct default**, not a new gate.

## Not measured this invocation

Runtime, VO drift vs the `data-start` table, peak dBTP, black-segment scan —
all require the master. Deferred to invocation 2.
