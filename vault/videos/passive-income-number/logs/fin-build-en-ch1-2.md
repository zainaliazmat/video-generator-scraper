---
summary: en ch1 fix pass against editor-en-ch1-1. Two edits only — the s2 chip row right-aligned off the alarm clock, and `#s3-bg` given `background-position: center 70%`, which is the OPPOSITE of the 40% the handoff proposed (40% cuts MORE of the phone; proven with two snapshots). The Lottie was already firing at +1.13 and needed no change. 31 frames across 5 fresh -o dirs, `npm run check` clean, `pipeline_check check build --chapter 1` PASS. Every timing byte-identical.
updated: 2026-08-08
source: studio/videos/passive-income-number-en-ch1/ · editor-en-ch1-1.md · fin-assets-en-ch1-{2,3}.md · tools/format.json chapter_design + layout
stage: fin-build, cut en, chapter 1, attempt 2 (fix pass)
---

# fin-build — en · chapter 1 · attempt 2 (FIX PASS)

Not a rebuild. `build.mjs` is the generator and the only file I edited; `index.html`
and `assets/audio.json` are its output. **`assets/audio.json` came out
byte-identical to attempt 1 (`e4110969…` before and after every edit)** — which is
the mechanical proof that no timing, no scene start and no SFX cue moved, since it
is derived from the same `sc[]` array the markup is.

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|
| start | 0 | 3.543 | 9.254 | 14.599 | 21.564 | 25.551 | 31.262 | 38.149 |
| `data-duration` | 3.993 | 6.161 | 5.795 | 7.415 | 4.437 | 6.161 | 7.337 | **8.271** |
| track | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |

Unchanged. Root 46.42s, seven joints overlapping by exactly 0.450s, s8 bare.

---

## 1 · s2's chip row — done

`#s2-chips { justify-content: flex-end; padding-right: 150px; }` — an ID rule in
the composition's own one-off block, beside `.v-chiprow` which it modifies.
150px is `.scene`'s own horizontal safe padding, so the row is flush at x1770
and starts at x761.

The clearance is not static, because s2's ken is a push-**out** (`xPercent +2.5 →
−2.5`), so the clock drifts left across the scene. Measured off the frames: the
clock's right edge runs **x715 at the first chip's pop (+1.10) → x657 at the
cut**. Worst-case gap 46px, widening to ~104px. Nothing else lives at the row's
y-band (660–740): the book stack's top edge starts at y≈745 and the bed is below
y≈850.

Confirmed at 6.643s (the row's max-density instant, all three chips settled): the
alarm clock is completely clear, the right void is filled, and the frame now reads
kicker top-left → rule → clock lower-left → mechanism mid-right. `.v-chiprow`
itself is untouched, so **1.6 is unaffected** — see finding B below for why that
is the right call for its new photograph.

## 2 · The Lottie — already at +1.13, no edit made

`build.mjs` line 115 has carried `const LOTTIE_AT = 1.13` since attempt 1, with the
faster-whisper derivation in the comment above it ("buzzes" at scene +1.730–1.920;
the asset's own jitter is frames 16–24 = +0.533–0.800 into it; 1.73 − 0.60 = 1.13).
The editor's ruling confirms the number rather than changing it. I re-verified it
in frames rather than in source — batch **b7**, seven samples across the stage:

| t | what is drawn |
|---|---|
| 15.60 | nothing (fire is 15.729) |
| 15.75 | nothing yet — the asset's own first frames are empty |
| 15.95 | card outline just appearing |
| **16.449** | **`$` badge drawn and legible, line-1 stub extending — the card is visibly LIGHTING** |
| 17.20 | line 1 filled, time bar in |
| 18.229 | fully assembled (asset end, 2.50s) |
| 20.50 | holding its last frame under the stmt |

Seven distinct states = it animates, not merely draws. **16.449 is the `buzz` SFX
cue in `audio.json`, and at that instant the banner is mid-build** — the diegetic
condition §8 exists for. The SFX stays at +1.85; I changed nothing in the sound
pass.

## 3 · `#s3-bg` — TAKEN, but at `center 70%`, not `center 40%`

**The value in the handoff is backwards and would have made the defect worse.**
`background-position-y` on a `cover` image that overflows vertically works
opposite to intuition: a *smaller* percentage aligns the image nearer its TOP,
which pushes content DOWN the frame and crops MORE off the bottom. 40% is the
direction that cuts more phone.

I did not want to settle that by arithmetic, so I rendered it. Two extra `-o`
dirs, one frame each at **t=14.55** (s3's ken end, scale 1.08 — the worst
instant):

