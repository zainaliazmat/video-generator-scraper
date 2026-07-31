---
summary: fin-assets, hi cut, attempt 1 — 86 of 87 image slots fetched and eyeballed via contact sheets; one mosaic cut-in (s42m) dropped for want of an honest image. Zero md5 collisions.
updated: 2026-07-31
source: contact-sheet review of 87 Pixabay sheets + 49 Pexels retry sheets, studio/videos/first-lakh-first-thousand-hi/assets/img/
stage: fin-assets, cut hi, attempt 1
---

# fin-assets — «पहला एक लाख» hi, attempt 1

**Accepted 86 · rejected 1 (dropped) · md5 collisions 0.**

## What was done

1. `--candidates 6` over all 87 manifest slots (Pixabay) → 87 contact sheets, 522 previews,
   one vision pass per sheet.
2. **43 slots passed on the first sheet. 44 failed all six cells** — the India/finance hit
   rate matches [[../../knowledge/stock-photo-sourcing]] exactly: generic objects land,
   India-specific and pay-slip/rate-card queries return nothing usable.
3. `@pexels` retry for those 44 → 40 resolved. Three more passes (4 slots, then 1, then 1)
   resolved everything except `s42m`.
4. `--pick` promoted 86 cells at full resolution. `md5sum studio/videos/*/assets/img/*.jpg`
   → 86 hashes, all unique, no collision with any other project.

**Sourcing split: 43 Pixabay / 43 Pexels.** Pexels carries the Indian-currency and
domestic-object pool that Pixabay does not have; every ₹ slot that survived came from there.

## Dropped

- **`s42m` (5.5 mosaic minor, "interest rate card macro") — dropped, not faked.** Three
  queries returned only: US credit-card APR disclosures (12.24%–23.24% legible — a rate
  that contradicts the scene's own ~7%/12% figures), euro/zloty notes, a `Platinum Credit
  Card` agreement, and duplicates of `s21m`/`s28`. A cut-in may be dropped rather than
  faked; a background may not. **Scene 42 keeps its background (`s42.jpg`, rooftop water
  tank) and is no longer a mosaic — fin-build must render it as a plain `B` scene.**
  The M-scene count drops 7 → 6.

## Rejections that shaped the picks (all caught at grid size)

- **Demonetised ₹500.** Every Pexels "indian rupee notes" sheet is dominated by the
  pre-2016 pale-green ₹500. Rejected on `s41`, `s53`, `s56`. `s41` took the one cell with
  no ₹500 in it (₹1/₹5/₹10/₹20/₹100 spread); `s56` abandoned notes entirely for a disc of
  Indian coins. `s50` verified at full resolution: **current purple ₹100 series, correct.**
- **Dollars answering a ₹ query.** `s34` (five of six cells were US bills in a red
  envelope), `s52m`, `s78`, `s11`, `s19` — all re-picked to a cell with no $ in frame.
- **Brand marks.** `ABUS 65/50` padlock (`s72`), `THE WALL STREET JOURNAL` (`s16`),
  `Royal Mail` (`s36`), `ethereum`/bitcoin coins (`s12`, `s18`, `s19`), `Tinkoff Bank`
  (`s78`), `LOTTO`/`EUROJACKPOT` (`s52m`), Mastercard in a jeans pocket (`s21m`),
  a payment terminal (`s42m`), `Minions` (`s17`), `BARCELONA` cast into a tap (`s35`),
  `YOKOHAMA` manhole (`s23`).
- **`s52m` was fetched, then re-picked after full-resolution inspection** — the first pick
  carried a legible `FICO` credit-score mark and unrelated 5.31%/11.0% figures. Replaced
  with a plain printed page (no brand). The stale CREDITS line was removed by hand.
- **Phone screens.** `s13`'s top four cells were month names on a phone; the whole slot was
  re-queried. `s78` (the scene the storyboard names as *the* phone trap) is an open
  handwritten account book — no screen anywhere in the cut.
- **Faces.** `s47` (woman on steps), `s49` (crowded bus queue), `s79`, `s52`, `s60` all
  re-picked to a hands-or-object cell. `s60` is a gloved hand on a ladder rung; `s49` is
  three silhouettes at a dusk bus stop; `s75` is a potter's hands only.
- **Chart direction.** `s12`'s only usable Pixabay cell was an *ascending* coin staircase —
  which argues the opposite of "100% savings, 0% returns" at 2.2. Re-queried to level
  stacks on a dark table.

## Notes fin-build and fin-audit must act on

1. **The one per-scene grade override: `s46` (5.9, R).** Near-black by capture — deep-shadow
   stone steps, most of the frame under ~20%. `grayscale(.32) brightness(.62)` will crush it
   flat. Set inline on that one `.bg`:
   `filter: grayscale(.32) brightness(1.40);` — **this is the video's only override; do not
   add a second.**
2. **R-scene left-third luminance is eyeballed, not measured.** The stage has no metering
   tool in its allowlist. The ten `R` scenes were chosen dark-left by eye: `s1` (dark bowl,
   lamp top-left), `s17`, `s26`, `s33`, `s46`, `s63`, `s76`, `s84` (b/w brick facade fills
   the left third). **`s76` is the weakest** — warm mid-brown shards on soil; measure it
   before locking chapter 8 and swap to a darker crop if it reads above 25%.
3. **`s14` (2.4, post office) carries Cyrillic counter signage** and four small out-of-focus
   figures in the far left. The subject — a wall of numbered brass-locked PO boxes — is
   correct and dominant, and Pixabay/Pexels have no Indian post-office interior. Kept
   deliberately; look at it once at grade, and if the signage reads, crop right.
4. **`s84` is a New-York-vernacular rooftop water tower**, not an Indian overhead tank. It
   was chosen for the R-scene luminance (dark left third) and the silhouette. The Indian
   register is carried by `s42` and `s58`, both plain domestic tanks.
5. **`s39` → `s40` continuous zoom works as designed** — a brass two-pan balance shot square
   on a shelf, so the tighter crop into the fulcrum at 5.3 (CROSSOVER) has something to
   crop into.

## Files

- 86 × `assets/img/s*.jpg` + 86 × `.src` (each `.src` holds the query that fetched it)
- `assets/img/CREDITS.txt` — 86 lines, one per kept image, verified 1:1 against the manifest
- `assets/img/manifest.json` — pruned to 86 slots, queries rewritten to the ones actually
  used (43 now carry the `@pexels` suffix), so a re-fetch reproduces this set
- `assets/img/_cand/` + `retry.json` — throwaway, not shipped, not archived
