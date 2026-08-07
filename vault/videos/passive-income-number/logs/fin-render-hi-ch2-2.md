---
summary: Chapter 2 draft re-render + contact sheet after fin-build's fix pass. All three fixes verified from the ENCODED frames, with numbers - 31/33px ink-to-ink comma clearance on s15 (was a strike), the s16 funnel present and its proportion measured subpixel at 3.002% against a declared 3.000%, and s17's derived figure now carrying both the rate and an ILLUSTRATIVE marker. Spine did not move - 2328 frames, 23 cues, silent s13-s14 joint, zero black. s16's background still is confirmed as a UI-panel failure and needs an fin-assets re-source.
updated: 2026-08-07
source: renders/DRAFT-ch2-v2.mp4 (encoded frames) - ffprobe -count_frames, ffmpeg blackdetect/astats/signalstats, per-pixel ink measurement on extracted PNGs, tools/chapter_sheet.py
---

# fin-render · passive-income-number · hi · CHAPTER 2 · attempt 2

Mode: **chapter draft** (§3b step 4). No gate two, no encode, no master QA.
Round 2, against `fin-render-hi-ch2-1.md` D1/D2 and the orchestrator's derived-income constraint.

## Commands run

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch2-v2.mp4 -q draft -f 30
python3 tools/chapter_sheet.py . renders/DRAFT-ch2-v2.mp4 -o renders/SHEET-ch2-v2.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30` as required.

## Artifacts

| Path | What |
|---|---|
| `studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2-v2.mp4` | 19.0 MB, h264, 1920x1080, 30/1 |
| `studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2-v2.jpg` | 13 cells, 4 cols |
| `studio/videos/passive-income-number-hi-ch2/renders/SHEET-ch2-v2.json` | index the orchestrator's cross-chapter PNG reads |

## The spine did not move

| Metric | Round 1 | Round 2 | Verdict |
|---|---|---|---|
| Frame count (`-count_frames`) | 2328 | **2328** | identical |
| Video stream duration | 77.600 s | **77.600 s** | identical |
| Container duration | 77.610667 s | **77.610667 s** | identical |
| Frame rate | 30/1 | **30/1** | identical |
| Declared root `data-duration` | 77.571 s | **77.571 s** | identical |
| 77.571 x 30 | 2327.13 -> ceil 2328 | same | expected, harmless |
| `blackdetect` d=0.1 pic_th=0.97 | 0 | **0 segments** | pass |
| Audio peak / RMS / flat (VO only, pre-mix) | -5.25 / -25.29 / 0 | **-5.25 / -25.29 / 0** | bit-identical, so no timing moved |
| `audio.json` | 24 entries = 1 hold marker + 23 cues | **same** | pass |
| s13->s14 joint (36.382) transition cue | none | **none** | pass - the hold is still silent |
| Rail | none | **none** | `#root class="cut-hi"`, no `rail` class, `chapter_design.rail` false |
| Render wall time | 2 m 40.3 s | 3 m 24.2 s | slower machine load, not a signal |

The +0.87-frame ceil is the same one round 1 measured and explained; `cut_assemble.py` writes one
rebased composition rather than concatenating video, so it never accumulates. Nothing to do.

The audio track being **bit-identical** to round 1 (same peak to 4 decimal places, same RMS, same
flat factor) is the strongest available evidence that none of the three fixes touched timing: a CSS
padding, an SVG `fill-opacity` and one added `<p class="foot">` cannot and did not move a cue.

---

## FIX 1 - the comma collision (round-1 D1). **VERIFIED, and measured.**

Rule read back at its promoted home, `tools/scaffold/assets/chapter-design.css:141-142`:

```css
.arch-b .mega { font-size: 300px !important; line-height: .84; letter-spacing: -14px;
                padding-bottom: .11em; }
```

The patch file and its `<link>` are gone: `index.html` links exactly two stylesheets
(`assets/blockframe.css`, `assets/chapter-design.css`) and both are symlinks into `tools/scaffold`.
**So what shipped is the archetype rule, not a scene fix, and chapters 3-7 inherit it with no action.**

