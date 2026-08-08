# fin-assets · passive-income-number · hi · chapter 2 · attempt 3

STATUS: ok (with two declared caveats and one open dependency at s20)

Finishes the work the killed attempt-2 dispatch started. `fin-assets-hi-ch2-2.md` is an OLDER
file about the style-A s16 graph-paper defect and is NOT a record of this work — nothing in it
was read as evidence, and nothing in it was clobbered.

**36 contact sheets, ~208 cells seen, 3 accepted.** Every promoted file read at FULL resolution
before acceptance; three were killed only at that read and one only by the md5 sweep.

---

## 1 · What changed

| slot | outgoing | incoming | source p90 (YHIGH) | source YAVG | px | predicted encoded p90 |
|---|---|---|---|---|---|---|
| **s9** | network-rack door + key (killed run, no log) | **₹5 coin macro**, monochrome, lit on a dark ground | 177 → **171** | 79.1 | 1880×1253 | 45.5 → **43.9** |
| **s19** | telecom cable tangle | **black phone, screen OFF**, top-down on slatted wood | 250 → **166** | 113.5 | 1880×1253 | 65.4 → **42.5** |
| **s20** | card-index drawer (graded to green cloth) | **cool grey painted concrete wall**, near-flat, raking light | 123 → **121** | 98.0 | 1733×1300 | 30.8 → **30.3** |

Formula as briefed: `y' = ((0.62y/255 − 0.5)·1.05 + 0.5)·255`, then `× 0.418`. Measured against
this chapter's own rendered values the model runs **~2–8 low** (s16 pred 30.8 / rendered 37.3;
s14 pred 56.9 / rendered 59.0; s20 pred 30.8 / rendered 39.0; s21 pred 46.9 / rendered 43.0), so
treat the column as ±5.

`pipeline_check check assets --slug passive-income-number --cut hi --chapter 2` → **PASS**.
Without `--chapter` it FAILS on the whole-cut manifest — negative control confirmed.
13 CREDITS rows / 13 manifest keys, one per slot. Every file ≥1600 px on the long edge
(min 1724). Every source YHIGH ≥110 (min 121 at s20).

---

## 2 · s9 — the killed run's file was a SERVER RACK. Replaced.

**Verdict on what was on disk: same failure in a new object, and worse than the brief guessed.**

The `.src` said "old steel cabinet door with a key in the lock". At full resolution, and then on a
1000×900 crop of the right two-thirds, the blurred background is **a fan of white patch cables
behind glass, with a green LED bottom-right and blue cabling under it.** It is a network
enclosure. Sound-off it says *data centre*, not *saved money* — and it is the same cable family
the editor blocked at s19, so the killed run had swapped a cable tangle for cables behind glass.

Independently of the background, the brief's suspicion is correct: **a lock reads STORAGE.** The
editor asked for the key because a key restores access, but every locked-container frame in
either pool reads "kept safe", which is the exact statement the two steamer trunks already
shipped. The key does not, on the evidence of 96 cells, change that reading.

**Sixteen sheets for this one slot.** Cash box / padlock / strongbox / almirah / safe / passbook /
money box / gullak / coins, on Pexels, Pixabay and Commons. What the pools actually contain:

- every **cash box** query returns the same grey steel box with a key in the lock and a spread of
  **EURO coins and euro banknotes** in the foreground (returned as cell 1 on four separate queries);
- **almirah / steel cupboard** returns modular kitchens and lockers — a bank of lockers is s58's rung;
- **strongbox / iron chest** returns, as cell 1, **the two steamer trunks the editor blocked**;
- **safe** returns an electronic keypad safe — s62's rung;
- **passbook** returns US dollar bills and a passport;
- **piggy bank** returns cartoon pink pigs — off-brand for this channel;
- `almirah@commons` returns **nothing at all**;
- the one genuinely right object — a carved wooden savings box with a brass coin slot — carries a
  **Nepali २ रुपैयाँ / NEPAL** coin balanced on the slot. Invisible on the sheet, unmissable at full
  resolution. Wrong country's currency on the ₹ cut. Killed.

