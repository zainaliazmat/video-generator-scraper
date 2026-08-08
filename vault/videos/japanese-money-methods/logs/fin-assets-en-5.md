# fin-assets — japanese-money-methods · en · attempt 5

Scope: exactly two slots — `s77.jpg` (scene 7.4) and `s32b.jpg` (scene 3.11 panel
swap). Library otherwise untouched, still 93 images / 93 `.src` / 93 CREDITS lines.

## What was wrong (fin-build-en flags)

| slot | on disk at start | why it failed |
|---|---|---|
| `s77.jpg` | Pexels "serene japanese garden bamboo fountain detail" — square stone block with a **round** water pool | 7.4's focal names "the empty square at the centre"; no square anywhere in frame, so the words pointed at nothing |
| `s32b.jpg` | Pixabay "plaster old texture fallen" — a second wall texture | the slot is framing 2 of a `data-framings` panel swap; a panel swap must reveal a NEW SUBJECT, and this was a colour shift off `s32` |

## Result

| slot | accepted | source | px | md5 |
|---|---|---|---|---|
| `s77.jpg` | dragon-spout chōzuya, **Kyoto** — square granite basin, bamboo ladles, water running, real vertical kanji on the post | Pexels / Sachith Ravishka Kodikara | 1880×1253 | `bed941e7…` |
| `s32b.jpg` | **Taitō-ku ward notice board**, Tokyo — 「台東区掲示板」/「浅草公園町会」, six public notices pinned to a green board on a blue block wall, red 消火器 cabinet | Pexels / Dane Cardiel | 1880×1246 | `bccd0359…` |

Accepted 2 · rejected (full-res or sheet) 4 named below + ~185 sheet cells · dropped 0.

## The s77 search — the specified subject does not exist in either free pool

The brief's first choice was the **Ryoan-ji zenigata tsukubai** (round stone, square
central hole, four kanji borrowing it as their 口). **9 query rounds, 32 contact
sheets, ~190 candidates, both pools** — it is not in Pixabay or Pexels free:

- English object queries: `tsukubai` (2 results total), `chozubachi` (0), `chozuya`,
  `temizuya` (3), `temizubachi` (0), `zenigata` (0), `japanese stone basin with
  square hole`, `japanese stone water basin top view`, `square stone basin filled
  with water`, `stone with a square hole`, `square hole carved in stone`
- place queries: `ryoanji`, `ryoan-ji`, `ryoanji temple kyoto`, `龍安寺` (1 result:
  the rock garden, no basin)
- Japanese-language queries: `つくばい`, `手水`, `手水鉢`, `水鉢`, `日本庭園 水鉢`,
  `知足` (0), `枡`, `四角い穴`
- offsets to #7/#13/#19/#25/#31 on every productive query

By round 4 both pools were visibly recycling the same ~8 basin photographs.

**Three full-resolution rejections at the promote step** (the sheet hid all three):

1. **Miyajima stone lantern** (`japanese temple stone basin#13@pexels` cell 6) — the
   sheet showed a clean empty square at the centre of carved granite. At 1880 px the
   square is glazed with a **latticed shoji panel**: not empty. Also a lantern, not a
   basin, and `s78` holds this same file on "water rings spreading" — a lantern has
   no water, so the hold pair breaks too.
2. **"Temple hand washing basin japan" cell 2** — the wooden placard reads
   **净手净身，礼拜佛陀，珍惜每一滴水**: `净` is the *simplified Chinese* form (Japanese
   writes 浄). A **Chinese** Buddhist temple sold by a Japan-tagged query. Same trap
   this run already caught with the Chinese menu board — invisible at grid size,
   obvious at full res.
3. Sheet-level: `japanese street wall covered with posters` cell 5 was Chinese
   (城市傍晚); `貯金箱` returned a **Kinder**-branded egg and euro notes; `japanese post
   office savings passbook` returned **Chinese** postage stamps (中国人民邮政).

### What was shipped instead, and the gap that remains

The accepted `s77` satisfies the brief's *second* acceptance clause — "any Japanese
stone tsukubai with a clear square central basin": the basin is a square-cut granite
box, it is the object the VO actually names ("the basin"), it carries water for the
`s78` hold ("water rings spreading"), the kanji in frame are real Japanese, and the
Pexels title independently places it in Kyoto.

**It does not show a small square HOLE at the centre of a round face.** That frame is
not sourceable from the free pools. Two ways to close it, both outside this stage:

- reword 7.4's focal from "the empty square at the centre" to something the frame
  supports (the square basin itself), **or**
- accept the square basin as the referent — the build already draws the `▣` glyph and
  the `reveal` at 518.77, so the square the viewer sees is the drawn one.

Flagging rather than silently shipping the same defect class.

## `filter:` override — the one this video is allowed

`s77.jpg` mean luminance **45.7**. Under the global grade
(`brightness(0.62)`) it lands at ~28 on screen — too dark for a RAIL-OFF full-bleed
hero. Neighbouring `s76` is 68.0 → ~42 on screen.

**Scene 7.4 (and 7.5, which holds the same file) wants:**

```
filter: grayscale(0.32) brightness(0.95) contrast(1.02);
```

45.7 × 0.95 ≈ 43 — matches `s76`'s on-screen luminance, so the pair reads as one
continuous shot. This is the **only** `filter:` override in the cut (fin-assets-en-3
recorded none), so the budget of one is now spent. `s32b` is 112.4 — no override.

## `s32b` — what it says and one thing to know

Scene 3.11's VO ends "…and a government savings campaign", and the panel swap needs a
new subject. A ward notice board with public notices pinned to it is the closest
sourceable read of "a government campaign poster on a wall": real Japanese civic
signage, no brand marks, no face as subject, and it is unmistakably a different
subject from `s32`'s plaster — which is what the swap exists to do.

Worth knowing before it ships: the largest poster on the board is a **Tokyo air-raid
records exhibition** (東京大空襲資料展) — bomber silhouettes over a map, ~10% of frame
width, legible only on a freeze. Two small portrait photos sit in other notices
(neither is the subject of any claim). Nothing that breaks a rule; noted because a
war notice under a savings line is off-topic if anyone pauses. The alternatives in
the same pool were worse: shopfront brand signage, an identifiable pedestrian with a
taxi, and a Chinese poster wall.

Nothing better exists for "vintage japanese government savings campaign poster":
`貯金箱`, `japanese piggy bank coin savings`, `vintage japanese poster wall retro`,
`japanese post office savings passbook` all returned euro currency, brand marks
(Kinder, Chanel, Alfa Romeo), or Chinese subjects.

## Integrity checks

- **md5 across BOTH cuts** — `md5sum studio/videos/*/assets/img/*.jpg | sort | uniq -d`
  on the hash column returns **empty**: no image on either cut shares a hash with any
  other, including the two new ones.
- **CREDITS 1:1 with disk** — 93 lines, 93 jpgs, `comm -3` between the two lists is
  empty. Both slots were **replaced** in place (lines 92/93), not appended; no probe
  slot (`p*`/`q*`/`r*`/`t*`/`u*`/`v*`/`w*`/`x*`/`y*`) leaked a CREDITS line.
- `.src` rewritten for both; `manifest.json` queries updated to what actually fetched
  the files (they had drifted — `s32b` still read the storyboard's wording, not the
  query that produced the file on disk).
- US-cut constraints: no ₹, no Devanagari, no Indian institution, no US-market
  contradiction in either frame. Both subjects are Japanese — correct, Japan is the
  story frame.
- The throwaway `_cand/` sheets are left in place for post-delivery cleanup; the
  temporary probe manifest was deleted.
