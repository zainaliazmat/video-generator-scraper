---
summary: Chapter-1 draft re-render after the asset rework. Spine is unchanged and exact (1073 frames / 35.767s / 30fps / no black). Four of the five re-fetches land; s3's Lottie now carries exactly ONE correct rupee glyph and s7's loaded pan survives both ken extremes. s4 fails a SECOND time — the round-1 grey slab was replaced by a crushed-black one, and the source's own YHIGH of 93 is the measurable cause.
updated: 2026-08-07
source: this run — studio/videos/passive-income-number-hi-ch1 draft render attempt 2, against editor-hi-ch1-1.md findings 1-7 and fin-assets-hi-ch1-3.md
stage: fin-render, cut hi, chapter 1, attempt 2
---

# fin-render — passive-income-number · hi · chapter 1 · attempt 2

**Mode: chapter draft (orchestrator §3b step 4).** No gate-two frame check, no
dissolve sampling at `qa.dissolve_sample_offsets`, no VO-drift/VAD measurement, no
peak-dBTP read, no 1080p encode. Those run once at cut level on
`renders/FINAL-1080p-hi.mp4` and none of them would mean anything on a chapter draft.

## Commands run (verbatim)

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch1-v2.mp4 -q draft -f 30
python3 tools/chapter_sheet.py studio/videos/passive-income-number-hi-ch1 \
        renders/DRAFT-ch1-v2.mp4 \
        -o .../passive-income-number-hi-ch1/renders/SHEET-ch1-v2.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. `-f 30`
matches the final fps, so the frame counts sum and the joints do not drift.

## Measured numbers

| Quantity | Measured | Expected | Verdict |
|---|---|---|---|
| Frame count (`ffprobe -count_frames`) | **1073** | ceil(35.745 × 30) = 1073 | exact |
| Video stream duration | **35.766667s** | 1073 / 30 = 35.76667 | exact |
| Container duration | 35.776s | — | +0.009s AAC frame pad, benign |
| Declared root `data-duration` | 35.745s | timing.json | matches |
| Frame rate | 30/1 CFR | 30 | ok |
| Resolution | 1920×1080 | 1920×1080 | ok |
| Last scene `data-duration` | 6.599 (bare) | bare by design | `cut_assemble.py` re-adds the 0.45 overlap |
| Scene starts | 0 / 3.961 / 9.776 / 12.327 / 17.123 / 23.304 / 29.146 | timing.json verbatim | unchanged from attempt 1 |
| Black segments (`blackdetect d=0.15 pix_th=0.10`) | **none** | none | ok |
| Draft audio max_volume | −5.1 dB | not silent | VO present (voice-only; bed/SFX are the post-mix step) |
| Draft audio mean_volume | −25.3 dB | — | unchanged from attempt 1 |
| Render wall time / size | 1m 09.4s, 8.4 MB | — | — |

Nothing was re-timed. Every start, duration and framing is byte-identical to
attempt 1; only the five photographs and the one Lottie changed.

## Artifacts

- `studio/videos/passive-income-number-hi-ch1/renders/DRAFT-ch1-v2.mp4`
- `studio/videos/passive-income-number-hi-ch1/renders/SHEET-ch1-v2.jpg` (7 cells)
- `studio/videos/passive-income-number-hi-ch1/renders/SHEET-ch1-v2.json`

