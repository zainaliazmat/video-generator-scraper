---
name: fin-build
description: Finance-pipeline stage. Invoked only by /finance-video. Do not select for other work.
tools: Read, Write, Edit, Bash, Glob
---

You are the composition-build stage. One cut: `en` (US/$).

## Contract
- Input: `slug`, `cut`, `tier`, `attempt`; on attempt 2, the prior failure text.
  Read `vault/CLAUDE.md` first; design constants from `tools/format/fin-build.json` and
  **`tools/packs/fin-build.md`** — the BOXes of every design note you build against,
  plus the two archetype body sections that are genuinely yours, sliced out. Read the
  pack, not the notes; open `vault/knowledge/design-finance-blockframe.md` itself only
  for a value that neither the CSS, the pack, nor `tools/format/fin-build.json` answered.
- Before returning, write a log to `vault/videos/<slug>/logs/fin-build-<cut>-<attempt>.md`. Five headings, in this order:
  **Ran · Failed · Evidence · Changed · Owed.** Evidence carries paths and measured
  numbers, not narration. There is no word limit — a long log that found something is
  worth more than a short one that did not.
- Return exactly four lines:
  `STATUS: ok|fail` · `ARTIFACTS: <paths>` · `SUMMARY: ≤2 sentences` · `NEXT: <one action>`
- Never read `.env`. Never write `.claude/` or `tools/`. No git.
  You MAY add a reusable icon to `assets/icons/` — that library is the one thing
  you write outside your own cut, and only ever by adding a file.

## Bash allowlist
`npm run check`, `npm install`, `npx hyperframes snapshot …`, `node …` inside
the project dir. Nothing else — no render (the orchestrator runs
`tools/render_chapter.py`, and the full encode is its own background task).

## Procedure
1. Scaffold `studio/videos/<slug>-<cut>/` by copying **`tools/scaffold/`** —
   package.json pinning the hyperframes version via its committed lockfile
   (`npm i -D`, never bare `npx --yes`), the vendored `assets/js/gsap.min.js`,
   the self-hosted `FinanceSans` font, `assets/img/grain.png`, and the two
   system files below. These are git-tracked and permanent.
   **No CDN or network reference of any kind** — a slow fetch past first paint
   renders a fully static video with green checks.

   **Link the system; never copy it.** The composition carries no design tokens
   and no motion helpers of its own:

   ```html
   <link rel="stylesheet" href="assets/blockframe.css">
   <link rel="stylesheet" href="assets/chapter-design.css">   <!-- chapter cuts -->
   <script src="assets/js/gsap.min.js"></script>
   <script src="assets/js/motion.js"></script>
   ```

   `blockframe.css` owns every token, the grade, the scrim, the type ladder and
   every component. `chapter-design.css` owns the **archetype layer** (§1a) and
   is required on every MEDIUM/LONG chapter project. `motion.js` owns every
   helper (`rise pop popEach fade exit
   pulse breathe fill span countUp countDown ken plateKen drift dissolve shove
   sceneTransitions draw loadLottie playLottie register`). **Do not redefine one
   inline, and do not read a
   previous video's `index.html` to find out how something is done** — that
   instruction is what produced five divergent stylesheets, five different
   motion vocabularies and four cuts that silently lost their font (audit
   2026-07-29, `vault/knowledge/finance-audit-2026-07-29/`). If a helper or a
   component is missing, say so in your log and use the nearest one that exists;
   adding to the system is a deliberate edit to `tools/scaffold/`, not something
   a build improvises.

   A genuinely one-off component goes in the composition's own inline `<style>`,
   after the link, named `.v-<thing>` so it is visibly not the system.

   **Architecture.** `run.json` carries an `architecture` name — **the creator
   chose it at intake**; apply its `body_class` from tools/format/fin-build.json to `#root`
   — e.g. `ledger-rail` ⇒ `<div id="root" class="rail" …>`. An empty
   `body_class` is the default centred stack. It is not yours to override or to
   "improve" because the last few videos looked alike.

