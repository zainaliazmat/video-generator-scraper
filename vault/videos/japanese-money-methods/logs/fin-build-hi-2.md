---
summary: fin-build for japanese-money-methods hi, attempt 2 (attempt 1 died mid-stream to an infra error). Wrote index.html (92 scenes, ledger-rail, 659.709s) and assets/audio.json (bed-resolve + 24 SFX). `npm run check` passes — 0 lint errors, 0 layout errors at 92 max-density frames, 17/17 WCAG AA; `pipeline_check check_build` clean. Four system gaps found and worked around; one real defect caught by the snapshot pass.
updated: 2026-08-01
source: storyboard-hi.md §1-§10, script-hi.md [rail …] cue blocks, assets/voice/timing.json, tools/format.json, tools/scaffold/assets/{css/blockframe.css,js/motion.js}
stage: fin-build, cut hi, attempt 2
---

# fin-build — japanese-money-methods-hi, attempt 2

## Result

| | |
|---|---|
| Artifacts | `studio/videos/japanese-money-methods-hi/index.html` · `assets/audio.json` |
| Scenes | **92** (one VO line = one clip = one scene), architecture `ledger-rail` (`run.json`) |
| Duration | **659.709s** = `timing.json` total = last scene end (652.457 + 7.252) |
| `npm run check` | **passed** — lint 0 errors / 3 warnings / 3 info · runtime 0 · layout 0 errors · contrast **17/17 WCAG AA** |
| `pipeline_check check_build` | **CLEAN** |
| Generator | one node script over `timing.json` + `script-hi.md` + storyboard §7; no timing number typed by hand |

