---
summary: fin-build chapter 1 (s1–s11, VO 1.1–1.11) of financial-freedom-after-50 -en. Chapter project scaffolded from tools/scaffold with the system LINKED (never copied), index.html generated from timing.json by a local build.mjs, `npm run check` PASS (0 errors, 0 warnings after one fix, contrast 12/12 AA), 12 max-density frames eyeballed across 2 snapshot batches. Chapter duration 68.672 s.
updated: 2026-08-15
source: studio/videos/financial-freedom-after-50-en-ch1/ · storyboard-en.md §2/§4/§5/§6/§7/§8/§10 · script-en.md ch1 [img:] cues · assets/voice/timing.json · tools/format/fin-build.json · tools/packs/fin-build.md
stage: fin-build, cut en, chapter 1, attempt 1
---

# fin-build — en, chapter 1, attempt 1

## Ran

- Read `vault/CLAUDE.md`, `tools/packs/fin-build.md` (BOXes + the two body sections that are
  mine), `tools/format/fin-build.json`, `run.json`, `storyboard-en.md` §1–§12, `script-en.md`
  chapter 1, `logs/fin-assets-en-1.md`.
- Read the code homes (they win over prose): `tools/scaffold/assets/blockframe.css`,
  `chapter-design.css`, `js/motion.js`; `tools/pipeline_check.py` `check_build` / `chapter_timing`
  / `offcanvas_art` / `uncovered_glyphs`; `tools/chapter_project.py`; `tools/audio/kit.json` +
  `mix.py`. Reference implementation: `vault/videos/japanese-money-methods/src/en-ch1/index.html`
  (the note names `hi-ch1/index-claudedesign.html`; that path does not exist — the archive holds
  `src/en-ch1/index.html`, one root html per chapter, exactly as `chapter_design.one_root_html`
  says it must).
- Scaffolded `studio/videos/financial-freedom-after-50-en-ch1/` — symlinks to
  `tools/scaffold/assets/{blockframe.css,chapter-design.css,js/motion.js,js/gsap.min.js,fonts,img}`
  and to the cut's `assets/voice`; `package.json` + `package-lock.json` copied from the scaffold;
  `npm install` (178 packages, hyperframes 0.7.66 from the lockfile — no bare `npx --yes`).
- Wrote `build.mjs` and ran it; wrote `assets/audio.json`; ran `npm run check` twice; ran
  `npx hyperframes snapshot` in two batches with two separate `-o` directories.
- No `.env` read. No `.claude/` or `tools/` write. No git. No render.

## Failed

Two things failed and both are fixed; one third-party defect is reported, not fixed.

1. **`hyperframes check` lint ERROR `missing_timeline_registry`** on the first run. `register()`
   lives in `motion.js`, and the rule is a TEXT scan of `index.html`, so linking the system
   (which is the standing instruction) trips it. This is not cosmetic: **a lint error makes
   `hyperframes check` SKIP the layout and contrast passes entirely** — the first run reported
   `Layout 0 issues across 0 sample(s)` and `Contrast 0/0 text checks`, i.e. two whole gates
   silently not run. Fixed the way every creator-approved chapter fixes it (verified in
   `japanese-money-methods/src/en-ch1/index.html:505`): one restated
   `window.__timelines = window.__timelines || {};` immediately before `register()`. Runtime
   no-op — `motion.js` already ran the identical line. After the fix: Layout ran 21 samples and
   Contrast ran 12/12.
2. **`build.mjs`'s own overlap assert fired on 1.4 → 1.5** (`overlaps the next by 0.449`).
   Not a drift: `timing.json` rounds `scene_duration` to 3 dp, so `scene_start + scene_duration`
   misses the next `scene_start` by 1 ms on that line. Loosened the assert to `check_build`'s own
   0.05 tolerance rather than "fixing" a measured number.
