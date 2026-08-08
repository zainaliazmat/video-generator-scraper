# editor · japanese-money-methods · en · chapter 5 · attempt 2
VERDICT: REWORK

Scope: -hi-parity image + drawn-art audit. Sheets rebuilt for both cuts
(`renders/SHEET.jpg`), frames sampled from `renders/CD-ch5.mp4` (en).

## Beat map (the two cuts are NOT 1:1)
| en | line | hi | note |
|----|------|----|------|
| s47–s52 | 5.1–5.6 | s47–s52 | same beats, same order |
| s53 | 5.7 automate / separate account | — | **en-only beat**, no hi counterpart |
| s54 | 5.8 not discipline | s54 | same |
| s55 | 5.9 · 62.2% | s53 | hi carries it 2 slots earlier |
| s56 | 5.10 · $200 (5%) | s55 · ₹1,500 | same beat, different figure |
| — | — | s56 · ₹500 SIP entry ticket | **hi-only beat** (AMFI); correctly absent in en |
| s57, s58 | 5.11, 5.12 | s57, s58 | same |

Art parity that IS already met: the three-scene B hold (ten cells → eight lit →
last two lit + bracket → last two leave) is wired identically in en s48/s49/s50,
and the s51 measure bar fills 0→0.20 to match. No parity gap in the diagram
itself — the gap is in the photographs underneath it and in two en-only holes.

