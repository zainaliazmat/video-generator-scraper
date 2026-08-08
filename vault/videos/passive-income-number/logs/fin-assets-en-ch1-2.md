---
summary: en ch1 fix pass — both blockers (s3+s4, s6) and both should-fixes (s5, s8) re-fetched and off wood; 18 contact sheets, 108 candidates, 4 new photographs + 1 re-derived crop. s5 took 8 sheets and one post-promotion full-resolution rejection (a gauge whose legible `bar` + `EN 837-1` were invisible at grid size). 0 md5 collisions, `check assets --chapter 1` PASS.
updated: 2026-08-08
source: fin-assets attempt 2, chapter 1, en cut — fix pass against editor-en-ch1-1.md.
---

# fin-assets — passive-income-number / en / chapter 1 / attempt 2

**PASS `check assets --slug passive-income-number --cut en --chapter 1`.**
8 image slots, 8 files, 8 CREDITS rows, **28 distinct md5s across every project on
disk — 0 collisions**, hi cut included.

**Accepted 5 · rejected 104 candidates + 1 post-promotion reversal · dropped 0.**
s1, s2 and s7 untouched, as instructed.

---

## The four fixes

| slot | was | now | source | W×H | YHIGH | R−B |
|---|---|---|---|---|---|---|
| **s3** | café table, red duffel + wallet + sunglasses, phone clipped at the right edge | dark stoneware mug of black coffee and a **whole black-screen phone** on a pale concrete table, dark ground behind | Pexels · Sheldon Li | 1880×1253 | 226 | −6.0 |
| **s4** | `crop=1600:900:133:290` — landed on the **mug** | `crop=1200:675:680:517` on the new s3 — **phone whole and dominant**, mug reduced to its handle at the left edge | (s3's source) | 1200×674 | 231 | −4.3 |
| **s5** | brass table-tent stamped `5` on a restaurant table | **a single arrow dead centre in an archery target**, no numeral legible anywhere | Pexels · RDNE Stock project | 1880×1253 | 149 | −1.8 |
| **s6** | blank kraft bag on a wooden plank wall | **the week's groceries at a US front door** — basil, pineapple, milk, pasta, sauce, a net of oranges, on flagstone against stone veneer, black mat, screen door | Pexels · RDNE Stock project | 1880×1253 | 215 | −0.1 |
| **s8** | weathered ladder on **wooden siding**, right two-thirds in shadow | **a wooden ladder against a terracotta adobe wall under open sky**, shot from below | Pexels · Rafael DeSoto | 1880×1253 | 182 | +25.7 |

Every source clears `MIN_SOURCE_YHIGH` 110 with ≥39 points of margin. Every fetched
file is 1880 px (Pexels `large2x`, per §10's resolution routing for a crop source).

### The wood count

Finding 6 is answered: **6 of 8 → 3 of 8**, and the three that remain (s1, s2, s7) are
exactly the three the brief protected. New grounds are pale concrete (s3/s4), a paper
target face on dark (s5), flagstone + stone veneer (s6), and adobe plaster + sky (s8).

---

## Blocker 1 — s3, then s4

The editor's test was three-part and all three now hold:

- **a mug** ✓ and **a whole dark-screen phone** ✓. The phone is occluded at its far end by
  the mug's handle — a natural overlap that still reads as one whole phone — and **not
  clipped by the frame edge**, which was the un-rescuable defect in the old source.
- **domestic, not a café** ✓. A concrete table, a stoneware mug, nothing else in frame. No
  duffel, no wallet, no sunglasses, no travel.
- **a right-hand crop makes the phone dominant** ✓ — see the crop below.

**The crop, and the one trade it makes.** The phone's far edge sits 26 px from the
source's right edge, so the *geometry* of "phone dominant" and "phone under the whole
`.p-d` band" cannot both be paid at a usable resolution:

| crop | phone starts at | resolution | verdict |
|---|---|---|---|
| 1880×1058 (full width) | 38% | native | mug dominant — the rejected framing |
| 1600×900 | 53% | 1.20× | mug and phone equal in mass |
| **1200×675 (shipped)** | **47%, and the only complete object in frame** | **1.60×** | **phone dominant** |
| 1000×563 | 63% | 1.92× | phone under the whole band, but too soft to ship |

To put the phone under the band's full x-range (550–1370 of 1920) the crop would have to
be **≤882 px wide** — a 2.18× upscale. So the shipped frame lands the banner across the
phone's screen with only its left edge over the mug's lower body, and the phone is the
object the eye goes to: it is complete, high-contrast against the pale table, and holds
the centre and right. **A horizontal flip would have solved the band cleanly and was
refused** — it breaks §6b's matched-frame hold, which is a jump cut wearing a dissolve.

**s4 is 1200 px, under the ≥1600 rule.** Declared, not hidden. The blocker was dominance;
1200 px under the locked grade plus 5% grain sits inside the band the library already
ships at, and 1600 px could only be bought by re-shipping the defect.

---

## Blocker 2 — s6

Two of the three named costs are now in frame — **groceries** (unmistakably, and in
quantity) and **the home** (a front door, a porch, a doormat). **Gas and the car are
not**, and that chip carries alone.

Five sheets were spent trying for all three, and the storyboard's flat-lay
(*bag + car keys + house keys in a row on dark slate*) **does not exist in either pool**.
Each phrasing hit a different stock genre by gravity:

| round | query | what came back |
|---|---|---|
| 1 | `…vegetables… dark slate… flat lay` | 6/6 **food photography** — slate boards and chef's knives; one cell carried a legible `Instacart` watermark, one a green-screen phone |
| 2 | `house keys and car key beside a paper grocery bag…` | 6/6 **real-estate stock** — three cells with legible marketing copy (`7 Reasons to Own a Home`, `MORTGAGE RATES`, `For Buyers`), one branded `NAJA` wallet |
| 3 | `…in the open trunk of a car…` | 6/6 **people**, including an identifiable face in a mask and an identifiable child |
| 4 | `…on the front doorstep of a house…` | 1/6 usable — **shipped**; the other five were a delivery mat reading `Please LEAVE PACKAGE HERE`, two shipping labels, and two more people |
| 5 | `still life of car keys wallet and a brown paper bag…` | 6/6 — a payment terminal, a lit phone screen reading `Shop now`, two people, and two frames on white/dark **wood** |

The old defect is gone on its own terms: the editor's frame was *"a pale rectangle on
brown wood"* with a **14-point** tonal spread in its right half. This one measures
**L: 120/159/212 · R: 49/128/215** — a 166-point spread on the right, because the black
doormat is in it. Neither half is flat, and it is off wood.

**Checked at 3× on the packaging**: `Spaghetti / Espaguetis` and a date code on an
unbranded milk carton are the only readable words, and **no identifiable brand mark
survives the zoom**, let alone the grade. Spanish-language packaging is normal US retail
and is not a place signal. Flagstone, stone veneer, a security screen door and a
half-gallon jug make the frame unambiguously American.

**Material rule honoured**: this is not more paper. The old frame was kraft — diffuse, no
specular ceiling. The new one is glass bottles, a glazed jar, a plastic jug and wet fruit
against stone, and it measures YHIGH 215.

---

## Should-fix 1 — s5, and the reversal that only a full-resolution read caught

This slot cost **8 sheets** (3 in attempt 1, 5 here) and is the one place I promoted a
file and then took it back.

**The instrument family the editor named is exhausted.** Gauges, calipers, dial indicators
and analogue meters were all worked, and the pool answers them with three things: car
dashboards (`km/h` speedometers — metric, and a pre-echo of s25's pump), European
pressure gauges, and grimy machinery too dark to clear the gate.

| round | query | result |
|---|---|---|
| 1 | `antique brass pressure gauge…` | best cell = a chrome `bar` gauge; a `WESTON AMMETER` brand mark on another |
| 2 | `vernier caliper polished steel…` | a legible **`Mitutoyo`**; a digital micrometer showing a readable figure; a tattooed forearm |
| 3 | `dial indicator gauge macro…` | **`Mitutoyo · 0.01mm · MADE IN JAPAN`** at full size; two hands-and-bench frames |
| 4 | `vintage manometer dial gauge…` | the chrome `bar` gauge again; a `km/h` speedometer at YHIGH 17 |
| 5 | `brass barometer dial…` | the chrome `bar` gauge a **third** time; a ship's-wheel novelty; a **clock face** (s2 already owns a clock — gate 4) |
| 6 | `set of steel number stamp punches…` | Soviet postage stamps (`ПОЧТА СССР`); a flat-lay spelling **`TAXES`**; a tag stamped `13108` — one legible figure, the rejected pattern exactly |
| 7 | `glowing analog meter needle…` | 6/6 car dashboards |
| 8 | `single arrow in the bullseye…` | **accepted** |

**The reversal.** The chrome gauge cleared every numeric gate (YHIGH 225, R−B +40.2 — the
only cell all run to clear the +40 warmth target) and I promoted it. At full resolution it
carries **`bar`** in 60 px type, **`EN 837-1`** — a European standards mark — and a
`0…16` numeral scale so large it *is* the subject; the needle also rests ambiguously
between `0` and `10`, so half the readings of the frame say **zero** under a line about a
number you *reached*. None of it was visible on the contact sheet. Rejected and refetched.
This is rule 1 of the stage doing exactly the job it was written for.

**Why the arrow.** *One arrow, dead centre* says **you reached exactly the mark you aimed
at, and not more** — which is both halves of the line, `NOT RICH` and `One specific
number`. It prints **no figure at all**, so it cannot plant the wrong one; the target's own
ring numerals are out of focus and illegible at 3× (checked). It is off wood, off a
restaurant table, brand-free, people-free, and `target` is already this video's declared
colour role, so the object is in the cut's vocabulary rather than imported into it. The
scattered old holes read as *many attempts, one that landed* — which is the chapter.

**Where it is weakest, stated plainly:** a bullseye is not literally a number, so
sound-off gate 3 is answered by analogy rather than by depiction. Every object that
answers gate 3 head-on either prints a single figure (the rejected `5`, a `13108` tag, a
micrometer readout) or prints a metric/branded scale. Given the choice the editor framed —
*"a blank tag fails gate 3; the answer is not a wrong number"* — this is the reading that
plants nothing.

§10's override row for s5 has been re-specified in the storyboard so this is not
re-argued in a later chapter.

---

## Should-fix 2 — s8

The editor asked for *"plaster, stucco, brick or open sky, so the rails and rungs separate
from the wall"*. Delivered: a pale weathered ladder against a **terracotta adobe wall**
with open sky behind — plaster **and** sky, the two brightest items on the list. The rails
and rungs now separate at maximum contrast instead of wood-on-wood, warmth went **0 →
+25.7**, and the left half is a broad, near-flat adobe field, which is a far better bed for
the `.centred` stack than the old shadow was. Southwestern adobe is also unambiguously
American. No `filter:` override was set or needed — none exists in this cut (§9).

**One declared deviation:** §10 asks for *"the lowest rungs… the top out of frame"*; this
is a low angle with the **bottom** out of frame and the top running over the roofline. The
purpose of the spec is that s8 be distinct from s23 (a macro of ONE rung) and s74 (the
whole ladder, full height) — it is, on both counts, and "the climb continues past the
frame" is the reading the line wants.

---

## The tension the "off wood" instruction created, and where the knob is

**All four replacements measure below the +40 R−B warmth target** (−6.0, −4.3, −1.8, −0.1;
s8 alone at +25.7). That is not four independent misses — it is the direct cost of the
instruction, because **warm brown wood was the thing supplying the warmth in every frame
that had it.** Off wood, the pool's answer is concrete, stone, paper and flagstone, and
those are neutral by construction.

Two things make this defensible rather than a regression:

1. **`R−B ≥ +40` is a guideline, not a gate.** `pipeline_check` enforces `YHIGH` only, and
   the predictor was calibrated on frames whose warmth came from the *subject*. The
   incumbent s7 (+2.0) and old s8 (0.0) already shipped past the editor without comment.
2. **§11's `--f1` ground is the mechanism for exactly this** — a per-scene two-stop ground
   at 38% on `.has-photo .field`. s3/s4 sit on `#241d15`, s6 on `#291f13` (the warmest in
   the chapter), s8 on `#1f1e1c`; s5's `#1c2027` is *meant* to be the neutral sobering
   step. A neutral photograph under a warm ground is the configuration §11 describes.

**If the encode reads cold, the ground values are the knob, not the photographs** — and
that call belongs to the editor, because the alternative is going back onto wood.

---

## Two editor rulings written into the storyboard

Both are recorded in `vault/videos/passive-income-number/storyboard-en.md` so chapter 2
inherits them rather than re-litigating them:

1. **§10's override table, s3/s4 row** — black-screen phones on **s1 / s3 / s4 are
   APPROVED** and are not a violation of the standing rejection. The rule targets *a lit
   screen carrying someone's brand and being the brightest thing in frame*; here the screen
   is the darkest object and carries nothing. The amendment also records the structural
   reason: a face-down black phone in a dark room has **no highlights by construction** and
   cannot clear `YHIGH ≥ 110`. s79 (6.11) is flagged to inherit the same treatment.
2. **§8's cue line** — `playLottie` is **+1.13**, not +1.85, with the measurement that
   settles it (card outline ≈+1.50, `$` badge and first masked line visibly building at
   +1.85, bar filling through ≈+3.6). The **`buzz` SFX stays at +1.85**, and the reason is
   spelled out: firing the Lottie at +1.85 would put the first drawn pixel at ≈+2.25 and
   let the sound precede the picture by ~0.4s.
3. (Housekeeping, same file) **§10's s5 row** re-specified — the blank enamel tag and the
   numbered replacement are both struck, with both rejections and the eight-sheet
   instrument search recorded.

---

## Standing rejections — swept over the four new files

- **No faces, no people.** Rejected on this ground alone: 11 candidates, including an
  identifiable child and an identifiable masked face on the s6 round-3 sheet.
- **No readable brand marks.** Rejected: `Mitutoyo` (×2), `MADE IN JAPAN`, `WESTON
  ELECTRICAL INSTRUMENT CORP`, `NAJA`, `Instacart`, `SAMSUNG`, plus three real-estate
  flyers and a delivery mat. Checked at 3× on s5 and s6, the two frames with any small
  print at all.
- **No legible figure anywhere.** s5 prints none. s6's only readable words are
  `Spaghetti / Espaguetis` and a date code.
- **No non-US marks.** This is what killed the promoted gauge (`bar`, `EN 837-1`) and two
  `km/h` speedometers. Every shipped frame is American or place-neutral.
- **No lit screens.** s3/s4's phone is black; rejected 6 candidates carrying a lit or
  white-mockup screen, one of them reading `Shop now`.
- **No currency in any frame**, so no wrong-currency trap applies. One candidate showing
  cash in a wallet was rejected — it argues with *"You did not get rich."*
- **Nothing reused inside the chapter.** Eight distinct objects. A clock face surfaced as
  an s5 candidate and was rejected because s2 already owns the clock (gate 4).
- **md5 swept across every project on disk** including both hi chapters: 28 files, 28
  hashes, 0 duplicates.

---

## Handoff

- **`s4.jpg`'s CREDITS row was re-keyed in the same move as the pixels** — it still carried
  the *old* s3's photographer (Engin Akyurt) and now carries Sheldon Li's. This is the
  licence breach the stage brief names; a derived crop that keeps its predecessor's credit
  row is an uncredited photograph. `manifest.json` and `s4.jpg.src` both record the new
  rect `crop=1200:675:680:517`.
- **fin-build:** nothing changes mechanically. s4 is still a derived crop, still the
  §6b hold partner of s3, and the Lottie still stages on `.p-d` — but note the banner's
  left edge now lands on the mug's lower body rather than on open table, and the Lottie
  fires at **+1.13**.
- **s5 and s6 share an author** (RDNE Stock project). Two frames, two unrelated subjects,
  no visual family — flagged for completeness, not as a defect.
- The cut-level manifest (`passive-income-number-en/assets/img/manifest.json`) still holds
  attempt 1's queries for s3/s5/s6/s8 and must be re-synced at cut assembly, together with
  s4's CREDITS row — the same standing item as attempt 1.
- `_cand/` holds the **last** round per slot (s3 r3, s5 r8, s6 r4 restored from backup,
  s8 r2). Earlier rounds are tabulated above; they were overwritten, which is the
  documented cost of re-querying a slot.

## Reusable findings

1. **A gate can only reject.** The chrome gauge had the best numbers on the entire run —
   YHIGH 225 and the only R−B above +40 — and was the worst frame, because the numbers
   cannot see `EN 837-1`. Two candidates on attempt 1 taught this; this run paid for it
   again with a promoted file. **Never let a clean measurement shorten the vision pass.**
2. **"Change the surface" and "keep it warm" are opposing instructions in a wood-heavy
   chapter.** Worth naming at storyboard time: if the design calls for warmth *and* forbids
   the material that supplies it, the ground layer has to absorb the difference, and
   somebody should say so before four slots are re-fetched.
3. **A three-object staged flat-lay is not a stock photograph, it is a shoot.** Five
   sheets, five different genres, zero hits. When a storyboard specifies a composition
   rather than a subject, the honest budget is *"which two of the three exist together in
   the world"* — groceries and a front door do; groceries, keys and a car do not.
4. **Occlusion is not clipping.** A phone half-hidden behind a mug reads as a whole phone;
   a phone cut by the frame edge reads as a sliver. Same pixel count, opposite verdicts —
   and it is the distinction that decided which s3 candidates were even worth measuring.
