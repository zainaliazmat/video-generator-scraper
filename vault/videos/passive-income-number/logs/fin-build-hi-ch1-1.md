---
summary: Chapter 1 («वो सुबह», 7 scenes, 35.745s) built as a standalone HyperFrames project at studio/videos/passive-income-number-hi-ch1. `hyperframes check` passes with 0 lint errors, so the layout and contrast passes actually ran (10/10 WCAG AA). Two real defects were caught by the snapshot pass and fixed — the Lottie data file was never loaded (blank scene, every check green) and the s7 foot orphaned a word on a system max-width — and the corpus/rate build assert is wired and proven to fail in both directions.
updated: 2026-08-07
source: run.json.constraints · storyboard-hi.md §3/§5/§6/§7/§8/§10 · script-hi.md ch1 cue blocks + Build handoff §5 · studio/videos/passive-income-number-hi/assets/voice/timing.json · tools/format.json chapter_design + scene + tiers.medium · knowledge/design-chapter-archetypes.md · tools/scaffold/assets/{blockframe,chapter-design}.css + js/motion.js
stage: fin-build, cut hi, chapter 1, attempt 1
---

# fin-build — hi · CHAPTER 1 · attempt 1

## What was built

`studio/videos/passive-income-number-hi-ch1/` — a standalone chapter project:

