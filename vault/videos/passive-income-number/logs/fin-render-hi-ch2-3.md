---
summary: Chapter-2 hi, attempt 3 — MEASURE ONLY on the 17:46 draft, no re-render. The hero question is SETTLED, not repeated: s16 leads s12 by +1.053 median on a complete-population measurement whose per-frame distributions do not overlap at all, and s16 passes all four clauses of the round-2 payoff ruling (#1 median, #1 p10, step in +7.43, sound-off pass). One named verification FAILS — s16's serial `962971` is legible for the whole scene and largest at the scene open, because s16's ken as emitted pulls BACK (1.16 -> 1.00), not in as its own scene note claims.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 (mtime 2026-08-08 17:46:12), all 2446 frames decoded at 1920x1080
---

# fin-render — passive-income-number hi ch2, attempt 3 (MEASURE ONLY)

Mode: **CHAPTER DRAFT, measurement pass.** No render, no snapshot, no encode. The
draft on disk is the artifact under test.

## 0 · Provenance — mtimes confirmed first hand, before any measurement

| Artifact | mtime | Ordering |
|---|---|---|
| `build.mjs` | 2026-08-08 **17:33:41** | — |
| `index.html` | 2026-08-08 **17:33:52** | after build.mjs |
| `assets-ch2/final/s11.jpg` | 17:11:55 | before the build |
| `assets-ch2/final/s14.jpg` | 17:11:57 | before the build |
| `assets-ch2/final/s16.jpg` | 17:18:44 | before the build |
| `assets-ch2/final/s15.jpg` | 17:20:06 | before the build |
| `renders/DRAFT-ch2.mp4` | 2026-08-08 **17:46:12** | after index.html ✓ |
| `renders/SHEET-ch2.jpg` / `.json` | 2026-08-08 **17:46:34** | after the mp4 ✓ |

All four replaced photographs pre-date `build.mjs`; the draft and sheet post-date
`index.html` by 12m 20s. **The draft is current. Nothing was re-rendered.**

---

## 1 · THE HERO QUESTION — SETTLED. s16 leads s12 by **+1.053 median**, and the two
scenes' frame distributions **do not overlap at all.**

### 1.1 · What was measured, and to what precision (stated before the answer)

- **Statistic:** luma (Y as stored) **median over each scene's settled span**
  (`start + 0.45` → next scene's start), full frame, 1920x1080.
- **Frames sampled: EVERY frame in every settled span.** One decode pass over the
  whole file produced a 256-bin histogram for each of the **2446** frames. s16
  contributes **147 frames**, s12 **223**. There is **no frame-choice sampling
  error** — the population is complete, not sampled. This is the specific thing
  fin-build could not claim at 4 fps.
- **Quantisation removed.** The percentile is linearly interpolated inside the
  8-bit bin, so it is continuous, not an integer. Interpolation step at the median
  bin: **5.6e-08 DN** for s12 (462,412,800 px pooled), **4.0e-08 DN** for s16
  (304,819,200 px). fin-build's "one quantisation step of my own sampler" does not
  exist in this measurement.
- **Per-frame spread, which is the honest error bar:**

|  | pooled median | per-frame median range | sd | n |
|---|---|---|---|---|
| **s16** | **37.765** | **37.67 – 37.84** | 0.05 | 147 |
| **s12** | **36.712** | **36.14 – 37.10** | 0.24 | 223 |

  **min(s16) 37.67 > max(s12) 37.10 — a clear gap of 0.57.** Every one of s16's 147
  frames is brighter than every one of s12's 223 frames. All 32,781 frame pairs
  point the same way; zero exceptions.
- **Bootstrap, 4000 resamples over frames:** difference **+1.069, 95% CI
  [+1.000, +1.137]**, P(s16 > s12) = **1.0000**.
- **Sensitivity to the span definition** (the artefact fin-build feared), 10
  definitions crossing settle offset +0.30/+0.45/+0.60/+0.90/+1.20 and tail trim
  0.00/0.45: the difference ranges **+1.005 to +1.099**. It never approaches zero
  and never changes sign.

**Verdict on precision: the margin is +1.05 with an uncertainty of about ±0.07.
That is roughly 15x its own error bar. It is RESOLVED. I am not declaring the
clause unsettled — this measurement can tell the two apart.**

### 1.2 · The robustness check that matters more than the CI: is the lead the
photograph, or the type?

s16 carries a very large white `₹10,00,000`. A median is robust to a small bright
area, but the claim deserves the test. Re-measured with the central type band
excluded, over four independent region definitions:

| Region | s16 | s12 | diff |
|---|---|---|---|
| full frame (**the ranking statistic**) | 37.765 | 36.712 | **+1.053** |
| rows 0–360 + 760–1080 | 36.378 | 35.884 | +0.494 |
| rows 0–320 + 720–1080 | 36.190 | 35.463 | +0.727 |
| rows 0–420 + 820–1080 | 36.764 | 35.895 | +0.869 |
| left + right thirds | 38.481 | 34.218 | +4.263 |

**Sign stable across all five; magnitude 0.49–4.26.** So roughly half the
full-frame margin is the type, and the photograph alone still leads — by a
smaller amount (+0.49 on the tightest reading). Reported as the honest shape of
the result: s16 wins on the ruling's statistic outright, and wins on the
photograph alone by a narrower margin that a re-crop could plausibly move.

### 1.3 · The full thirteen-scene table

MEDIAN ranks. `p90 − p50` is reported beside it and is **not** a credit.

| Rank | Scene | Settled span | n | **MEDIAN** | **p10** | **p90−p50** | per-frame range | sd |
|---|---|---|---|---|---|---|---|---|
| **1** | **s16 (payoff)** | 45.182–50.077 | 147 | **37.765** | **25.620** | 10.391 | 37.67–37.84 | 0.05 |
| 2 | s12 | 18.132–25.535 | 223 | 36.712 | 21.609 | 15.678 | 36.14–37.10 | 0.24 |
| 3 | s21 | 73.475–81.531 | 241 | 35.014 | 23.033 | 8.588 | 34.84–35.33 | 0.10 |
| 4 | s18 | 55.872–60.062 | 125 | 33.906 | 18.896 | 15.924 | 33.86–33.99 | 0.03 |
| 5 | s17 | 50.527–55.422 | 147 | 32.707 | 17.085 | 15.879 | 31.38–32.86 | 0.46 |
| 6 | s20 | 67.059–73.025 | 179 | 31.389 | 24.007 | 11.064 | 31.30–31.46 | 0.05 |
| 7 | s15 | 38.112–44.732 | 198 | 30.335 | 18.790 | 16.864 | 30.09–30.58 | 0.14 |
| 8 | s14 | 31.696–37.662 | 179 | 29.670 | 18.599 | 17.470 | 29.15–30.05 | 0.24 |
| 9 | s11 | 12.003–17.682 | 170 | 29.256 | 16.915 | 19.120 | 28.76–29.74 | 0.26 |
| 10 | s19 | 60.512–66.609 | 183 | 29.122 | **13.191** | 9.147 | 27.94–30.08 | 0.64 |
| 11 | s9 | 0.450–5.293 | 145 | 24.285 | 15.451 | 16.594 | 23.95–26.02 | 0.64 |
| 12 | s10 | 5.743–11.553 | 174 | 21.410 | 15.744 | 23.421 | 20.85–22.05 | 0.35 |
| 13 | s13 | 25.985–31.246 | 158 | 20.936 | 15.131 | 22.000 | 20.53–21.38 | 0.22 |

    MEDIAN  s16 37.77 · s12 36.71 · s21 35.01 · s18 33.91 · s17 32.71 · s20 31.39
            · s15 30.34 · s14 29.67 · s11 29.26 · s19 29.12 · s9 24.29 · s10 21.41 · s13 20.94
    p10     s16 25.62 · s20 24.01 · s21 23.03 · s12 21.61 · s18 18.90 · s15 18.79
            · s14 18.60 · s17 17.08 · s11 16.91 · s10 15.74 · s9 15.45 · s13 15.13 · s19 13.19

**s11 moved 44.0 → 29.26 median** (attempt 2 → now), from #1 of 13 to #9. The
photograph that blocked the un-inversion is gone as a blocker, and it did not
merely fall below the hero — it fell to the middle.

### 1.4 · Sound-off gate, top of the ranking — type covered, name a concrete object

Read at full resolution, each at its scene's last cue.

| Rank | Scene | With the type covered, what can a viewer name? | Gate |
|---|---|---|---|
| 1 | **s16** | A fan of Indian **₹500 banknotes** lying over each other, plus a **stack of ₹ coins** at the upper right. Denomination `५००`, `भारतीय रिज़र्व बैंक` and Gandhi's portrait all read. | **PASS** |
| 2 | s12 | **Two brass/iron water taps** bolted to a plaster wall, one with a white plastic cap. | PASS |
| 3 | s21 | A **brick wall with one brick pushed out** of the course. | PASS |
| 4 | s18 | The round numbered **keys of an old adding machine** (50, 30, 10, 20, 40 legible). | PASS |
| 5 | s17 | Same adding-machine keys, wider (70, 50, 30, 10). | PASS |
| 6 | s20 | **Nothing.** A blank dark plaster wall. Its twelve drawn cells are the only nameable content, and they are drawn, not photographed. | **FAIL** (leads nothing at #6 — carried forward as fin-assets' open ruling request, unchanged) |
| 9 | s11 | A **stepped stone-and-brick water tank** with a carved spout finial and standing water at the bottom. The tank through-line now has a subject. | PASS |

**The hero is eligible to lead.** s16's spread (10.39) is mid-pack, not near-zero,
so the "even but empty" trap does not apply either.

### 1.5 · The four clauses of `payoff_clause_and_metric_2026-08-08`

| Clause | Requirement | Measured | Verdict |
|---|---|---|---|
| Sound-off gate (runs first, as a floor) | name a concrete object with type covered | ₹500 notes + coin stack | **PASS** |
| Median | top quartile = ceil(13/4)=4, floored at 3 ⇒ **top 4** | **#1 of 13**, 37.765 | **PASS** |
| p10 | #1 or #2 | **#1 of 13**, 25.620 (+1.61 over s20) | **PASS** |
| Median step IN | non-negative at the entering joint | s15 30.335 → s16 **+7.430** | **PASS** |

⚠ One arithmetic note on the brief, which does not change the verdict: the brief
computes the quartile as "ceil(13/4) floored at 3 → **top 3**". ceil(13/4) = 4, so
the ruling's own formula gives **top 4** (floor-at-3 is a minimum, and 4 > 3).
s16 is #1, so it passes under either reading.

**ALL FOUR CLAUSES PASS. The hero is settled. The lever fin-build named (move s12)
is NOT needed on these numbers.**

---

## 2 · Every joint's median step, and what each one SHOWS

scdet at threshold 8 returned **zero detections across the whole chapter** — it
cannot rank or even find these joints, exactly as the brief says.

| Joint | step | What the eye actually sees |
|---|---|---|
| s9→s10 | −2.87 | coin macro on black → night desk, lamp and paper stacks |
| s10→s11 | +7.85 | night desk → daylit stepped stone tank |
| s11→s12 | +7.46 | tank interior → two taps on a lit plaster wall |
| s12→s13 | **−15.78** | lit wall → a single dark valve on near-black (chapter's biggest fall, and the chapter's darkest frame follows) |
| s13→s14 | +8.73 | dark valve → fan of sharpened pencils on cloth |
| **s14→s15** | **+0.67** | **DECLARED HOLD — same photograph, move continues** |
| **s15→s16** | **+7.43** | pencils → the ₹500 field. **The payoff's entering joint, non-negative.** |
| s16→s17 | −5.06 | notes → adding-machine keys |
| **s17→s18** | **+1.20** | **DECLARED HOLD — same photograph, derived crop** |
| s18→s19 | −4.78 | keys → black phone, screen off, on wooden slats |
| s19→s20 | +2.27 | phone → grey plaster + the twelve green cells |
| s20→s21 | +3.62 | plaster → lit brick wall |

**The two declared holds carry the two smallest absolute steps of the twelve
(+0.67 and +1.20).** That is independent corroboration that they are holds and not
cuts, obtained from the ranking statistic itself rather than from scdet.

---

## 3 · The s14→s15 hold — ONE continuous move on ONE photograph. Confirmed three ways.

fin-build re-derived the crop geometry from the files (+77+43, MAD 1.10,
1/0.917553 = 1.08986 = HOLD_A's 1.090). This is the encode's answer, independently.

**(a) No ghosting dip.** Cross-dissolving two DIFFERENT pictures collapses edge
energy mid-overlap; cross-dissolving two ALIGNED copies of one picture does not.
Edge energy (mean |∇Y|, photograph rows only) through each joint:

| Joint | before | **mid-overlap min** | after | dip below the lower endpoint? |
|---|---|---|---|---|
| **s14→s15 (declared HOLD)** | 1.455 | **0.715** | 0.731 | **no — monotonic, min is 2% under the endpoint** |
| s17→s18 (declared HOLD) | 1.519 | 1.382 | 1.525 | shallow, 9% |
| s15→s16 (real dissolve) | 0.757 | **0.673** | 1.975 | **yes, deep** |
| s16→s17 (real dissolve) | 2.038 | **1.128** | 1.413 | **yes, deep** |

**(b) Frame-to-frame MAD peak through the overlap** — hold **0.161**, against
**1.267** (s15→s16) and **2.120** (s16→s17). 8–13x smaller.

**(c) Registration.** Searching scale 0.94–1.10 between a frame before the joint
(37.60) and one after it (38.20): the declared hold registers with residual MAD
**1.60** (best scale 1.000, expected ~1.011 — inside this test's resolution on a
soft subject). The control real dissolve s15→s16 **does not register at all**:
best residual **6.92**, and the curve is flat across every scale, i.e. no scale
exists that maps one to the other. **4.3x separation.**

**The hold is one photograph. It does not dissolve mid-hold to a different
picture.**

⚠ **One observation for fin-editor, not a defect.** Edge energy at full resolution
falls **0.95 → 0.53 (−44%)** across this joint and stays there for s15's whole
7.07s. Same picture, but s15.jpg (1725 px wide) is upscaled harder than s14.jpg
(1880 px) to fill the same bled frame, so the second half of the hold is visibly
softer than the first. It reads as focus falling off during a push, not as a cut.
If it is ever worth fixing, the lever is cropping s15 from the full-resolution
parent rather than from the 1880 px derivative.

---

## 4 · s11 — the subject reads, and the layout is no longer standing on an empty sky

The frame is an ancient stepped water tank: brick and stone side walls, a stepped
descent, a carved spout finial mid-frame, standing water at the bottom. Nameable
in one word. It carries the tank through-line, and its masonry now agrees with
s12's wall and s13's stone.

- **Type** — the centred stack lands over the pool and the far steps. Amber
  `You filled it slowly, over years` against dark water and stone: clean at both
  ends of the move, no point where the focal crosses a bright patch.
- **Scrim** — system default, and the tank is fully readable through it at every
  sampled time. It is not being used to rescue a blown sky, because there isn't one.
- **Ken** — the move is slow and centred on the tank; the vessel is unmistakable at
  both ends. **I could not resolve its DIRECTION from the encode with a method that
  passed its own control, and I am therefore not claiming one.** A scale search over
  a 5s baseline failed its control (s14, a declared 1.000→1.090 push-in, measured
  0.992 with a flat residual curve — the method has no power on soft low-texture
  subjects at that baseline). A patch-tracker did pass the same control (+20.3 px
  mean radial on s14, four of four patches agreeing, residuals 0.9–3.8) but
  saturated its ±40 px search on s11. Recording the failure instead of the number.
  The emitted call is `ken("#s11-bg", S.s11, D.s11, false)` and build.mjs emits that
  flag as `s.ken === "i"`, so **s11 ships as "o"** — which is what fin-build declared.

---

## 5 · ⚠ s16 — THE NAMED CHECK FAILS. A serial number is legible for the whole scene.

The brief: *"Confirm no single note is cropped large enough for a serial to be
legible."* **It is not confirmed. The opposite is true.**

The ascending serial panel **`962971`** is fully legible across the upper-left of
the hero frame for the entire 5.35s scene. Digits run roughly **45–75 px tall** in a
1920x1080 frame and the group spans **~430 px** — this is not a full-resolution
pixel-peep, it is legible at thumbnail scale on the contact sheet. The three-character
prefix is cropped off at the note's edge, so what ships is a legible **six-digit
partial serial**, not a complete one.

**And it is at its LARGEST when the scene opens.** Comparing the same crop region at
t=45.30 and t=49.90, the digits are distinctly bigger at the start — i.e. **s16's ken
PULLS BACK (1.16 → 1.00)**, it does not push in. This is measured off a
high-contrast feature and is unambiguous, unlike §4's failed attempt.

⚠ **Which contradicts s16's own scene note in `index.html`**, which reads *"the
`.bg` is full-bleed under a 1.00->1.16 ken, so no framing magnifies a serial panel
further than the still already does."* The emitted call is
`ken("#s16-bg", S.s16, D.s16, false)` = `s.ken === "i"` false = **"o"**, matching the
encode and contradicting the prose. The note's conclusion happens to survive (no
framing magnifies the serial *beyond the still*, because "o" starts at the still's
own 1.16 bleed) but its stated direction is wrong, and it is the sentence that was
used to clear this slot.

Everything else the brief asked about s16 holds: the field is evenly lit, no note is
blown or crushed, **only one serial is in frame** so the two-notes-one-serial
prop-money tell cannot fire, and the currency is current-series ₹500.

---

## 6 · Cross-dissolve sampling — the outgoing text FADES WITH ITS SCENE. No stacking defect.

Sampled at **both** `qa.dissolve_sample_offsets` (0.225 and 0.38) plus the full
overlap, at four boundaries. Looking at the +0.38 frames, two scenes' type is
visible at once at every boundary — **so I measured it rather than trusting the
eye**, because that is exactly what the japanese-money-methods defect looked like.

For each boundary I built a mask of the outgoing headline's own pixels and solved a
two-endpoint mix model for the outgoing layer's remaining alpha, separately over the
**text mask** and over the **background**. If the text is stuck on top, alpha_text
stays near 1.0 while alpha_bg falls. If the dissolve is correct, they track.

| offset | s19→s20 text / bg | s10→s11 text / bg | s15→s16 text / bg |
|---|---|---|---|
| +0.00 | 1.000 / 0.996 | 1.000 / 0.997 | 1.000 / 0.999 |
| +0.10 | 0.875 / 0.882 | 0.888 / 0.887 | 0.923 / 0.924 |
| **+0.225** | 0.373 / 0.379 | 0.414 / 0.426 | 0.471 / 0.474 |
| +0.30 | 0.158 / 0.173 | 0.187 / 0.209 | 0.224 / 0.238 |
| **+0.38** | **0.033** / 0.055 | **0.047** / 0.075 | **0.021** / 0.040 |
| +0.44 | 0.001 / 0.010 | 0.003 / 0.016 | 0.001 / 0.007 |
| +0.50 | 0.000 / 0.000 | 0.000 / 0.000 | 0.000 / 0.000 |

**alpha_text tracks alpha_bg within 0.02–0.03 at every offset and reaches 2–5% by
+0.38, zero by +0.44.** The outgoing type is a fading ghost, not a painted layer.
The japanese-money-methods signature (alpha_text ≈ 1.0 through the overlap) is
absent. The ~3–5% residual at +0.38 is what my eye over-read on the contact frames —
the measurement is the answer, and it is clean.

---

## 7 · The rest of the named verifications

| Check | Expected | Measured | Verdict |
|---|---|---|---|
| Frame count | 2446 | **2446** (`-count_frames`, and 2446 packets) | **PASS** |
| **CFR from PACKET TIMESTAMP deltas** | one rate, no third value | 2445 deltas, **exactly two values**: 0.033333 x1630, 0.033334 x815. First pts 0.0, last 81.5 | **PASS** |
| Video duration | 81.531 root | 81.533333s stream / 81.536000s container; ceil(81.531 x 30) = 2446 ✓ | **PASS** |
| Resolution / pix_fmt | — | 1920x1080 yuv420p bt709 | — |
| **blackdetect** `d=0.05:pix_th=0.10` | 0 | **0 segments** | **PASS** |
| scdet threshold 8 | — | **0 detections** (cannot see these joints at all) | noted |
| **s18 figure settles** | 1.380s | digit motion ends **58.70** (countUp end 58.682 ✓, within one frame); pop scale settles **58.83** (58.832 ✓); region then **absolutely static to 60.06**. Settled = 60.062 − 58.682 = **1.380s**, of which **1.23s** is pixel-static. Floor 1.20s | **PASS** |
| **s20 twelve cells** | 12, above fill floor | **12 of 12 render.** Cell means 44.2–57.5 against local background 33.6; **min ΔY +10.60** | **PASS** |
| **Comma clearance on `.huge`** | not clipped | s16 `₹10,00,000` and s18 `₹2,500` inspected at 2x: both comma tails render complete below the baseline with clear space to the foot. s17's `₹10,00,000 / ₹30,000` likewise | **PASS** |
| **`tools/audio/cues.py`** | exit 0 | **exit 0, stderr empty**, 17 cues, music `bed-resolve` | **PASS** |
| Audio (draft) | — | true peak **−3.7 dBFS**, integrated −22.9 LUFS, LRA 2.8 | below −1 dBTP |

**cues.py vs `assets/audio.json`** — not byte-identical, and the difference is
**declared, not staleness**: build.mjs downgrades s14's derived `hero` cue to
`reveal` (storyboard §2 rings only s16 in this chapter) and records why in a
`_hero` key, plus `0` vs `0.0`. Nothing else differs across 17 cues.

---

## Verdict

**FAIL — on one named verification, not on the hero clause.**

The question this pass existed to settle is **settled and passes**: s16 leads s12
by **+1.053 median** measured on every frame of both settled spans at full
resolution, with **non-overlapping per-frame distributions** (gap 0.57), a
bootstrap CI of **[+1.000, +1.137]**, and a sign that survives ten span definitions
and four type-exclusion regions. It is **#1 of 13 on median, #1 of 13 on p10, +7.43
median step in, and it passes the sound-off gate.** All four clauses of the round-2
ruling are met. s12 does not need to move.

What fails is the serial check: **`962971` is legible across the hero frame for its
whole 5.35s**, and largest at the scene open because s16's ken pulls back rather
than pushing in — which also makes s16's own scene note in `index.html` wrong about
its move.

**The lever, and the coupling that must not be missed:** the fix is framing, not the
photograph — push the serial panel out of frame (re-crop s16.jpg, or take the
adjacent frame from the same 6HP shoot). But the hero's lead over s12 is **+1.053
full-frame and only +0.494 photograph-only**, so **any re-crop of s16 can invert the
clause that was just settled.** Re-measure both after the change; do not assume the
margin survives.

Carried forward unchanged, not mine to close: **s20's photograph fails the sound-off
gate** (blank plaster, #6 on median so it leads nothing — fin-assets' ruling request
stands) and **s19 still holds the chapter's lowest p10 at 13.19**, with the black
phone screen sitting where the type lands.
