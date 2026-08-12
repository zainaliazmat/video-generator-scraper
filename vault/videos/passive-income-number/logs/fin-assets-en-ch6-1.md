# fin-assets — passive-income-number · en · ch6 · attempt 1

Final chapter of the cut: s69–s81, VO 6.1–6.13. **12 slots fetched, 12 accepted.**
s75 is not fetched — it is a declared crop of s76 (§7 / §10) and is **owed to fin-build**.

## Ran

1. Built `studio/videos/passive-income-number-en-ch6/assets-ch6/final/manifest.json` from the
   master queries in `…-en/assets/img/manifest.json` (s69–s81 minus s75), all routed `@pexels`
   (`assets.min_width_px` 1600; `pick_width_px.pixabay` is 1280 and cannot clear it).
2. `pixabay_fetch --candidates 6` — **19 contact sheets** over 6 rounds (12 slots + 7 re-queries
   before promotion), each read with one vision pass.
3. `--pick` → 12 full-res promotions, then **6 re-picks after the full-resolution read**, then 1
   more (s74) after comparing against ch1's shipped ladder.
4. `tools/image_sheet.py … --chapter 6` → `IMAGES-ch6.jpg`, read for repetition (twice: once on
   the first promoted set, once after the re-picks — the gate refuses a stale sheet, correctly).
5. Full-resolution `Read` of every promoted jpg, in two batches (s69–s74 / s76–s81) with a
   progress marker between, plus targeted full-res reads of **ch1 s8** and **ch1 s5** and **ch2 s9**
   to settle three cross-chapter repetition questions on evidence rather than memory.
6. Cross-project md5 dedupe with the `find … -print0 | xargs -0 md5sum | uniq -Dw32` form.
7. `pipeline_check check assets --chapter 6` → **PASS assets-en**.

## Failed

Nothing outstanding. **Eight defects were found and closed here; seven of the eight were
invisible at contact-sheet size and would have reached a render.**

**HARD — licence / factual class**

| slot | defect | how found | fix |
|---|---|---|---|
| **s76** | promoted image was **byte-identical to ch5's s61** (`918a5d9c…`, Pexels `wooden-boxes-by-wall-19746290`, Gene Samit). Pexels returns that one photograph for *every* crate query — it came back as a cell in **5 of 6** crate sheets | md5 dedupe | re-queried 5×; final pick is a different photographer's farmyard crate stacks |
| **s70** | the sheet cell was a **real named organisation's financial statement, fully legible**: `FIND AID FOR THE AGED, INC. AND AFFILIATES · CONSOLIDATED STATEMENTS OF FUNCTIONAL EXPENSES · Year Ended December 31, 2018/2017`, with line items and dollar totals — under a line citing **Morningstar's 3.9%**. The fabricated-source-document defect, naming a real charity | full-res read | re-queried 4×; see the s70 trail |
| **s73** | the alarm-clock heap carried **`Zoprol 30 mg Lansoprazol · TOPRAK İLAÇ`** (a Turkish pharmaceutical brand), **`WEST GERMANY`**, `REGAL` ×3, `GALAXY`, `BILOTTI`. Readable brand marks + foreign-country text on an all-American cut. It also collided with the alarm-clock motif that ch1's s2 owns and that **6.11 ("No alarm") depends on** | full-res read | replaced, see below |

**STRONG — the image argues with its line (sound-off gate 2)**

| slot | defect | fix |
|---|---|---|
| **s69** | spirit-level macro: at full res **the bubble is dead centre between the marks — the frame says *level, settled*** under `stmt: It is not a settled number.` The balanced-scale-under-"thirty-times-apart" failure, verbatim | replaced with a **weather vane** — an instrument whose whole job is to keep turning |
| **s81** | the CTA frame shipped an **OPEN, blank ruled notebook** under *"a closed notebook and a capped pen… finished"*. Open + blank reads *start writing*, the opposite of the beat, on the last frame anyone looks at | re-picked: a **closed** white hardback with its elastic band and a capped pen |
| **s74** | ladder standing against an orange wall with its **bottom out of frame**, under *"here is the ladder in order, **all of it**"*; and it is the exact complement of s8's declared statement ("the lowest rungs, top out of frame") | tried a whole-height stepladder — **rejected in turn**, see below — and the orange frame was restored deliberately |
| **s76** | the first replacement (crates against a cracked plaster wall) was **busy** — arched niches, conduit boxes, a wine-bottle rack, a copper cauldron — on a scene §10 routes to *near-flat, low-key* because it is art-forward and carries two `.sub` lines plus the drawn `ladder-bars-4-5`; and the crate count was unreadable, so the s75 crop had nothing to crop | replaced |

