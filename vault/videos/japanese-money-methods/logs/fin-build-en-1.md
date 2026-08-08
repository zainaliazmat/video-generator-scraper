---
summary: fin-build for japanese-money-methods en, attempt 1. Wrote index.html (92 scenes, ledger-rail, 626.586s) and assets/audio.json (bed-resolve + 24 SFX). `npm run check` passes with the browser passes ACTUALLY RUNNING — 0 lint errors, 0 layout errors, 21/21 WCAG AA; `pipeline_check check build` clean. 92/92 max-density frames captured across 8 batch directories and reviewed; one real defect caught (the CTA rendered white) and fixed.
updated: 2026-08-01
source: storyboard-en.md §1-§12, script-en.md [rail …] cue blocks, assets/voice/timing.json, tools/format.json, tools/scaffold/assets/{blockframe.css,js/motion.js}, logs/fin-build-hi-2.md
stage: fin-build, cut en, attempt 1
---

# fin-build — japanese-money-methods-en, attempt 1

## Result

| | |
|---|---|
| Artifacts | `studio/videos/japanese-money-methods-en/index.html` · `assets/audio.json` |
| Scenes | **92** (one VO line = one clip = one scene), architecture `ledger-rail` (`run.json`) |
| Duration | **626.586s** = `timing.json` total = last scene end (620.692 + 5.894) |
| `npm run check` | **passed** — lint 0 errors / 3 warnings / 3 info · runtime 0 · layout **0 errors**, 13 infos · contrast **21/21 WCAG AA** |
| `pipeline_check check build` | **PASS build-en** |
| Generator | one node script over `timing.json` + the 92 `[rail …]` cue blocks + storyboard §7; no timing number and no on-screen string typed by hand |

