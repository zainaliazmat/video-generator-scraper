# editor · japanese-money-methods · en · chapter 8 · attempt 2

VERDICT: REWORK

Brief: -hi-parity image + drawn-art audit of the closing chapter (s85–s92).
Compared cell-by-cell against `studio/videos/japanese-money-methods-hi-ch8/`
(`chapter.json` design intent + `renders/CD-ch8.mp4`). Sheet rebuilt at
`studio/videos/japanese-money-methods-en-ch8/renders/SHEET.jpg`; every judgement
below is from frames pulled out of the encoded `renders/CD-ch8.mp4`, not the browser.

## Parity map

| scene | line | -hi picture | -en picture | parity |
|---|---|---|---|---|
| s85 | MOTTAINAI — ask before buying | stocked shop shelf, jars + price tags; fork with a red X on the "no" branch | **empty walk-in closet**, no goods, no store; fork drawn but the X is off-frame | **FAIL ×2** |
| s86 | HARA HACHI BU — live on eight | ₹ notes + 10 cells, 2 leaving | $20 bills + 10 cells, 2 leaving | OK (currency correctly localised) |
| s87 | KAKEIBO — four questions | handwritten ledger page + 4 rows, row 2 lit | old accounting ledger **under a magnifying glass** + 4 rows, row 2 lit | art at parity, photo drifts |
| s88 | TARU WO SHIRU — what is enough | market stall + 4-square figure | temple chōzuya basin + ladles + 4-square figure | **-en is better than -hi** — keep |
| s89 | One page. One pen. | latte + notebook + pen | notebook + pen + cup under a lamp, page blank | OK |
| s90 | information vs understanding | hand writing in a notebook, kicker THE WHOLE VIDEO | list page "Today / 2) / 3)", **kicker missing** | photo OK, kicker FAIL |
| s91 | SUBSCRIBE / comment | closed white notebook + capped pen | **eyeglasses** on a closed notebook, no pen | weaker |
| s92 | send it to the friend | several glasses, shared table | **one mug** + moka pot on a kitchen counter | **FAIL — contradicts** |

