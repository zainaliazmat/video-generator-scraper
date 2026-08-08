---
summary: hi ch3 built — 9 scenes s22-s30, root 61.143s at offset 124.007s, timings byte-exact from timing.json with gap asserts, one drawn layer (corpus-doubles at s28) with both declined alternatives written down, all five guard branches proven to throw by planting violations. THE PAYOFF CLAUSE FAILS ON THE ENCODE: s27 is #4 of 9 on median and #3 of 9 on p10, measured on every frame at full resolution across four span definitions — but the top four frames sit inside 0.39 points and the top three inside 0.06, so the chapter is tonally flat at the top rather than the payoff being dark. Two composition-side framings changed on the snapshot evidence: a declared window on s22 (the opening frame failed the sound-off gate at its own scene open) and s24's countUp 0.45 -> 0.30 (the review sheet was printing a figure that appears nowhere in the video).
updated: 2026-08-09
source: measured from studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4 (1835 frames, 30fps CFR) + timing.json (MEASURED, Amrut, 519.331s) + faster-whisper word timings on this cut's own 3.1/3.3/3.6 clips + fontTools against the shipped woff2 at weight 900
stage: fin-build, cut hi, chapter 3, attempt 1
---

# fin-build — passive-income-number hi ch3, attempt 1

Scenes **s22–s30** (lines 3.1–3.9), the second rung. Project
`studio/videos/passive-income-number-hi-ch3/`; generator `build.mjs`, emitted
`index.html` + `assets/audio.json`.

**Root 61.143s · offset 124.007s** (= ch2's offset 42.475 + ch2's own root
81.531, so the three built chapters abut frame-exact) · 9 scenes · draft **1835
frames** against `ceil(61.143 × 30) = 1835`.

---

## 1 · THE CONTAINER LADDER — and the two stale places, named

Applied as ruled (`run.json rulings_binding_on_both_cuts.container_ladder_2026-08-09`):
**four rungs, s22 → s31 → s58 → s62, starting here.** s22 is briefed and
commented as rung one **in its own right**; the words "bigger than s16" appear
nowhere in `build.mjs` or `index.html`, and ch2 is described where it is
mentioned as **rung 0** — money with no container (one ₹5 coin at s9, loose
notes at s16).

**The stale row is in §10 ("The returning objects"), not §12** — §12 is
transitions and timing and carries no ladder row. That row is stale in exactly
two places:

| # | what the row says | why it is wrong |
|---|---|---|
| **1 · membership** | `s16 (2.8) · s22 (3.1) · s31 (4.1) · s58 (6.1) · s62 (6.5)` — **five** rungs, starting at s16 | the ruling has **four** and s16 is off the ladder entirely; it is pinned by the payoff clause, the serial constraint and §8's no-drawn-layer rule |
| **2 · s22's own cell, and its comparator** | "notes in a box → **two cash boxes** → a steel trunk…", and "**Each visibly bigger than the last**" | the shipped file is **ONE carved sheesham money box** with a brass coin slot, not two steel boxes (fin-assets §4.1: ten sheets, ~60 cells, no buyable steel cash box that is not euro-denominated) — and with s16 gone there is no predecessor for s22 to be bigger than, so the comparator clause has nothing to compare against at rung one |

⚠ **A third place, outside the row and outside this chapter's scope:** §9c
repeats the same dead five-rung list in prose ("a cash box (s16) → two cash
boxes (s22) → a steel trunk (s31) → a bank locker (s58) → a safe door (s62),
each container visibly bigger than the last"). ch4 reads that sentence for s31.

---

## 2 · THE PAYOFF CLAUSE — scored from the ENCODE, and it FAILS

**Payoff scene: s27 (3.6, THE RATE HELD, `num 3.0%`)** — fin-assets' nomination,
accepted on the merits: it is the chapter's thesis, its longest scene (8.976s),
the only scene taking `pop`, and the only content `stamp`.

**Method.** Every frame of each scene's SETTLED span (scene start + 0.55, so the
incoming cross-dissolve is excluded, to scene end − 0.05), full 1920×1080,
BT.601 gray, **complete population — 1,752 frames across the chapter, not a
sample.** 8-bit quantisation removed by in-bin interpolation; without it three
scenes tie at an integer 31 and the rank flips on nothing. Composed frame
(type included), which is what the ch2 editor and CEO both measured.

