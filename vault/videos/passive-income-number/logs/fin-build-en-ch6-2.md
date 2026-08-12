---
summary: Attempt-2 rework of en chapter 6 — s77's five reference rungs refilled fund-green (review blocker 1, now ΔRGB 38.8–40.7 against the overrun's 45.8), s71's stale storyboard prose corrected for the replaced photograph and its amber figure re-sampled at 6.68:1 on the new brighter ground. Nothing re-timed; check PASS.
updated: 2026-08-12
source: studio/videos/passive-income-number-en-ch6/{build.mjs,index.html}; vault/videos/passive-income-number/logs/{review-en-ch6-1.md,fin-assets-en-ch6-2.md}; measured on snapshots/qa/{b6,b7,b8} composed frames
---

# fin-build · passive-income-number · en · chapter 6 · attempt 2

STATUS: ok. Two blockers closed, both measured on composed frames rather than predicted.
`studio/videos/passive-income-number-en-ch5/` never opened.

## Ran

1. `vault/CLAUDE.md`, `tools/format/fin-build.json`, `tools/packs/fin-build.md` (all four BOXes
   + the two body sections that are this stage's). No OPENED-BODY owed —
   `design-finance-blockframe.md` and `design-chapter-archetypes.md` were not opened; every
   value needed was in `blockframe.css`, `chapter-design.css` or the pack.
2. `review-en-ch6-1.md` and `fin-assets-en-ch6-2.md` in full, before touching anything.
3. Read the new `assets-ch6/final/s71.jpg` at full resolution — the object description had to
   come from the pixels, not from fin-assets' prose about them.
4. **Edited `build.mjs`, not `index.html`.** `index.html` is GENERATED (`node build.mjs` from
   `../passive-income-number-en/assets/voice/timing.json`); a hand-edit there survives until
   the next regeneration and then silently disappears. Both fixes are in the generator. The
   first pass of this attempt did hand-edit `index.html`, and regenerating overwrote it —
   recorded because that is the trap, not a confession of process.
5. Re-implemented the chapter's composed tone chain to re-measure the ONE scene whose
   photograph changed, and validated the re-implementation against four scenes whose files
   are byte-unchanged before trusting it (below).
6. `node build.mjs` → `npm run check`.
7. Max-density snapshot pass, 13 of 13 scenes at each scene's own LAST cue + 0.75s, plus the
   s76→s77 dissolve midpoint and s77 at +1.5s. Three batch dirs, `-o` never reused.
8. Two measurement scripts over the composed PNGs (ΔRGB on the rungs, WCAG on the amber).

## Failed

**The one real failure this attempt, and it is the documented one.** A retry loop I had left
running in the background re-invoked `hyperframes snapshot` into `snapshots/qa/b5` while I was
reading frames out of it, and `snapshot` WIPES its `-o` directory on every run. Four of the
seven frames were gone before the second read. Killed the loop, re-shot into `b7`/`b8`, and
re-ran the s71 measurement on a *second, independent* shot to prove the number was not read off
a half-written file: `b5/frame-02-at-15.86s.png` and `b8/frame-00-at-15.86s.png` return
identical figures (9,821 glyph px, 6.68:1, worst-5% 4.17:1). The rule in the brief is about
batching; the sharper form is **never leave a snapshot retry loop alive while you read the
frames it writes.**

**The reviewer's finding 3 could not be taken, and it is a real conflict, not a decline.**
Finding 3 asked to pull `fade("#s77-foot")` from +6.39 to ≈+5.0 if finding 1 touched this scene
anyway. It does — but `build.mjs`'s own cue sweep enforces `layout.cue_min_gap_seconds = 0.8`
between two authored elements in a scene, and s77's num cue is at **+5.59**:

| foot at | gap to the +5.59 num cue | verdict |
|---|---|---|
| +6.39 (shipped) | **0.80** | exactly the floor — which is why it is 6.39 |
| +5.59 (lands with the figure) | 0.00 | throws |
| +5.00 (the review's number) | 0.59 | throws |

The 1.52s hold review measured is what the 0.8s cue floor leaves once the anchor at +5.59 and
the 1.10s countUp are fixed, and both of those are measured and untouchable. Moving the foot
means either moving the spoken anchor or exempting a non-cascade pair from the gap floor.
Neither is worth 0.8s of foot hold on a note review itself graded "not a
`derived_income_carries_assumption` failure" — the binding assumption
`AT A 1.08% DIVIDEND YIELD` is in frame from +1.10 and holds the whole scene. **Left at +6.39,
declared here rather than silently skipped.**

## Evidence

### 1 · BLOCKER — s77's reference rungs are now on screen. Measured, same instrument as review.

`overrun()` in `build.mjs` emitted the five rungs as `<rect class="fl" … fill-opacity=".2">`.
`.art .fl` is `fill: var(--ink)` and `.has-photo.art-forward .art { opacity: .52 !important }`,
so the effective alpha was ≈0.10 — review measured ΔRGB **6–10** (1.07–1.09:1) against the gap
above each bar. They are now `class="flf"` (`fill: var(--fund)`) with **no** `fill-opacity`,
which is exactly the treatment s75 and s76 already carry, so the device reads as one thing
across all three scenes.

Measured on `snapshots/qa/b6/frame-01-at-59.12s.png` (s77 at +7.14, everything on screen),
bar interior vs the 20px gap immediately above it, mean RGB over the bar's own x-extent:

| | bar mean RGB | gap-above mean RGB | ΔRGB | was (review, attempt 1) |
|---|---|---|---|---|
| rung 1 | (44.4, 68.1, 50.3) | (53.9, 41.3, 46.5) | **40.1** | 6–10 |
| rung 2 | (41.8, 64.1, 47.5) | (49.2, 37.1, 43.1) | **38.8** | 6–10 |
| rung 3 | (39.4, 60.6, 45.6) | (45.9, 33.9, 39.6) | **39.1** | 6–10 |
| rung 4 | (34.8, 55.7, 41.8) | (36.8, 26.5, 32.2) | **40.7** | 6–10 |
| rung 5 | (30.5, 53.4, 40.0) | (30.7, 24.1, 30.0) | **39.4** | 6–10 |
| overrun bar | (60.3, 28.3, 33.7) | (26.0, 22.1, 28.5) | **45.8** | ≈40 |

The brief's target was "comparable to the overrun bar's ≈40". The five rungs land at
**38.8–40.7 against the overrun's 45.8** — inside 7 points of the thing they are compared to,
and 4–6× their attempt-1 value. The overrun still leaves the frame: sampled at **x=1900**,
bar (59.0, 29.6, 33.8) vs gap (23.3, 25.9, 29.6), **ΔRGB 43.6** — still bar at the right edge.

**`no_return_promise` — what was deliberately NOT added.** The rungs got a fill and nothing
else. No 920px ghost track behind them (a full-width rule behind five bars is an axis), no
tick, no numeral, no label, no gridline. The denominator is on screen as rung 5, which *is* the
full 920px track, and both figures in the ratio are printed in this chapter with their rates
($1,963,375 at 4.0% on s76, $5,555,556 at 1.08% here). Nothing in the drawing implies a
projection. Two new asserts in `build.mjs` hold this shape mechanically, on the emitted markup
with comments stripped: exactly `RUNGS.length` `.flf` rects and **no `fill-opacity` at all** in
the overrun (the regression), and exactly one `.flw` plus exactly six `<rect>` total (the
inverse — the overrun may not grow a track or an axis). The pre-existing "no `<text>`, no
tick/axis, no forecast/project/estimate" sweep is unchanged and now runs against the ladder and
the overrun separately, so the ghost-track assert can no longer be satisfied by the *other*
drawing.

**Colour also carries the sentence now**: five green sourced rungs, one red bar that does not
fit — the split review asked for in the fix text.

### 2 · BLOCKER, build half — s71's storyboard note, and the amber re-sampled

**The prose.** The `<!-- -->` note above `#s71` (and its `note:` field in `build.mjs`, which is
its one home) said *"A hardback lying face-down and open, spine up, title not legible."* That
described a file that no longer ships — `container_ladder_CORRECTION_2026-08-09`'s exact
failure. It now describes the object that does ship, read off the pixels at full resolution:
an open book hanging spine-up and seen edge-on, a bright white page block fanning down against
a soft sage bokeh, four neon plastic index flags (orange · cyan · yellow · magenta) marking
pages. The note also now carries WHY it was replaced (the antique volume contradicted
`Wiley, August 2025` in its own foot) so the next reader does not re-litigate it.
**§10's justification is unchanged and still true on the new file** — no title, no spine, no
figure, no seal, no brand, and the only ink in frame is illegible handwriting on two flags,
i.e. satisfied by the pose rather than by a crop, exactly as the note always claimed.

**The amber `4.7%`, re-sampled on the new ground** — `b8/frame-00-at-15.86s.png` (s71 at +2.92,
figure settled), glyph pixels isolated by distance to `--target #f59e0b`, background taken as
the non-glyph, non-white pixels *inside the figure's own bounding box* (x 831–1090, y 487–568),
i.e. the ground the figure actually sits on rather than a frame average:

| against | RGB | contrast |
|---|---|---|
| mean of the ground inside the glyph bbox | (49.9, 40.1, 24.6) | **6.68:1** |
| the brightest 5% of that ground | (95.0, 68.2, 22.5) | **4.17:1** |
| its single brightest pixel | (151, 100, 13) | 2.34:1 |
| mean of the whole local band (700–1220 × 430–620) | (56.9, 48.0, 34.6) | 6.00:1 |

`.huge` is far above the 18.66px large-text threshold, so the AA floor is **3.0**; the worst
5% of the ground under the figure clears it by 1.17 and the mean clears the *normal-text* 4.5
floor by 2.18. The brightest single pixel is an amber-tinted shadow edge, not a field. The risk
the brief named was real — the page block is white — but the scrim's centre pull lands the
figure on the book's shadowed lower third, and `hyperframes check` independently reports
**15/15 text checks pass WCAG AA**. **No token was touched to achieve this**; the figure, its
colour and its size are as shipped.

**s71's tone, re-measured because its photograph changed.** The chapter's tone table in
`build.mjs` is labelled "measured on this build's own composed chain", so a replaced file makes
one cell of it a lie. The chain was re-implemented from the attempt-1 log's description
(cover-fit into `.bg`'s `inset:-8%` box → ken 1.08 → `grayscale(.32) brightness(.62)
contrast(1.05)` → `.field` at `.38` carrying `--f1` → the four `.scrim` layers incl. `--tint` →
BT.601; `.rules`/`.glow`/`.band`/`.grain` not modelled) and **validated against four scenes
whose jpgs are byte-unchanged before being used on s71**:

| scene | shipped | re-implemented | delta |
|---|---|---|---|
| s70 | 36.17 | 36.46 | +0.29 |
| s78 | 40.85 | 40.76 | −0.09 |
| s77 | 34.96 | 35.30 | +0.34 |
| s69 | 43.19 | 43.35 | +0.16 |
| **s71** | 24.79 (old file) | **31.43** | — |

Max deviation 0.34, so the new number is on the same scale as the twelve it sits beside rather
than on a second instrument. **s71: 24.79 → 31.43, rank 5 → rank 7 of 13.** Direction is the
safe one: it moves AWAY from the floor. The floor (`s75` 18.37), its separation to `s79`
(0.98, inside the 1.0 tie band), the payoff and the CTA are all arithmetically untouched by it,
and the generator's INVARIANT block re-runs and passes. **Nothing else was re-measured** — the
other twelve files are byte-identical and re-measuring them would have been a second
instrument's numbers pasted into a settled argument.

### 3 · Max-density snapshot pass — 13 of 13 scenes, eyeballed, per batch

One `-o` per batch, none reused. Every frame below was opened and looked at, not merely
written:

| batch | frames written | frames I opened | scenes |
|---|---|---|---|
| `snapshots/qa/b7` | 6 | **6** | s69 1.85 · s70 9.45 · s72 22.73 · s73 28.25 · s74 34.43 · s75 43.14 |
| `snapshots/qa/b6` | 6 | **6** | s76 49.96 · s77 59.12 · s78 61.74 · s79 67.69 · s80 74.60 · s81 80.36 |
| `snapshots/qa/b8` | 3 | **3** | s71 15.86 · the s76→s77 dissolve midpoint 52.21 · s77 early 53.50 |
| `snapshots/qa/b5` | 7 then wiped mid-read | 3 before the wipe | superseded by b7/b8 |

**15 distinct composed frames opened, covering 13 of 13 scenes.** Every `.stack` sits inside
the safe area, nothing overflows, no text is struck through, the watermark is on every frame
bottom-right and no scene paints into its box, and there is **no rail anywhere**. s77 at +1.5s
(before the figure) is a composed frame, not a bare one: kicker, rate and five green rungs.

### 4 · One thing I saw, measured, and did NOT fix — for review to rule on

**The ladder staggers during the s76→s77 cross-dissolve now that s77's rungs are visible.**
The two scenes plate the same drawing differently, by design: s76 is `.p-d` (`top: 424px`,
viewBox 1920×656, rows at vy 160/230/300/370/440, h44 → **screen y 584/654/724/794/864**), s77
is `.p-a` (full-frame 1:1, rows at y **560/620/680/740/800**, h40). So across the 0.45s
dissolve the five bars sit **−24, −34, −44, −54, −64px** apart, at identical widths and the
same left edge (x=500). At attempt 1 this was invisible because s77's rungs were; it is visible
now (`b8/frame-01-at-52.21s.png`).

I left it, deliberately: the aligned layout does not fit. Matching s76's rows exactly puts
rung 5 at y864–908, and the overrun bar then has to start below 908 — pushing a 64px bar into
y≥920, which crosses the watermark keep-out box (`#root::after`, x1772–1856, y956–1040) that no
scene may paint into. The half-measure (shifting all five rungs down 24px so rung 1 aligns
exactly and the rest land within 40px) narrows the gap between rung 5 and the overrun from 40px
to 16px, which starts to read the red bar as rung 6 of the same series. Both are geometry
changes to the payoff frame, which is more than review asked for and more than I would spend
un-asked. **The plate override to `p-a` is itself load-bearing** — `.p-b` would cut the 2,603px
bar at vx=800 (gotcha 8), and `p-d`'s 656px viewBox has no room below the rungs for it. Numbers
are here so this is a ruling, not a discovery.

### 5 · What I confirmed UNCHANGED

Every item the brief listed as settled, checked in the regenerated file rather than assumed:

- **No re-timing, anywhere.** `build.mjs` recomputes all four homes from `timing.json` and its
  own gap asserts pass. Build output: offset **441.900** + root **85.973** = **527.873**, which
  is timing.json's own total. Every `data-start` / `data-duration` / `data-framings` is
  identical to attempt 1 — s69 0/6.919/6.469 … s77 51.984/8.355/7.905 … s81 78.407/7.566/7.566.
  The s77 anchor stays at **+5.59** and the countUp at **1.10s**, settling 1.215s before the
  dissolve.
- **s77's figure, its geometry and its timing — untouched.** The rung fill is the device's
  readability; the figure's 4.86:1 and its rank-7 ground were settled on the encode and nothing
  here moves them. `--warn`, `.huge`, `p-a`, the `vrule`, the `band` and the `span` to 2.8296
  are all as shipped.
- **The floor argument, untouched.** `FLOOR = "s75"` and the separation limb still hold on the
  build's chain; review's encode measurement ({s79 38.872, s75 38.928} tied at 0.057, s76 out
  at 1.775) is a different instrument and is review's to own. **s75 was not brightened** — that
  is the forbidden trade under `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`.
- **s70's legible governance prose — kept**, exactly as review settled it. Its `note:` field is
  byte-unchanged, including the carried-forward paragraph explaining the call. The new s71 is
  the frame beside it and fin-assets' four separation axes hold on the composed frames: s70 is
  a warm horizontal flat macro dense with body prose, s71 a cool vertical edge-on block with
  none.
- **s75 stays a derived HOLD crop of s76** (`crop=1280:720:20:250`), `plateKen` 1.16→1.08→1.00,
  one continuous pull-back. Rungs 1–3 are still emitted on s76 at scale 1 with no `span` call.
- **s81 is the cut's ONE terminal CTA**; no rail, no chapter title, no scene counter, no slide
  number on any of the 15 frames opened.
- **§10's three-beat crate rhyme was NOT restored.** The note stands as s75/s76 only — s77 is a
  steel container and ch5's s61 has left the crate family. No text was added claiming otherwise.

### 5b · `npm run check` — PASS

```
0 error(s), 0 warning(s), 9 info(s)
Motion    0 errors, 0 warnings
Contrast  15/15 text checks pass WCAG AA
◇ Check passed
```

The nine infos are all `container_overflow #sNN-bg inside #sNN` — the `.bg`'s `inset: -8%` ken
window by construction, on nine of thirteen scenes. Not a defect and not silenced:
`known_benign` is `[]` and stays `[]`, and **no design token was edited to satisfy any check.**

## Changed

Two files, both in `studio/videos/passive-income-number-en-ch6/`:

1. **`build.mjs`** — five edits, no timing among them:
   - `overrun()`: the five reference rects `class="fl" … fill-opacity=".2"` → `class="flf"`,
     no fill-opacity. Its header comment now records why (the measured ΔRGB 6–10) and what was
     deliberately not added with them (`no_return_promise`).
   - The ladder assert block: split into ladder-only and overrun-only, kept the existing
     numeral/tick/axis/forecast sweep over both, added two asserts — five solid `.flf` and no
     `fill-opacity` in the overrun, and exactly six rects (five rungs + one bar).
   - `s71.note` — the object description, replaced (prose only).
   - `s77.note` — one appended paragraph recording that review resolved the payoff-legibility
     clause on the encode and that only the rungs changed.
   - `TONE.s71` 24.79 → 31.43 and its ordering in the prose table above it, with the validation
     deltas recorded in the comment.
2. **`index.html`** — regenerated by `node build.mjs`. No hand edits survive in it.
3. `snapshots/qa/{b5,b6,b7,b8}` — QA frames, throwaway.

Nothing under `assets-ch6/` was touched — all thirteen jpgs, `manifest.json`, `CREDITS.txt` and
the `.src` sidecars are byte-unchanged from fin-assets attempt 2. `assets/audio.json` is
regenerated by the same run and is identical (18 cues). No icon added to `assets/icons/`.
`studio/videos/passive-income-number-en-ch5/` never opened.

## Owed

1. **fin-review, to rule on §4:** the ladder's −24…−64px stagger across the s76→s77 dissolve,
   now visible. If it reads as a defect the fix is one constant (`OV.y0`), but it trades against
   the rung-5-to-overrun gap and I would not spend it unasked.
2. **fin-review, to re-measure on the encode, not to take from here:** s71's ground moved
   24.79 → 31.43 on the BUILD's chain; its encode YAVG was 45.225 at attempt 1 and will rise.
   It cannot reach the floor and cannot pull the payoff or CTA down, but the chapter's median
   (45.225 was the median) shifts, which is the number the payoff-legibility clause is graded
   against. **Nine-for-nine on `predictions_missed_a_sixth_time` if this one misses too — treat
   it as a direction, not a value.**
3. **The orchestrator, not this stage:** `tools/render_chapter.py` for the draft encode. The
   rung ΔRGB above is measured on composed browser frames; the encode adds h.264 chroma
   subsampling, which touches saturated green on dark ground more than it touches luma. The
   margin (38.8 vs the 45.8 reference) is wide enough that this is a note, not a doubt.
4. **Nothing owed to fin-assets.** Both halves of blocker 2 are closed.
