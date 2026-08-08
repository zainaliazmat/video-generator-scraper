---
summary: Chapter-4 hi assets, attempt 1. 12/12 slots carry a real photograph — 10 fetched over ~40 contact sheets / ~230 cells, 2 derived crops, 0 reused. THREE shipping duplicates were caught by the cross-cut/sibling-chapter md5 sweep after passing both the sheet and the full-resolution read, one of them against this cut's own ch2. The payoff s34 passes all four clauses on predictions with the median margin safe (+4.9) and the p10 margin inside noise but immunised by the "#1 or #2" wording. s31 was re-briefed on the CONTAINER IDEA after the orchestrator's mid-task correction, and its sound-off verdict is stated on the GRADED frame, not the source.
updated: 2026-08-09
source: measured from studio/videos/passive-income-number-hi-ch4/assets-ch4/final/, predicted through the render simulator re-fitted on the 13 encoded ch2 scenes in fin-render-hi-ch2-2.md (the same fit ch3 used)
---

# fin-assets — passive-income-number hi ch4, attempt 1

Scenes **s31–s40** (lines 4.1–4.10), plus `s34b` (the §6a second framing) and `s35b` (the §10
cut-in) = **12 files**. Project created at `studio/videos/passive-income-number-hi-ch4/` via
`chapter_project.scaffold()`, so its `assets/` symlinks match -hi-ch2/-hi-ch3 exactly. New files
land only in `assets-ch4/final/`.

`pipeline_check check assets --chapter 4` **PASS**. Zero duplicate md5s anywhere under
`studio/videos`. Every file ≥1600 px wide (min 1600, the s34b crop). Every source YHIGH ≥ 110
(min 130).

---

## 0 · The three md5 collisions, because they are the finding of this pass

All three had **already passed the contact sheet AND the full-resolution read** and were sitting
in their slots with credit rows written.

| Slot | Collided with | What it was |
|---|---|---|
| **s38** (r2) | `passive-income-number-en-ch4/assets-ch4/final/s46.jpg` | a cast-iron park standpipe with a genuine thin stream — **the sibling cut's ch4, shipping right now** |
| **s39** (r1) | `passive-income-number-hi-ch2/assets-ch2/final/s10.jpg` | a 1970s office desk with an orange dome lamp — **this cut's own ch2, live** |
| **s38** (r3) | `passive-income-number-hi-ch2/assets-ch2/final/s13.jpg` | a sunlit brass bib-tap macro — **this cut's own ch2, live** |

The third is the most useful: it explains why that brass tap kept returning as the top hit on
every tap query for seven rounds. **ch2 had already spent the pool's best brass tap**, and
nothing but the sweep could see it. Third chapter running that the sweep has earned its place.

The s39 collision also **burned a whole shoot**: the same room, lamp and teal adding machine came
back as two further cells on a later round and were refused on sight.

---

## 1 · The chapter, scene by scene

`d-med` is the median step entering the scene. All values **PREDICTED** through the simulator
(16:9 cover crop → `.bg` `inset:-8%` × mid-scene ken 1.08 → `grayscale(.32) brightness(.62)
contrast(1.05)` → `.field` at .38 → the four `.scrim` layers → BT.601 luma), then through the
affine fit on ch2's thirteen encoded scenes. p90 is **reported only as `p90 − p50`** and ranks
nothing.

