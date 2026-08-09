# fin-build · passive-income-number · hi · ch3 · attempt 2

Scope: the single should-fix from `editor-hi-ch3-2.md` — s22's stale inline window.
Two edits, both in `build.mjs`. No other scene touched.

## Ran

- `node build.mjs` (twice: once to reproduce the throw, once to emit)
- `npm run check` → `hyperframes check` 0.7.66
- `npx hyperframes snapshot --at 0.20,1.20,3.10,5.30 --no-end -o snapshots/qa-fix/b2`
  (first invocation into `snapshots/qa-fix/b1` was discarded — repeated `--at` flags
  do not stack, the CLI wants one comma-separated list, so b1 held only 2 frames)
- a node geometry computation of the `.bg` cover box, before and after

## Failed

Nothing outstanding. One thing failed on the way in and is worth recording, because
it is the reason the defect existed:

`node build.mjs` **already threw** on the current tree, before any edit:

```
Error: s22: s22.jpg is 1880,1058 but win was cut against 1880,740
    at build.mjs:474
```

So the emitted `index.html` was never a product of the current asset. `fin-assets`
replaced `assets-ch3/final/s22.jpg` on attempt 2; `build.mjs` was not re-run
afterwards, so the stale `background-size`/`background-position` survived in the
emitted HTML while the generator that produced it could no longer run at all. The
guard at `build.mjs:471-475` (`jpegSize` read from the JPEG's own SOF marker, never
`identify`) is exactly the assert designed to catch a re-sourced file under a
declared window, and it did — it was simply never invoked. Root cause is a missing
rebuild, not a missing check.

## Evidence

Geometry, computed rather than asserted. `.bg` is `inset:-8%`, so its box is
1920×1.16 by 1080×1.16 = **2227.2 × 1252.8**; `ken` sweeps scale 1.16→1.00 with
xPercent +2.5→−2.5. Source is now **1880×1058** (read from the SOF marker, not from
the `.src` prose).

| | rendered image | top uncovered band, box px | that band's edge vs. frame top @ scale 1.00 | zoom vs. plain cover |
|---|---|---|---|---|
| stale inline window (`2781.37px auto` @ `38.74px 79.00px`) | 2781.4 × 1565.3 | **79.0** | **−7.4 px** (i.e. 7.4px of clearance, nothing more) | **1.249×** |
| plain `cover` (shipped) | 2227.2 × 1253.4 | **0** | **−86.4 px** | 1.000× |

Both editor numbers reproduce exactly: the 1.249× tighter crop and the 7.4px. The
band is now **structurally absent**, not merely pushed further off-screen — under
`cover` on a 16:9 source in a 16:9 box the rendered image is the box, so there is no
uncovered region at any point in the sweep. Remaining slack: **97.9px horizontally**
after the ±55.68px xPercent drift, **86.4px vertically**.

`hyperframes check` corroborates from the other side — at t=3.4s `#s22-bg` overflows
its clip on all four sides (left 234.63 / right 207.75 / **top 124.41** / bottom
124.41). A positive top overflow is the band's negation measured by the runtime.

Check result, full project:

```
Layout    0 error(s), 0 warning(s), 13 info(s)
Motion    0 errors, 0 warnings
Contrast  17/17 text checks pass WCAG AA
◇  Check passed
```

The 13 infos are unchanged in kind and count from the passing attempt-1 state: 9 ×
`container_overflow` on the nine `.bg` elements (the `inset:-8%` ken box, by design,
one per scene), plus s28's `#s28-plate` overflow / `panel_out_of_canvas` and the two
`text_occluded` reports on its drawn labels under `.scrim` — all pre-existing, all on
the one art scene, none introduced here. No token was touched.

Frames reviewed: **4 of 4** in `snapshots/qa-fix/b2` (0.2s, 1.2s, 3.1s, 5.3s), read
individually at 0.2s and 5.3s and the pair 1.2/3.1 off the contact sheet.
0.2s is the opening frame the sound-off gate has standing over: full-bleed stacked
terracotta gullaks, round vessels with countable black coin slits and vent holes,
edge to edge, no `--bg` anywhere. 5.3s is the ken's loosest scale — the frame the
band would have appeared in — fully covered, stack inside the safe area, watermark on
`#root::after` bottom-right. `₹20,00,000` is settled by 3.1s (countUp 1.90 → 3.10) in
`en-IN` grouping.

Emitted markup:

```html
<div class="bg" id="s22-bg" style="background-image:url(assets-ch3/final/s22.jpg)"></div>
```

`grep -c background-size index.html` → **0**. Timing is byte-identical to attempt 1:
root 61.143s, offset 124.007s, 9 scenes, s22 `data-start="0" data-duration="5.874"`
`data-framings="5.424"` track 2.

## Changed

`studio/videos/passive-income-number-hi-ch3/build.mjs`

1. **SCENES row `3.1`** — dropped `src: [1880, 740], win: [40, 5, 1337.7778, 735]`.
   `.bg` now takes plain `cover`. This is the fix at the generator, so a rebuild
   cannot reintroduce it.
2. **SCENES row `3.1` `note:`** — rewritten. It described the deleted carved sheesham
   money box, its brass hasp and the window fitted to keep that hasp in the sweep
   union. It now describes the stacked terracotta gullaks that ship, states the file
   is 16:9 so the centre-crop pathology that forced the window cannot arise, records
   why the previous file was killed, and records the stale window's two measured
   consequences (1.249× / 7.4px) as the reason it was dropped. This note is emitted
   verbatim as the scene comment, so it is the same edit as "fix index.html line ~99".
   Kept intact: the container-ladder ruling, the `s16` prohibition, NO FOOT, the
   neutral ground and the `+1.90` floor derivation.
3. **`THE DECLARED WINDOW (s22)` comment block, ~line 436** — its trailing ⚠ cited
   the superseded file's 740px height and "clears it by 7.4px", now false in both
   numbers. Replaced with a note that no scene in ch3 declares a `win` any more, why,
   and why the mechanism stays: its `jpegSize` assert is what caught this.

`studio/videos/passive-income-number-hi-ch3/index.html` — regenerated, not hand-edited.
Diff against attempt 1 is the s22 comment, the s22 `.bg` style attribute, and nothing
else. `assets/audio.json` re-emitted identically (12 cues, `bed-resolve`).

Nothing written outside the cut directory except this log. No asset byte changed;
s22.jpg's md5, manifest row and CREDITS entry all stand.

## Owed

- Nothing on this fix. The three regressions the editor named are untouched by it and
  cannot be re-verified from a composition — s22's containers read at +0.40/+4.50/+5.10,
  s29's cable tangle holding its red `stmt` across the ken, and s27's payoff separation
  are encode-level findings and belong to the next `fin-render` pass.
- `fin-render` must re-render ch3; the current `renders/` mp4 predates this change and
  still carries the 1.249× crop.
- Note for whoever ships the next chapter: the `win` mechanism's guard fires at build
  time only. A `fin-assets` swap that lands after the last `node build.mjs` leaves a
  stale emitted `index.html` and a generator that throws — the throw is the signal, so
  a rebuild after every asset swap is the cheap way to surface it.