| scene | line | ground | **MEDIAN** | **p10** | **p90 − p50** | median step in | held | sound-off: what a viewer names, type covered |
|---|---|---|---|---|---|---|---|---|
| s22 | 3.1 | `#1c2027` | **30.97** | 19.59 | 9.21 | — | 5.42 | a carved wooden money box with a brass coin slot |
| s23 | 3.2 | `#17291f` | 24.47 | 14.01 | 24.18 | −6.50 | 6.13 | an abacus |
| s24 | 3.3 | `#17291f` | 26.94 | 15.24 | 24.10 | +2.46 | 6.05 | the same abacus, tighter |
| s25 | 3.4 | `#1f1e1c` | 30.94 | 15.50 | 12.43 | +4.00 | 6.78 | an old metal desk fan |
| s26 | 3.5 | `#291f13` | **19.49** | 15.18 | 15.54 | −11.45 | 8.22 | a rusted kWh meter, KILOWATT-HOURS legible |
| **s27** | 3.6 | `#2a2113` | **30.91** | **19.74** | 18.79 | **+11.41** | **8.98** | a wooden rubber stamp and a numbering stamp on a counter of forms |
| s28 | 3.7 | `#1a1e24` | 27.91 | 18.75 | 14.74 | −3.00 | 8.51 | a two-pan brass balance |
| s29 | 3.8 | `#2b1418` | 28.94 | **21.96** | 12.94 | +1.03 | 5.40 | horn loudspeakers on a pole |
| s30 | 3.9 | `#1f1e1c` | **31.30** | 19.97 | 20.49 | +2.36 | 5.66 | a bullock cart at rest |

    MEDIAN  s30 31.30 · s22 30.97 · s25 30.94 · s27 30.91 · s29 28.94 · s28 27.91
            · s24 26.94 · s23 24.47 · s26 19.49
    p10     s29 21.96 · s30 19.97 · s27 19.74 · s22 19.59 · s28 18.75 · s25 15.50
            · s24 15.24 · s26 15.18 · s23 14.01

Duration-weighted chapter median **27.79**.

### The four clauses

| clause | requirement | result |
|---|---|---|
| **1 · sound-off gate** (binary, first) | name a concrete object with the type covered | **PASS** — a rubber stamp and a numbering stamp standing on a ruled form |
| **2 · MEDIAN top quartile** | `ceil(9/4)` floored at 3 → **top 3** | ❌ **FAIL — #4 of 9** (30.91). Behind s25 by **0.03** and s22 by **0.06**; behind #1 (s30) by 0.39 |
| **3 · p10 #1 or #2** | | ❌ **FAIL — #3 of 9** (19.74). Behind s30 (#2) by **0.23**, behind s29 (#1) by 2.22 |
| **4 · median step in** | s26 → s27 must not fall | **PASS — +11.41**, the largest step in the chapter |

**The rank is STABLE, so the failure is not a measurement artefact.** Re-measured
on four different span definitions — settled, mid (+0.90 to −0.50), late half,
and the whole scene including both dissolves — s27 is **#4 on median in all
four** and #3 or #4 on p10. The sign does not move.

**The p10 comparator escape does NOT apply.** The ruling waives the p10 clause
where the only frame above the payoff is an admitted near-flat host/backdrop.
The two frames above s27 are s29 (six horn loudspeakers, spread 12.94) and s30
(a bullock cart in a field, spread 20.49) — both real subjects with real
content. Neither is a host wall. I am not claiming the escape.

