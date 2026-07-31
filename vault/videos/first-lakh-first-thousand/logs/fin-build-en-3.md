---
summary: fin-build, en cut, attempt 3 — rebuild against fin-assets' three replaced images plus ONE structural fix: a bar copy that is empty or a bare dash now suppresses the title bar entirely, so s91's CTA no longer holds a full-width black bar carrying one dash. Duration unchanged at 505.561s, `npm run check` unchanged (1 error / 95 warnings — the same linked-stylesheet false positive), all four timing homes still agree.
updated: 2026-07-31
source: fin-render-en-1 s91 report + fin-assets-en-3 log + studio/videos/first-lakh-first-thousand-en/snapshots/qa4/
stage: fin-build, cut en, attempt 3
---

# fin-build — «The First $10,000 Is The Hardest» en, attempt 3

## Result

| | |
|---|---|
| Composition | `studio/videos/first-lakh-first-thousand-en/index.html` (92 scenes, 1720 lines) |
| Duration | **505.561 s** — unchanged from attempt 2 |
| `npm run check` | 1 error, 95 warnings, 1 info · Runtime 0/0 · Layout 0/0 · Motion 0/0 — identical counts to attempt 2 |
| Timing homes | 92 sections / 92 `<audio>` / 92 `S` keys / root 505.561 — **0 mismatches**, tracks alternate 1-2, every non-last scene overlaps the next by 0.45 s |
| Snapshots | 13 frames in **5 separate `-o` dirs**, none reused; **10 read at full or 3× resolution**, 3 measured numerically |
| Verdict | **ok** |

## 1. The s91 title bar — root cause and the general fix

fin-render is right that the bar renders one short dash, and the cause is upstream of the
composition. **`script-en.md` 9.9 literally says `bar: —`**, using the same em dash the
storyboard uses in every "none" cell of its scene table. The scene table in `build.mjs`
transcribed that dash as *copy* and the builder rendered it as a title.

So the fix is not to invent CTA wording (none was ever approved) and not to special-case
s91. It is one predicate in `build.mjs`, applied to every scene:

```js
const blankBar = (s) => !String(s ?? "").replace(/[—–-]/gu, "").trim();
```

When it is true the stage now: skips `glyphCheck`, skips `ladderFit`, emits **no**
`.swissbar` element at all, and drops the `rise("#sN-bar", …)` cue — a cue on a missing
selector is a silent GSAP no-op, so leaving it would have been a second latent defect.
A 7-case `die()` assert sits directly under the predicate, so a future copy edit that
re-introduces a placeholder bar fails the build instead of shipping a dash.

**Why suppression is safe geometrically.** `.swiss-band .scene` is
`grid-template-rows: 60px 120px 600px 240px 60px` with `.swissbar` pinned to row 2, and
the aperture is absolutely positioned at `top: 180px`. Removing the bar leaves row 2 empty
rather than reflowing anything: rows 1+2 become one continuous 180 px of `--bg` above the
band, matching the 60 px above every other scene. Verified in the frames — the rule, the
`--pop` block and the foot are all exactly where they were.

Count check on the emitted HTML: **91 `.swissbar` for 92 scenes, 92 `.swissrule`, 91 bar
cues.** Exactly one scene suppressed, and it is s91.

**The rule stays.** A rule with the statement hung under it is a complete Vignelli element
on its own and appears in all 92 scenes; the bar is the part that read as breakage. Losing
both would have made the CTA the only scene missing two system elements.

⚠ **The hi cut carries the identical latent defect.**
`studio/videos/first-lakh-first-thousand-hi/build.mjs:113` is
`["9.9","B","cta","pop","—","SUBSCRIBE",null,"s85",null,507.17]` — same dash, same CTA
scene. That cut is out of this stage's scope (cut: en) and has already rendered, so I did
not touch it. The predicate above is a three-line port when someone owns that decision.

## 2. The three replaced images — what was actually looked at

`node build.mjs` reproduced the composition against the new files; images are referenced
by basename, so the swap changes the render without changing timing. md5 moved
(`9f83b35…` → `a5bf922…`) **only** because of the s91 bar fix.

### s21 — the question fin-assets asked

**Answer: it holds, and it needs no second `filter:` override. The one per-video grade
allowance can stay on s90.**

Three frames across the full ken sweep, plus numeric luminance on the 1920×600 aperture
(`sharp`, greyscale, after the CSS grade):

| frame | ken scale | mean | p50 | p90 | p99 | % below 16 |
|---|---|---|---|---|---|---|
| s21 t=109.20 (darkest — just after the dissolve) | 1.01 | — | — | — | — | eyeballed |
| s21 t=110.18 | ~1.03 | 32.4 | 9 | 93 | 135 | 55.0 % |
| **s21 t=114.25 (ken MAX, 0.09 s before scene end)** | **1.16** | **38.7** | **22** | **96** | **137** | **46.5 %** |

The load-bearing finding: **the ken push makes this scene brighter, not darker.** Mean
rises 32.4 → 38.7, median 9 → 22, and the sub-16 black share drops 55 % → 46.5 %, because
the 1.0→1.16 push crops away the unlit surround and fills the aperture with the lit pages.
The scene's worst frame is its *first*, and at that frame the subject is already legible.

Against the two reference points on this same cut:

| reference | mean | p50 | p90 | reading |
|---|---|---|---|---|
| s10 legal pad (bright) | 117.4 | 138 | 144 | top of the cut's range |
| s63 cold fire pit (dark, no override) | 70.2 | 60 | 124 | ordinary dark scene |
| **s90 — the scene that DID need `brightness(1.25)`** | **14.5** | **12** | **19** | crushed: p90 = 19, 89 % of pixels below 16 |
| s21 at ken max | 38.7 | 22 | 96 | subject at p90 = 96 with p99 = 137 |

