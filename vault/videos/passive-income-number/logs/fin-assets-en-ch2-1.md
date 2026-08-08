---
summary: en ch2 sourced from scratch — 15 fetched backgrounds (s9–s23) + 1 derived crop (s10b), all ≥1600px, all YHIGH ≥ 138, 0 md5 collisions, `check assets --chapter 2` PASS. 24 contact sheets / 144 candidates; 16 accepted, 128 rejected, 0 dropped. Seven images passed their contact sheet and were killed by the full-resolution read — including one that md5 could not see, because it was the hi cut's own s16 re-encoded through the other pool.
updated: 2026-08-08
source: fin-assets attempt 1, chapter 2, en cut — VO 2.1–2.15, storyboard-en §7/§8/§10/§11.
---

# fin-assets — passive-income-number / en / chapter 2 / attempt 1

**PASS `check assets --slug passive-income-number --cut en --chapter 2`.**

**Accepted 15 fetches + 1 derived crop · rejected 128 candidates · dropped 0.**
Chapter 1 untouched. `assets/lottie/` untouched (the storyboard asks for no lottie in ch2).

| slot | line | subject | W×H | YHIGH | pool |
|---|---|---|---|---|---|
| s9 | 2.1 | blank kraft notebook + sharpened pencil, dark grey felt | 1880×1253 | 203 | pexels |
| s10 | 2.2 | row of brass taps on a steel manifold over a steel trough | 1732×1300 | 170 | pexels |
| **s10b** | 2.2 | **derived** `crop=1600:900:132:250` of s10 — tighter, nearest tap near centre | 1600×900 | 152 | — |
| s11 | 2.3 | one rusted nail through a weathered plank, nothing hanging on it | 1880×1254 | 211 | pexels |
| s12 | 2.4 | two blank sheets side by side, top-down, walnut | 1880×1253 | 192 | pexels |
| s13 | 2.5 | open book, macro, text dissolved by DOF, black ground | 1880×1058 | 211 | pexels |
| s14 | 2.6 | wall of card-catalogue drawers, ONE drawer pulled out | 1880×1253 | 157 | pexels |
| s15 | 2.7 | closed bound volume, macro corner + page block, dark table | 1880×1253 | 181 | pexels |
| s16 | 2.8 | stack of paper-sheet corners, raking light, black left third | 1880×1253 | 192 | pexels |
| s17 | 2.9 | wooden box of rubber type stamps on kraft | 1880×1253 | 170 | pexels |
| s18 | 2.10 | hands writing a short mark on a kraft tag, no face | 1880×1253 | 202 | pexels |
| s19 | 2.11 | egg carton, carrots, greens on a dark kitchen table | 1880×1253 | 228 | pexels |
| s20 | 2.12 | paper bag full of vegetables, carried, no face | 1880×1253 | 138 | pexels |
| **s21** | 2.13 | **HERO** — single rustic loaf, dark table, hard side light | 1880×1253 | 144 | pexels |
| s22 | 2.14 | rack of **blank** US time cards, warm low key | 1880×1253 | 152 | pexels |
| s23 | 2.15 | wooden ladder against a plank wall, tight on three rungs | 1880×1253 | 177 | pexels |

Every file ≥1600px on the long edge (§10 resolution routing; s10 at 1732 is the only
sub-1880, and it is 4:3 so Pexels `dpr=2&w=940` sized it that way — still 132px of
horizontal slack above the 1600 crop floor s10b needs). Every YHIGH ≥ 138 against the
110 gate. **0 md5 collisions** across every image in `studio/videos/` including the hi cut.

---

## The full-resolution read killed seven images the contact sheet passed

This is the whole value of the stage on this run. Each of these was invisible at
512×288 and fatal at 1880px.

| slot | what the sheet showed | what the full read found | fix |
|---|---|---|---|
| s9 | black pencil on a blank notebook, black ground | **`STAEDTLER … Noris … Germany`** imprinted on the pencil barrel, silver on black, ~12px on the encode — a brand mark AND a non-US country of origin on an all-American cut | free re-pick → cell 4 |
| **s14** | ruled ledger, red/blue rules, columns of figures | **the same photograph as hi ch2's s16** — identical surnames and identical figures (4464 / 8525 / 2000). Pexels ingested it from Pixabay, so the two encodes have different bytes and **md5 cannot see it** | 5 re-queries → card catalogue |
| s15 | open paperback, dramatic side light | legible Turkish text and the character names **`FAUST` / `MEFİSTO`** at ~27px on the encode, on the one scene whose job is to name three specific authors | free re-pick → cell 1 |
| s15 (r1) | open volume on a stack of old books | running head **`Breton 75`** — a surname, on the same scene | re-picked before promotion |
| s17 | date stamp on a workbench with old forms | legible Dutch — **`AANGIFTE TOT INVOER`**, `PLAATSBEWIJS DER POSTERIJEN, TELEGRAFIE EN TELEFONIE`, `GESCHIKT` — a named foreign institution and a customs desk | free re-pick → cell 3 |
| s18 | hands writing on a form, dark ground | **`FORM 9 — PARTICULARS OF STILL-BIRTH`**, fully legible, under a line about dividing a grocery bill | re-pick → cell 1 |
| s18 (r2) | hands writing on paper, warm, calm | a fully legible **love letter** (`To my sweetheart … Forever yours, Alex`) | re-query → new sheet |
| s22 | punch clock + card rack on brick | **`DIMEP`** brand on the clock face, plus a noticeboard reading `Aniversariantes de Maio 2024` with a column of dates and Brazilian names — Portuguese, not American | free re-pick → cell 2 |

