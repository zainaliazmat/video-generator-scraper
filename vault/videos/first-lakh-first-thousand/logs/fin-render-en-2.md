---
summary: fin-render gate-two FRAME CHECK, en cut, attempt 2 — PASS. Re-shot ONLY the three changed scenes (s21, s57, s91), 8 full frames + 3 zoom crops, all read at 1:1 or 3x. All three blocking findings from attempt 1 are closed; the s91 CTA reads as designed with the bar suppressed, not as a missing element; s21 holds at delivery resolution without a second filter override (measured). No encode was run.
updated: 2026-07-31
source: studio/videos/first-lakh-first-thousand-en/snapshots/qa5/{b1,z21,z57,z91,z91scuff} + qa3 (attempt-1 reference frames)
stage: fin-render, cut en, attempt 2 — invocation 1 of 2 (frame check only)
---

# fin-render — «The First $10,000 Is The Hardest» en, attempt 2 — GATE TWO: PASS

**No encode was run.** Per orchestrator scope this invocation is the frame check only.
`renders/` does not exist and must not be created by this stage.

## Scope of this review — stated plainly

**This is NOT a full 92-scene re-review.** Only three image files changed since attempt 1
(`s21.jpg` `5c28492a…`, `s57.jpg` `a71a51d0…`, `s91.jpg` `51db34ea…`) plus one composition
change (bar suppression, which touches exactly one scene — 91 `.swissbar` for 92 scenes).
Scenes 21, 57 and 91 were re-shot and re-read here. **The other 89 scenes were read at native
1920x1080 during attempt 1 and were not re-opened.** Their pass carries forward on the basis
that their pixels are byte-identical, not on a fresh look.

## Sampling times — the attempt-1 dissolve rule applied

Every scene here carries a 0.45 s cross-dissolve, so the first safe sample is
`scene_start + 0.45`. Attempt 1's s57 sample at 306.05 s photographed **scene 56's cheesecake**;
that is not repeated. Each frame below was confirmed to be the intended scene by its own bar /
foot copy before anything was judged.

| scene | start | first safe | sampled at | scene confirmed by |
|---|---|---|---|---|
| s21 | 108.630 | 109.080 | **109.10** (darkest), **114.25** (ken max 1.16) | bar `SAME INPUT`, foot `CH 3 · 21 / 92` |
| s57 | 305.894 | 306.344 | **306.40** (ken max 1.16), 309.61 (last cue), **312.60** (ken min 1.00) | bar `20% OF $4,000`, foot `CH 6 · 57 / 92` |
| s91 | 496.307 | 496.757 | **496.80**, 497.86 (last cue), 499.70 | focal `SUBSCRIBE`, foot `CH 9 · 91 / 92` |

8 full frames in `snapshots/qa5/b1`, every one verified `1920x1080 rgb24` by `ffprobe` —
snapshots come out at delivery resolution, so 1:1 inspection is exact, not a proxy.
6 CLI attempts absorbed by the retry loop on b1 (`Navigation timeout of 10000 ms exceeded`);
the directory on disk is the run that succeeded. No contact sheet used as evidence.

## The three blocking findings — all closed

### s21 — `SUMA PLN` gone; frame carries no text at all

3x crop of `#s21-img` at the ken maximum (`qa5/z21`, 5760x1950). Both ledger pages are
**blank** — no print, no receipt, no currency mark, no glyph structure anywhere in the
aperture. Abacus rods and beads resolve; the dark object at lower left is an ornamented
case/rule with no lettering. **The Polish fiscal receipt is gone.** Closed.

### s21 brightness — fin-build's "no second `filter:` override" claim VERIFIED at delivery resolution

Measured on the delivered 1920x600 aperture (`crop=1920:600:0:180,format=gray,signalstats`,
limited-range Y):

| frame | ken | YMIN | YLOW (p10) | **YAVG** | **YHIGH (p90)** | YMAX |
|---|---|---|---|---|---|---|
| **s21 @ 109.10 — worst frame, first safe after the dissolve** | 1.01 | 0 | 0 | **30.80** | **92** | 161 |
| **s21 @ 114.25 — ken max** | 1.16 | 0 | 0 | **38.67** | **96** | 161 |
| s90 @ 494.30 — the scene that DID need `brightness(1.25)` | — | 0 | 0 | **13.79** | **33** | 255 |
| s63 @ 342.26 — ordinary dark scene, no override | — | 0 | 31 | 70.01 | 123 | 164 |
| s10 @ 48.40 — bright reference | — | 0 | 18 | 117.33 | 144 | 243 |

