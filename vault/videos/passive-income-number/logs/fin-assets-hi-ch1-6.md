---
summary: Style-E ch1 (hi) sourced — 8 slots, 6 reused verbatim under new names (a full rotation), 2 fetched. 24 candidates read across 4 sheets for 2 slots; 22 rejected. PASS assets-hi.
updated: 2026-08-08
source: fin-assets attempt 6, chapter 1, hi cut. Storyboard-hi §7/§10/§10a (style-E rebuild).
---

# fin-assets — passive-income-number / hi / chapter 1 / attempt 6 (style E)

**8 slots: s1–s8. 6 REUSED (no fetch), 2 FETCHED. Accepted 8, rejected 22 candidates.**
`pipeline_check check assets --chapter 1` → **PASS assets-hi**.

## The rotation, and the file it would have destroyed

Style E re-cuts ch1 by SUBJECT, so five of the six reused files change slot number.
The mapping is a rotation inside one directory, which is exactly where a copy
clobbers its own source:

| new | ← style-A | subject |
|---|---|---|
| s1 | s3 | smartphone face **down**, dark table |
| s2 | s1 | twin-bell alarm clock, light oak |
| s3 | s2 | steaming glass on a wooden sill |
| s5 | s4 | white enamel **275** plaque, red door |
| s6 | s5 | three glass jars — beans / lentils / rice |
| s7 | s6 | monochrome stone staircase |

Done by copying out of a preserved backup, never in place:
**`assets-ch1/style-a/` now holds the whole superseded style-A `final/` verbatim**
(images, `.src`, its own CREDITS.txt). That backup is not optional bookkeeping —

⚠ **`s28.jpg` (ch3) is specified as a reuse of ch1 `final/s7.jpg`, and `final/s7.jpg`
is now the STAIRCASE.** The weighing scale it actually wants survives only at
`assets-ch1/style-a/s7.jpg`. The cut manifest entry for s28 has been repointed there
and carries its credit line ("dried herbs and incense on a weighing scale", Chinese
Medicine Podcast Podcast, Pexels License). A ch3 asset run that follows the storyboard's
path literally would have silently shipped the staircase twice.

## Fetched — 2 slots, 4 sheets, 24 candidates, 2 promoted

### s4 (1.4) — the phone, face **up**, screen dead

The storyboard's own query is **retired**: a 25-word natural-language string
(`…screen completely dark and switched off… no visible brand@pexels`) tokenised into
"smartphone / kitchen / brand" and Pexels answered with brands by name — TikTok logo,
Russel Hobbs logo, a Pexels-logo mockup, a ChatGPT conversation on a lit screen. **0/6,
and the sheet tiled only 2 of the 6 previews** (the documented silent-truncation: cells
3–6 measured a flat YLOW=YAVG=YHIGH=17, the tell that they are filler and not dark
photographs).

Round 2, short and object-led — `turned off black smartphone lying face up on a wooden
kitchen table@pexels` — returned 6/6 real cells, all ≥ YHIGH 160.

| cell | what it is | YHIGH | call |
|---|---|---|---|
| 1 | phone + Apple Watch + AirPods + notebook | 205 | reject — four objects, two brand-shaped |
| **2** | **one black phone, screen dead, on a light-oak table edge** | **175** | **PICK** |
| 3 | phone + AirPods case | 213 | reject — brand silhouette |
| 4 | phone on a slatted garden bench | 160 | reject — the place is a garden, not a counter |
| 5 | gold iPhone + MacBook keyboard | 182 | reject — brand, and a desk not a counter |
| 6 | phone **screen lit**, wallpaper + a notification + "5:33" | 195 | reject — the banned lit screen, and it pre-empts the Lottie |

Promoted, read at full resolution: **1880×1253, YHIGH 177**, no logo, no legible text,
no glow. Distinct from s1 by light, surface, angle and time of day — s1 is a dark room
at a low angle, s4 is bright oak from above — which is what the "morning" rhyme needs
(same object family, legibly different photograph).

### s8 (1.8) — the stamp. Pexels is exhausted for this object; Pixabay is not

Two Pexels sheets, 12 cells, **0 usable**, and the second sheet returned four of the
same photographs as the first — the pool is spent, not unlucky:

- **Sheet 1 cell 1** (Dutch customs desk) was promoted, then **rejected at the
  full-resolution read**: `GESCHIKT` twice in large type, `AANGIFTE TOT INVOER`,
  `RIJKSTELEGRAAF EN TELEFOON`. Foreign signage, invisible at contact-sheet size, and
  a standing rejection for this cut. This is rule 1 of the stage earning its keep.
- The rest of both sheets is one genre: craft/scrapbook stamping. 4 cells carry a
  person or hands (hands are permitted only on s16/s70/s78), 3 carry legible German
  (`Persönlich - vertraulich`, `Für Ihre Aktion`, `Duplikat`), 1 is a gift-wrapping
  flatlay, 2 are letterpress type cases (letters, not a stamped document).

Pool change → **Pixabay**, short keyword query `rubber stamp ink pad wooden table`.
6/6 cells, all ≥ YHIGH 194.

