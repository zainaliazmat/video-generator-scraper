---
summary: fin-assets, en cut, attempt 1. 93/93 image slots filled via contact sheets; 27 slots re-queried after the first sheet failed all six cells, 5 more re-picked on md5 collision with the hi cut, 1 rejected at credit-check for being a foreign government building. Zero duplicate hashes across either channel.
updated: 2026-07-31
source: tools/stock/pixabay_fetch.py contact sheets (_cand/), storyboard-en.md §6/§9, knowledge/stock-photo-sourcing.md, script-en.md VO lines
stage: fin-assets, cut en, attempt 1
---

# fin-assets — en cut, attempt 1

## Result

**93 accepted / 93 slots. 0 dropped. 0 cut-ins removed.** Every scene ships a
background photo (`photo_free_scene_ratio` 0 holds). 120 contact sheets built
(93 first pass + 27 retry + 3 second retry), one vision pass per sheet.

| | count |
|---|---|
| Slots in manifest | 93 |
| Accepted on the first sheet | 66 |
| Re-queried (all six cells failed) | 27 |
| Re-picked on md5 collision with the hi cut | 5 (s82, s42, s91, s71, s43) |
| Re-picked at credit-check (wrong country) | 1 (s40) |
| Cross-project duplicate hashes remaining | **0** |
| Images without a CREDITS line | **0** |

## The 27 slots whose first sheet failed entirely

The manifest's queries were over-specified noun phrases; the APIs matched one
or two words and returned the wrong subject. Shortened, object-first queries
fixed all 27. Representative failures:

- `pay stub perforated edge macro@pexels` → six photos of **perforated metal panels**.
- `enamel mug coins bills kitchen counter` → six **real-estate kitchen interiors**, no mug, no money.
- `two glass jars coins side by side` → **couples walking and horses**.
- `wall calendar months crossed off` → four of six were **phone screens** displaying month names (the shipped-three-times trap).
- `hand crank drill on workbench` → **Bosch** and **DeWalt** logos legible, plus a branded beer can.
- `hand dropping bills into steel cash box` → six frames of **euro** notes and coins in a `$` cut.
- `stone federal building facade low angle` → the **Reichstag**, a **Bundestag** U-Bahn sign, and the German Federal Court.
- `three galvanized buckets in a row` → **soldiers in dress uniform**, faces to camera.

Lesson for the manifest: two-to-four concrete nouns beat a full descriptive
sentence. Every retry query is now written back into `manifest.json`, so the
manifest matches what actually shipped and a re-run reproduces it.

## Rejections by trap category (cells refused, not slots)

- **Phone screen as a background** — s13 (4 of 6 cells), s58, s61, s84, s31, s35. Never promoted one.
- **Non-US currency in a `$` cut** — euro cash boxes (s19), Polish złoty (s11, s5, s36), a €10 note (s57), Peruvian soles (s87), UK coins (s85), a German Reich coin (s5 first pass).
- **Foreign government / landmark** — Reichstag, Bundestag, German Federal Court (s40 first pass); **Dublin's Four Courts (s40, caught only at credit-check — the photo itself looks like anonymous grey neoclassical stone)**; Leaning Tower, Eiffel Tower, Tower Bridge, Toronto skyline (s27, s46).
- **Readable brand marks** — Bosch, DeWalt, Merrell, Nissan, Mazda, Casio, Apple, Zippo, "OZLIK'S", "PosPad Plus" payment terminals (the whole s21 sheet), a "CASSA" binder, "Black Cat" peanut butter.
- **Identifiable face on a negative money claim** — s31's first sheet led with a woman posed on a couch under "what do most people waste the first six months on"; s54 cell 5 was a man's face under the median-earnings statistic. Both refused.
- **Foreign-language text in frame** — Portuguese desk calendars (s13 retry, 5 of 6), Cyrillic/Uzbek binder labels, Japanese fire buckets, a Chinese milestone, Land's End / John O'Groats signposts.
- **Chart direction against the VO** — s88 cell 3 was four coin stacks *descending* left-to-right under "the tenth ten thousand buys you six and a half months"; s35 cell 5 was a line chart with red arrows pointing down.
- **Off-brand subject** — physical Bitcoin/Ethereum props in the s91 and s43 sheets (the persona makes no product picks); a Quran on a rehal returned twice by unrelated queries.

## Two subject substitutions, declared

The storyboard's object is unavailable in either pool; the scene keeps its
background and the keyword, with a different object.

