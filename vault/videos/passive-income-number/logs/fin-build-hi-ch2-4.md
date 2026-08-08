---
summary: Chapter-2 hi build, attempt 4. Regenerated against the four replaced photographs (s11, s14, s15-crop, s16); the s15 crop geometry was re-verified numerically against the NEW 1.78:1 parent rather than carried forward, and the two carry-over fixes (s18's 1.380s settled figure, s20's one drawn layer) were confirmed present in the EMITTED file, not just declared. All checks green; the encode says the hero now leads on median and p10 — by 1.0 median point, which is one quantisation step of my own sampler and is fin-render's to settle.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch2/ (index.html 17:33:52, renders/DRAFT-ch2.mp4 17:46:12) and from assets-ch2/final/ at full resolution
---

# fin-build — passive-income-number hi ch2, attempt 4

Nothing structural changed. The photographs under s11 / s14 / s15 / s16 changed, so what
this pass owed was (a) re-derive every artifact so index.html post-dates the pixels, (b)
re-verify the two things that are true of the FILES and not of the markup — the hold crop
geometry and the pictures the shipped notes describe — and (c) prove the two carry-over
fixes are in the emitted document rather than in a log entry.

## 1 · The s14→s15 hold — geometry re-verified against the NEW aspect, not carried forward

The brief's warning is the one that could have shipped silently, so it was answered with a
measurement rather than by copying last pass's numbers.

    s14.jpg  1880 x 1057   aspect 1.778619
    s15.jpg  1725 x  970   aspect 1.778351

**Search, not assertion.** Sliding s15 over every window of s14 in dx 70..85 / dy 36..51,
the mean-absolute-difference minimum is at **+77 +43, MAD 1.10** (JPEG noise floor — a
wrong offset in this search runs 8–20×). That offset is the geometric centre to within half
a pixel: (1880−1725)/2 = 77.5, (1057−970)/2 = 43.5.

| Quantity | Value | What it has to equal |
|---|---|---|
| linear ratio 1725/1880 | **0.917553** | the 0.91754 spec |
| vertical ratio 970/1057 | 0.917692 | the same, within 0.015% |
| **1 / 0.917553** | **1.08986** | **HOLD_A's end scale 1.090** ✓ |
| aspect delta s14 vs s15 | 0.015% | must be ~0, or `cover` scales the two files differently and the ratio stops governing |

So `HOLD_A = [1.000, 1.090]` and `HOLD_B = [1.000, 1.065]` are **unchanged and still
correct** — the new pair happens to land on the same geometry the old one did, which is why
they must be re-derived rather than assumed: identical constants over a re-derived crop is
the *evidence*, not the shortcut.

The old pair's numbers, for the record, were 1725×1142 out of 1880×1245 at +77+51. The
`.src` and the s15 note in build.mjs both said that until this pass; both now say +77+43.

**Confirmed a second way, from this pass's own encode.** Frame-to-frame MAD on the top
400 rows (photograph only), 30 fps, at four joints:

| Joint | window mean | window max | in-scene baseline |
|---|---|---|---|
| **s14→s15 (declared HOLD)** | **0.146** | 0.245 | 0.076 |
| **s17→s18 (declared HOLD)** | **0.350** | 0.527 | 0.300 |
| s15→s16 (real dissolve) | 0.782 | 1.385 | 0.305 |
| s16→s17 (real dissolve) | 0.984 | 2.158 | 0.481 |

Absolutely, the hold produces **5–7× less** frame-to-frame change than the dissolves either
side of it. ⚠ One honest note: as a RATIO to its own baseline the s14→s15 hold reads 1.9×
where attempt 2 measured ~1.0× on the notebook pair. That is a property of the new picture,
not of the crop — sharpened pencils are a high-frequency subject, so both the baseline and
the dissolve-window numbers rise together, and the ratio is the wrong statistic when the
denominator is a near-static dark frame. The absolute comparison above is the one that
answers "is a cut being made", and it says no. fin-render's full-resolution scdet + MAD
pass is still the settlement.

## 2 · s11 — the frame now has a subject, and the layout's old excuse is gone

s11 is an ancient stepped water tank (brick and stone, steps down to standing water),
replacing the pale-sky rooftop tank that the round-2 ruling made ineligible to lead.

The composition **did** treat this slot as an empty backdrop, in exactly one place: the
scene note's rationale, *"the empty sky is exactly where the centred stack sits."* That
sentence is dead and has been rewritten rather than left as shipped documentation of a
picture that no longer exists — stale prose in the emitted file is the same failure family
as everything else on this chapter.

Nothing structural needed to move, and I checked each of the three the brief names:

- **Type placement** — `.centred` is a property of `art-off`, chapter-wide (twelve of
  thirteen scenes), not a judgement about s11's sky. The stack now lands over the pool and
  the far steps. **Verified from a snapshot at this scene's last cue** (t=13.40): the amber
  focal reads clean against the dark water, `npm run check` reports the band AA, and the
  tank is unmistakable around the type.