**Promoted instead: a current Indian ₹5 coin, macro** — «पाँच रुपये», `5`, `FIVE RUPEES`, the
wheat-sheaf reverse — already monochrome, the coin lit against a dark textured ground, two more
coins behind it in shadow. Currency-correct, unmistakably India, no brand, no text but the coin's
own legend, no face, one focal point.

Why this over a container, stated plainly so a later run does not re-litigate it:

1. The editor's actual complaint was *"no money … at the scale it renders."* This frame is money.
2. The script's own chapter note is **"the mechanism in the smallest unit, then rung 1."** A single
   coin IS the smallest unit; the type carries "mechanism".
3. **No notes in frame**, so s16's hero corpus is not pre-spent — which is why the ₹500 flatlays
   that the same queries returned (five of them, all current-series and all clean) were rejected.
4. Monochrome, so the scene's colour role cannot destroy it.

Declared weakness: it is not a container, so it contributes nothing to the ladder — see §5(a),
where that is ruled rather than left open.

---

## 3 · s19 — both named subjects are unbuyable. One is now present, brand-free.

Eight sheets, 46 cells, three pools. The router pool is **RGB gaming units** (magenta/cyan, fatal
under the grade), **legible brand marks** (`tp-link TL-SG1005P`, `NOS`, `WIFI 6`, and on Commons
literally `D-Link DI-524`, `Google WiFi`, `Linksys`, `LevelOne`), or **high-key white pucks**. The
phone pool is lit screens — green, white, an iOS home screen, a Samsung logo, an Apple back.

Two full-resolution / md5 kills on this slot alone:

- a phone-and-keyboard desk shot that looked clean on the sheet: at full resolution the keyboard is
  **German QWERTZ** — `Ü Ö Ä AltGr PgUp/PgDn`, Z where Y is. Foreign localisation on an INR cut.
- a second phone-on-oak shot that passed the sheet AND passed the full-resolution read: the md5
  sweep found it **byte-identical to `passive-income-number-hi-ch1/assets-ch1/final/s4.jpg`** —
  the ch1 scene "the phone face-up beside the glass, screen dark". It would have shipped the same
  photograph twice in one video, 60 seconds apart, with every other check green. Caught only
  because the sweep covered sibling chapters of the same cut, exactly as the brief instructed.

**Promoted: a black phone in a plain black case, screen completely off, top-down on a slatted
wooden bench in daylight.** No logo, no text, no lit screen, no face. The screen is the darkest
object in frame — the inversion of the never-a-lit-screen rule, and the storyboard's own approved
s4 override applied to a new file. md5 `c0d1bcf5…`, unique across all 146 images in `studio/`.

⚠ **DECLARED for fin-editor** — two things, both deliberate:

1. **Only one of the two named subjects is in frame.** The phone is; the internet is not. This is
   an improvement on a frame that carried neither, and it is the editor's own floor ("one object
   per named subject… brand-free"), but it is not the full fix. **Recommended, and cheap:** one
   drawn **wifi-arc icon** (`icon_first` — an inline `<svg class="icon">` with `draw()`, not a
   Lottie) over the phone. That puts both named subjects on screen and is the ch1 s6 pattern —
   three drawn tick cells over three real jars — which this editor already ruled reads *better*
   than the photograph would have. Chapter is at 0 of `max_per_chapter: 4`.
2. **Object-family proximity to the morning phone** (ch1 s1 face-down at first light, ch1 s4
   face-up beside the chai glass; callbacks at s74/s75). This is a different photograph in a
   different state, surface and light — but it is a phone in the middle of the cut, and whether it
   dilutes the ch1→ch7 callback is an editorial call, not mine.

---

## 4 · s20 — the count is not photographable. Routed to drawn art; the photo is the host.

Twelve sheets, ~66 cells. **A countable twelve does not exist in these pools in an acceptable form:**

