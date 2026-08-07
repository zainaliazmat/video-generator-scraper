---
summary: Chapter 2 fix pass (attempt 2) against fin-render-hi-ch2-1's two eye-only defects plus the orchestrator's derived-income constraint. Mega descender clearance fixed at the ARCHETYPE in a shared stylesheet so chapters 3-7 inherit it, the s16 funnel raised from .094 to .30 effective, and the build/runtime rate assert extended to derived income figures with a 10-case self-check covering every remaining chapter's beat. No timing touched, root still 77.571s, check passes with 0 lint errors and 11/11 AA.
updated: 2026-08-07
source: fin-render-hi-ch2-1.md D1/D2 · run.json constraints.derived_income_carries_assumption · tools/format.json chapter_design.{gotchas,art_opacity} · measured in-page font metrics (puppeteer + canvas actualBoundingBox) · snapshots/qa2/{b1,b2,zoom2}
---

# fin-build · passive-income-number · hi · CHAPTER 2 · attempt 2 (FIX PASS)

Three fixes, one regenerate, one check, 13 snapshot frames eyeballed. **No timing
was touched**: `build.mjs` re-derived every `data-start` / `data-duration` /
`data-framings` / `S` / `D` / `<audio>` row from `timing.json` as before and the
console line is identical to attempt 1 — root **77.571 s**, chapter offset
35.745 s, 12 scenes, tracks alternating 1/2.

## Artifacts

| Path | What |
|---|---|
| `studio/videos/passive-income-number-hi/assets/chapter-design-patch.css` | **NEW, and the file the orchestrator asked about — see below.** |
| `studio/videos/passive-income-number-hi-ch2/assets/chapter-design-patch.css` | symlink to the above |
| `studio/videos/passive-income-number-hi-ch2/build.mjs` | the generator; all three fixes live here or in the file it links |
| `studio/videos/passive-income-number-hi-ch2/index.html` | regenerated, 387 lines |
| `studio/videos/passive-income-number-hi-ch2/snapshots/qa2/{b1,b2,zoom2}` | 4 + 8 + 1 frames |
| `studio/videos/passive-income-number-hi-ch2/assets/audio.json` | UNCHANGED — see §4 |

---

## FIX 1 — mega-to-foot collision. Which file I changed, and why not the one you meant.

**Where the rule now lives:**
`studio/videos/passive-income-number-hi/assets/chapter-design-patch.css`, a new
file in the CUT's assets, symlinked into the chapter project and linked in
`<head>` immediately after `assets/chapter-design.css`.

**Where it BELONGS is `tools/scaffold/assets/chapter-design.css`** — every chapter
project symlinks that one file, so a rule there is inherited by 3-7 with no
further action. I could not write it: the fin-build contract is explicit
("Never write `.claude/` or `tools/`"), and the chapter project's
`assets/chapter-design.css` is a symlink INTO `tools/scaffold`, so editing it
through the project is the same write. This is the same wall ch1 hit on the
`.arch-b .foot` cap, which it answered by pasting a `.v-footwide` one-off into
the composition — that is the "five more discoveries" path and I did not repeat
it. The patch file is the strongest thing available inside my write boundary:
**one rule, one home, symlinked**, rather than the same rule re-typed into seven
inline `<style>` blocks. It is written as the exact text to paste upstream and
is deleted the moment it is pasted.

**The one line, ready to paste beside `.arch-b .foot { margin-top: 4px }`:**

```css
.arch-b .mega { padding-bottom: .11em; }
```

**Why .11em, measured in the page rather than guessed** (FinanceSans at 300px,
canvas `actualBoundingBox*` + computed line box):

| | |
|---|---|
| `.arch-b .mega` line-height | `.84` → line box **252px** |
| font ascent + descent | 321 + 88 = **409px** content box |
| half-leading | (252 − 409) / 2 = **−78.5px** → baseline sits 242.5px down, box ends only **9.5px** below the baseline |
| comma ink below baseline | **42.19px** |
| ⇒ ink hanging below the line box | **32.7px** |
| available gap | `.arch-b .stack` gap 18 + `.arch-b .foot` margin-top 4 = **22px** |

