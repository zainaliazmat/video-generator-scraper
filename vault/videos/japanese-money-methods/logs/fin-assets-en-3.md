---
summary: fin-assets en cut attempt 3 — full-resolution visual read of all 93 images. Narrow scope: no re-sourcing, only replace what fails the read.
updated: 2026-08-01
stage: fin-assets, cut en, attempt 3
---

# fin-assets — en cut, attempt 3 (full-res visual read)

Scope handed down by the orchestrator: everything mechanical is already verified
(93 files, 0 md5 dupes in-cut and cross-cut, 7 RAIL OFF slots all 1880px,
CREDITS complete, manifest rebuilt, `pipeline_check check assets --cut en` passes).
This pass is ONE job: look at every image at full resolution and find what must go.

Reference for what each slot was asked for: `storyboard-en.md` §per-scene table
(the `bg file — search query` column), not the `.src` sidecar alone — several
sidecars carry a *retry* query that is looser than the storyboard's spec.

## Verdicts, batch by batch (written as I go — a stall costs one batch, not the pass)

### Batch 1 — s1, s3, s4, s5, s6, s7

| slot | verdict | note |
|---|---|---|
| s1 | **REJECT** | see below — the cold-open hero |
| s3 | ok | stack of coloured envelopes + kraft mailers on wood. No text, no marks. Reads "bills and mail". |
| s4 | ok (marginal) | white card + kraft envelope + coffee + pen flat-lay. Tiny printer's mark on the envelope lip (`STORY www… MADE IN KOREA` + recycling icons) — ~120px wide in a 1920 frame, not legible at playback, not a consumer brand. Not the insurance letter that was specified, but reads as mail-on-a-table. |
| s5 | ok | three kraft gift bags (gold stars / dots) on a rock. No brand marks, no Christmas iconography — the stars are generic gift stock, not seasonal. |
| s6 | **REJECT** | see below |
| s7 | ok | multilingual wall-calendar grid. English `Monday…Sunday` is the primary column; `September/Septembre/Septiembre/Settembre` secondary. No currency, no market claim. |

**s1 — REJECT (worst defect in the cut).** Storyboard asked for `dark kitchen
counter at night lit by a small screen glow, phone edge on, screen not legible`
— an object shot with no people. What is in the file is a black-and-white kitchen
with **a child at the table**, face clearly readable in profile at full res.
Three separate failures stacked on the highest-stakes frames in the video:
1. It is the RAIL OFF cold-open, on screen **11.474s** across scenes 1.1+1.2 as
   one continuous zoom, and 1.2 is specified as a *tighter* crop — the zoom ends
   on the child's face.
2. An identifiable minor is the subject under the hook line about a paycheck
   that vanishes — the licence's unflattering-use problem, and the one the
   agent brief names explicitly.
3. Wrong subject: no phone, no glow, no counter. It is a homework scene.
Also mono, which fights every other frame in the cut.

**s6 — REJECT.** Storyboard: `small paper receipts fanned across a kitchen table`.
The file is a Polish desk flat-lay with fully legible **`SUMA PLN`** and
**`267,96`** on an orange receipt, plus `Warszawa`, `NIP` tax numbers and Polish
line items. Wrong-market currency, legible, in a US-market cut — the exact defect
class that killed nine images on the hi cut.

### How the photo is actually seen (calibrates every verdict below)

`.rail` puts the photo in a **hard-edged right panel, x=1180→1920 (740×1080)**, not
full-bleed — except on the 7 RAIL OFF scenes. A 1880×1253 file cover-fits to
1620×1080, so the panel shows the **central ~x∈[0.26, 0.74] band, full height**,
at ~0.86× native pixels (ken 1.0↔1.06 moves it ±1.2%). Text outside that band never
ships; text inside it renders at ~0.86× its pixel size. Every legibility call below
is made against that band, not against the whole file.

### Batch 2 — s8, s9, s10, s11, s12, s13