Everything timed is generated: `data-start` / `data-duration`, the `S` map, the 92 `<audio>`
rows and the root `data-duration` come from one pass over `timing.json`.
`data-duration = scene_duration + 0.45` on s1–s91, s92 bare; track index alternates 1/2 by
scene parity (matches the storyboard's `trk` column on all 92 rows).

## The scaffold-path fix is confirmed working — the browser passes really ran

The orchestrator's directive was the load-bearing one. The scaffold now ships
`assets/blockframe.css` (no `../` in its `url()`s), the composition emits
`<link rel="stylesheet" href="assets/blockframe.css">`, and lint reports **0 errors** — so
`runCheckPipeline` did **not** short-circuit to `emptyBrowserResult()`. Evidence that the
passes executed rather than reporting a vacuous zero:

- Layout: **13 findings across sampled frames** (t=34.81s, 104.43s, 174.05s … 591.78s), not
  `0 issues across 0 sample(s)`.
- Contrast: **21/21** text checks, not `0/0`.
- Motion and Runtime both reported against real samples.

All 13 layout findings are `info`: `#sN-bg` overflowing `#sN-panel` (the Ken Burns bleed,
clipped by `.v-panel { overflow: hidden }`) plus the three `panel_out_of_canvas` siblings of
the same push. Nothing overflows the safe area.

`.warnc` also confirmed working: s24's padlock renders `--warn` red in the 148.288s frame.
The hi cut's one real defect does not recur.

## The one real defect the snapshot pass caught

**s91's `SUBSCRIBE` rendered white, not `--pop` orange.** The storyboard's §7 focal column
reads `num · **pop**`, which looks like the fourth member of the `fundc / warnc / targetc`
role-class family — **and there is no `.pop` colour class.** `--pop`'s form in
`blockframe.css` is the `.cta` component (filled `--pop` block, `#0d1017` ink, 46px), and
nothing else. A `class="huge pop"` matched nothing and painted `--ink`: exactly the failure
mode `.warnc` had in the hi cut, one token later.

Fixed to `<p class="cta" id="s91-num">` (the hi cut's shape) and re-snapshotted at 617.8s —
the block now renders as the orange CTA. `pipeline_check` and `npm run check` both pass
either way, so **only the visual pass could have caught this**.

> Worth fixing at the source, same family as the `.warnc` note: either add a `.popc`
> colour-only class to `tools/scaffold/assets/blockframe.css`, or make the storyboard
> template write `cta` rather than `pop` in the focal column. This stage may not write
> `tools/`.

## What was built

- `#root class="rail cut-en"` — architecture body class + the **en** watermark class.
  Verified pixel-level: the painted mark has the **pink** ring (`wm-en.png`,
  @moneymavens101), not the green `wm-hi.png` ring. Present bottom-right in all 92 frames,
  including the dark RAIL OFF hook (checked by cropping `frame-00` at 1920×1080).
- Per scene: `.railcol` (`.railno` 2-digit / `.v-hair` / `.raillabel`), `.stack.v-col`
  (`.head2` 54 → focal → `.foot` 26 **or** an icon), `.v-panel` > `.bg` (+ extra framings).
- **7 RAIL OFF scenes** (s1, s17, s33, s43, s65, s77, s90) — rail hidden, photo full-bleed,
  scrim and text-shadow restored, focal stepped UP the ladder: 112 (s1), 240 (s17's
  `30 TIMES`), 88 (s33), 76 (s43/s65/s77/s90). Ladder steps only, never interpolated.
- **11 `num` scenes**, never with a `stmt`. One role colour per scene, from the script's
  `colour:` field. `--pop` exactly once (s91, as `.cta`).
- **5 icons, 0 Lotties**, exactly as §8 declares — all four shapes pasted from the
  git-tracked library, **nothing new drawn, nothing added to `assets/icons/`**:
  `padlock-closed` (s24, `.warnc`), `checkbox-tick` (s38/39/40, `.fundc`),
  `reorder-rules` (s69, `.fundc`). Ids namespaced `sNN-i-*` so the three repeated checkboxes
  do not collide.
- **3 `data-framings`, exactly the three the run directive named**, each partitioning its own
  `scene_duration`: s32 `"5.66,2.48"` (8.140), s36 `"2.74,2.03,3.031"` (7.801),
  s79 `"5.50,2.849"` (8.349). Longest framing anywhere 5.66s against `max_scene_seconds` 9.0.
  Every other scene has one framing and carries no attribute.
- **3 continuous-zoom hold pairs** (s1→s2, s65→s66, s77→s78): the partner scene reuses the
  *same file* with a tighter crop and its `ken` runs in the **same** direction — one
  continuous zoom, never a self-dissolve (creator rule, firaun 2026-07-23). The 0.45s overlap
  stays on all three, as on every other boundary.
- **Two shoves**: `sceneTransitions([…], S, { acts: ["s34", "s74"] })` — s33→s34 out of the
  debunk, s73→s74 into the unpromised fourth. (One scene later than the hi cut's, per D18.)
- `assets/audio.json`: `bed-resolve` + the 24 storyboard cues, all names from
  `tools/audio/kit.json`, sorted, closest pair 6.31s apart. **No music or SFX `<audio>` rows
  in the composition** — voice only, track 10. No compensation for bed length; `mix.py`
  crossfade-loops it per the directive.
- Font subset checked programmatically before writing: every on-screen string (all heads,
  focals, foots, the 8 chapter labels, digits) against the font's **97 codepoints** —
  **0 characters outside it**. `·` `—` `"` `'` `$` `%` all present; no CJK anywhere, romaji
  only, the kanji live inside the s76/s77/s88 photographs.

## s66 — the recut hold partner, aimed as directed

s65 landed on the storyboard's **retry-ladder rung 3** (§12.1): a `$100 + $20` fan on black,
mean luminance ~50, 1880px — a dark-surface money frame with **no ledger and no column
headings**. Per the directive, s66's push-in is aimed at the note's printed panel rather than
at headings that no sourceable frame carried:

```html
<div class="bg" id="s66-bg" style="background-image:url(assets/img/s65.jpg);background-size:auto 150%;background-position:22% 32%"></div>
```

Verified at full resolution (443.88s frame, panel cropped to 740×1080): the frame carries
`…ERVE NOTE`, the serial `…9666 D`, `UNITED STATES OF AMERICA`, `ONE HUNDRED DOLLARS` and the
`100` numeral. That is the `100` / `FEDERAL RESERVE NOTE` field, as specified. **Recording
what the storyboard demanded be recorded: this is rung 3, weaker than a ruled heading, and
6.8's line ("her own expense headings were different ones") is carried by the type, not by
the photograph.**

## System gaps — helpers and components the storyboard assumes that do not exist

Per the stage contract nothing was redefined inline; the nearest existing helper was used
and the substitution is recorded. This table is **identical to the hi cut's** — a fix travels.

| Storyboard asks for | In `motion.js`? | Used instead |
|---|---|---|
| `panelOpen` (clip-path wipe) | no | `fade("#sN-panel", start, 0.55)` |
| `hairDraw` (scaleY from top) | no (`fill` is scaleX) | `fade` |
| `panelSwap` (cross-dissolve in panel) | no | `fade` on the second `.bg` — mechanically identical |
| `railIn` (panel edge 1920→1180) | no | the default `sceneTransitions` dissolve already carries the layout change |
| `ken` at 1.0↔1.06 in the panel | no amplitude argument | system `ken` (1.0↔1.16), clipped by `.v-panel { overflow: hidden }` |

**Components.** Same five `.v-*` one-offs as the hi cut, for the same reasons (`.v-panel`,
`.v-col`, `.v-hair`, `.v-stmt`/`.md`/`.lg` at 44/54/88, `.v-bleed`/`.v-full`), plus
`#root { position: relative; width: 1920px; height: 1080px; overflow: hidden }` — **still
owed to the scaffold.** `blockframe.css` styles everything inside `#root` but never sizes the
stage, and `.scene { position: absolute }` / `#root::after` both need a positioned, sized root.

`window.__timelines = window.__timelines || {};` above `register()` is also still needed:
`missing_timeline_registry` is a regex over the composition file only, so `register()` inside
the linked `motion.js` is invisible to it. Also a scaffold-level fix.

Remaining lint after both: **0 errors**. The 3 warnings are `composition_file_too_large`
(2477 lines) and `timeline_track_too_dense` (46 clips per track ×2) — intrinsic to a 92-scene
LONG cut, and both advise splitting into sub-compositions, which would break the single-file
archive contract.

## The rail label is the CHAPTER, not the per-scene beat

Same divergence the hi cut landed on, for the same measured reason. Storyboard §7's `rail
beat` column duplicates the `head:` string on a large fraction of the en scenes too — s3
`THEN RENT` / head `THEN RENT`, s5 `AND THEN` / `AND THEN`, s2 `IT LANDED` = s1's head, and
so on. Built as specified, those scenes print the same words twice. Reverted to the script's
own spec ("At LONG the label is the chapter name, persisting for the whole chapter so the
rail reads as a spine"), which gives the eight chapter labels: `YOUR PAYCHECK MONTH` ·
`JAPAN'S TWO NUMBERS` · `WHERE IT GOES` · `MOTTAINAI` · `HARA HACHI BU` · `KAKEIBO` ·
`TARU WO SHIRU` · `TONIGHT`. Duplication drops to the four scenes that open a chapter with
its own name (s34, s47, s59, s74). Running index + panel photograph carry per-scene variance.

## Other decisions worth knowing

- **Anchored cues use the storyboard's fallback fractions**, not faster-whisper word timings
  (§4 permits it). All twelve anchored arrivals were checked against the assembly: every one
  clears `cue_min_gap_seconds` 0.8 from the preceding content cue, and the foot on an
  anchored scene is pushed to `max(start + 2.20, anchor + 0.80)`.
- **`countUp` is not used.** All eleven `num` focals are percentages, ratios or words
  (`37.8%`, `ABOUT 1%`, `30 TIMES`, `4 IN 10`, `OVER 20%`, `$200`) and `countUp` rounds to
  integers, so they arrive with `pop`. `.huge`/`.mega` already carry `tabular-nums`;
  `Intl.NumberFormat("en-US")` grouping is baked into the strings the script wrote.
- **Statement focal size is chosen by string length** — ≤28 chars → 88, ≤42 → 54, else 44.
  All three are ladder steps; nothing is interpolated and nothing focal drops below 44 in the
  760px rail column (§3's own correction specifies 44 as the `.rail` statement size).
- **Element budget** never exceeds 5 (`idx`, `beat`, `head`, focal, one of `foot`/`icon`)
  against the ceiling of 6. No scene carries both a `foot` and an `icon`.
- Icons render at `.icon.sm` (130px). The storyboard says 96×96, which is not a system size.

## QA — the max-density snapshot pass

Timestamps are each scene's **last cue time + 0.55s**, clamped inside the scene, derived from
the generated cue list rather than guessed. **One `-o` directory per batch, never shared** —
`hyperframes snapshot` wipes `-o` on every run.

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
| b9-cta | s91 re-check | 1 | 1 frame, cropped |

**92 of 92 frames captured and reviewed** — all 15 contact sheets read at full size, plus
four frames opened at 1920×1080 and cropped (s1 bottom-right for the watermark colour, s66
panel for the note crop, s87 panel to confirm the ledger is Latin script and not a non-US
market signal, s91 for the CTA fix). Nothing overflows; the rail, index, hairline, chapter
label, panel gradient and watermark are present and correctly placed in every frame. All
three hold pairs and all four panel swaps fired at the right times (s32 verified at 211.647s,
s36's second swap at 240.628s, s79 at 537.766s).

`hyperframes snapshot` threw `Navigation timeout of 10000 ms exceeded` constantly, unaffected
by `--timeout`: worst case **b8 failed 20 consecutive tries**, then succeeded on try 4 of a
fresh invocation; b6 needed 12 tries, b3 six, b1 one. Every batch was retried until it
succeeded. **No batch was skipped and no frame went unreviewed.**

## Owed to other stages — image content that does not match its slot

The asset gate passed and every file is on disk, but three promoted photographs are not what
§7/§9 specified, and one of them argues against its own type. Flagged for gate ②, not fixed
here (fetching is not this stage):

1. **`s32b.jpg` is a second weathered wall, not the vintage savings-campaign poster.** The
   swap at +5.66 fires correctly and the two textures are visibly different (grey cracked
   plaster → orange rust), but nothing in the frame reads as a government poster. The scene's
   `data-framings` is therefore currently a texture change, which is close to the cosmetic
   framing the new check exists to reject. **One file re-fetch fixes it; nothing in the
   composition changes.**
2. **`s77.jpg` has no square opening.** 7.4's focal says "All four share one part — the empty
   square at the centre" over a photograph of a bamboo spout and a round basin. This is the
   "check what the picture is saying" test failing outright, and it is the cut's second-most
   exposed frame (RAIL OFF, full-bleed, 14.3s across the s77→s78 hold).
3. **`s79.jpg` / `s79b.jpg` are approximations** — an American kitchen with no diploma or car
   keys, and an apartment block with no sedan. Legible, but the swap loses the specific
   "the phone, the car, the apartment" anchor the framing was declared for.

## Owed elsewhere

1. **`tools/scaffold/`**: a `.popc` colour-only class (or a storyboard-template fix), the
   `#root` stage sizing, and the `window.__timelines` init line. The `assets/blockframe.css`
   path move landed today and is confirmed working — the `known_benign` entry is correctly
   gone.
2. **`bed-resolve` is 248s against a 626.586s cut** (§2, D23) — `mix.py` will dip to silence
   at ≈248.0s (inside s37) and ≈496.0s (inside s73, a DRY `num` scene 2.0s before SHOVE #2).
   Not fixable from this stage; `audio.json` deliberately does not compensate.
3. **`format.json cuts.en.chars_per_second`** is still owed its raise from 16.1 — this cut is
   the third flat measurement above 17.3 (17.39 c/s). Both-or-neither: the budget formula
   first, then the key. `tools/` is not writable here.