| Scene | line | ground | **MEDIAN** | **p10** | **p90−p50** | d-med | sec | sound-off verdict **ON THE GRADED FRAME** |
|---|---|---|---|---|---|---|---|---|
| s31 | 4.1 | `#1c2027` | 27.1 | **14.8** | 18.1 | — | 4.56 | **PASS** — a large domed, iron-banded wooden chest |
| s32 | 4.2 | `#17291f` | 24.8 | 17.6 | 24.6 | −2.3 | 6.18 | **PASS** — a thick stack of old paper sheets |
| s33 | 4.3 | `#17291f` | 29.1 | 19.6 | 18.3 | +4.3 | 6.50 | **PASS** — the same stack, tighter |
| **s34** | 4.4a | `#291f13` | **42.0** | **29.3** | 10.9 | **+12.9** | 5.02 | **PASS** — bowls of rice, lentils and beans |
| **s34b** | 4.4b | `#291f13` | **43.4** | 27.6 | 10.5 | +1.4 | 4.14 | **PASS** — the same bowls, closer |
| s35 | 4.5 | `#2d2214` | **24.4** | 15.7 | 15.5 | −19.0 | 7.98 | **PASS** — open jute sacks of pulses |
| s36 | 4.6 | `#1c2027` | 26.6 | 18.1 | 14.0 | +2.2 | 5.71 | **PASS** — a blank signpost where a path forks |
| s37 | 4.7 | `#301519` | 35.6 | 24.0 | 14.4 | +9.0 | 5.29 | **PASS** — a stepped stone water tank, water low at the bottom |
| s38 | 4.8 | `#2a2113` | 37.7 | 28.4 | **9.6** | +2.1 | 6.18 | **PASS** — a steel tap dripping a thin chain of water |
| s39 | 4.9 | `#191f28` | 34.0 | 24.3 | 13.2 | −3.7 | 8.40 | **PASS** — bundles of paper files tied with string |
| s40 | 4.10 | `#2e2411` | 30.1 | 16.9 | 19.4 | −3.9 | 5.53 | **PASS** — worn stone steps rising |
| s35b | cut-in | — | 23.0 | 12.5 | 19.7 | — | — | **PASS** — fresh vegetables in a steel thali |

    MEDIAN  s34b 43.4 · s34 42.0 · s38 37.7 · s37 35.6 · s39 34.0 · s40 30.1
            · s33 29.1 · s31 27.1 · s36 26.6 · s32 24.8 · s35 24.4
    p10     s34 29.3 · s38 28.4 · s34b 27.6 · s39 24.3 · s37 24.0 · s33 19.6
            · s36 18.1 · s32 17.6 · s40 16.9 · s35 15.7 · s31 14.8

Duration-weighted chapter median **31.7** over 65.50 s. **No frame fails the binary sound-off
gate**, and every verdict above was taken on a SIMULATED COMPOSED FRAME — the source read was
never accepted as the answer, because that is the check s22 passed and the encode failed.

---

## 2 · The payoff: **s34 (4.4, «घर का पूरा राशन» — WHAT ₹10,000 BUYS)**

Nominated on the storyboard's own signals, before any number was looked at: it is the chapter's
**longest scene** (9.159 s), the **only two-framing scene** in the chapter, the only scene §6a
wrote a ruling about, and one of the two lines attempt 3 deliberately **expanded** — its stated
purpose being to mark rung three as *the first rung that pays a need, not a convenience*, which
is the chapter's distinctive claim. (The alternative nomination, s33's `₹10,000 A MONTH` on the
`--fund` ground, is recorded here so the editor can overrule me: on the same numbers s33 is #7
of 10 on median and would FAIL the clause, so the nomination is load-bearing.)

| Clause | Requirement | Result |
|---|---|---|
| **Sound-off gate** (binary, first) | name a concrete object, type covered | **PASS** — nine full bowls of Indian staples: urad, rajma, chana, basmati, masoor dal |
| **MEDIAN top quartile** | `ceil(10/4)` floored at 3 → **top 3** | **PASS — #1 of 10** (42.6 duration-weighted across its two framings), +4.9 over #2 |
| **p10 #1 or #2** | | **PASS — #1 of 10** (28.5 weighted), ahead of s38 by **0.13** |
| **Median step in** | s33 → s34 must not fall | **PASS — +12.9**, the largest step in the chapter |

