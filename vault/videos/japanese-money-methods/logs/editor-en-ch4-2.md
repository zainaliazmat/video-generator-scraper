# editor · japanese-money-methods · en · chapter 4 · attempt 2

VERDICT: REWORK

Scope: **-hi-parity image + drawn-art audit.** Sheet built at
`studio/videos/japanese-money-methods-en-ch4/renders/SHEET.jpg`, read against
`studio/videos/japanese-money-methods-hi-ch4/renders/SHEET-ch4.jpg`, both
index.html files diffed scene by scene, and the -en frames sampled from
`renders/CD-ch4.mp4`.

## Drawn-art parity — CLEAN

The -en composition is a faithful structural port of -hi. Verified present and
firing in the encoded -en mp4:

- **s38/s39/s40** — `.measure` + `.measure-lab under` "THE THREE CHECKS", the
  three-scene bar held across the cut, `span()` at 0→.3333→.6667→1. Identical
  to -hi.
- **s43** — the decision-branch SVG (one path in, two out, MAYBE struck
  through), `art-forward`, band at 52%.
- **s44** — the four tally strokes, fourth at opacity .38, `art-forward art-lift`.
- Neither cut uses a Lottie in ch4 (both are inline SVG), so there is no -hi
  Lottie to port. **No blocker under item 2 of the brief.**