### What the numbers actually say, which is not "the payoff is dark"

**The top four frames sit inside 0.39 points and the top three inside 0.06.**
s30 / s22 / s25 / s27 are 31.30 / 30.97 / 30.94 / 30.91 — one band, four
different photographs. So a rank test over them is measuring nothing: the
ordering of s22, s25 and s27 is a coin flip at 0.03–0.06 points, and even the
leader's margin is 0.39. **The chapter's defect is that nothing at the top is
bright, not that the payoff is at the bottom** — the payoff is inside the top
band; it just is not first in it, and the band is 0.4 points wide.

**Levers, from the encode rather than from the prediction.** fin-assets wrote
"the lever is s25 on median and s28 on p10, in that order". The encode disagrees
on both:

- **On MEDIAN** the only frame with a real lead over s27 is **s30** (+0.39, the
  bullock cart); s22 and s25 are ties, not leads. Pulling either down moves s27
  from #4 to #3 or #2 on a 0.03-point edge — that is number-shuffling, and the
  ruling exists to forbid exactly it. **The move that resolves all three at once
  is bringing s27 UP**, i.e. a brighter, more evenly-lit stamp counter.
- **On p10** the one genuine gap is **s29** at 21.96 (+2.22). s30 at 19.97 is
  0.23 ahead, i.e. a tie. s28 — fin-assets' nominated p10 lever — is at 18.75,
  BELOW s27, and moving it does nothing.

