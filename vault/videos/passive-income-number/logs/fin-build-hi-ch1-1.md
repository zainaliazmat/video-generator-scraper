---
summary: hi chapter 1 (s1–s8, 42.475s) rebuilt for style E. The half-written build.mjs left by the killed session was one stray backtick away from parsing; fixed, run, and index.html regenerated from it — the stale style-A composition that pointed at the rotated photographs is gone. hyperframes check passes with 0 errors, both rate asserts armed and proven to fail, all 8 max-density frames eyeballed across two snapshot batches.
updated: 2026-08-08
source: run.json (constraints, chapters.hi.1._style_E_state_2026-08-08) + storyboard-hi.md §1–§12 + script-hi.md ch1 + studio/videos/passive-income-number-hi/assets/voice/timing.json + tools/format.json + tools/scaffold/assets/{blockframe,chapter-design}.css + knowledge/design-chapter-archetypes.md
stage: fin-build, cut hi, chapter 1, attempt 1
---

# fin-build — hi chapter 1, attempt 1

**STATUS: ok** · `hyperframes check` passes · root **42.475s**, 8 scenes.

## What the half-state actually was

The killed session's `build.mjs` (41 KB) was **complete and coherent** against the style-E
storyboard — every SCENES row matched §7 rows 1–8, the timing block read `timing.json` and
asserted GAPS rather than totals, both rate asserts were written. It did not run for one reason:

```
line 529:  rate must live in an element whose id starts `sN-rate`, …
```

a pair of backticks inside a comment **inside the `html` template literal**, which terminates the
literal and throws `SyntaxError: Unexpected identifier 'sN'`. One-character class of fault, total
blocker. Changed to double quotes; nothing else in the generator was touched.

`index.html` (2026-08-07 14:30, style A) was **regenerated**, not reused. Confirmed the danger the
handoff named: the style-E asset rotation re-keyed `assets-ch1/final/`, so the old composition's
`s1.jpg` is now the *alarm clock's* file, `s2.jpg` the chai counter, `s7.jpg` the staircase. The
old composition loads all eight of them and every check would have gone green.

## Timing — read, never re-derived

Source is `../passive-income-number-hi/assets/voice/timing.json` (Amrut `LHJy3mhZWsvhUjy0zUM1`,
measured, 519.331s). The chapter-local `assets/voice/timing.json` is byte-identical on lines
1.1–1.8; the generator reads the cut-level file so chapters 2–7 inherit one path.

| scene | line | start | dur | d-dur | track |
|---|---|---|---|---|---|
| s1 | 1.1 | 0.000 | 4.222 | 4.672 | 1 |
| s2 | 1.2 | 4.222 | 4.144 | 4.594 | 2 |
| s3 | 1.3 | 8.366 | 3.856 | 4.306 | 1 |
| s4 | 1.4 | 12.222 | 5.763 | 6.213 | 2 |
| s5 | 1.5 | 17.985 | 3.673 | 4.123 | 1 |
| s6 | 1.6 | 21.659 | 8.167 | 8.617 | 2 |
| s7 | 1.7 | 29.825 | 5.345 | 5.795 | 1 |
| s8 | 1.8 | 35.171 | 7.304 | **7.304** | 2 |

Every row is §7 verbatim. Rebase offset is 0.000 (chapter 1 opens the cut) but is still written as
an explicit subtraction. s8 carries its **bare** `scene_duration` — no successor to dissolve into;
`cut_assemble.py` adds the +0.45 back at fold-in. The generator throws if any joint's overlap is
not 0.45 ± 0.005, if any gap differs from the shipped cut's `scene_start` delta, if two adjacent
scenes share a track, or if any scene holds one photograph past 9.0s. **Nothing was re-timed to
make a layout work**; the four `S`/`D`/`<audio>`/root copies are all computed from the one file.

## The archetype layer

Sequence **A D A D A D B A**, §7 verbatim. `#root class="cut-hi"`, no body class (blockframe-9),
`data-framings` emitted on all eight (one value = `scene_duration`; ch1 declares no breach).
Five scenes are `art-off centred`; the three D scenes have something real on the other side —
1.2's chip cascade, 1.4's Lottie stage, 1.6's drawn count — each absolutely positioned into the
`.p-d` band rather than through `.row`, because `.row` is a child of `.stack` and `.arch-d` hangs
`.stack` at the top of the frame. Grounds are §11's: `#161f2b · #1a1e24 · #241d15 · #241d15 ·
#1c2027 · #291f13 · #1f1e1c · #191f28`, with `#241d15` held across s3/s4 so the buzz sits inside
one temperature. No role colour anywhere — the cut's first red is 3.8.

**NO RAIL.** No chapter title, no scene counter, no slide or rung number. Verified by grep and on
all eight frames. The watermark is `cut-hi` on `#root` only.

Every scene: `has-photo` + a real full-bleed `.bg` from `assets-ch1/final/`, one `ken` per scene
alternating `i o i o i o i o`, no plate push competing with it. No per-scene grade override.

## The two asserts, armed and proven

Wired into the composition and made to throw (a `console.warn` is what let this ship before).
Chapter 1 renders no figure, so both are vacuously true — they were still **positively
controlled** by planting a token in `#s5-stmt` and re-running the check:

- planted `₹10,00,000` → `✗ page_error: RATE ASSERT FAILED — s5 renders ₹10,00,000 with no
  #s5-rate carrying a rate` · **Check failed**
- planted `₹2,500 A MONTH` → fires **both** clauses, including
  `…with neither a rate nor an ILLUSTRATIVE marker in frame` (`derived_income_carries_assumption`)
- `index.html` regenerated afterwards and diffed byte-identical to the clean build; check passes.

