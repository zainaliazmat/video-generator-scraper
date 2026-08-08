# fin-build · japanese-money-methods · en · chapter 2 · attempt 3
STATUS: ok — one file edited: `studio/videos/japanese-money-methods-en-ch2/chapter.json`

Scope was seven of the editor's twelve blockers (7, 8, 9, 10, 11, 12, 17). Nothing
else was touched: `-en/index.html` was read only, `-en-ch2/index.html` was not
written (it is generated), no render, no scaffold.

## What changed, finding by finding

**12 · the player and the wrappers.** Top-level `"lottie": ["stats-table-row",
"two-rates-30x", "who-is-counted", "one-number-travels"]`. The generator turns
that into `<script src="assets/js/lottie.min.js">` before `motion.js` plus the
four wrapper rows after it — the whole finding is solved by declaring the list,
not by hand-writing script tags into a generated file. Four is exactly
`max_per_chapter`, so no justification is owed and no fifth is available.

**7 · s15.** Was `arch: a`, no art, on a NUMBER beat. Now B — which is what this
file's own `note` already claimed ("holding B across s15/s16/s17") while the spec
said A. Carries `.band` + `<div class="lottie v-table" id="s15-lottie">` and
`playLottie(t15, S.s15 + 1.90, 4.00)`, verbatim from -hi. Behind it, -hi's column
ruling, so the row is pulled out of a table rather than out of nothing.

**8 · s17.** `#s17-hi` / `#s17-lo` deleted. They were arithmetically honest and
visually unreadable — a 1920-authored ratio slice-cropped into an 860px plate.
Replaced by `two-rates-30x` at `S.s17 + 1.90, 4.00` over a `.band`, with -hi's
measuring-rule field as the ground.

**9 · s19.** `who-is-counted` wired. Two things I changed from -hi's numbers on
purpose, and this is the part to check:

- -hi plays it at `S.s19 + 2.70` because -hi's framing boundary is +5.200. The
  -en scene's boundary is **+4.446** (`data-framings="4.446,3.407"`, already in
  the shipped cut). The Lottie's second pass — "everyone else" — begins at frame
  74 of 135, i.e. 54.8% through, = +2.466 into a 4.50s play. So the -en offset is
  **+1.98**, which puts the turn on 4.446 exactly. Copying -hi's 2.70 would have
  lit "everyone" 0.72s after the photograph already swapped to it.
- fence exit +4.30, open brackets +4.446, band up +1.50 / out +4.35 — the same
  shape as -hi, rebased onto the -en boundary.

28 of 108 lit is left alone. It is not 37.8% and must not become it: 37.8% is a
share of disposable income, not a share of households. The reason is now in the
scene comment, so it travels with the composition instead of only living in
`assets/lottie/src/who-is-counted.py`.

**10 · s20.** `one-number-travels` at `S.s20 + 1.90, 4.00`, over a `.band`. Also
switched s20 from A to **D** with `"centred": false`. A's stack is vertically
centred and would have landed on top of `.v-spread` (top 452px); D puts the type
in the upper band and gives the mechanism the lower two-thirds, which is what
-hi does and what this file's `note` already said the archetype was. `centred`
has to be explicit — the generator's default re-centres an `art-off` D and would
have dropped the stack straight back onto the Lottie. I did **not** port -hi's
concentric-ring SVG: the Lottie already radiates, and two radiating things over
one photograph is one too many.

**11 · s16 — the truth bug.** Track `width="1480"` at `x=220 y=716 height=96`,
nub `width="16"` = **1.08%**, full-frame viewBox, -hi's tick marks under it. The
previous build had 16px in a 600px track = 2.67% printed under a focal reading
"ABOUT 1%" — a drawn proportion 2.4x off a published figure. Root cause worth
naming: the pixel value was copied without the track it is a fraction OF. Track
width and nub width are a pair; the scene comment now says so at the point of
edit. Motion also taken from -hi (nub +1.20, pulse +2.60) so the growth finishes
before the pulse instead of overlapping it.

