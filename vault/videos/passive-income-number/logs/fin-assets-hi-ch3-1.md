---
summary: Chapter-3 hi assets, attempt 1. 9/9 scenes carry a real photograph — 8 fetched over ~47 contact sheets, 1 derived crop; the storyboard's one reuse row was rejected after reading the file. The cross-cut md5 sweep caught TWO shipping duplicates that had already passed both the sheet and the full-resolution read, one of them a file this cut has now killed three times. Payoff s27 passes all four clauses of the round-2 ruling on predictions, with two margins under 3 points declared unsafe.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch3/assets-ch3/final/, predicted through a render simulator re-fitted on the 13 encoded ch2 scenes in fin-render-hi-ch2-2.md
---

# fin-assets — passive-income-number hi ch3, attempt 1

Scenes **s22–s30** (lines 3.1–3.9). Project created at
`studio/videos/passive-income-number-hi-ch3/` via `chapter_project.scaffold()`, so its
`assets/` symlinks match -hi-ch1/-hi-ch2 exactly (css → tools/scaffold, fonts/img/voice/lottie
→ the cut, `js/motion.js` → scaffold, `js/gsap.min.js` + `js/lottie.min.js` → the cut,
`node_modules` → the cut). New files land only in `assets-ch3/final/`.

---

## 0 · The two md5 collisions, because they are the finding of this pass

Both had **already passed the contact sheet AND the full-resolution read** and were sitting in
their slots with credit rows written. Neither would have been caught by any other check.

| Slot | Collided with | What it was |
|---|---|---|
| **s23** (payoff source at the time) | `passive-income-number-hi-ch2/assets-ch2/style-a/s16.jpg` | Pexels **164686**, the high-key ledger the storyboard's own DISCARDED table calls "graph paper that reads as a UI panel". ch2 recorded that it "tried to return twice and was caught both times". **This was its third return.** |
| **s27** | `passive-income-number-en-ch2/assets-ch2/final/s17.jpg` | cottonbro **3838319**, the wooden case of type stamps — *shipping in the other cut, right now*. |

The sibling-chapter + cross-cut sweep is the only reason this chapter is not shipping either.
The ledger kill then cascaded: re-sourcing s23 forced a re-derive of s24 and a change of
artefact for the whole hold pair (§3).

A third hit is **not** a defect and is declared: `assets-ch3/originals/s22-original.jpg`
(the archived, unshipped parent of the s22 crop) is byte-identical to
`assets-ch2/style-a/s11.jpg`. Both are archives; the shipped crop is unique. See §2.

**Zero duplicate md5s among the 112 shipping/archive images under `studio/videos`** that are
not archive-vs-archive pairs. Every remaining duplicate group is `final ↔ superseded-r*` or
`final ↔ style-a` inside ch1/ch2, i.e. pre-existing archive aliases.

---

## 1 · The predictor, re-fitted before anything was bought

The ch2 simulator did not survive its session, so it was rebuilt and re-fitted against **all
thirteen encoded scenes** in `fin-render-hi-ch2-2.md` (using `superseded-r2/` for the four
files that were live at that render). Model: 16:9 cover crop → `.bg` `inset:-8%` × the
mid-scene ken scale 1.08 → sRGB `grayscale(.32) brightness(.62) contrast(1.05)` → `.field`
(`--f1` → `--bg`, 158°) at .38 with `.rules`/`.glow` → the four `.scrim` layers → BT.601 luma.

| Measure | Affine fit | RMS | max abs residual | rho |
|---|---|---|---|---|
| **median** | `1.0908x + 1.31` | **1.93** | 3.86 | 0.959 |
| **p10** | `1.9380x − 15.74` | **0.88** | 1.41 | 0.988 |
| p90 | `0.635x + 20.22` | 3.75→**2.27** | 4.67 | **0.894** |

Same conclusion ch2 reached independently: **median and p10 are predictable, p90 is not a
property of the photograph.** p10's slope of 1.94 means the fit amplifies small simulated
differences, so p10 ranks are reported but p10 *gaps* under ~1.5 are noise.