| slot | verdict | note |
|---|---|---|
| s8 | ok | mono hand + pen on a notepad. No screen (spec's ⚠), no text. Mono is a style outlier, not a defect. |
| s9 | ok | tomatoes rinsed in a metal colander under a running tap. Colander + water = the leak metaphor 1.9 asks for. |
| s10 | ok | empty chairs round a wooden table, one lamp. Exactly the slot. |
| s11 | ok | real Japanese post-town street at dusk (Magome/Tsumago). **Checked for the AI-signage trap:** the black noren at frame-left carries genuine brush calligraphy, correctly formed; the small A-frame sign is a real bilingual `SLIP` caution board. Photographic, not generated. |
| s12 | ok | full silhouette, phone screen dark, no face, no brand. Sparkler is an off-message prop but not a defect. |
| s13 | **REJECT** | see below |

**s13 — REJECT.** Scene 2.3 is where the video asserts its central figure (hero
`num 37.8%`). The file is a corporate-marketing deck whose headings read
**`Phases of Project Management`** and **`The Marketing Funnel`**, plus a
`Projected Budget` table. The USD column is fine for this market — the problem is
the labels: a marketing-funnel diagram is the backing plate for a claim about a
Japanese household savings survey. `The Marketing Funnel` sits inside the panel
band and is legible. Storyboard asked for `printed statistics table with rows of
numbers macro`.

### Batch 3 — s14…s19

| slot | verdict | note |
|---|---|---|
| s14 | ok (marginal) | ornate leather book on chalkboard green. No embossed seal as specified, but reads "an official volume". No text at all. |
| s15 | ok | mono financial report + bar chart + calculator, laptop **closed** (no screen). Body copy is stock lorem, no currency symbol, no misleading heading. |
| s16 | ok (marginal) | the "reference volumes" are Italian classics (`MARCO POLO IL MILIONE`, `GUERRA E PACE`, `CLUB DEL LIBRO`). Book titles are not a brand or a market signal; spines read as reference matter. |
| s17 | ok | RAIL OFF. Rusty scale weights `5kg`/`2kg`/`0.5kg` — perfect for the `30 TIMES` ratio. Metric marks on a US cut are not a market defect (they are antique scale weights, not a price). |
| s18 | ok (marginal) | one blank clipboard, not two printed forms. Very high-key white — a tonal outlier in a dark cut; flagged for grade, not replaced. |
| s19 | ok | Osaka/Tokyo crossing from above, umbrellas, faces indistinct. Exactly the slot. |

### Batch 4 — s20…s25

| slot | verdict | note |
|---|---|---|
| s20 | ok (measured) | international newspaper price panel carries `Norway NKr 29.00; Turkey TL 7.00; Greece €2.50`. **Measured, not eyeballed:** that type is ~9px tall on a 1080 frame, rotated, at the band's right edge — not legible at delivery scale. Kept; the contrast with s6 (≈40px, dead centre) is the whole reason s6 goes and this stays. |
| s21 | ok | genuine worn US $20s, single serial `JF 1822…` visible — no repeated-serial prop-money tell possible with one note legible, and the paper/wear reads real. |
| s22 | ok (marginal) | US asset-depreciation ledger (`New Dodge City`, `Dodge Pickup Serial #…`). Not a bank ledger on a counter, but columns of entries in English, right market. |
| s23 | ok | hand at a wooden counter, phone **screen dark** — passes the ⚠ no-faces and the never-a-phone-screen rule. |
| s24 | ok | school lockers + combination padlocks standing in for safe-deposit boxes. Cropped the lock: the engraving is an inventory mark (`PEN…`), **no Master Lock wordmark legible**. |
| s25 | ok (marginal) | open book under a lamp, deep blue — no chart as specified, but reads as printed source material and sits beautifully in the palette. |

### Batch 5 — s26…s31

| slot | verdict | note |
|---|---|---|
| s26 | **REJECT** | headline reads **`Cosmetics Sales Volume`** / `Product Trends by Month`, series `Shampoo · Perfume · Lipstick`, bars rising. Scene 3.5 is the BOJ US-column comparison. A cosmetics sales chart is the backing plate for a central-bank statistic — same failure as s13, and the heading is large and centred in the band. |
| s27 | ok (watch) | honey jar, lid on — the slot exactly. Carries an embossed `DEUTSCHER IMKERBUND / ECHTER DEUTSCHER HONIG` guild seal, but it is **debossed glass at very low contrast** — I had to push contrast 1.8× to read it. Not a printed consumer brand (the hi cut's `ALMOND BREEZE` was ink on a carton). Kept. |
| s28 | **REJECT** | see below |
| s29 | ok | tree-ring cross-section for the 1961–1986 growth era. Strong, textless. |
| s30 | ok (marginal) | graph paper, but it is a **maths-textbook exponential decay** with axes `−3…3` and a labelled point `(0,−9)` — it falls but never peaks, against the storyboard's ⚠ `must peak then fall`. Direction does **not** contradict the VO ("peaked, then fell"), so it stays; noted as the weakest chart in the cut. |
| s31 | ok (marginal) | a pencil filling in an OMR exam sheet, not the specified academic working paper. Reads "paper + pencil"; no text, no market signal. |

**s28 — REJECT.** Two strikes on one file. (1) `HELIOS` is engraved white-on-black
across the front lens barrel, dead centre of the panel band — a readable brand
mark. (2) The subject is **two camera lenses**; the old photographs are only
scatter beneath them. Scene 3.7 asked for `black and white 1950s tokyo street
archival grain`, and even the retry query asked for the photograph, not the
hardware.

### Batch 6 — s32…s36

| slot | verdict | note |
|---|---|---|
| s32 | ok | cracked grey plaster, flat and even — the calmest bg in the cut, which is what the densest scene needs. Mid-grey, so **no `filter:` override needed**. |
| s32b | ok (weak) | the cut-in is a second wall texture (orange peeling plaster), not the specified savings-campaign poster. Kept rather than dropped: a texture-to-texture `panelSwap` is a soft change but it is not a defect, and dropping it would strand `data-framings="5.66,2.48"`. |
| s33 | ok | RAIL OFF. Genuine Kyoto/Fushimi night street, lanterns, real 黄桜 kanji sign. **AI-fake check passed** — glyphs correctly formed, lighting and perspective coherent. The kanji are a sake maker's name, unreadable as a brand to a US audience and consistent with the storyboard's own "the kanji live in the photograph" stance at s76. |
| s34 | ok (marginal) | matcha chawan on a bamboo tray. Not the kintsugi repair the slot wanted, but a genuine Japanese ceramic bowl for the MOTTAINAI open. (This is the file the orchestrator re-encoded from PNG — verified real JPEG, 1880px.) |
| s35 | ok (watch) | needle + red thread = mending, which is the beat. **Saturated red fills the frame** and red is this video's `--warn` role colour on a scene that carries no role colour — flagged for the grade, not replaced. |
| s36 | **REJECT** | see below |

**s36 — REJECT.** Scene 4.3's whole argument is **ONE** shirt traced back to a
field and a truck. The file is a retail wall of *hundreds* of folded tees — it
argues against the line it sits under. It also carries a readable retail brand,
**`Jennyfer`**, repeated across several stacks, plus `100% COTTON`. Third strike:
at 1280×573 (2.23:1) the panel keeps only ~30% of its width and upscales 1.88×,
so it is the softest file in the cut.

### Batch 7 — s36b…s40

| slot | verdict | note |
|---|---|---|
| s36b | ok (marginal) | misted stubble field at dawn — maize, not cotton, but it reads "a farmer's crop" for a 2.03s cut-in. |
| s36c | ok (measured) | semi truck. Two things checked and both survive the panel crop: the trailer's ad wrap is a blue graphic with **no legible wordmark** even at full res, and the non-US circular metric `90` sign sits at x≈0.845 — **outside the band, never rendered**. |
| s37 | ok (watch) | high-key bokeh alarm clock + teacup. Mood fights a `warn` scene and it is the brightest file in the cut; flagged for grade. Dial reads `QUARTZ` — generic, not a brand. |
| s38 | ok | dense closet, white shirt on a hanger. No price tags as specified; no brand, no text. |
| s39 | ok (marginal) | a printed invoice with **US dollars** — right market — totalling `$8,573.40`, `Tax 8.25%`. It is an invoice rather than the specified card statement, and the figure is larger than the "small recurring charges" beat, but all type is rotated 90° so it does not read as a competing headline. Hands only, no faces, no screen. |
| s40 | **REJECT** | see below |

**s40 — REJECT.** This is the hi cut's `ALMOND BREEZE` defect in an American
fridge. Printed on the punnet: the **Aldi three-chevron logo** plus
`STRAWBERRIES · SWEET & JUICY` in large caps, with `CAESAR SALAD KIT` alongside.
Measured: the logo sits at x≈0.30 and the wordmark spans x≈0.19–0.42, so both are
inside the panel band, and the cap-height renders ~41px on a 1080 frame for the
full 5.5s of scene 4.7. That is a readable brand mark by any reading of the rule.

### Batch 8 — s41…s46
| slot | verdict | note |
|---|---|---|
| s41 | ok (marginal) | stacked boxes printed `THANK YOU COME AGAIN` — a generic phrase, not a brand. |
| s42 | ok (marginal) | hand holding an apple rather than hovering at a shelf; dark, textless, palette-correct. |
| s43 | ok | RAIL OFF. Empty glass on a sill in hard side light — the slot exactly. |
| s44 | ok | cart in a lot. Cropped the handle label: a red/white blur, **no legible store mark**. |
| s45 | ok | worn tall boots beside newer boots on a porch. |
| s46 | ok (marginal) | one katsu-and-rice bowl, not a set meal in small bowls; genuine Japanese food, no text. |

### Batch 9 — s47…s51
| slot | verdict | note |
|---|---|---|
| s47 | ok | elderly couple walking away, faces never visible. |
| s48 | ok | rice bowl + chopsticks top down. High-key white — grade note. |
| s49 | ok (marginal) | a full plated dish rather than chopsticks set down; strongly red-dominant, grade note. |
| s50 | ok | **saved by the panel crop, verified by rendering the band**: the GE fridge badge (x≈0.79), the Keurig (x≈0.90) and the TV (x≈0.13–0.24) all sit outside x∈[0.26,0.74]. What ships is counter, cabinets and sink. |
| s51 | ok | the storyboard's ⚠ prop-money check **run and passed**: two different serials legible in one frame — `MG 78777259 D` and `PE 07500145 G` — with real wear and register. |

### Batch 10 — s52…s58
| slot | verdict | note |
|---|---|---|
| s52 | ok (marginal) | a folded wallet; you cannot actually see that it is empty. |
| s53 | ok | one kraft envelope + note card + glasses. Passes the ⚠ **no bank UI, no account type**. |
| s54 | ok | dusty switch in the on position. European rocker plate on a non-🇺🇸 scene — immaterial. |
| s55 | ok (marginal) | a **US IRS withholding worksheet** (`Married Filing Jointly`, `Head of Household`, `$0–$9,999`…). This was a *defect on the hi cut and is right-market here*; all type is inverted, so it reads as "dense dollar table", which is the slot. |
| s56 | ok | hands counting genuine $20s; the phone in shot is dark and face-down. |
| s57 | ok | US highway, yellow double centre line. Exactly the slot. |
| s58 | ok | shelf of old bound volumes. |

### Batch 11 — s59…s64
| slot | verdict | note |
|---|---|---|
| s59 | ok | writing in a notebook, head cropped out of frame, phone dark. |
| s60 | ok | letterpress type (mirror-reading, as real type is). |
| s61 | ok (marginal) | the uniform spines are `SACRED BOOKS OF THE EAST… BUDDHIST SUTTAS`, legible. Reads as an identical annual series, which is the beat; no brand, no market error. |
| s62 | ok | blank ruled page — the slot exactly. |
| s63 | ok (watch) | correct US quarters (`QUARTER DOLLAR`, `UNITED STATES OF AMERICA`) but a visible **CGI render**, not a photograph — the only synthetic frame among 92. A faint ghost-lettering artefact on the left stack sits at x≈0.02–0.08, outside the band. Kept: right currency, no deception; flagged as a style outlier. |
| s64 | ok | inkwell/globe/wax-seal still life. |

### Batch 12 — s65…s73  ·  Batch 13 — s74…s85  ·  Batch 14 — s86…s92
| slot | verdict | note |
|---|---|---|
| s65 | **REJECT** | see below |
| s67 | ok (marginal) | blank spiral page, no printed date header; very high-key. |
| s68 | ok (marginal) | the four handwritten lines are **Spanish** cursive, rotated 90°. Not a product name, not a currency; unreadable at speed. |
| s69 | ok (marginal) | numbered handwritten list. Faintly legible study notes (`Paul`, `John Mark`, `High School Chapel`) — no brand, no claim. |
| s70 | ok (marginal) | notebook + pen in a café; the background tablet screen is blurred and blank. No face-down phone as specified. |
| s71 | **REJECT** | see below |
| s72 | **REJECT** | see below |
| s73 | ok (marginal) | a shopper with bags, back to camera, no face — not the specified card terminal. Weakest match in the cut, but no defect class: no brand, no currency, no identifiable person. |
| s74 | ok | genuine Kyoto-style mossy stone path. |
| s75 | ok (flag) | a genuine karesansui — but it is **Kongobu-ji (Koyasan), not Ryoan-ji**, while the rail beat reads `RYOAN-JI`. Photographically sound; flagged as a factual-precision note for audit, not an image defect. |
| s76 | **REJECT** | see below |
| s77 | ok | RAIL OFF. Bamboo spout + square-mouthed stone basin — the slot exactly, genuine, dark enough for type. |
| s79 | ok (marginal) | US open-plan kitchen; no diploma or keys as specified. |
| s79b | ok (marginal) | modern apartment façade, no car — carries "the apartment" half of the swap. |
| s80 | ok | motorsport finish line on asphalt. |
| s81 | ok (marginal) | a rack of jackets rather than two near-identical ones. |
| s82 | ok | rain-night bokeh; **no legible billboard brand**, which was this slot's ⚠. |
| s83 | ok (marginal) | chairs by windows, very high-key. |
| s84 | ok (marginal) | Japanese maple in autumn colour, not a rock garden. Momiji is a permanent Japanese motif, **not** a holiday marker, so it is not the seasonal-giveaway class; it is a bright tonal outlier. |
| s85 | **REJECT** | see below |
| s86 | ok | genuine $20s, **multiple distinct serials** (`MC 05930777 F`, `MB 77999924 K`, `MF 91850626 E`) — prop-money check passed, and visibly a different framing from s51 as the ⚠ requires. |
| s87 | ok | handwritten ledger under a magnifier — the slot exactly, no currency symbol. |
| s88 | ok | genuine chōzuya, framing distinct from s76/s77 as required. |
| s89 | ok (marginal) | the laptop in shot has an **ISO/European keyboard** (`Alt Gr`, `€`) — but it sits at x<0.38 and the band shows only wood, notebook and pen. |
| s90 | ok | RAIL OFF. `Today` + `1) 2) 3) 4)` handwritten — the four-questions CTA, in English, perfectly on-beat. Bright (lum 167) under light type; grade note. |
| s91 | ok (marginal) | leather notebook, no pen; a four-leaf-clover charm sits oddly on a "method, not luck" thesis. |
| s92 | ok (marginal) | one chalk-labelled `coffee` mug indoors, not two on a porch rail. Dark, no brand. |

---

## The five rejects found only at full resolution (batches 12–14)

**s65 — REJECT (the §12 placeholder).** RAIL OFF, full-bleed, **14.217s** across 6.7+6.8
— the longest exposure any single file gets in this cut. What was there: money scattered
on a **near-white** surface (mean luminance **206**, by far the brightest of the seven
RAIL OFF frames, under light type) with a Himalayan-salt lamp prop, no four groups and
**no handwritten labels at all** — which also leaves scene 6.8's specified framing
("tighter crop on one handwritten label") with nothing to crop to.

**s71 — REJECT.** Scene 6.13 is `APP vs LEDGER` 🇺🇸. The page carried **`Apple 74% NPS`
in handwriting**, plus `Development Strategy 2020`, `KPI`, `CSI 90%` and a printed
`SCIENTIFIC RESEARCH: ITALY CALLS EUROPE` chart. Rendering the band confirmed `Apple`
is legible inside it. This is the hi cut's handwritten-`facebook` defect, on the one
frame in the video where a tech brand name is most loaded.

**s72 — REJECT.** A 1930s museum garage. Band render kept `LUCAS`, `ENERGOL` and
`Castrol S` legible (SHELL and `Pratts` fell outside). Multiple live automotive brand
marks, and it does not read as the modern repair bill that scene 6.14's `$400` needs.

**s76 — REJECT.** Scene 7.3 `WHAT IT SAYS` is the tsukubai beat and the storyboard
requires **the kanji to live in the photograph**. The file had no carved characters at
all and instead floated **flowers and small orange pumpkins** in the basin — a seasonal
autumn/Halloween prop, the giveaway class the brief names.

**s85 — REJECT.** `RECAP ONE` asks for a shelf **with a gap**. The shelf was completely
full, wall-to-wall, and every can carried a legible product wordmark (`Tender Feasts`,
`OLD FA… WHOOP…`). No gap, dozens of labels.

---

## Replacements — 17 fetches for 12 slots, and what the full-res read caught in them

Sheets were built from a side manifest (`manifest-fix3*.json`, since deleted) so the
cut's real `manifest.json` was never a fetch target. **Every promoted candidate was read
at full resolution before acceptance**, and that read rejected five *replacements*:

| slot | what the contact sheet hid | fix |
|---|---|---|
| s6 (1st) | Pexels' receipt pool is one Polish photographer's set: `PARAGON FISKALNY`, `NIP 527-010-33-85`, **`IKEA RETAIL SP. Z O.O.`** — wrong-market fiscal receipt *and* a brand | re-pick |
| s6 (2nd) | same set again; the `PARAGON FISKALNY` slip sat at x 0.775–1.0, only ~2.3% outside the band. **Refused to ship a defect that is merely cropped out** | Pixabay retry (0/6 receipts), then a subject change |
| s36 (1st) | a tuxedo jacket + dress shirt = a wedding shoot, not the plain cotton shirt scene 4.3 traces to a field and a truck; hanger tags legible | re-pick |
| s40 (1st) | showroom-empty fridge, against a beat about food you already bought and forgot; `ATLANT` badge in band | re-pick |
| s65 (1st) | **four gold BITCOIN coins** — from a query that never mentions crypto, on the RAIL OFF hero. This is precisely the rule-3 trap and the sameness the brief flags (props refused elsewhere then accepted on a hook) | denomination-named retry |
| s72 (1st) | a fully identifiable mechanic's face centred in the band under a `warn` money claim | re-pick to an object-led frame |
| s85 (1st) | `$` prices read as US at sheet size; at full res the aisle is **`coles`** (twice), `Barilla`, `SAN REMO` — Australian, multi-brand | two retries |

**Final 12, all 1880 px, all read at full resolution:**

| slot | replacement | why it clears |
|---|---|---|
| s1 | dark modern kitchen, marble counter, no people | RAIL OFF hero: lum 22→**75**, still dark for light type; matches the `dark kitchen counter at night` keyword; no text, no faces, no minor |
| s6 | blank sheet + pen + three crumpled paper balls, dark wood, top down | zero text, zero brand, zero currency; reads "a lot of small paper" for `NOTHING BIG` |
| s13 | US financial statement, `LIABILITIES AND NET ASSETS`, one total circled in red | dense dollar figures + a circled number under the `37.8%` hero; no marketing headline |
| s26 | stacked column chart, `100%…−60%` axis, series `Out01–Out05` | a percentage column chart with **no** misleading label, for the BOJ next-column beat |
| s28 | grainy B&W street, hatted silhouette | archival read, no legible text, no faces, lum 73 |
| s36 | plain white/cream tees on wooden hangers | reads "a plain cotton shirt", no wordmark anywhere |
| s40 | person (back only) at an open fridge with real contents | the *action* the CHECK THREE beat asks for; the one dark container's label magnifies to an illegible white blur — verified at 7.5× |
| s65 | US **$5 / $20 / $50 laid out in three denomination groups**, top down | the only cell in two sheets that is genuinely *sorted*; serials checked at high magnification — the one fully legible serial (`ML 62814485 L`) repeats only in its own note's two printed positions, and the neighbouring `ML 6281…` prefix is normal sequential banding, not reproduction |
| s71 | open notebook + printed sheet + ruler on a wooden table | structurally the slot (printed page beside a written one); no brand, no currency |
| s72 | car underbody filling the frame, mechanic small and lower-right | object-led, no signage, modern workshop |
| s76 | bronze dragon chōzuya, bamboo ladles | genuine, no seasonal props, and **kanji are burned into the ladles inside the band** — partially restoring the storyboard's "kanji live in the photograph" |
| s85 | empty wooden shelving room | the retry ladder's last rung: a quiet image that still reads the keyword. Nothing on the shelves is the gap |

## Bookkeeping

- **md5 across every project: 0 duplicates.** Two first-round picks collided with the hi
  cut (`s26`↔hi `s25`, `s76`↔hi `s75`) and were resolved by **re-picking a different
  cell from the sheet already on disk — no extra fetch**.
- `CREDITS.txt` **deduplicated to exactly 93 lines**, one per file. The fetcher appends,
  so re-picks had left 134 lines with stale entries (15 of the duplicate slots predate
  this attempt). Kept the last line per slot — verified last-wins is correct by
  spot-checking s34 (matcha bowl) and s10 (wooden table) against the files on disk.
- `manifest.json` re-synced to the `.src` sidecars: 93 entries, 12 queries updated.
- Temp fix-manifests deleted. `_cand/` sheets left in place (throwaway, not shipped).
- `pipeline_check check assets --slug japanese-money-methods --cut en` → **PASS**.

## Handoffs (not defects — decisions the next stage owns)

1. **s65 still owes the creator a made photograph.** Storyboard §12.1 requires four
   groups with four handwritten labels (`NEEDS · WANTS · CULTURE · UNEXPECTED`) and says
   escalate rather than substitute. Two sheets (12 cells) produced no four-group cell;
   the promoted file has three denomination groups and no labels. Consequences: mean
   luminance is **212**, the brightest RAIL OFF frame, and **scene 6.8's specified
   "tighter crop on one handwritten label" has no label to land on** — fin-build needs
   either the real photograph or a different second framing for 6.8.
2. **Grade, not replacement.** Brightest files, all RAIL ON: s67 (232), s18 (226), s37
   (212), s71, s48, s83. s35 and s49 are red-dominant on scenes carrying no role colour,
   and red is this video's `--warn` token. No near-black texture needs a `filter:`
   override, so the one permitted override is unspent.
3. **s75 is Kongobu-ji, not Ryoan-ji**, under a rail beat reading `RYOAN-JI`.
4. **s63 is a CGI render** among 92 photographs — correct currency, but the only
   synthetic frame.