⚠ **THE p10 MARGIN IS 0.13 AND I WILL NOT CALL IT A MEASUREMENT.** It is inside method noise by
an order of magnitude. It does **not** endanger the clause, and that is the clause working as
designed: the CEO wrote "#1 **or** #2" precisely to retire tests that flip on error, and s34 is
#1 or #2 whichever way this lands. The **median** margin (+4.9 over s38, +6.9 over s37) is the
one that carries the clause, and it is above the ~3-point unsafe line — though this run's
predictor has been wrong by 7–8 points four times, so fin-render should still settle it.

---

## 3 · Clause 1, the floor, and the stopping rule

- **Darkest is s35, 24.4, at 7.984 s** — 4.5's «आटा, दाल, चावल, तेल, दूध और सब्ज़ी … और तनख़्वाह
  में से एक रुपया नहीं गया», which is the payoff itemised, and it carries `#2d2214`, **the
  warmest ground in the whole video**, spent exactly once by §11. A substantive beat, so the
  invariant holds by construction rather than by argument.
- **Longest-held is s34, 9.159 s — and it is now the BRIGHTEST frame in the chapter.** The
  inversion the ruling exists to stop is absent.
- **THE FLOOR, REPORTED NOT CHASED.** Median floor s35 (the ration list, 7.98 s); p10 floor
  **s31, 14.8** — the chapter's opening frame. Under the stopping rule a relocated floor is a
  defect only when the new bottom is the payoff or the longest-held frame, and it is neither.
  I did not spend a round moving it.
- **s31 passes the opening-frame sound-off gate on its own**, which is a gate and not a rank:
  with the type covered the domed lid, three iron bands and painted panels read as a chest.

**DECLARED, NOT BURIED:** three of the chapter's top five frames (s38, s37, s39) are **caveat**
beats — why the tap is small, the money comes out of your own tank, and tax. Only the payoff
outranks them. That is legal under the clause as written and I have not pre-empted a ruling on
it, but if the editor wants the reward frames raised rather than the caveats lowered, the levers
are s33 (a crop, so s32 moves with it) and s35.

---

## 4 · s31 — the container ladder, re-briefed mid-task

⚠ **THE ORCHESTRATOR'S CORRECTION LANDED WHILE THIS SLOT WAS BEING SEARCHED AND CHANGED THE
BRIEF.** I was told to anchor rung 2 to `assets-ch3/final/s22.jpg` and did read that file at full
resolution first (a carved sheesham money box with a brass coin slot, shot as an extreme macro).
Then fin-editor measured s22 on the **encode** and found a pale slab with a slot and no
silhouette. **I re-briefed s31 on the CONTAINER IDEA rather than on that file's silhouette**, and
picked a frame that escalates from *any* legible small money box: one large domed, iron-banded,
hasp-fastened wooden chest, whole object, filling the frame, with a floor and a broom for scale.

- **The ladder is FOUR rungs, s22 → s31 → s58 → s62. s16 is not on it.** I had not read §9c
  before the correction arrived, so nothing was briefed as "rung 3 of five" or "bigger than s16";
  the ruling in `run.json` was the only ladder text used.
- **The two stale places I can confirm from the files:** §10's returning-objects row lists **five**
  rungs starting at s16, and its s22 cell says *"two cash boxes … each visibly bigger than the
  last"* where the shipped file is **one** carved box with no predecessor. §12 contains no ladder
  row at all — the ladder lives in §10, and §9c is the third copy fin-editor found.
- **s31's sound-off verdict is stated on the graded frame**, simulated through the full layer
  stack. This is the test s22 failed, and it is the reason the verdict column above says "on the
  graded frame" for every row.
- Refused over four rounds / 24 cells: riveted steamer trunks (the exact subject ch2's editor
  blocked at s9), padlocks and door bolts, a mannequin torso, an attic of dolls, **the s22 shoot
  itself** (two cells of the temple-donation-box round are the same carved box, one carrying the
  Nepali `2 rupaiyan` coin ch2 killed), a Japanese offering box with legible kanji, and two
  Nepali temple interiors with a legible `DONATION BOX` sign and a person.