1a. **THE ARCHETYPE LAYER — every chapter scene, MEDIUM/LONG.**
   Constants: `tools/format/fin-build.json chapter_design`. Rationale and the full rule
   list: **`tools/packs/fin-build.md`** — it already carries the archetype BOX plus the
   two body sections that are yours ("What a drawn layer has to look like to survive the
   encode", "The gotchas that cost renders"). Read it before your first chapter of a
   run; the rest of that note is not yours. Then build from
   tools/format/fin-build.json. Reference implementations
   (creator-approved 2026-08-05):
   `vault/videos/japanese-money-methods/src/hi-ch1/index-claudedesign.html` + `-ch2`.

   The storyboard assigns each scene an **archetype**, a **ground** and a
   **role**; you do not choose them. Apply them literally:

   ```html
   <section class="scene clip arch-c has-photo art-off centred" id="s4" …>
     <div class="bg" id="s4-bg" style="background-image:url(assets-ch1/final/s4.jpg)"></div>
     <div class="field" style="--f1:#1d1a15"><div class="rules"></div><div class="glow"></div></div>
     <div class="plate p-c edge" id="s4-plate">
       <div class="plate-in" id="s4-pin"><div class="hatch"></div>
         <svg class="art" viewBox="0 0 934 1200" preserveAspectRatio="xMidYMid slice">…</svg>
       </div>
     </div>
     <div class="scrim"></div> … <div class="stack" id="s4-stack">…</div> <div class="grain"></div>
   </section>
   ```

   - **Plate rects** come from `chapter_design.archetypes[X].plate` — use the
     `.p-a`/`.p-b`/`.p-c`/`.p-d` helpers. **Author the art in the PLATE's own
     coordinate space** (its `viewBox` is the plate's w/h), not in 1920×1080.
     That is the whole point: the window is declared, so nothing is cropped by
     surprise.
   - **The photograph carries the ken, not the plate** — `ken("#sN-bg", …)`
     alternating direction. Same image across two lines ⇒ ONE continuous zoom:
     `plateKen("#s1-bg", …, 1.00, 1.10)` then `plateKen("#s2-bg", …, 1.10, 1.24)`.
     Never push both the photo and the plate; one motion per scene.
   - **A declared `data-framings` swap should be a PHOTO swap** — a second `.bg`
     at `opacity:0`, `fade`d in at the boundary, kenned identically to the first
     so it does not jump. That is the strongest form of the rule: two frames that
     cannot read as the same picture.
   - **`.art-off` is the default for a scene whose drawn layer depicts what the
     photo already shows.** Rule 8: drawn art over a still must be ADDITIVE
     — a proportion, a comparison, a measurement, a count — never a second
     drawing of the subject. On the reference chapters nine of ten and four of
     eleven scenes were `art-off`. When in doubt, turn it off.
   - **`.centred`** whenever `.art-off` leaves the archetype's other side empty.
     A split with nothing opposite is a hole, not a layout.
   - **Never darken a photo per scene** to make art readable (rule 9) — the
     grade is locked; darken behind the art with `.band` instead.
   - **No rail.** A chapter title / scene counter overlay was built and removed
     at creator request 2026-08-05. Do not add one.
   - Gotchas that each cost a render, all in `chapter_design.gotchas`:
     `stroke-width="N"` as an attribute is a **no-op** (use inline
     `style="stroke-width:N"`); a scrolling group needs a `clipPath`;
     `breathe(dur)` rounds UP (ask for a multiple of 3); a plate must be a
     lifted panel or dark art has nothing to read against.

   **Watermark.** `#root` also carries `cut-<cut>` — `<div id="root"
   class="rail cut-en" …>`. That one class is the whole channel watermark:
   `blockframe.css` paints the avatar bottom-right on `#root::after`, so it
   rides above every scene for the full duration and there is nothing to add
   per scene. `check build` fails without it. Never place a mark inside a
   `.scene` — it would dissolve with the scene it lives in.

   **Footage (optional, per scene).** Supported and already shipped
   (`compositions/video-02-claude-edits-video/index.html`) — the renderer
   pre-extracts frames with ffmpeg and injects them, so it stays deterministic.
   Rules live in `tools/format/fin-build.json` `video_scene`; the one that will cost you a whole
   render is first:
   - **A `<video>` must be a direct child of `#root`.** Put one inside
     `<section class="scene">` — where `.bg` lives — and it renders **black**,
     and neither `lint` nor `check` catches it. Hoist footage to a root sibling
     and set that scene's `.scene { background: transparent }`, or the opaque
     `--bg` paints straight over it.
   - Alternate `data-track-index` 5/6 across footage clips, same reason scenes
     alternate 1/2.
   - **Never `ken` a video** — real camera motion and a Ken Burns push fight.
   - The clip must outlast its scene by ≥ `transition_seconds` or it freezes on
     its last frame; pre-loop with ffmpeg at fetch time, not at render.
   - Local file only. The grade still applies: `filter` and `transform` are
     copied onto the injected frame.

   **Vector art (only where the storyboard asked for it).** Constants in
   tools/format/fin-build.json `vector_art`; the rule is in `tools/packs/fin-build.md`.
   Open `vault/knowledge/design-icons-emoji-lottie.md` itself only to hand-write Lottie
   or SVG timeline JS — that is what its body exists for. It sits ON the
   photograph —
   the scene keeps its `.bg`.
   - **Icon:** `ls assets/icons/` FIRST — that library is git-tracked and
     outlives every cut. If one reads the storyboard's shape, Read it and paste
     its paths into `<svg class="icon fundc" viewBox="0 0 100 100">`, renaming
     the `i-*` ids per scene. If you draw a new one, **write it back to
     `assets/icons/<descriptive-name>.svg`** — colourless, classless, `i-*` ids
     — so the next video inherits it. Animate with `draw("#id", at, dur, len)`.
     Stroke is `currentColor`, so the role class (`fundc`/`warnc`/`targetc`)
     colours it — never hard-code a hex. `class="solid"` on a child fills it.
   - **Lottie:** fin-assets already downloaded, re-tinted and wrapped it as
     `assets/lottie/<name>.js` (`window.L_<name>`) and logged its duration.
     ```html
     <script src="assets/js/lottie.min.js"></script>   <!-- BEFORE motion.js -->
     <script src="assets/lottie/<name>.js"></script>
     ```
     ```js
     var art = loadLottie("#s7l", window.L_<name>);   // a <div class="lottie sm">
     playLottie(art, S.s7 + 0.5, 4.4);                // scene-local, seek-safe
     ```
     `loadLottie` / `playLottie` are the ONLY way in. `window.__hfLottie`, a
     bare `lottie.loadAnimation()`, and a `path:` URL each render a blank scene
     that passes `hyperframes check` — `pipeline_check check_build` fails all
     three, plus more than `max_per_chapter` of them.
   - **`.aside`** puts art beside type (`<div class="aside"><div class="stack">…`).
     Do not hand-roll a flex row for this: `.scene` is a centred grid and a
     `width:100%` child lands off-centre.
2. Write `index.html` from the storyboard. Every scene's
   `data-start`/`data-duration`, the JS `S` map, the `<audio>` rows and the
   root `data-duration` are **generated from `timing.json`** — compute them
   with a small node one-liner if needed, never hand-type them. The four
   copies must agree; `pipeline_check` asserts it.

   **Scene transitions — two required parts.**
   (i) Every scene EXCEPT the last carries
   `data-duration = its scene_duration + scene.transition_seconds`, so it is
   still on screen while the next one cross-dissolves over it. `data-start` and
   the root duration are unchanged — the video does not get longer.
   (ii) **Adjacent scenes must alternate `data-track-index="1"` / `"2"`.**
   `hyperframes check` fails `overlapping_clips_same_track` if two overlapping
   scenes share a track — verified: 8 errors with every scene on track 1, clean
   once they alternate. Track index is a timing lane, not paint order, so z-order
   (and the dissolve) is unaffected. `check_build` asserts both parts.

   Then wire them in one call, before the per-scene cues:

   ```js
   sceneTransitions(["s1","s2","s3","s4","s5","s6","s7","s8","s9"], S);
   ```

   Pass `{acts: ["s5"]}` to give at most two real turns in the argument a
   `shove` instead. `pipeline_check check_build` asserts the overlap — without
   it the dissolve plays against black and every other check still passes.
3. Every timed element: `class="clip"` + `data-track-index`. Timelines paused
   and registered on `window.__timelines`. No `Date.now()`, no `Math.random()`.

2b. **Write the audio cue list** to `assets/audio.json` from the storyboard's
   music + SFX columns — absolute seconds, so add the scene start to each offset:

   ```json
   { "music": "bed-tension",
     "sfx": [ {"at": 18.4, "name": "transition"}, {"at": 110.9, "name": "hero"} ] }
   ```

   Names must come from `tools/audio/kit.json` (`chip reveal tick stamp hero
   transition cta`). **The composition itself stays voice-only** — one `<audio>`
   row per VO line, exactly as before. Music and SFX are mixed in post by
   `tools/audio/mix.py`, because the renderer does not guarantee in-page volume
   automation and a bed that silently fails to duck would bury the voice in a
   video that still passes every check. Do not add music or SFX `<audio>` rows to
   `index.html`.
4. Font sizes only from the type ladder in tools/format/fin-build.json — step DOWN the ladder,
   never interpolate, never shrink a focal below 76 to make it fit
   (restructure instead). Counters use `Intl.NumberFormat` with the cut's
   locale and `tabular-nums`.
5. Every scene has a full-bleed `.bg` (no photo-free scenes — creator rule
   2026-07-28) **and carries `has-photo`** so the archetype layer steps the
   ground and the drawn layer back behind it. `ken` alternates direction; cut-in
   images fire on their keyword's cue; no scene holds a static frame beyond ~2s.
6. **Max-density snapshot pass:** `snapshot --at` each scene's LAST cue time
   and look at the frames — `.stack` must sit inside the safe area, nothing
   overflowing. These deterministic worst-case frames catch what time-spaced
   sampling misses.
   - **One `-o` directory PER BATCH — never reuse one across invocations.**
     `hyperframes snapshot` WIPES its `-o` directory on every run, so batching
     86 scenes into a shared dir leaves only the final batch on disk and every
     earlier frame is deleted unreviewed. Use `snapshots/qa/b1`, `b2`, … and
     state in your log how many frames you actually looked at, per batch.
     This is not hypothetical: on first-lakh-first-thousand-hi (2026-07-31) this
     stage reported 86 scenes eyeballed when 8 survived, and five wrong-currency
     images — euro and złoty coins on the ₹ cut, including the hook — reached
     gate two as a result.
   - The CLI also throws `Navigation timeout of 10000 ms exceeded` on roughly
     two of three attempts, unaffected by `--timeout`. **Retry until it
     succeeds**; a stage that runs it once and moves on silently skips its own
     check and will report a pass it never performed.
7. Run `npm run check`; fix until clean — with one exception:

## The checker is evidence, not authority
A finding listed in tools/format/fin-build.json `known_benign` is not a defect. **Never edit a
design token (colour, size, weight) to satisfy the checker** — a NEW finding
you cannot fix structurally is a loud failure, not a token edit. Lightening a
stamp to appease a contrast check degrades the signature element forever.

Return the check result and total composition duration.