So the box collided by 10.7px and the ink by 3.7px — exactly the reported strike
of the first comma on the `f` of `of` and the second on `ari` of `arithmetic`.
`3.0%` on s13 descends **4.69px**, which is why the identical variant-B stack
does not collide there. **The trigger is the comma**, so the fix is on the
archetype and nothing is scene-scoped.

`.11em` = 33px at 300px = exactly the overhanging ink, so the mega's box now
contains its own descenders and the ladder's normal gap is air again:
**29.3px ink-to-ink on s15** (s13 goes 34 → 67). em rather than px so a future
change to the mega's size carries its clearance along. Verified on a 2x zoom
crop of the s15 comma band (`snapshots/qa2/zoom2`): clean background between
both comma tails and the foot's cap line.

**Chapter 1 is unaffected either way** — it has an `arch-b` scene (s7) but zero
`.mega` elements, so the rule is a no-op there and the approved ch1 render does
not need re-cutting when this moves upstream.

## FIX 2 — `#s16-afunnel`

`.18` → **`.58`**, in `build.mjs`'s `art16()`.

The floor in `chapter_design.gotchas` is about what lands ON SCREEN, and every
`fill-opacity` in this plate is multiplied by `.52` — `.has-photo.art-forward
.art` sets the layer opacity and is `!important`. So `.18` was **`.094`
effective**, half the floor, which is why the encode showed nothing. `.58 × .52
= .30` = `format.json art_opacity.over_photo` exactly, and it stays subordinate
to the sliver and the twelve ticks at `1.0 × .52 = .52`. **The proportion is
untouched**: bar 700 wide, sliver `700 × 0.030 = 21.0` = 3.00%, twelve cells of
700/12. On the new frame at t=53.95 the drawing reads as ONE object — bar, sliver
at its right end, funnel fanning down-left, twelve bars — so *that sliver, split
twelve ways* is finally on screen. (The graph-paper still is still the queued
fin-assets re-source; not touched.)

The multiplier is now written into the `art16()` header comment, because a
`fill-opacity` that looks legal and lands at half its value is a trap the next
chapter's drawn layer would walk into.

## FIX 3 — derived income figures

**On screen:** s17 gains a foot, in the storyboard's existing ILLUSTRATIVE
vocabulary, cued by the ladder's own variant-A slot (`fade` at +1.90, the same
slot s9's foot uses — no new timing, 0.80s after the statement, on screen for
3.58s of a 5.476s hold):

> ILLUSTRATIVE · ₹2,500 a month is 3.0% of the corpus, divided by 12

It deliberately does NOT restate `₹10,00,000`: the corpus token would have
pulled s17 into the CORPUS branch of the assert and demanded an `#s17-rate`
element, which is machinery this frame does not need. It carries both accepted
markers anyway — the literal rate token and the word ILLUSTRATIVE.

**In the assert** (both copies — `build.mjs` at build time, and the runtime IIFE
at the bottom of `index.html`, so neither a regenerate nor a hand-edit can get
around it):

```js
const DERIVED = /WHAT ₹[\d,]+ BUYS|₹[\d,]+\s*(?:\/|a |per )\s*(?:month|year)/i;
// satisfied by:  RATE.test(text) || /ILLUSTRATIVE/.test(text)
```

Two alternates because a derived income figure takes exactly two shapes across
this cut: the `WHAT ₹N BUYS` kicker (2.10, plus ₹5,000 / ₹10,000 / ₹12,500 in
the later rungs) and `₹N / month` (6.7, 6.15, 6.16). Either marker satisfies it,
per `run.json constraints.derived_income_carries_assumption`.

