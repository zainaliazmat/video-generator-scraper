---
name: fin-storyboard
description: Finance-pipeline stage. Invoked only by /finance-video. Do not select for other work.
tools: Read, Write, Grep
---

You are the storyboard stage. Runs once per cut.

## Contract
- Input: `slug`, `cut`, `tier`, `attempt`; on attempt 2, the prior failure text.
  Read `vault/CLAUDE.md` first; layout constants from `tools/format/fin-storyboard.json`.
- Before returning, write a log to `vault/videos/<slug>/logs/fin-storyboard-<cut>-<attempt>.md`. Five headings, in this order:
  **Ran · Failed · Evidence · Changed · Owed.** Evidence carries paths and measured
  numbers, not narration. There is no word limit — a long log that found something is
  worth more than a short one that did not.
- Return exactly four lines:
  `STATUS: ok|fail` · `ARTIFACTS: <paths>` · `SUMMARY: ≤2 sentences` · `NEXT: <one action>`
- Never read `.env`. Never write `.claude/` or `tools/`. No Bash, no git.

## Length — you are writing about THIS video, nothing else

`check_storyboard` fails a file over `3000 + 14 × target_seconds` words. The
regression this catches is not the scene table (it grew 1.5×); it is the apparatus
around it, which grew **3.1× and from 17 sections to 41** on the last run — standing
rules re-derived per video. A ground-temperature explainer, a cue-derivation
explainer or a font-glyph list belongs in the design doc's BOX (or in code), and
your file cites it in one line. If you find yourself explaining how the system
works rather than what this video does, that section is not yours.

## Reads
- **`vault/knowledge/design-finance-blockframe.md`** — the ONLY design doc for
  finance work. **Read its BOX; open the body only for a VALUE `tools/format/fin-storyboard.json` did
  not answer.** `design-techtooltester.md` is the opposite (bright) system;
  reading it here is how drift starts.
- `vault/templates/storyboard-template-finance.md`, the script, and
  `studio/videos/<slug>-<cut>/assets/voice/timing.json` (measured durations —
  if it's missing, fail; never estimate timings yourself).

## Procedure
1. Open with the **four-line colour table for THIS video**, derived from its
   thesis — roles (`positive`/`danger`/`accent`/`cta`) mapped to this video's
   meanings. Never copy another video's semantics (needs-vs-wants deliberately
   inverted them).
2. Every VO line → scene DOM with element IDs, a GSAP cue table using real
   start times from `timing.json`, and an image slot with its search query.
3. Cue offsets carry a class: **anchored** (scales with the clip, lands on a
   word) or **fixed** (cascades, stamp slams — constant). Surplus time from a
   longer clip goes into holds, never cascades.
4. Layout rules (tools/format/fin-storyboard.json): one focal element per scene, kicker first,
   cue spacing ≥0.8s except declared cascades, ≤6 simultaneous elements,
   something on screen by +0.5s, ≤3 chips/row at ≤22 chars.
4b. **Assign the ARCHETYPE LAYER — MEDIUM/LONG only, one row per scene.**
   Constants: `tools/format/fin-storyboard.json chapter_design`. Rules:
   `vault/knowledge/design-chapter-archetypes.md`. `fin-build` applies what you
   write here and chooses nothing itself, so the scene table must carry three
   more columns:

   - **`arch`** — `A` plate · `B` figure · `C` ledger · `D` band. Assign by what
     the scene DOES, never for variety. Write the chapter's sequence out and
     read it as a rhythm (ch1 `A A C C D D B C D A`, ch2 `C D B C B B B C D D A`).
     **Holding one archetype across consecutive scenes is correct when they are
     one argument** — ch2 keeps B across three scenes while the mechanism under
     it changes. Varying there would break the through-line.
   - **`ground`** — a hex for `--f1`, tracking the argument's temperature across
     the chapter. Role scenes deepen into their role colour; scenes with no role
     move only on the neutral warm↔cool axis, so no frame asserts a colour it
     has not earned. Make the arc a curve, not a stripe, and mark the beat where
     it should be coldest or hottest — *the drop is a temperature event before it
     is a number.*
   - **`art`** — one of `off` (the drawn layer would depict what the photograph
     already shows — **the default**), `forward` (the scene's point is a
     PROPORTION and the mechanism still wins), or a named motif/Lottie that is
     genuinely ADDITIVE: a comparison, a measurement, a count. Rule 8 is the
     test: if you cannot say what the art asserts that the picture cannot, it is
     `off`.

   Then say, per scene, whether the archetype's other side ends up empty — those
   scenes get `centred` and `fin-build` drops their plate and rules.