**Prediction vs encode, seventh instance on this run.** fin-assets predicted
s27 at median 31.9 (#2 of 9) and p10 21.0 (#2 of 9), and declared its 1.6-point
and 1.2-point leads UNSAFE. It was right to. The absolute errors are small
(−0.99 median, −1.26 p10) but **both ranks inverted**, because the whole chapter
compressed into a 12-point band. Two other slots moved further: s30 predicted
28.9 (#6) and measured 31.30 (#1); s26 predicted 22.3 and measured 19.49. The
rule stands: a prediction shortlists, only the encode settles.

### Clause 1 (the invariant) and the STOPPING RULE — both satisfied

- **The floor is s26**, median 19.49 / p10 15.18, held 8.219s. That is line 3.5,
  «मई में जो बिल देखकर घर में बहस होती है…» — the chapter's LIVED CONSEQUENCE
  and its warmest ground, a rusted kWh meter with KILOWATT-HOURS legible.
- **Under the stopping rule this is NOT a defect:** the new bottom is neither
  the payoff (s27) nor the longest-held frame (s27, 8.976s). s26 is the
  second-longest, and it is a substantive beat, not a throwaway. I am not
  chasing it.
- No frame in the chapter fails the sound-off gate at its settled span: there is
  no blank wall, no pale-sky field and no closed notebook here.

---

## 3 · The opening-frame gate — and the one composition-side re-frame it forced

The hi ch2 ruling gave the sound-off gate **standing on the chapter's opening
frame**, and s22 is both that frame and rung one of the ladder. Snapshotted at
its own scene open (`snapshots/qa/b5`, t = +0.20) at the file's native `cover`
framing, **it failed**: a dark blur with one black diagonal bar and no nameable
object. Two things compound —

1. the file is **1880×740, aspect 2.541**, so `cover` on the 16:9 box already
   discards the outer 30% of its width and keeps the CENTRE;
2. s22's ken is `o`, so **the scene OPENS at its tightest** (scale 1.16) — and
   the centre of this particular macro is the out-of-focus middle of the lid.

**Fixed as a COMPOSITION edit, not an asset edit.** ch2's declared-window
mechanism is ported verbatim (`bgWindow` + the `jpegSize` SOF guard): an
explicit `background-size`/`background-position` expressing a **1297.78 × 730
window at source +40 +5**, so not one pixel of `s22.jpg` is rewritten and its
md5, its manifest row and its CREDITS entry all stand. What it buys is the
SHIFT, not a zoom: the sweep union moves from source x 282–1598 to x 40–1338,
which brings the **brass hasp** at the lower left permanently into frame beside
the brass slot plate. Two hard-edged brass fittings on a carved wooden lid is a
money box; a soft carved surface is not.

It bounds the **sweep UNION**, not one frame — the mistake that let ch2's serial
ship for 5.35s. At the tightest 1.16 the visible region is still x 128–1250,
y 57–683 and both fittings are inside it. Verified at both ends of the ken
(`snapshots/qa/b6`, t = +0.20 and +5.20). Trade, declared: 1298 source px
against 1316 full-bleed, so the upscale goes 1.459× → 1.479×. 1.4%.

⚠ **Left standing for the editor.** This is a shallow-DOF macro whose 2.54
aspect makes a 16:9 crop structurally unable to show the box's silhouette — the
widest legal 16:9 window is 1316 of 1880 px. The window is the ceiling for this
file; the only further lever is a re-fetch. The opening frame now passes the
gate, but it passes it NARROWLY, exactly as ch2's s9 did.

---

## 4 · The one drawn layer, and the two claims it was chosen over

**§8 grants chapter 3 exactly one and names it: `corpus-doubles` on s28 (3.7).**
Built in the `.p-b` plate's own coordinate space — `viewBox 0 0 860 610`, the
plate's exact w/h, so viewBox units map 1:1 to screen x and the gotcha-8 cliff
at **vx 800** is asserted in the generator rather than trusted.

The arithmetic is real and is the frame's whole claim:

    W2 / W1 = 336 / 168 = 2.000  =  ₹20,00,000 / ₹10,00,000
    W4 / W3 = 336 / 168 = 2.000  =  ₹5,000     / ₹2,500

The two pairs are drawn IDENTICAL because the ratio IS identical — that is the
line («दोनों तीन परसेंट पर») — with one rate rule under both, because the rate
is the thing that did not move. Each long block carries a 9px **notch** at its
own midpoint so "exactly twice" is checkable by eye, not only asserted in a
comment.

- **Additive under rule 8 by construction:** the photograph is an EMPTY, level
  two-pan brass balance. There is nothing in the picture to re-draw, and no
  sentence shows "the same ratio on both sides" at a glance.
- **The art carries NO figures** — labels are `CORPUS`, `A MONTH` and the rate.
  Printing all four amounts in the plate as well as in the focal would put every
  figure on screen twice in one frame.
- **Solid fills only**, nothing thinner than 9px, `.art-forward` (52%) +
  `.art-lift` + a `#s28-band` INSIDE the plate. Rule 9 holds absolutely: both
  darken behind the art inside the declared rect and neither can reach the
  photograph.
- **Not `popEach`, deliberately.** `cues.py` emits a `chip` per pop/popEach and
  §7 gives this scene a single `reveal`; three `fade` calls emit nothing and the
  reveal binds where the storyboard puts it, on the band. Assembled by **+3.30**,
  inside the +3.3 sheet mark.

**DECLINED IN WRITING, both at their own scenes:**

1. **A drawn ÷12 across the s23→s24 hold** (ch2 declined the same thing at the
   same joint). The division is already asserted three times in type: s23 prints
   the yearly line, s24 prints ₹5,000, s24's foot prints "₹60,000 divided by 12".
   A fourth statement is padding. Declined on necessity, not merit.
2. **A drawn "same stamp, three rungs" motif at s27.** Refused on two grounds,
   not deferred: the photograph IS a stamp mid-press, so a drawn stamp over it
   is rule 8's ghost-envelope failure by name; and a count of rungs is a rung
   COUNTER, which §3's no-rail rule forbids outright.

Asserted in the generator: `sc.filter(s => s.art !== "off").length !== 1`
throws, so a later edit cannot quietly add a second.

---

## 5 · Two findings the snapshot pass produced, and what each cost

**(a) The band was making the plate an opaque black card.** Built first at an
inline `height:100%`; `.art-lift`'s .66→.34 panel PLUS a full-height band turned
the declared plate into a black rectangle pasted on the photograph, with a hard
edge at the top corner — the aperture the archetype layer exists to give a photo
scene, gone (`snapshots/qa/b3`). Reverted to the class's own 54%
(`snapshots/qa/b4`): the lower pair and the rate rule keep the floor they need
and the bottom of the plate fades into the still.

Also load-bearing and found by reading the stylesheet rather than the render:
**`.band` is `z-index:1` and `.art` is `z-index:auto` inside a plate that is its
own stacking context**, so the band would have painted OVER the drawn layer
whatever the DOM order — the chapter's one mechanism hidden behind its own
backing, with every check green. Levelled with an inline `z-index:0`.

**(b) The review sheet was printing ₹4,820 — a figure that is in no frame of the
video and no source.** `tools/chapter_sheet.py` samples a countUp scene at
exactly **+4.50**; at `countDur 0.45` s24's roll finished at **+4.60**, so the
sheet caught it 0.1s short. **countDur 0.45 → 0.30**, landing the count at +4.45,
half a frame before the sample. Settled time goes 1.451s → **1.601s**, still well
over the 1.20s floor fin-editor set at ch2's s18. The spoken anchor (+4.15,
measured) does not move, the foot does not move, `timing.json` is not touched.

The distinction is the point and it is why s27 was NOT re-timed the same way:
s27 has no countUp, so the sheet samples it at +2.60 while its figure is
anchored at +2.95, and **its sheet cell is honestly empty**. An absent number is
an artefact a reviewer can be told about (ch2 recorded the same thing for s14's
mega); a WRONG number is a defect report waiting to happen.

---

## 6 · Timing, and the asserts that make a re-time throw

Every `data-start` / `data-duration` / `data-framings`, both JS maps, all nine
`<audio>` rows and the root are computed from `timing.json` and nothing is typed.

| scene | line | start | dur | d-dur | track | arch | ctr | ken | focal | num |
|---|---|---|---|---|---|---|---|---|---|---|
| s22 | 3.1 | 0.000 | 5.424 | 5.874 | 2 | A | centred | o | — | +1.90 |
| s23 | 3.2 | 5.423 | 6.129 | 6.579 | 1 | B | centred | hold 1 | 88 | — |
| s24 | 3.3 | 11.552 | 6.051 | 6.501 | 2 | B | centred | hold 2 | — | +4.15 |
| s25 | 3.4 | 17.603 | 6.782 | 7.232 | 1 | C | centred | o | 88 | — |
| s26 | 3.5 | 24.385 | 8.219 | 8.669 | 2 | A | centred | i | 88 | — |
| s27 | 3.6 | 32.604 | 8.976 | 9.426 | 1 | B | centred | o | — | +2.95 |
| s28 | 3.7 | 41.580 | 8.506 | 8.956 | 2 | B | **split** | i | 76 | — |
| s29 | 3.8 | 50.086 | 5.398 | 5.848 | 1 | C | centred | o | 88 | — |
| s30 | 3.9 | 55.484 | 5.659 | **5.659** | 2 | A | centred | i | 88 | — |

- Every non-final scene overlaps its successor by exactly **0.45s**; s30 carries
  its bare `scene_duration` because a chapter has no successor to dissolve into
  (`cut_assemble.py` adds it back). Tracks alternate 1/2 at every boundary.
- The **1 ms rounding at the s22→s23 joint** is timing.json's own (§12 names s23
  as one of the eleven): the gap measures 0.451 against 0.450 and is inside the
  0.005 assert. **`scene_start` is read, never summed forward.**
