# fin-assets · passive-income-number · hi · chapter 1 · attempt 8

**Scope:** targeted re-fetch of TWO slots only — `s3` (the editor's blocker) and
`s1` (should-fix, ruling 3). Nothing else in `assets-ch1/final/` was touched;
`pipeline_check check assets --slug passive-income-number --cut hi --chapter 1`
→ **PASS**.

| slot | outgoing | incoming | px | md5 |
|---|---|---|---|---|
| `s3.jpg` | chai glass on a window sill (archived `retired-attempt6/s3.jpg`) | glass of tea + porcelain cup + **whole dark-screen phone** on one table | 1880×1253 | `0f9b33b703034e39edf84b1750751dfe` |
| `s1.jpg` | dark phone on a dark wooden table (archived `retired-attempt6/s1.jpg`) | unmade bed, first light through an open window — **textile** | 1733×1300 | `3628bfdd247cd2a9a644acb1b1f6b9de` |

Both hashes are unique across every `.jpg` under `studio/videos/` (151 files,
`_cand/` excluded). Both credits are Pexels-native — neither carries the
"by Pixabay" tell that marks a cross-pool duplicate. CREDITS.txt rows were
re-keyed by the tool on promotion and the stale attempt-7 `s3` row is gone.

## s3 — the blocker, and the answer to the question the brief asked

**Confirmed, having opened `assets-ch1/final/s3.jpg` at FULL RESOLUTION
(1880×1253, byte-identical to the file I read — md5 verified against my stashed
copy): the frame contains BOTH a GLASS of tea and a WHOLE dark-screen PHONE, on
one table.** Specifically: a clear glass mug of amber tea with a spoon standing
in it (left of centre), a smartphone lying face-up with a completely dark screen
directly below it, and a porcelain cup and saucer to the right. Screen dark, no
logo, no legible text anywhere in frame, no hands, no faces, no currency, no
signage. This is the thing attempt 7 got wrong (it fetched the phone and dropped
the glass) and it is what closes the blocker.

**Object positions, normalised — fin-build needs these for the crop:**

| object | x | y |
|---|---|---|
| tea glass | 37–53% | 53–76% |
| **phone** | 34–65% | **75–87%** |
| porcelain cup + saucer | 55–90% | 30–79% |
| window strip (blurred street, a blurred animal walking) | — | 0–26% |

The phone sits **low** in the source. A low `background-position` (≈`center 90%`)
does two jobs at once: it lifts the glass+phone pair toward the middle of the
16:9 crop, and it crops the window strip and the animal out of the top. The
§6b hold is then **one file, one `background-position`, ken 1.00→1.08 on s3 and
1.08→1.30 on s4** — the exact construction `editor-en-ch1-2` finding 1 settled on
for the sibling cut. At 1.30 the glass sits centre-frame and the phone reads at
~40% of frame width. `s4.jpg` stays on disk, unused, with its credit row intact;
the manifest says so explicitly so nothing dangles.

**Declared deviation on s3:** it is a tea GLASS, not a *chai* glass, and the
setting is a café table by a window rather than an Indian domestic counter — the
gold-rimmed porcelain cup beside it reads European tea-room. The frame is
currency-neutral and text-free, so it breaks no standing rejection, but it is not
the Indian kitchen counter the script's `img:` cue describes. It does keep an
antecedent for **s80 (7.7)**, whose callback was briefed to rhyme with the chai
GLASS: the rhyme survives as *a glass of tea*, and s80's own brief should be
re-read against this file rather than against the retired sill photograph.

## The measured finding: chai-glass-plus-phone is not in either pool

**25 contact sheets, ~150 candidate cells, both pools.** Queries tried, all
scanned by result slug and the promising ones opened as sheets:

- Pexels: `chai glass and smartphone on a table` (+`#7`, `#13`) · `chai phone` ·
  `chai smartphone` · `glass of tea and mobile phone on wooden table` ·
  `tea glass mobile phone` · `indian tea glass and mobile phone on kitchen counter` ·
  `turkish tea glass and mobile phone on a table` · `turkish tea and smartphone on wooden table` ·
  `morning newspaper tea glass and mobile phone` · `still life mobile phone and glass of tea on a table` ·
  `tea in glass cup and mobile phone flat lay` · `glass tumbler and mobile phone on table` ·
  `smartphone and drinking glass on wooden table warm light` · `morning tea and phone on the table at home` ·
  `flat lay tea glass smartphone notebook morning` · `red coffee mug on table with smartphone` ·
  `cup of tea and smartphone on a wooden table` · `glass of tea and smartphone on a dark wooden table morning light`
- Pixabay: `tea smartphone` · `chai glass phone` · `tea cup mobile phone wooden table` ·
  `tea glass smartphone table morning` · `tea glass phone table wood`

**The pattern is stable and worth recording:** a query naming *chai / tea glass*
returns chai and no phone; a query naming *phone* returns a phone and no drink;
a query naming both returns whichever noun the photographer titled the file
with. The two-object still life the brief asks for exists in exactly one
aesthetic — the Western "coffee + phone" flatlay — and every warm, uncluttered
instance of it fails on something else. **`cup of tea and smartphone on a wooden
table@pexels` is the only phrasing that returned a frame with both**, and it
returned the same frame at cell 1 for two different queries, i.e. it is the
pool's single best match, not a lucky draw.

### Two near-misses killed at FULL RESOLUTION, both invisible on the sheet

1. **`red coffee mug on table with smartphone` (10000×7501).** Best cell of 18
   sheets on the contact grid. At full size it is an **outdoor café table**: two
   wallets, sunglasses, a red duffel bag and a pavement behind, and the phone is
   **cut off by the right frame edge** — so it could never be the centre of s4's
   crop. Rejected.
2. **`cozy coffee setup with smartphone and mug` (7952×5304).** Warm oak flatlay,
   looked clean on the grid. At full size the phone is **face-down with a legible
   Apple logo**, beside a coffee tin with legible label text. Rejected — this is
   the readable-brand-mark rule, and it was completely invisible at cell size.

Both confirm the standing rule: the contact sheet is a shortlist, never a verdict.

## s1 — textile, and a deviation I am flagging rather than hiding

Editor ruling 3 asked for bed linen or a bedside cloth. Delivered: an unmade bed,
rumpled linen, first light through a small open window, cool-toned. It matches
s1's **declared ground `#161f2b`** and the storyboard §11 colour walk ("ch7
returns to the morning, the same cool as s1") — which is why I took this cell over
the warm sunrise-stripe alternative in the same sheet, which is the prettier frame
but would have fought the declared ground. No people, no brand, no text, no lit
screen. It breaks the s1/s4 near-pair and takes wood off the chapter's opening.

**Declared deviation: the phone is not in frame,** so sound-off test #3 ("is the
thing the line NAMES actually in frame?") is not met on the letter — 1.1 names
the phone. Four sheets / 24 cells across both pools (`smartphone with a dark
screen lying on a crumpled linen cloth`, `black smartphone face down on rumpled
bed sheet morning light`, `smartphone on a pillow`, `smartphone lying on a wool
blanket`, `black smartphone on white bed sheet`, `turned off smartphone lying on
a linen cloth flat lay`, Pixabay `smartphone bed sheet blanket`) returned only
four kinds of thing: a person in bed holding a phone (a face — barred by the
storyboard's own standing rejection, which names s16/s70/s78 as the only frames
with a hand), a **lit** phone screen (barred), high-key white bedding (barred by
the grade rule), or textile with no phone at all. There is no fifth option in
either pool.

What the frame does say sound-off is *"a day beginning, unhurried, nobody up"* —
which is the subject of 1.1's main clause («सोचिए, एक ऐसा दिन…»), with the phone
carried by the `stmt` and by s2's alarm clock immediately after. I think that is
the right trade against a face or a brand, but it is the editor's call and I am
not pretending it is a clean pass.

## What fin-build has to do with this

1. Point **`#s4-bg` at `assets-ch1/final/s3.jpg`** with the same
   `background-position` as `#s3-bg`, and chain the ken (1.00→1.08, then
   1.08→1.30). That is the whole of editor ruling 1, and it also fixes
   should-fix 3 — s4 no longer opens on a near-black rectangle, because at 1.08
   the glass and the table are still in frame.
2. Use a **low `background-position`** (≈`center 90%`) on both, per the object
   table above.
3. `s3`'s declared ground `#241d15` (warm dark brown) no longer matches the
   photograph, which is cool with a pale tabletop. Re-derive it, and re-check the
   s2→s3 and s3→s4 temperature steps in §11's colour walk.
4. `s4.jpg` is now **unused** but must stay on disk and in CREDITS.txt.

## Counts

- **Accepted: 2** (`s3.jpg`, `s1.jpg`) — both read at full resolution before acceptance.
- **Rejected: ~150 candidate cells across 25 sheets**, of which 2 were rejected
  only after a full-resolution read (the café-clutter mug, the Apple-logo flatlay)
  and 1 was promoted, read, and replaced (the same café mug).
- **Dropped: nothing.** Both background slots are filled; no cut-in was removed.
- **Not delivered as briefed: the Indian chai glass** (delivered as a tea glass in
  a European setting) and **a phone in s1** (delivered as textile with no phone).
  Both are argued above rather than quietly shipped.