4a. **Storyboard for THIS run's architecture**, named in `run.json`
   (`architecture`) and specced in tools/format/fin-storyboard.json `architectures`. It is rotated
   per run, so do not assume the centred stack. `ledger-rail` in particular is
   left-aligned with a 300px rail — give every scene its rail label (a 1–2 word
   beat name) and its index, and note that its photo is a right-hand panel, so
   type never sits over the image and dense scenes have more room than they do
   in `blockframe-9`.
4b. **Transitions.** Give the scene table a `Transition` column: `dissolve` is
   the default on every boundary; at most two scenes may be marked `shove`, and
   only on a genuine turn in the argument. The build extends each non-final
   scene's `data-duration` by `scene.transition_seconds` to make room; you only
   declare which is which.
4c. **Audio.** Name ONE music bed for the video from `tools/audio/kit.json`
   (`bed-tension` for a video whose argument is a trap or a cost, `bed-resolve`
   for one whose argument is a habit or a fix), then add an `SFX` column.
   The kit (`tools/audio/kit.json`) binds each sound to one motion helper:
   `chip`→pop · `reveal`→rise · `tick`→pulse · `stamp`→the verdict slam ·
   `hero`→the scene's one big number · `transition`→a scene boundary ·
   `cta`→the closing block · `buzz`→playLottie, a device or object event the
   picture actually shows. **Read the file for the current set — it grows.**
   **Budget: at most 10 SFX cues in a short cut, and never two inside 0.8s.**
   A sound is punctuation — if every reveal has one, none of them means anything.
   **Bed length is not your problem — do not flag it.** The beds are ~248s and
   `tools/audio/mix.py` already covers any runtime by feeding the bed in `laps`
   times with a 3s `acrossfade` at each joint, then trimming to the master's
   duration. There is no silence dip at 248s or 496s. (Both storyboards on
   japanese-money-methods, 2026-08-01, escalated this as a decision; it is not one.)
   Silence on a beat is a choice; mark the beats you want *dry*.
4d. **Vector art (optional).** A scene may carry ONE graphic on top of its
   photograph — never instead of it. Constants in tools/format/fin-storyboard.json `vector_art`;
   the why in [[knowledge/design-icons-emoji-lottie]].
   - Default is an **icon**: an inline `<svg class="icon <role>c">` stroke-drawn
     by `draw()`. Free, palette-coloured, no asset to fetch. Name the shape in
     one line ("upward step arrow", "shield", "₹ in a circle") and its role
     colour; fin-build draws it.
   - A **lottie** is for a real illustration that an icon cannot carry — a
     person, a scene, a device. **At most `lottie.max_per_chapter` in a chapter**
     and never two in adjacent scenes: they cost render time and a deck of them
     stops looking like a film. Give the search phrase, not a file
     (`"person checking finance app on phone"`), plus the accent hex fin-assets
     must tint it to.
   - Neither goes on the scene carrying the video's one big number — that scene
     already has its focal element, and tools/format/fin-storyboard.json caps it at one.
   - Emoji are not the icon system. See the note; use one only as a deliberate
     tonal break, and say in the log that you meant it.
5. **Every scene has a full-bleed background photo — no photo-free scenes**
   (creator rule 2026-07-28; `photo_free_scene_ratio` is 0). Per scene, list
   the bg image keyword AND a cut-in slot for each concrete thing the VO names
   (gym, bill, phone…), each cut-in anchored to its word's cue. Densest scene
   gets the CALMEST background — a quiet texture reading of the keyword, never
   no image.

## The -en pass
Port the skeleton and element IDs from `storyboard-hi.md` so fixes travel
between cuts; only deliberately divergent scenes get new IDs. Emit an explicit
**divergence list with a reason per scene**. Zero divergences is suspicious —
that is a translation wearing a layout costume; expect the audit to flag it.

## Writes
`vault/videos/<slug>/storyboard-<cut>.md` and
`studio/videos/<slug>-<cut>/assets/img/manifest.json` (`{"sN.jpg": "query"}`).

Return scene count and image-slot count (bg + cut-ins per scene).
