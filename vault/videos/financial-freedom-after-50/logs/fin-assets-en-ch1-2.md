# fin-assets · financial-freedom-after-50 · en · chapter 1 · attempt 2

REWORK pass against `logs/review-en-ch1-1.md`. 6 slots re-picked (s3, s5, s6, s9, s10, s11),
5 slots untouched (s1, s2, s4, s7, s8). 6 contact-sheet rounds, 11 full-resolution reads,
2 promoted-sheet reads.

## Ran

1. Baseline: `pipeline_check check assets --chapter 1` → PASS; cross-project md5 (`find` form,
   both layouts) → empty.
2. Round 1 sheets (`--candidates 6 --only s3 s5 s6 s9 s10 s11`, all `@pexels`): index-card,
   older-chess, trading-floor, handwritten-cards, note-cards, hand-placing-card queries.
3. Round 2 sheets: s3 `five wooden blocks in a row…`, s6 `New York Stock Exchange building
   facade@commons`, s9 `sticky notes in a row…`, s10 `note cards pinned in a row on string`,
   s11 `hand placing wooden block…`.
4. Round 3 sheets: s3 `wooden numbers one two three four five…`, s9 (same pinned-cards pool
   promoted full-res to see the three cells whose previews never rendered), s11
   `hand opening door to bright sunlight outside`.
5. Round 4 sheets: s9 `hundred dollar bills on dark wooden table`, s10 `bridge over river in
   morning light`, then s10 `Golden Gate Bridge San Francisco@commons`.
6. Promoted `s3=1, s5=6, s6=2, s9=6, s10=6, s11=4`; rebuilt `IMAGES-ch1.jpg` twice and read it
   twice (the first read found a defect the per-image reads could not — see Evidence 6).
7. Final: md5 dedupe → empty; `pipeline_check check assets --chapter 1` → PASS.

`--only` was used on every `--candidates` call. It is a narrowing flag on the allowlisted
command; without it each round would have re-searched all 11 slots and re-downloaded 66
previews to look at 6.

## Failed

- **`five index cards in a row on wooden table@pexels` — all 6 cells rejected.** The pool has
  no row of five discrete cards. Cell 3 was four blank cards in a 2×2 grid (a frame stating
  FOUR under "five-step plan" argues with the line — worse than bland); cell 4 carried
  "Products to help you reach your goals" plus credit cards (readable brand marks); cell 5 was
  four aces (a bet, on a line whose stmt is "A system, not a bet"); cell 2 was the incumbent
  s3 fan. **No stock photograph of "five countable cards in a row" exists in either pool** —
  three separate queries across two rounds returned zero.
- **`stock exchange trading floor traders@pexels` — all 6 cells rejected.** Every one was a
  monitor wall of candlestick charts, i.e. someone else's UI as the brightest thing in frame.
  That is the phone-screen-as-background trap in a bigger bezel.
- **`handwritten index cards…`, `sticky notes in a row…`, `note cards pinned in a row…` — all
  rejected.** Diwali/New-Year calligraphy cards (wrong market), a corkboard note reading
  "ASK ABOUT BITCOIN" (crypto prop from a query that never mentioned crypto — the failure mode
  rule 3 names), "NO racism"/"Black Lives Matter" lettered cards, Apple keyboards.
- **`hand placing blank card on wooden table@pexels` — all 6 rejected.** Every cell was a blank
  business-card mockup. Sound-off it says "here is my business card", not "Step one."
- **`bridge over river in morning light@pexels` cell 6, promoted then rejected at full res** —
  a red DB-livery European commuter train crossing, plus graffiti on the abutment. A European
  commuter train is a place cue in a US-market cut; re-picked from `@commons`.

## Evidence

**1 — s3, the count blocker. `s3.jpg` = wooden numerals `1 2 3 4 5` in a row, with a matching
row of five blocks beneath them** (pexels 1329292, 5472×3648 source, 116,321 b).
`.src` = `wooden numbers one two three four five on wooden table@pexels`. Read at full
resolution: five numerals, in order, no sixth, no text, no brand mark. Three of the six cells
in that sheet stated the WRONG count (`123456`, `1234567`, `123`) and were rejected on it —
the count is the whole job of this frame. The ground is a saturated red field; under the locked
`grayscale(.32) brightness(.62)` it resolves to a deep maroon, not a bright red, and it is the
only graphic frame in the chapter, which is why it now also breaks the s2–s7 tabletop run.
**No drawn layer was added** — chapter 1 stays at 0 of 4, as storyboard §8 declares.