**Rejected candidates, and why** (applied consistently across all 19 sheets): faces and people
(s72 c2, s78 c2/c3/c6, s70 c4, s73 c6, s81 c4, s69 c4); readable brand marks (**NIKE** shoe boxes
on two separate crate sheets, **USPS/EMS** labels across all six cells of the first s73 sheet,
`Olympia` typewriter, `S. JEFFS & SONS WILLINGHAM` stencil, `MSC`/`Hapag-Lloyd` containers,
AirPods, an Apple home-button iPhone as the *subject*, a Google Home Mini); legible typed text
(`PRIVACY POLICY`, `TERMS OF SERVICE`, `VALUEABLE`, `Review`, `LUKE`, `WE CARE`, `Tax Deadline`,
`one nation.`, `The State of Employer Branding`, `#HASHTAG`, `Financial reports`, a `2|0|2|4`
diary); foreign text (Arabic on a map flatlay, Cyrillic on a crate, a Turkish shop fascia);
fabricated charts (three separate infographic/pie-chart flatlays); **a lit phone screen as the
brightest object in frame** (s79 c3/c6 — the standing rejection, twice); and one wrong-count
frame (seven hanging tags under a three-answers line).

## Evidence

**Gate.** `PASS assets-en` on the final 12 — bytes, `YHIGH ≥ 110` and attribution all clear on
first measurement; no slot in this chapter ever measured below the luma floor.

**Dedupe.** Final run: **empty output**. It was *not* empty mid-run — s76 collided with ch5's s61
byte-for-byte. The `find` form saw it; the retired `md5sum studio/videos/*/assets/img/*.jpg` glob
would have read zero files for this chapter-based cut, as it did between 2026-08-05 and -08-09.

**Dimensions** (checked per the ch5 `@commons` 3888×2592 outlier warning): all 12 land at
**1880 px wide** (s77 is 1713×1300, 4:3 native), 98 KB–439 KB. No file is out of family with its
chapter; the `commons_hits` fix held, and in any case no slot in ch6 needed the `@commons` rung.

### The three cross-chapter comparisons, made on the files and not from memory

- **s74 vs ch1 s8.** I read `…-en-ch1/assets-ch1/final/s8.jpg`: a wooden ladder running diagonally
  up an **adobe pueblo wall against blue sky**. ch6's s74 is a weathered ladder standing
  **vertically against a flat orange stucco field, no sky, no building form**. Same object family
  (declared, §10), legibly different photographs. I then tested the "full height" reading by
  promoting a whole-height stepladder (Pexels 8137999-class, room mid-decoration) and
  **rejected it**: dust sheets, a paint tray, a colour-swatch fan and a bucket make the frame say
  *someone is redecorating*, which fails sound-off gate 1 outright. A clean partial ladder beats a
  complete ladder inside the wrong scene. **Stated plainly for fin-editor: s74 does not show the
  whole ladder, and §10 asked for "full height."** Four ladder sheets returned no clean
  whole-ladder-against-a-plain-wall frame in either pool.
- **s81 vs ch2 s9.** ch2's s9 is a **kraft cover corner + a sharpened pencil on charcoal felt**,
  cropped tight. ch6's s81 is a **white hardback, closed, elastic band, chrome-and-rosewood pen,
  on warm red-brown wood**. Not a repeat, and the open→closed axis is the point.
- **s73 vs ch1 s5.** See the open question below.

### The s70 trail — four sheets, and why it ends where it does

The slot wants "a research report, title out of focus" and §10 lists s70 among the frames that
must carry **no legible title, figure or agency name**. This slot's subject *is* a document, and
a document is where text lives, so every sheet failed on text:

1. **stapled-report query** — six cells: two hands-in-frame, one high-key donut-chart flatlay, one
   legible `The State of Employer Branding` + `#HASHTAG`, and the **FIND AID FOR THE AGED**
   statement (promoted, then killed at full res).
2. **closed-hardcover query** — a `2|0|2|4` diary (a legible year, and the wrong one), a
   `U.S. MAIL` + `Financial reports` flatlay, and two closed notebooks that would have made s70
   and s81 twins.
3. **typewriter query** (a deliberate object change — a machine that publishes, not a page) —
   dead. Five of six cells carry typed words (`PRIVACY POLICY`, `TERMS OF SERVICE`, `Review`,
   `VALUEABLE`) and the sixth shows an `Olympia` badge. Stock typewriters exist to carry captions.
4. **lifted-corner / shallow-DOF query** — cell 1 promoted.