3. **`tools/scaffold/assets/blockframe.css` has a broken comment that kills `.stamp.warn`.**
   The comment at line 184 closes at `known_benign. */` and the paragraph that follows
   (`The role modifier must RE-STATE the dark ink: …  so they win. */`) is therefore LIVE CSS.
   It runs on as a selector prelude until the next `{`, which is `.stamp.warn`'s — so that one
   rule is dropped and `class="stamp warn"` renders **red text on transparent**, which is exactly
   the bug the paragraph was written to record as fixed (passive-income-number hi ch5,
   2026-08-12). Measured in headless Chrome against the real file:
   `.stamp.warn → color rgb(239,68,68), background rgba(0,0,0,0)` vs
   `.stamp.fund → color rgb(13,16,23), background rgb(34,197,94)`; `font-size 44px` on both, so
   `.stamp` itself is intact and the damage is exactly that one rule.
   **No effect on this chapter or this cut** — storyboard §2 renders every "stamp" cue as a
   verdict `pop` on the focal and writes no `.stamp` markup anywhere in the 123 scenes. It will
   bite the next cut that uses a red verdict stamp. I cannot write `tools/`; owed below.

## Evidence

**Project:** `studio/videos/financial-freedom-after-50-en-ch1/`
**Artifacts:** `index.html` (generated), `build.mjs` (the generator), `assets/audio.json`,
`snapshots/qa/b1/` + `snapshots/qa/b2/`.

### `npm run check` — PASS

```
Lint      0 error(s), 2 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 21 info(s)   (21 samples)
Motion    0 errors, 0 warnings
Contrast  12/12 text checks pass WCAG AA
Check passed
```

- The 2 warnings are both `timeline_track_too_dense` (track 1 = 6 timed elements, track 2 = 5).
  That is the archetype layer's own structure — 11 scenes alternating tracks 1/2 is *required*
  by `check_build` and by `overlapping_clips_same_track`. Its suggested fix (split into
  `data-composition-src` sub-compositions) would break `one_root_html`. Not actioned, no token
  touched.
- The 4 lint/layout info classes are all system geometry, not defects: `pointer_events_none` on
  `.grain` / `#root::after`; `container_overflow` on every `#sN-bg` (`.bg { inset: -8% }` is the
  ken headroom, by design); `text_occluded … inside div.scrim` (the scrim is four translucent
  gradients at z 1, the stack is z 2); `content_overlap #s7-head inside #s8-head` at t=41.97,
  which IS the 0.45 s cross-dissolve — its presence is evidence the overlap is real.
- `known_benign` in `tools/format/fin-build.json` is still `[]` and stays that way: nothing was
  silenced, and **no design token (colour, size, weight) was edited to satisfy any checker.**

### Timing — four homes, one source, asserted in the generator

`assets/voice/timing.json` lines `1.1`–`1.11` are the only home. `build.mjs` derives the
`<section>` attributes, the JS `S` map, the `<audio>` rows and the root duration from them, then
**re-reads its own output** and asserts, per scene: `data-start` exact, `data-duration` =
`scene_duration + 0.45` (last scene bare), `data-framings` sum = `scene_duration`, no framing
> 9.0 s, adjacent tracks differ, and the successor overlap = 0.45 ± 0.05. Nothing is hand-typed.

| scene | line | data-start | data-duration | framings | own hold | track | arch | ground | art | ctr |
|---|---|---|---|---|---|---|---|---|---|---|
| s1 | 1.1 | 0 | 5.377 | 4.927 | 4.927 | 1 | A | `#131a24` | off | Y |
| s2 | 1.2 | 4.927 | 6.579 | 6.129 | 6.129 | 2 | A | `#101720` | off | Y |
| s3 | 1.3 | 11.056 | 6.396 | 5.946 | 5.946 | 1 | D | `#241d15` | off | Y |
| s4 | 1.4 | 17.002 | 6.631 | 6.181 | 6.181 | 2 | A | `#1c2027` | off | Y |
| s5 | 1.5 | 23.184 | 8.721 | 8.271 | 8.271 | 1 | D | `#241d15` | off | Y |
| s6 | 1.6 | 31.455 | 5.926 | 5.476 | 5.476 | 2 | C | `#1f1e1c` | off | Y |
| s7 | 1.7 | 36.931 | 5.038 | 4.588 | 4.588 | 1 | C | `#0f2a1a` | off | Y |
| s8 | 1.8 | 41.518 | 9.923 | 4.6,4.873 | 9.473 | 2 | A | `#291f13` | off | Y |
| s9 | 1.9 | 50.991 | 6.344 | 5.894 | 5.894 | 1 | D | `#0f2a1a` | off | **N** |
| s10 | 1.10 | 56.885 | 8.617 | 8.167 | 8.167 | 2 | D | `#12351f` | off | **N** |
| s11 | 1.11 | 65.051 | **3.621** | 3.621 | 3.621 | 1 | D | `#12351f` | off | Y |