- **Scrim** — the system `.scrim`, no per-scene override anywhere in this cut. Untouched.
- **Ken** — stays `o` (1.16 → 1.00, pulling back). Over an empty sky that direction was
  arbitrary; over a stepped tank it opens out from the water to the whole vessel, which is
  what «सालों से थोड़ा-थोड़ा भरा» wants. It is also parity-locked: the build asserts every
  in-chapter boundary alternates, so flipping s11 would throw.

**Side effect worth carrying to ch4/ch5:** the editor's finding #9 (the tank through-line
has no recognisable constant) now has a candidate. s11 is masonry, s12 is a brick wall,
s13 is a brass tap on stone — the material finally agrees. Whoever briefs 4.7–4.8 and
5.4–5.5 should brief **this** tank class, not the retired plastic one.

⚠ **One observation, not a finding, for the editor.** The stepped tank reads to me as a
Newar *hiti* (Bhaktapur/Patan) rather than an Indian stepwell — same visual family,
subcontinental either way, brand-free and currency-neutral, so nothing in the constraint
set is breached. fin-assets calls it Indian on the photographer's own title. Raising it
once because this run has been bitten four times by "close enough" geography, then dropping
it.

## 3 · s16 — the hero, and the composition does not crop to a note

Current-series ₹500 over a field of further ₹500s, even light, one ₹-coin stack. One serial
(`962971`) is legible; there is no second serial in frame, so the two-notes-one-serial test
cannot fire. Per the brief I did not re-litigate the currency read.

What I *did* check, because it is mine: **no framing in this composition crops to a single
note.** The `.bg` is full-bleed with the standard `inset -8%` bleed under one `ken`
(1.00 → 1.16); there is no cut-in, no plate, no zoom-to-region on this scene, and no
`data-framings` swap. Peak magnification is the same 1.16 every other scene gets, so
nothing here enlarges a serial panel beyond what the still already shows.

## 4 · The two things that had to survive — verified in the EMITTED file

Attempt 2 declared a fix it never emitted, so both were read back out of `index.html` after
the build rather than inferred from build.mjs:

    index.html:441  pop("#s18-num", S.s18 + 2.81, 0.6);
    index.html:442  countUp("#s18-num", S.s18 + 2.81, 0, 2500, "en-IN", 0.45, "₹", "");
    index.html:443  fade("#s18-foot", S.s18 + 3.11, 0.5);

**Present.** The spoken anchor is still +2.81 and `timing.json` is untouched. Settled time
= 4.640 − (2.81 + 0.45) = **1.380s**, against the build's own 1.20s floor, which throws if
a later edit lengthens the roll. s16's hero benchmark is 2.245s, unchanged.

**The drawn layer** is still exactly one, s20's twelve cells, and the build asserts the
count (`chapter 2 carries exactly ONE drawn layer`). Twelve cells render — counted in the
snapshot at t=70.06 and in the sheet cell.

**The two declines re-read against the files that are actually on disk now**, since
fin-assets reverted both slots after the ruling:

- **s19 wifi arc — decline still correct.** The file is the black phone, screen off, on
  wooden slats (md5 `c0d1bcf5…`, viewed at full resolution). So the premise of the decline
  is unchanged: one of two named subjects is in frame, and the second is carried by the
  statement over it. The mast that briefly occupied this slot is gone, and with it the only
  thing that could have changed the argument.