Every blocker below is a **photograph**, not a missing drawn layer.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s36 | blocker | Chain plays **shirt-rack → cotton field → truck** against the line "A farmer's crop. A mill's hours. A truck's diesel." Framings 2.74/2.03/3.031 put the shirt rack on "farmer's crop" and the field on "mill's hours". | Every picture in the chain lands on the wrong phrase, and the chain is the entire point of the scene. -hi got the order right (field → loom → truck under crop → weaver's hands → truck). Also: the -en cut has **no mill image at all** — no loom, no factory floor — so the middle link of the chain is unillustrated. Script 4.3 specifies "a cotton field at dawn, wide" as the scene's opening image. | Reorder + refill the three slots: `s36.jpg` = cotton field (the current `s36b.jpg` already is one — promote it); `s36b.jpg` = **source new: interior of a US textile mill, spinning frames or a loom in motion, no faces**; `s36c.jpg` = keep the semi truck. Retire the shirt-rack file entirely (see #2). |
| 2 | s36 / s38 | blocker | The same subject — **white shirts on hangers in a closet** — is the background of two scenes in one chapter, 13 seconds apart. On the sheet the two cells read as one photograph. | One image per point. The sameness is invisible per-scene and unmissable on the grid; this is the exact defect this checkpoint exists for. -hi has no such collision (cotton field vs clothes rail). | Resolved by #1 — the shirt rack leaves s36. s38's closet stays; it is the correct picture for "count the clothes still wearing their tags", though it needs the tags to actually read (see #9). |
| 3 | s39 | blocker | Line reads **"The subscriptions screen. All of it."** The picture is a hand pointing at a **printed paper form** (reads as a bank deposit slip). | The subject NAMED in the line — a screen — is absent. Paper contradicts it. This is a -en-only regression: -hi's copy says "list" and -hi shows a printed number grid, so -hi is self-consistent; -en changed the copy to "screen" and kept a paper photograph. Script 4.6 explicitly specifies "a phone's subscriptions settings list on a table, screen text illegible, hand only". | `source new:` a phone held or on a table showing a **recurring-payments / subscriptions settings list**, US app-store or bank-app style, rows of $ amounts, **text illegible at frame scale** — no fabricated brand names or legible figures. Do **not** reuse `hi/s39.jpg`; that number grid is paper too. |
| 4 | s45 | blocker | Line: "Not spending less. Using fully what was bought." Picture: a decorative rustic still-life — **two pairs of cowboy boots and three brass vessels** against barn wood. | Sound-off, this cell says "antique shop window". Nothing in it is worn-and-still-serving, nothing is new-in-box, and the brass jugs are pure noise. Script 4.12 specifies "a worn, resoled leather boot beside a new one still in its box" — neither element is present. -hi delivers one worn work boot, clean and legible. | `reuse hi:studio/videos/japanese-money-methods-hi-ch4/assets/img/s45.jpg` (a single worn leather work boot — market-neutral, US-readable), or `source new:` a resoled boot beside a boxed new pair, one light, no props. |
| 5 | s34 | should-fix | Chapter-opening frame — the video's hinge. Line: "A thing's real value, going unused." Picture: an **intact matcha bowl with a sweet on a tray**. | It says "Japanese tea ceremony", not "value going unused". The repair — the whole idea, and what script 4.1 asked for ("a chipped ceramic bowl repaired with visible seams") — is absent. Supporting: it is the chapter's second bowl-of-Japanese-food cell alongside s46, so the chapter opens and closes on near-identical shapes. -hi at least shows hands making a vessel (labour embodied). | `source new:` **kintsugi** — a ceramic bowl with visible gold repair seams, close, on wood. This is the one image in the chapter that carries the method's whole argument; it is worth a dedicated fetch. |
| 6 | s37 | should-fix | Line: "The hours of your own pay that bought it." Picture: a **pastel alarm clock beside a coffee cup** in high-key bokeh. | Says "good morning routine", not "hours of your working life traded". It is also the only bright cream frame in a scene the design grades red-hot (`--f1:#2f1215`, warn tint) — on the sheet the red intent is nowhere. Script 4.4 asked for "a wall clock in an office corridor, evening". | `reuse hi:studio/videos/japanese-money-methods-hi-ch4/assets/img/s37.jpg` (institutional hall clock, dark, no market markers), or `source new:` a wall clock in an empty office corridor at dusk. |
| 7 | s40 | should-fix | Line: "What gets thrown out next week." Picture: a **blonde woman shot from behind at a bright, near-empty white fridge**. | The person is the subject, not the food; the shelves read clean and stocked, so nothing in frame is on its way to the bin. It is also the only human-figure-led cell in an otherwise entirely object-led chapter, which breaks the chapter's visual language on the third of three checks. Script 4.7 asked for "an open refrigerator shelf, takeout containers and wilting greens". | `source new:` close on a fridge shelf — takeout containers, wilting greens, a half-used bunch of herbs. No person in frame. |
| 8 | s42 | should-fix | Line: "And it is asked before, not after." Picture: a **hand holding an apple** against black. | The moment the line describes is the moment *before a purchase*. An apple in a hand has no shop, no shelf, no price, no decision. Script 4.9 asked for "a hand hovering over a store shelf, not yet touching". Secondary: putting food here pre-empts the s46 hand-off to the dinner table. | `source new:` a hand hovering over a boxed product on a US retail shelf, price label visible but not legible, hand only. |
| 9 | s38 | should-fix | The closet is right, but at frame scale **no price tag is legible** — the shirt reads as an ordinary hanging shirt. | The line is an instruction to *count tags*; the check the viewer is asked to perform is not visible. -hi has the same weakness, so this is not a parity gap, but it is the scene's one job. | `source new:` tighter — two or three garments with white price tags clearly hanging, US closet. If a re-fetch is not worth it, tighten the ken framing onto the tag. |
| 10 | s44 | should-fix | Line: "The question comes up three or four times a month", kicker "ON $4,000". Picture: an **empty shopping cart dumped in a car park** on weeds. | Reads "abandoned / derelict", the opposite of a live purchase decision, and it is outdoors — script 4.11 asked for a cart "abandoned mid-aisle in a **US grocery store**". The cart's wire lattice also runs straight through the type block, hurting readability of the 3-line stmt (see the 70.0s frame). | `source new:` a half-full cart standing in a US supermarket aisle, or a checkout counter mid-transaction. Keep the tally plate on the right — it is working. |
| 11 | s43 | should-fix | -en drops the `THE QUESTION` kicker that -hi carries, and sets the stmt at **88px** where -hi uses 76px. The result is three lines of type jammed against the top edge, the last line "NO." sitting on the `brule`. | Type collision + a parity regression on the chapter's one piece of drawn argument. -hi's kicker+76px reads in two clean lines above the rule. | Add `<p class="kicker" id="s43-head">THE QUESTION</p>` and set `font-size:76px`, matching -hi. |
| 12 | s35 | note | Line: "It is regret. Not instruction." Picture: a **saturated red thread spool with a needle**. | Legible as sewing, but the scene is designed as the chapter's coolest frame (`--f1:#171b21`) and the photo is the hottest thing in the opening — on the sheet s35 renders deep maroon. No mend is actually visible; it is a spool, not a repair. | `reuse hi:studio/videos/japanese-money-methods-hi-ch4/assets/img/s35.jpg` (denim with a visible hand-stitched seam — market-neutral, and it shows the mend). |
| 13 | s41 | note | Boxes read as **flat, empty, unsealed cardboard trays** stacked in a bright room, not as unopened deliveries. | Weakens "value already bought and never used" — nothing in frame was ever bought. Not false, so not a blocker. | `source new:` sealed corrugated boxes with shipping labels and tape, stacked in a room corner, if a re-fetch is cheap. Otherwise leave. |
| 14 | all | note | `data-framings` is declared on **s36 only** in -en; -hi declares it on all 13 scenes. | No viewer-visible defect (twelve scenes are single-framing), but the -en composition no longer states its framing contract, so a future ken change cannot be checked against it. | Regenerate from `chapter.json` so the attribute is emitted per scene, matching -hi. |

## Measure-label / track collision — CSS fix CONFIRMED LANDED

Reported separately as asked, **not** a blocker.

- The `.measure-lab` / `.measure` overlap **is still visible in the -en
  `renders/CD-ch4.mp4`** — at 30.6s the green fill runs straight through the
  middle of "THE THREE CHECKS" (all three of s38/s39/s40).
- That render is **stale**, not broken. Encode timestamps:
  - `en-ch4/renders/CD-ch4.mp4` — 2026-08-05 09:05:07
  - `tools/scaffold/assets/chapter-design.css` (the `margin:0; line-height:1` fix) — 2026-08-06 00:06:39
  - `hi-ch4/renders/CD-ch4.mp4` — 2026-08-06 00:11:15
- The -hi mp4 is the only one encoded *after* the fix, and at 44.5s its label
  sits cleanly above its track with a full gap. **The fix landed.** The -en
  collision clears on the next encode; no further work needed.

## What is working

- **Drawn-art parity is complete.** The three-scene measure bar, the s43
  decision branch and the s44 tally are all present in -en and all fire
  correctly in the encoded file. Do not touch the s44 plate or the s38–s40 bar
  timing in the fix pass.
- The archetype ladder (A A D A B B B A A D B A A), the ground-colour arc, the
  cue ladder (+0.30 / +1.10 / +1.90, broken exactly once by the carried bar) and
  the bare last-scene duration on s46 are all correct and match -hi.
- s41, s46 and the s38 closet are the right *ideas* for their lines; the fixes
  above are about which frame, not which concept.
