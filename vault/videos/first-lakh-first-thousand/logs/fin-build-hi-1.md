---
summary: fin-build, hi cut, attempt 1 — 86-scene swiss-band composition generated from timing.json (514.789s). pipeline_check check_build PASSES; `npm run check` has ONE remaining error and it is in the system stylesheet (`../fonts/`, `../img/`), which this stage may not edit. Three system defects found and worked around; three storyboard helpers do not exist and were mapped to the nearest system ones.
updated: 2026-07-31
source: storyboard-hi.md + script-hi.md + studio/videos/first-lakh-first-thousand-hi/assets/voice/timing.json + tools/format.json + tools/scaffold/
stage: fin-build, cut hi, attempt 1
---

# fin-build — «पहला एक लाख» hi, attempt 1

## Result

| | |
|---|---|
| Composition | `studio/videos/first-lakh-first-thousand-hi/index.html` (86 scenes, 98 KB) |
| Generator | `build.mjs` — every duration derived from `assets/voice/timing.json`, nothing hand-typed |
| Duration | **514.789 s** (8:35), root == timing.json total == last scene end |
| `pipeline_check check build` | **PASS** |
| `npm run check` | **1 error, 89 warnings** — the one error is in the linked system stylesheet (below) |
| Snapshots | all 86 scenes captured at their max-density cue and eyeballed; times in `snapshots-at.txt` |

## What was built

- Scaffolded from `tools/scaffold/` — pinned `hyperframes 0.7.66` via the committed lockfile
  (`npm i -D`), vendored GSAP, self-hosted FinanceSans, `grain.png`. **No network reference
  of any kind** in the composition; `check` confirms.
- `blockframe.css` and `motion.js` are **linked, not copied**. The composition adds only
  `.v-*` one-offs, all in one inline `<style>` after the link.
- `data-start`/`data-duration`, the JS `S` map, the 86 `<audio>` rows and the root duration
  are all emitted from `timing.json` in one pass, so the four homes cannot drift.
- Transitions: `sceneTransitions(..., { acts: ["s46","s58"] })` — 83 dissolves + the two
  shoves the storyboard names (5.8→5.9, 6.10→7.1). Scenes 1–85 carry
  `scene_duration + 0.45`; tracks alternate 1/2. Both asserted by `check_build`.
- Continuous-zoom pairs (1.1+1.2, 1.5+1.6, 5.2+5.3): **one `ken` tween across both
  scenes' `.bg` elements**, so the phase matches at the boundary and the 0.45 s crossfade
  is invisible. s40 takes a tighter crop (`background-size:132%`) of the same source, per
  the storyboard's remedy for the 9 s hold.
- `assets/audio.json`: `bed-resolve` + the 22 SFX cues, absolute seconds, all names from
  `tools/audio/kit.json`, closest pair 2.40 s apart. No music/SFX `<audio>` rows in the
  composition — voice only, track 10.
- The one permitted per-scene grade override is on s46 (`brightness(1.40)`), per fin-assets
  note 1. No second override.

## The one remaining `npm run check` error — a SYSTEM defect, not a composition defect

```
✗ invalid_parent_traversal_in_asset_path: Found 2 asset path(s) traversing above the
  project root with "../" (../fonts/, ../img/)
```

Both strings are in `tools/scaffold/assets/css/blockframe.css` (lines 24 and 79); the
composition itself contains no `../`. **This stage may not write `tools/`, and diverging the
project's copy of the stylesheet is exactly what the 2026-07-29 audit forbids**, so it is
reported rather than patched.

It is a **false positive for a linked stylesheet**: CSS `url()` resolves against the
*stylesheet*, so `assets/css/../fonts/` is `assets/fonts/` — inside the project. Verified
empirically, not by argument: every snapshot renders in real FinanceSans at weight 900 with
`₹` present (not the Arial Black fallback the audit found on four cuts), and `grain.png` is
visible. Runtime check: 0 errors.

**Minimal correct fix, for whoever owns `tools/`:** move `blockframe.css` up one level to
`assets/blockframe.css` and change the two urls to `fonts/NotoSansFinance-var.woff2` and
`img/grain.png`. No `../`, and still correct relative to the stylesheet. Do **not** take the
linter's suggested `assets/fonts/...` — from `assets/css/` that resolves to
`assets/css/assets/fonts/` and 404s for real.

## Three more system defects found (worked around inside the composition)

1. **swiss-band puts the rule and the statement in different columns.** `blockframe.css`
   gives `.swissbar` `grid-row: 2` and both `.swissrule` and `.stack` `grid-row: 4`, but
   never a `grid-column`. Two items declaring only a row are auto-placed into two *implicit
   columns*: the rule and the statement rendered side by side, the black title bar stopped
   mid-frame, and every bar wrapped to three lines. Snapshot-confirmed. Worked around with
   `.v-col1 { grid-column: 1 }` on all three. **This is the first swiss-band build, so the
   variant had never actually rendered** — the fix belongs in the system.
2. **`.stamp.warn` paints the verdict red on red.** `class="stamp warn"` matches both the
   fill modifier `.stamp.warn` *and* the text-colour modifier `.warn`, and `.warn` is
   declared after `.stamp` at equal specificity, so it wins. s19 rendered as an **empty red
   block**. Worked around with `.stamp.v-stamp { color: #0d1017 }`. Every role stamp in
   every architecture has this bug.