**What shipped, and the residual risk, stated so the judgement is auditable:** a thick document
with its pages fanning open on a pale wood desk, black cover beneath, green highlighter marks.
It carries **no title, no figure, no agency and no brand** — but roughly 40 words of body prose
are legible at full res in the left third: *"…ate governance is very much an evolving area… the
need to restore investor confidence… governments alike have been proactive… boards are more
accountable, that qualified independent non-exec…"*. It is **corporate-governance prose, not a
withdrawal-rate claim**, so it asserts nothing false and impersonates no source; it is English,
so it carries no wrong-market signal. I judged that below the bar that killed `Sparda-Bank` and
`1 ZŁOTY` (which were brand, currency and language defects). The one text-free alternative on
that sheet was a closed book under orange light — which would have made s70 a near-twin of s81's
closed notebook, trading a small text risk for a repetition defect. **fin-editor's call if it
disagrees; the re-pick is free from the existing sheet (`--pick s70=5`).**

### The s76 / s75 pair — five sheets, and what the pool actually holds

§6b makes **s76 the SOURCE and s75 a tight crop of it** (inverted hold, 15.419 s across the pair),
and §8 is explicit that the photograph does **not** carry the proportions — the drawn bars do
("the photo shows three crates; it cannot show 119 : 156 : 308"). So the frame's only real job is
*a countable line of crates, calm enough to take a drawn bar over it, with a subset that crops*.

Five sheets, and the same spent photograph in five of them (see Failed). What shipped is
**Mathias Reding, `wooden-crates-beside-a-house`**: four stacks of weathered wooden crates
**ascending left to right** — two-high, four-high, then two tall stacks — against a rendered
farm wall under overcast light. Calm, low-key, textless, and the ascending order is legible with
the sound off. The left group is a clean subset for the s75 crop.

**Owed to fin-build, and this is the part the build stage must not miss:** `s75.jpg` does not
exist and cannot be produced here — deriving it needs **ffmpeg, which is on the build stage's
allowlist and not on mine**. It is **not** in `manifest.json` on purpose: `check assets` iterates
the manifest and would fail on a missing file, which is why ch5 also left `s56b`/`s67b` out.
Source is in place at **1880×1253**. Suggested rect, to be verified by eye: a 16:9 crop of about
**`crop=1400:787:60:300`** frames the three ascending stacks with the tall stack at frame right,
so the pull-back to the full frame reveals the two right-hand stacks as rungs four and five. The
convention to follow is ch2's `s10b` / ch4's `s42`: write the crop string into the chapter
manifest as a `derived crop of s76.jpg (no fetch) — ffmpeg crop=…` entry **in the same move**.

### The three forward-referenced drawn layers (s75, s76, s77)

