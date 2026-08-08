# editor · japanese-money-methods · en · chapter 7 · attempt 2
VERDICT: REWORK

Scope: -hi-parity image + drawn-art audit. Beats mapped by VO line, not scene id
(-en s74–s84 = 11 lines; -hi s73–s84 = 12; hi 7.11 "WHY IT MATTERS" has no en
counterpart — storyboard divergence D20, correctly absent, not a finding).

Drawn-art parity is already clean: all three of the -hi layers are present and
firing in the encoded mp4 — the four-blocks-around-a-square diagram held across
s77→s78, the six-marker escalating list on s79, the two-line income/need chart on
s81. No Lottie exists in -hi ch7, so none is owed here. Every finding below is a
PHOTOGRAPH finding: the queries in the `.src` sidecars are right, the files the
provider returned are not.

## Findings
| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s76 (7.3) | blocker | an ornate **dragon chōzuya** with wooden ladles, not a tsukubai | The foot cites "The tsukubai inscription at Ryoan-ji, Kyoto" over a photograph of a different object at a different place, with no basin and no four characters. A frame that contradicts a cited attribution is a factual error. -hi s75 is a legible top-down stone basin. | `reuse hi:studio/videos/japanese-money-methods-hi-ch7/assets/img/s75.jpg` |
| 2 | s77 + s78 (7.4, 7.5) | blocker | an out-of-focus wooden trough with a floating leaf; no basin, no square, no centre | The diagram asserts "all four share one part — the emptiness at the centre" and the photograph under it cannot be identified as a basin at all, so the drawn claim floats. This is the chapter's only cross-boundary hold, on the cut's weakest file. -hi s76 reads as a stone basin instantly. | `reuse hi:studio/videos/japanese-money-methods-hi-ch7/assets/img/s76.jpg` — one file, both scenes, hold intact (s78 stays file-less) |
| 3 | s80 (7.7) | blocker | a paving-slab / patched-asphalt texture | Sound-off it says nothing — no chalk, no line, no finish. The query asked for "chalk finish line half rubbed out and redrawn"; nothing of the kind arrived. -hi s79 carries visible chalk strokes and is why -hi could justify `art-off` here. | `reuse hi:.../hi-ch7/assets/img/s79.jpg`, or `source new: a chalk/paint finish line on asphalt, one line half rubbed out and a second redrawn a few feet further along, nothing else in frame` |
| 4 | s79 f1 + f2 (7.6) | blocker | f1 = a suburban open-plan kitchen/living room; f2 = an apartment balcony facade. No diploma, no keys, no car. | Both framings say the same thing — *housing* — so the swap spends 8.3s (the cut's longest scene) restating one of the six items twice while "Degree. Job. First paycheck. Phone. Car." go unillustrated. chapter.json promises "the diploma and keys, then the car outside the apartment"; neither photo delivers it. Two cells of one idea is the repeat rule. | f1 `source new: a framed US diploma and a set of car keys lying together on a kitchen counter, close` · f2 `source new: a used sedan parked at the kerb outside a US apartment block, evening, the car unmistakably the subject` |
| 5 | s82 (7.9) | blocker | a person under an umbrella in the rain, city bokeh behind | The line names *an entire industry* that makes what you own feel like less. The subject named is advertising; what is on screen is a rainy night and a stranger, which asserts a different scene. Storyboard asked for "a wall of backlit billboards over a night street". | `source new: a wall of backlit billboards / illuminated ad screens over a US night street, text illegible` (fallback `reuse hi:.../hi-ch7/assets/img/s81.jpg` — pure red neon bokeh, weaker but at least signage-coded and no human subject) |
| 6 | s83 (7.10) | blocker | an empty **conference room** — long table, six-plus chairs, office windows | The VO is "the only one here you have to answer for yourself". A boardroom is the collective frame; it argues with the line. -hi s82 is one chair by a window in a home, which is the whole point of the beat. Grade is also the flattest in the chapter — low-contrast grey-green mush, barely a photograph. | `reuse hi:studio/videos/japanese-money-methods-hi-ch7/assets/img/s82.jpg` |
| 7 | s84 (7.11) | should-fix | a macro of red maple leaves | The line closes the whole method and the storyboard asked for the Ryoan-ji garden at last light, wide. A leaf macro drops the callback and pairs with s74's mossy path as a second generic-foliage plate. Do not literally reuse s75 — a different angle of the same garden is the point. | `source new: the Ryoan-ji rock garden, wide, last light — a different angle from s75` (named monument, so `@commons` before a stock provider) |
| 8 | s80 (7.7) | note | no drawn layer on a beat that is literally a line that moves | -hi cut its moving-line proposal because its photograph already *is* a rubbed-out chalk line. If finding 3 is fixed with a photograph that does not carry the movement, this beat has no excuse left and earns the moving line (chapter is at 3 drawn layers, 0 Lotties, cap 4). | resolve after finding 3; if the new photo is static, `add measure bar: a first line, then the same line redrawn further right — asserts the move the photo cannot` |

## What is working
- All three drawn layers render correctly in the encoded mp4 and finish before their cuts: the s77→s78 square-then-scatter hold is intact and is the best idea in the chapter; the s79 six-marker escalation reads as a count at a glance; the s81 chart lands the right way round (need clearly above and steeper than income by 54.0s).
- s75 is genuinely the Ryoan-ji hōjō and rock garden — accurate, and full parity with -hi s74. s74 and s81 are both fine as they stand.
- Timing is clean: cue ladder gaps all ≥0.8s, first cue at 0.25s, s79's `data-framings` 5.50+2.849 partitions its own scene, s84 carries the bare 6.834 duration and the root sums exactly. No duplicate image hash anywhere in the chapter.
