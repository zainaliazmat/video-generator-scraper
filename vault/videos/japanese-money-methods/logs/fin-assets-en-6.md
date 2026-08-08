# fin-assets — japanese-money-methods · en · attempt 6

**Scope as briefed:** replace `assets/img/s76.jpg`, delete `s77.jpg`.
**Scope as executed:** replaced `assets/img/s77.jpg`. Nothing deleted. Reason below.

## The brief named the wrong file (en scene numbering is +1 vs hi)

The hold pair is real, but in the en cut it is **s77 + s78**, not s76 + s77:

| beat | hi scene | hi image | en scene | en image |
|---|---|---|---|---|
| 7.2 | s74 | s74.jpg | s75 | s75.jpg |
| 7.3 "what there is, is enough" | s75 | s75.jpg | **s76** | **s76.jpg** |
| 7.4 "the empty square hole…" | s76 | s76.jpg | **s77** | **s77.jpg** |
| 7.5 "each needs that emptiness…" | s77 | s76.jpg (held) | **s78** | **s77.jpg (held)** |

`index.html` already wires the en pair to ONE file — `#s77-bg` and `#s78-bg` both
carry `url(assets/img/s77.jpg)` (s78 at `background-size:auto 130%`), and there is
no `s78.jpg` on disk or in the manifest. The en cut was **never** broken in shape;
it was broken in *subject* — the one held image was a dragon-spout chozuya with no
square anywhere in frame.

Deleting `s77.jpg` as instructed would have blanked BOTH 7.4 and 7.5. Not done.
`s76.jpg` is scene 7.3's own background (its own VO line, rail on) — a separate
scene, correctly a separate photo, left untouched.

## What shipped

`s77.jpg` — stone garden basin shot from above, unmistakable **square** opening
filled with still dark water, one fallen leaf, green bokeh beyond.

- query `square stone water basin japanese garden@pexels#7`, cell 2
- https://www.pexels.com/photo/serene-leaf-floating-on-water-in-birdbath-37181885/ · Dhanush N · Pexels License
- **1880 × 1253** (RAIL OFF full-bleed hero, honours the ≥1600 rule)
- **mean luminance 119.9** measured (`ffmpeg format=gray` → byte mean), inside the
  60–120 band; no `filter:` override needed
- md5 `b10dbac4…` — `md5sum studio/videos/*/assets/img/*.jpg | uniq -d` returns
  nothing across both cuts and every other project
- read at full resolution: no text, no signage, no brand mark, no people, no
  currency, no CGI

## Sheets viewed (4 searches, 4 vision passes, 20 cells)

1. `tsukubai stone water basin square hole japan@pexels` — 6/6 rejected: every
   basin round (flower pot, granite ladle basin, bamboo spout), one Buddhist
   statue as subject, one cluttered frame with a bystander's clothing.
2. `ryoanji tsukubai stone basin kanji inscription kyoto@pexels` — 6/6 rejected:
   carved stone pillars (not a basin), a temple *signboard* (readable kanji as
   the subject — same trap as a brand mark), and **cell 5 was the hi cut's own
   s76.jpg**, i.e. the pool's answer to this query is the image I must not reuse.
3. `tsukubai` (pixabay) — sheet came back **2 of 6**; both round backyard water
   features, one a garden-centre installation. Rejected. (`ryoanji` on pixabay:
   zero results — the ₹-pool lesson generalises, this pool has no Ryoan-ji.)
4. `square stone water basin japanese garden@pexels` — same six as sheet 1,
   re-ranked. Re-run at **`#7`** (offset, no new query) surfaced the winner.

**The knob that worked:** the offset, not the wording. Three different phrasings
returned the same six photographs — Pexels' top-6 for "japanese stone basin" is a
fixed set, and every one of them is round. `#7` was the only move that reached new
inventory. Reach for `#N` earlier when two rewordings return a familiar sheet;
rewording a third time is the expensive way to page through the same results.

**Second note:** naming the SHAPE beat naming the place. `ryoanji`/`tsukubai`
returned signage and pillars; `square stone water basin` returned the object the
VO points at. Same lesson as naming the denomination on a currency slot.

## The trade in the accepted image

It is a garden basin, not a photographed Ryoan-ji tsukubai — no kanji ring, no
temple in frame. Ryoan-ji's basin is not in either free pool (20 cells prove it),
and the alternatives were: a square-cut Japanese chōzubachi whose opening reads
*rounded* at full size (fails the one word the VO says — "square"), or reusing the
hi cut's file (fails md5). Chose the frame that shows the square, since the act's
surrounding scenes (zen gravel, moss path, the 7.3 basin, the on-screen
"tsukubai inscription at Ryoan-ji" footer) already carry the location. Nothing in
the frame contradicts Japan; it simply doesn't assert it.

## Files touched

- `assets/img/s77.jpg` (replaced), `s77.jpg.src` (rewritten by the tool)
- `assets/img/manifest.json` — s77 query updated
- `assets/img/CREDITS.txt` — s77 line replaced in place (not appended)

Verified 1:1: 93 jpgs, 93 CREDITS lines, 93 manifest keys, zero orphans either way.

**Accepted 1 · rejected 19 · dropped 0.**
