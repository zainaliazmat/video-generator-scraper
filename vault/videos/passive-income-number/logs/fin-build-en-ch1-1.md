---
summary: fin-build en chapter 1 — RESUMED after an API transport death, verified from encoded frames rather than source, and passed. 8 scenes / 46.42s, hyperframes check clean (0 errors, contrast 10/10 AA), Lottie proven to animate, both rate asserts proven to execute. One tooling false positive found in check_build's Lottie regex.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1/ · storyboard-en.md §7/§8 · timing.json (81 lines, 527.873s) · tools/format.json chapter_design · tools/audio/kit.json
stage: fin-build, cut en, chapter 1, attempt 1 (resume)
---

# fin-build — en · chapter 1 · attempt 1 (RESUME)

The previous invocation of this attempt died on an API transport error at the line
"Now let me actually look at every frame" — i.e. it had produced the artifacts and
died at the one step that matters. Nothing was rebuilt. **This run is the
verification that never happened**, plus the two gates.

## What was already on disk, and what I confirmed about it

`index.html` (21.6 KB, 8 scenes), `build.mjs`, `assets/audio.json`, the symlinked
system + voice + Lottie, `node_modules`, and two orphaned snapshot batches.

**`index.html` is genuinely the generator's output, not a hand-edited descendant
of it.** Re-running `node build.mjs` reproduces both `index.html` and
`assets/audio.json` **byte-identically** (`md5 01153f33…` / `e4110969…` before and
after). That matters more than it sounds: it means the timings in the DOM, the `S`
map, the eight `<audio>` rows and the root duration all came from one derivation
of `timing.json`, and the four copies cannot have drifted apart by hand.

Timing checked against `timing.json`'s chapter-1 slice, verbatim:

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|
| start | 0 | 3.543 | 9.254 | 14.599 | 21.564 | 25.551 | 31.262 | 38.149 |
| own dur | 3.543 | 5.711 | 5.345 | 6.965 | 3.987 | 5.711 | 6.887 | 8.271 |
| `data-duration` | 3.993 | 6.161 | 5.795 | 7.415 | 4.437 | 6.161 | 7.337 | **8.271** |
| track | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |

All seven joints overlap by exactly 0.450s; tracks alternate 1/2 throughout; s8
carries its **bare** duration because a chapter has no successor
(`cut_assemble.py` adds the +0.45 back at fold-in). Root `data-duration` 46.42 =
38.149 + 8.271 = the `scene_start` of line 2.1. Nothing re-timed.

## The frame pass — 33 frames, four batches, one `-o` dir each

Batches b1 and b2 survived the dead run; b3 and b4 are new. **Every batch has its
own `-o` directory** — `snapshots/qa/b1…b4` — because `hyperframes snapshot`
wipes its output dir on every invocation.

