# fin-assets · passive-income-number · en · chapter 5 · attempt 3
STATUS: fail — single-slot re-fetch of **s61 (5.9, `ROUGHLY 4 TIMES`)**. Nothing on disk
was changed. The replacement spec — *two physically separated groups, roughly four
against one, background between them, countable at a glance* — **is not satisfiable from
the pools this stage can reach**, and every near-miss the pools do hold reproduces the
exact defect under repair (a group whose count is 3, 5, 8 or 10+, i.e. a stated multiple
that is the wrong one). Per the brief's own bar (*never accept a near-miss*; acceptance
is terminal here) I stopped rather than degrade the frame, and escalate with the
evidence and a named remedy.

## Ran
- Read `vault/CLAUDE.md`, `tools/format/fin-assets.json` (`assets`, `layout`),
  `tools/packs/fin-assets.md`, the ch5 storyboard rows for 5.9 (§7 line 525, §8 line 676,
  §10 line 841), `script-en.md` 5.9, `review-en-ch5-1.md` finding 1, and `index.html`'s
  s61 comment (fin-build's attempt-2 geometry refusal).
- **26 contact-sheet rounds**, ~150 preview cells + **9 full-resolution reads**, all in
  the scratchpad (`/tmp/claude-1000/.../scratchpad/probe1..27`), nothing written into the
  project. Pools: Pexels (24 rounds), Wikimedia Commons (2 rounds; first 429'd, second
  returned 3/6 cells). Pixabay was never eligible: s61 is a ken-push hero slot, so
  `assets.min_width_px` 1600 rules out that pool's 1280 (`assets.pick_width_px`).
- Verification of the untouched chapter: cross-project md5 dedupe (the `find`-based
  form), `pipeline_check check assets --chapter 5`, CREDITS/file parity.

## Failed
- **s61 not replaced.** No candidate cleared the gate. The blocker stands.
- Commons round 1 died on `HTTP 429 … robot policy`; round 2 succeeded but confirmed
  Commons indexes *named things* — `four wooden crates@commons` returned a stencilled
  ammunition box and two archive photographs of Wojtek the bear.

## Evidence

### 1 · What was searched, and what came back
Object families tried for "four grouped + one apart" (all `@pexels` unless noted; `#N`
offsets used to go deeper where the family looked plausible):

| family | queries | best cell found | why rejected |
|---|---|---|---|
| wooden crates | 9 rounds inc. offsets #2 #3 #4 #5 #6 #7 #13 #19 #25 | the same ~20 photographs recur; the current s61 photo itself reappears as `qb#2`, `qh#2`, `sp#6` | no frame in the pool has a separated single crate; every stack is a contiguous wall |
| cardboard boxes | 3 | 5-box pyramid on white brick | count 5, no separation; other cells carry **NIKE** boxes |
| shipping containers | 2 | `ya#1` — 4–5 white containers + 1 green-doored | full-res: overlapping, count ambiguous, faded stencils, forklift mast. Other cells: ONE / K LINE / EVERGREEN / MSC brand marks |
| pallets, sacks, barrels, tires, bricks, cinder blocks | 6 | tire stack `qr#2` | tire-shop signage ("USED"), and pallets/warehouse would repeat s59 |
| books, plates, cups, stools, chairs | 4 | `ua#1` stack of ~4 books, `ra#2` 3 cups + 1 | counts ambiguous at 4-or-5; `rc#1` is a scale/distance trick, not a count |
| eggs (bowl, carton, row, net bag) | 5 | **`ta#2`** — 3 eggs in a net bag + 1 apart, clean gap, minimal | full-res count is **3**, not 4. Ships the same defect in a smaller number |
| apples, walnuts, chestnuts, corks, lemons | 5 | **`sa#2`** — exactly four apples, hard venetian-blind light, dark wood | full-res: the fourth apple is **rotten/shrivelled** — adds "decay", a meaning the line does not carry |
| game pawns / concept still-life | 3 | **`ri#1`** — red group + 1 dark pawn, wide gap, mirrored surface | full-res count is **5** red (4 front + 1 behind), and see the contrast note below |
| dominoes, dice, blocks, cubes, paper clips, matches, pencils, stones | 6 | — | lettered blocks (`ONE TEAM`, `2025`, `SALES`), or rows of 11–12 units |
| silos, mailboxes, fence posts, hay bales, chairs | 4 | rural mailbox cluster `so#3` | counts arbitrary (3, 6, 7); silo rows are 6–8 |
| cash bundles / dollar bills | 2 | **`zb#2`** — exactly four $100 bundles, 2×2, navy ground, correct currency for -en | **PROP MONEY.** Full-res reads `СУВЕНИРНАЯ ПРОДУКЦИЯ · SOUVENIR PRODUCTION` across every note face and Russian text on the bands. Hard reject (the demonetised-₹500 failure in another currency's clothes) |
| "the gap" as a photograph (canyon, chasm, split rock, drawbridge, cracked earth, alley) | 5 | `ba#5`, `ag#3`, `zd#4` | `ba#5` is **Kjeragbolten** — the boulder is *wedged in* the gap, i.e. the frame says the gap is spanned, and the fog sits exactly where the `.huge` sits; `ag#3` reads as rock texture, not a gap; `sq#4` is the **Berlin Holocaust memorial** (hard reject); cracked earth is a flat many-crack texture |

### 2 · The structural finding (this is the transferable one)
**"Four of a thing grouped, plus one of the same thing apart" is not a composition
either stock pool holds.** Real-world photographs have arbitrary counts, and the one
genre that *stages* counts — concept still-life — stages either **lettered blocks**
(text on the object) or **people-shaped pawns against a crowd of 8–20** (the
leadership/odd-one-out trope). Naming the numeral in the query does work occasionally
(`four apples` returned a frame with exactly four apples; `four eggs one egg` returned a
3+1) but it cannot be steered to 4+1: across ~150 cells the observed group sizes were
1, 2, 3, 5, 6, 8, 10, 12, 14+. Never four-with-one.

### 3 · Full-resolution reads caught what the grids could not (3 of 9)
`zb#2` prop-money legend · `xa#4` **SMITH'S** moulded into the milk crate and an
**ANGRY ORCHARD** carton inside it (an alcohol brand), plus graffiti on the brick ·
`ta#2` count 3 not 4 · `sa#2` the rotten fourth apple. All four were invisible at grid
size. The rule earns its keep again.

### 4 · Why the two least-bad candidates were still refused
- **`ri#1` (pawns, 4-front-plus-1-behind vs one).** Composition is right — the only true
  "group + separated single" in 150 cells. Refused on two counts. (a) The group reads
  **5**, and the parent's bar is explicit: a frame the viewer must count carefully has
  already failed. (b) Legibility: the ground is pale mint. Pushing it through the locked
  chain (`grayscale(.32) brightness(.62) contrast(1.05)` then `.scrim`'s centre
  `rgba(13,16,23,.46)` + the two outer gradients) lands the plate ground near
  (65,72,74) → `--warn` `#ef4444` at roughly **2.4:1**, against the chapter's measured
  range of **4.97–7.90** (`review-en-ch5-1.md`). The hero number would be the least
  legible in the chapter, on the beat that *is* the chapter's argument.
- **A no-count "gap" frame** (the authority ladder's terminal rung — *a quiet texture
  that still reads the scene's keyword*). I pursued this and could not land it either:
  every legible instance is a named landmark, is contradicted by its own subject
  (Kjeragbolten), puts a high-key slot exactly under the `.huge`, or repeats a neighbour
  — a corridor repeats s63, a road repeats s64, a warehouse repeats s59, a top-down
  ground texture repeats s64. The rung is available in principle; the pool did not
  furnish a clean instance in 5 rounds.

### 5 · State of the chapter (verified, untouched)
- `md5sum` dedupe across `studio/videos` + `vault/videos`, `find`-based form: **empty
  output — no collisions**, including against ch6's 12 images now on disk.
- `python3 tools/pipeline_check.py check assets --slug passive-income-number --cut en
  --chapter 5` → **`PASS assets-en`**.
- **18 image files ↔ 18 CREDITS rows**, one per file, keyed exactly (16 fetched + the two
  derived crops s56b/s67b, each carrying its parent's re-keyed row). The
  newline-in-Commons-author bug did **not** recur — s55's Commons row is intact and there
  is no orphan licence line. (The parent's "16 for 16" is 18 for 18 once the two derived
  crops are counted.)
- Dimensions unchanged and uniform: 15 files at 1880×~1253, s56b/s67b at 1600×900.

## Changed
**Nothing.** No fetch was promoted, no file written into
`studio/videos/passive-income-number-en-ch5/`, `manifest.json` and `CREDITS.txt` are
byte-identical to attempt 2, and `assets-ch5/final/s61.jpg` is still the 14-crate wall.
This is deliberate: a half-swapped slot is worse than a known-bad one. ch6's directory
was not touched. All 26 rounds of previews live in the session scratchpad, outside the
project.

## Owed
The decision that unblocks 5.9 sits **above this stage**, because both remaining routes
change a declaration this stage does not own. Ranked:

1. **Re-open storyboard §8's refusal of drawn art on 5.9 — its premise is now known
   false.** §8 declines drawn art *"on the explicit ground that the photograph is four
   crates against one"*. There is no such photograph, in any object family, in either
   pool. `tools/packs/fin-assets.md` and `layout.image_relevance` both name exactly this
   case: *when the beat is an abstraction — a ratio — no photograph exists and searching
   harder will not conjure one; draw it.* A minimal drawn device (five identical marks,
   four grouped and one apart, decorative level, no scale, no numerals) states the ratio
   the frame is missing and is **not** the measure bar §9a rules off this frame. This is
   a storyboard-level amendment, not an asset pick.
2. **Or re-spec 5.9's image to something photographable** and let the picture carry a
   different true thing about the line — the frame does not have to carry the count if
   the storyboard stops asserting that it does. If that route is taken, the ranked
   photographable substitutes I verified at full resolution, so nobody re-searches:
   - `sa#2` — exactly four apples, hard side light, dark wood (Pexels, 1880×1253,
     `four apples`, cell 2). States four, correct number, no ratio; costs the rotten
     fourth fruit.
   - `ue#3` — four white eggs in a white bowl on dark wood (`four eggs in a bowl and one
     egg beside it on a dark table`, cell 3). Dark, tonally native to ch5; no separation.
   - `ri#1` — the pawns, if the count-of-5 and the ~2.4:1 contrast are acceptable.
3. **Whatever is chosen, s61 must not stay as it is.** The shipped frame states a
   multiple and states the wrong one, directly under `ROUGHLY 4 TIMES`.

Cross-chapter note for whoever takes this: §10's crate rhyme (s61 → s75/s76 → s77) is
already one-legged — ch6's s77 was fetched as *"large steel shipping container standing
alone in an empty yard"*, not a crate. If s61 leaves the crate family too, the rhyme is
s75/s76 only and §10 should say so rather than claim a three-beat chain.

OPENED-BODY: none.
