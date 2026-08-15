# review · financial-freedom-after-50 · en · chapter 1 · attempt 2
VERDICT: PASS
PASS 1: 0 blockers, 0 should-fix
PASS 2: 0 blockers, 0 should-fix (4 notes)

Sheet: `studio/videos/financial-freedom-after-50-en-ch1/renders/SHEET.jpg`, rebuilt by me
at 15:11 from `DRAFT-ch1.mp4` (15:10:06, md5 `2ce5828d…`, 68.736 s) — the draft postdates
`index.html` (14:57:11), so the encode I read is the fixed build, not attempt 1's.
Frames sampled from the mp4: 11.6, 13.656, 16.6, 25.8, 53.6, 59.7, 66.9, 68.4.

## Verification of attempt 1's findings

| # | was | now | verified on |
|---|---|---|---|
| 1 | P1 blocker — the count "five" asserted nowhere | **FIXED.** `1 2 3 4 5` in wooden numerals, in order, no sixth, with five blocks below repeating the count. All five glyphs hold frame for the whole 6.396 s — the `plateKen(0.94→0.87)` pulls back rather than in, so the count is countable from the first frame, not just the back half. | mp4 11.6 s and 16.6 s |
| 2 | P1 blocker — two staircases at s9/s10 | **FIXED.** s9 is a single US $100 note (one note, so no shared-serial prop-money problem), s10 is the Golden Gate at golden hour. Nothing else in the chapter is a banknote, a bridge or water. The repeat is gone and did not reappear one slot right — s10/s11 were caught and re-picked by `fin-assets` before I saw them. | sheet cells s9/s10, mp4 53.6/59.7 |
| 3 | P1 blocker — arch-D with an empty 656 px band | **FIXED.** `grep 'class="brule"' index.html` → 0 elements; 0 of 11 scenes lack `centred`. On frame, both chip rows sit at frame centre with no rule and no dead band. | index.html + mp4 53.6/59.7 |
| 4 | P1 blocker — s11 crushed to unreadable | **FIXED.** The closing frame now reads unmistakably as a door standing open onto a sunlit park — tree, grass, bench, paving all legible, and "Step one." in `fundc` sits clean on the aperture. It is still a mostly-black frame, but it is a *composition* now, not a texture. | mp4 66.9 s and 68.4 s |
| 5 | P1 should-fix — young hands on the chess frame | **FIXED.** Visible knuckle structure, veining and loose skin; reads 60+. Opponent present, no face. The chess metaphor is intact. | mp4 25.8 s, left half at 1:1 |
| 6 | P2 should-fix — five tabletop frames in a row at 00:05–00:37 | **FIXED, and by the right method.** The run is broken twice inside itself: s3 (graphic, red, hard-edged) and s6 (architecture, vertical, grey, `AMERICAN STOCK EXCHANGE` cut in stone and it is the thing the line names). The strip now runs cold room → cold glasses → hot graphic → dawn exterior → dark interior → grey architecture → green notebook → misty figures → macro → landmark → aperture. No two adjacent cells share a picture type. | sheet, read as a strip |

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P2 | s3 | note | The ground of the promise frame is a saturated red field. Under the locked grade it lands as a dark oxblood, not alarm red — but it is unambiguously red, and it is the hottest frame in the chapter. §10 declares s3 as the *warming* beat at `#241d15` (warm brown), and §1 fixes red as "what is working against you while you do nothing". | 2.3 — the frame the video makes its promise on is painted in the token this video reserves for the cost of *not* acting. It also pre-spends ch2's declared "first red run". | **Do not re-fetch for this.** Three queries across two rounds returned zero countable rows of five, and the count was the blocker; the count now lands and it lands hard. Carry this forward instead: when ch2's red run is built, check it against this frame so the escalation to `#38151a` at s17 still reads as an escalation. If the creator wants it neutral, the lever is the reviewer's escape hatch — one `art-forward` numbering layer over a calm photo — not a fourth sheet. |
| 2 | P2 | s9 | note | Chip reads `2 Maximize` with no object; VO says "your most powerful savings years". Carried over from attempt 1 finding 7, deliberately not taken by `fin-build` (its Owed 1). | 2.2 — "Maximize" alone does not name what is being maximized. | `2 Maximize savings` is 18 chars, inside `max_chip_chars` 22, one word in `SPEC[8].chips[1]`. **Not worth a render on its own** — take it only if ch1 is rebuilt for another reason. |
| 3 | P2 | s9 | note | A macro of a $100 bill is the single most generic frame in finance stock. | 2.3 — "would this be at home in any generic finance video". | It earns its slot here (breaks the tabletop family, US-correct, one note so no prop-money serial issue, the chapter's only money frame) and the alternative cost a fetch round. Recorded as taste, not as work. |
| 4 | P2 | s9, s10 | note | Storyboard §6 `ctr` column still reads **N** for both; the shipped build is `centred`. | Evidence rule 4 — a stale plan row is how a later pass "fixes" a correct build backwards. The §6 premise (the chip row occupies arch-D's lower band) was untrue as built: `.arch-d .stack` is `align-self:start`, so chips render at the top and the band stayed empty. | Update §6 `ctr` to Y for s9/s10 with a one-line note, or leave it and this log is the record. No build change. |

## Would I keep watching?
Yes, and further than last time. The first six seconds are unchanged and still the best thing
in the chapter — a man who genuinely reads sixty, not looking up, "OVER FIFTY? / The ship has
not sailed." The promise now *lands* rather than merely arriving: at 11.06 s (inside the 15 s
gate) the screen fills with `1 2 3 4 5` at 400 px tall and the line says "A five-step plan, in
order." That is the frame the chapter was missing, and it is now the strongest frame in it.

**The attention risk has moved from 00:31 to 00:23–00:31** — s5, the chess hold. It is the
longest single-framing scene in the chapter at 8.271 s, it is the darkest non-closing frame,
and it follows the chapter's loudest frame, so the drop in energy is felt. It is not a defect:
the line is 8.3 s of VO, the metaphor is right, the hand is now correctly cast, and there is no
fix that does not cost a render. Naming it so it is watched in the assembled cut.

The chapter ends on an open door and "Step one." — a loop opened, not closed. Correct hand-off
into ch2.

## Regressions vs my last pass
**None.** Checked explicitly, because this pass touched six of eleven slots:
- All eleven `data-start` / `data-duration` / `data-framings` triples and the root `68.672`
  are byte-identical to the file I reviewed on attempt 1. Nothing was re-timed to fix a picture.
- s1 untouched, as instructed. s8's two framings still push wide → tighter across 9.473 s, so
  no single framing holds past `max_scene_seconds` 9.0.
- The temperature arc survives: s1/s2 still the coldest, s7 still the first green in the video
  and still on "take back control", the chapter still closes green on `#12351f`.
- First cue at 0.25 s (under `first_cue_by_seconds` 0.5); s11 still carries a bare 3.621 s
  duration equal to its single framing, i.e. no transition tail on the chapter's last scene.
- Chapter is still **0 of 4** drawn layers, as storyboard §8 declares for ch1. The count beat
  that would have justified one is carried by the photograph, which is the outcome §8 predicts.

## What is working
- **s3 is now the payoff frame the script asked for.** The deviation the parent flagged —
  numerals instead of five cards — is the better answer, not a compromise: a photographed row
  of cards would have needed the viewer to count edges, and `1 2 3 4 5` at that scale is
  countable at 1.5× on a phone. The card chain I asked for was the wrong ask; this is the
  right object. Do not "restore" the cards in a later pass.
- **The strip has real variety now** and it was fixed the way the archetype box demands — by
  changing what two scenes are *of*, not by adding layouts. Eleven scenes, no adjacent
  repeats, and the argument's turn (s7, green) still lands on the temperature turn.
- **s6 is the model for how to break a flat run.** Scale, a vertical, and legible carved
  lettering that is exactly what the line names. The rejected NYSE alternative carrying
  Christmas wreaths on an evergreen video is the kind of catch that should keep happening.
- **s9/s10 chip rows read clean at frame centre.** Whatever the archetype table says, this is
  what should ship.
