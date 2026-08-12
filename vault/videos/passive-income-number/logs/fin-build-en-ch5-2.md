---
summary: en ch5 fix pass after fin-review REWORK. ONE of the two items is done and one is REFUSED with geometry. Item 2 (s64, the chapter's thesis line) is CENTRED — the chip row now sits at frame centre 959.5 against 960, and the exemption in the generator's own art-off⇒centred guard that produced the defect is DELETED, not narrowed. Item 1 (s61, `ROUGHLY 4 TIMES`) IS NOT FIXED AND NOTHING ABOUT s61 WAS TOUCHED: the reviewer's first-choice lever does not exist on this file — the source is 1880x1253 into a 16:9 `.bg`, so `cover` is width-limited and `background-position` has exactly 0px of horizontal authority — and no derived crop reads 4:1 either, because the photograph has no isolated crate at all: it is ONE contiguous stepped mass from x 61 to x 1200 whose low right end physically abuts the stack's base crate. Three 16:9 crops were cut and reviewed graded; the tightest window that could hold four faces plus one separated crate is ~420 source px = 4.6x upscale, and the geometry it would need is not in the frame. Per the brief this stage STOPS rather than ship a near-miss and routes s61 to fin-assets as a re-fetch. `npm run check` PASS, 0 errors, 14/14 WCAG AA, identical finding profile to attempt 1. NO TIMING MOVED — all 16 `data-start`/`data-duration`/`data-framings`, both swap points (s56 2.500, s67 4.800) and the root 106.084s are byte-identical to the reviewed draft. The three settled verdicts (s59 PEAK 2, the s54 floor, comma clearance) were not touched by anything here.
updated: 2026-08-12
stage: fin-build, cut en, chapter 5, attempt 2 (fix pass)
source: vault/videos/passive-income-number/logs/review-en-ch5-1.md findings #1, #2, #4; storyboard-en.md §7 row 64 and §8; tools/packs/fin-build.md box item 7; measurements taken on assets-ch5/final/s61.jpg (1880x1253) and on 4 rendered frames in snapshots/qa/b4
---

# fin-build — passive-income-number en ch5, attempt 2 (fix pass)

Two items were assigned. **One is done, one is refused with its geometry.** Item 3
(s57's tank callback) is held in the pre-assembly batch by the orchestrator and was
not looked at.

| item | scene | verdict |
|---|---|---|
| 1 · P1 blocker | s61 (5.9) | **NOT FIXED — the source cannot be cropped to read ~4:1.** Nothing about s61 was changed. Routed to fin-assets |
| 2 · should-fix | s64 (5.12) | **DONE — `centred`**, plus the generator guard that allowed the defect is deleted |
| 3 · should-fix | s57 (5.5) | not mine this pass |

---

## Ran

1. Read `vault/CLAUDE.md`, `review-en-ch5-1.md` in full, `tools/format/fin-build.json`,
   `tools/packs/fin-build.md` (box item 7 and the two body sections), and my own
   attempt-1 log. **No `OPENED-BODY:` line is owed** — no design note's body was opened.
2. Read storyboard-en §7 row 64 (`ctr N`, confirmed) and §8's refusal table (the two
   rows that matter: 5.9 "the photograph is four crates against one" and 5.12 "the
   photograph is three converging lanes").
3. **Measured s61.jpg's geometry** — source dimensions, crate-mass extents, the `.bg`
   cover fit, the horizontal slack available to `background-position`, and the visible
   source-x window at both ends of the ken.
4. **Cut three 16:9 derived crops with ffmpeg-equivalent geometry, graded them with the
   locked grade (`grayscale .32 · brightness .62 · contrast 1.05`) and looked at every
   one at full size.** None shipped.
5. Edited `build.mjs` (three comment blocks, one `ctr` flag, one guard), regenerated
   `index.html` + `assets/audio.json`.
6. `npm run check` → PASS. Four snapshot frames in a FRESH batch dir `snapshots/qa/b4`,
   all four opened individually at full resolution; the amber chip geometry measured off
   the PNG with numpy.

---

## Failed

**Item 1 is refused, not deferred, and the refusal is the deliverable.** It is written up
in Evidence §1 with the numbers. Nothing else failed.

⚠ One correction against my own attempt-1 work, which is where this defect came from and
is worth stating plainly: attempt 1 wrote a guard reading *"art-off ⇒ centred **unless**
the scene carries a declared cascade"* and cited §7's `ctr N` as its authority. That
exemption is wrong — see Evidence §2 — and I built it, asserted it, and printed it in the
log as if it were a rule. It is deleted.

---

## Evidence

### 1 · s61 — WHY NO CROP OF THIS FILE READS 4:1

**The premise, restated from the picture rather than from §8.** `assets-ch5/final/s61.jpg`
is **1880×1253** (aspect 1.5004). The crates are **one contiguous stepped mass**, not two
groups:

| feature | source px |
|---|---|
| crate wall, 5 columns × 4 rows ≈ 14 visible faces | x **61 – 989**, y **570 – 1155** |
| the stack's base crate (pale, open-topped, brightest object in frame) | x **912 – 1200**, y 1015 – 1145 |
| the "low crate at the right end" | x **1050 – 1165**, y 935 – 1020 |
| floor line under the crates | y ≈ 1155 |
| wooden roof post (the only other object) | x **1469 – 1616**, full height |

**There is no background gap anywhere between "the one" and "the many", at any x.** The
low right-hand crate sits ON the base crate, and the base crate runs back under the wall.
The far left end (checked separately at full size) is a flush 4-high wall with no isolated
crate either. So "four against one" is not a crop of this photograph — it is a different
photograph.

**Limb A — the reviewer's first-choice lever, `background-position`, has ZERO horizontal
authority on this file.** `.bg` is `inset:-8%`, i.e. **2227×1253** on a 1920×1080 stage,
`background-size:cover`. Cover scale for a 1880×1253 source is
`max(2227/1880, 1253/1253) = 1.1846` → the image renders at **2227×1484**. Horizontal fit
is **exact (2227 = 2227) ⇒ 0px of slack**; the only slack is 231 rendered rows = **195
source rows, vertical**. This is the same width-limited geometry my attempt-1 log recorded
for s54's bgpos sweep, and it has the same consequence: **`background-position` cannot
exclude a single crate column.**

**Limb B — and the ken cannot either.** `ken()` is `scale 1.16 → 1.00` with
`xPercent +2.5 → −2.5` (±55.7px on a 2227px element). Inverting the transform against the
1920×1080 viewport, the **visible source-x window is**:

| moment | visible source x | visible source y |
|---|---|---|
| ken start (scale 1.16, xPercent +2.5) | **282 – 1679** | 233 – 1018 |
| ken end (scale 1.00, xPercent −2.5) | **83 – 1704** | 98 – 1155 |

The 14-crate wall (x 61–989) is **inside both windows for every frame of the scene**.
That is exactly what the reviewer saw on the encode.

**Limb C — three derived 16:9 crops, cut and reviewed graded. All rejected.**
(A derived crop is within my remit — it is how `s56b`/`s67b` exist — so this was tried
properly, not waved off.)

| crop | source rect | size | upscale to 1920 | why rejected |
|---|---|---|---|---|
| **C1** | (830,570)–(1855,1147) | 1025×577 | 1.56× | the crates jam against the LEFT frame edge with the count running off it; ~60% of frame is bare wall plus the dark roof post; the "one" is the stack's own base crate, touching it |
| **C3** | (700,560)–(1780,1168) | 1080×608 | 1.48× | same failure one column wider — the stack is unbounded at the left edge, so there is no number in the frame at all |
| **C4** | (600,700)–(1466,1187) | 866×487 | **1.85×** | best composition of the three and still reads "a stack of crates, and more crates": the left edge cuts through the wall, and the pale front crate that would have to be "the one" is physically joined to the stack. Visible softness in the wood grain at 1.85× before the ken's further 1.16× |

A crop tight enough to hold **exactly four faces plus one separated crate** would be
≈ **420 source px wide → 4.6× upscale at ken 1.16** — unshippable on resolution alone,
and the separation it would need is not in the frame at any zoom.

**Conclusion.** Per the brief: *"If the source genuinely cannot be cropped to read ~4:1 —
say so and STOP rather than shipping a near-miss."* It cannot. **s61 is byte-identical to
the reviewed draft** — no crop, no `background-position`, no ken change, no drawn layer
(review forbade that by name and I agree: a drawn 4:1 bar over a 14-crate wall is the
composition arguing with itself), no timing change. The only thing that changed on s61 is
its **HTML comment**, which now records the false premise instead of repeating it, so the
next reader of this file is not told the photograph is four against one.

**What a re-fetch needs, stated so fin-assets does not have to re-derive it:** two
physically separated groups on one ground plane — a countable few (four) and a single —
with visible background between them, shot wide enough that both survive a 16:9 cover crop
whose visible window is only the central ~86% of the width and ~74% at ken start. §10 also
needs it to rhyme forward: the ch6 recap at 6.7/6.8 is a line of five increasing and then
one far larger, so the crate object itself should be kept.

### 2 · s64 — CENTRED, and the guard that blocked it is deleted

**§7's `ctr` column says `N` for row 64, and box item 7 overrides it.** Both halves of the
reason are recorded in the scene's own comment in `index.html`:

1. **The cascade is not "something real on the other side."** It lives in `.stack` — the
   TYPE column. The side box item 7 is talking about is the **plate's**, and `art: off`
   empties that by construction. A stack cannot occupy the other side of itself. That was
   attempt 1's reasoning error, and it is the only reason s64 was not centred.
2. **§7 wrote `N` against a photograph that does not ship.** The row assumes three parallel
   painted lanes converging — something for type to sit beside. `s64.jpg` is a top-down of
   5–6 lanes carrying a left-turn arrow, two straights and two merges (fin-assets declared
   this; review confirmed it). So even on §7's own logic the `N` has nothing to hold.

**The plate check the brief asked for — nothing on s64 lives in the plate.** `s64`'s
`.stack` holds exactly a `.kicker` and one `.row` of three `.chip`s. The emitted document
contains **0 `.plate`, 0 `.vrule`, 0 `.brule`, 0 `.crule`, 0 `<svg>`** — all sixteen scenes
are `art-off` — so `.scene.centred .plate{display:none}` hides nothing that exists. The
ch4 4.7 trap (a centred scene erasing its own plate content) cannot fire here.

**Measured on the rendered frames**, `snapshots/qa/b4`:

| t | what | measurement |
|---|---|---|
| 74.30 | chip 1 only | chip 1 ink at **x 694–838** — identical x to its position in the settled frame |
| 75.20 | chips 1–2 | no horizontal shift of chip 1 |
| **76.90** | last cue + 0.09, settled | amber chip-row ink **x 694 – 1225, y 527 – 611**; row centre **959.5** against frame centre 960 (**0.5px**), row width 531px inside the 1500px centred cap |
| 79.60 | tail, 0.37s before the cross-dissolve | unchanged, settled |

**The chips do not re-centre as they arrive**, which was the one real risk in moving a
cascade into a centred stack: `pop()` animates `opacity` + `scale` only, both of which are
paint, so all three chips hold their layout box from t=0 and each simply appears in place.
Verified in the picture at 74.30 vs 76.90, not inferred from the helper.

The 0.5px centring is `.scene.centred .stack{padding-left:0}` doing its job — the
system-level fix ported into `chapter-design.css` on 2026-08-08 after two chapters found it
independently. It needed no local patch here.

**Nothing else about s64 moved**: the three cue times stay at the measured +1.18 / +2.06 /
+3.36, the ken stays `i`, the ground stays `#2a2113`, the role stays `--target`, the three
`chip` cues stay on the `counted` list.

### 3 · The root-cause edit — the exemption is deleted, not narrowed

```
-  if (s.art === "off" && !s.ctr && !s.chips)
+  if (s.art === "off" && !s.ctr)
```

Box item 7 has no exception, so the generator now has none. This matters beyond s64:
**ch6 copies this file** and ch6 has drawn layers, so a live exemption saying "a cascade
counts as the other side" would have travelled. The converse guard
(`art !== off && ctr ⇒ throw`, i.e. `.centred` would hide the plate the drawn layer needs)
is untouched and still live for exactly that reason.

### 4 · Nothing the reviewer settled was disturbed

| settled verdict | state after this pass |
|---|---|
| **s59 PEAK 2 PASSED** (ink y535–634 / x677–1244, 4.97:1, count-up completing 1.23s early) | s59 markup, cues and photograph **byte-identical**. My attempt-1 prediction of a three-limb failure is retired; the encode measured it and it did not reproduce |
| **s54 is the floor, discharge UPHELD** (23.52 vs s67 25.50) | s54 untouched. No knob spent, no bgpos, no re-order |
| **Comma clearance PASSES** (s68 27px, s63 26px) | both untouched; no `.huge`, no foot, no size changed anywhere in the chapter |
| **The two swap points** (s56 +2.500 re-cut, s67 +4.800 kept) | `data-framings="2.5,5.013"` and `"4.8,3.706"` — unchanged |
| **s55's `.mega`** at 1489.7px | untouched, still the only `.mega`, still `.v-nowrap`-pinned |
| **s67's measure bar** at 920px / scaleX 1.0000 | untouched |

**No timing moved.** All sixteen `data-start` / `data-duration` / `data-framings` and the
root `106.084` re-emit identically to the reviewed draft (verified by re-reading them out
of the regenerated `index.html` against attempt 1's table, row by row: s53 0/7.885/7.435 …
s68 98.988/7.096/7.096, s68 correctly carrying no transition tail). `assets/audio.json`
re-derives to the same **29 cues** on `bed-tension`.

### 5 · Checks

| check | result |
|---|---|
| `npm run check` | **PASS** — 0 errors, 4 warnings, 2 infos, **14/14 text checks WCAG AA** |
| Lint | 0 errors / 4 warnings — the same four as attempt 1 (`composition_file_too_large`, 2 × `timeline_track_too_dense`, `composition_heavy_overlay_count_high` at 32) |
| Runtime | 0 / 0 |
| Layout | 0 errors, 0 warnings, **9 `container_overflow` infos** — all nine are `.bg` reporting its `inset:-8%` ken window, as on every locked chapter of this run |
| Motion | 0 / 0 |
| scene / track structure | 16 sections, **16 `centred`** (was 15), alternating tracks 1/2 intact |

**No design token was edited** and `format.json known_benign` stays empty. The finding
profile is byte-for-byte the same as attempt 1 — the fix added no new finding and
suppressed none.

### 6 · Frames looked at — ONE batch, ONE fresh directory, all four opened

`snapshots/qa/b4` (never reused; `snapshot` wipes its `-o` dir). **4 frames captured, 4
opened individually at full resolution** — 74.30 · 75.20 · 76.90 · 79.60, all on s64,
because s64 is the only scene whose markup changed. The CLI's `Navigation timeout` was
wrapped in a retry loop and did not fire.

Attempt 1's 19 frames in `b1`/`b2`/`b3` stand for the other fifteen scenes, which are
byte-identical.

---

## Changed

- `studio/videos/passive-income-number-en-ch5/build.mjs` — s64 `ctr: false → true`; the
  `&& !s.chips` exemption removed from the art-off⇒centred guard; three comment blocks
  rewritten (the `ctr` field doc, the archetype-layer header, s64's note) and s61's note
  amended to record the open blocker instead of repeating the false premise.
- `…/index.html` — regenerated. Diff against the reviewed draft: **one class token**
  (`centred` on `#s64`) plus comment text. No attribute, no cue, no id, no asset path.
- `…/assets/audio.json` — regenerated, identical derivation (29 cues, `bed-tension`).
- `…/snapshots/qa/b4/` — 4 new QA frames.
- This log.

**Nothing else was touched.** No image was fetched, cropped, replaced or dropped — all 18
promoted jpgs including `s61.jpg` are byte-unchanged. `manifest.json`, `CREDITS.txt`,
`IMAGES-ch5.jpg`, `cues-tables.json`, `run.json` and every other chapter project
(including `-en-ch6`, which another agent is building) were not opened for writing.
`blockframe.css` / `chapter-design.css` are still the scaffold symlinks, unmodified; no
motion helper was redefined inline; no CDN or network reference exists
(`grep -cE 'https?://' index.html` = 0). Nothing was written to `tools/`, `.claude/`,
`assets/icons/` or `assets/lottie/`.

---

## Owed

1. ⚠ **P1, TERMINAL-GATE, NOT MINE — s61 needs a re-fetch and only fin-assets can make
   that call.** The full geometry is in Evidence §1; the short version for the fetch
   query is: **two physically separated groups on one ground plane, four countable objects
   against one, with visible background between them**, framed so both survive a 16:9
   cover crop that shows only the central ~74–86% of the width. Keep the crate as the
   object — §10's three-beat rhyme (s61 → s75/s76 → s77) depends on it and the ch6 recap
   is being built right now against a s61 that does not establish the count.
2. **A storyboard correction pass on §8 is now owed on TWO rows, not one.** §8 declines
   drawn art at 5.9 and at 5.12 on the stated ground that the photograph already carries
   the content, and neither photograph does. 5.12 is discharged by centring; 5.9 is not.
   This is the fourth stale storyboard row this run has routed around, after
   `container_ladder`, the hi ladder and §10's derived-crop table.
3. **`chapters.en.5` should record: attempt 2 built, s64 fixed, s61 open at fin-assets.**
   The `s58→s59` SHOVE is still inside this project; the `s52→s53` joint still belongs to
   the assembly.
4. ⚠ **The re-render is going to happen anyway once s61 lands** — so if the orchestrator
   is still holding s57's tank layer in the `owed.en_ch2_s10_tank_layer` pre-assembly
   batch, **that batch and the s61 re-fetch should land in the same ch5 render**, not two.
   Both are ch5 picture changes with no timing consequence.
5. Attempt 1's items 4, 5, 6, 8, 9, 10 and 11 (the cue-rung defect at s60/s67, the `.mega`
   over the frieze, s65's cropped part-month, s66→s67 adjacency, the overlay count of 32,
   the stale §10 crop row, and comma clearance from the encode) are **unchanged and still
   open** — none of them was touched by this pass, and review has now settled comma
   clearance (PASS) and the `.mega` (no finding).