| file | what it is |
|---|---|
| `build.mjs` | the generator. Reads `../passive-income-number-hi/assets/voice/timing.json` and a 7-row `SCENES` design table (storyboard §7 verbatim), emits `index.html` **and** `assets/audio.json`. |
| `index.html` | 7 scenes, root **35.745s**, generated. Not hand-edited. |
| `assets/` | per-entry **symlinks** (not a whole-dir link, so `audio.json` can be a real file here): `blockframe.css` / `chapter-design.css` / `js/motion.js` → `tools/scaffold`; `js/gsap.min.js`, `js/lottie.min.js`, `fonts`, `img`, `voice`, `lottie` → the cut. |
| `assets/audio.json` | 7 cues (6 joint `transition` + 1 `buzz`), `bed-resolve`. |
| `assets-ch1/final/` | the 7 backgrounds, untouched (fin-assets'). |
| `node_modules` | symlink to the cut's, `hyperframes` **0.7.66** via the scaffold's committed lockfile (`npm i -D`, no `npx --yes`). |

The cut dir `passive-income-number-hi/` was missing every shared binary, so the
scaffold's `blockframe.css`, `chapter-design.css`, `js/`, `fonts/`,
`img/{grain,wm-hi,wm-en}.png`, `package.json` and `package-lock.json` were copied
into it first. That is the one write outside the chapter dir and it is the cut's
own scaffold, which fin-build for the full cut needs anyway.

## The four gates the orchestrator verifies (§3c)

Checked programmatically against the generated file, not by eye:

1. **`image_per_scene`** — 7/7 scenes carry `has-photo` and a real `.bg` pointing at
   a file that exists on disk. `photo_free_scene_ratio` = 0. ✓
2. **No rail** — the rendered text of the whole chapter is exactly the 13 authored
   strings; no `rail` class, no "chapter", no `N / total`, no slide number. ✓
   (Full extracted on-screen text is in §"What is on screen" below.)
3. **Archetype layer** — every scene's `arch-*`, `--f1`, `centred`, `art-off` /
   Lottie matches storyboard §7 row-for-row: `A A D A D A B`, grounds
   `#241d15 #221c17 #161f2b #1f1b16 #221c17 #1f1e1c #1c2027`, `art-off` on 6 of 7
   and `centred` on 6 of 7 (s3 is the one scene with something real on the other
   side). ✓
4. **The corpus/rate assert** — wired as a `<script>` after `register()`, and
   **proven in both directions**: injecting `₹1,00,00,000` into s1 produced
   `Runtime ✗ page_error: RATE ASSERT FAILED — s1 renders ₹1,00,00,000 with no
   #s1-rate carrying a rate`; adding an `#s1-rate` carrying `3.0%` cleared it.
   Chapter 1 has no corpus frame, so it is vacuously true here and chapters 2-7
   inherit it. ✓

## Timing — generated, and asserted on GAPS

Every `data-start` / `data-duration` / `data-framings`, the `S` and `D` maps, the
7 `<audio>` rows and the root duration come from `timing.json` in one pass.
`build.mjs` refuses to write if any adjacent gap differs from the shipped cut's,
if two neighbours share a track, or if the last scene misses the root — because a
correct total with drifted internal cuts is exactly what a re-time produces.

| s | line | start | dur | d-dur | track | arch | ground | art |
|---|---|---|---|---|---|---|---|---|
| s1 | 1.1 | 0.000 | 3.961 | 4.411 | 1 | A | `#241d15` | off · centred |
| s2 | 1.2 | 3.961 | 5.816 | 6.266 | 2 | A | `#221c17` | off · centred |
| s3 | 1.3 | 9.776 | 2.550 | 3.000 | 1 | D | `#161f2b` | **Lottie** |
| s4 | 1.4 | 12.327 | 4.797 | 5.247 | 2 | A | `#1f1b16` | off · centred |
| s5 | 1.5 | 17.123 | 6.181 | 6.631 | 1 | D | `#221c17` | off · centred |
| s6 | 1.6 | 23.304 | 5.842 | 6.292 | 2 | A | `#1f1e1c` | off · centred |
| s7 | 1.7 | 29.146 | 6.599 | **6.599 bare** | 1 | B | `#1c2027` | off · centred |

Chapter offset **0.000s** — chapter 1 opens the cut, so it is already frame-exact
against the full cut with no rebase. s7 carries its bare duration (a chapter has
no successor to dissolve into); `tools/cut_assemble.py` adds the +0.45 back.
Longest single framing 6.599s against `max_scene_seconds` 9.0. ✓

## Two real defects the max-density snapshot pass caught

Snapshots at each scene's LAST cue time + 0.8s settle, **one `-o` directory per
batch** (`snapshot` wipes its `-o` on every run):

| batch | frames | looked at | what it found |
|---|---|---|---|
| `snapshots/qa/b1` | 7 (1.90, 5.861, 12.076, 14.227, 19.023, 25.204, 31.846) | **all 7** | the two defects below |
| `snapshots/qa/b2` | 2 (11.0, 12.076) | **both** | Lottie fix confirmed |
| `snapshots/qa/b3` | 1 (31.846) | **1** | foot fix confirmed |

The CLI succeeded on the first attempt each time; no navigation-timeout retries
were needed.

1. **The Lottie rendered nothing and every check was green.** `lottie.min.js` was
   vendored but the DATA file was not — `window.L_phone_notify_credit` was
   `undefined`, `loadLottie` drew an empty stage, and lint/runtime/layout/contrast
   all passed. Exactly the failure mode the launch brief warned about, reached by a
   different route (a missing `<script>` rather than the hyphenated file). Fixed by
   loading `assets/lottie/phone_notify_credit.js` — the **underscored** file —
   before `motion.js`, and by adding a one-line guard that **throws** if the global
   is undefined, so a blank Lottie scene is now a build failure rather than a
   review note.
2. **s7's foot orphaned "arithmetic" on its own line.** `.arch-b .foot` is capped
   at 900px because archetype B hangs its type in a left column beside the art
   plate; `.scene.centred` correctly drops the plate, the crule, the vrule and the
   brule and re-centres the stack at 1500px — but it does **not** release that cap.
   Patched in the composition with a `.v-footwide` one-off. See the system gap
   below: the real fix is one rule in `chapter-design.css`, which is a deliberate
   scaffold edit and not a build's to improvise.

## System gaps — reported, not improvised

- **`chapter-design.css`: `.scene.centred` does not release `.arch-b .foot` /
  `.arch-b .huge`'s 900px caps.** Every centred B scene with a foot longer than
  ~58 characters will orphan a word, in both cuts, on every chapter. Suggested
  scaffold edit: `.scene.centred .foot { max-width: 1400px }` beside the existing
  `.scene.centred .plate {display:none}` block. Patched here as `.v-footwide`.
- **`tools/audio/cues.py` carries two PER-VIDEO constants from
  `japanese-money-methods`.** Its output for this chapter is wrong twice:
  `HOLDS` declares `s1→s2` a matched-frame continuous zoom and therefore
  suppresses that joint's `transition` (false here — s1 is an alarm clock, s2 is a
  glass of chai; this cut's only hold is s13→s14 in chapter 2), and `BUZZ` puts the
  diegetic cue on `s1` at +0.95 (s1 is the alarm that did **not** go off;
  storyboard §2 declares it on **s3 at +0.90**). `assets/audio.json` is therefore
  emitted by `build.mjs` from the composition's own scene starts instead, with both
  corrections documented at the point of edit. The generator's density rule is
  right; its video-specific tables want to move into the storyboard or a per-video
  file.

## Copy: one deliberate omission

**s4's `foot:` was dropped.** `script-hi.md` 1.4 carries
`foot: The number is withheld until Chapter 6 — this is the open loop`. That is a
production annotation that landed in an on-screen field: rendering it would put
the chapter structure on screen (gate 2, a hard run rule) and read as a note to
the builder. The scene keeps kicker + focal and lands at 4 countable elements
against a ceiling of 6. Nothing was rewritten — copy is script-owned and inventing
a replacement is not a build's job. **fin-editor / fin-ceo decision owed:** drop it
permanently, or have fin-script issue viewer-facing copy for that slot.

## What is on screen

```
A TUESDAY · The alarm did not go off
THE MORNING · Tea. The window. One buzz.
(no kicker) · Money arrived. While you slept.
NOT RICH · You just reached a number
WHAT IT PAYS · Electricity. Ration. Rent.
RUNG BY RUNG · Smallest rung first
THE CONDITION · Every figure ships with its rate
   A corpus without its withdrawal rate is a promise, not arithmetic
```

Focal sizes are the deterministic rule keyed on `stmt` length, not eyeballed:
112 · 88 · 88 · 88 · 88 · 112 · 88. Nothing below 76. No `.chip`, no role colour
and no `--tint` anywhere in chapter 1 — correct, since §7 gives all seven scenes
`focal · A · —`.

## Motion

`sceneTransitions(IDS, S)` — six 0.45s cross-dissolves, no `shove` (this cut's two
act changes are s37→s38 and s54→s55, both downstream). The **photograph** carries
the move on every scene: `ken` alternating `i o i o i o i`, run for the scene's own
duration so it lands exactly as the next scene fades up. Cue ladder variant A
throughout (kicker +0.30, stmt +1.10, foot +1.90, every gap 0.80s); s3 is the one
declared exception — no kicker, and stmt + `playLottie` share +0.30 because a
2.550s scene cannot afford the +1.10 step. The Lottie runs at true speed (75f @
30fps = 2.50s) so its bloom peaks at +0.80, which is the frame `buzz` at +0.90 is
bound to. Every helper is `motion.js`'s; none is redefined inline.

## `npm run check` — PASSED

```
Lint       0 error(s), 1 warning(s), 2 info(s)
Runtime    0 errors, 0 warnings
Layout     0 error(s), 0 warning(s), 9 info(s)
Motion     0 errors, 0 warnings
Contrast   10/10 text checks pass WCAG AA
Check passed
```

Zero lint errors is the load-bearing part — a lint ERROR makes `check` **skip**
layout and contrast entirely, and the first run did exactly that
(`missing_timeline_registry`: the linter reads the composition, not `motion.js`,
so `window.__timelines = window.__timelines || {};` has to appear in the file
beside `register()`, as the shipped `japanese-money-methods-hi` cut does — its
chapter reference file does **not**, and would have failed here). Fixing it turned
"0 samples / 0 text checks" into 9 layout samples and 10 contrast checks.

The three remaining findings are structural, not defects, and **no design token
was touched to silence them**:

- `container_overflow` ×9 on `#sN-bg` — `.bg` is `inset:-8%` and `ken` scales it to
  1.16; the overflow is the Ken Burns move itself, clipped by `.scene`'s
  `overflow:hidden`. Every shipped cut has it. Candidate scaffold fix if the noise
  ever hides a real one: `data-layout-allow-overflow` on `.bg` in the system, not
  per cut.
- `timeline_track_too_dense` — 4 timed elements on track 1. Inherent to one-line-
  one-scene with a 1/2 alternation; the suggested fix (sub-compositions) would
  break the chapter/assemble pipeline.
- `pointer_events_none` ×2 — `.grain` and `#root::after`, both system, both info.

`format.json known_benign` is `[]`, so none of these has an entry; they are logged
here rather than added, because adding one is a format.json edit.

## Flags for fin-editor (imagery — fin-assets' call, not a build defect)

All seven images are on disk, credited and unique, and every scene satisfies
`image_per_scene`. Three read weaker than their storyboard brief under the grade:

- **s2** — the brief was "chai on a windowsill, morning street out of focus
  behind"; what landed is masala chai on marble with ginger. The line is "Tea. The
  window. One buzz." and the window is not in frame.
- **s4** — the brief was "a single closed brown envelope squared on a bare table".
  Under `brightness(.62)` it reads as a flat dark panel rather than an envelope.
- **s5** — the brief was "three household bills fanned — electricity, a grocery
  slip, a rent receipt"; what landed is a large stack of office paperwork, so the
  frame says "paperwork", not "your three bills". The sound-off rule is per line.

s1 (alarm clock), s3 (phone face-down, correct — the screen is never shown), s6
(stone steps) and s7 (brass balance) all read.

## Owed / next

- Creator review of the chapter draft (fin-editor → fin-ceo), per the
  chapter-by-chapter rule. No render was run — that is fin-render's stage.
- The three scaffold/tooling gaps above, if the orchestrator wants them fixed
  before chapter 2 rather than after chapter 7.