- every full-year calendar is **Portuguese** (`JANEIRO`, `FEVEREIRO`, `MARÇO`, on 2025 and 2026
  spirals) — foreign signage;
- or it is the same **2021 clipboard**, which I promoted and read at full resolution: twelve months
  are perfectly countable, month names are English — and **`2021 CALENDAR` is set in the largest,
  boldest type on the page**, bigger than every month name. Its YAVG is **184.7** with white paper
  filling ~65% of frame. That is high-key white stock, which the standing rules forbid outright,
  and it would have become the chapter's brightest frame at predicted 62.1 — reproducing the
  editor's own finding #11 (light landing on the least eventful picture) in a new slot. **Rejected
  on both counts**, and rejected consistently with the Portuguese calendar (foreign text) and the
  graph paper (high-key / reads as a UI panel, the discarded s16 defect returning);
- **slips / stubs** return blank-card branding mockups and graph paper;
- **letter-box slots**, which would have said "where the bills arrive", all carry legible
  `LETTERS` / `Mailbox` / `OUTGOING MAIL` / `CORREIO` / `LETTRES`.

So: **fin-editor's option (b).** `vector_art.reach_for_it_when` is explicit that a COUNT is a FAIL
as a flat photograph, not a missed opportunity, and the editor named s20 as an alternative host for
the drawn count in finding #7. The photograph becomes the calm host, which is the storyboard's own
routing for an art-forward frame ("the densest scenes get the calmest backgrounds… near-flat,
low-key subjects").

**Promoted: a cool grey painted concrete wall, near-flat, with a real left-to-right raking
gradient and surface incident** (calm ≠ flat). YAVG 98, YHIGH 121, 1733×1300. It is **cool**, which
is the point: the `--fund` green tint lands on a neutral grey and cannot repeat the
amber-manila-becomes-folded-green-cloth destruction that was half of this blocker. That half of the
blocker is closed outright.

⚠ **DECLARED — two, and the first is a dependency, not a caveat:**

1. **The twelve must be drawn, or this scene states no count.** If fin-build puts the one drawn
   layer at the s17→s18 `÷12` instead (the editor's first choice in #7), **s20 has nothing** and
   the blocker is only half-fixed. The two cannot both host the count (rule 8, and the editor said
   so), so this is a genuine either/or that fin-build must resolve knowingly. If s20 gets it: twelve
   equal marks, arriving across the scene, computed from 30,000 ÷ 12 = 2,500 exactly.
2. **s20 → s21 is now wall → wall.** Cool smooth plaster into warm coursed brick, at a declared
   `dis` between two topics, with different colour temperature and different structure — but it is
   the same class of adjacency as the s12/s13 blocker and I am not going to pretend otherwise. If
   fin-editor rules the pair too close, **re-source s20, not s21**: s21's file was ruled fine and
   only needs its ken retargeted onto the recessed brick (editor #10).

---

## 5 · The two through-line rulings, decided from the files at full resolution

Both are **BINDING on ch3–ch7** and should be written into `run.json`.

### (a) THE CONTAINER LADDER — **rung 1 is s22, and it is ONE box, not two**

Evidence: ch2 ships **no container at all**. s16 is hands counting loose current-series ₹500 notes
and carries a standing DO-NOT-RE-FETCH (it is what killed the demonetised-notes blocker). s9 is now
a coin macro. Sixteen sheets proved no Indian locked money container is buyable, so manufacturing a
rung inside ch2 would cost more fetches for a worse frame.

**RULING:**
- **ch2 is rung 0 — money with no container.** A coin (s9), then loose notes (s16). The climb
  begins the moment a container first appears.
- **Rung 1 = s22 (3.1): ONE small steel cash box.** This overrides §12's "two cash boxes". The
  ladder's own stated law is *"each visibly bigger than the last"* — two boxes side by side is a
  **count**, not a size, and two boxes cannot read as bigger than the nothing that precedes them.
  One box can, and the steel trunk at s31 can then beat one box.
- Ladder as it now stands: **s22 one steel cash box → s31 steel trunk → s58 bank locker → s62 safe
  door.** Four rungs, each unambiguously larger.
- ⚠ **Sourcing warning that this run paid for:** do not query "cash box" on either pool without
  guarding for euro coins. On four separate queries the top hit was a grey steel cash box with a
  key in the lock and a spread of **euro coins and euro banknotes** in front of it. Brief s22 as
  *"closed/open STEEL cash box, no coins or notes of any currency visible except current-series ₹"*
  and **read it at full resolution for euro coins before promoting.** A locker bank and a keypad
  safe also both surfaced repeatedly and both belong to later rungs — reject them at s22.

### (b) THE TANK THROUGH-LINE — hi's own constant, read off hi's own three files

What the three planted files actually are, at full resolution (not what §12 says they are):

- **s11** — a **BLACK plastic rooftop water tank on a white-painted steel frame**, against pale sky,
  a hose tied over the lip (inlet) and a galvanised elbow below (outlet). The South-Asian icon.
- **s12** — **two galvanised bib taps** on an exposed pipe run across a **grey concrete-block wall**,
  outdoors, effectively monochrome. Left tap: **cross/T handle**, bare open mouth. Right tap: a
  white **hose coupling** screwed on.
- **s13** — a warm **brass bib tap with a four-lobe cross handle**, macro, on a dark blurred ground,
  no water.

**RULING — the hi constant is:**

> **A black plastic rooftop tank on a painted steel frame, fed and drained by EXPOSED GALVANISED
> PIPEWORK ending in a HAND-TURNED CROSS-HANDLE BIB TAP, outdoors in daylight.**
> The **tank** carries the wide frames; the **cross-handle bib tap** carries the flow frames.

- This is deliberately **not** the en cut's constant ("aged brass lever tap + industrial pipework
  under daylight, white tiled wall, no vessel in frame"). Different country, different material,
  different vessel — and hi actually *has* a vessel, which en does not.
- **§12's declared constant — "the plain steel body under workshop light" — is now factually wrong
  about three of its six frames and must not be briefed to ch4/ch5.** Nothing on disk is
  steel-bodied and nothing is in a workshop.
- **The refinement the en lesson forces, applied to hi's evidence:** **neither s12 nor s13 shows
  water**, and s12's two taps are differentiated only by a hose coupling. Tap position alone is
  therefore *not* legible in this cut's plants. So **s37/s38 (4.7–4.8) and s44/s45 (5.4–5.5) must be
  briefed for VISIBLE FLOW** — a stream from a cross-handle tap, and the tank's level read against a
  visible fill mark — not for a tap angle. A domestic chrome faucet, a lever tap or a steel brewery
  vessel will NOT read as a callback.

---

## 6 · s12 / s13 — CHECKED at full resolution. The duplication is gone. s13 stays.

The editor's blocker #4 is closed:

| | s12 (as refetched) | s13 (untouched) |
|---|---|---|
| colour | effectively **monochrome**, cool grey | warm **gold** brass |
| scale | two full taps + pipe run on a wall | one tap, **macro** |
| ground | grey concrete blocks, flat daylight | dark blurred stone, raking warm light |
| p90 / YAVG | 200 / 120.3 | 154 / 62.6 |

They do not read as one photograph. **s13 is not re-sourced**, exactly as the editor directed
("Do not fix it at s13 — 'an empty tap' is literally 2.5's cue").

s12 also answers its own blocker: **exactly TWO taps under the kicker `TWO TAPS`.**
⚠ Declared: direction is still only weakly stated — there is no vessel and no water, and the in/out
contrast rests on one tap having a bare mouth and the other a hose coupling. That is better than
five outlets, and it is the best the pool offered; fin-editor should rule it from the encode.

---

## 7 · What my changes do to the chapter's shape — honestly, not much

The chapter's diagnosed problem is that it is **inverted**: the brightest, longest-held frame is a
blank notebook page (s14/s15, source p90 219/218 → predicted 56.9) and the darkest is the hero
corpus (s16, source p90 123 → predicted 30.8).

**I cannot fix that from the asset side, and no future fin-assets run can either.** All three
frames that define the inversion are locked reuses: s16 carries an explicit DO-NOT-RE-FETCH (it is
the file that closed the demonetised-notes blocker), and s14/s15 carry the cut's only `.mega` plus
a render-verified continuous zoom whose crop geometry is already proven (0.91755 vs 0.91754).

What the three replacements actually do:

- **s19 removes the chapter's one blown frame.** Source p90 **250 → 166** (its old YAVG was only
  87.8, so that 250 was pure specular blowout). Predicted encoded **65.4 → 42.5** — it drops out of
  the top of the chapter and into mid-pack, immediately after the ₹2,500 number.
- **s9 and s20 are tonally neutral moves.** 177→171 and 123→121; both land within ~1 point of where
  they were. Deliberate: s9 opens the chapter low and s20 sits low before the close, which is the
  right *direction*; neither has the range to create an arc on its own.
- Net: the chapter still has **no arc**, but it no longer has a false peak on the frame that says
  the least.

**The only remaining lever is a per-scene `filter:` override on s14/s15** to bring the blank page
down toward ~50. I have deliberately **not** taken it, for two reasons: the editor routed the arc to
the CEO to be set across ch1+ch2 together (hi ch1 has never been tone-measured), and creator rule 9
makes darkening a photograph contentious in its own right (*"it fails to black and white"*). My one
per-video override budget is unspent and should be spent there, by the CEO, or not at all.

---

## 8 · Verification

- **md5 sweep across all 146 `.jpg` in `studio/`** (both cuts, every chapter, `_cand/` and
  `renders/` excluded). **Zero shipping duplicates.** The ten pairs that remain are all
  archive-vs-final copies of *intentional* reuses (ch2 s14/s15/s16 ↔ their `style-a/` originals; ch1
  finals ↔ their `style-a/` originals; `superseded-r1/s9` ↔ `style-a/s8`) — none of them ships twice.
- **Cross-pool tell checked:** two CREDITS rows read *"by Pixabay"* — s17 and s18, the adding
  machine. Both pre-date this attempt and the through-line was accepted by the editor, but per the
  known md5 hole that credit is a dedupe warning. Grepped `passive-income-number-en*` for that
  source (`219570` / "adding machine"): **no match**, so there is no cross-cut collision. None of
  my three new files credits Pixabay.
- **CREDITS.txt: 13 rows, 13 manifest keys, one per slot**, all three new rows written by the tool
  on fetch and verified present.
- `pipeline_check check assets --chapter 2` **PASS**; the same command without `--chapter`
  **FAILS** as the negative control (it reads the whole-cut manifest, which has no images yet).
- Every promoted file read at full resolution; s9's outgoing file additionally read as a zoomed
  crop, which is what identified the patch cables.

**Outgoing files were overwritten in place by `--force`, not moved to an archive dir** — noted
rather than hidden. All three were editor-blocked with recorded reasons and their credit rows have
been replaced, so nothing is owed; they are recoverable from their source URLs if ever needed:
s9 `pexels.com/photo/close-up-of-key-in-modern-locking-mechanism-37717005/` (panumas nikhomkhai) ·
s19 `pexels.com/photo/a-bunch-of-tangled-wires-18082922/` (pipop kunachon) ·
s20 `pexels.com/photo/rows-of-folders-11176866/` (George Diamanto).

---

## 9 · Counts

- **Accepted: 3** (s9, s19, s20). **Dropped: 0** — every slot keeps a background.
- **Rejected: ~205 cells across 36 contact sheets** (s9 ×16 sheets, s19 ×8, s20 ×12).
- **Killed after passing their contact sheet — 5**, and this is the number that matters:
  1. **s19** — a German QWERTZ keyboard (`Ü Ö Ä AltGr`) on the INR cut. Full-resolution read.
  2. **s9** — a **Nepali २ रुपैयाँ / NEPAL** coin on an otherwise perfect Indian savings box.
     Full-resolution read.
  3. **s20** — `2021 CALENDAR` as the page's largest type, YAVG 185. Full-resolution read.
  4. **s9 (inherited)** — a fan of white patch cables and a green LED behind glass: a network rack,
     not a cupboard. Zoomed crop of a file that already had a plausible `.src`.
  5. **s19** — byte-identical to **hi ch1 `final/s4.jpg`**. **md5 sweep only.** Nothing else would
     have caught it: it passed the sheet, and it passed the full-resolution read.
- **Two sheets came back short without saying so** (`s20` 1-of-6 on the painted-wall query, `s19`
  4-of-6 on Commons, `s20` 5-of-6 on the night-interior query). Cells were counted, and the
  painted-wall pick came from reading `_cand/s20.json` rather than the tiled sheet.

---

# SCOPE EXTENSION — the CEO ground-temperature ruling (continuation, same attempt)

The en ch2 CEO gate landed mid-run and added two slots: **the hero (s16)** and **the 59.0 plateau
(s14/s15)**. Ruling as received: ground temperature is assigned by **argumentative weight**; the
**payoff frame's photograph must be the most legible in its chapter, never the least**; and **the
lever is always the photograph** — never the ground, never the scrim, never the grade. hi ch2's
target is **UN-INVERTED, not brighter**.

**Both were replaced. And the hero replacement turned out to be mandatory for a reason that has
nothing to do with tone.**

## 10 · ⚠⚠ s16 was PROP MONEY. The DO-NOT-RE-FETCH was protecting a fake.

Instructed to *"read it at full resolution and confirm the corpus figure will sit on something
readable"*, I read it — and then read a 2× crop of its two serial panels.

> **Two distinct ₹500 notes in the same frame both read serial `ILR 176177`.**

Identical serial numbers across notes is reproduction / prop money. Under **the video's first
corpus figure**, on a money channel. It is the demonetised-₹500 failure wearing a different
costume, and it is invisible at contact-sheet size *by construction* — spotting it needs two notes
legible in one frame.

The previous log recorded this file as *"Serial- and series-checked and CLEARED … serial ILR
176177"* and gave it a standing **DO NOT RE-FETCH**. That check read **one** serial and cleared it.
The check is whether **two notes share one**. They do. The instruction was issued to keep
demonetised notes out; it cannot protect a counterfeit, so it is void and I have overridden it.

**The same defect disqualifies a second shoot**, and it is the one the ₹ pool keeps serving: every
frame carrying `6UW 643492` shows **three notes with that one serial**. It came back as a cell on
**five separate ₹ queries** across this attempt. Any future run on this cut should treat `ILR
176177` and `6UW 643492` as known-bad and reject on sight.

**Promoted:** current-series (post-2016 MGNS) ₹500 — modern ascending-size serial panel,
`भारतीय रिज़र्व बैंक`, `केंद्र सरकार द्वारा प्रत्याभूत` — with two ₹-coin stacks and three further notes
layered beneath. **Serials are DISTINCT**: `6HP 962971` on the focal note, `6FS 112…` on the one
beside it. Real currency. No brand, no face-as-subject, no screen, no foreign currency, no
legible text but the notes' own bilingual legends.

**Source p90 123 → 209. Predicted encoded 37.3 → 54.2.** The hero moves from the chapter's trough
to the top of it.

## 11 · s14 / s15 — the plateau is gone, and s15 had to be re-derived

**s14** was the blank spiral pad holding **source p90 219 / rendered 59.0 — the chapter's brightest
value — for 11.6s on no argumentative weight.**

**Promoted:** an open dotted notebook on dark walnut with a **sharpened pencil** and a technical
pen laid across it. **Source p90 219 → 174, predicted encoded 56.9 → 44.7.** The plateau is gone.

Per *"do not simply darken a blank page"*: it is no longer blank. The pencil is 2.6's own cue
(*"a single figure written in **pencil** on ruled paper"*) and it reads *chosen, provisional, not
promised* — which is precisely 2.7's sentence, the one the whole video's honesty rests on. Matte
paper, so it takes the grade without a specular floor. Pen-barrel print checked at 2× zoom:
out of focus, no brand resolves.

⚠ **s15 had to be re-derived, and this is a landmine worth naming.** s15 is not a fetch — it is the
**91.754% centre crop of s14's own source**, and that is what makes the s14→s15 hold one continuous
zoom instead of a self-dissolve. Re-sourcing s14 without re-deriving s15 would have left s15 a crop
of a **completely different photograph**, and the "continuous zoom" would have dissolved mid-hold
to an unrelated frame — with every check still green, because a photograph satisfies
`image_per_scene` merely by loading.

Re-derived at full resolution: **crop 1725×1142 from 1880×1245 at +77+51, ratio 0.91755** — the
same geometry the render already verified on this cut (0.91755 against the specified 0.91754; joint
scdet 0.073 vs 0.184/0.214 either side). 1 ÷ 0.91755 = 1.0899 = s14's ken end scale, so the push-in
remains unbroken. s15 predicted encoded **47.7**.

⚠ **And its credit row was stale.** After the crop, `CREDITS.txt` still credited s15 to the *old*
notebook photographer (Soumith Soman) while the pixels were now MESSALA CIULLA's. That is the
copy-without-its-credit breach the standing rules name, created by my own edit. Re-keyed in the
same move; zero stale rows remain.

## 12 · The chapter is now un-inverted — measured, and hedged where it must be

Every ch2 file, sorted by predicted encoded p90:

| rank | scene | what it is | YAVG | source p90 | predicted encoded p90 |
|---|---|---|---|---|---|
| **1** | **s16** | **HERO — the corpus, ₹10,00,000** | 138.8 | **209** | **54.2** |
| 2 | s11 | rooftop tank, pale sky (accepted plant) | 180.8 | 204 | 52.8 |
| 3 | s12 | two taps | 120.3 | 200 | 51.8 |
| 4 | s18 | ₹2,500 | 117.7 | 196 | 50.7 |
| 5 | s17 | the sum | 115.0 | 194 | 50.1 |
| 6 | s15 | the hold, tighter | 118.7 | 185 | 47.7 |
| 7 | s21 | the first brick | 138.6 | 182 | 46.9 |
| 8 | s10 | SWP, the name | 78.9 | 174 | 44.7 |
| 9 | s14 | the hold, 3.0% | 108.6 | 174 | 44.7 |
| 10 | s9 | ₹5 coin | 79.1 | 171 | 43.9 |
| 11 | s19 | the phone | 113.5 | 166 | 42.5 |
| 12 | s13 | the empty tap | 62.6 | 154 | 39.2 |
| **13** | **s20** | near-flat wall, hosts drawn art | 98.0 | **121** | **30.3** |

**The inversion is reversed.** The brightest frame is the hero corpus; the darkest is a near-flat
texture whose count is drawn. Before: brightest 59.0 = a blank page held 11.6s, darkest 37.3 = the
hero. The 11.6s plateau at the top of the range no longer exists — the hold now sits at 44.7→47.7,
mid-pack, where its argumentative weight puts it.

⚠ **Where the method is not good enough, said plainly.** As briefed, this predictor **over-predicted
en ch2 s20 by 7 points**. Treat the table with the same status as a contact sheet: good enough to
reject, never good enough to certify. Two consequences:

1. **s16 (54.2) leads s11 (52.8) by 1.4 — well inside the error.** The ordering that matters most is
   the one the model is least able to settle. **fin-render must measure the encode**, and if s11
   comes out at or above s16 the lever is **s11's photograph**: it is the pale-sky rooftop tank
   (YAVG 180.8, by far the chapter's highest average), a *plant*, not a payoff, and the editor's
   acceptance of it predates this ruling. It is the correct next file to move, and it is the only
   one — I have not touched it because it is now the anchor of the tank constant ruled in §5(b).
2. The absolute target `encoded p90 ≥ 55` may or may not be met at 54.2 predicted. The **relative**
   clause — most legible in its chapter — is met with the whole chapter measured on one scale.
   That is the clause the invariant actually turns on, and the number was set against the en cut's
   own 59 ceiling, which hi ch2 no longer has.

⚠ **One new adjacency to declare:** with s16 changing from *hands counting notes* to a
*notes-and-coin-stacks still-life*, the chapter now has two money still-lifes — s9 (a single ₹5
coin, monochrome, macro, dark) and s16 (₹500 notes in colour, bright, coins as objects on them).
Different scale, different colour, different point, seven scenes apart — not the s12/s13 class of
defect — but the coin element does now repeat and fin-editor should rule it. Note that s9's ₹5 coin
is the *least* colliding option available: it was chosen specifically because it carries no notes,
and every alternative the ₹ pool offered for s9 was a ₹500 flatlay.

## 13 · What the two through-line rulings look like after the extension

**Unchanged, and now better supported.**

- **(a) Container ladder — rung 1 is still s22.** The new s16 has no container either (loose notes
  and coins), so ch2 remains rung 0: money with no container, from a single coin at s9 to a small
  pile at s16. The climb still begins at s22, and it is still **ONE steel cash box, not two**.
- **(b) Tank constant — unchanged**, and s11 is its anchor, which is exactly why §12's tone note
  above routes any further tone work to s11 as a *decision*, not a reflex.

## 14 · Verification after the extension

- **Zero shipping md5 duplicates** across all of `studio/`. Note that the three ch2 archive
  collisions reported in §8 (s14↔`style-a/s13`, s15↔`style-a/s14`, s16↔`style-a/s11b`) have now
  **disappeared**, because all three files were re-sourced — ch2 no longer reuses a single style-A
  photograph. Remaining pairs are ch1 archive-vs-final only.
- **13 CREDITS rows / 13 manifest keys**, one per slot, with s15's row re-keyed by hand onto its new
  source and zero stale rows.
- `pipeline_check check assets --slug passive-income-number --cut hi --chapter 2` → **PASS**.
- All 13 files ≥1600 px long edge (min 1724); all source YHIGH ≥110 (min 121).
- Full-resolution read on every promoted file, plus 2× serial-panel crops on both the outgoing and
  incoming s16.

## 15 · Revised counts for the whole attempt

- **Accepted: 6** — s9, s14, s15 (derived), s16, s19, s20. **Dropped: 0.**
- **~44 contact sheets, ~250 cells seen.**
- **Full-resolution / md5 kills — 7**, i.e. seven defects that passed a contact sheet:
  1. s19 — German QWERTZ keyboard on the INR cut.
  2. s9 — Nepali `२ रुपैयाँ / NEPAL` coin.
  3. s20 — `2021 CALENDAR` headline + YAVG 185 high-key.
  4. s9 (inherited) — a network patch-cable fan and a green LED behind glass.
  5. s19 — byte-identical to hi ch1 `final/s4.jpg`. **md5 sweep only.**
  6. **s16 (inherited, DO-NOT-RE-FETCH) — prop money, two notes sharing serial `ILR 176177`.**
     2× crop only.
  7. **s15 — a stale credit row created by my own re-derivation.** Caught by re-reading CREDITS
     against the file I had just written, not by any tool.

## NEXT

fin-build: re-draft ch2 (no rebuild needed — same filenames throughout, including the re-derived
s15). Apply the editor's s18 countUp fix (1.2 → 0.45, foot +3.61 → +3.11) and **decide the one
drawn layer knowingly** — the `÷12` at s17→s18 *or* twelve marks at s20; s20 states no count
without it. Recommended second layer: one drawn wifi arc over s19's phone. Then fin-render must
**measure s16 against s11 from the encode** (§12), and §5(a), §5(b) and the two prop-money serials
go into `run.json` before ch3/ch4 assets are sourced.