### Ink-to-ink measurement on the encoded s15 frame (t=48.100, native 1920x1080)

Per-column lowest bright-ink row in the mega band vs the foot's topmost ink row **in the same columns**:

| Comma | Column run | Comma ink bottom row | Foot ink top row | **Clearance** |
|---|---|---|---|---|
| first (`10,`) | x 760-809 | 718 | 750 | **31 px** |
| second (`00,`) | x 1162-1211 | 717 | 751 | **33 px** |

Round 1 had 32.7px of comma ink hanging *below* the line box against a 22px stack gap - a strike, with
the first comma through the `f` of `of` and the second through `ari` of `arithmetic`. Both strikes are gone;
there is clean graded background between every comma tail and the foot's cap line.

Whole-stack ink runs on the same frame, for the record: kicker 314-334, sub 377-404,
mega 460-718 (259px incl. descenders), foot 751-769. Global mega-to-foot air **32px**.

fin-build predicted 29.3px from in-page font metrics; the encode measures 31-33px. The 2-4px
difference is the anti-alias threshold, not a discrepancy.

### No regression on the chapter's other `.mega`

`s13` (t=34.884) is the only other `.arch-b .mega` in the chapter (`3.0%`, which descends ~4.7px and
never collided). Checked by eye: stack still vertically centred, foot still inside the safe area,
the extra .11em simply reads as a slightly more generous ladder. `s14` and `s16` are `arch-b` but
carry no `.mega`, so the rule is a no-op on them. Chapter 1 has an `arch-b` scene with zero megas -
the approved ch1 render does not need re-cutting.

## FIX 2 - `#s16-afunnel`. **VERIFIED, and the proportion is intact.**

`fill-opacity` `.18` -> `.58`; the `.has-photo.art-forward .art` layer multiplies by `.52`, so effective
is `.58 x .52 = .3016` = `format.json chapter_design.art_opacity.over_photo` (0.30) exactly, and above
the ~.2 floor in `chapter_design.gotchas` that `.18 x .52 = .094` was under.

On the encoded frame at t=53.950 the drawing reads as **one connected mechanism**: the pale corpus bar,
the green sliver at its right end, the wedge fanning down-and-left from that sliver to full bar width,
and the twelve bars beneath it. *That sliver, split twelve ways* is now a sentence the picture states.
Round 1's "two unrelated objects" is fixed.

### Measured from the frame, not the source

| Quantity | Method | Value |
|---|---|---|
| Corpus bar width | luma integral / plateau (subpixel, AA-unbiased) | **662.69 px** |
| Sliver width | greenness integral / plateau | **19.89 px** |
| **Sliver / bar** | | **3.002 %** |
| Declared | `x=719 w=21` on a `x=40 w=700` bar | 3.000 % |
| Bar right edge vs sliver right edge | | 1858 vs 1859 px - flush |
| Tick count | greenness runs at y=520 | **12** |
| Funnel top edge span | | the sliver's 21 units |
| Funnel bottom edge span | | the full 700-unit bar width, over the ticks |

The naive threshold-count reads 24px/698px = 3.44%; that is 100% anti-alias bleed on a 21px rect.
The integral method is the honest one and it lands on **3.002%**. The truth bar is met.

## FIX 3 - s17's derived income figure. **VERIFIED.**

Frame at t=59.470 carries, in the same frame as `WHAT ₹2,500 BUYS`:

> ILLUSTRATIVE · ₹2,500 a month is 3.0% of the corpus, divided by 12

Both accepted markers are present - the literal `3.0%` rate token **and** the explicit `ILLUSTRATIVE`
word - satisfying `run.json constraints.derived_income_carries_assumption` twice over. Cued by the
existing variant-A `fade` slot at +1.90, on screen for 3.58s of a 5.476s hold; no new timing.

The structural half is in the composition too: `index.html:394` carries the runtime
`var DERIVED = /WHAT ₹[\d,]+ BUYS|₹[\d,]+\s*(?:\/|a |per )\s*(?:month|year)/i;` alongside the corpus
assert, so chapters 3-7 cannot render `WHAT ₹5,000 BUYS` / `₹25,000 a month` bare.