- **s27 is 8.976s against the 9.0s cap** — §6c's one-framing ruling with 0.024s
  of margin, and it holds only while 3.6 is not re-voiced. Asserted at build.
- Ken parity: `o i i o i o i o i`. The hold's direction is fixed by physics (the
  second file is a tighter crop; a tighter crop can only continue a push IN), and
  that fixes the whole chapter. The one repeat it forces lands on the **chapter
  joint** — ch2's s21 pulls back and s22 pulls back — which is where ch1→ch2 put
  its repeat too. Asserted.

**Anchors are MEASURED**, faster-whisper word timings on this cut's own clips,
with §5's character fractions used only as the cross-check they are declared to
be:

| line | word | measured into clip | scene anchor | what the storyboard said |
|---|---|---|---|---|
| 3.1 | «बीस लाख» | 0.780s | +1.03 → **floored to +1.90** | §5 predicted the floor for the same shape at s16 ✓ |
| 3.3 | «पाँच हज़ार» | 3.900s | **+4.15** | §5 fallback +4.34 (0.19s late) |
| 3.6 | «तीन परसेंट» | 2.700s | **+2.95** | ⚠ §6c's aside says "pop at +2.00" — **0.95s early**, and the measurement governs per §5 |

**No cascade in this chapter** — no scene enumerates anything, so
`tools/tts/clauses.py` has nothing to anchor and no `popEach` is emitted.