3. **86 `<audio>` rows stall page load past the snapshot CLI's fixed 10 s navigation
   timeout.** Every snapshot failed until `preload="none"` was added to the rows; with it,
   they pass consistently. Measured both ways. `id` on each row is separately required
   (`media_missing_id` — without it the render is SILENT).
   ⚠ **fin-render should confirm the master actually carries voice**, since `preload="none"`
   is new here and `check_render` only compares duration.

## Storyboard helpers that do not exist in `motion.js`

The storyboard §4 names `bandOpen`, `hang16`, `hang12`, `ruleDraw`, `scaleArrive`, `wipeX`
and `wipeY`. None is in the system. Per the fin-build contract they were **not invented
inline**; each was mapped to the nearest existing helper:

| storyboard | used | note |
|---|---|---|
| `bandOpen` (aperture iris) | *dropped* | the scene's own `dissolve` already is the aperture arriving; a second reveal on the same element is noise |
| `hang16` / `hang12` | `rise(sel, at, dur, 16 / 12)` | `rise` already takes the travel distance |
| `ruleDraw` | `fill` | `scaleX 0→1`; needed `.v-ruledraw { transform-origin: left }` because `.swissrule` has none |
| `scaleArrive` | `rise(..., 12)` | storyboard §3 retires `back.out` in swiss-band, which rules out `pop` |
| `wipeX` / `wipeY` (tone, mosaic minor) | `fade` | a hard directional wipe is not in the vocabulary |

Also unavailable: **half-amplitude `ken`**. `ken(sel, at, dur, zoomIn)` has fixed endpoints
(1.0↔1.16, ∓2.5 xPercent), so the storyboard's `1.0↔1.06 / ∓1.2` inside the band is not
expressible without an edit to `motion.js`. The system amplitude is used everywhere.
Consequence handled: the system's `.swiss-band .bg` has no horizontal bleed, so the
xPercent move would expose a 48 px strip of `--bg`; the `.v-ap` wrapper gives the photo
`left:-3%; width:106%` inside a fixed, untransformed window.

**The `.v-ap` apertures also deliberately avoid `clip-path`** — `check` warns that ~40
clip-path/blur/gradient elements make the capture layer emit solid black for half a render,
and 86 scenes would have carried 92 of them. The window is the wrapper's own box +
`overflow:hidden` instead. Warning count dropped accordingly.

## Design decisions the audit should look at

- **Grade.** The storyboard asks for `grayscale(.85) brightness(.55) contrast(1.25)` in
  swiss-band. The system ships `grayscale(.32) brightness(.62) contrast(1.05)` and a grade
  is a **design token**, so it was NOT edited to match prose. Visible consequence: the
  colour scenes (s43/s83 roadside verge, s58 green tanks) are the most saturated frames in
  the cut. If the darker swiss grade is wanted it is a deliberate edit to
  `tools/scaffold/assets/css/blockframe.css`, not a per-video override.
- **Type sizes come from the system, not the storyboard's prose.** Bar = `.huge` in
  `.swissbar` (96 px), focal `num` = `.huge` (112), focal `stmt` = `.head2` (54), foot = 26.
  The storyboard's 84/200/54 are not on the ladder (200 is not; 240 will not fit a 240 px
  zone). Bars, nums and stamps **step DOWN the ladder** when a line will not fit its column
  — never interpolated. Only one bar reaches the bottom of that walk: s17
  "WHAT THE MARKET BOUGHT YOU" at 54 px in the 1055 px reversed-field column.
- **Furniture merged into the foot.** `mark` + `idx` render as one 26 px muted prefix
  (`CH 4 · 37 / 86 · …`) instead of two absolutely-positioned elements needing per-aperture
  offsets. Keeps the 240 px statement zone at bar + one focal + one 26 px line, which is the
  two-sizes rule the style is built on, and guarantees every scene carries a foot.
- **Forbidden glyphs.** `→` is drawn with `.arr`; `~` was rewritten as "around" / "roughly"
  / "NEAR" (`~₹5,00,000` → `NEAR ₹5,00,000`), `×` as "for 12 months". `·`, `—` and `–` are
  in the subset (318/324 uses across shipped cuts).
- **s42 (5.5) built as a plain `B` scene**, not a mosaic — fin-assets dropped `s42m` rather
  than fake it. Mosaic count is 6, not 7.
- **s27's verdict has no role colour** in the storyboard; `.stamp` with no modifier has no
  fill and dark text, i.e. invisible. Rendered on `--ink` via `.v-stamp-ink`.

## Still open (not this stage's to close)

- **Anchored cues are the storyboard's `f` fallbacks, not word-level timings.**
  faster-whisper is outside this stage's allowlist. The absolute times from storyboard §2/§6
  are asserted at build time to fall inside their own scene.
- **The hard directional wipe is unproven against `ffmpeg scdet`** (storyboard §10). It is
  built as the system `dissolve` at the same 0.45 s, so the scene arithmetic is identical
  either way and the fallback is already the shipped state.
- **`bed-resolve` is 248 s against a 514.789 s cut** — `run.json owed_before_mix` still
  stands, unchanged by this stage.