**2 — s5, the young-hands finding.** Re-picked (pexels 8865110, 6688×4459). Full-res read: an
aged hand — visible knuckle structure, loose skin — moving a black pawn; the opponent is
present, blurred, no face in frame. The gold sports watch and smooth skin of the old pick are
gone. The chess metaphor the reviewer asked to keep is unchanged.

**3 — s6, the flat-run break (P2 finding 6).** `s6.jpg` = the American Stock Exchange facade
from street level, Commons, 1880×1253, CC BY-SA 3.0, Patrick Nouhailler. Full-res read:
`AMERICAN STOCK EXCHANGE` cut into the stone is the only legible text and it is the thing the
line names; no advertising, no people, no screens, blown-out sky so highlights are real.
Rejected from the same sheet: cell 6 carried a `KEYSIGHT TECHNOLOGIES` banner (brand mark) and
cell 4 — the NYSE with flag drapes, the better photograph — carried Christmas wreaths and
string lights, which date an evergreen video. Cells 1 and 3 were dense bronze plaques.

**4 — s9, half of the two-staircase blocker.** The card chain the reviewer specified is not
sourceable (see Failed), so s9 leaves the card family entirely: `s9.jpg` = a single US $100
note on dark woven cloth (pexels 10149290, 8192×5464). Full-res read: **one** note, so the
shared-serial prop-money test is not applicable by construction; `HUNDRED DOLLARS`, `100` and
the green seal are legible and correct; pre-2013 series, which is still legal US tender and
not the demonetised-note failure class. It is the chapter's only money frame, on the line that
announces the savings steps. **Cell 2 of that same sheet was rejected on the serial rule** —
two notes in one frame both read `73395666` (`B2 73395666 R` and `MB 73395666 R`), i.e. one
plate, i.e. prop money.

**5 — s11, the crushed closing frame. REPLACED, not re-framed.** Judgement the parent asked
for: the old `hand opening door morning light` source is a near-black door filling frame with
vertical grain and a hand at the same value as the wood — the hand and handle are legible at
1:1 only because nothing is competing, and there is no framing of it that survives the grade
plus the scrim, because the frame contains no highlight to protect. It is replaced by pexels
35349316 (3888×2592): a door standing open in a black interior onto a sunlit tree, water and
paving. Full-res read: no text, no faces, no brand. Contrast is the point — a bright aperture
inside a black field cannot crush, and it is the chapter's green hand-off ("Let's start
building that future, right now", `#12351f`). The `hand` of the storyboard prompt is gone; the
door and the light are what the line needs.

**6 — the defect only the promoted sheet could show.** On the first `IMAGES-ch1.jpg` rebuild,
s10 (stone stairway to a blown-out sky) and s11 (dark room to a sunlit doorway) sat next to
each other and said the same sentence — *dark passage opening onto light* — on consecutive
scenes at 56.9 s and 65.1 s. Each had passed its own per-image read. That is the s9/s10
repeat blocker reappearing one slot to the right, and it is exactly what the grid exists to
catch. s10 was re-fetched: **`s10.jpg` = the Golden Gate Bridge at golden hour from the Fort
Point shore** (Commons `GG-ftpoint-bridge-2_b.jpg`, 1880×1253, **CC BY 2.5**, David Ball /
Georgfotoart). Sound-off it reads *crossing over* — the last of its three chips is
`5 Transition` — it is US-correct, it repeats nothing (the only landmark and the only water in
the chapter), and no other slot in the whole 126-slot cut uses a bridge, so nothing downstream
is stolen.

**7 — second promoted-sheet read, final 11.** No two cells say the same thing. Closest
kinships, both judged acceptable: s2 and s7 are shallow-DOF tabletop objects but different
objects on lines 20 s apart with s3–s6 between them; s4 and s10 are both wide warm exteriors
but a suburban street and a suspension bridge. The s2–s7 run the reviewer called flat is now
broken twice inside itself — s3 (graphic, red) and s6 (architecture, vertical, grey) — not
once.

**8 — acceptance numbers.** `pipeline_check check assets --slug financial-freedom-after-50
--cut en --chapter 1` → **PASS**, so every one of the 11 promoted images clears
`min_image_bytes` 10240 (smallest: s3 at 116,321 b), `min_source_yhigh` 110 (including the
mostly-black s11 — its aperture is what the 90th percentile lands on), and every image
`index.html` renders has an attribution row. Every promoted source is **≥1880 px wide**
against `assets.min_width_px` 1600 — Pexels picks land at 1880, Commons at 1880, and the raw
sources for the two zoom-heavy slots are 5472×3648 (s3) and 8192×5464 (s9). No Pixabay
anywhere in this chapter.