Checked as instructed — a drawn layer buys the photograph nothing. All three photographs satisfy
`image_per_scene` and the sound-off test standing alone: s76 is a countable ascending line of
crates; s77 is one very large container alone in a wide empty field (§10's "one far larger,
alone"); s75 will inherit s76's. All three are also **calm**, which is what §10 asks of the
art-forward frames — s77 in particular is sky-and-grass behind the cut's only element permitted
to leave the frame.

**One declared deviation on s77:** §10's crate rhyme wants "one crate far larger than all the
others, alone in a wide empty bay". Three sheets (18 cells) returned no such frame — the pool's
answer to "one giant crate" is a *wall* of small crates, i.e. the opposite statement. I changed
the object one notch up the same family: **a steel shipping container**, which is a crate at the
next scale and therefore states the escalation the beat needs. Legible marks: a stencilled
**`HJCU 138656`** container ID inside the door frame — an ISO owner code, not a logo; judged at
the same bar as ch5's kept `0004` unit plate and `32` roller-door number.

### The s69 override — honoured in intent, unsourceable in fact

The recorded override (brass plumb bob, dark workshop wall, chosen so that s80's empty chair is
not doubled) was worked through **three sheets and 18 cells across both pools** and the object
does not exist in either: Pexels answers "plumb bob" with brass **taps and plumbing fittings**
— which would have collided with the tank/tap motif at s10/s46/s47/s57 — and Pixabay answers it
with a pineapple, a flower, a rice bowl and cherry blossom (the pixabay search returned nothing
related at all). Two further instrument families were tried and killed: a **spirit level**
(promoted, then killed at full res because the bubble reads *level*) and a **metronome** (1 of 6
cells returned, and it was a Google Home Mini).

What shipped is a **rooster weather vane in silhouette**, compass arms visible, against a pale
sky over clay pantiles. It keeps the override's actual purpose — an instrument, not a chair, so
s80 remains the chapter's only chair — and it states 6.1 more directly than the plumb bob did:
*the answer turns with the wind*. Two flags: the pantile roof reads Mediterranean as easily as
US-Southwest (no signage, plates or vehicles in frame), and a rooster carries a faint
dawn/alarm association that 6.11 later disclaims — I judged both below the bar, and the compass
arms make the object unambiguous.

### Rank / luma — deliberately not a verdict

Per `predictions_missed_a_sixth_time_2026-08-10` I am not handing a rank table downstream;
**settle it on the encode.** What I can say from the promoted frames rather than from prediction:
the chapter's two protected beats are **s77 (the payoff — hero `$5,555,556`, the ladder-overrun)
and s81 (the CTA, the cut's only `--pop` element)**. s77 is the second-brightest frame in the
chapter (open sky) and s81 is a white object on mid-warm wood; **neither is anywhere near the
floor**, so the invariant — *a substantive beat must not be left in the chapter's darkest frame* —
is satisfied by the frames as picked, and I did nothing to chase a rank. The darkest frames are
**s72** (a lit globe on black) and **s79** (a dark phone on dark wood, with a warm highlight band
across the top); both are supporting beats, both hold real subject, real edges and real falloff,
which is the failure the floor actually predicts, and both cleared `YHIGH ≥ 110` on measurement.
Moving either would push a *more* substantive beat down, which the ruling forbids.

## Changed

All under `studio/videos/passive-income-number-en-ch6/assets-ch6/final/`:

- `manifest.json` — created; 12 slots, each query updated to the one that actually found the
  shipped file (7 slots were re-queried between one and five times).
- `s69.jpg` `s70.jpg` `s71.jpg` `s72.jpg` `s73.jpg` `s74.jpg` `s76.jpg` `s77.jpg` `s78.jpg`
  `s79.jpg` `s80.jpg` `s81.jpg` — promoted at full resolution, all 1880 px wide.
- `s*.jpg.src` — 12 sidecars (written by the tool).
- `CREDITS.txt` — **12 rows for 12 files, zero orphans**, all Pexels License, verified against
  disk after the last re-pick.
- `IMAGES-ch6.jpg` + `.json` — built, then rebuilt after the re-picks and re-read.
- `_cand/` — 19 throwaway sheets, left for post-delivery cleanup.

**Accepted 12 / 12. Re-picked 7 after promotion** (s69, s70, s73, s74, s76, s81, and s76 again
after the dedupe collision). **Dropped 0** — every scene keeps its background, per the standing
rule. No lottie in this chapter (`vector_art.lottie` untouched; ch6's drawn layers are the
en measure-bar device, which fin-build generates).

## Owed

1. **`s75.jpg` — a derived crop of `s76.jpg`, owed to fin-build.** ffmpeg is not on this stage's
   allowlist. Rect suggestion and the manifest convention are in Evidence above. Nothing else in
   the chapter derives from another file.
2. **fin-editor's call on s73.** It is the one open editorial question in the chapter, and I am
   naming it rather than burying it: s73 is an **archery target with six arrows scattered from
   the gold out to the blue** — and **ch1's s5 is an archery target with one arrow in the gold**.
   The rhyme is real and it is *undeclared* (§10 lists four returning objects; the target is not
   one of them), and s5's own storyboard note chose the arrow partly because it "cannot be
   mistaken for a pre-echo". Against that: the difference is legible with the sound off (one
   arrow, dead centre, tight crop vs six arrows, scattered, wide with the stand and sky), the two
   frames are 68 scenes apart, and the pairing says exactly what chapter 6 says — *chapter 1
   promised one specific number, chapter 6 admits three answers.* The alternatives are documented
   as spent: blank price tags fail sound-off gate 3 the same way the blank enamel tag did at s5
   (a blank tag states no answer at all), the clock heap failed on Turkish pharma branding and
   `WEST GERMANY`, and a dartboard trades the problem for a gambling connotation on a finance
   channel. If fin-editor wants it gone, that is a fresh sheet, not a re-pick.
3. **fin-editor's second look at s70's legible governance paragraph** (Evidence above). Free
   re-pick available: `--pick s70=5`.
4. **Two Europe-leaning frames, flagged not hidden**: s76 (a French-looking farmyard — rendered
   stone, clay pantiles) and s69 (pantile roof). Neither carries signage, text, plates, vehicles
   or currency, so both clear the mechanical sweep; they are the same class of call as ch5's s64
   ("faintly European" tram rails), which shipped flagged.
5. **s74 does not show the whole ladder** (Evidence above) — a knowing trade, not an oversight.
