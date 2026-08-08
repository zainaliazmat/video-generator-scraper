---
summary: en ch3 attempt 2 — rebuilt against the two replaced photographs, drafted and sheeted for the first time. 16 scenes / 96.601s / 2899 frames, `hyperframes check` 0 errors + 14/14 AA, check_vo_frame PASS, cues.py exit 0, `check build --chapter 3` PASS. The invariant breach is CLOSED ON THE ENCODE, not on a prediction: s31 ($656,650) moves median 7.1→70.7 at source and measures 35.0 (#8 of 16) with p10 24.0 (#4) on the mp4; s27 measures 42.0 (#3) / 31.0 (#2). The payoff s34 re-scores PASS on all four clauses from the encode (median 45.0 #2, p10 36.0 #1, step-in +17.0). One measured recommendation taken: `bgpos: center top` on s27, verified by eye at composed size. ⚠ THE FLOOR MOVED, IT DID NOT GO: it is s37 on the encode too (median 21.0, LAST; p10 15.0), carrying line 3.14 — reported, not pre-empted.
updated: 2026-08-09
source: fin-build attempt 2, chapter 3, en cut — vault/CLAUDE.md + tools/format.json + knowledge/design-finance-blockframe.md + knowledge/design-chapter-archetypes.md + run.json rulings_binding_on_both_cuts + chapters.en.3 + logs/fin-assets-en-ch3-3.md + logs/fin-build-en-ch3-1.md; measurements from assets-ch3/final/*.jpg and renders/DRAFT-ch3.mp4.
stage: fin-build, cut en, chapter 3, attempt 2
---

# fin-build — passive-income-number / en / chapter 3 / attempt 2

**Project:** `studio/videos/passive-income-number-en-ch3/`
**Artefacts:** `build.mjs` · `index.html` · `assets/audio.json` · `snapshots/qa/b6`
· `renders/DRAFT-ch3.mp4` · `renders/SHEET-ch3.jpg`
**16 scenes · 96.601s · 2899 frames · s24–s39 · lines 3.1–3.16.**

| check | result |
|---|---|
| `npm run check` (`hyperframes check`) | **PASS** — 0 errors, 4 warnings, 13 infos; **14/14 WCAG AA** |
| `tools/check_vo_frame.py … --chapter 3` | **PASS** — 16 scenes cross-checked |
| `tools/audio/cues.py <project>` | **exit 0** — 24 cues, min gap **1.100s**, bed `bed-tension` |
| `tools/pipeline_check.py check build … --chapter 3` | **PASS** |
| frame count | `ffprobe -count_frames` → **2899**, r_frame_rate 30/1 = `ceil(96.601 × 30)` ✓ |
| file order | `build.mjs` 00:48:05 < `index.html` 00:48:11 < `DRAFT-ch3.mp4` 00:53:30 < `SHEET-ch3.jpg` 00:53:53; both photographs 08-08 18:44/18:48, older than all four ✓ |

`known_benign` is still empty and stays empty. The four warnings and thirteen
infos are attempt 1's class exactly (`composition_file_too_large`, two
`timeline_track_too_dense`, `composition_heavy_overlay_count_high`, per-scene
`container_overflow` on every `inset:-8%` `.bg`, `#s30-plate` 60px off-canvas =
the `.p-b` constant `1120 + 860 = 1980`). No design token was touched.

---

## 1. What actually changed in this attempt

Three edits to `build.mjs`, then a regenerate. **No timing, no copy, no cue, no
archetype, no ground, no ken, no measure value moved.**

1. `s27` gains `bgpos: "center top"` (§2 below).
2. `s27` and `s31`'s scene notes rewritten to describe the photographs that are
   now on disk, with this stage's own measurements.
3. The header's ruling-2 block rewritten: the s31 escalation is closed and the
   relocated floor is recorded in its place.

Everything else in the file is byte-identical to attempt 1. The regenerate was
verified deterministic: after the assert re-proof below, `node build.mjs`
reproduced `index.html` at md5 `9b2c49ac…` and `assets/audio.json` at
`ac4c6a32…`, the same hashes as the shipped pair.

## 2. THE TWO PHOTOGRAPHS, RE-MEASURED HERE — not taken on trust

fin-assets validated its method against my attempt-1 table; I did the reverse and
ran **my own chain over the live files**, including the superseded pair still in
`assets-ch3/superseded-invariant-r1/`. Chain: cover-crop into the `inset:-8%`
box with the scene's `background-position`, take the central 1920×1080 the viewer
actually sees, then `brightness(.62) contrast(1.05)` (`grayscale(.32)` is
chroma-only and does not move a neutral), Rec.601 luma percentiles.

| file | median | p10 | p90−p50 |
|---|---|---|---|
| superseded s27 | 25.4 | 0.0 | 50.9 |
| **live s27** (`center`) | **97.0** | **82.2** | 26.1 |
| **live s27** (`center top`, shipped) | **97.9** | **82.9** | **38.1** |
| live s27 (`center bottom`) | 95.9 | 80.8 | 12.4 |
| superseded s31 | 6.9 | 0.0 | 95.6 |
| **live s31** (`center`, shipped) | **70.7** | **43.2** | 59.9 |
| live s31 (`center top`) | 71.9 | 44.5 | 61.8 |

Independent agreement with fin-assets is **≤0.2 points on every cell**, including
both outgoing files. Two instruments, two stages, same numbers.

**The white-dominant rule correction is confirmed arithmetically and visually.**
255 through this grade lands at 159.6, not charcoal; both replacements measured
*brighter* than everything they replaced. The live risk on a white subject is
flatness, and that is what the spread column is for — which is exactly why
`center bottom` was rejected on s27 despite costing only 1.1 of median: it
collapses the spread to 12.4, the even-and-empty direction the CEO's sharpening
names.

### The `bgpos: center top` recommendation on s27 — TAKEN

Not taken on the numbers alone. I rendered both crops graded at composed size and
looked at them: on `center` the top of the handle recess is **cut by the frame
edge**; on `center top` the whole object sits in frame with clearance, upper-right,
leaving frame centre to the `.centred` stack. It costs nothing (+0.9 median, +0.7
p10) and buys +12.0 of spread on the chapter's emptiest photograph. Shipped.

**Rejected, with the reason:** `center top` on s31. It buys +1.2 median / +1.3
p10 — inside my own chain's agreement noise with fin-assets, and not worth moving
a composed frame that already clears every clause. No knob is better than a knob
that only moves a decimal.

## 3. THE ENCODE TABLE — all sixteen scenes, measured off DRAFT-ch3.mp4

ch2's render method, reused so the numbers are comparable: decode at full
1920×1080 on a 10 fps grid, take each scene's **settled span** (its last cue
settled → the cross-dissolve out), pool the frames, whole-frame Rec.601 luma
percentiles. Whole-frame means scrim, tint, vignette and type are *in* the
number, which is why the band is compressed against the source-side table — the
two scales are not interchangeable, only their ORDER is.

| scene | settled span (s) | frames | **p10** | **median** | p90 | p90−p50 | median step in | source-side prediction |
|---|---|---|---|---|---|---|---|---|
| s24 | 1.80–2.89 | 10 | 16.0 | **23.0** | 33.0 | 10.0 | — | 36.7 (15th) |
| s25 | 5.94–9.02 | 30 | 26.0 | **38.0** | 54.0 | 16.0 | +15.0 | 93.8 (6th) |
| s26 | 16.18–16.92 | 7 | 19.0 | **34.0** | 48.0 | 14.0 | −4.0 | 92.6 (7th) |
| **s27** | 21.79–23.52 | 17 | **31.0** | **42.0** | 49.0 | 7.0 | **+8.0** | 97.9 (4th) |
| s28 | 25.32–29.89 | 45 | 24.0 | **40.0** | 51.0 | 11.0 | −2.0 | 95.8 (5th) |
| s29 | 32.39–36.30 | 39 | 19.0 | **33.0** | 57.0 | 24.0 | −7.0 | 58.7 (12th) |
| s30 | 39.50–42.95 | 34 | 15.0 | **30.0** | 45.0 | 15.0 | −3.0 | 62.1 (11th) |
| **s31** | 47.48–49.55 | 20 | **24.0** | **35.0** | 54.0 | 19.0 | **+5.0** | 70.7 (10th) |
| s32 | 51.35–56.15 | 47 | 20.0 | **36.0** | 48.0 | 12.0 | +1.0 | 91.2 (8th) |
| s33 | 57.95–59.72 | 17 | 14.0 | **28.0** | 40.0 | 12.0 | −8.0 | 57.8 (13th) |
| **s34** | 62.12–66.69 | 45 | **36.0** | **45.0** | 54.0 | 9.0 | **+17.0** | 128.3 (2nd) |
| s35 | 68.49–73.29 | 47 | 15.0 | **48.0** | 57.0 | 9.0 | +3.0 | 137.9 (1st) |
| s36 | 78.08–79.60 | 15 | 17.0 | **28.0** | 51.0 | 23.0 | −20.0 | 50.3 (14th) |
| **s37** | 82.00–86.75 | 47 | **15.0** | **21.0** | 51.0 | 30.0 | −7.0 | 20.5 (16th) |
| s38 | 88.45–93.06 | 46 | 21.0 | **35.0** | 48.0 | 13.0 | +14.0 | 77.4 (9th) |
| s39 | 94.06–96.60 | 25 | 20.0 | **38.0** | 44.0 | 6.0 | +3.0 | 102.2 (3rd) |

```
median  s35 48 · s34 45 · s27 42 · s28 40 · s25 38 · s39 38 · s32 36 · s31 35
        s38 35 · s26 34 · s29 33 · s30 30 · s33 28 · s36 28 · s24 23 · s37 21
p10     s34 36 · s27 31 · s25 26 · s28 24 · s31 24 · s38 21 · s32 20 · s39 20
        s26 19 · s29 19 · s36 17 · s24 16 · s30 15 · s35 15 · s37 15 · s33 14
```

**Prediction quality, stated because five predictions have been wrong on this
run:** the source-side chain got the two things that matter exactly right —
#1/#2 on median (s35, s34) and #15/#16 (s24, s37) are the same scenes in the same
order on the encode. Largest displacement in the middle of the table is three
places (s26 7th → 10th, s39 3rd → 5th). The encode compresses the range from
20–138 down to 21–48 because the scrim is in it; a 27-point band is still more
than double ch1's rendered spread of 12, which answers the ch1 tone note on the
mp4 rather than on a source file.

### The invariant, scored on the encode

| clause | s31, before | s31, now (encode) |
|---|---|---|
| on the chapter's luminance floor | median 7.1, **LAST of 16** | **35.0, #8 of 16** |
| crushed p10 | 0.0 | **24.0, #4** |
| arrives on a drop | **−52.8** | **+5.0** |

The chapter's largest figure, `$656,650`, no longer sits on the floor by any
measure available. s27 rides along at #3 median / #2 p10 with a +8.0 step-in.

### The payoff frame re-scored FROM THE ENCODE — s34 still passes all four

Top quartile = `ceil(16/4)` = **4**.

| clause | s34 on the encode | verdict |
|---|---|---|
| sound-off pass | a contract page with a pen | **PASS** |
| top quartile on median | 45.0, **#2 of 16** | **PASS** |
| #1 or #2 on p10 | 36.0, **#1 by 5.0** | **PASS** |
| non-negative median step in | s33 28.0 → 45.0 = **+17.0** | **PASS** |

Headroom shrank exactly as fin-assets warned it would: s34's p10 lead over the
field was +61.6 predicted at attempt 1 and is **+5.0 measured** now that s27 is
bright. It still leads. s35 is #1 on median (48.0) and 13th-equal on p10 (15.0) —
the same white-forms-on-black shape as before, still failing clause 3.

## 4. ⚠ ESCALATION — the floor RELOCATED to s37, and the encode agrees

Not actioned, as briefed. **The chapter's luminance floor is now s37: median
21.0 (LAST of 16 on the encode as well as at source), p10 15.0, spread 30.0
(the chapter's widest), arriving on −7.0.** It holds **line 3.14** —

> “Early retirees who anticipate long payout periods should plan on lower
> withdrawal rates.”

— the verbatim Trinity conclusion, archetype C, 76px over three lines. That is
one of the two beats the whole fine-print run exists to deliver, so the question
the invariant asks ("is the darkest longest-held frame the most substantive
beat?") has a real answer either way and it is **the editor's and the CEO's to
give, not mine**. Facts they will want with it:

- s37 is not newly dark: it was 15th at 21.6 in attempt 1's table and only became
  last because s31 climbed past it. Nothing this attempt did moved it.
- It is the chapter's **third-longest scene** (7.148s), so "longest-held" cuts
  against it.
- Its photograph passes the sound-off gate cleanly (an open book under a desk
  lamp), and its 30.0 spread is a lit page against a dark room — two real
  regions, not a specular pinprick.
- The **p10** floor is a different scene: **s33 at 14.0** (median 28.0), the
  hands-leafing-a-document hand-off line. And the chapter's #15 on median is
  **s24 at 23.0**, which is the deliberately cool opener §11 asks for.
- If the ruling goes against s37, the lever is the photograph and this stage
  cannot supply it — same shape as attempt 1's s31 escalation, one re-fetch.

## 5. Everything the brief said to preserve, verified present

| item | verified how |
|---|---|
| s34 payoff, four clauses | re-scored **from the encode**, §3 above |
| all three rate-assert branches | **RE-PROVEN on this file**, §6 |
| s30 `housing-share` at exactly 0.334 | the `SHARE` constant and its build-time throw are untouched; the bar reads a third on the sheet |
| s26 cascade speech-anchored | `chipAt [4.37, 5.01, 5.89, 6.71]` unchanged; three chips visible on the sheet, the fourth lands after the sample |
| s27 / s31 in the cut's `dry` list | `cues-tables.json` still lists both; `audio.json` emits **only the joint `transition`** inside each rung's span |
| s26 `brule` 400 | unchanged (the 252 fix from attempt 1's snapshot pass) |
| timing 16 / 96.601s / s24–s39 | all four homes regenerated from `timing.json`; the gap, overlap, track-parity and framing asserts all ran; max drift 0.000s |
| 24 cues, min gap 1.100s, `bed-tension` | `cues.py` exit 0 on the shipped file |

## 6. The rate asserts, re-proven rather than assumed — without disturbing the artefacts

`$656,650 $2,500 a month $13,318` planted into **s33's kicker** (a scene with no
rate, no marker and no derivation), regenerated, `hyperframes check` returned one
hard `page_error` carrying all three messages:

```
RATE ASSERT FAILED — s33 renders $656,650 with no #s33-rate carrying a rate ·
s33 renders the derived income $2,500 a month with neither a rate nor an
ILLUSTRATIVE marker in frame · s33 renders the published figure $13,318 with no
rate, no provenance and no derivation in frame
```

⚠ **Method note worth keeping.** The plant was run AFTER the render, so a naive
revert would have left `index.html` newer than the mp4 and broken the freshness
invariant the gate checks. Clean artefacts were copied out with `cp -p` first,
the revert regenerate was confirmed **byte-identical by md5**, and the originals
were restored with `cp -p` so the mtimes are their true generation times rather
than a touch. Nothing was faked and nothing was re-rendered for a test. **Better
next time: prove the asserts before the render, not after.**

## 7. The max-density snapshot pass — two frames, and I looked at both

Only s27 and s31 changed; the other fourteen are byte-identical to the frames
attempt 1 opened. **One fresh `-o` directory, never reused:**

| batch | dir | times (s) | frames on disk | frames I opened |
|---|---|---|---|---|
| b6 | `snapshots/qa/b6` | 21.87 (s27 last cue settled) · 47.61 (s31) | 2 | **2, both full-resolution** |

The CLI succeeded on the first attempt with the retry loop in place. `--no-end`
was passed so the two times on disk are the two times asked for — filenames read,
not exit codes trusted (`frame-00-at-21.87s.png`, `frame-01-at-47.61s.png`).

What the two frames show: both `.stack`s inside the safe area, kicker / rate /
mega / foot in order with nothing colliding, the `THE LADDER` measure bar and its
label bottom-left with **s31's fill visibly about twice s27's** (307.7px against
156.0px — the climb reads), the `cut-en` watermark riding bottom-right, no
overflow anywhere. On s27 the handle sits upper-right and the type owns frame
centre, which is what `center top` was chosen for. On s31 the escutcheon runs
behind the mega and the sunlit doorway holds the right third; the type is legible
over both.

## 8. For fin-editor and the CEO — flagged before review finds them

1. **The relocated floor at s37 (§4).** The one ruling this chapter needs.
2. **s27 is the chapter's emptiest photograph** — ~75% smooth panel — and it is
   now #3 on median. That combination is precisely what the CEO's "near-zero
   spread is not a credit" sharpening exists to catch, so it is declared rather
   than banked: it is *not* the payoff frame, it does not lead anything, and it
   carries the chapter's heaviest type load (rate + mega + foot + measure bar),
   which is §10 routing the busiest frame to the quietest picture. Its encode
   spread is 7.0, the second-narrowest in the chapter after s39.
3. **s27 / s28 sat 1.2 points apart at source and the encode separates them** —
   42.0 against 40.0, with s26 at 34.0. The three-in-a-row sameness fin-assets
   warned about is real but mild on the mp4; worth an eye on the sheet.
4. **Carried forward from attempt 1, unchanged and still true:** s30's `.art-lift`
   panel edge reads as a tonal step on the smooth sky; s34's legible words are
   `9. Insurance` / `10. Assignment` under a quotation about taxes; s35's sticky
   note says "Tax time!" and the form is dated 2020; **s36 sheets without its
   focal** (+4.19 against the sheet's +2.6 sample) — judge it from the mp4;
   s25's foot wraps and orphans `2025`.
5. **`motion.js` drift, still open and still not mine to fix:**
   `grep -L "AUTHORED OPACITY" studio/videos/passive-income-number-*/assets/js/motion.js`
   still returns `-en-ch2` and `-hi`. Harmless for ch2 as it stands; the full-cut
   assembly needs one motion.js, not two.

## 9. Nothing improvised

No system helper redefined inline, no previous video's `index.html` read for
technique, no CDN or network reference (`check_build`'s `https?://` sweep is
clean), no per-scene `filter:` override anywhere — the locked grade stands
unamended on all sixteen scenes, and the only photograph knob used is
`background-position`, which moves the picture inside its own cover box. The
composition's inline `<style>` still holds exactly the four plate rects and the
one `.v-chiprow` component.