1. **s1 / s87 — the enamel mug pair is gone.** No "mug of coins" exists on
   Pixabay or Pexels; both sheets returned kitchen interiors and empty mugs.
   Replaced with a **money pair** that preserves the same "first frame small,
   last frame fuller" recall: s1 = US coins and small bills on a table,
   s87 = a wide spread of $100 bills and scattered coins. Storyboard §7's
   "s87 ← s1 re-photograph" relationship survives; only the object changed.
2. **s46 — no water tower.** `water tower sky` returned lighthouses and city
   skylines. Shipped a **lighthouse at dusk** — the same job (a fixed distant
   marker you are heading toward) for the ~$96,000 beat, and dark enough for
   the mosaic.

Smaller substitutions of the same kind: s6 (hands working clay, not a
hand-crank drill — every drill in the pool carried a legible brand), s21
(receipts + calculator, not adding-machine tape — every tape shot was a
branded payment terminal), s34 (a bare windowsill, no envelope), s71 (three
doors in a row, not three buckets — the bucket frame collided with hi s64),
s82 (a dark cracked surface, not a spilled coin jar — the only spilled-jar
photo in the pool is already the hi cut's s81).

## Two notes fin-build must act on

1. **s90 (9.8, `R`) is the one per-scene `filter:` override in this cut.**
   Measured at full res: the frame is near-pure black with a small fire core
   and a left third at effectively 0% luminance. Reversed type will read
   perfectly, but the system grade `brightness(.55)` crushes the image to
   nothing. Set on that one `.bg` only:
   `filter: grayscale(.85) brightness(1.25) contrast(1.15);`
   This is the single grade override for the video — do not add a second.

2. **s68 (7.6, `R`) should be demoted to `B`.** Storyboard §9 flagged it and
   set the rule: reject an `R` image whose left third measures above 25%.
   The shipped image is a full-frame charcoal bed — mid-grey charcoal across
   the whole frame with an orange flame *in the left third*, which is exactly
   the condition the rule was written for. The image itself is right for the
   line ("one log on a real coal bed") and should be kept; take §9's own
   fallback and **ship 8 `R` scenes instead of 9**. `R` count is a design
   choice, not a checked constant.

## Watch items (accepted, but a second pair of eyes would help at Gate ②)

- **s59** (6.7, small pile beside large pile) — copper stacks on black, but a
  few loose coins in the pile are foreign at full resolution. Dark and
  low-salience; the VO makes no currency claim on this frame.
- **s84** (9.2) — the shipped photo is a genuine paper **"Credit Card/Debit
  Card Authorization"** form, which satisfies the storyboard's hard "NOT a
  phone" guard and is the closest real object to a transfer authorisation.
  The words are legible at full res; the grade should bury them, but if the
  build shows them, re-pick cell 3 of the same sheet (a hand signing a plain
  form, no legible text).
- **s89** (9.7) — a US interstate exit sign reading "Hachita / Antelope Wells
  1 MILE". Unmistakably US and imperial, but it carries place names, which
  §6 excluded for s92 (not for s89). Left as-is.

## Dedupe

`md5sum studio/videos/*/assets/img/*.jpg` → **no repeated hash anywhere on
either channel**. Five collisions with `first-lakh-first-thousand-hi` were
caught and re-picked from the existing sheets at no fetch cost:

| en slot | collided with | fixed by |
|---|---|---|
| s82 | hi s81 (spilled coin jar) | cell 6, a dark cracked surface |
| s42 | hi s7 (desk flatlay) | cell 6, a clean white desk |
| s91 | hi s78 (open ledger) | re-queried; a closed journal with a pen |
| s71 | hi s64 (galvanised buckets) | cell 4, three doors in a row |
| s43 | hi s39 (brass balance) | cell 1, a lab beam balance |

The storyboard's provider-alternation mitigation held for the other 88 slots,
but five collisions out of 93 confirms §9's warning: alternation is a
mitigation, not a guarantee, and the md5 gate is what actually catches it.

## Files

- 93 × `assets/img/s*.jpg` + 93 × `.src` sidecars
- `assets/img/CREDITS.txt` — 93 lines, one per shipped image, rewritten to drop
  the six stale lines left by re-picks (the tool appends and never rewrites, so
  a re-picked slot ends up with two attributions; only the current one is kept)
- `assets/img/manifest.json` — updated to the 27 corrected queries
- `assets/img/retry.json` — throwaway retry manifest, safe to delete
- `assets/img/_cand/` — 93 contact sheets + metadata, throwaway