fin-build reported 38.7 / p90 96 at ken max; my independent read is **38.67 / 96** — exact
agreement, and it holds on the delivered pixels, not on a pre-grade source. The ken push
brightens (YAVG 30.80 → 38.67, p90 92 → 96), so the scene's worst frame is its first, and even
there it sits at **2.2x s90's mean and 2.8x s90's p90**. s21 is chiaroscuro, not crushed.
**No second override needed. The one per-video grade allowance stays on s90.** Confirmed.

### s57 — US $20s, no serial in the aperture at any point in the ken

Read at both ken extremes. 3x crop at **312.60** (ken minimum = the most of the source ever
visible, i.e. the worst case for an unwanted marking) in `qa5/z57`: three overlapping US
twenties, legible engraving `20`, `20`, `TWENTY`, partial `FED…`. **No serial number enters the
3.2:1 aperture at any point in the sweep**, so the repeated-`E 34112707 E` defect cannot recur —
the crop never reaches the part of the note that carries one. Currency correct for a $ cut.
Aperture at 306.40: YAVG 69.55, p90 127. Closed.

### s91 — pen unmarked; and the CTA reads as DESIGNED, not as a missing element

3x crop (`qa5/z91`) plus an **8x** pixel-region crop of the one remaining light mark
(`--zoom "430,680,240,90" --zoom-scale 8`, `qa5/z91scuff`). The pen barrel is completely
unmarked — grey metal, clip, knurled grip, **no engraving, no brand, no country of manufacture**.
The notebook is blank ruled paper. At 8x the desk mark is a scatter of pale specks on wood
grain (region YAVG 37.6, p90 120) with **no letterforms and no glyph structure**.
`Kaweco AL Sport Germany` is gone. Closed.

**On the suppressed bar — asked to confirm, and it confirms.** With `bar: —` now suppressed the
top 180 px of s91 is one continuous field of `--bg`, identical in colour to the frame surround.
There is **no leftover black bar strip, no stray dash, no empty container box** — the three tells
that would make it read as a title that failed to load. Every other system element is present and
in place: the `.swissrule` fires on schedule (absent at 496.80, drawn by 497.86 — `fill` starts at
496.857, so that is correct, not a defect), the `SUBSCRIBE` pop block, and the foot. It reads as a
deliberately quiet close. **Confirmed as designed.**

## Layout, safe area, contrast — measured on the three frames

- Left margin on all elements: 100 px (5.2 %). Type is `.stack`-aligned and nothing overflows.
- Foot vs background contrast, limited-range gray: **161 vs 17** on every frame checked
  (≈169 vs ≈1 full-range). Focal and bar are brighter still. No legibility risk.
- **One measured note, not a blocker:** s91's foot (`CH 9 · 91 / 92`) has its lowest ink at
  **y≈1059**, a **21 px bottom margin (1.9 %)** — inside a 3.5 % action-safe box, it would be a
  miss. Checked against attempt 1's own s91 frame (`qa3/b8/frame-06-at-497.86s.png`): lowest ink
  at **y≈1057**. **The bar fix moved nothing** — this is the pre-existing `pop` layout variant
  (s91 is the only `"pop"` row in `build.mjs`), it was present in the frame set I passed on layout
  at attempt 1, and no changed file caused it. It is the chapter counter, not copy. Recorded as a
  design note for the next cut (the `pop` variant should reserve the same 60 px foot band the
  other 91 scenes use); **not re-litigated as a blocker on a cut that has spent its fix pass.**

## Evidence on disk

| dir | frames | how reviewed |
|---|---|---|
| `snapshots/qa5/b1` | 8 @ 1920x1080 | all 8 read at 1:1; 4 measured with `signalstats` |
| `snapshots/qa5/z21` | 1 @ 5760x1950 (3x) | read |
| `snapshots/qa5/z57` | 1 @ 5760x1950 (3x) | read |
| `snapshots/qa5/z91` | 1 @ 5760x1950 (3x) | read |
| `snapshots/qa5/z91scuff` | 1 @ 1920x720 (8x region) | read + measured |

(`snapshots/qa5/` root also holds 5 default-spacing frames from a shell mis-quote — junk, not
evidence, and no earlier directory was overwritten.)

## Verdict

**PASS — gate two cleared.** Scenes 21, 57 and 91 re-verified at 1:1 and 3x on delivery-resolution
pixels; all three attempt-1 blockers closed; s21 needs no second grade override (measured);
the s91 CTA reads as designed. The other 89 scenes carry forward from attempt 1 unchanged and
were not re-shot. The orchestrator may run the encode.