| batch | frames | what it samples | how many I actually looked at |
|---|---|---|---|
| b1 | 8 | each scene's LAST cue time (max-density worst case) | **8 of 8, at full 1920×1080**, plus the contact sheet |
| b2 | 8 | the s3→s4 hold and the Lottie draw, densely | 8 of 8, contact sheet |
| b3 | 8 | each scene's start +0.05 | 8 of 8, contact sheet |
| b4 | 9 | the six remaining joints at **+0.38** (`format.json qa.dissolve_sample_offsets` — the only offset where both scenes' text can be up), plus 44.0 / 46.30 / 46.41 | 9 of 9, contact sheet |

Both snapshot batches succeeded on the first invocation; the documented
`Navigation timeout` flake did not occur, and the retry loop was in place if it had.

### 1. Every scene paints a photograph — proven, not assumed

All eight `.bg` files are **distinct** (eight distinct md5s), and all eight are
visible as real graded photographs in b1's full-res frames. This is the failure
mode where `image_per_scene` is satisfied by a file that loads and never paints;
it did not happen here. s1 at **t=0.05s** is already a photograph — the first
frame of the video is not black.

s3 and s4 share a source by design (§6b matched-frame hold) but are genuinely two
different framings: `s3.jpg` 1733×1300 and `s4.jpg` 1600×900, the latter recorded
in its `.src` as `ffmpeg crop=1600:900:133:290` on the promoted s3 source. The
continuous zoom is `plateKen 1.00→1.08` then `1.08→1.16`, so it reads as one
uninterrupted push and never as a self-dissolve back to the same file.

### 2. The Lottie draws AND animates

Four distinct states across the frames, which is what distinguishes "it drew" from
"it animated": at **15.9s** the shell plus the `$` chip and a stub bar, at
**16.449s** the short bar plus the right-hand time bar, at **18.499s** fully
assembled, at **21.62s / 21.944s** holding its last frame under the outgoing
dissolve.

The asset's own header confirms the geometry the composition assumes:
`ip 0 · op 75 · fr 30 · w 820 · h 300` — **75 frames at 30 fps = 2.500s exactly**,
matching `playLottie(s4art, S.s4 + 1.13, 2.50)`, and a native 820×300 box matching
`.v-lstage`'s declared `820px × 300px`, so it renders 1:1 with no scaling at all.
The `$` glyph is legible in every frame after +1.5 — that is the hi cut's ch1
blocker ("a banner with no ₹ says *a notification arrived*, not *money arrived*")
closed on the en side.

### 3. Every dissolve fires against a live frame; nothing is blank

b4 catches all six remaining joints at +0.38 and b2 catches the seventh (s3→s4 at
14.979s). In every one, the outgoing scene's type is ghosted at partial opacity
**over the incoming photograph**, with the incoming kicker already up — i.e. two
live scenes, never a fade against black. b3 independently confirms the outgoing
side: at each scene's start +0.05 the previous scene is still fully composed.

The tail is correct for a chapter: at **44.0s, 46.30s and 46.41s** s8 is still
fully painted and is **not** fading out. A chapter that faded to black on its last
frame would put a black flash inside the assembled cut.

### 4. Both constraint asserts execute — proven by making them fail

"Wired" is not the same as "runs", and this run's whole theme is checks reporting
green over the thing they exist to catch. So I planted `$1,500,000 $2,500 a month`
into `#s8-kick`, re-ran the gate, and got:

```
Runtime
  ✗ page_error: RATE ASSERT FAILED — s8 renders $1,500,000 with no #s8-rate
    carrying a rate · s8 renders the derived income $2,500 a month with neither
    a rate nor an ILLUSTRATIVE marker in frame
  1 error(s)
```

**Both** branches fired — `withdrawal_rate_on_screen` and the extended
`derived_income_carries_assumption` — and `hyperframes check` turns the throw into
a hard error rather than swallowing it. Restored with `node build.mjs`, md5 back to
`01153f33…`. Chapter 1 renders no figure, so the asserts are vacuously true here;
they are now demonstrably armed for chapters 2–6.

### 5. No rail

Every occurrence of "chapter" / "rail" / "slide" in `index.html` is inside an HTML
comment, the `<title>`, or a stylesheet filename. Nothing renders, and no frame in
any of the 33 shows a title, a counter or a slide number. The `cut-en` watermark
rides `#root::after` and is present bottom-right in all 33.

## Gate results

**`npm run check` → PASS.**

```
Lint      0 error(s), 3 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 9 info(s)
Motion    0 errors, 0 warnings
Contrast  10/10 text checks pass WCAG AA
```

The three warnings are `composition_file_too_large` (310 lines) and
`timeline_track_too_dense` ×2 (4 timed elements per track) — both are the shape
this pipeline's one-file-per-chapter build always has. The eleven infos are nine
`container_overflow` on `#sN-bg` (that IS the ken push scaling the bg past the
section that clips it) and two `pointer_events_none` on system CSS.

Per the `known_benign` note I checked **what the findings suppress**, not just
whether they look harmless: nothing was suppressed. There are 0 lint *errors*, so
Layout and Contrast both genuinely ran — the exact trap that let four earlier cuts
ship with WCAG never executed. `known_benign` is `[]` and I added nothing to it. No
design token was touched.

**`pipeline_check check build --chapter 1` → refused by the tool, by design:**

```
error: --chapter is only implemented for 'assets'; the other chapter artifacts
are verified by `hyperframes check` and the draft render
```

`check_build` calls `studio_dir()` directly rather than `project_dir()`, so it is
not chapter-aware; run without `--chapter` it would look at
`studio/videos/passive-income-number-en/`, which has no `index.html`, and report a
missing file that says nothing about the chapter. Rather than skip its assertions,
I ran **the real `check_build` function** against the chapter project (module
imported, `studio_dir` pointed at a scratch mirror holding this `index.html` and a
chapter-1 slice of `timing.json` — 8 lines, total 46.42). Everything it asserts
passes: root duration vs last scene end, scene count vs line count, root vs
timing total, `cut-en` watermark, no network fetch, the 0.45s overlap on all seven
joints, 1/2 track alternation, `data-framings` partitioning each scene,
`max_scene_seconds`, no `__hfLottie`, no `path:` load, 1 Lottie against a cap of 4.

**One finding, and it is a false positive in the checker:**

```
x calls lottie.loadAnimation() directly — use loadLottie() from motion.js
```

The composition calls `loadLottie` / `playLottie` and nothing else. The only
`loadAnimation` in the file is at **line 53, inside the CSS comment** that explains
*why* `.v-lstage` is sized in pixels ("lottie-web sizes its `<svg>` from the
container's box at `loadAnimation()` time"). `check_build`'s
`re.search(r"loadAnimation\s*\(", html)` scans raw HTML with no comment stripping.

## System gaps found (reported, not improvised)

1. **`check_build`'s three Lottie regexes match inside comments.** Above. It will
   fire on every future chapter whose build documents the pixel-stage trap — i.e.
   it punishes the comment that prevents the bug. The home for the fix is stripping
   `<!-- … -->` and `/* … */` before those three `re.search` calls in
   `tools/pipeline_check.py`. **I did not edit `tools/` — outside this stage.** I
   also deliberately did **not** reword the comment to dodge it: silencing the
   match would hide the defect from the next agent, who would then not report it
   either.
2. **`check_build` is not chapter-aware** while the run is chapter-first. Its
   assertions are the ones most worth having per chapter (overlap, track
   alternation, framings, Lottie traps) and today they only run if an agent
   reconstructs them by hand, as I did. `project_dir()` already exists; `check_build`
   just needs to use it, with the timing comparison against the chapter's slice.

Nothing was missing from the motion vocabulary: `sceneTransitions`, `ken`,
`plateKen`, `rise`, `pop`, `popEach`, `fill`, `loadLottie`, `playLottie`,
`register` covered this chapter with no helper redefined inline. Two one-off
components are declared `.v-lstage` and `.v-chiprow` in the composition's own
`<style>`, after the system links, exactly as the one-off rule requires.

## Deviations and observations for fin-editor

1. **Lottie cue at +1.13, not the storyboard §8's +1.85.** `audio.json` keeps the
   `buzz` SFX at +1.85 (16.449s absolute) and records the reason: with a +1.13
   start the banner's jitter beat lands on +1.85, so the sound and the picture
   coincide. The frames are consistent with that. Flagging it because the
   storyboard says +1.85 for both; the editor should rule.
2. **s6's photograph** — the paper grocery bag reads as a large flat pale
   rectangle filling the right half, and the left half falls to near-black under
   the locked grade. Legible, but the same high-key-subject-under-a-locked-grade
   shape that produced three hi ch1 blockers.
3. **s8's photograph** — the ladder is only legible in the left third; the right
   two-thirds is near-black shadow. Weakest frame of the chapter.
4. **s3/s4** — the crop is real and the hold works, but the **mug** is the
   dominant object in both, not the phone, even though `.src` describes a
   "smartphone face down next to a coffee mug". The Lottie carries the "money
   arrived" beat; the photograph does not contradict it, but it does not help.

2–4 are `fin-assets` territory (marked done) and not fixable inside a build — no
per-scene brightness override is permitted and the grade is locked. Recorded so
the editor is not the first to notice.

## Result

**8 scenes · s1–s8 · 46.420s** — chapter 1 of six, chapter offset 0.000s, so it
concatenates frame-exact as-is. `hyperframes check` passes.