Drawn-art parity: -hi ch8 carries no Lottie and no measure bar (`chapter.json`
has neither), so there is no missing-Lottie gap to close. All four recap SVGs
(fork, ten cells, four rows, shared square) are present in -en. Only s85's is
mis-positioned — see finding 2. `art-off` on s89–s92 is correct in both cuts and
matches archetype rule 8: those four frames are already the picture.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s85 | blocker | `assets/img/s85.jpg` is an **empty wooden walk-in closet** — no shop, no goods, no shopper, no hand | The script cue is "the store shelf from 4.9, hand withdrawn" and the line is "ask before buying, not after". Sound-off with the type stripped this frame says *empty wardrobe*; there is nothing in it to decide about, so the fork drawn over it has no subject. The -hi cut opens the recap on a shelf packed with jars — you can see the thing you might buy. This is the first frame of the payoff chapter. | `reuse hi:studio/videos/japanese-money-methods-hi-ch8/assets/img/s85.jpg` — a stocked tea-shop shelf, English labels, one Japanese tin; no Indian currency, signage or subject, so it is clean for the US cut, and 8.1 is **not** on the must-be-American list in script-en handoff §7. Fallback: `source new: a stocked US retail shelf, one product held or a hand withdrawing from the shelf, no faces.` |
| 2 | s85 | blocker | the fork art is **drawn off the right edge of the frame** — the accept branch is cut and the **X never appears at all** | `.p-b` is `left:1120px; width:860px` on a 1920 frame, so viewBox x maps 1:1 to screen x and anything past vx=800 is outside the frame. -en has `#s85-yes` running to x=1032 and the X at x=846–932 → screen 1966–2052, entirely off-canvas. -hi puts the same figure at 372→780 with the X at 596–700 and it reads fully. The X *is* the point of this frame — the purchase refused — and in the -en cut it does not exist on screen. This is the one thing in the chapter drawn art has to assert. | Re-lay the s85 SVG on the -hi coordinates from `japanese-money-methods-hi-ch8/chapter.json` → stem `60,292 → 360,300`, node at 352, `s85-yes` `M 372 296 L 500 208 L 780 208`, `s85-no` `M 372 296 L 500 392 L 780 392`, X `M 596 344 L 700 440` / `M 700 344 L 596 440`. Keep the -en stroke weights and the existing draw cues (1.9 / 2.2 / 2.65 / 2.8). |
| 3 | s92 | blocker | `assets/img/s92.jpg` is **one mug** and a moka pot on an indoor kitchen counter | The line is "send this to **the friend** who says every month: I have no idea where it goes", and the composition comment in `index.html` already claims "Two mugs on a porch rail". One cup on a counter reads *alone* — it argues against the only instruction the frame carries, and it is the last frame of the whole video, the one the end-screen sits on. -hi closes on a shared table with several glasses, which is why that beat lands. | `source new: two coffee mugs side by side on a US porch rail or a stoop at night, both used, no people, no faces` — exactly the 8.8 cue. 8.8 **is** on the must-be-American list (handoff §7), so do **not** reuse the -hi izakaya frame. |
| 4 | s91 | should-fix | CTA frame is a pair of **eyeglasses** on a closed notebook; the cue asks for "a closed notebook and a capped pen, finished" | The pen is the through-line of the whole chapter — s89 "one pen", s90 the written page, s91 the pen put down. Swapping it for glasses breaks that three-frame sentence and reads as "stopped reading" rather than "finished the job". The type is unaffected (SUBSCRIBE + the comment line both render correctly at 44.5s), so this is weak, not false. | `reuse hi:studio/videos/japanese-money-methods-hi-ch8/assets/img/s91.jpg` — closed white notebook, capped fountain pen, wood table. Market-neutral, no localisation risk, and it closes the pen arc. |
| 5 | s90 | should-fix | the `THE WHOLE VIDEO` kicker is **absent** from -en; the `index.html` comment says "No kicker on this scene, verbatim" | script-en 8.6 cue reads `[RAIL OFF \| img: … \| head: THE WHOLE VIDEO \| stmt: …]` — the head is specified, and -hi renders it. `RAIL OFF` kills the ledger rail, not the kicker. Without it this frame loses the "here is the thesis of the last eleven minutes" signal and reads as one more notebook shot. | Add `<p class="kicker" id="s90-head">THE WHOLE VIDEO</p>` above `#s90-stmt` and a matching `rise("#s90-head", 33.69, 0.50, 24)` with `#s90-stmt` pushed to 34.49 so the ladder keeps its 0.8s gap. |
| 6 | s87 | note | the ledger photo is an old **accounting** page seen through a **magnifying glass** | The magnifier says *audit / scrutinise the past*; the line says *write four questions at the start of the month*. It does not contradict the line and the drawn four-row figure carries the real assertion, so it is survivable — but -hi's plain handwritten page is the cleaner read and this one is also a decade-old bookkeeping ledger rather than a household budget. | Optional: `source new: a US household budget page part-filled in ballpoint, four handwritten category lines, no magnifier`. Leave as-is if the fix pass is tight — the art carries it. |
| 7 | s89 / s90 | note | both cells are a spiral notebook on a dark surface and read alike on the sheet | Normally a repeat finding, but script-en 8.6 explicitly asks for "**the same table**, the page now carrying four handwritten lines" — the pairing is the intent and the blank-page → written-page change does read. No action. | none |

## What is working

- **s88 is the best frame in the chapter and beats its -hi counterpart** — the temple chōzuya
  basin with the ladles is exactly the "still basin from 7.3" the cue asks for, the amber
  four-square tsukubai figure sits fully inside the plate, and the amber-against-green break
  marks it as the one that governs the other three. Do not touch the photo or the art.
- **s86 is correctly localised**: US $20 bills under "live on eight", with the ten cells and
  the same two dropping out that the viewer saw in chapter 5. Currency, geometry and the
  recall of the earlier device are all right.
- **s89 and s90 are the American action frames the handoff §7 demands** — lamp-lit table,
  blank page then four written lines, no non-US signal anywhere. s90's "Today / 2) / 3)"
  page is arguably stronger than -hi's.
- Cue ladder is clean: first cue at 0.3s, 0.8s head→stmt gaps throughout, s92 carries a bare
  `data-duration` as the chapter's last scene, and the s91 `foot` line does render in the
  encoded file.