**The s14 catch is the one worth carrying forward.** The dedupe rule says no image may
repeat across videos or channels, and md5 is the tool we use to enforce it — but md5
only sees bytes. The same photograph delivered through two different pools at two
different resolutions is two different hashes and one identical picture. The ledger
would have shipped in both the Hindi and the English cut of the same video. Nothing but
reading the full-resolution file next to the sibling cut's log would have caught it.
**Pexels credits some contributors as "by Pixabay" — that is the tell that a Pexels
result may be a Pixabay image, and vice versa.**

---

## Two slots where the object had to change, not the adjective

Both were walked down the retry ladder to exhaustion first, and both are logged so a
later pass does not "fix" them back.

### s10 (2.2) — the tank. 6 sheets, 36 candidates, no tank exists.

Queries tried: steel water tank + brass tap in a workshop · metal water barrel with a
tap low on its side · stainless beverage dispenser with a spigot · rain barrel with a
brass spigot · steel fermentation tank with a valve · wooden barrel with a brass tap.
The pools answer with either **tanks and no tap** (brewery halls, wine cellars) or
**taps and no tank** (garden faucets, bar rails), and three sheets carried hard rejects
outright — `GUINNESS`, `Coca-Cola`, `CONDENSADO`/`TINA REG TEQUILA` in Spanish, and a
pressure gauge that §10's own cue forbids.

**Taken: a receding row of heavy brass taps on a steel manifold above a steel trough.**
§10's returning-objects table declares the fallback and names the constant — "the
**brass tap on a plain steel body under workshop light** is the recognisable constant …
**the tap is what carries the rhyme, not the tank's silhouette**" — and this frame
carries that constant verbatim. It also solves §6a, which is the harder constraint:
s10b must be a *tighter crop of the same frame* (ken 1.06→1.16 continues the push, never
a self-dissolve), and this frame crops cleanly onto the nearest tap.