Known limit, restated rather than papered over: this scans **on-screen tokens**, so it cannot see
a VO line that speaks a derived figure over a bare frame (`owed.derived_income_assert_is_frame_only`).
The storyboard closes that one case by hand at s65 (§4a); the VO cross-check belongs in
`pipeline_check`, not here.

## The comma-descender fix is picked up, not reintroduced

`assets/blockframe.css` and `assets/chapter-design.css` are **byte-identical to
`tools/scaffold/`** (verified by diff), so the fix carries in as
`.arch-b .mega { padding-bottom: .11em }` plus `.arch-b .foot { margin-top: 4px }`. Chapter 1
renders no `.mega` and no comma-grouped figure, so there is nothing here for it to bite — the
point is that the ch3–ch7 rungs inherit the fixed stylesheet by link, not by copy.

## Sound

`assets/audio.json`: bed **`bed-resolve`**, **12 cues** over 42.475s. Seven joint `transition`s
(no hold in ch1), `buzz` at 15.702 (s4 +3.48, the kit's one diegetic sound, picture leading it by
~0.73s), three `chip` clicks on s6's counted cascade, `stamp` at 36.271 on s8's `pop`. s1, s2, s3,
s5, s7 are declared dry. Every name is from `kit.json`. No music or SFX `<audio>` rows in the
composition; voice only, one row per line on track 10.

**I also rewrote `studio/videos/passive-income-number-hi/assets/cues-tables.json`** — flagging it
because it is outside this cut's directory. It still held the **style-A** tables (7 cold-open
scenes, a hold at `s13→s14`, buzz on `s3`), and style E renumbered the cut to 81 scenes, so every
entry named a different scene than it meant: `cues.py` would have suppressed the whoosh at a real
cut and punctuated a hold. Replaced verbatim with storyboard §2's block (5 holds, `buzz s4 3.48`,
`counted [s6]`, the 47-entry dry list). Zero invention; the storyboard assigns this file to
fin-build by name.

## Max-density snapshot pass — 8 frames, 2 batches, all 8 looked at

`-o snapshots/qa/b1` and `-o snapshots/qa/b2`, **separate directories**, because `snapshot` wipes
its output dir per run. Times are each scene's last cue + its duration (the settled worst case):

| batch | frames looked at | at |
|---|---|---|
| b1 | 4 | 1.80 (s1) · 6.97 (s2) · 10.17 (s3) · 17.40 (s4) |
| b2 | 4 | 19.79 (s5) · 24.76 (s6) · 31.63 (s7) · 37.57 (s8) |

Both invocations succeeded first try (no navigation timeout this session). Every `.stack` sits
inside the 1620×860 safe box; nothing overflows but the `.bg` layers, which is the architecture's
own `inset:-8%` and is the only Layout finding.

Two things the frames actually settle:

- **s4's Lottie draws, and the card carries the ₹.** Read off the encode-path frame, not off the
  file: the banner is on the phone's lower body, the mark is legible in the card icon, the amount
  is masked to two bars. That is the recorded ch1 round-1 blocker ("a notification arrived", not
  "money arrived") closed. The `grep ₹` false negative was not relied on.
- **s6's three drawn cells land over the photograph's three real jars** — bulb, sack, house, each
  with its checkbox ticked, one drawn cell per real jar, last mark complete at +3.10.

## Check result

```
Lint      0 errors, 3 warnings, 2 infos
Runtime   0 errors, 0 warnings
Layout    0 errors, 0 warnings, 10 infos
Motion    0 errors, 0 warnings
Contrast  10/10 text checks pass WCAG AA
Check passed
```

All findings are `known_benign`: `pointer_events_none` (`.grain`, `#root::after`),
`composition_file_too_large` (356 lines — a chapter is one file by design),
`timeline_track_too_dense` (4 per track, which is what the 1/2 alternation produces), and
`container_overflow` on every `.bg` (the full-bleed `inset:-8%`). **No design token was edited to
satisfy the checker.**

## For fin-editor — three declared items, built as specified, not silently fixed

1. **s3 → s4 is a DISSOLVE, not the script's declared continuous zoom.** Built that way per
   storyboard §10 and left for a real ruling. s3 is the reused chai-glass counter and contains no
   phone, so no crop of it can produce s4's frame; s4 was fetched on the same counter material so
   the place still reads as one place. The en cut's equivalent joint became a blocker when it read
   as two pictures and the answer there was to point both scenes at one file — **that answer is
   unavailable here.** Judge it from the encode.
2. **s2's photograph is a high-key clock face** and the chips sit across it rather than under it —
   the build's geometry note predicted the clock's base at y690 and it actually fills the frame.
   The pills are opaque so the copy is legible, but the frame is the chapter's brightest and the
   locked grade has no lever. Noted, not re-fetched (it is a verified reuse).
3. **fin-assets' two open caveats stand**: s8 is 1280px drawn at ~1.63×, and 5 of 8 frames are on
   wood. Both are encode calls.

## Notes for the next chapter build

- The generator pattern is chapter-agnostic: change `CH`, `LINES` and the `SCENES` table. The
  timing block, the asserts, the audio emitter and the rate asserts port unchanged.
- The inline `<style>` declares `.p-a`…`.p-d` from `format.json chapter_design.archetypes`
  because `chapter-design.css` does **not** carry the plate rects. Chapter 1 uses no plate (every
  scene is `art-off` or puts its mechanism in D's band), so they are currently unused there — a
  chapter with a real plate needs them present.
- `tools/audio/cues.py` was **not** run (outside this stage's bash allowlist). `assets/audio.json`
  is hand-derived from storyboard §2 and should be diffed against `cues.py --write` at render.