- **Root `data-duration` = 68.672** = last scene end = `chapter_timing()`'s recomputed total for
  chapter 1 (65.051 + 3.621). `check_build`'s three timing equalities all hold.
- **s11 carries a BARE duration** (no +0.45) — no successor inside this project to dissolve into;
  `cut_assemble.py` adds it back at concat.
- **s8 is the chapter's only `max_scene_seconds` breach** (9.473 > 9.0) and is the one scene the
  storyboard §5 gave two framings. Longest framing 4.873 s, sum 9.473 = the measured
  `scene_duration`, so it partitions the scene rather than ducking the guard.
- Tracks: `1 2 1 2 1 2 1 2 1 2 1` — no two adjacent scenes share a lane.
- `sceneTransitions(IDS, S)` is wired once, before the per-scene cues. **No `acts`** — storyboard
  §5 puts both shoves at s28→s29 and s72→s73, neither of which is in this chapter.

### What the chapter is made of

- **`.has-photo` on all 11 scenes**, each with a real full-bleed `.bg` from
  `assets-ch1/final/sN.jpg`. `photo_free_scene_ratio` 0 honoured. No per-scene `filter:` override
  anywhere — the grade stays `grayscale(.32) brightness(.62) contrast(1.05)`.
- **`art-off` on 11 of 11, so no scene emits a plate.** Storyboard §8 declares ch1 at 0 drawn
  layers / 0 icons / 0 Lotties, and rule 8 agrees: every beat here is an object a photograph
  states better (cards, a newspaper, a notebook, stairs, a door). An empty plate would be an
  aperture onto nothing, so none is written; `offcanvas_art` has nothing to find and
  `lottie.min.js` is not loaded at all.
- **`.centred` on 9 of 11.** s9 and s10 are the exceptions — their declared chip row occupies D's
  other side, so the split is a layout and they keep their `.brule` at `top:424px`. Every centred
  scene drops plate/crule/vrule/brule.
- **`--tint` is unset on all 11** (§1) — `--f1` carries the temperature under
  `.has-photo .field` at 38%, and the four fund scenes (s7, s9, s10, s11) set
  `--gl:rgba(34,197,94,.16)` on `.glow` instead. One role colour per scene; 7 of 11 carry none.
- **The silent-white trap avoided:** role text uses `.fundc` (the colour class), chips use
  `.chip fund` (the component modifier). Confirmed green on the frames, not white.
- **Type ladder:** `.kicker` 30 (system) and focal `.huge` at **76 px** on the 8 stmt scenes,
  `.chip` 32 on the two chip scenes. Every value is on `layout.type_ladder_px`; nothing
  interpolated, nothing shrunk below 76. Two content elements per scene (kicker + focal) against
  a ceiling of 6; no `foot` in this chapter because no ch1 line carries a `src:`.
- **Chips:** 2 and 3 per row (≤3), longest `5 Transition` = 12 chars (≤22). No wrap risk.
- **Cue ladder (§4), fixed offsets, no literal times** — every call hangs off `S.sN`:
  `head +0.30` (rise y24 0.50) · `stmt +1.10` (rise y40 0.70) · chips `popEach +1.10` at 0.65
  stagger · s11 `pop +1.10` (0.60, `back.out(1.7)`) as the declared verdict entry. First cue at
  +0.30 ≤ `first_cue_by_seconds` 0.5 on all 11; +0.30→+1.10 = 0.80 = `cue_min_gap_seconds`; the
  0.65 chip gap is the declared cascade exemption.