**Self-check, 10 cases, all pass** (run as a `node -e` one-liner, not left in the
tree): the original s17 string FAILS, the fixed one passes, s16 passes on its
existing rate, s15 is correctly *not* derived (it is corpus, and the corpus
branch still owns it), and every one of the four later-chapter beats
— `WHAT ₹5,000 BUYS`, `WHAT ₹10,000 BUYS`, `WHAT ₹12,500 BUYS`, `₹25,000 /
month`, `≈ ₹19,000 / month` — FAILS while bare. So chapters 3-7 cannot render one
of these frames without its assumption; nobody has to catch it on a draft.

---

## 4 · audio.json — regenerated, and it did NOT move

`python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch2` to
stdout, compared against the file on disk: **byte-identical**, so no `--write`
was needed. Still **23 real cues** (24 array entries — the first is the
`s13->s14 is a HOLD` marker) over s8-s19, bed `bed-resolve`, and the s13→s14
joint still correctly emits no transition.

Why it did not move even though I added a motion call: `cues.py` emits on scene
joints, `+1.10` statement rises, `pop()`ed numbers, rate pulses and framing
swaps. A `fade()` on a `.foot` is not a cue source — s9's foot fade at +1.90
produces none either. The other two fixes (a CSS padding, an SVG `fill-opacity`)
touch no motion call at all.

## 5 · `npm run check` — PASSED

```
Lint      0 errors, 3 warnings, 2 infos
Runtime   0 errors, 0 warnings          <- the extended assert runs here and is silent
Layout    0 errors, 0 warnings, 12 infos
Motion    0 errors, 0 warnings
Contrast  11/11 text checks pass WCAG AA
```

**0 lint errors, so the layout and contrast passes actually ran** (the
`_known_benign_note` failure mode). Every finding is the same set attempt 1
carried: `pointer_events_none` on `.grain` / `#root::after`,
`composition_file_too_large` (387 lines — one root html is mandatory for a
chapter project), `timeline_track_too_dense` (6 per track — the alternation
`overlapping_clips_same_track` requires), and the 12 layout infos, 11 of which
are `.bg`'s deliberate `inset: -8%` ken headroom plus `#s16-plate`'s declared
60px bleed past the right edge (archetype B's plate is 1120+860 on a 1920 frame,
by design). **No design token was edited to satisfy anything.**

## 6 · Snapshots — 13 frames, and I looked at all 13

One `-o` directory PER BATCH, never reused:

| Batch | Dir | Frames | What I checked |
|---|---|---|---|
| b1 | `snapshots/qa2/b1` | **4** at 34.66 / 48.10 / 53.95 / 59.47 | the four scenes this pass changed, each at its last cue |
| b2 | `snapshots/qa2/b2` | **8** at 1.80 / 7.38 / 13.33 / 21.72 / 27.39 / 38.80 / 64.34 / 71.02 | the eight untouched scenes, to prove nothing else moved |
| zoom | `snapshots/qa2/zoom2` | **1** at 48.10, 2x crop of `520,660,900,120` | the comma/foot band at native density |

All 13 clear the safe area, nothing overflows, the `cut-hi` watermark is on every
frame. The b1 frames are the evidence for FIX 1 (s15 clean, s13 unchanged in
character), FIX 2 (funnel present and connecting) and FIX 3 (s17 foot up).
The CLI's `Navigation timeout of 10000 ms` was retried in a loop as required;
each batch succeeded on the first attempt this run.

## 7 · What is still owed, and by whom

1. **`.arch-b .mega { padding-bottom: .11em; }` must be pasted into
   `tools/scaffold/assets/chapter-design.css`** and
   `assets/chapter-design-patch.css` deleted (plus its `<link>` and symlink).
   Until then, every chapter project must link the patch file — chapter 3 will
   inherit it only if its build does. **This is the only part of FIX 1 that is
   not done, and it is outside fin-build's write boundary.**
2. `.v-footwide` and `.v-ratespan` are still composition-inline one-offs
   carrying real system gaps (ch1's finding and ch2's `pulse()`-on-an-inline
   finding). Unchanged this pass; they belong in the same upstream edit.
3. s16's background still (`squared graph paper grid texture close up`) reads as
   a UI panel — fin-assets re-source, queued separately, deliberately not
   touched here.