**These are predictions. Only the encode settles.** This run's record is −7.1 / +8.6 / +7.5
errors and one declared 1.4-point lead that became an 8.0-point deficit.

---

## 2 · The chapter, scene by scene

`d-med` is the median step entering the scene. All values PREDICTED.

| Scene | line | ground | **MEDIAN** | **p10** | **p90−p50** | d-med | sec | sound-off: what a viewer could name with the type covered |
|---|---|---|---|---|---|---|---|---|
| s22 | 3.1 | `#1c2027` | **33.3** | 18.8 | 12.5 | — | 5.42 | **PASS** — a wooden money box with a brass coin slot |
| s23 | 3.2 | `#17291f` | 24.8 | 12.7 | 22.0 | −8.5 | 6.13 | **PASS** — an abacus |
| s24 | 3.3 | `#17291f` | 28.3 | 14.3 | 19.5 | +3.5 | 6.05 | **PASS** — the same abacus, tighter |
| s25 | 3.4 | `#1f1e1c` | 30.2 | 14.9 | 15.3 | +2.0 | 6.78 | **PASS** — an old electric fan |
| s26 | 3.5 | `#291f13` | **22.3** | 14.6 | 16.9 | −8.0 | 8.22 | **PASS** — an old electricity meter with counting dials |
| **s27** | 3.6 | `#2a2113` | **31.9** | **21.0** | 15.3 | **+9.6** | **8.98** | **PASS** — a rubber stamp and a numbering stamp on a counter of forms |
| s28 | 3.7 | `#1a1e24` | 30.3 | 19.8 | 11.2 | −1.6 | 8.51 | **PASS** — a two-pan brass balance |
| s29 | 3.8 | `#2b1418` | 30.2 | **21.7** | 13.8 | −0.1 | 5.40 | **PASS** — a cluster of horn loudspeakers on a pole |
| s30 | 3.9 | `#1f1e1c` | 28.9 | 19.6 | 23.9 | −1.3 | 5.66 | **PASS** — a wooden bullock cart at rest |

    MEDIAN  s22 33.3 · s27 31.9 · s28 30.3 · s25 30.2 · s29 30.2 · s30 28.9 · s24 28.3
            · s23 24.8 · s26 22.3
    p10     s29 21.7 · s27 21.0 · s28 19.8 · s30 19.6 · s22 18.8 · s25 14.9 · s26 14.6
            · s24 14.3 · s23 12.7

Duration-weighted chapter median **28.8**. No frame fails the binary sound-off gate — there is
no blank wall, no pale-sky field and no closed notebook in this chapter.

### The payoff: **s27 (3.6, THE RATE HELD, `num 3.0%`)**

Nominated on the storyboard's own signals, not on the numbers: it is the chapter's **thesis**
(«दर हर सीढ़ी पर एक ही मुहर है, बदलती सिर्फ़ रक़म है»), the **longest scene** (8.976s), the only
scene carrying `pop`, the only content `stamp` SFX, and the only one §6c wrote a ruling about.

| Clause | Requirement | Result |
|---|---|---|
| **Sound-off gate** (binary, first) | name a concrete object | **PASS** — a wooden rubber stamp and a metal numbering stamp standing on a ruled form |
| **MEDIAN top quartile** | `ceil(9/4)` floored at 3 → **top 3** | **PASS — #2 of 9** (31.9), behind s22 by 1.4 |
| **p10 #1 or #2** | | **PASS — #2 of 9** (21.0), behind s29 by 0.7 |
| **Median step in** | s26 → s27 must not fall | **PASS — +9.6**, the largest step in the chapter |

⚠ **TWO MARGINS I WILL NOT CALL SAFE, DECLARED NOT BURIED.** s27 leads #4 (s25, 30.2) on
median by **1.6**, and leads #3 (s28, 19.8) on p10 by **1.2**. Both are inside this run's
measured error. If the encode inverts either, **the lever is s25 on median and s28 on p10** —
in that order, and neither is a payoff beat. The clause survives a swap with s22 (median) or
s29 (p10) because it grants #1 *or* #2; it does not survive a slip to #3.

### Clause 1 — the darkest longest-held frame