---

## 7 · Sound

`assets/audio.json` derived by `tools/audio/cues.py` from the emitted file, run
from inside `build.mjs` so the cue list and the markup come from one derivation.
**12 cues, bed `bed-resolve`, min gap 1.100s** against the 0.8s floor. The
s23→s24 joint is suppressed (declared hold) and s23/s24/s26/s30 take joints
only (the cut's `dry` table).

Two corrections the generator cannot make for itself, both storyboard facts,
both applied loudly in `build.mjs` and recorded in the file's `_hero` key:

- **s27 `hero` → `stamp`.** §2 lists s27 in the five-scene stamp set whose focal
  enters with `pop`; that entry IS the verdict slam. `cues.py` cannot know which
  pop is a slam and which is an arrival.
- **s22's derived `hero` DROPPED.** §7 row 22's sfx column is `—`, and §2 is
  explicit: s16, s62 and s64 ring and *"no other rung rings. If every rung gets a
  hero the ladder has no shape."* s22 is a rung.

⚠ **The cut's shared `cues-tables.json` was deliberately NOT edited** to encode
s22's silence. That table is §2's prose list verbatim; s22's silence is a
per-scene fact from §7's row. Putting one section's fact into the other
section's file is how the two drift. The consequence, declared: a bare
`cues.py` run emits a 13th cue (`hero` at 1.90 on s22) that the shipped
`audio.json` does not carry, exactly as ch2's s14 downgrade did.

---

## 8 · The rate constraint — five branches, every one proven to throw

Not asserted; **exercised.** A violation was planted for each branch, the
failure observed, and the plant reverted.

| # | branch | planted | observed |
|---|---|---|---|
| 1 | in-page **CORPUS** without a rate | renamed `#s22-rate` → `#s22-nope` | `hyperframes check` Runtime: `✗ page_error: RATE ASSERT FAILED — s22 renders ₹20,00,000 with no #s22-rate carrying a rate` |
| 2 | in-page **DERIVED** with neither rate nor marker | s28 focal → `₹7,777 A MONTH`, rate element removed, `ILLUSTRATIVE` struck from the foot | `✗ page_error: RATE ASSERT FAILED — s28 renders the derived income ₹7,777 A MONTH with neither a rate nor an ILLUSTRATIVE marker in frame` |
| 2b | the **MARKER escape** must not over-fire (negative control) | same frame, `ILLUSTRATIVE` foot restored | `Check passed`, 0 errors — the declared escape clears it |
| 3 | build-time **unknown ₹ token** | s24 foot → `₹7,777 divided by 12` | `Error: s24: renders ₹7,777, which the rate assert's CORPUS list does not carry…`, exit 1 |
| 4 | build-time **font-subset guard** | `THE RATE HELD?` · a Devanagari kicker | `Error: s27: on-screen string carries "?" — banned in this cut` · `Error: s30: Devanagari on screen — the font subset has none` |
| 5 | build-time **one focal per scene** | `stmt` and `num` on s30 | `Error: s30: never a stmt AND a num (§3)` |

Five rate/derived frames in this chapter exercise the live path: s22 and s23
(₹20,00,000), s23 (₹60,000), s24 (₹5,000), s25's kicker (the ₹5,000 callback)
and s28 (all four figures at once, plus the only `A MONTH` derived token). The
`$`-anywhere and banned-payout-word greps run over the whole emitted document,
comments included.

`tools/check_vo_frame.py` closes the half the in-page assert cannot see and
PASSES on all nine scenes.

---

## 9 · Copy and layout decisions, declared

- **s28's focal is the script's copy, BROKEN** — the cue block's middle dot
  between the two pairs becomes a line break and the four figures stack as two
  pairs. `.arch-b .huge` is capped at 900px (the type shares the frame with the
  art plate) and `₹10,00,000 TO ₹20,00,000` measures **903.5px at the 76px
  floor** — measured with fontTools against the shipped woff2 at weight 900, not
  estimated. Stepping the focal below 76 to make a line fit is forbidden, so the
  copy was restructured instead, and the four short lines now mirror the drawn
  layer's two block pairs exactly. ⚠ **This is the one place where §3's focal-size
  ladder and archetype B's 900px column genuinely conflict:** the ladder's own
  "≤24 chars → 112px" is unbuildable for a money string in a non-centred B scene
  (24 chars at 112px is 1330px). Worth a system note if another B scene ever
  carries a figure pair.
- **s23's focal carries an authored break** (`₹20,00,000 AT 3.0%` /
  `IS ₹60,000 A YEAR`), typographic, not copy — a greedy break would orphan
  `A YEAR`. Same for s25, s26 and s29.