| dir | value | phone's bottom |
|---|---|---|
| `snapshots/qa/b5/frame-03` | 50% (as built) | **off-frame** |
| `snapshots/qa/bg40/frame-00` | **40%** | **off-frame, and the phone starts ~30px lower — visibly worse** |
| `snapshots/qa/bg70/frame-00` | **70%** | **rounded corner in frame with ~40px of table below it** |

Applied as `bgPos` on the 1.3 spec row, emitted inline on that one `.bg`. It is a
**framing** override, not a grade one — no `brightness`, no `filter`, nothing
`format.json`'s `grade_note` forbids, and it is the only per-scene `.bg` override
in the chapter.

Two things it buys beyond the phone, both visible in the frames:

- **The §6b hold got tighter, not looser.** s3's and s4's crop windows were
  offset by ~143 source px vertically at the joint; 70% closes ~40 of that. At
  **14.979** (the joint at +0.38) there is one phone at one position with s3's
  type ghosted over it — not two ghosted phones at different scales.
- The cost is the mug's top rim at the frame edge, which **s4 already crops**
  (fin-assets-en-ch1-3, declared deviation 2), so s3 is now more consistent with
  the frame it is dissolving into, not less.

## 4 · Three stale scene notes corrected

`build.mjs`'s `SCENES` notes are the design record the archive keeps, and three of
them still described photographs that no longer exist: s3 as "the same kitchen
counter", s5 as "a brass table-tent stamped 5", s6 as "a grocery bag on wood".
Rewritten to the delivered pictures with the ruling that produced each. No
behaviour change (`audio.json` md5 unmoved), but a false fact in the one place the
next chapter reads from is worth one line.

---

## The frame pass — 31 frames, 5 batches, one `-o` dir each

Every batch has its **own** `-o` directory. `hyperframes snapshot` wipes its output
dir per invocation, and the 2026-07-31 defect on `first-lakh-first-thousand-hi` was
exactly a shared dir plus an unearned count.

| batch | frames | samples | how many I actually looked at |
|---|---|---|---|
| `b5` | 9 | each scene's LAST cue (max density) + s3's ken end | **9 of 9 at full 1920×1080** |
| `bg40` | 1 | s3 ken end, `center 40%` | 1 of 1 full res |
| `bg70` | 2 | s3 ken end + mid-scene, `center 70%` | 2 of 2 full res |
| `b6` | 7 | all seven joints at **+0.38** (`qa.dissolve_sample_offsets`) | contact sheet (7 of 7) + **14.979 at full res** |
| `b7` | 7 | the Lottie stage | contact sheet (7 of 7) + **16.449 at full res** |
| `b8` | 5 | final state: t=0.05, s2, s3 ×2, the tail 46.41 | 4 of 5 full res; the 5th (11.854) is content-identical to `bg70/frame-01`, read full res |

**18 read at full resolution, 13 more on the two contact sheets.** No
`Navigation timeout` flake occurred on any of the six invocations; the retry loop
was in place regardless.

### Every scene paints its NEW photograph

Eight distinct md5s, eight distinct graded photographs visible in b5 at full res.
This is the failure mode where `image_per_scene` is satisfied by a file that loads
and never paints; it did not happen. All eight are ≥1600px on the long edge
(seven at 1880×1253, s4 the derived 1600×900).

| | what actually renders |
|---|---|
| s1 | *unchanged* — white phone, dead screen, warm bamboo, hard sunbeam |
| s2 | *unchanged* — alarm clock, book stack, unmade bed, nothing switched on |
| **s3** | **new** — overhead terrazzo table, whole black-screen phone, black coffee, bud vase |
| **s4** | **new** — the same table, tighter; phone centred and dominant under the banner |
| **s5** | **new** — archery target, one arrow standing in it |
| **s6** | **new** — loaded grocery bags on a house doorstep: pineapple, milk, sauce jar, oranges |
| s7 | *unchanged* — hands on keys, screen edge-on, warn-red slam |
| **s8** | **new** — ladder against a stucco wall, sky behind |

### All seven dissolves fire against a live frame

b6 at +0.38 on every joint: in each one the outgoing scene's type is ghosted at
partial opacity **over the incoming photograph**, with the incoming kicker already
up. Never a fade against black. b8 at **t=0.05** shows s1's photograph already
painted with no type yet (kicker fires at +0.30) — the first frame of the video is
not black. **t=46.41** shows s8 fully painted and **not** fading, which is what a
chapter must do so the assembled cut takes no black flash at the fold.

### No rail

Every occurrence of "rail" / "chapter" / "slide" in `index.html` is inside an HTML
comment, the `<title>` or the `chapter-design.css` filename. Nothing renders. No
frame of the 31 carries a chapter title, a counter, a slide number or a progress
mark. The `cut-en` watermark rides `#root::after` and is bottom-right in all 31.

---

## The warmth question — reported, not fixed

The encode reads **cold**, and the `--f1` ground is currently not the compensating
layer it is described as.