- **Ken alternates on every boundary**, and the direction is pinned by s8: out · in · out · in ·
  out · in · out · **in (s8)** · out · in · out. No two pushes in a row. `ken` runs the scene's
  full on-screen length (its `data-duration`, dissolve tail included), so no scene holds a static
  frame.
- **s8's two framings are ONE continuous push, not a self-dissolve** (firaun rule): the same
  `#s8-bg` gets `plateKen(1.00→1.06)` over framing A and `plateKen(1.06→1.26)` over framing B —
  pure scale, exact hand-off, second half faster. Verified on frames: 43.618 s is a wide two-shot
  on the trail, 49.500 s is a visibly tighter crop of the same file. No second image slot spent.
- **Watermark:** `<div id="root" class="cut-en" …>`; the avatar is present bottom-right in all 12
  QA frames, i.e. it rides above every scene and every dissolve. Nothing was placed inside a
  `.scene`.
- **Determinism:** no `https?://` anywhere in `index.html`, no `Date.now`, no `Math.random`, no
  render-time fetch. GSAP, the font, grain and the watermark are all local (symlinked to the
  git-tracked scaffold, so the system is linked and never copied).
- **Glyphs:** on-screen text is ASCII plus one em dash (s4 "Common — and still a myth."). U+2014
  is carried by FinanceSans — verified by precedent (`japanese-money-methods/src/en-ch2`
  `#s21-stmt` ships one) and by eye on frame 03, which renders a real dash, not tofu. No forbidden
  literal (`→ ▶ > ~ × ≈ ¢`) anywhere.

### `assets/audio.json` — chapter 1's four cues

```json
{ "music": "bed-resolve",
  "sfx": [ {"at": 1.1, "name": "reveal"}, {"at": 12.156, "name": "reveal"},
           {"at": 57.985, "name": "chip"}, {"at": 66.151, "name": "stamp"} ] }
```

Every time is derived (`S.sN + 1.10`) and every one matches storyboard §2's own absolute figure
to the millisecond (1.100 / 12.156 / 57.985 / 66.151). Names are `kit.json` entries and each
lands on the helper the kit binds it to (`reveal`→`rise`, `chip`→`pop` on the row's first chip,
`stamp`→the verdict `pop`). Closest pair is 11.06 s apart, far past the 0.8 s floor. **No music
or SFX `<audio>` rows in `index.html`** — the composition is voice-only, 11 rows, one per VO line;
`mix.py` owns the bed and the hits.

### Max-density snapshot pass — 12 frames, 2 batches, 2 separate `-o` directories

Sampled at each scene's LAST cue completion (+2.10 s on stmt scenes, +2.90 s on the two chip
scenes, +2.00 s on the verdict scene), plus one extra inside s8's second framing.

| batch | dir | `--at` | frames | looked at |
|---|---|---|---|---|
| b1 | `snapshots/qa/b1` | 2.1, 7.027, 13.156, 19.102, 25.284, 33.555 | 6 | **6 of 6** |
| b2 | `snapshots/qa/b2` | 39.031, 43.618, 49.5, 53.891, 59.785, 67.051 | 6 | **6 of 6** |

**12 of 12 frames opened and read individually** (not judged off a contact sheet), covering
11 of 11 scenes. Both invocations succeeded first try — the `Navigation timeout of 10000 ms`
flake did not appear; no batch was written into a directory another batch would later wipe.

Findings from the frames:

- Every `.stack` sits inside the safe area; nothing overflows or clips. Longest line (s2, 48
  chars at 76 px) wraps to two centred lines and clears both the kicker and the frame edge.
- s7 and s11 focals render **green** (`--fund`), s9/s10 chips render green-bordered on
  `--panel` — the `.fundc` / `.chip.fund` split is correct on screen, nothing painted white.
