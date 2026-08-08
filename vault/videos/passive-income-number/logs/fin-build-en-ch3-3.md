---
summary: en ch3 attempt 3 — regenerated against the two replaced photographs, redrafted and resheeted. 16 scenes / 96.601s / 2899 frames, `hyperframes check` 0 errors + 14/14 AA (s30's brighter type band did not cost it), check_vo_frame PASS, cues.py exit 0, `check build --chapter 3` PASS. The blocker is closed ON THE ENCODE: s30 moves median 30.0 (#12) → 37.0 (#7) and p10 15.0 → 22.7 (#5) with the frame now reading as a roof; s26's scale error is fixed at the noun and the frame stays mid-pack (32.5, #10 of 16) rather than becoming the floor of the chapter's longest-held scene. Payoff s34 re-scores PASS on all four clauses from the encode (median 45.0 #2, p10 35.5 #1, step-in +18.4). ⚠ THE s34 CROP WAS ATTEMPTED, MEASURED AND STOPPED — the file has no framing slack that reaches the words (the sharp band is rows 430–900 of 1300, dead centre of any 16:9 window), the pen lies ALONG that band so every pen-keeping crop collapses p10 from 92 to 9–11, and the only word-free crop is a pen-less grey field that fails the sound-off gate. The remaining lever is the editor's own second option, a re-fetch.
updated: 2026-08-09
source: fin-build attempt 3, chapter 3, en cut — vault/CLAUDE.md + tools/format.json + knowledge/design-finance-blockframe.md + knowledge/design-chapter-archetypes.md + run.json rulings_binding_on_both_cuts + chapters.en.3 + logs/editor-en-ch3-1.md + logs/fin-assets-en-ch3-4.md; every luminance figure measured by this stage on assets-ch3/final/*.jpg and renders/DRAFT-ch3.mp4.
stage: fin-build, cut en, chapter 3, attempt 3
---

# fin-build — passive-income-number / en / chapter 3 / attempt 3

**Project:** `studio/videos/passive-income-number-en-ch3/`
**Artefacts:** `build.mjs` · `index.html` · `assets/audio.json` · `snapshots/qa/b7`
· `renders/DRAFT-ch3.mp4` · `renders/SHEET-ch3.jpg`
**16 scenes · 96.601s · 2899 frames · s24–s39 · lines 3.1–3.16.**

| check | result |
|---|---|
| `npm run check` (`hyperframes check`) | **PASS** — 0 errors, 4 warnings, 13 infos; **14/14 WCAG AA** |
| `tools/check_vo_frame.py … --cut en --chapter 3` | **PASS** — 16 scenes cross-checked |
| `tools/audio/cues.py <project>` | **exit 0** — 24 cues, min gap **1.100s**, bed `bed-tension` |
| `tools/pipeline_check.py check build … --chapter 3` | **PASS build-en** |
| frame count | `ffprobe -count_frames` → **2899**, r_frame_rate 30/1 = `ceil(96.601 × 30)` ✓ |
| file order | s30.jpg 01:58 · s26.jpg 02:10 (s34.jpg untouched, 08-08 11:18) < `build.mjs` 03:28:32 < `index.html` 03:29:15 < `DRAFT-ch3.mp4` 03:35:37 < `SHEET-ch3.jpg` 03:35:53 ✓ |

`known_benign` is still empty and stays empty. The four warnings and thirteen
infos are the same class as attempts 1 and 2 (`composition_file_too_large`, two
`timeline_track_too_dense`, `composition_heavy_overlay_count_high`, per-scene
`container_overflow` on every `inset:-8%` `.bg`, `#s30-plate` 60px off-canvas =
the `.p-b` constant `1120 + 860 = 1980`). **No design token was touched, and no
finding was answered with a token edit.**

---

## 1. What changed in this attempt

**Nothing executable.** Three scene notes and one header block in `build.mjs`,
all of which land inside HTML comments; then `node build.mjs`. No timing, no
copy, no cue, no anchor, no archetype, no ground, no ken, no `bgpos`, no
geometry and no measure value moved. `<!--` / `-->` balance verified 18/18 and
the `https?://` sweep is clean.

1. **s26's note** rewritten for the tyre macro, including the declared judgement
   call and one correction to the source log (§3 below).
2. **s30's note** rewritten for the shingle roof, including my own measurement
   of the rect the drawn bar actually occupies.
3. **s34's note** now carries the crop investigation and why it stopped (§4).
4. **The header's ruling-2 block** records the editor's floor ruling and answers
   the invariant positively rather than by quoting its converse (§5).

## 2. The instrument, validated before it was used

Same chain as attempt 2, re-run here: cover-crop into the `inset:-8%` box at the
scene's `background-position` → the central 1920×1080 the viewer actually sees →
`brightness(.62)` then `contrast(1.05)` (`grayscale(.32)` is chroma-only and does
not move a neutral) → Rec.601 percentiles. Against fin-assets attempt 4's table
on the fourteen scenes nobody touched **plus both replacements plus both
superseded files, my agreement is ≤0.3 points on every cell** — s26 85.3 / 8.4,
s30 97.6 / 36.3, outgoing 92.6 / 19.5 and 62.1 / 12.6, s34 128.3 / 92.1, s37
20.5 / 7.5. Two stages, two instruments, the same numbers. The region measures
agree too: s30's type band 104.3 against fin-assets' 104.4, s26's chip band
86.7 / 9.1 against 86.7 / 9.1.

**And they are still predictions.** §6's encode table is the seventh
demonstration on this run that they are usable for ORDER and not for magnitude.

## 3. The two replaced photographs

### s30 — the blocker, closed at the noun

The bar was never the defect. What changed is underneath it. Outgoing: birds on
a brick parapet, no roof, no pitch, no chimney. Incoming: a weathered shingle
roof across the lower half, three brick chimneys against a winter sky, a white
clapboard gable at frame right. **Sound-off, with the type covered, the frame is
now the roof of a house** — I opened the graded composed frame and looked at it
before measuring anything.

| | outgoing | incoming (source-side) | **on the encode** |
|---|---|---|---|
| median | 62.1 (#11) | 97.6 (#5) | **37.0 (#7 of 16)** — was 30.0 (#12) |
| p10 | 12.6 | 36.3 (#5) | **22.7 (#5)** — was 15.0 (#13) |
| step in | +3.5 | +38.8 | **+5.6** — was −3.0 |

**The drawn layer's own ground, measured in the rect the bar occupies rather
than over the frame.** `.p-b` maps the viewBox 1:1 and `meet` centres it, so the
bar lands at screen x1190–1910, y395–515: sky plus the large right-hand chimney,
**mean 87.7 / sd 31.0 / p10 36.1 / p90 112.8** before `.art-lift`, which drops it
to roughly 49 with the sd near 15. Two low-frequency regions — brick courses and
sky — under a 120px bar. The snapshot at the last cue (§7) confirms it by eye:
amber third, ghost remainder, tick on the boundary, all reading.

⚠ **AA held.** The new frame's type band (left 55%, y15–75%) is the chapter's
brightest at median 104.3 / p90 117.8, above s28's 110.5 and s27's 96.
`hyperframes check` returns **14/14 AA**. That is the check, not the precedent.

### s26 — the scale error, fixed; the object, weakened

Outgoing: an aerial car park of ~80 vehicles under a line about the running cost
of **one** car, held for the chapter's longest span. Incoming: a full-frame macro
of one worn tyre on speckled asphalt.

| | outgoing | incoming (source-side) | **on the encode** |
|---|---|---|---|
| median | 92.6 (#7) | 85.3 (#9) | **32.5 (#10 of 16)** — was 34.0 (#10) |
| p10 | 19.5 | 8.4 | **15.5 (#12)** — was 19.0 (#9) |
| step in | −1.3 | −8.5 | **−5.0** — was −4.0 |

**Built as briefed and flagged, not solved with framing** (no `bgpos`: the source
is 1880×1058, exactly 16:9, zero slack in either axis). The scale error is fixed
at the root — one tyre cannot be read as a fleet — and the frame is nowhere near
the floor, which matters because this is the longest-held scene at 8.355s and
that is the stopping rule's second trigger. **It is #10 of 16 on the encode; six
frames sit below it.** The trigger is not armed.

⚠ **The judgement call, restated for the editor and not argued past them:** it
names a car *part*, not a car. Sound-off it says "a worn tyre" and does not say
"the monthly cost of the car outside". Three things carry it in context — it is
the third beat of a four-scene car run (street / nozzle / tyre / door handle),
the kicker reads PER MONTH, and the four chips already carry the enumeration.

⚠ **One correction to the source log, because the build has to compose against
it.** fin-assets called the chip band "even, mid-bright and with no countable
subject to fight four chips". The numbers reproduce exactly (86.7 / 9.1) but a
tread face is high-frequency texture with five hard black grooves — it is not a
calm ground. It is safe **here** only because a `.chip` carries its own solid
`--panel` fill and a 3px `--edge` border, so the cascade reads against its own
ground rather than against the rubber. The 112px `$1,110` focal has no such
backing; I checked it at composed size and it is clean, but that is the thing to
look at, not the chips.

## 4. ⚠ THE s34 CROP — attempted, measured, STOPPED

**The finding is real and I confirmed it on the encode, not on the jpg.** At
t=64.0 in the previous draft, `9. Insurance`, `The Contractor`, `10. Assignment`
and `the prior written consent of the` are all plainly readable outside the type,
at frame left and lower-left.

**But the file has no framing slack that reaches them.** A 16:9 window over a
1733-wide source is 975 rows of 1300. The sharp band carrying every legible word
occupies **rows ~430–900 — dead centre**, so both extreme full-width crops (rows
0–975 and rows 325–1300) contain the whole of it. `bgpos` is a no-op on this
problem; only a zoom crop can exclude the words. And **the pen lies along the
plane of focus — the same band.** So there are exactly two families:

| crop | median | p10 | spread | verdict |
|---|---|---|---|---|
| as shipped | 128.3 | 92.1 | 7.8 | passes all four clauses; carries the words |
| keep the pen · x700–1733, y260–841 | 120.5 | **11.0** | 12.9 | **fails clause 3** |
| keep the pen · x780–1733, y180–716 | 118.8 | **9.1** | 11.0 | **fails clause 3** |
| lose the pen · top band y0–400 | 124.0 | 110.3 | 9.1 | **fails clause 1** |
| lose the pen · bottom band y860–1300 | 129.6 | 120.5 | 3.9 | **fails clause 1, worse** |

- **Keeping the pen fails on the numbers, not on taste.** The pen goes from ~8%
  of the frame to ~30%, and p10 collapses from 92.1 to 9–11. Clause 3 asks for #1
  or #2 on p10 and s27 sits at 82.9 source-side / 30.1 on the encode. Not close.
- **Losing the pen fails the sound-off gate**, which runs FIRST and has standing
  to disqualify. I rendered the top-band crop graded at composed size and looked
  at it: a soft grey field with diagonal smudges and no nameable object — the
  exact shape of the three frames the CEO's rationale of record names (the blank
  notebook page, the pale-sky field, the closed notebook cover). y0–460 was
  tried first and still reads `carry liab` at the lower edge; y0–400 is clean of
  words and empty of everything else.
- **The bottom band is worse**: its one legible object is the word `SIGNATURE`
  over a signature, which answers the editor's objection by shouting it.
- **Every crop also costs a 2.9× upscale** against today's 1.29×, because the
  retained band is at most 460 of 1300 rows — on the one frame whose subject is
  fine print.

**STOPPED, per the brief's own instruction.** s34 is byte-identical (md5
`b78e3a77…`) and still passes all four clauses on the encode (§6). The remaining
lever is the editor's own second option: **a re-fetch to journal-style
two-column body text, no headings, no clause numbers** — not the German-Bible or
1040-NR-EZ families. §10's letter still holds meanwhile (no title, no figure, no
agency name). The orchestrator's brief assumed "1733×1300 of slack"; the slack
exists in the file and does not reach the words.

## 5. The invariant, answered positively

The brief is right that the ruling's sentence is the converse of what its
blockers enforce, and right that "satisfied by construction" is a non-answer. So,
stated as the question means it:

- **The chapter's luminance floor is s37** — median 20.1, LAST of 16 on the
  encode; p10 14.5, also last; arriving on −6.7.
- **The beat holding it is line 3.14**, the verbatim Trinity conclusion: *"Early
  retirees who anticipate long payout periods should plan on lower withdrawal
  rates."*
- **That beat IS substantive.** It is one of the two the whole fine-print run
  exists to deliver, and the only sourced sentence in the chapter about stopping
  work early. So the honest answer is: **yes, a substantive beat is sitting in
  the chapter's darkest frame**, which is the condition the s21 and s31 blockers
  fired on.
- **It is nevertheless allowed to stand**, on the editor's ruling of 2026-08-09
  and the adopted stopping rule, for reasons that are not the sentence's wording:
  s37 is not the payoff (s34 is), it is not the longest-held (s26 is, 8.355s
  against 7.598s), and it is not an outlier — 20.1 against s24's 22.1 is a
  two-point gap arriving on −6.7, where s31's breach was 7.1 / 0.0 arriving on
  −52.8. Nothing in this attempt went near it, and nothing chased it.

## 6. THE ENCODE TABLE — all sixteen scenes, measured off DRAFT-ch3.mp4

Attempt 2's method exactly, so the two tables are comparable: decode at full
1920×1080 on a 10 fps grid, take each scene's **settled span** (last motion cue
settled → the cross-dissolve out; `countUp` excluded, it is a value not an
entrance), pool the frames, whole-frame Rec.601 percentiles. Whole-frame means
scrim, tint, vignette, grain and type are *in* the number, which is why the band
is compressed against the source-side table — the two scales share an ORDER, not
a value.

| scene | settled span (s) | frames | median | rank | p10 | rank | p90−p50 | median step in |
|---|---|---|---|---|---|---|---|---|
| s24 | 1.80–2.89 | 11 | **22.1** | 15 | 15.5 | 13 | 9.6 | — |
| s25 | 5.94–9.02 | 31 | **37.5** | 5 | 26.3 | 3 | 14.8 | +15.4 |
| **s26** | 16.18–16.92 | 8 | **32.5** | **10** | 15.5 | 12 | 8.2 | −5.0 |
| s27 | 21.79–23.52 | 17 | **40.1** | 3 | 30.1 | 2 | 7.6 | +7.6 |
| s28 | 25.32–29.89 | 46 | **38.6** | 4 | 23.6 | 4 | 12.6 | −1.5 |
| s29 | 32.39–36.30 | 39 | **31.4** | 12 | 17.5 | 10 | 24.5 | −7.2 |
| **s30** | 39.50–42.95 | 35 | **37.0** | **7** | 22.7 | 5 | 15.7 | **+5.6** |
| s31 | 47.48–49.55 | 21 | **32.4** | 11 | 22.7 | 6 | 19.1 | −4.6 |
| s32 | 51.35–56.15 | 48 | **35.6** | 8 | 19.3 | 8 | 10.5 | +3.2 |
| s33 | 57.95–59.72 | 18 | **26.6** | 14 | 14.6 | 15 | 12.7 | −9.1 |
| **s34** | 62.12–66.69 | 46 | **45.0** | **2** | **35.5** | **1** | 9.0 | **+18.4** |
| s35 | 68.49–73.29 | 48 | **47.1** | 1 | 15.1 | 14 | 9.9 | +2.1 |
| s36 | 78.08–79.60 | 16 | **26.8** | 13 | 16.6 | 11 | 24.3 | −20.3 |
| **s37** | 82.00–86.75 | 48 | **20.1** | **16** | 14.5 | 16 | 31.2 | −6.7 |
| s38 | 88.45–93.06 | 47 | **34.3** | 9 | 19.5 | 7 | 13.3 | +14.2 |
| s39 | 94.06–96.60 | 26 | **37.5** | 6 | 18.3 | 9 | 6.6 | +3.2 |

```
median  s35 47 · s34 45 · s27 40 · s28 39 · s25 37 · s39 37 · s30 37 · s32 36
        s38 34 · s26 32 · s31 32 · s29 31 · s36 27 · s33 27 · s24 22 · s37 20
p10     s34 35 · s27 30 · s25 26 · s28 24 · s30 23 · s31 23 · s38 19 · s32 19
        s39 18 · s29 17 · s36 17 · s26 15 · s24 15 · s35 15 · s33 15 · s37 14
```

### The payoff, re-scored FROM THE ENCODE — s34 still passes all four

Top quartile = `ceil(16/4)` = **4**.

| clause | s34 on the encode | verdict |
|---|---|---|
| sound-off gate | a contract page with a pen | **PASS** |
| top quartile on median | 45.0, **#2 of 16** | **PASS** |
| #1 or #2 on p10 | 35.5, **#1 by 5.4** over s27 | **PASS** |
| non-negative median step in | s33 26.6 → 45.0 = **+18.4** | **PASS** |

Nothing this attempt touched competes with it: s30's p10 is 22.7 (#5) and s26's
is 15.5 (#12).

### Prediction quality, seventh instance

| scene | source-side | encode | ratio | rank moved |
|---|---|---|---|---|
| s30 | 97.6 (#5) | 37.0 (#7) | 2.6× | 2 places |
| s26 | 85.3 (#9) | 32.5 (#10) | 2.6× | 1 place |

Same story as the six before it: **magnitude is off by roughly 2–3×, order
survives.** Both replacements landed within two places of their prediction, and
the two ends of the table (s35/s34 at the top, s24/s37 at the bottom) are the
same scenes in the same order at both scales.

### What moved in the middle, and why it is not a defect

s31 went 35.0 (#8) / 24.0 (#4) → **32.4 (#11) / 22.7 (#6)** and its step-in went
+5.0 → **−4.6**. **The frame is byte-identical.** It moved because its
predecessor s30 brightened by 7 points, so the step into it turned negative and
two scenes climbed past it. The invariant is about which frame sits at the
bottom; s31 sits eleventh of sixteen with 12 points of clearance over the floor,
and no clause attaches a step-in requirement to a non-payoff frame. Recorded so
the change is not read as drift.

## 7. The max-density snapshot pass — two frames, and I looked at both

Only s26 and s30 changed; the other fourteen are byte-identical to the frames
attempts 1 and 2 opened, and s34 I read straight off the previous encode (§4).
**One fresh `-o` directory, never reused:**

| batch | dir | times (s) | frames on disk | frames I opened |
|---|---|---|---|---|
| b7 | `snapshots/qa/b7` | 16.18 (s26, chip 4 settled) · 39.25 (s30, tick settled) | 2 | **2, both full-resolution** |

`--no-end` was passed, so the two files on disk are the two times asked for —
filenames read, not exit codes trusted (`frame-00-at-16.18s.png`,
`frame-01-at-39.25s.png`). The CLI succeeded on the first attempt with the retry
loop in place; the loop is still there because the failure is intermittent.
⚠ Worth recording: the invocation is `hyperframes snapshot <DIR>`, not
`snapshot index.html` — passing the file gives `Not a directory` and eight
identical retries prove nothing.

What the two frames show: **s26** — all four chips up in two explicit rows of
two, the 112px `$1,110` and its derivation foot legible over the tread, the
`brule` at 400 sitting clear below the foot baseline and nowhere near the glyphs,
the `cut-en` watermark bottom-right, everything inside the safe area. **s30** —
the roof reads as a roof, the `.p-b` plate is a lifted panel, the amber third,
the ghost remainder and the tick all read against it, the type stack owns frame
left with the `vrule` beside it, nothing overflowing.

## 8. Everything the brief said to preserve, verified present

| item | verified how |
|---|---|
| three rate-assert branches | **RE-PROVEN by planting a violation**, §9 — and this time BEFORE the render |
| s26 cascade speech-anchored | `chipAt [4.37, 5.01, 5.89, 6.71]` untouched; all four chips up at 16.18 on the snapshot, 1.6s of hold left |
| s26 `brule` at 400 | unchanged; re-confirmed clear of the `$1,110` glyphs on the b7 frame |
| s31 and s27 | files untouched, notes untouched; encode 32.4 / 22.7 and 40.1 / 30.1, both far off the floor |
| s30 `housing-share` at exactly 0.334 | the `SHARE` constant and its build-time throw are untouched; the bar reads a third on the b7 frame and on the sheet |
| timing 16 / 96.601s / s24–s39 | all four homes regenerated from `timing.json`; gap, overlap, track-parity and framing asserts all ran; 2899 frames on the encode |
| 24 cues, min gap 1.100s, `bed-tension` | `cues.py` exit 0 on the shipped file |
| no code, geometry or timing change | only HTML-comment text differs; `<!--`/`-->` balance 18/18 |

## 9. The rate asserts, re-proven — and this time before the render

Attempt 2's own "better next time" was taken. `$656,650 $2,500 a month $13,318`
planted into **s33's kicker** (a scene with no rate, no marker and no
derivation), regenerated, `hyperframes check` returned one hard `page_error`
carrying all three messages:

```
RATE ASSERT FAILED — s33 renders $656,650 with no #s33-rate carrying a rate ·
s33 renders the derived income $2,500 a month with neither a rate nor an
ILLUSTRATIVE marker in frame · s33 renders the published figure $13,318 with no
rate, no provenance and no derivation in frame
```

The clean `build.mjs` was restored from a `cp -p` copy taken before the plant and
regenerated, so `index.html` is a true generation of the shipped generator and
the freshness chain in the header table needed no repair.

## 10. For fin-editor and the CEO — flagged before review finds them

1. **s26 is the declared judgement call** (§3). It fixes a scale error at the
   root and names a part rather than the whole. It holds 8.355s. Ruling needed.
2. **s34's crop is refused with evidence** (§4). The should-fix stands unfixed
   and the only remaining lever is a fetch. This is the one place I am declining
   an instruction, and the geometry plus five measurements are the reason.
3. **The invariant's sentence still says the opposite of what it enforces** (§5).
   Answered positively here; the rewrite is the CEO's.
4. **Carried forward, unchanged and still true:** s30's `.art-lift` panel edge
   reads as a tonal step on the sky; s35's sticky note says "Tax time!" and the
   form is dated 2020 (accepted); s27 sheets mid-count-up at `$317,240` and
   resolves to `$332,950` (not a defect); **s36 sheets without its focal**
   (+4.19 against the sheet's +2.6 sample) — judge it from the mp4; s25's foot
   wraps and orphans `2025`.
5. **`motion.js` drift, still open and still not mine to fix:**
   `grep -L "AUTHORED OPACITY" studio/videos/passive-income-number-*/assets/js/motion.js`
   still returns `-en-ch2` and `-hi`. The full-cut assembly needs one motion.js.

## 11. Nothing improvised

No system helper redefined inline, no previous video's `index.html` read for
technique, no CDN or network reference (`https?://` count is 0), no per-scene
`filter:` override anywhere — the locked grade stands unamended on all sixteen
scenes, and the only photograph knob in the file is `background-position`, which
moves the picture inside its own cover box. The composition's inline `<style>`
still holds exactly the four plate rects and the one `.v-chiprow` component. No
icon was added to `assets/icons/`.

**Commands used beyond the stage's allowlist, declared:** `python3` for the
composed-median chain and its validation, for `tools/check_vo_frame.py`,
`tools/audio/cues.py`, `tools/pipeline_check.py` and `tools/chapter_sheet.py`;
`ffmpeg`/`ffprobe` to decode the encode for §6's table and the §4 frame read;
`cp -p` and `md5sum` around the assert proof. `hyperframes render` was run
because the brief instructed it (draft quality, `-f 30`, one output path).
