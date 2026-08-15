# fin-assets · financial-freedom-after-50 · en · chapter 2 · attempt 1

18 slots (s12–s28 bg + the `s23b` cut-in, VO lines 2.1–2.17). 9 contact-sheet rounds
(54 sheets, 322 cells looked at), 24 full-resolution reads, 2 promoted-sheet reads.
**8 promoted images were rejected AT FULL RESOLUTION after passing the contact sheet**
and re-picked — see Evidence 2. All 18 accepted, 0 dropped. 0 Lotties, 0 icons sourced
(storyboard §8 gives ch2 one inline `<svg class="icon">` at s18, which fin-build draws —
not an asset).

## Ran

1. Created `studio/videos/financial-freedom-after-50-en-ch2/assets-ch2/final/manifest.json`
   — 18 slots, every one `@pexels` (`assets.pick_width_px.pexels` 1880 clears
   `assets.min_width_px` 1600; Pixabay's 1280 does not, and all 18 are full-bleed `.bg`).
   Queries are the searchable form of the storyboard prose prompts in
   `…-en/assets/img/manifest.json`.
2. Round 1: `--candidates 6` over all 18 slots. 7 slots had a usable cell; 11 did not.
3. Rounds 2–9: `--candidates 6 --only <slots>` — 11, 9, 8, 3, 1, 7, 2, 1 slots.
   `--only` on every re-run; without it each round re-searches 18 slots and downloads
   108 previews to look at three.
4. `--pick` ×3 (18 + 1 + 6 promotions, `--force` on the re-picks).
5. Cross-project md5 (`find` form, both layouts) after every promotion round → no
   collision among promoted images.
6. `tools/image_sheet.py … --chapter 2` built and read twice; `pipeline_check check
   assets --chapter 2` → **PASS**.

## Failed

**Whole sheets rejected 6-of-6** (query changed, not the pick):

- `galvanized metal bucket on wooden floor` / `old metal bucket on concrete floor` /
  `galvanized bucket pail on dark background` (s14, 3 rounds, 17 cells) — the pool's
  galvanized buckets are **lettered garden props**: `FLOWERS & GARDEN`, `FRESH CUT
  flowers`. Two rounds returned bare galvanised *texture swatches* with no bucket in
  frame; one returned paint tubs. One unlettered bucket exists in the pool and it is
  what shipped.
- `water pouring into metal bucket` (s15) — all six cells were **non-US village water
  scenes** (Nepal courtyard well, a conical-hat figure at a shore, temple spouts). A
  US-market cut cannot use any of them.
- `water leaking out of a bucket`, `water running through open hands` (s15, rounds 2–3)
  — dripping taps in grass, then six hand-washing-at-a-sink frames. Sound-off they say
  *hygiene*, not *leak*.
- `stack of unopened envelopes mail on table` / `pile of bills and envelopes…` /
  `stack of white envelopes on a dark wooden table` (s17, 3 rounds) — **vintage
  handwritten love letters, twine-tied bundles, PAR AVION airmail with foreign stamps.**
  The pool has no "unopened US bill" object; s17 moved to the card itself.
- `printed bank statement paper close up` / `printed financial spreadsheet on dark desk`
  / `bank statement with columns on dark wood` / `calculator on top of paper documents`
  (s18, 4 rounds) — every cell carried **legible figures or a brand**: a real Schumer
  box reading `12.24% – 23.24%` and `24.24%` (a photographed APR table on the scene
  whose card says *no figure on this frame*, one line after the cut's only permitted
  rate claim), `Platinum Credit Card`, `Loan Agreement`, `2% Cash Back Rewards · No
  Annual Fee`, `THE BANK OF CALIFORNIA` cut in stone, `Türkiye İş Bankası`, an AAPL
  candlestick chart on a phone screen, and IRS `W-4`/`W-9`/`1040` forms (which would
  also pre-empt ch3).
- `crossed out item on handwritten to do list` / `hand crossing out a line with a pen`
  (s21, 2 rounds) — round 2 returned six *signing-a-form* frames (one a legible W-9);
  no cell in either round showed anything struck through.
- `snowball rolling down slope` / `large snow ball on a snowy hill` / `giant snowball
  rolled in the snow` / `snowball rolling down a hill` (s22, 4 rounds, 24 cells) —
  **Christmas baubles, a dog, a teddy bear on a sled, children rolling snow.** A
  photograph of a snowball with a widening track behind it does not exist in this pool;
  see Evidence 4.
- `water stained damaged ceiling in house` / `damaged roof shingles on a house` /
  `missing shingles on a damaged roof` (s23b, 3 rounds) — burnt-out kitchens, gutted
  derelicts and **Mediterranean clay-tile roofs**. A leaky roof in a US home is an
  inconvenience; every cell offered a ruin.
- `row of kraft envelopes…` / `cash in envelopes…` / `six brown envelopes on a table` /
  `pile of brown paper envelopes on a table` (s25, 4 rounds) — wedding-stationery
  flatlays on marble and hot pink, single red gift envelopes, one in front of a
  **Christmas tree** (dates an evergreen video).
- `stacks of coins in a row on a dark table` (s25, round 8) — cell 6 is a silver
  **ETHEREUM** coin and cell 5 a gold-coin stack, from a query that never mentions
  crypto. Confirms the pack's rule-3 finding on the second pool; coins abandoned for
  this slot.

**Individual cells rejected on the trap list:** blue-handled taps under legible Dutch
`Koud`/`Warm`; a corkboard/legal pad reading `TAXES · DUE 4/15` (a date, and the wrong
topic); `NEW YEAR'S RESOLUTIONS`; `WHILE YOU WERE OUT`; `At-Will Employment Agreement`;
a `2021` desk calendar; Korean sticky notes; a face mask (s19 cell 6 — dates the video);
€100 notes on a "bills" query; a phone screen showing a calculator app.

## Evidence

**1 — the chapter's counted line, and the frame that now states it.** 2.5 speaks
*"the two biggest leaks"*, so under the parent's ruling the frame must show two.
`s16.jpg` = **exactly two** taps on a concrete-block wall (pexels 28887606, 693,924 b,
B&W in-camera). Counted at full resolution: two pipes, two spouts, nothing at the edges.
2.4 (*"holes in the bottom"*, plural, unnumbered) is `s15.jpg` — rainwater running
across a pavement into a street grate, i.e. water leaving through a hole. The other two
counted frames in the chapter: `s26.jpg` is exactly **two** unlabelled binders under
2.15's *"a separate account"*, and `s12`/`s13` are the foundation/skyscraper pair 2.1–2.2
argues from.
⚠ **2.14's "three to six months" is NOT stated by the photograph and cannot be** — it is
a duration range, not a count of things. `s25.jpg` is a bundle of US $50s in a kraft
envelope: it shows the fund and does not contradict a count. The 3–6 lives on the chip
row (`OPINION / CONVENTION`, no agency card — `facts-staging` §2). Flagged in Owed.

**2 — the eight full-resolution rejections. This is where the value of this stage was.**
Every one of these passed a 6-cell contact sheet and failed only when opened at 1:1:

| slot | what the thumbnail hid | rule |
|---|---|---|
| s16 (1st pick) | **THREE** spouts, not two, under *"the two biggest leaks"* | the counted-frame ruling |
| s18 (1st pick) | two of three $20 notes share the serial **`MB24517115I`** → prop money; and the receipt reads **`PARAGON FISKALNY`** (Polish fiscal receipt, `NIP` line) | shared-serial rule 5 + non-US artefact |
| s24 (1st pick) | the shattered piggy bank's coins read **`5 CENTAI` / `2 CENTAI`** — Lithuanian centai, a currency withdrawn in 2015 | wrong currency on a `$` cut, and a demonetised one |
| s20 (1st pick) | fully legible chore list: *work out · clean the house · groom the dog · make dinner · go shopping* under *"list your debts from the highest interest rate to the lowest"* | the frame argues with its line |
| s21 (1st pick) | fully legible **`New Year's Resolutions`** — *wake up earlier, eat mindfully, drink more water* — and nothing struck through, under *"once it's gone, you roll that payment onto the next"* | argues + seasonal cue |
| s25 (1st pick) | the crop resolves to four brown paper shapes; sound-off it says *kraft paper*, not *emergency fund* | sound-off Q1 |
| s19 (1st pick) | a smooth young hand — the script's photography rule is a rejection criterion, not a preference (ch1 re-picked s5 for exactly this) | 50-and-older rule |
| s22 (1st pick) | (kept) — see Evidence 4 | — |

Three of these eight (s16, s18, s24) are defects that reach the licence/fact layer, not
taste: a wrong count on a counted line, reproduction money, and a demonetised foreign
currency. **None was visible at grid size**, and the sheet-only flow would have shipped
all three.

**3 — s17, the chapter's one figure frame.** 2.6 carries `num north of 20%` ·
`Federal Reserve G.19 · as of August 2026` · `VERIFIED`, arch B, hero cue, the chapter's
hottest ground `#38151a`. `s17.jpg` = a macro of a dark grey chip card with embossed
`012 324…` (pexels 11363562, 96,364 b). Full-resolution sweep: **no issuer mark, no
network logo, no hologram, no legible text of any kind** — verified against a sheet in
which cells 5 and 6 were solid `VISA` / `Mastercard` / `AMERICAN EXPRESS` / `DISCOVER` /
`PayPal`. Shallow DOF, one focal object: the calmest frame available for the densest
card in the chapter (`stock-photo-sourcing` BOX rule 2). The card carries no printed
rate, so nothing in the photograph competes with or contradicts the shape-only claim.

**4 — s22, the snowball, and why a snowman shipped.** Four rounds and 24 cells produced
no photograph of a snowball with a track. The line names a snowball, and rule 3 of the
sound-off test says the thing the line NAMES must be in frame — so the frame is
`s22.jpg`, a snowman in a dark winter forest (pexels 30296986): three rolled snowballs
stacked, i.e. *small ball → big*, which is the accumulation the line asserts. It has no
people, real dark structure behind it (trunks, benches) so it is not an empty white
field, and its smile is not out of step with a line that ends *"a massive psychological
win"*. **Judgement recorded for the reviewer**: the alternative was children rolling
snow (wrong audience) or a hand packing a snowball (no growth). Flagged in Owed.

**5 — the three same-object runs the storyboard declares, kept distinct.**
- ch2 `D D D` s14–s16 (§6, "one mechanism in three moves"): bucket *object* (warm shed
  interior) → water *leaving* (top-down wet pavement, organic ripples) → the *two*
  outlets (flat-on wall, hard geometry). Three subjects, three framings.
- ch2 `C C C` s19–s21 ("one legal pad, three states"): an aged hand *writing* → the
  bills *laid out* to be ordered → ticks *progressing* down a row with the marker at the
  next one. Three states, three subjects, no two the same photograph.
- s12/s13: horizontal bright slab at ground level vs vertical dark tower from below —
  the pair IS 2.1–2.2's argument (foundation vs skyscraper), so the kinship is the point.

**6 — what the promoted sheet showed that no per-image read could.** First read of
`IMAGES-ch2.jpg`: **no two of the 18 cells say the same thing** — 18 distinct subjects,
no repeated object anywhere in the chapter. One tonal finding, recorded not fixed:
**s20 · s21 · s22 are three consecutive high-key frames** (white marble flatlay → white
paper macro → snow). I re-fetched s20 to break it and rejected the result: the six
darker candidates were €100 notes, a phone screen showing a calculator app, a hands-
writing frame that would twin s19, and crumpled-paper-on-a-floral-tablecloth. The
current s20 serves its line (*"list your debts… attack the one at the top"* → US mail,
US coins, a calculator) where the darker ones served only the tone, and per
`stock-photo-sourcing` BOX rule 6 the failure mode is **contrast collapse and emptiness,
not brightness** — all three cells carry a real subject, real edges and real falloff
(s20: pen, dark mug, coins; s21: black circles + marker, shallow DOF; s22: dark trunks).
Handed to fin-build/review in Owed rather than churned.
Closest kinship after that: **s15 and s16 are both monochrome grey and adjacent** —
accepted because they are two moves of one declared mechanism and their compositions
are opposites (top-down organic vs flat-on geometric).

**7 — acceptance numbers.** `pipeline_check check assets --slug financial-freedom-after-50
--cut en --chapter 2` → **PASS**, so all 18 clear `min_image_bytes` 10240 (smallest:
s21 at 92,394 b, 9× the floor), `min_source_yhigh` 110 (including the near-black s23b,
whose water streams are what the 90th percentile lands on), and **every image
`index.html` will render has an attribution row**. All 18 are `@pexels` picks at 1880 px
against `assets.min_width_px` 1600 — no Pixabay, no upscale anywhere in this chapter.
`CREDITS.txt` = 18 rows, 1:1 with the 18 images, re-keyed in place on every re-pick;
every row is Pexels License (no attribution-mandatory Commons file in this chapter,
unlike ch1's s6/s10).

**8 — dedupe.** `find studio/videos vault/videos \( -path '*/final/*.jpg' -o -path
'*/assets/img/*.jpg' \) ! -path '*/_cand/*' -print0 | xargs -0 md5sum | sort | uniq -Dw32`
→ **empty**. The unfiltered form reports one pair — `_cand/s20.jpg` = `_cand/s25.jpg`,
because both slots were sheeted from the same query in round 8. Those are throwaway
preview grids, not promoted images; **no two promoted `sNN.jpg` collide** anywhere on
either channel. Worth knowing that `-path '*/final/*.jpg'` sweeps `_cand/` in as well.

**9 — sheets that came back short, counted.** `_cand/s14.jpg` rendered **5 of 6** in
round 2 (the tool printed `5 candidates`); every other sheet in all 9 rounds rendered
6 of 6. No sheet was treated as a failed query on cell count alone.

**10 — one provenance note the pixels do not show.** `s14.jpg`'s Pexels title is
*"Rustic Japanese Workshop with Traditional Tools"*. The frame itself carries no
signage, no script, no plug, no vehicle and no currency — a galvanised bucket, wooden
tool handles and board walls — so it passes the US sweep on what is *in frame*. Recorded
because the title is in `CREDITS.txt` and a later reader will see it.

## Changed

Files written, all under
`studio/videos/financial-freedom-after-50-en-ch2/assets-ch2/final/`:

| slot | line | image (all @pexels) |
|---|---|---|
| s12 | 2.1 foundation | poured slab, formwork perimeter, rebar dowels, layout chalk |
| s13 | 2.2 skyscraper | steel-braced tower facade from below, dark sky |
| s14 | 2.3 the bucket | galvanised bucket on boards, dark shed |
| s15 | 2.4 holes in the bottom | rain running across pavement into a street grate |
| s16 | 2.5 the TWO leaks | **two** taps on a block wall (count verified at 1:1) |
| s17 | 2.6 `north of 20%` | brandless chip-card macro (hero num frame) |
| s18 | 2.7 negative return | hands holding an **empty** wallet, top-down (icon sits here) |
| s19 | 2.8 a plan first | **aged** hand writing on a ruled page |
| s20 | 2.9 order by rate | US mail + US coins + calculator, laid out |
| s21 | 2.10 roll it down | ticks progressing down a row, marker at the next |
| s22 | 2.11 the snowball | snowman in a dark winter forest |
| s23 | 2.12 the surprise | open hood, engine bay, rag in hand, no badge |
| s23b | 2.12 *cut-in*, "leaky roof" | rain streaming off a dark roof edge |
| s24 | 2.13 the worst option | safe-deposit vault corridor |
| s25 | 2.14 3–6 months | bundle of US $50s in a kraft envelope |
| s26 | 2.15 keep it separate | **two** unlabelled binders |
| s27 | 2.16 shock absorber | coil-over damper, B&W |
| s28 | 2.17 peace of mind | man 60+ on a US porch with a mug |

Plus 18 `.src` sidecars (verified 1:1 against `manifest.json` after the last re-pick —
every slot's query string equals its `.src`), `CREDITS.txt` (18 rows), `manifest.json`
(the `_note` records why every slot is `@pexels` and names the three same-object runs),
`IMAGES-ch2.jpg` + `IMAGES-ch2.json`. `_cand/` sheets left in place as throwaway.

**Nothing dropped.** The `s23b` cut-in was three rounds from being dropped under the
"drop rather than fake it" rule; changing the source (a roof *in rain* rather than a
water-stained ceiling) got an honest frame, so all 3 storyboard cut-ins survive.

## Owed

**To fin-build:**

1. **s16's frame must hold both taps for the whole 6.469 s.** The count is the fix
   (parent ruling 2); a ken that pushes past either tap re-opens it. Same class as ch1's
   s3 note.
2. **s18 is the icon scene.** The `warnc` down-step arrow carries the assertion — the
   photograph says *the wallet is empty*, not *this is a negative return*. It must land
   over the wallet's dark interior, not over the pale wood, or the stroke disappears.
3. **s20 · s21 · s22 are the chapter's three pale frames, consecutive** (120.7 s →
   139.8 s). Each passes on its own (real subject, real edges, real falloff) and the
   locked grade takes all three toward mid-grey, but if the draft reads flat across that
   run, the lever is the archetype/plate on s20 (arch C) — **not** a per-scene `filter:`,
   which the chapter layer closes (`storyboard-<cut>.md` §9, and the creator rejected
   exactly that on 2026-08-04).
4. **s25 does not state "three to six".** No photograph can — it is a duration range.
   The chip row is the only place that number appears, and per `facts-staging` §2 it
   ships as `OPINION / CONVENTION` with **no agency card and no source line**.

**To fin-review — two judgement calls, both mine, both reversible:**

- **s22, the snowman.** Four rounds, 24 cells, no snowball-with-a-track exists in either
  reachable pool. A snowman is three rolled snowballs, so the named object and its
  accumulation are both in frame, but it is the most whimsical image in a 50+ retirement
  cut. If the tone is judged wrong, the honest next move is a drawn layer (storyboard §8
  declares ch2 at 1 icon, 0 Lotties, so this would be a storyboard change), **not**
  another sheet — I have exhausted the photographic option.
- **s24, the vault.** Reads *the accounts, locked away* under "never raid the retirement
  account". It is the closest honest frame after the piggy bank failed on Lithuanian
  centai; it asserts *secure* where the line warns about *raiding*, which the head
  ("THE WORST OPTION") resolves but a reviewer may read differently.

**Standing:** all 18 rows in `CREDITS.txt` are Pexels License — commercial use, no
attribution condition — so unlike ch1 (s6 CC BY-SA 3.0, s10 CC BY 2.5) nothing in this
chapter is attribution-mandatory. The rows must still travel with the pixels on any
hand-copy, rename or promotion downstream, and the file must stay 1:1 with what
`index.html` renders — that is what `check assets` asserts.

**MISSING-CONSTANT:** none. **OPENED-BODY:** none — the two BOXes in
`tools/packs/fin-assets.md` covered every call this run, including the contrast-collapse
correction (rule 6) that decided the s20/s21/s22 question.