**What it costs, stated plainly:** sound-off gate 3 is the weakest in the chapter — the
line names a *tank* and no tank silhouette is legible. The scene's own head reads THE
TANK, and framing 2 resolves to a single tap, which is the beat ("how much can you draw
out"). **⚠ ch4/ch5 inherit this:** s46, s47 and s57 must match this tap on this steel,
not a tank. Sourcing them as tap/stream macros in the same material family is exactly
the fallback §10 already declares.

### s14 (2.6) — the printed table. 5 sheets after the duplicate was caught.

Queries tried: columns of printed numbers on an old page · old accounting ledger
(Pixabay — returned the hi cut's photograph) · adding-machine paper tape · old ledger
from `#7` · printed table of numbers on a page · handwritten calculations on graph paper.
The pools answer "page of numbers" with **Bibles** (three separate sheets returned the
same Nazirite passage), German WWI documents, French and Italian manuscripts, Arabic and
Persian illuminated pages, a Polish newspaper, and a hand-drawn graph whose curve falls
toward zero — which would have *contradicted* the line.

**Taken: a wall of card-catalogue drawers with one drawer pulled out full of cards.**
Sound-off: many records, and the one set he pulled and ran. The storyboard's cue asked
for "one row lit"; one drawer out of a wall of drawers is that idea in an artefact the
pool actually has. It also hands the scene a clean grey right-hand field, which arch C
needs — s14 carries a stmt *and* a foot.

⚠ **Concept echo across cuts, declared:** hi ch2's s9 is also a card catalogue. Different
photograph (that one is a tight close-up of card edges; this is a wide of a cabinet wall),
different chapter, different channel, different md5. Flagged rather than hidden.

---

## The sound-off test, applied per line

All fifteen pass gates 1–3 and 5. Gate 4 (one picture per point) drove three decisions:

- **s19 was re-picked for gate 4, not for a defect.** The first pick was a paper bag
  spilling produce with a bread loaf on a board behind it — defensible alone, but it
  contained s20's subject (a paper bag) *and* s21's subject (a loaf) one and two scenes
  before each of them. Swapped to the egg carton, which owns "food" without borrowing
  either. Brightness improved as a side effect: YHIGH 117 → 228.
- **s23 vs ch1's s8.** Both are wooden ladders, by design (§10's returning objects). ch1
  ships an outdoor stucco wall in warm evening sun, wide; s23 is a tight framing on three
  rungs against a dark plank wall, and the ladder's own shadow doubles the rungs beside
  it. A whole-ladder frame was rejected specifically to leave s74 (ch6, "the whole ladder,
  full height") its own statement.
- **s20 vs ch1's s6.** ch1 has bags on a doorstep; s20 is a bag being carried, full, close.

**The four-artefact C run (s12–s15) survives the substitutions** and still changes
underneath, which §7 says is the only through-line the chapter has: two blank sheets flat
on wood → an open book macro on black → a wall of card drawers → a closed bound volume.
Four objects, four scales, four grounds.

**s22 got better than specified.** The cue asked for a punched time card with the hours
*illegible*; the frame taken has hours **absent** — every card in the rack is blank. Under
"the grocery bill stops costing you hours" that is the line rather than a decoration of it.
Its printed field labels (`NAME` `DATE` `REGULAR TIME` `MONDAY`) are legible but are
generic English pre-printed form furniture on an unfilled US card: no title, no figure, no
agency, no brand — the informational opposite of a fabricated source.

## Density and grade

The seven art-forward and chip-cascade frames get the calmest backgrounds (§10). ch2's
two art-forward scenes are handled: **s16** (`survival-grid`) is a paper-corner macro
whose left third is near-black, exactly where the `p-b` plate sits, and it carries no
chart to fight the drawn one; **s18** (`division-block`) is a wooden table under the
`p-d` band. No per-scene `filter:` override is set anywhere in this chapter — §10 forbids
them under the chapter archetype layer, and nothing here needed one.

**Warmth was not screened on.** Per the parent's correction and §10's amended note, source
R−B was not measured and no slot was sent back for it.

**Wood count: 5 of 16**, and only s12 is a warm brown plane — s11 is grey weathered, s15
and s19 are dark tables, s23 is greyed. ch1's 6-of-8 problem is not rebuilt.

## Flags for fin-editor

1. **s10 / s10b** — the tank is a tap rail. Weakest gate-3 fit in the chapter; the reasoning
   and the ch4/ch5 consequence are above. If it fails review, the honest fix is a
   storyboard decision about the object family, not another fetch round.
2. **s18's upper right is blown** (YHIGH 202 concentrated there) and there is a saturated
   yellow marker cap at frame left. The `p-d` band covers the calm lower half; the bright
   patch is the one place a grade issue could show.
3. **s20 is the chapter's busiest frame** — a brown/grey/red plaid shirt across ~45% of it,
   which grayscale(.32) only partly tames.
4. **s13 and s16 are both white-on-black paper macros**, four scenes apart with s14 and s15
   between. Legibly different (an open book with a gutter vs a stack of sheet corners), but
   they are the chapter's closest pair.
5. **s9, s12 and s15 are all large pale planes.** Each has a real object edge, a cast shadow
   and directional falloff — none is the flat-texture failure — but three in one chapter is
   worth a look in the draft.

## Counts

| | |
|---|---|
| contact sheets built | 24 (15 slots, 9 re-queried 1–5 times each) |
| candidates seen | 144 |
| accepted | 16 (15 fetched + 1 derived crop) |
| rejected | 128 — 41 legible/foreign/brand text · 27 people or faces · 22 wrong object · 18 high-key · 11 off-tone or arguing · 5 below YHIGH 110 · 3 duplicate-of-sibling-cut · 1 gate-4 collision |
| dropped | **nothing** — every background was replaced, never dropped |
| Pexels searches | 23 · Pixabay 2 · Commons 0 |
| free re-picks (no fetch) | 8 |
| lottie work | none — ch2 asks for none |

## Verification

- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en --chapter 2`
  → **PASS assets-en**. Negative control run: **without** `--chapter 2` the same command
  FAILs, because it reads `-en/assets/img/` (ch1's manifest) instead of
  `-en-ch2/assets-ch2/final/`. The flag is what makes the assertion reach these 16 files.
- **16 manifest keys ≡ 16 CREDITS rows ≡ 16 `.src` sidecars**, checked programmatically —
  no orphan on disk, no credit row without a key, and every `.src` byte-equal to its
  manifest query, so no throwaway exploratory query survives as false provenance.
- **`s10b` is hand-placed and carries its own credit row**, re-keyed onto the new filename
  from s10's source in the same move, plus its own manifest key and `.src` recording the
  crop rect. A derived crop that is on disk but not in the manifest is never reached by the
  licence assertion.
- `index.html` does not exist yet (fin-build has not run), so pipeline_check's
  render-time attribution half is skipped — expected at this stage, and it will cover
  these files once the chapter is built.

## For the next run

**Count the cells you actually got — the number burned into the cell is the candidate
index, not the grid position.** Three sheets this run came back short (s9 rendered 2 of 6,
s21 5 of 6, s23 4 of 6, s14 2 of 6) because some previews fail to download and ffmpeg's
image2 demuxer then starts at the first cell file that exists. The labels stay correct, so
`--pick sN=<label>` is always right — but a sheet whose visible cells are numbered 5 and 6
means candidates 1–4 were never looked at, and re-running `--candidates` usually recovers
them. Measuring YAVG/YHIGH per cell before viewing catches this for free: an unrendered
cell measures exactly 17/17, the sheet's padding colour.