- **s22 ships with NO foot** and that is the script's own choice: 2.8's cue block
  carries an ILLUSTRATIVE foot and 3.1's does not. The rate lives where §4 puts
  it, a first-class 40px `.sub` at +1.10, before the figure lands.
- **s24 and s28 split the script's foot** so the rate is a `.sub` and not a 26px
  foot a density pass can drop — the same split ch2 shipped at s18.
- **s25's rate takes ladder A's cue 3 (+1.90)**, not variant B's +1.10: the
  figure it qualifies is in the kicker and is a callback, not a new corpus.

---

## 10 · Checks

| check | result |
|---|---|
| `npm run check` (`hyperframes check`) | **PASS** — 0 errors, **17/17 text checks pass WCAG AA**. 3 warnings and 15 infos, all structural advice the pipeline declines: `composition_file_too_large` / `timeline_track_too_dense` (splitting into sub-compositions), `container_overflow` on every `.bg` (that IS `inset:-8%`), `pointer_events_none` on `.grain`, and on s28 `panel_out_of_canvas` for `.p-b` overflowing right by 60px — the system's own plate rect, cropped by the frame edge by design, with all art inside vx 800 |
| `tools/check_vo_frame.py … --chapter 3` | **PASS** — 9 scenes cross-checked against their VO lines |
| `tools/audio/cues.py …-hi-ch3` | **exit 0**, empty stderr, no gap violation on either the generated or the shipped list |
| `tools/pipeline_check.py check build … --chapter 3` | **PASS build-hi** |
| `tools/pipeline_check.py check assets … --chapter 3` | **PASS assets-hi** — re-run AFTER the build, as fin-assets asked, so its attribution-vs-composition assertion actually reaches the nine rendered images |

`known_benign` is empty and stays empty: nothing above is an error, and no
design token was touched to satisfy a checker.

**Snapshot pass — 15 frames looked at, per batch:**