- **s3 / s4 are the coldest frames in the chapter.** Terrazzo is neutral by
  construction and the grade desaturates what little cast it has. Their ground is
  `--f1:#241d15`, the warmest value in the chapter besides s6's — and I cannot see
  it. `.has-photo .field { opacity: .38 }` means the ground is a 38% tint sitting
  *under* `.scrim`'s four layers; over a mid-dark neutral stone it contributes
  almost nothing. The knob exists but is turned far too low to answer a −1.8 R−B.
- **The chapter's temperature arc now reads:** warm (s1, bamboo) → cool (s2) →
  neutral-cold (s3, s4) → **saturated** (s5) → pale cool (s6) → warm-red (s7,
  the `--warn` role) → cool (s8, sky). Two warm frames of eight, where the wood
  pass had six.
- **My read: this is defensible as an arc, not as an accident.** A cold, colourless
  what-if that only takes colour twice — once on the target and once on the
  verdict — is a stronger structure than six brown tabletops, and the editor's
  finding 6 was that the brown was the problem. But it is now cold *by default*
  rather than *by design*, and if fin-editor wants warmth back the honest lever is
  raising `--f1` on s3/s4/s6 (a per-scene ground value, which §11 owns) or lifting
  `.has-photo .field`'s opacity in `chapter-design.css` — **a deliberate edit to
  the system, not something a build should improvise.** I changed neither.
- One measurement that does not match its number: fin-assets logged **s8 at R−B
  +25.7**, the warmest of the four replacements. On screen s8 is one of the
  coolest frames in the chapter — the +25.7 is the dark adobe mass, while the
  half of the frame the eye goes to is blue sky. R−B on a whole file does not
  predict the frame when the subject and the ground have opposite casts.

## Observations for fin-editor — not fixed, not mine to fix

**A · s5's arrow is not in the bullseye.** The object answers the ruling — it means
*one exact mark* without asserting a figure, it is off wood and off a restaurant
table. But the arrow stands in the gold ring slightly off centre, and the target
carries a dozen older holes. Sound-off that is closer to "archery practice" than to
"one specific number", and the line is about exactness. Also the only strongly
saturated frame in the chapter (red / gold / **teal** rings) — a colour event
nothing else here has, under a grade whose job is making unrelated photographs read
as one film.

**B · s6 is a doorstep delivery, not the specified top-down flat-lay.** The blocker
is answered — the bag is full and groceries are unmistakably in frame — but two
things the editor's fix depended on did not arrive: there are **no car keys and no
house keys**, so two of the line's three named things are still carried only by the
chips; and it is not a flat-lay, so the "it resolves itself" prediction for the chip
row did not apply. I left the row **centred** anyway, deliberately: the subject fills
the left two-thirds and the door and mat fill the right, so unlike s2 there is no
void to move into, and right-aligning would park all three chips on a blank dark
door. Say the word if you want it moved.

**C · s8's ladder is small and lands under the statement.** The wall is stucco and
the sky does separate the rails, so the material note is answered. But the ladder
occupies about 10% of the frame width in the right-of-centre third, the left
two-thirds is a large dark adobe mass, and `s8-stmt` crosses the ladder's top rungs.
It reads — it does not read *instantly*, and this is the frame s23 and s74 return to.

## Gates

**`npm run check` → PASS**, identical in shape to attempt 1 — neither edit
introduced a finding.

```
Lint      0 error(s), 3 warning(s), 2 info(s)
Runtime   0 errors, 0 warnings
Layout    0 error(s), 0 warning(s), 9 info(s)
Motion    0 errors, 0 warnings
Contrast  10/10 text checks pass WCAG AA
```

The 3 warnings are `composition_file_too_large` (310 lines) and
`timeline_track_too_dense` ×2 — the shape every one-file-per-chapter build in this
pipeline has. The 11 infos are nine `container_overflow` on `#sN-bg` (that IS the
ken scaling the bg past the section that clips it) and two `pointer_events_none` on
system CSS. 0 lint **errors**, so Layout and Contrast both genuinely ran. `known_benign`
is `[]` and I added nothing to it. **No design token was touched** — no colour, no
size, no weight, and the `#s3-bg` override is framing, not grade.

**`pipeline_check check build --slug passive-income-number --cut en --chapter 1`
→ PASS build-en.** Native, no scratch mirror. The attempt-1 false positive
(`loadAnimation` matching inside a CSS comment) is gone and the chapter-awareness
fix works — that comment is still in the file, still explaining the pixel-stage
trap, and no longer punished for it.

## Result

**8 scenes · s1–s8 · 46.420s.** Chapter 1 of six, chapter offset 0.000s, so it
concatenates frame-exact as-is. Two design edits, three comment corrections, zero
timing changes. Ready for a fresh draft render.