- **Darkest is s26, 22.3, at 8.219s** — line 3.5, «मई में जो बिल देखकर घर में बहस होती है…»,
  the May argument. That is the chapter's lived consequence and its warmest ground; the
  invariant is satisfied by construction, not by argument.
- **Longest-held is the s23→s24 hold, 12.180s**, at median 24.8/28.3 (8th/7th) — the rung's
  arithmetic and the chapter's derived income figure `₹5,000`. Substantive.
- **The median leader is s22** (the container-ladder rung), not an empty frame. Nothing bright
  and featureless is at the top of this chapter.

---

## 3 · Every file changed, declared

| File | Source | What it is |
|---|---|---|
| `s22.jpg` | fetched + **cropped** | carved wooden money box, brass coin slot — 1880×740 crop at +0+513 |
| `s23.jpg` | fetched | soroban abacus, top-down on a woven mat |
| `s24.jpg` | **derived crop of s23** | 1725×1147 at +77+51, ratio 0.917553 |
| `s25.jpg` | fetched | vintage metal desk fan, close |
| `s26.jpg` | fetched + **cropped** | rusted kWh meter, dials — 1880×790 crop at +0+0 |
| `s27.jpg` | fetched + **cropped** | clerk's counter, rubber stamp + numbering stamp — 1880×900 crop at +0+0 |
| `s28.jpg` | fetched | two-pan brass balance on a wooden shelf |
| `s29.jpg` | fetched | six horn loudspeakers on a pole |
| `s30.jpg` | fetched | empty bullock cart at rest, rural road |

Also written: `manifest.json` (9 keys, each with its full rationale), `CREDITS.txt` (9 rows),
nine `.src` files, and `assets-ch3/originals/{s22,s26,s27}-original.jpg` (the three uncropped
parents, archived, **not** in the manifest and **not** shipped). Plus the project scaffold
(`assets/` symlinks, `package.json`, `renders/`) and the throwaway `_cand/` sheets.
**Nothing outside `studio/videos/passive-income-number-hi-ch3/` was touched.**

### The three crops are load-bearing, not tidying

- **s26** — the uncropped frame carries `CHAMBERLAIN & HOOKHAM LTD / SOLAR WORKS / BIRMINGHAM`
  on the maker's plate: a readable brand mark *and* a British city, which would have been the
  **third European frame** the brief forbids. Cropping to the top 63% removes it. What is left
  is generic metering English (`THOUSANDS. HUNDREDS. TENS. UNITS.`, `KILOWATT-HOURS`).
- **s22** — the parent carries a **`NEPAL / २ रुपैयाँ` coin** balanced on the slot: the exact
  frame `fin-assets-hi-ch2-3` §5 killed ("wrong country's currency on the ₹ cut"). The crop
  removes the coin entirely, so the shipped frame carries no currency of any country. That was
  the kill's only stated cause, and it is gone.
- **s27** — the parent carries two pale-blue cards reading **`GESCHIKT`** at the foot of the
  frame. Cropped out. (Residual declared in §5.)

---

## 4 · Five overrides against the storyboard, each with its reason

1. **s22 — the container ladder's rung 1 is NOT a steel cash box.** The ch2 ruling is explicit
   and I could not honour it: **ten sheets, ~60 cells**, across Pixabay, Pexels and Commons.
   `cash box` returns the grey steel box with euro coins and euro banknotes that ch2 already
   documented (cell 1, four separate queries, again here). `lock box` returns padlocks on
   doors. `petty cash` and `shop drawer` return payment terminals and foreign notes.
   `cash register` is dollar-denominated — ch2's own finding. `cash box steel@commons` returns
   two men on a lawn. What ships is the object the rung needs rather than the object the
   ruling names: **one carved sheesham money box with a brass coin slot, filling the frame.**
   It is a container, it is Indian, it carries no denomination, and the steel trunk at s31
   still beats it. **The ladder is unbroken: s22 one wooden money box → s31 steel trunk →
   s58 bank locker → s62 safe door.**