| batch | frames | at |
|---|---|---|
| `snapshots/qa/b1` | 3 | s22 +3.40 · s23 +3.30 · s24 +4.80 (each scene's last cue, settled) |
| `snapshots/qa/b2` | 3 | s25 +2.60 · s26 +2.60 · s27 +3.75 |
| `snapshots/qa/b3` | 3 | s28 +3.50 · s29 +2.00 · s30 +2.00 |
| `snapshots/qa/b4` | 1 | s28 +3.50, after the band fix |
| `snapshots/qa/b5` | 2 | s22 at **both ends of its ken** (+0.20, +5.20) — the opening-gate read |
| `snapshots/qa/b6` | 3 | s22 +0.20, +3.40, +5.20, after the declared window |

Every one was opened and read; each batch has its **own** `-o` directory,
because `hyperframes snapshot` wipes the directory it is given. The `.stack`
sits inside the safe area on all nine, nothing overflows, and the chapter sheet
agrees.

---

## 11 · For fin-render, fin-editor and the CEO

1. ⚠ **THE PAYOFF CLAUSE FAILS AND IT IS NOT CLOSE-BUT-FIXABLE IN THE BUILD.**
   s27 is #4 on median and #3 on p10, stable across four span definitions. I did
   **not** re-frame s27 to chase it: the only window that would raise it enough
   shifts right onto the notebook and cream envelope, which drops the numbering
   stamp out of frame and pulls the right-edge scale (`POSTSTUKKEN`, legible
   Latin type) IN — trading a legibility gain of ~1 point for a new
   foreign-text risk on the frame fin-assets already cropped once for exactly
   that. Ruling wanted, not a fix improvised here.
2. **The real finding is flatness at the top**: four photographs inside 0.39
   points. If a fetch round opens, the brief is *raise s27*, not *lower s25/s22*.
3. **s22's opening-frame gate passes NARROWLY** and only because of the declared
   window. A 2.54-aspect shallow-DOF macro cannot show its subject's silhouette
   in 16:9; the window is this file's ceiling.
4. **fin-assets' caveats, all still standing and none of them closed by me:**
   s27's residual `GESC` / Dutch form text behind the stamp · s23/s24 make two
   consecutive rungs whose artefact is a calculating device, so **ch4's s32/s33
   counterfoil MUST be paper** or §10's five-artefact ledger spine is gone ·
   s28's balance shows no weights (by design — the drawn layer carries the ratio)
   and carries a cast `3Kg` on the beam · s30's ~15px figure on the far road.
5. **s27's sheet cell is honestly empty** (sampled +2.60, figure anchored +2.95).
   Judge that scene from the mp4 at +3.75.
6. **The s23→s24 hold is one photograph under one push.** Registration checked
   arithmetically rather than assumed: s24's visible source rows map to s23 rows
   139.3–1109.7 against s23's own 97.6–1155.4 — centres 2.4 screen px apart.
   Worth confirming on the encode the way ch2's was.

---

## Verdict

**PASS.** 9 scenes, root 61.143s at offset 124.007s, all four required checks
green, all five guard branches proven to throw, one drawn layer with both
declined alternatives written down, and the container ladder applied as ruled
with the storyboard's two stale places named.

**One declared FAILURE handed up rather than papered over: the payoff clause
(clauses 2 and 3) fails on the encode, and the cause is a 0.39-point tie at the
top of the chapter rather than a dark payoff.**

## Artifacts

- `studio/videos/passive-income-number-hi-ch3/build.mjs`
- `studio/videos/passive-income-number-hi-ch3/index.html`
- `studio/videos/passive-income-number-hi-ch3/assets/audio.json`
- `studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4` (1835 frames)
- `studio/videos/passive-income-number-hi-ch3/renders/SHEET-ch3.jpg` + `.json`
- `studio/videos/passive-income-number-hi-ch3/snapshots/qa/b1…b6`