- Declared: the chest's painted floral cartouches are Central-Asian/Rajasthani folk in style —
  currency-neutral, no signage, but not provably Indian.

---

## 5 · Full-resolution kills the sheet could not have shown

1. **s32 — a THAI RESTAURANT BILL.** Promoted, credit written, then read at full size: a `CASH
   SALE` counterfoil in Thai script, handwritten `Edamame / Beef Curry / Miso Soup / Avo Roll`,
   total **1,090 baht**, plus a café brand card. ch2 already killed a Thai restaurant bill in
   this cut. On the sheet it was an anonymous warm paper.
2. **s38 — a legible cast `TESTED 20KG`** on the tap body, dead centre where the type sits. Same
   family as this run's `3Kg` and `SEHKO / MT 250` kills.
3. **s34 — three defects in one frame.** A white kitchen cupboard of jars that the sheet made
   look perfect carries an embossed **`Ball` / `WIDE MOUTH` brand** on five jars, **Italian
   pasta** in the last canister, and — worst — **six nearly empty canisters** under
   `WHAT ₹10,000 BUYS / The month's ration`. A frame that argues the opposite of its line, on
   the payoff beat.
4. **s32 (again) — the `LB45440078L` repeated-serial dollar shoot** surfaced as a cell and was
   refused on sight from the known-bad list in `stock-photo-sourcing.md`.

---

## 6 · Overrides against the storyboard, each with its reason