Everything timed is generated: `data-start` / `data-duration`, the `S` map, the 92
`<audio>` rows and the root `data-duration` all come from one pass over `timing.json`.
`data-duration = scene_duration + 0.45` on s1–s91, s92 bare; track index alternates 1/2 by
scene parity (matches the storyboard's `trk` column on all 92 rows).

## What was built

- `#root class="rail cut-hi"` — architecture body class + the watermark class. Watermark
  verified visible bottom-right in every snapshot.
- Per scene: `.railcol` (`.railno` 2-digit / `.v-hair` / `.raillabel`), `.stack.v-col`
  (`.head2` 54 → focal → `.foot` 26 **or** an icon), `.v-panel` > `.bg` (+ second framing).
- 7 RAIL OFF scenes (s1, s17, s33, s43, s65, s76, s90) — rail hidden, photo full-bleed,
  scrim and text-shadow restored, focal stepped up the ladder (112 / 88 / 76; s17's
  `30 TIMES` at 240 as the storyboard specifies).
- 10 `num` scenes, never with a `stmt`. One role colour per scene, from the script's
  `colour:` field. `--pop` exactly once (s91, as the `.cta` block).
- 6 icons from the git-tracked library — **nothing new drawn, nothing added to
  `assets/icons/`**: `padlock-closed` (s24), `checkbox-tick` (s38/39/40),
  `reorder-rules` (s69), `pen-nib-line` (s83). Ids namespaced `s24-i-*` so the three
  repeated checkboxes do not collide. 0 Lotties, as declared.
- Panel swaps: s19 +5.20, s25 +5.40, s32 +5.00, s36 +3.10 / +5.60 — a second `.bg` inside
  the panel, `fade` + its own `ken` for the remainder.
- `data-framings="5.20,3.985"` / `"5.40,3.602"` / `"5.00,4.760"` on s19/s25/s32. Sums
  partition each scene's own duration; longest framing 5.40s against `max_scene_seconds` 9.0.
- Grade override applied exactly once: `s36c` cut-in gets inline
  `filter: grayscale(.32) brightness(1.35)` (fin-assets-hi). Verified in the 245.27s frame
  — the truck reads as a lit silhouette, not a black rectangle.
- `assets/audio.json`: `bed-resolve` + the 24 storyboard cues, all names from
  `tools/audio/kit.json`, sorted, closest pair 5.9s apart. No music or SFX `<audio>` rows in
  the composition — voice only, track 10.

## The one real defect the snapshot pass caught

**s24's padlock rendered white, not red.** The storyboard (§8) and the `.icon` comment
inside `blockframe.css` both name a class **`.warnc`** — **it does not exist**. The
stylesheet defines `.warn` / `.fundc` / `.targetc` / `.inkc`. `.fundc` worked, so the five
green icons were fine and only the single red one was silently uncoloured. Fixed to
`.warn` and re-snapshotted (147.06s): padlock now `--warn` red.

> Worth fixing at the source: the comment in `tools/scaffold/assets/css/blockframe.css`
> above `.icon` says "`.fundc`/`.warnc`/`.targetc`", which is what the storyboard copied.
> Either rename `.warn` → `.warnc` (it collides with the `.chip.warn` / `.stamp.warn`
> modifiers) or fix the comment. This stage may not write `tools/`.

## System gaps — helpers and components the storyboard assumes that do not exist

Per the stage contract I did not redefine anything inline; I used the nearest helper that
exists and am recording the substitutions.

| Storyboard asks for | In `motion.js`? | Used instead |
|---|---|---|
| `panelOpen` (clip-path wipe) | no | `fade("#sN-panel", start, 0.55)` |
| `hairDraw` (scaleY from top) | no (`fill` is scaleX) | `fade` |
| `panelSwap` (cross-dissolve in panel) | no | `fade` on the second `.bg` — mechanically identical |
| `railIn` (panel edge 1920→1180) | no | the default `sceneTransitions` dissolve already carries the layout change |
| `ken` at 1.0↔1.06 in the panel | no amplitude argument | system `ken` (1.0↔1.16), clipped by `.v-panel { overflow: hidden }` |

**Components.** `blockframe.css`'s `.rail` is a different DOM from the storyboard's §3
sketch: it ships `.railcol` / `.railno` / `.raillabel` and makes `.bg` itself the 740px
panel; there is no `.idx`, `.hair`, `.beat` or `.panel`, and no statement size between
`.head2` 54 and `.huge` 112. Five one-offs in the composition's own `<style>`, all `.v-*`:

- `.v-panel` — a clipping parent for the panel. Without it a `ken` push scales `.bg` past
  its own left edge into the type column, and a second framing has nothing to stack in.
- `.v-col` — `padding-right: 860px` so type stops at x=1060, 120px clear of the panel.
  `.rail .stack` alone lets a line run to x=1770, straight across the photograph.
- `.v-hair` — the ledger rule between index and label.
- `.v-stmt` / `.md` / `.lg` — the statement focal at **44 / 54 / 88**, all on the ladder,
  chosen by string length. The 760px rail column cannot hold a 76px focal (14 characters a
  line); the storyboard's §3 correction 1 already anticipated this and specified 44 as the
  `.rail` statement size. Weight (500/600/800 against the head's 900) is what separates head
  from focal, so "two type sizes per scene" survives.
- `.v-bleed` / `.v-full` — the 7 RAIL OFF scenes: rail hidden, `.bg` full-bleed at the
  blockframe grade, `.scrim` and `text-shadow` switched back on.
- Plus `#root { position: relative; width: 1920px; height: 1080px; overflow: hidden }` —
  **`blockframe.css` styles everything inside `#root` but never sizes the stage**, and
  `.scene { position: absolute }` / `#root::after` both need a positioned, sized root. That
  belongs in the scaffold.

## Two lint findings that are scaffold bugs, not composition bugs

1. **`invalid_parent_traversal_in_asset_path` is no longer cosmetic.** `runCheckPipeline`
   calls `shouldBlockRender(...)` on the lint result and returns `emptyBrowserResult()` if
   there is **any** lint error — so while this finding stands, `hyperframes check` skips the
   browser entirely and reports `Layout: 0 issues across 0 sample(s)`, `Contrast: 0/0`. Four
   cuts have shipped with the runtime, layout, motion and contrast gates silently not run.
   I applied the `preferred_fix` already recorded in `format.json known_benign`, inside this
   project only: `assets/css/blockframe.css` → **`assets/blockframe.css`**, with `url(../fonts/`
   → `url(fonts/` and `url(../img/` → `url(img/`. Byte-identical otherwise; browser
   resolution is unchanged (both forms resolve to `assets/fonts/…`), and the font, grain and
   watermark are all visible in the snapshots. **Owed: the same move in
   `tools/scaffold/`, then delete the `known_benign` entry.**
2. **`missing_timeline_registry`** — the lint is a regex over the composition file only, so
   `register()` inside the linked `motion.js` is invisible to it. The composition carries
   `window.__timelines = window.__timelines || {};` above `register()` to satisfy it. Also
   a scaffold-level fix (or a `data-no-timeline`-style opt-out) rather than per-cut boilerplate.

Remaining after both: **0 lint errors**. The 3 warnings are `composition_file_too_large`
(2491 lines) and `timeline_track_too_dense` (46 clips per track) — both intrinsic to a
92-scene LONG cut and both advise splitting into sub-compositions, which would break the
single-file archive contract. The 16 layout infos are all `#sN-bg` overflowing `.v-panel`:
that is the Ken Burns bleed, and it is clipped.

## Divergence from the storyboard: the rail label is the CHAPTER, not the beat

Storyboard §3 correction 2 replaced the script's persisting chapter label with a per-scene
beat name, for variance. Built that way, **39 of the 85 rail-on scenes printed the same
words twice** — `raillabel` and `head2` were identical strings ("WHO IS IN", "RECAP TWO",
"THE METHOD"…). Reverted to the script's spec: eight chapter labels
(`AAPKA SALARY MONTH` … `AAJ RAAT KA EK KAAM`). Duplication drops to three scenes
(s34/s47/s59), which are exactly the scenes that open a chapter with its own name. The
running index and the panel photograph carry the per-scene variance.

## Other decisions worth knowing

- **Anchored cues use the storyboard's fallback fractions**, not faster-whisper word
  timings. All eleven anchored arrivals were checked against the assembly: none lands
  within 0.8s of another content cue (the foot on a `num` scene is pushed to
  `max(start+2.20, num+0.80)`). Word alignment was not run; §4 permits the fallback.
- **`countUp` is used once** (s55, `₹1,500`, `Intl.NumberFormat("en-IN")`). The other nine
  `num` focals are percentages or words (`ABOUT 1%`, `30 TIMES`) and `countUp` rounds to
  integers, so they arrive with `pop`. `.huge`/`.mega` already carry `tabular-nums`.
- **Hold pairs** (s1→s2, s65→s66, s76→s77): the partner scene reuses the same file with
  `background-size: auto 130%` — a genuinely tighter crop of the identical photograph — and
  its `ken` runs in the **same** direction. No self-dissolve; the 0.45s overlap stays, as on
  every other boundary.
- **Two shoves**, `sceneTransitions([...], S, { acts: ["s34", "s73"] })`.
- Icons render at `.icon.sm` (130px). The storyboard says 96×96, which is not a system size.
- Every on-screen string was validated against the font's 97-codepoint subset before
  writing: **0 characters outside it** (`·`, `—`, `’`, `₹` are all present).
- `s65` keeps the simplest possible wiring — one `.bg`, one file — so a creator-supplied
  flat-lay is a file swap and nothing else. `s66`'s "tighter crop on one handwritten label"
  is not honourable with the fallback photograph (fin-assets-hi); it holds a tighter crop of
  the ₹ fan instead.

## QA — the max-density snapshot pass

Two passes, both at the same 92 timestamps: each scene's **last cue time + 0.55s**, clamped
inside the scene. Times derived from the generated cue list, not guessed.

1. **Geometric.** `hyperframes check --at <92 times>` → **0 errors, 0 warnings**, 155 infos
   (all of them the clipped `.bg` ken bleed), contrast 19/19. No text overflows the safe
   area at any scene's densest frame.
2. **Visual.** `hyperframes snapshot` in **8 batches, one `-o` directory each**
   (`snapshots/qa/b1 … b8`, plus `b9-icons` for the re-check) — never a shared directory,
   because `snapshot` wipes `-o` on every run.

| batch | scenes | frames on disk | contact sheets read |
|---|---|---|---|
| b1 | s1–s12 | 12 | 2 |
| b2 | s13–s24 | 12 | 2 |
| b3 | s25–s36 | 12 | 2 |
| b4 | s37–s48 | 12 | 2 |
| b5 | s49–s60 | 12 | 2 |
| b6 | s61–s72 | 12 | 2 |
| b7 | s73–s84 | 12 | 2 |
| b8 | s85–s92 | 8 | 1 |
| b9-icons | s24, s38, s83 | 3 | 1 |

**92 of 92 frames captured and reviewed** — all 15 contact sheets read at full size, plus
four frames opened at 1920×1080 (s2 for the rail geometry, s24 twice for the icon colour,
s69 cropped to confirm the `reorder-rules` icon was drawn and not clipped). Nothing
overflowed; the rail, index, hairline, chapter label, panel gradient and watermark are
present and correctly placed in every frame; both hold pairs and all five panel swaps fired
at the right times.

`hyperframes snapshot` threw `Navigation timeout of 10000 ms exceeded` on 12 of 20
invocations, unaffected by `--timeout`. Every batch was retried until it succeeded (worst
case 5 tries); no batch was skipped.

## Owed to other stages

1. **`tools/scaffold/`**: the `assets/blockframe.css` path move (deletes a `known_benign`
   entry and restores the layout/motion/contrast gates), the `#root` stage sizing, the
   `window.__timelines` init line, and the `.warnc` comment.
2. **`bed-resolve` is 248s against a 659.709s cut** (storyboard §2) — `mix.py` will dip to
   silence at ≈248s and ≈496s. Not fixable from this stage.
3. **s65 is still the fallback photograph**, not the four-group flat-lay (storyboard §12).