- s4's em dash draws correctly.
- s8's A and B framings are visibly different crops of one continuous push (above).
- The watermark is present and unclipped in all 12.
- **One thing a reviewer may want to look at, and it is not a build defect:** s10's stone
  stairway is the darkest frame in the chapter — it is the chapter's only monochrome original
  (fin-assets Owed #3, YHIGH 203) and it sits under the deepest green ground in ch1 (`#12351f`),
  which reads slightly teal. The chips are fully legible over it (contrast passed 12/12) and I
  did not touch the grade or the ground, because both are locked and the fix, if one is wanted,
  is the declared re-pick `s10=4` from `_cand/s10.json`.

## Changed

- **New:** `studio/videos/financial-freedom-after-50-en-ch1/` gains `index.html`, `build.mjs`,
  `package.json`, `package-lock.json`, `node_modules/`, `renders/`, `assets/audio.json`,
  `assets/{blockframe.css,chapter-design.css,fonts,img,voice}` + `assets/js/{motion.js,gsap.min.js}`
  (all symlinks), `snapshots/qa/{b1,b2}/`. `assets-ch1/final/` (fin-assets') untouched.
- **`build.mjs` is the only hand-authored logic** and it owns no timing: an 11-row SPEC table of
  archetype / ground / role / centred / strings, lifted from storyboard §6–§8 and the script's
  `[img:]` cues, plus the cue-ladder emitter. Chapters 2–7 can reuse it by swapping `CH` and the
  table, which is why it exists as a file rather than as a one-liner.
- **No new component and no inline `.v-*` one-off was needed** — every element in this chapter is
  system (`.stack .kicker .huge .row .chip .field .rules .glow .scrim .grain .brule`). The
  composition's inline `<style>` carries only `#root`'s box and the four `.p-*` plate rects
  (inert here; ch1 emits no plate).
- **Nothing added to `assets/icons/`** — the chapter draws nothing.
- Nothing in `tools/`, `.claude/`, or the vault outside this log.

## Owed

1. **`tools/scaffold/assets/blockframe.css` line ~184–192: close the comment.** The stray
   paragraph after `known_benign. */` is live CSS and eats the `.stamp.warn` rule (measured
   above). One `/*` restores it. Every cut that ships a red verdict stamp inherits red-on-red
   until then, and `hyperframes check` cannot see it — the element is a `<span>` with a
   transparent background, so contrast is computed against whatever is behind it.
2. **`missing_timeline_registry` is a standing tax on linking the system.** Every chapter project
   must restate `window.__timelines = window.__timelines || {};` in its own script or lose the
   layout and contrast passes to a lint error. Worth one line in `motion.js`'s header comment (or
   an emitted line in `chapter_project.py`) so the next build does not rediscover it by failing.
3. **MISSING-CONSTANT: `architectures["per-line-chapters"].body_class`.** `run.json.architecture`
   is `per-line-chapters`, and `tools/format/fin-build.json architectures` carries only the three
   `short`-tier entries — so the slice cannot answer what class `#root` takes at LONG. I applied
   the empty/default (`class="cut-en"`, no `swiss-band`, no `rail`), which is what storyboard §
   header states in prose ("no centred nine-segment stack and no `.rail`; the archetype layer owns
   the layout"). Add the entry, or say in the slice that MEDIUM/LONG take no body class.
4. **Reference path in `tools/packs/fin-build.md` is wrong.** It names
   `vault/videos/japanese-money-methods/src/hi-ch1/index-claudedesign.html` +`-ch2`; the archive
   has no `hi-*` chapter and no `index-claudedesign.html` (both correctly forbidden by
   `chapter_design.one_root_html`). The live reference is `src/en-ch1/index.html` … `en-ch8/`.
5. **`storyboard-en.md` §3's DOM example writes `data-framings="4.500 4.502"` space-separated.**
   `check_build` splits that attribute on `,` only, so a space-separated pair would be parsed as
   one token and crash `float()`. Emitted comma-separated (`4.6,4.873`), as the shipped chapters
   do. Worth correcting in the storyboard before chapters 3/5/6 build the other ten.
6. **Chapters 2–7 are not built.** ch2 needs its images (fin-assets), and it carries the first
   `shove` (s28→s29), the first `icon` (s18, a `warnc` step arrow — check `assets/icons/` first
   and write any new one back), and the cut's first `num` scenes.
7. **Not this stage:** the render, `mix.py`, `loudnorm.py`, the nine source screenshots, and
   `hook_gate_en` measured on the encode (the model says 11.306 s, inside 15).