| Slot | Storyboard says | What ships | Why |
|---|---|---|---|
| **s32 / s33** | "a carbon-copy receipt counterfoil"; ch3 added *"must be PAPER or the ledger spine is gone"* | a macro of a thick stack of aged card/paper sheets | **The artefact is paper; the written sum on it is not buyable.** 14 sheets / ~80 cells returned only hands, dollars, euro+VISA, koruna, forint, a `GST 7%` receipt, payment terminals, an Apple wordmark, a US 1040, `At-Will Employment Agreement`, `CHILD ADOPTION CERTIFICATE`, `CONTRACT`, `PRIVATE EQUITY`, a Bible page, an Esperanto dictionary, French book spines, blank spiral notepads (ch2's blank-notebook failure) and the known-bad dollar shoot |
| **s34 / s34b** | "kirana counter, wide" → "tight on the handwritten ration list" | nine full bowls of Indian staples on a light field → a 1.175× push onto the six largest | 9 rounds / ~54 cells: every `indian shop` query returns a European deli with OSRAM/ZEBRA signs, branded shelves (MAIZENA, HINDS, JOLLY), rand-priced jars, `ORGANIC TAPIOCA STARCH` labels, or a shopfront with a scooter/person. A handwritten list in these pools is always English or European handwriting |
| **s36** | "a road sign post with one arm snapped off, plain sky behind" | a **blank** wooden signpost where a gravel path forks | Two rounds returned only US/European signs with legible place names (`MILTON DR`, `GOODHOUSE RD`, `BEST HAMBURGER IN TEXAS`) on wide blue skies — and a plain-sky field is the exact frame the CEO ruled **ineligible to lead** in hi ch2 |
| **s38** | "the same tank's outlet tap opened a quarter turn, a thin steady stream" | a steel bib tap with a thin chain of falling drops | Nearest buyable after 10 rounds; the drips read as "barely open", which is the line |
| **s40** | §10's staircase row: "three worn treads" | worn stone treads, **uncountable** | **run.json's ch1 ruling overrides the storyboard: the staircase is the ladder's METAPHOR, never its INVENTORY — no scene may show a countable number of steps.** Checked against ch1's s7 (a narrow monochrome stairwell shot upward): not a twin |

---

## 7 · Declared for the editor — five things I will not decide alone

1. **s34 and s35 are adjacent and both are grain.** Differentiated by container (ceramic bowls vs
   jute sacks), place (a light table vs a dark shop), light (high-key top-down vs low-key raking)
   and scale, and they carry different halves of one beat — but this is the s12/s13 twinning
   family the ch2 editor blocked.
2. **s32 and s39 are both paper**, five scenes apart: a single-stack macro (warm, raking) vs a
   room-scale field of tied bundles (cool, square-on). Same material twice in one chapter.
3. **s35b carries the vegetables and NOT the milk.** «दूध और सब्ज़ी» names both. Three rounds
   returned either vegetables with no milk or Slavic milk still-lifes with no vegetables and no
   Indian vessel. A cut-in may be dropped rather than faked; the honest half was preferred to a
   faked whole.
4. **s36 is a subalpine conifer forest** — currency-neutral, no signage, no person, no product,
   but visibly not India and the least Indian frame in the chapter. ch1's s3 European tea service
   is already on the books; this is the second.
5. **s37 is made of steps**, and the inherited rule bans countable steps. That rule governs the
   s7/s21/s40/s61/s79 **staircase** family; here the steps are the **tank's** construction, they
   are uncountable, and the same tension already exists in the constant at ch2 s11. The hi tank
   constant is preserved — the Indian stepped stone tank — and **the en cut's brass-tap constant
   was not imported**; s38 is the family's tap frame, not a new constant.

---

## 8 · Every file changed, declared

**Created** (12 images + 12 `.src` + `manifest.json` + `CREDITS.txt`), all under
`studio/videos/passive-income-number-hi-ch4/assets-ch4/final/`:

    s31.jpg  s32.jpg  s33.jpg*  s34.jpg  s34b.jpg*  s35.jpg
    s35b.jpg s36.jpg  s37.jpg   s38.jpg  s39.jpg    s40.jpg      (* = derived crop, no fetch)

**Created** (project scaffold): `studio/videos/passive-income-number-hi-ch4/` — `assets/` symlinks,
`assets-ch4/final/`, `assets-ch4/originals/` (empty; the two crop parents ship as their own slots,
so no archive copy was kept), `renders/`, `package.json`, `node_modules` symlink.

**Derived-crop geometry**, recorded so it can be re-derived:

- `s33.jpg` = **1725×992 from s32's 1880×1084 at +77+46**. Ratios 0.917553 / 0.915129 — ch2/ch3's
  verified hold geometry (1/0.917553 = 1.08986 = `HOLD_A`'s end scale 1.090), so **HOLD_A/HOLD_B
  carry over unchanged**. Encoded `format=yuvj444p` *before* the crop, per ch3's finding.
- `s34b.jpg` = **1600×900 from s34's 1880×1253 at +280+353** — a 1.175× push that stays at
  1600 px and is natively 16:9, so the `.bg` cover-crop discards nothing. The region is the six
  largest bowls, so the push lands on **more** ration, not on empty field.
- **Both credit rows were re-keyed from their parents in the same move**, and both `.src` files
  record the parent dependency: if s32 or s34 is ever re-fetched, the crop must be re-derived in
  the same move or the hold/swap dissolves into an unrelated photograph with every check green.

**Not written:** nothing in `assets/img/` (the cut-level dir), nothing in `tools/`, nothing in
`.claude/`. `_cand/` sheets are throwaway and left in place.

---

## 9 · Counts

- **Accepted 12** — 10 fetched, 2 derived, **0 reused** (this chapter has no §10a reuse row).
- **Rejected ~218 cells over ~40 contact sheets.** Slot cost: s38 **10 rounds** (~58 cells),
  s32 **9 rounds** (~54), s34 **9 rounds** (~54), s31 4, s39 5, s35b 3, s36 2, s35/s37/s40 1 each.
- **Dropped: nothing.** Every background slot is filled and the one cut-in ships (carrying one of
  its two named subjects, declared).
- **3 md5 collisions**, **4 full-resolution kills**, **1 YHIGH gate rejection** (a brass tap on a
  dark wall at source YHIGH 66 — `check assets` caught what my eye had passed).
