---
summary: fin-build, en cut, attempt 2 — pure rebuild against fin-assets' six replaced images. `node build.mjs` reproduced index.html BYTE-IDENTICAL (same md5), so duration, timing, transitions and audio cues are unchanged at 505.561s; `pipeline_check check build` PASS. All six replaced slots re-snapshotted and reviewed at full and 3x resolution: every attempt-1 imagery defect is gone and no new one appeared.
updated: 2026-07-31
source: fin-build-en-1 rejection list + fin-assets-en-2 log + studio/videos/first-lakh-first-thousand-en/snapshots/qa2/
stage: fin-build, cut en, attempt 2
---

# fin-build — «The First $10,000 Is The Hardest» en, attempt 2 (rebuild)

## Result

| | |
|---|---|
| Composition | `studio/videos/first-lakh-first-thousand-en/index.html` (92 scenes, 1722 lines) |
| Duration | **505.561 s** — unchanged |
| `node build.mjs` | reproduced `index.html` **byte-identical** (md5 `9f83b352749b4afcede0638e39e6f7d1` before and after) |
| `pipeline_check check build` | **PASS build-en** |
| `npm run check` | 1 error, 95 warnings, 1 info · Runtime 0/0 · Motion 0/0 — the same linked-stylesheet false positive as attempt 1 and as the hi cut |
| Snapshots | 6 full frames + 5 zoom crops, **6 separate `-o` dirs**, all 11 reviewed at full or 3x |
| Verdict | **ok** |

## Why the rebuild is a no-op on the HTML, and why that is the right answer

`build.mjs` references images by basename (`assets/img/s36.jpg`), so replacing the file
changes the render without changing a byte of the composition. The identical md5 is the
proof that fin-assets' swap touched only pixels: timing, the `S` map, the 92 `<audio>`
rows, the root duration, the 89 dissolves + 2 shoves and `assets/audio.json` are all
exactly what gate ① already passed. Nothing else about the composition changed, as
instructed.

The retired s2 ↔ s88 jar pair costs the composition nothing structurally — neither scene's
copy ever named a jar (s2 is `THE TENTH $10,000 / 6 MONTHS`, s88 is
`RECAP TWO / The tenth $10,000: the same market buys 6.5`). The recall was carried by the
photography alone, so its loss is invisible to the build and is recorded here only so the
storyboard's §7 pair list is not trusted later. **s1 ↔ s87 is intact and is now the only
cold-open-to-payoff callback.**

## The six slots, re-checked at the resolution that catches defects

Full frames at each scene's max-density cue (`snapshots/qa2/b1`), then a 3x
`--zoom` crop on the background of every slot where text could be legible.

| slot | cue | verdict at 1:1 / 3x |
|---|---|---|
| **s1 (1.1)** 3.81 s | worn US singles on plank wood | `AMERICA`, green Treasury seal, distinct serials across notes. US. **Clean** |
| **s2 (1.2)** 9.92 s | fan of $100s | `FEDERAL RESERVE SYSTEM`, `Treasurer of the United States`, Geithner signature, Franklin. No crypto prop anywhere in frame. **Clean** |
| **s36 (4.6)** 194.66 s | two $1 notes | at 3x: `FEDERAL RESERVE NOTE`, `UNITED STATES OF AMERICA`, Washington, `WASHINGTON, D.C.`, green seal, serial `B57053322`; the second note's serial differs (`30…`), so no repeated-serial prop tell. **The attempt-1 blocker is closed** — the BEA 2.7 % statistic now sits on US currency |
| **s59 (6.7)** 320.75 s | banded roll on white | US-style engraving, green edge, no denomination and no foreign marking legible even at 3x. **Clean** |
| **s84 (9.2)** 456.65 s | hand signing with a plain blue pen | at 3x the form's only text is a blurred sub-legible block at the bottom-left; **no `Credit Card/Debit Card Authorization`, no brand, no product**. **Clean** |
| **s88 (9.6)** 480.67 s | three jars packed with rice, buckwheat, oats | currency-neutral, reads "full to the brim" literally. **Clean** |

Layout on all six is unchanged and correct: `.stack` inside the safe area, bar + rule +
focal + foot present, one focal per scene, nothing overflowing.

## One new watch item, from the 3x pass (not blocking, not a replaced slot)