s90's failure mode is that its *top decile* sits at 19 — there is no subject left to see.
s21's top decile sits at 96 with headroom to 137. It is a chiaroscuro frame, not a crushed
one, and reads as deliberate low-key still-life. Visually confirmed at all three times:
open ledger pages at clear mid-tone, every abacus rod and bead resolved, desk plane and
the ruler at lower left present. **No text of any kind in the frame** — the `SUMA PLN`
receipt is gone.

### s57 — serials

Read at both ken extremes (306.60 at scale 1.16, 312.60 at scale 1.00) and at the
309.61 focal cue. Three overlapping US $20 notes; legible engraving is `20`, `20`,
`TWENTY` and a partial `FED…`. **No serial number is inside the 3.2:1 aperture at any
point in the sweep**, so the identical-`E 34112707 E` defect cannot recur here — the crop
never reaches the part of the note that carries one. Currency correct for the en cut.

One process note worth keeping: my first attempt at s57's ken maximum used **306.05**,
which is 0.16 s into the s56→s57 cross-dissolve and returned a frame of **s56's
cheesecake**, not s57. After a transition-carrying scene starts, the first safe sampling
time is `scene_start + transition_seconds`; anything earlier silently photographs the
outgoing scene. Discarded that frame and re-took at 306.60.

### s91 — pen markings

Full frames at 497.86 and 499.70, plus a 3× `--zoom "#s91-img"` crop (~5760 px across the
band). The pen barrel is **completely unmarked** — no engraving, no brand, no country of
manufacture; the notebook is blank ruled paper. `Kaweco AL Sport Germany` is gone. The
only non-wood mark in the whole aperture is an indistinct pale scuff on the desk at lower
left that does not resolve into glyphs even at 3×.

Composition note, not a blocker: the right two-thirds of s91's aperture is empty dark
wood. It reads as a deliberate "laid down, finished" close and matches the storyboard's
intent, but it is the emptiest frame in the cut.

## 3. Snapshot method — the honest count

Five `-o` directories, one per invocation, **none reused** (`snapshots/qa4/…`; `qa`,
`qa2`, `qa3` from earlier stages left untouched):

| dir | at | frames | CLI attempts | how reviewed |
|---|---|---|---|---|
| `qa4/b1` | 110.18, 309.61, 497.86 — each scene's last cue | 3 | 1 | all 3 read full-res |
| `qa4/b2` | 114.25, 306.05, 499.70 — ken extremes | 3 | 1 | all 3 read full-res (306.05 discarded, see above) |
| `qa4/b3` | 48.40, 342.30, 493.85 — luminance references | 3 | 1 | measured numerically, **not** opened |
| `qa4/b4` | 109.20, 306.60, 312.60 — corrected extremes | 3 | 4 | all 3 read full-res |
| `qa4/z91` | 499.70, `--zoom "#s91-img" --zoom-scale 3` | 1 | 1 | read at 3× |

**13 captured · 10 read at full or 3× resolution · 3 measured numerically.** No contact
sheet was used as evidence for anything. `Navigation timeout of 10000 ms exceeded` fired
three times on b4 and the retry loop absorbed it; every directory on disk is the run that
succeeded.

New tool worth writing down: `sharp` is already in `node_modules`, so a greyscale
histogram of the 1920×600 aperture is a one-liner. "Does this dark image hold?" stops
being an opinion and becomes p50/p90 against s90, the cut's known-crushed scene. That
comparison is what makes the "no second override" answer defensible.

## 4. The one `npm run check` error — unchanged, still the system's

```
✗ invalid_parent_traversal_in_asset_path: 2 asset path(s) traversing above the project
  root with "../" (../fonts/, ../img/)
```

Both strings live in `tools/scaffold/assets/css/blockframe.css` (lines 24, 79); the
composition contains no `../`. This stage may not write `tools/`, and `known_benign` in
`format.json` is still `[]`, so it is neither patched nor suppressed. It is a false
positive for a *linked* stylesheet — CSS `url()` resolves against the stylesheet, so
`assets/css/../fonts/` is `assets/fonts/`. Confirmed empirically again: every frame in
this pass renders in real FinanceSans at weight 900 with the grain visible.

**Fourth cut in a row reporting it.** The fix for whoever owns `tools/`: move
`blockframe.css` to `assets/blockframe.css` and use `fonts/…` / `img/…`. Do **not** take
the linter's suggested `assets/fonts/…` — from `assets/css/` that resolves to
`assets/css/assets/fonts/` and 404s for real.

## 5. Everything from attempts 1–2 that still stands

Unchanged and not re-litigated: the glyph-safety assert, `MUST_FOOT`, the type-ladder
walk-downs, `.v-col1` / `.v-stamp` (both still workarounds for real `blockframe.css`
defects), `preload="none"` on all 92 `<audio>` rows, the s90 grade override, the 89
dissolves + 2 shoves, `assets/audio.json` (`bed-resolve` + 23 SFX cues, byte-identical).

Open items carried forward: `bed-resolve` is 248 s against a 505.561 s cut and its second
loop dip still lands on the CTA — `owed_before_mix` stands. Attempt-2's 3× watch items
(s59's minor dashboard, s22, s71, s64, s24/s48, s13/s38-min, s89) are untouched and
unchanged.

## Files

- `index.html` (bar fix only), `build.mjs`, `snapshots-at.mjs`, `snapshots-at.txt`
- `assets/audio.json` — unchanged
- `snapshots/qa4/{b1,b2,b3,b4,z91}` — 13 PNGs
- attempt-1/2 evidence retained at `snapshots/qa/*` and `snapshots/qa2/*`