- **`÷12` at s17→s18 — decline still correct.** s17/s18 are unchanged, and the division is
  still asserted three times in type (s17's statement, s18's figure, s18's foot).

## 5 · `fade()` now animates to the authored opacity — verified INERT here

The scaffold change is live through the symlink. Checked rather than assumed, because the
helper reads an **attribute**, not CSS:

    var a = el.getAttribute && el.getAttribute("opacity");

Every `fade()` target in this composition is a `<p>` — `#s10-foot #s16-foot #s17-foot
#s18-foot #s20-foot #s19-rate` — and **none carries an `opacity` attribute**. Grepped:
the only `*opacity=` in the whole document is `fill-opacity=".2"` ×12, on s20's ghost
cells, which are static SVG rects that no helper ever touches. The other partial opacity in
play is CSS (`.has-photo.art-forward .art { opacity: .52 !important }`), also untouched by
`fade`.

So the ~.2 fill floor reads exactly as fin-render measured it last pass (ghost ring +7.78
ΔY, green mark +19.72 ΔY over local background) — the layer was never a `fade` target, so
there was nothing for the old hardcoded 1 to have been forcing. **No change, and the reason
is structural rather than lucky.** If a later chapter authors a drawn layer at a partial
`opacity` attribute AND fades it in, that chapter gets the fixed behaviour.

## 6 · Checks

| Check | Result |
|---|---|
| `npm run check` | **0 errors**, 4 warnings, 13 infos · Runtime 0/0 · **Contrast 13/13 AA** · "Check passed" |
| `tools/check_vo_frame.py … --cut hi --chapter 2` | **PASS**, 13 scenes cross-checked |
| `tools/audio/cues.py <project>` | **exit 0**, empty stderr, 17 cues, music `bed-resolve` |
| `pipeline_check.py check build --cut hi --chapter 2` | **PASS build-hi** |
| Frames / duration | **2446** (`-count_frames`) / **81.533333s** — ceil(81.531 × 30) = 2446 ✓ |
| Root / offset | 81.531s · 42.475s (= hi ch1's root; the chapters abut) |
| mtimes | build.mjs 17:33:41 → index.html 17:33:52 → DRAFT 17:46:12 → SHEET 17:46:34 ✓ |

The four warnings are the four this project has carried since attempt 1 —
`composition_file_too_large`, `timeline_track_too_dense` ×2,
`composition_heavy_overlay_count_high` — plus `container_overflow` infos on every `.bg`
(the declared `inset -8%` ken bleed) and on `#s20-plate` (the archetype-C rect is
`left 1046 / top −60 / 934×1200` per format.json, i.e. 60px off-canvas by specification).
**No token was edited to satisfy anything**, and `known_benign` stays empty — these are
warnings and infos, and neither suppresses the layout or contrast passes, both of which ran.

**Max-density snapshot pass — 14 frames, all looked at, three batches, three separate `-o`
directories** (`snapshots/qa4/b1` 5 frames · `b2` 5 · `b3` 4), one per invocation because
the CLI wipes its output directory. Sampled at each scene's LAST cue completion:
1.85 · 7.74 · 13.40 · 19.53 · 27.39 | 36.40 · 40.91 · 47.98 · 53.33 · 59.07 | 62.51 ·
70.06 · 74.88 · 81.40. Every `.stack` sits inside the safe area, nothing overflows, the
watermark rides bottom-right on all 14, and s20's twelve cells are all present and countable
at 70.06.

## 7 · What the encode says about the un-inversion (indicative — fin-render settles it)

Measured off this draft, 4 fps over each scene's settled span (start+0.45 → next start),
full-resolution Y as stored:

    MEDIAN  s16 38 · s12 37 · s21 35 · s18 34 · s17 33 · s20 31 · s14 30 · s15 30
            · s11 29 · s19 29 · s9 24 · s10 21 · s13 21
    p10     s16 26 · s20 24 · s21 23 · s12 22 · s14 19 · s15 19 · s18 19 · s11 17
            · s17 17 · s10 16 · s9 15 · s13 15 · s19 13

| Round-2 clause | Requirement | Measured |
|---|---|---|
| Sound-off gate | name a concrete object | pass — ₹500 notes and a coin stack |
| Median | top quartile (ceil(13/4)=4, floored at 3 ⇒ top 4) | **#1 of 13**, 38 |
| p10 | #1 or #2 | **#1 of 13**, 26 |
| Median step in | s15 → s16 must not fall | **+8.0** |
| (spread p90−p50, reported beside) | — | 10.0, and not claimed as a credit |

⚠ **The margin fin-assets would not call safe got tighter, not looser.** The declared
prediction was a ~1.3-point median lead over s12; measured here it is **+1.0**, which is
**one quantisation step** of an integer median off a 4 fps sample. I am reporting this as
an indication that the swap went the right way, **not** as the settlement — the whole reason
this attempt exists is that a declared margin inside the error bar was treated as a result.
fin-render measures it properly, and if it inverts, fin-assets has already named s12 as the
lever.

Two things the ruling touches that are still open and are not mine to close: **s20 fails the
binary sound-off gate** (a blank grey plaster wall names no object; it is 6th on median so
it leads nothing, but it is legible only because this build draws twelve cells on it —
fin-assets has flagged for a ruling whether an art-hosting background must pass the
photograph gate), and **s19 still holds the chapter's lowest p10** (13), with the black
phone screen sitting exactly where the type lands.

## Verdict

**PASS.** Regenerated against the four replaced photographs. The s15 crop was re-derived and
verified numerically against the new 1.78:1 parent (+77+43, MAD 1.10, 1/0.917553 = 1.08986 =
HOLD_A's 1.090) so the hold is one continuous zoom and not a mid-hold cut to another picture;
s11's dead "empty sky" rationale is gone and its subject is respected in type, scrim and ken;
s18's 1.380s settled figure and s20's single drawn layer were read back out of the emitted
file; and `fade()`'s new authored-opacity behaviour is verified inert here for a structural
reason. `hyperframes check` 0 errors / 13-13 AA, `check_vo_frame` PASS, `cues.py` exit 0,
`pipeline_check check build` PASS, 2446 frames / 81.533s, root 81.531s, offset 42.475s.
