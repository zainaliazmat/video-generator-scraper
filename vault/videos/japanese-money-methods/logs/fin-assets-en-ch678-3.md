# fin-assets · japanese-money-methods · en · attempt 3 (targeted re-source, ch6–ch8)

Scope: only the slots the ch6/ch7/ch8 editor logs mark `source new`. Every
`reuse hi:`-only row was left untouched (parent is copying those by hand).
Nothing under `assets/img/manifest.json` or any existing `sN.jpg` was modified —
all new files are `<slot>-fix.jpg` / `<slot>b-fix.jpg`.

Manifest: `studio/videos/japanese-money-methods-en/assets/img/manifest-fix-678.json`
(pruned to the 11 files that landed). 20 contact sheets built, ~120 candidates
looked at, 11 accepted, 3 fetched-then-rejected at full resolution.

## Landed — slot -> file

| slot | file | what it is | why it clears the line |
|---|---|---|---|
| s60 | `s60-fix.jpg` | Japanese goshuin book held open, brush inscription + red seals | replaces Latin letterpress (Western type under a Japanese 1904 claim). Japanese, hand-written, book-form |
| s65 | `s65-fix.jpg` | top-down: US bills in FOUR distinct piles ($20/$10/$5/$2), hand laying the fourth | the four-categories beat; four groups on a real wooden surface, not a black studio cut-out |
| s70 | `s70-fix.jpg` | iPhone lying screen-DOWN on wood beside stacked notebooks | the named subject; replaces the DSLR |
| s72 | `s72-fix.jpg` | green card on a stack of US CONSUMER CREDIT CARD APPLICATION forms | carries the `OVER 20%` half the garage shot never carried |
| s73 | `s73-fix.jpg` | hands holding an OPEN EMPTY wallet, top-down, notebook + pen | the shortfall, not the shopping. No currency in frame = no currency error |
| s79 f1 | `s79-fix.jpg` | black "Diploma of Graduation" folder on a metal bench, brick | the degree |
| s79 f2 | `s79b-fix.jpg` | black sedan at the kerb outside a red clapboard house, overcast | the car. f1+f2 now say two different items instead of "housing" twice |
| s82 | `s82-fix.jpg` | defocused night signage — warm band over blurred colour | see caveat 1 below |
| s84 | `s84-fix.jpg` | **Ryoan-ji karesansui, wide, low winter sun**, from the veranda, oil wall behind | genuinely Ryoan-ji (Commons file `250201_Ryoan-ji_Kyoto_Japan06s3.jpg`), and a completely different angle from s75 |
| s85 | `s85-fix.jpg` | crates of pomegranates/persimmons on a grocery display, shallow depth | something in frame to decide about; no text, no prices, no faces |
| s92 | `s92-fix.jpg` | two identical white mugs side by side on a wooden rail, one steaming | "send this to the friend" — two, shared, outdoors |

## Rejected AFTER promotion — do NOT wire these; files remain on disk only because deletion is out of scope

| file | why |
|---|---|
| `s66-fix.jpg` | Pexels titles it "bookmarks in Japanese"; at full res it is **Chinese** — 道德经, 唐鐘紹京, 趙孟頫. Asserts the wrong country under a Japanese woman's expense headings |
| `s72b-fix.jpg` | same photoshoot as `s65-fix` (same table, same sleeve, same "Capital Solutions" printouts) — two frames of one shoot inside one chapter |
| `s87-fix.jpg` | non-US coins (at least one bimetallic) beside the $100s; wrong currency on a US cut. s87 was the editor's optional row — leaving the existing file is the right call |

Their CREDITS.txt lines were written by the tool as they landed — strip those three
lines if the files stay unused.

## s66 — no new file, use a crop of `s65-fix.jpg`

The editor's fix for s66 is "crop hard onto ONE label of the new flat-lay; the crop
must change the subject". `s65-fix.jpg` is a wide top-down with four separated piles,
so a hard crop on the right-hand `$2` stack changes the subject from *four groups* to
*one group* — exactly the ask, at zero fetch cost. Suggested start:
`background-size:auto 260%; background-position:86% 55%`. Two stock rounds for a
standalone s66 frame both failed the trap list (motivational sticky notes with legible
off-topic text; then the Chinese calligraphy above).

## Caveats the parent should decide on

1. **s82 is the weak one.** The brief was "a wall of backlit billboards over a US night
   street, text illegible". Four sheets: every real billboard photo carried legible
   brands — Piccadilly (LANCÔME), Milan (Zalando + Italian copy), Shinjuku/Shibuya, and a
   B&W Times Square with GUESS ×3, Starbucks, Ernst & Young, She-Hulk. The vault rule is
   categorical ("Never put a real brand on screen"), so all were rejected; empty-billboard
   skeletons contradict the line (they say advertising is *absent*). What landed is
   brand-free abstract signage bokeh — the same class as the editor's own
   `reuse hi:s81` fallback. If the parent prefers the -hi file, nothing is lost.
2. **s72 small print** reads `Elan Location Code` and one `Visa` in body copy — body-copy
   scale, illegible under the scrim/grade, but it is a real issuer name. Recommend using
   it as **framing 2** of s72 (keep the garage as framing 1 for the $400 surprise), which
   also delivers the editor's split-framing option.
3. **s60 carries a modern date.** The goshuin page reads 令和六年七月八日 (Reiwa 6 = 2024)
   in small vertical brush text — legible only to a Japanese reader, versus the current
   file which asserts *the West* to everyone. Net improvement, known residual.
4. **s79 has no car keys.** No sheet in two rounds put a diploma and keys in one frame;
   f1 = the degree, f2 = the car covers two of the six items separately, which is what the
   "both framings say housing" complaint actually needed.
5. **Commons could not serve s60.** `Hani Motoko` / `Motoko Hani` → no article images;
   `Fujin no Tomo` → one modern konbini magazine rack; `Meiji era` → a trade dollar, a map,
   Emperor Meiji, museum lacquerware; `Jiyu Gakuen Myonichikan` → Frank Lloyd Wright
   buildings; `Yomiuri Shimbun` → modern office towers. The article-first provider reaches
   only subjects enwiki illustrates, and her article is not illustrated.

## Full-resolution reads that caught a defect (the sheet was lossy every time)

- s73 first pick: IKEA Poland receipts — `PARAGON FISKALNY`, `NIP 527-010-33-85`.
- s65 first pick: **four gold bitcoin props** on the table, from a query that never
  mentioned crypto — the documented failure, again.
- s85 first picks: Thai baht (`0.12B/1G`), then Colombian pesos (`$3.740`, `BERENJENA`) —
  price tags that look like dollars and are not.
- s87: bimetallic non-US coins. s66: Chinese, not Japanese. s72b: duplicate shoot.
- Provider titles are not evidence: s60 is titled "Chinese writing" and is Japanese
  (令和 era dating, 上野); s66 is titled "in Japanese" and is Chinese. Only the read counts.

## Checks

- md5 across `studio/videos/*/assets/img/*.jpg`: **no collision** for any of the 11 new
  files, none against each other, none against the other agents' `-fix` files. (The
  18-way duplicate groups in that sweep are the per-chapter project mirrors of existing
  images, not new duplicates.)
- CREDITS.txt: every landed file has its line. `s84-fix.jpg` is **CC BY-SA 4.0 by
  663highland** — attribution is a licence condition, not a courtesy; it must ship.
- Resolution: every Pexels pick is 1880 px wide (`large2x`); the Commons Ryoan-ji is
  5472 px. Nothing under the 1600 px zoom floor.