**Promoted cell 4** — a worn wooden-handled rubber stamp resting on a paper slip that
already carries its blue impression. **1280×914, YHIGH 214, YAVG 110.** Sound-off it
says *the condition, applied*, which is 1.8's whole job; the impression is ink texture,
not readable words. Two caveats for fin-editor, both declared rather than hidden:

1. **1280 px** — a ~1.63× draw at full bleed. The storyboard's resolution routing
   explicitly does not list s8 ("Pixabay is fine everywhere else"), and Pexels cannot
   supply this object at all, so this is the routed trade, not a lapse.
2. **Warm brown wood** — the chapter now runs 5 of 8 frames on a wood surface
   (s2, s3, s4, s6, s8). Mitigating: the five are light oak, a dark sill, light oak,
   a pale counter and an orange-red desk, and s1 (near-black), s5 (deep red) and s7
   (monochrome stone) break the run. If it still reads samey in the encode, s8 is the
   one to move — it is the newest file and the least argued-for surface.

## The eight, measured

| slot | line | subject | px | YHIGH | md5 |
|---|---|---|---|---|---|
| s1 | 1.1 | phone face down, dark table | 1880 | 134 | `1d4daf6f9c7c` |
| s2 | 1.2 | twin-bell alarm clock | 1880 | 244 | `5fb188d34d05` |
| s3 | 1.3 | steaming glass on a wooden sill | 1880 | 162 | `83d560a3597f` |
| s4 | 1.4 | phone face up, screen dead | 1880 | 177 | `5b6b7877d663` |
| s5 | 1.5 | enamel **275** plaque, red door | 1880 | 203 | `8aaa7d6dbc0d` |
| s6 | 1.6 | three glass jars | 1880 | 160 | `ebc3f7deece1` |
| s7 | 1.7 | stone staircase, monochrome | 1880 | 203 | `699ef5b030a6` |
| s8 | 1.8 | rubber stamp on a stamped slip | 1280 | 214 | `da06090b37af` |

All eight ≥ YHIGH 110. **md5 across every image in `studio/` (both cuts, all four
chapter projects): zero duplicates** — checked with `uniq -d`, not by eye. No non-₹
currency, no `$`, no demonetised note, no prop money, no face, no readable brand, no
lit screen in any of the eight.

## Two corrections to the storyboard's reuse ledger

1. **§10a describes ch1 `s5.jpg` as "desk of paper documents". It is not** — it is
   three glass jars of beans, lentils and rice on a wooden counter (the incumbent
   attempt-5 kept, credit: Ron Lach, "clear glass jars with raw beans seeds and rice").
   The mapping is still right and the ruling still holds: the jars carry *ration*, the
   three drawn tick cells carry the count. Worth fixing in the note so the next reader
   does not go looking for a document photograph. **Bonus the ledger did not claim:
   there are exactly THREE jars under three drawn cells.**
2. **§10a says ch1 r1 blocked old `s2.jpg` "for having no window" — the photograph has
   a window.** The reuse stands either way (style E's 1.3 names a counter, and a
   steaming glass in morning light is the beat); the recorded reason is just inverted.

## Lottie — nothing fetched, nothing tinted, nothing owed

`phone-notify-credit` is already in the git-tracked library and already loadable in this
cut. **fin-build needs: 75 frames @ 30 fps = 2.500 s** for `playLottie`.

- Library file `assets/lottie/phone-notify-credit.json`; loadable wrapper already at
  `studio/videos/passive-income-number-hi/assets/lottie/phone_notify_credit.js`
  (`window.L_phone_notify_credit`), which ch1's `assets/lottie` symlink resolves to.
  The hyphenated `phone-notify-credit.js` beside it is a tombstone — do not load it.
- **No tint**, per `index.json`: authored in the system's own palette.
- **The ₹ blocker is closed and my first check was a false negative.** Grepping the JSON
  for `₹`/`₹` returns nothing because the mark is not text — `src/phone-notify-credit.py`
  draws it as five round-capped strokes (`def rupee(...)`), deliberately, with the doubled
  bar so it cannot read as ₣/$/€. Anyone re-verifying this should read the generator,
  not grep the artefact.
- `used_in` already records this cut; nothing to write back.

## Housekeeping

- `assets-ch1/final/manifest.json` — 8 keys, the two fetched queries verbatim as run.
- `CREDITS.txt` rewritten whole: 6 rows **re-keyed** to their new filenames (the rotation
  moves pixels, and a re-key in the same move is the only thing that stops it being a
  licence breach), 2 rows written by the fetcher, 1 Lottie row re-keyed `s3 lottie` →
  `s4 lottie`. The style-A `s7` (weighing scale) row was deliberately NOT carried into
  ch1 — it belongs to ch3's s28 and lives in `style-a/CREDITS.txt`.
- `.src` sidecars: the six reused files keep the query that originally produced them.
- Cut-level `assets/img/manifest.json` updated for all 8 ch1 slots + the s28 path fix.
- `_cand/` holds the last sheet per slot only (s4 round 2, s8 round 3); the rejected
  sheets are described above in full because the files were overwritten.
