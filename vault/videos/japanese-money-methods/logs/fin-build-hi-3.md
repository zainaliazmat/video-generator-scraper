---
summary: Targeted rebuild of japanese-money-methods-hi — three surgical edits (s66 crop retargeted to the note's printed panel, s24 icon back to the now-existing .warnc, scaffold CSS re-copied), nothing else touched. `npm run check` passes with the browser passes actually running (0 lint errors / 0 layout errors / 17-17 WCAG AA); pipeline_check build-hi PASS.
updated: 2026-08-01
source: task brief (attempt 3) · storyboard-hi.md §12.1 + §7 rows 65-66 · logs/fin-storyboard-recut-2.md · logs/fin-assets-s65-4.md · tools/scaffold/assets/blockframe.css · tools/format.json
stage: fin-build, cut hi, attempt 3 (targeted rebuild)
---

# fin-build — japanese-money-methods-hi, attempt 3 (targeted rebuild)

## Result

| | |
|---|---|
| Artifacts | `studio/videos/japanese-money-methods-hi/index.html` · `assets/blockframe.css` |
| Scenes / duration | **92** · **659.709s** — unchanged, re-verified against `timing.json` |
| `npm run check` | **passed** — lint **0 errors** / 3 warnings / 3 info · runtime 0 · layout **0 errors**, 16 info · motion 0 · contrast **17/17 WCAG AA** |
| `pipeline_check check build` | **PASS build-hi** |
| Diff size | 3 lines of HTML + a 3-line comment, and one file copy |

## The three edits, and nothing else

### 1. s66's push-in retargeted to the note's printed panel

`#s66-bg` gained `background-position:86% 8%`. It was inheriting `.bg`'s
`background-position: center`, which — on the ₹500 fan that landed at **rung 3** of §12.1's
ladder — pointed the crop at the ₹20 coin in the middle of the frame, i.e. at nothing the
line is about.

`86% 8%` puts the **₹500 numeral and the serial `6UW 643492`** in the panel. Geometry, so
it is checkable rather than eyeballed: the panel is 740×1080, `background-size:auto 130%`
scales the 1920×1280 file to 2106×1404, so the visible window is 35.1% of the image's width
and 76.9% of its height; at `86% 8%` that window is image-x **55.8%–90.9%** and image-y
**1.9%–78.8%**, which contains the serial band (x 81–88%, y 2–31%) and the ₹500 numeral
(x 70–81%, y 27–48%) whole. Confirmed in the frames, not just on paper.

The hold is intact: one file across s65/s66, `ken(..., false)` on both halves, zoom
continuing through the pair — s66 at 469.6s is visibly tighter than at 466.2s, and there is
no self-dissolve. `data-start`, `data-duration`, the S map, the cue ladder and s67-onward's
`ken` parity are all untouched, which is exactly what the recut promised in exchange for
keeping the hold.

**Recorded per §12.1 rung 3 and fin-assets-s65-4:** the crop lands on a printed note panel,
**not** on a band of ruled column headings. Weaker than the recut intended, shippable, and
the reason is mechanical rather than sourcing effort — a page of pale ledger paper large
enough for legible headings measures 190–210 mean luminance and cannot also be the ≤140
RAIL OFF hero. One consequence worth naming: the acceptance criterion *"no Devanagari on the
page"* is not met either, because at rung 3 the page is a banknote and Indian currency
carries Devanagari by law. It is inside the photograph, not composition text, so the
romaji-only sign-off rule is not broken — but it is a criterion the shipped frame does not
satisfy and someone should see that written down rather than infer it.

s65 itself needed **zero** edits: still RAIL OFF full-bleed, `--warn`, `stamp` at 456.92,
`foot` carrying the sourcing caveat, 9.139s (8.689 + 0.45 transition).

### 2. s24's padlock — back onto `.warnc`

`tools/scaffold/assets/blockframe.css` now defines `.warnc` (the fix for what attempt 2
found), so the icon is `class="icon sm warnc"` again — the role-colour form the storyboard
§8 specifies and the `.icon` comment in the stylesheet promises. Attempt 2's workaround
(`.warn`, the component modifier) rendered identically; this is the convention-correct form
now that the system supports it. **Verified red, not white**, in the 147.06s frame.

### 3. Scaffold CSS re-copied

`cp tools/scaffold/assets/blockframe.css → assets/blockframe.css`. Diffed **before** copying:
the only difference between the cut's attempt-2 copy and the scaffold was the 7-line `.warnc`
block. No token, no component, no geometry rule changed — which is why the 92-frame
max-density pass from attempt 2 is not invalidated by this copy (see the snapshot section).

`assets/js/motion.js`, `assets/js/gsap.min.js`, `assets/fonts/NotoSansFinance-var.woff2`,
`assets/img/grain.png` and `assets/img/wm-hi.png` all byte-match the scaffold — checked, not
assumed. The link tag is `<link rel="stylesheet" href="assets/blockframe.css">`; no `url(../`
anywhere in the stylesheet; no CDN or network reference in the composition.

## The browser passes actually ran

This is the thing the scaffold move exists to guarantee, so it gets stated as evidence rather
than as a claim. `hyperframes check` reported **0 lint errors** (3 warnings + 3 info, none of
them errors), and the Layout, Motion and Contrast sections each produced real findings —
Layout listed 16 info items at nine sampled times, Contrast reported 17/17. A skipped pass
prints nothing; these printed. `known_benign` in format.json is empty and stays empty: no
finding was reclassified and **no design token was edited to satisfy the checker.**

The 16 layout items are all info-level `container_overflow` / `panel_out_of_canvas` on
`#s<n>-bg` inside its `.v-panel` — that is `ken()`'s scale overshooting the panel it is
clipped by, which is what a Ken Burns push inside `overflow:hidden` is supposed to do. Zero
errors.

## Snapshot pass — 1 batch, 4 frames, all 4 looked at

`snapshots/qa3/b1` (a **fresh** `-o` directory; nothing reused, nothing overwritten), one
invocation, succeeded first try — no `Navigation timeout` on this run.

| frame | at | what I checked | verdict |
|---|---|---|---|
| 00 | 147.06s | s24 padlock colour | **red** (`--warn`), rail + stack inside the safe area |
| 01 | 458.20s | s65 last cue (`foot` at 457.723 + 0.40) | full-bleed, 76px focal + foot both inside safe area |
| 02 | 466.20s | s66 last cue (`stmt` at 465.612 + 0.50) | crop on ₹500 + `6UW 6434…`, panel correct |
| 03 | 469.60s | s66 near scene end | tighter than frame 02 — zoom continues, no re-cut |

**Four frames, not 92, and that is a deliberate call rather than a skipped check.** The
92-frame max-density pass ran at attempt 2 and passed; the only inputs to layout that changed
since are three elements in two scenes plus a stylesheet whose diff I verified is a single
additive colour rule. There is no mechanism by which s1–s23, s25–s64 or s67–s92 could have
moved. Re-running them would have produced 88 frames I already know the content of and would
have made this log's frame count less honest, not more.

## Verified, not rewritten

Re-asserted programmatically over the file (`node`, not by eye): 92 `<section class="scene">`
· root `data-duration` **659.709** = `timing.json` total = s92's 652.457 + 7.252 · **0**
adjacent scenes sharing a track index · 92 `<audio>` rows (voice only — no music, no SFX
rows) · `data-framings` present on s19 / s25 / s32 (`5.20,3.985` · `5.40,3.602` ·
`5.00,4.76`) · `s36c` still carries its inline `brightness(1.35)` grade override ·
`#root class="rail cut-hi"` (ledger-rail body class + the watermark class; the avatar is
visible bottom-right in all four frames) · `assets/audio.json` unchanged (`bed-resolve`
+ 24 cues).

## System gaps — none new

Nothing was missing from `blockframe.css` or `motion.js` this attempt. The one gap attempt 2
reported (`.warnc`) has been fixed in `tools/scaffold/`, and this rebuild consumed the fix
rather than re-working around it. No icon was added to `assets/icons/` — the six this cut
uses were already in the library. No inline `.v-*` component was added.

## Still open, and not mine to close

1. **`bed-resolve` is 248s against a 659.709s cut** (storyboard §2 / §12.2). `mix.py` laps
   the bed with a crossfade, so per the recut log this should not be re-escalated — but the
   bed choice is fin-render/audio's, not this stage's.
2. **The three `max_scene_seconds` breaches** (§6, s19 / s25 / s32) are resolved *visually*
   by the second framings and declared via `data-framings`; `check_build` passes. The
   orchestrator decision on whether `check_build` should read `data-framings` natively still
   lives under `tools/`, which this stage may not write.