---

## Cross-dissolve boundaries - re-sampled, because FIX 1 changed a stack's height

Three boundaries, at **both** `qa.dissolve_sample_offsets` where it is informative.

| Boundary | Offset | t | What the frame shows |
|---|---|---|---|
| s15 -> s16 | +0.225 | 50.877 | outgoing s15 stack still up and fading, **incoming s16 text not yet risen** - the documented structural blind spot, behaving exactly as `_dissolve_note` says. The comma clearance holds mid-dissolve. |
| s15 -> s16 | +0.38 | 51.032 | incoming `THE SUM` crisp; outgoing `₹10,00,000` a ghost **under** it, visibly occluded by the incoming plate. Correct z-order. |
| s16 -> s17 | +0.38 | 57.448 | incoming `WHAT ₹2,500 BUYS` crisp over the ethernet photo; outgoing green s16 stack ghosted **under** the incoming photograph. |
| s17 -> s18 | +0.38 | 62.924 | incoming `ALL TWELVE MONTHS` crisp; outgoing s17 stack ghosted **under** the incoming photograph. |

No double-paint at any boundary. `.scene { isolation: isolate }` still holding.

## Contact-sheet cells that read as broken and are not (unchanged from round 1)

`chapter_sheet.py` samples every non-Lottie scene at start + 2.6s.

* **s13 cell shows no `3.0%`** - `pop("#s13-num", 34.061)` is start + 3.677, anchored to its spoken word.
* **s15 cell shows `₹8,36,874` and no foot** - mid `countUp` (46.318 -> 47.518), 0.1s before the foot fades in.
* **s16 cell (t=53.252) shows the funnel faint but present** - `fade("#s16-afunnel", +2.30, 0.5)` completes at 53.452, so the sheet samples it 0.2s before it is fully up. It is fully up and reads correctly from 53.5 on; judge s16 from the mp4, per `chapter_design.gotchas`.

---

## Still open, and NOT fixed this pass: s16's background still

**My call: yes, it needs an fin-assets re-source.** Looked at both the graded frame and the raw source.

`assets-ch2/final/s16.jpg` (`squared graph paper grid texture close up@pexels`) is a scanner-flat,
edge-to-edge, axis-aligned repeating grid. There is **no photographic cue anywhere in it**: no
perspective, no object boundary, no shadow, no light falloff, no depth of field, no paper edge. It is
visually indistinguishable from a CSS `repeating-linear-gradient`, and `art-lift`'s dark plate on top
finishes the job - the frame reads as a UI panel on a UI background, the only frame in the chapter
that does not read as film. This is the near-miss `format.json layout.image_relevance` forbids in so
many words: *"When a slot cannot be photographed, change the SOURCE or draw it - never accept a
near-miss."*

**Why the source-YHIGH gate cannot catch it, stated precisely.** The graded frame measures
YAVG 58.0 / YLOW 47 / YHIGH 66 - spread 19. `s10` (the calendar) measures YAVG 61.7 / spread 17 and
reads unmistakably as a photographed wall calendar, because it has pins, a curled paper edge, shadows
and perspective. **The two are numerically indistinguishable and visually opposite**, so luma is the
wrong feature: the failure is the *absence of an object*, not brightness. If this is ever mechanised,
the signal is "the still contains an edge that is not part of a periodic grid", not a luma percentile.

What the slot actually needs is the same idea photographed *on an object in a room* - a graph-paper
notebook on a desk at an angle, pen and lamp shadow across it - which keeps the grid-means-arithmetic
association and gives the frame depth. fin-assets' call, not mine.

Note that **FIX 2 is independent of this**: the drawn mechanism now reads correctly regardless of
what is behind it. Re-sourcing the still improves the frame; it does not re-open the funnel finding.

## What I did not do

No gate-two frame set, no encode, no faster-whisper pass, no VO-drift measurement, no loudnorm/dBTP
read. All of that belongs to the full-cut render, not the chapter loop. The audio figures above are
the raw VO track only; `assets/audio.json` is a post-mix step and is not in this draft.