**17 · s13, s16, s17 — the plate.** All three now use `"plate": "p-a"` +
`"viewbox": "0 0 1920 1080"`. `p-b edge` gave them a 1px `var(--edge)` border on
an 860x610 box which read as a UI panel pasted on the photograph, and s13's
`"lift": true` filled that box with a visible dark gradient — that was the flat
grey rectangle. `p-a` is left:0/top:0/1920x1080 with no `edge` class, and
`.has-photo` already kills `.plate-in`'s background and the hatch, so the art now
sits *in* the picture with no container at all. `"lift"` dropped from s13.

Rule 8 held throughout: every drawn layer here is additive — a repetition, a
proportion, a subset, a spread. Rule 9 held: no per-scene photo darkening; the
three scenes that needed a darker ground for their Lottie got `.band` (s15, s17,
s19, s20).

## The system, as found

Nothing missing. `.band`, `.lottie`, `loadLottie`/`playLottie`, `p-a`, `art-forward`
and `centred` all did what was needed. The four `.v-*` stage rects are the only
new CSS and they went in `spec["css"]` (the chapter's own inline block), copied
from -hi. They are geometry, not tokens.

## ONE THING THAT WILL SILENTLY BLANK ALL FOUR

`studio/videos/japanese-money-methods-en-ch2/assets/lottie` **does not exist.**
The chapter's `assets/` links were made at 08:03 on 2026-08-05; the cut's
`assets/lottie/` directory was created at 00:32 today, so `scaffold()` never saw
it and never made the link. `assets/js/lottie.min.js` IS linked and fine.

Without that symlink the four `<script src="assets/lottie/*.js">` rows 404,
`window.L_*` is undefined, `loadLottie` throws on the first one and **every
later timeline in the script never registers** — the chapter renders as
photographs with type and no art at all, and `hyperframes check` passes.

Fix before generating: run `tools/chapter_project.py japanese-money-methods
--cut en --chapter 2 --scaffold`. The `--scaffold` flag is not optional this
time. (I did not create the link myself — I was told not to scaffold.)

## What to check in the encoded mp4, and where

I cannot render, so these are the four proofs. Chapter-local timestamps (add the
chapter's start if checking the concatenated cut). Scene starts inside the
chapter: s15 11.971, s16 18.883, s17 25.247, s19 40.065, s20 47.918.

| # | Lottie | look at | must show |
|---|--------|---------|-----------|
| 7 | stats-table-row | **00:15.4** (s15 +3.4, mid-play) | a table row lifted clear of the rows around it, in the 1040x430 box under the type. A frozen or absent row = blank-mode. |
| 8 | two-rates-30x | **00:28.6** (s17 +3.4) | TWO bars, the lower one a sliver ~1/34 of the upper. If you see one bar and nothing under it, the second never drew. |
| 9 | who-is-counted | **00:42.5** (s19 +2.4) then **00:45.0** (s19 +4.9) | at 42.5 a scattered green minority in a faint 18x6 grid; at 45.0 the whole grid lit. Same frame twice = blank-mode or the offset is wrong. |
| 10 | one-number-travels | **00:50.6** (s20 +2.7) | rings leaving ONE token, the other token still. |

Two failure modes, both of which pass every check:
1. **Missing player or missing wrapper** (the symlink above) — the `.lottie` div
   is empty, so you see the photograph, the band and the type, and a clean
   rectangle of nothing where the art should be. Distinguishing sign: *all four*
   are blank, and s16 (no Lottie, pure SVG) still animates.
2. **Loaded but never advanced** — `playLottie` not on `tl`, or seeking past the
   end. The art is visible but identical in every frame of the scene. Test:
   compare 00:42.5 against 00:45.0 on s19; if those two frames match, the play
   is frozen and the fix is the offset, not the wiring.

Also worth one glance while you are there: **00:20.1** (s16 +1.2 to +2.3) — the
nub should stop at roughly one hundredth of the track. If it looks like a
noticeable chunk, the 1480 did not survive.

## Not mine, flagged

- s19's `fade("#s19-bg2", …)` and the `-hi.jpg` filenames live in the shipped
  `-en/index.html` and are yours. My s19 art and Lottie are timed to +4.446; if
  the framing split moves, those four offsets move with it.
- Findings 1–6, 13–16, 18, 19 (photographs, kicker copy, the type cue ladder)
  are all in the shipped cut, untouched here.