**s59's mosaic MINOR panel (`s59-min`, untouched since attempt 1)** is a desk of US $2/$5/$10/$20
stacks on printed finance reports. At 3x, one report carries an *MTD revenue by currency*
bar chart listing `GBP USD EUR BRL AUD SGD CZK CNH CAD ZAR` and a `£10,000,000`/`£20,000,000`
axis. Every banknote in frame is US, and the panel is a ~640 px minor at delivery
resolution where none of that type resolves — so this is a **3x-only artifact, reported
rather than fixed**. Flagging it because "foreign currency symbol in frame" is a standing
rejection and a future 3x sweep will find it again; the honest reading is that a currency
column in a finance dashboard is on-message, not off it.

## Snapshot method — what was actually looked at

Six `-o` directories, one per invocation, none reused:

| dir | what | frames | CLI attempts |
|---|---|---|---|
| `snapshots/qa2/b1` | full frames, all six slots at their max-density cue | 6 | 1 |
| `snapshots/qa2/z84` | 3x crop of `#s84-img` | 1 | 1 |
| `snapshots/qa2/z36` | 3x crop of `#s36-img` | 1 | 1 |
| `snapshots/qa2/z1` | 3x crop of `#s1-img` | 1 | 1 |
| `snapshots/qa2/z59` | 3x crop of `#s59-min` (the minor) | 1 | 2 |
| `snapshots/qa2/z59b` | 3x crop of `#s59-img` (the replaced major) | 1 | 1 |

**11 frames captured, 11 read at full or 3x resolution.** No contact sheet was used as
evidence for anything. The `Navigation timeout of 10000 ms exceeded` fired once (z59) and
the retry loop absorbed it; every dir on disk is the run that succeeded.

`--zoom` on a scene's own image id is the sharp tool here and is worth writing down: it
takes a raised deviceScaleFactor crop rather than resizing anything, so layout, grade and
`ken` phase are identical to the shipped frame — which is exactly the property a currency
check needs. `--zoom-scale 3` at 1080p put ~5760 px across the band on s36.

Also worth noting for the next cut: I zoomed `#s59-min` before `#s59-img` and got a
different photograph than the one under review. **In a mosaic scene the replaced slot is
`#sN-img`; `#sN-min` is a second, unrelated file.**

## The one `npm run check` error — unchanged, still the system's

```
✗ invalid_parent_traversal_in_asset_path: 2 asset path(s) traversing above the project
  root with "../" (../fonts/, ../img/)
```

Both strings live in `tools/scaffold/assets/css/blockframe.css` (lines 24, 79); the
composition contains no `../`. This stage may not write `tools/`, and `known_benign` in
`format.json` is still `[]`, so it is neither patched nor suppressed here. It is a false
positive for a *linked* stylesheet — CSS `url()` resolves against the stylesheet, so
`assets/css/../fonts/` is `assets/fonts/`. Confirmed again empirically in this pass: all
11 frames render in real FinanceSans at weight 900 and the grain is visible.

**Third cut in a row reporting it.** Minimal fix for whoever owns `tools/`: move
`blockframe.css` to `assets/blockframe.css` and use `fonts/…` / `img/…`. Do **not** take
the linter's suggested `assets/fonts/…` — from `assets/css/` that resolves to
`assets/css/assets/fonts/` and 404s for real. Either fix it upstream or add the finding to
`known_benign`; leaving it as a live error on every build is what trains a stage to skim
its own checker.

## Everything from attempt 1 that still stands

The attempt-1 log is the design record for this composition and nothing in it was
invalidated: the glyph-safety assert, the `MUST_FOOT` assert, the type-ladder walk-downs,
the two `.v-*` workarounds (`.v-col1`, `.v-stamp`), the `preload="none"` requirement, the
grade-token decision, and the still-open items (anchored cues are storyboard `f` fallbacks;
the wipe is built as the system `dissolve`; `bed-resolve` is 248 s against a 505.561 s cut
and its second loop dip lands on the CTA — `owed_before_mix` stands).

Untouched watch items for gate ②, unchanged: **s22** legible "Platinum Credit Card ·
Cardmember Agreement" (630 px minor), **s71** the saturated seaside doors, **s64** blue
smoke against "Matches. Kindling. That's it.", **s24** / **s48** keyword drift, **s13** /
**s38-min** bilingual wall calendar, **s89** place names.

## Files

- `index.html` (unchanged), `build.mjs`, `snapshots-at.mjs`, `snapshots-at.txt`
- `assets/audio.json` (unchanged — `bed-resolve` + 23 cues)
- `snapshots/qa2/{b1,z1,z36,z59,z59b,z84}` — 11 PNGs
- attempt-1 evidence retained at `snapshots/qa/b1…b8` + `snapshots/qa/zoom-s36`