2. **s23/s24 — the "cloth-bound account register" is an abacus.** Forced, and this is the one
   override I would most like the editor to look at. Seven ledger sheets produced exactly two
   usable ledgers and **both are named prior kills on this cut** (§0: the graph-paper file and
   the `Dodge Pickup / New DODGE CITY / STANDARD PROPERTY LEDGER FORM 20-A` US asset ledger).
   Everything else was a US 1040, a `GST 7%` receipt, euro notes, German diaries, or an Italian
   1813 register. An abacus carries **no text in any language**, no currency and no country,
   and it says the line («हिसाब सामने कीजिए»). ⚠ It also makes **two consecutive rungs whose
   paper artefact is a calculating device** (ch2's adding machine, now this). **ch4's s32/s33
   counterfoil must be paper** or §10's five-artefact ledger spine is gone.
3. **s25 — the Indian electricity bill is a fan.** Four sheets: every printed bill in these
   pools is a US utility statement, a `GST 7%` Singapore receipt, a 1040, a euro flatlay or a
   lit laptop, and half of every sheet carried hands. §10 already routes 3.4/3.5 as
   "bg and meter carry it across two frames", so s25 takes the **cost** and s26 the **meter**.
4. **s28 — the storyboard's reuse row is rejected**, which is what the row itself asks for
   ("VERIFY BEFORE PROMOTING: 3.7's balance must put two clearly different weights in frame").
   Read at full resolution, `assets-ch1/style-a/s7.jpg` is a **Chinese-medicine dispensary**:
   one hanging pan heaped with dried herbs, one counterweight, jars behind. It shows no second
   weight, and §10 routes the two `art-forward` scenes to the **calmest** backgrounds — it is
   the busiest frame that was available. A head-on empty two-pan brass balance replaces it.
   §8 is explicit that the drawn `corpus-doubles` layer, not the photograph, asserts the 2.00×.
5. **s29 — the glossy flyers are loudspeakers.** Four sheets returned `BLACK FRIDAY SALE
   25% off`, `SALE / VENDITA / AUSVERKAUF / REBAJA`, a pile of red `50% 30% 10%` cards
   (competing percentages under a 3.0% video, and a pre-spend of 5.2's `10% OR 12%` beat),
   a **PEXELS**-branded sticker pile, and torn-poster walls with legible Norwegian and Arabic.
   Six horn loudspeakers on a pole say *amplification* — «बहुत बड़ा और बहुत जल्दी बना दिया जाता है» —
   with no text at all, and it is a street object at home in India.

---

## 5 · Rejections — ~47 sheets, ~270 cells

**Killed at full resolution after promotion** (the sheet could not have shown any of these):

- **s22** — `नेपाल NEPAL / २ रुपैयाँ` on the coin, the ch2 kill returning. Cropped out, kept.
- **s26** — `CHAMBERLAIN & HOOKHAM LTD / SOLAR WORKS / BIRMINGHAM`. Cropped out, kept.
- **s27** — `GESCHIKT` ×2 on the pale-blue cards. Cropped out, kept.
- **s29** — a **`TOA`** brand mark inside the horn mouth, dead centre where the type lands.
  Replaced.
- **s23** — the `Dodge Pickup / New DODGE CITY / STANDARD PROPERTY LEDGER FORM 20-A` US asset
  ledger, a ch2 kill. Replaced.
- **s25** — Min An 1650031, a moulded **`SEHKO`** + `MT 250` on the fan housing. Replaced.
- **s25** — Mike van Schoonderwalt's cabin fan: a **phone with a charging cable** in frame
  (it would have muddied the ch1→ch7 phone callback) plus a foreign wall socket. Replaced.

**Rejected on the sheet**, by family: euro cash boxes and euro/złoty note flatlays; the whole
`6UW 643492` prop-money shoot (three of six cells on one s22 sheet, exactly as recorded);
US 1040s, income statements, `TAXES DUE 4/15`, CASIO calculators with dollar bills; hands
(the single commonest reason — ~30 cells across the stamp, ledger and bill queries); faces
(five of six cells on the first s30 sheet, children on three abacus cells, a fan-repair-shop
portrait); legible German (`GEDRUCKT`, `Für Ihre Akten`, `VermAnG`), Italian (`ENTRATE 1813`),
Dutch, Norwegian, Arabic and Swedish (`Kakor / Kaffe`); letterpress words (`PASSION`,
`SHOWTIME`, `ACHIEVEMENT`, `INSPIRE`, `OUTRO`, `THE END`); brands (`Jim Beam`, `PEXELS`,
`SmartMeter`); high-key white stacks and beige flat-lays; European and Turkish farm wagons
(cobblestones, Cappadocian fairy chimneys); Lady Justice; and a spin-blur pinwheel round.

**Tooling notes, both already documented and both confirmed here:** one s29 sheet came back
**3 of 6** with no warning; the Commons sheet came back **1 of 1** and the single cell was
irrelevant to the query.

---

## 6 · Caveats left for fin-editor to rule from the encode

1. **s27's residual Dutch.** After the crop, a partly-occluded **`GESC`** sits behind the
   wooden stamp (~50 px in an 1880-wide file, rotated, half-hidden) plus small rotated form
   text (`AANGIFTE TOT INVO…`, `SOORT VAN DE GOEDEREN`). It is not currency, not a brand and
   not a country name, and eight stamp sheets produced no cleaner frame that was not a hand,
   a German law book, a letterpress word, ch2's own adding machine, or the en-cut duplicate.
   **If the editor rules it a blocker, the stamp through-line (s8 → s27 → s77) has to be
   re-briefed, not re-fetched** — the object is not in these pools.
2. **s23/s24: the ledger spine is now half devices.** See §4.2.
3. **s28 shows no weights.** A level, empty balance. It is the calm host §10 asks for and §8
   says the drawn layer carries the ratio — but if the editor wants two weights, the frame has
   to change and the drawn layer becomes redundant.
4. **s28 carries a cast `3Kg`** on the beam (~1.5% of frame width) under a scene printing
   `₹10,00,000 TO ₹20,00,000`. Small, and a capacity mark rather than a competing figure.
5. **s30 has one unidentifiable human figure**, ~15 px, on the far road. Not the subject.
6. **s22 is from the shoot ch2 killed.** Declared in full in §3; the cause of that kill is not
   in the shipped frame, but a later pass should not rediscover the association and panic.
7. **Ground variety:** wood at s22/s28/s30, metal at s25/s26/s29, paper/bead at s23/s24, mixed
   at s27 — 3 of 9 on wood, against hi ch1's 6 of 8.

## 7 · Checks

- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut hi
  --chapter 3` → **PASS assets-hi**. (Its attribution-vs-composition assertion currently
  reaches nothing, because ch3 has no `index.html` yet — **fin-build must re-run it after the
  build**, when that assertion becomes the one that cannot go stale.)
- **9 manifest keys = 9 files on disk = 9 CREDITS rows**, verified by set equality. No orphan,
  no stale row; `s24`'s row is re-keyed from `s23` in the same move as the crop, and the three
  crops carry a note naming their archived parent.
- **All 9 ≥ 1600 px wide** (min 1725 on the derived crop; eight at 1880 or 1733).
- **All 9 source `YHIGH` ≥ 110** — min **118** (s26), then 119 (s29), 170, 182, 185, 186, 223,
  223, 228.
- **Zero duplicate md5s among shipping images across all of `studio/videos`** (112 files
  swept, `_cand/`, `renders/`, `snapshots/` excluded). The only ch3 hit is the archived,
  unshipped `originals/s22-original.jpg`, declared in §0.
- **Every promoted file read at FULL RESOLUTION before acceptance** — all nine, plus the seven
  that were promoted and then killed or cropped.
- No lottie was asked for in ch3 (§8 gives it one drawn layer, `corpus-doubles` on s28, which
  is fin-build's).

## Verdict

**PASS.** 9/9 scenes carry a real photograph: **8 fetched, 1 derived, 0 reused** (the one
storyboard reuse row rejected on the file). The payoff satisfies all four clauses of the
round-2 ruling on predictions — gate, **#2 of 9 median**, **#2 of 9 p10**, step in **+9.6** —
and the chapter's darkest frame is its lived consequence rather than a throwaway. The two
numbers I would not defend as safe are s27's **1.6**-point median lead over s25 and its
**1.2**-point p10 lead over s28; fin-render must settle both from the encode.
