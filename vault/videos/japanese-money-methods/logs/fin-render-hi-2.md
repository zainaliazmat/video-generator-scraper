---
summary: Gate-two re-check for japanese-money-methods-hi after the `.scene { isolation: isolate }` fix. The attempt-1 defect is gone — frames 551/552 of the s3→s4 boundary carry zero scene-03 text, and nine boundaries plus all three hold pairs composite correctly. PASS, encode may start.
updated: 2026-08-01
source: hyperframes snapshot v0.7.66 + ffmpeg signalstats against studio/videos/japanese-money-methods-hi/index.html
---

# fin-render — hi — attempt 2 (GATE TWO, frame re-check)

Invocation 1 of 2. **No encode was run.** `renders/` does not exist yet.
Audio/VO/loudness QA is deferred to invocation 2.

## Verdict

**STATUS: ok.** The attempt-1 boundary defect is fixed and no regression was
introduced by the CSS copy.

## The fix, verified in place

`studio/videos/japanese-money-methods-hi/assets/blockframe.css:63` —
`.scene { … isolation: isolate; }`, with the load-bearing comment above it.
(Note the cut's copy is `assets/blockframe.css`, not `assets/css/blockframe.css`
as attempt 1's fix note guessed.)

Frame rate 30 fps (no `data-fps` on `#root`). Root `data-duration` = **659.709 s**
= `assets/voice/timing.json` `total` 659.709 s — matched, 0.000 s apart.

## 1. Boundary forensics — s3→s4, the attempt-1 proof

Dissolve window 17.917 → 18.367 s (`dissolve(0.45, power1.inOut)`).
Measured region: the headline/statement box, `crop=700:230:300:430`, via
`ffmpeg -vf signalstats`. Background floor in that box is YAVG 29.956 / YMAX 31;
settled scene-03 (t=17.70) is **YAVG 42.484 / YMAX 225**.

| t (s) | Frame | YAVG | YMAX | s3 text residual | Reads as |
|---|---|---|---|---|---|
| 17.70 | 531 | 42.484 | 225 | 100% (baseline) | settled s3 |
| 18.15 | 544 | 36.655 | 135 | 53.5% | legit 50/50 composite |
| 18.20 | 546 | 33.372 | 84 | 27.3% | decaying |
| 18.25 | 547 | 32.128 | 65 | 17.4% | decaying |
| 18.30 | **549** | 30.454 | 39 | **3.98%** | decaying |
| 18.35 | **550** | 30.086 | 33 | **1.04%** | nearly gone |
| 18.367 | **551** | 29.956 | 31 | **0.00%** | pure scene-04 |
| 18.40 | **552** | 29.956 | 31 | **0.00%** | pure scene-04 |

- **Frames 551 and 552 carry zero scene-03 text.** In attempt 1 frame 551 was
  rail `04` + scene-03's headline at 100% opacity — the unambiguous wrong frame.
  It is now bit-identical to the settled scene-04 background in that box.
- **Frame 549/550 residue is under-paint, not over-paint.** 3.98% measured
  against 4.43% predicted by `power1.inOut` at p=0.851 — agreement to 0.45 pp,
  i.e. the outgoing scene is now compositing *below* the incoming one at exactly
  the tween's own alpha. The rail number reads `04` cleanly with scene-03's
  headline ghosting *behind* it, the inverse of attempt 1.
- **Decay is monotonic** across all six in-window samples (135 → 84 → 65 → 39 →
  33 → 31). No pop, no discontinuity, no hard cut at the end of the dissolve.

## 2. Nine boundaries sampled mid-dissolve — all correct

| Boundary | t (s) | Type | Result |
|---|---|---|---|
| s1→s2 | 4.63 | dissolve, **hold pair** | rail `02` rising, s1 text dimmed under, no doubling |
| s3→s4 | ×8 above | dissolve | PASS, quantified |
| s19→s20 | 115.08 | dissolve, outgoing has **two `data-framings` bg layers** | rail `19`+`20` both partial, s19 text visibly attenuated by s20's bg — not solid on top |
| s32→s33 | 214.246 | dissolve, rail → `v-bleed` | s32 text greyed under s33's full-bleed lantern; rail `32` fading |
| s33→s34 | 222.50 | **act `shove`** (0.42 s + 4% x-push) | s33 text + green statement under-painted; s34 rail `34` at ~27% (its own `fade` at 222.392); s34 head/stmt correctly not yet risen |
| s45→s46 | 311.16 | dissolve | rail `45`/`46` cross-ghosting, s45 text dimmed |
| s65→s66 | ×5 below | dissolve, **hold pair** | PASS, quantified |
| s72→s73 | 515.42 | **act `shove`** | s72 text + gold `7.1%` under-painted, rails `72`/`73` cross-ghosting |
| s76→s77 | 542.85 | dissolve, **hold pair**, `v-bleed` → rail | rail `77` rising, s76 gold statement under-painted, no double-edge |
| s90→s91 | 643.94 | dissolve, `v-bleed` → rail | s90 text dimmed under s91's panel |

In every one the outgoing scene's `.stack` and `.railcol` sit **under** the
incoming scene and are attenuated by its alpha. The failure signature — outgoing
type at full brightness over the incoming photo — does not appear anywhere.

### `data-framings` panel swap, checked separately from the scene boundary

s19's swap is an intra-scene crossfade (`fade("#s19-bg2", 110.872, 0.40)`), not a
boundary. Sampled at **t=111.07** (mid-swap): crowd-crossing bg blends into the
blossom/shrine bg2 inside the panel, while the rail number, headline, statement
and footnote all stay at **full** opacity — correct, the swap must not touch the
type. s32's swap sampled at **t=209.461**: same behaviour, dark green board
framing at ~50%.

## 3. Hold pairs — self-dissolve flicker check

The complete set of scenes sharing a background file (derived from the
`background-image:url()` map, not assumed): **s1/s2** (`s1.jpg`), **s65/s66**
(`s65.jpg`), **s76/s77** (`s76.jpg`). All three sampled.

Panel-region mean luma, `crop=730:1080:1190:0`:

| Pair | t (s) | YAVG | |
|---|---|---|---|
| s1→s2 | 4.45 | 54.761 | |
| | 4.63 | 47.496 | |
| | 4.80 | 39.574 | monotonic ↓, Δ 15.19 over 0.35 s |
| s65→s66 | 464.20 | 43.794 | |
| | 464.30 | 43.308 | −0.49 (s65's own `ken` drift, 1.1%) |
| | 464.44 | 45.373 | |
| | 464.55 | 50.657 | |
| | 464.66 | 55.122 | |
| | 467.00 | 56.055 | settled s66; monotonic ↑, Δ 12.26 over 0.46 s |

**No flicker.** Both curves are single-direction ramps into the settled value —
a flicker would show as a dip-then-recover or a spike. The 0.49 wobble on
s65→s66 is 1.1% and is the outgoing scene's own Ken Burns, not the dissolve.
s76/s77 was read visually at 542.85 and shows no double-edge.

Why these dissolve cleanly despite sharing a file: the two framings are far
enough apart in scale that no single feature appears twice. s66 is
`background-size:auto 130%; background-position:86% 8%` against s65's full-bleed
cover — a punch-in, not a same-scale self-dissolve. Confirmed at t=467.0: the
rung-3 crop target lands, ₹500 numeral + serial **6UW 64349** legible in the panel.

## 4. Interior spot-checks — no regression from the CSS copy

| Scene | t (s) | Check | Result |
|---|---|---|---|
| s24 | 147.4 | padlock icon RED (`.warnc`) | **PASS** — solid red, stroke fully drawn, sits below the statement inside the content column |
| s36 | 245.6 | s36c not crushed to black | **PASS** — inline `filter: grayscale(.32) brightness(1.35)` holds; truck silhouette against a graded sky that keeps deep-red → orange → yellow separation, no clipping |
| s51 | 355.3 | layout + currency | **PASS** — `ON ₹30,000` / `₹6,000 out · ₹24,000 to live on`, ₹500 notes with Gandhi portrait, footnote inside the column |
| s86 | 612.8 | layout + currency | **PASS** — `RECAP TWO`, green statement, ₹20 note panel |
| s66 | 467.0 | rail scene after a hold | **PASS** — rail `66`, KAKEIBO, `SAY IT PLAINLY`, panel crop correct |
| s90 / s91 | 642.5 / 648.0 | `v-bleed` scrim, end card | **PASS** — s90 white-on-photo legible with scrim + shadow; s91 SUBSCRIBE button + `Comment which of the four hit hardest` |

- **Watermark:** the @cashguruguides mark is present bottom-right in **all 24
  frames** sampled this attempt, including every mid-dissolve and both act shoves.
- **Rail numbers:** correct in every rail frame read — 02, 19, 24, 32, 34, 36,
  45, 51, 66, 72/73, 77, 86, 91, and 03→04 across the proof boundary.

## Soft notes (non-blocking, do not hold the encode)

1. **s90/s91 share a subject, not a file.** Different images (md5 differs), but
   both are "hand + pen + notebook", so the 0.45 s dissolve at 643.94 reads as a
   soft double-exposure of a pen rather than a change of shot. Same class of
   note as attempt 1's s32 observation. Legal, just weak.
2. Attempt 1's s32 note stands: both `data-framings` are low-information
   abstract textures, so the swap reads as a colour shift, not a new subject.

## Not measured this invocation

Runtime, VO drift vs the `data-start` table, peak dBTP, black-segment scan — all
require the master, which does not exist yet. Deferred to invocation 2.

## Snapshot artifacts

`snapshots/g2-b1` (s3→s4 proof frames) · `g2-base` (settled-s3 baseline) ·
`g2-decay` (dissolve decay profile) · `g2-b2` (framings + mid-cut boundaries) ·
`g2-b3` (s45→s46, s65→s66) · `g2-b4` (s66 settled + late boundaries) ·
`g2-b5` (s1→s2 + five interiors) · `g2-b6` (hold-pair luma sample points).