⚠ **Sheet-glob collision.** `renders/` now holds three index files that all match
`SHEET-*.json`: the round-1 `SHEET-ch1.json`, its unversioned twin `SHEET.json`
(the tool's default name), and this run's `SHEET-ch1-v2.json`. The orchestrator's
cross-chapter PNG builder globs `SHEET-*.json` and will pick up the round-1 pair as
well. **Use `SHEET-ch1-v2.json` explicitly, or delete the round-1 pair** before the
cross-chapter sheet is built.

## The grade test — every background judged against it

The chapter's own rule: the blockframe grade is locked at
`grayscale(.32) brightness(.62) contrast(1.05)` with no per-scene override
permitted (§9), so a subject whose own highlight ceiling is low can only land as a
flat panel. Measured off the ENCODED frames (`signalstats`, whole frame; YMAX 255
everywhere is the white type, so YHIGH — the 90th percentile — is the number that
matters):

| scene | t | YAVG | YLOW | YHIGH | spread | reads as |
|---|---|---|---|---|---|---|
| s1 | 2.600 | 44.84 | 19 | 55 | 36 | clock dial and numerals — the reference frame |
| s2 | 6.561 | 32.26 | 19 | 40 | 21 | window, mullion, bokeh street, chai glass with steam |
| s3 | 12.026 | 28.83 | 15 | 40 | 25 | phone face-down, body edge and glow now discernible |
| **s4** | 14.927 | **24.82** | **13** | **27** | **14** | **abstract dark diagonals — no object** |
| **s4** (widest) | 16.600 | **24.86** | **13** | **27** | **14** | identical; the pull-out reveals nothing |
| s5 | 19.723 | 32.43 | 17 | 41 | 24 | three glass jars, contents legible, wooden shelf |
| s6 | 25.904 | 29.30 | 16 | 45 | 29 | stair treads rising to a bright gap |
| s6 (widest) | 29.000 | 29.07 | 16 | 45 | 29 | still the stair; does NOT widen onto rock |
| s7 | 31.746 | 30.28 | 15 | 42 | 27 | loaded brass pan, chain, counterweight |
| s7 (tightest) | 34.500 | 30.14 | 15 | 42 | 27 | pan dominates; counterweight clipped but present |

**Six of seven pass. s4 fails, and it is the same scene that failed round 1.**

Nothing in the chapter has overcorrected into crushed black except s4 — s2, s3, s5,
s6, s7 all sit in a 28.8–32.4 YAVG band with 21–29 levels of spread, which is the
band s1 and s7 occupied in round 1 when the editor called them "the two frames that
survive the grade".

## s4 — the blocker that changed direction instead of clearing

`.src` is `single brown envelope on a black background studio light@pexels`. The
delivered file is a macro flat-lay of **several overlapping kraft envelopes on a
black ground** — warm, textured and perfectly legible at full resolution.

On screen it is not an envelope. It is a set of dark grey diagonal wedges on black.
No flap, no seam, no closure, no single object; the one envelope-shaped feature (a
perforated dashed line, lower left) is a hairline in shadow. Sound-off, against
1.4's *"You just reached a number"*, the frame says nothing — which is the same
verdict attempt 1 returned, arrived at from the opposite end of the histogram.
Round 1 was a **grey slab**; round 2 is a **black slab**.

**The cause is measurable in the source, before any render.** Source-file luma:

| src | YAVG | YHIGH |
|---|---|---|
| s1 | 144.14 | 244 |
| s2 | 92.21 | 162 |
| s3 | 56.51 | 134 |
| **s4** | 59.43 | **93** |
| s5 | 109.23 | 160 |
| s6 | 80.10 | 203 |
| s7 | 70.91 | 180 |

s4 is **the only source of the seven whose 90th-percentile luma never reaches
mid-grey**. Its ceiling of 93 becomes 27 after `brightness(.62)` plus `.has-photo`'s
38% tint. Note it is *not* the darkest source by average — s3 is darker at 56.5 and
survives, because s3 has a specular ceiling of 134 to spend. **Average brightness is
not the predictor; the highlight ceiling is.**

Proposed promote-time rule, in the same family as the aspect-ratio check
`fin-assets` added in attempt 3: **under the locked grade a candidate needs source
`YHIGH ≳ 130` to render as an object.** Every scene that reads in this chapter
clears it; the one that does not is the one that fails. It costs one `ffprobe
signalstats` call per candidate and it is checkable before a file is ever promoted —
this is the "correct default, not a blocking gate" shape.

The swap direction that follows: an envelope shot with a **light source on it** —
a bright flap edge, a window highlight across the paper, a hand holding it — or drop
the envelope and take an object that carries its own bright element (a passbook page
under a lamp, a milestone marker).

## The three items the rework owned — verified from the encoded frames

**1 · s3's Lottie — the ₹/₣ blocker. CLEARED.** Read at 1:1 and again at 8× nearest-
neighbour from the encode at t=12.250, crop `120×120+640+760`:

- **Exactly ONE glyph**, in the app-mark square. The amount bar is a plain solid bar
  flush-left with the title — the second glyph the 06:13 source drew is gone, and
  the pre-glyph `AMT_X/AMT_W` geometry is restored.
- **The glyph is ₹, not ₣.** Two full-width horizontal bars, a left stem, a bowl
  that closes back to the stem, one diagonal leg descending right. **There is no
  third bar.** That is the U+20B9 skeleton and it cannot be read as ₣ / ₱ / F.
- **The open loop survives, exactly as declared (§8).** The title bar and the amount
  bar are both featureless rounded rects — no digits, no legible figure. The phone
  is still face-down. The card now says MONEY without saying HOW MUCH, which was the
  whole and only brief.

**2 · s7 — loaded balance. CLEARED, with one note.** A brass hanging pan loaded with
pale contents, its chain rising out of frame, on dark wood. Checked at both ken
extremes (`ken` true → tightest at scene end):

- The **pan and its contents survive the grade** and are the brightest thing in
  frame at both extremes (YHIGH 42, second only to s6).
- The **counterweight survives the crop** at both extremes — it is the hanging brass
  element at the far left, plus a small pale dish at lower left.
- *Note for the editor:* at the tightest framing (t=34.5) the counterweight sits in
  the outer ~6% of frame and is clipped by the left edge. It is present, and the
  "two things together" reading holds — but it is carried more by the small pale
  dish at lower left than by the counterweight itself. Not a defect; a taste call
  the editor may want to make on a re-crop.

**3 · s6 — re-crop. CLEARED.** `ken` direction is still `false` in index.html
(`ken("#s6-bg", S.s6, D.s6, false)`), so the alternation i/o/i/o/i/o/i holds. At the
WIDEST framing (t=29.000, scene end) the stair treads still own the centre of frame
and the bright gap at the top is still in shot. **The pull-out does not widen back
onto rock** — YHIGH is 45 at both extremes, the highest in the chapter after s1,
which is the bright gap surviving. Round 1's "dark ravine" read is gone.

**s2 — CLEARED.** Window frame, mullion, out-of-focus bokeh street behind, chai
glass with visible steam on the sill, warm wooden posts left and right. The
storyboard spec ("steaming on a windowsill, morning street out of focus behind") is
now met and the white-marble high-key failure is gone. One observation, not a
defect: the window light itself is **cool** (SATAVG 2.86, hue in the blue band), so
the frame reads night-into-dawn rather than §10's "warm first light". The wooden
posts carry what warmth there is. Editor's call.

## s5 — clears the grade, but only answers one third of its own line

The new file is `jars of rice and lentils on a wooden kitchen shelf warm light`:
three glass jars (dark seeds, lentils, white flour or salt) on a shelf under a
wooden tray. It **passes the grade test** — YAVG 32.4, contents legible, an object
not a panel — and it kills the round-1 office-desk / paperwork-backlog read cleanly.

But the line and the on-screen copy are **"Electricity. Ration. Rent."**, and the
frame carries **ration only**. No electricity, no rent. The editor's blocker #1 asked
for "three household papers fanned on a home table — an Indian electricity bill, a
kirana slip, a rent receipt"; what shipped is a different object satisfying one of
the three nouns. Raising it because the blocker was written against the count of
three, not against the desk: this is a content call and **`fin-editor` owns it**, not
this stage.

## Confirmed still holding from round 1

- **Frame count exact** against the declared length — 1073, no drift.
- **No black segments** anywhere in the 35.767s.
- **No rail anywhere on screen.** All seven scenes read at full resolution: no top
  rail, no chapter title, no scene counter, no slide number. The only two matches for
  `rail` in index.html are both inside the comment at lines 23–24 that says there
  isn't one. The single persistent mark is `#root.cut-hi::after`, the
  @cashguruguides watermark bottom-right — brand mark, not a chapter indicator.
- **Seven distinct photographs**, seven distinct md5s, no reuse.
- **Type legible on all seven** — white over scrimmed dark ground throughout; s7's
  foot still fits on one line.