**9 — dedupe.** `find studio/videos vault/videos \( -path '*/final/*.jpg' -o -path
'*/assets/img/*.jpg' \) -print0 | xargs -0 md5sum | sort | uniq -Dw32` → **empty output**,
run after the last pick. No collision anywhere on the channel.

**10 — lossy sheets, counted.** `_cand/s10.jpg` rendered **3 of 6** cells on the pinned-cards
query and **1 of 6** on the Commons Golden Gate query; `_cand/s9.jpg` rendered 3 of 6 on the
same pinned-cards pool. In every case the JSON held all 6 and was read; where a candidate
could not be previewed and looked promising by title it was promoted full-res and looked at
(that is how the Italian festival cards below were caught). No sheet was treated as a failed
query on cell count alone.

**11 — what the thumbnail could not have caught.** `s9` at contact-sheet size, cell 2: two
serials, identical. `s9`'s earlier pick (pinned "note cards", pexels 1467217) at contact-sheet
size: a row of blank cards on a line — at full resolution, an Italian literary-festival card
carrying legible Italian copy, two sponsor logos (`alce nero`, Festivaletteratura) and three
social handles. Promoted, read, rejected, re-picked. Both looks were owed and they answered
different questions.

## Changed

| slot | before | after | why |
|---|---|---|---|
| s3 | fanned stack of ~10 ruled index cards | wooden numerals `1 2 3 4 5` + five blocks (pexels 1329292) | P1 #1 — the count is now stated, countable, in order |
| s5 | chess, young hand + gold watch | chess, aged hand, opponent present (pexels 8865110) | P1 #5 should-fix — script's 50-and-older photography rule |
| s6 | folded newspaper + coffee mug | American Stock Exchange facade (Commons, CC BY-SA 3.0) | P2 #6 — the tabletop run's weakest frame, replaced with scale |
| s9 | wooden staircase against brick | single US $100 note, dark cloth (pexels 10149290) | P1 #2 — one of the two staircases is gone |
| s10 | stone staircase to sunlight | Golden Gate Bridge, Fort Point shore (Commons, CC BY 2.5) | P1 #2 + the s10/s11 repeat the promoted sheet exposed |
| s11 | hand on a dark door handle | open door onto sunlit ground (pexels 35349316) | P1 #4 — replaced, not re-framed |

Untouched: s1, s2, s4, s7, s8 (s1 explicitly per the reviewer's "do not touch it").

Files written: `studio/videos/financial-freedom-after-50-en-ch1/assets-ch1/final/{s3,s5,s6,s9,s10,s11}.jpg`
+ their `.src` sidecars, `CREDITS.txt` (11 rows, 1:1 with the 11 images, re-keyed in place on
every re-pick — the two Commons rows are licence conditions), `manifest.json` (6 queries
updated, `_note` rewritten to record why two slots are `@commons`), `IMAGES-ch1.jpg` +
`IMAGES-ch1.json`. `_cand/` sheets left in place as throwaway.

## Owed

**To fin-build — three framing notes, one of them a decision the reviewer left conditional:**

1. **s3 must hold all five numerals in frame for the whole 5.946 s.** The count is the fix; a
   ken that pushes past `1` or `5` re-opens P1 #1. The block row along the bottom may leave
   frame — the numerals may not. This is the "photograph plus the ken-burns framing" half that
   is not mine to build.
2. **s9 and s10: take the reviewer's FALLBACK on finding #3, `centred` + drop the `brule`.**
   Their preferred fix was conditional on a filling card row landing in the bottom band — it
   did not land, because no such photograph exists in either pool. Both slots are plain
   photographs, so arch-D's 656 px band under the rule would still be an empty half.
3. **s11 must keep the doorway aperture in frame for the whole 3.621 s.** It is the only
   luminous object in the file; a ken that pushes into the surrounding black reproduces P1 #4
   with a different photograph.

**To fin-review:** s3's ground is a saturated red field (deep maroon after the grade). It was
taken on the count, which was the blocker, over three sheets that produced no alternative
stating five. If the tone is judged wrong, the honest next move is the reviewer's own escape
hatch — one `art-forward` layer numbering 1–5 over a calm photograph — not another sheet.

**Standing:** `s6` (CC BY-SA 3.0) and `s10` (CC BY 2.5) are attribution-mandatory. Their rows
exist in `CREDITS.txt`; any hand-copy, rename or promotion of those two files downstream must
carry the row with the pixels in the same move.