## Findings
| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s50 | blocker | "Now the paycheck · Live on eight parts, move two out on day one" sits on a wide real-estate listing shot of an empty American kitchen/living room (`american kitchen counter@pexels`) | Sound-off it says "house for sale". No money, no paycheck, no food. It also breaks the three-scene hold: s48 and s49 are food, so the one scene that transfers the food rule ONTO money shows neither. hi keeps the hold (greens bowl → bowl → thali) and its ground reads clean; the green tint over this bright interior is the worst grade in the chapter. | `source new:` tight top-down US kitchen counter, dark laminate or wood, a small stack of $20s and a folded paycheck stub pushed to one side, half the frame empty right for the ten-cell art. Do NOT reuse hi:s50 (Indian thali). |
| 2 | s52 | blocker | "What is left at month end is always zero" on a CLOSED, zipped yellow purse — a product shot | A shut wallet cannot say empty. Sound-off it is a handbag advert. The script asked for a wallet "lying open"; hi has exactly that. | `reuse hi:studio/videos/japanese-money-methods-hi-ch5/assets/img/s52.jpg` — hands holding an open, visibly empty leather wallet. No currency in frame, so it is market-neutral. |
| 3 | s55 | blocker | 62.2% cited to "Statistics Bureau FIES 2024, Table I-2-2" sits on a photo of two people marking a printed table of numbers **in red pen** (`printed table of numbers on paper@pexels#6`) | A generic marked-up tally sheet stands in for a named government table, with semi-legible figures and correction marks on it. That is the invented-source-document failure (`format.json` → `truth_bar`), and it reads as somebody editing the numbers. hi deliberately refuses a document here. | `reuse hi:studio/videos/japanese-money-methods-hi-ch5/assets/img/s53.jpg` — Japanese apartment block, lit windows at dusk = salaried households. Correct in the -en cut too: the figure is Japan's, not America's. |
| 4 | s56 | blocker | "IF 20% IS TOO MUCH · $200 · 5% of the $4,000 worked example" sits on hands counting a thick wad of $20s | The picture argues the opposite of its line: the line is *start smaller*, the image is abundance. It also contradicts the shipped intent — `s56.jpg.src` says "one twenty dollar bill on a wooden table" and the file on disk is not that. hi shows a bowl of small coins, which points the right way. | `source new:` a single $20 bill lying beside a much thicker folded stack, top-down, plain table — the contrast IS the point. hi:s55 is Indian coins, not reusable in the US cut. |
| 5 | s53 | blocker | en-only beat 5.7 ("automate it so it moves without a decision, into an account separate from the one the card and the bills touch") is a stationery flat-lay: notebooks, glasses, a plant, a hand writing on a card | Two subjects are NAMED and neither is present: no automation, no second account. Sound-off it says "someone writing a thank-you note". It is also the palest frame in the chapter and sits flat against the grade. | `source new:` a screen showing a scheduled recurring transfer — repeat-monthly UI, amounts illegible, no brand mark or product name (the AUDIT note forbids naming a bank/app/category). |
| 6 | s53 | blocker | 5.7 is a PROCESS beat carried on a flat photo, with no drawn art | `format.json` → `reach_for_it_when`: a process is a FAIL as a flat photo, not a missed opportunity. This is en-only, so no hi parity covers it. Chapter is at 0 Lotties against a cap of 4. | `add art:` inline SVG in the same idiom as s48–s50 (art-forward, art-lift, fund role) — two separated containers, one arrow leaving the left and landing in the right, the arrow repeating a second time to say *every month*. Asserts separation + recurrence, which the photo cannot. Not a duplicate of the ten cells. |
| 7 | s55, s56 | should-fix | both figures render at `.huge`; hi renders both at `class="mega" font-size:240px`, and hi count-ups ₹1,500 | In a `centred` B scene the number IS the scene. At `.huge` 62.2% and $200 read as headlines, not as the subject. hi's s56 hole is also filled by the countUp; en s56 has a 3.6s dead gap between foot (67.03) and num (70.60). | Copy the hi treatment: `mega` + 240px on `#s55-num` / `#s56-num`, and `countUp("#s56-num", …, 0, 200, "en-US", 1.2, "$")` moved earlier into the gap. |
| 8 | s48 | should-fix | brim-full bowl of white rice isolated on a pure-white studio background | Under "EIGHT PARTS IN TEN · Stop there" the bowl is *full*, which is the state the line rejects; and the white cyc is the only blown-out frame in a chapter of dark grades — the unlit cells of the diagram disappear into it. hi uses a partly-filled bowl on dark metal and the cells read. | `reuse hi:.../hi-ch5/assets/img/s48.jpg` — copy is identical ("Stop there."), so the reuse is exact. |
| 9 | s49 | should-fix | bright red restaurant plate of noodles and shrimp under the cool ground (#171d26) | The red plate fights the cool ground and puts a hot orange blob directly under the ten-cell art; "the last two parts are surplus" wants restraint, not a full plate. hi's steaming bowl holds the run and the grade. | `reuse hi:.../hi-ch5/assets/img/s49.jpg` — copy identical. |
| 10 | s57 | should-fix | daytime desert highway, bright blue sky and white clouds, under the chapter's hottest red and its most sober line | The red tint over blue sky renders muddy purple, and a cheerful sky argues against "this fails in month one, and that is not your fault". hi's night road under stars carries it. | `reuse hi:.../hi-ch5/assets/img/s57.jpg` — an empty road at night, no signage, market-neutral. |
| 11 | s58 | should-fix | a shelf of ornate gilded library books | The line hands off to *accounting*; a decorative library says "old books", not ledger. hi shows a stack of worn bound ledgers. | `reuse hi:.../hi-ch5/assets/img/s58.jpg`. |
| 12 | s47 | note | English hedgerow lane, elderly couple | Reads "old couple, old habit", which is enough; but it is visibly not a coast and not Okinawa. hi is no better. Leave unless a cheap coastal path shows up. | — |
| 13 | s51 | note | an even fan of identical $20s under "$800 out · $3,200 to live on" | The split is asserted only by the measure bar; the photo shows one undifferentiated pile. Same weakness in hi, so not a parity gap. | optional `source new:` two unequal squared stacks, as the script asked. |

## Separately: `.measure-lab` overlap (not counted above)
**Still visible in this mp4.** At 31.0s and 33.5s "MOVED OUT ON DAY ONE" is struck
through by its own track — the bar crosses the word MOVED. But `CD-ch5.mp4` was
encoded 08-05 08:34 and the fix in `tools/scaffold/assets/chapter-design.css`
(`.measure-lab { margin: 0; line-height: 1 }`, with the load-bearing comment)
landed 08-06 00:06. The chapter dir symlinks that file, so the fix is wired but
has never been rendered. It will be proven by the next encode, not by this one.

## What is working
- The three-scene B hold is intact and reads: ten cells → eight lit → last two lit + bracket → last two leave the row, with s51 restating the same 0.20 as one length. Do not touch the diagram or the measure fill.
- Cue ladder is clean throughout: first cue at 0.3s, no gap under 0.8s except the deliberate art beats inside s49, and s58 carries a bare 7.67s duration.
- s54 (dusty switch in the ON position) is the one image in this chapter that is already at hi parity — it says "one decision" with the sound off. Keep it.
- s55/s56 are correctly `centred` — no empty half in either B split.
