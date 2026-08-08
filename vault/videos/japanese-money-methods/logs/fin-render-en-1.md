---
summary: Gate-two frame check for the -en cut, attempt 1. FAIL on one scene image — s77.jpg is a garden birdbath, not the Ryoan-ji tsukubai the VO describes, and it is held across two scenes (14.798s). Everything else passed, including the cross-dissolve stacking fix.
updated: 2026-08-01
source: hyperframes snapshot on studio/videos/japanese-money-methods-en (invocation 1 of 2 — no encode run)
---

# fin-render — japanese-money-methods · cut `en` · attempt 1

**STATUS: fail (gate two, before any encode).** No render was started; the master
does not exist and must not be paid for until the finding below is fixed.

## What was measured

| Quantity | Value |
|---|---|
| Composition runtime (`#root` data-duration) | **626.586 s** (10:26.586) |
| `timing.json` total | 626.586 s — identical, 0.000 s drift |
| Scenes | 92 (`s1`…`s92`), VO lines 92 |
| Scene boundaries | 91, every one a cross-dissolve |
| Measured overlap at every boundary | 0.449–0.451 s (nominal 0.450) |
| Act shoves (vs plain dissolve) | 2 — `s34`, `s74` |
| Frames sampled | **113** — 92 scene frames + 5 extra framing frames + 10 mid-dissolve + 5 late-dissolve + 1 re-shot (s24) |
| Snapshot artefacts | `studio/videos/japanese-money-methods-en/snapshots/qa/r1/{a…l,x1,x2,x3}` |

Audio QA numbers (VO drift, peak dBTP, blackdetect, runtime-vs-timing on the
master) are **not in this log** — they belong to invocation 2, which cannot run
until a master exists.

## 1. Blocker — `s77.jpg` shows the wrong object

`assets/img/s77.jpg` is a **square garden birdbath, filled to the brim with
water**, one dry leaf floating on it. Sampled at 519.618 / 521.500 / 523.500 /
526.766 / 528.500 / 531.300 s.

It is supposed to be the Ryoan-ji **tsukubai**: a round stone with a **square
opening cut through the centre**, the four characters 吾唯足知 arranged around
it so that the square hole is the shared 口 radical of all four.

What the cut says over that image:

- VO line `7.4` (`assets/voice/7.4.txt`, verbatim):
  *"All four characters share one single part, and that shared part is the empty
  square hole in the middle of the basin."*
- On-screen `#s77-stmt`: *"All four share one part — the empty square at the centre."*
- On-screen `#s78-stmt`: *"Each needs the emptiness in the middle to be whole."*
- Set up two scenes earlier by `#s75-stmt`: *"A stone basin. Four characters cut into it."*

There is no square opening in the frame, no round stone, and no carved
characters. The image contradicts the line it illustrates, and it is the one
image in the video the narration spends the most words explaining.

**Exposure: 14.798 s across two scenes** — `#s77-bg` (517.368 → 524.966) and
`#s78-bg` (524.516 → 532.166, `background-size:auto 130%`) both point at
`assets/img/s77.jpg`.

Root cause is in the sourcing, not the build. `assets/img/s77.jpg.src` reads
`square stone water basin japanese garden@pexels#7`; result #7 of that search is
titled **"serene leaf floating on water in birdbath"** (Dhanush N, Pexels
License — `assets/img/CREDITS.txt` line 93). The query matched "square" and
"basin" as words and returned a Western birdbath. The object being described is
never named in the query, so the search could not have found it: it needs
**tsukubai / chōzubachi / Ryoan-ji**, and the frame must contain the square
central opening.

*Related but not blocking:* `s76`'s panel (`s76.jpg`, "japanese stone water
basin tsukubai with bamboo ladle") is a generic dragon-spout chōzubachi while
`#s76-foot` reads "The tsukubai inscription at Ryoan-ji, Kyoto". It reads as
illustrative and the line on screen is the inscription, not the design, so it
passes. `s77` does not, because `s77`'s whole job is the design.

## 2. The cross-dissolve stacking fix holds — verified inside the transitions

The `.scene { isolation: isolate; }` fix (blockframe.css line 63, added after
the japanese-money-methods-hi finding) was checked **inside** the overlap, not
between transitions, because one-frame-per-scene sampling is structurally blind
to this class of defect.

**Mid-dissolve, T+0.225 s of 0.450 (`snapshots/qa/r1/x1`, `x2`)** — 10 boundaries
spread across the cut, including both act shoves and the CTA boundary:
4.264 (s1→s2) · 71.030 (s12→s13) · 152.676 (s23→s24) · 220.950 (s33→s34, shove) ·
292.914 (s44→s45) · 386.253 (s57→s58) · 498.214 (s73→s74, shove) ·
524.741 (s77→s78) · 574.201 (s84→s85) · 614.266 (s90→s91).

**Late-dissolve, T+0.400 s of 0.450 — incoming at ~97 % (`snapshots/qa/r1/x3`)**:
4.439 · 71.205 · 293.089 · 524.916 · 614.441.

Result at all 15: **never two scenes' text legible at once.** At mid-dissolve the
outgoing headline is visibly dimmed by the half-opaque incoming scene painting
*over* it; at T+0.400 it is extinguished to near-background grey while the
incoming rail number is already crisp. That ordering — outgoing under, incoming
over — is exactly what was inverted in the hi cut. The incoming scene's own
headline has not risen yet at either sample (text cues sit at T+0.6…+0.8), so the
overlap window contains at most one legible text block by construction.

## 3. The rest of gate two — pass

| Check | Result |
|---|---|
| `#root` cut class | `class="rail cut-en"` — correct |
| Watermark | `wm-en.png` = pink ring / yellow bespectacled coin = **@moneymavens101**. Distinct file from `wm-hi.png` (md5 `21de2de7…` vs `292c19c0…`); the hi mark is nowhere in this cut. Present bottom-right in all 113 frames, including every mid-dissolve frame (it hangs off `#root`, so it survives transitions). |
| SUBSCRIBE colour | Live path is the **`.cta` block**, not `.popc`: `background: var(--pop)` `#ff5c39` with `#0d1017` text. Sampled at 618.100 s — solid pop-orange pill, dark label. Coloured, not white. `.popc` now exists in the scaffold but `s91` does not use it; either path would paint correctly. |
| `.warnc` fix | `#s24-icon` (closed padlock, `class="icon sm warnc"`) paints **red** at 148.588 s, not white. The hi-cut s24 defect does not recur here. |
| `data-framings` scenes | All framings render and are visually distinct. `s32` (5.50/2.849 split): cracked wall @209.000 → Japanese shopfront noticeboard @211.847. `s36` (2.74/2.03/3.031): shirts on hangers @237.500 → misted field @239.500 → highway truck @240.928. `s79` (5.50/2.849): US kitchen counter @535.000 → apartment block @538.066. |
| `s77`/`s78` motion | One continuous Ken Burns push per scene on the shared image (`ken` in, 7.598 s then 7.650 s); the boundary is a plain cross-dissolve of the same photograph, so there is **no self-dissolve flicker** — confirmed at 519.618/521.500/523.500 and 526.766/528.500/531.300. The motion is correct; the photograph is not (§1). |
| Safe area | All headline / statement / rail / foot type inside the 110×150 px scene padding in all 92 scene frames. No clipping, no overflow, no element under the bottom-right watermark. |
| Contrast over photography | Legible in every frame. The two brightest backgrounds — `s43` @282.655 (green on tan) and `s65` @437.728 (red on USD bills) — both hold up; `npm run check` already scored 21/21 WCAG AA. |
| Currency & market | **$ only.** `$4,000` worked example, `$800`/`$3,200`, `$200`, `$400`, `$83,730` (Census P60-286), USD banknotes and a quarter as b-roll. JPY appears only where Japan's own statistics are quoted (JPY 197,432 / 522,569 / 175,241 / 6,705 — FIES 2024), which is correct. US institutions throughout: Federal Reserve G.19, Federal Reserve SHED 2025, US Census. |
| Prohibited imagery | **No ₹, no Devanagari, no Indian institution in any of the 113 frames.** The only non-Latin script on screen is Japanese signage in `s32`'s second framing and `s33` — both intentional. |
| Phone screens | `s39` @257.711 (subscriptions list) and `s12` @66.539 (phone silhouette) carry no currency symbol and no localised UI. Clean. |

## 4. Cosmetic, not blocking

`#s69-icon`'s arrowhead (`#s69-i-head`, `M82 26 L74 34 L82 42`) merges into the
tail of the swap curve at the `.icon.sm` 130 px size — the glyph reads as a hook
rather than an arrow (466.345 s). It draws, it takes the `fundc` green, and it
is legible as motion. Worth a nudge next time the icon set is touched; not worth
a rebuild.

## 5. Process note for the next run

Sampling ran against a machine already encoding the hi cut (load 7–11, ~28
headless Chrome processes). `hyperframes snapshot` failed with
`Navigation timeout of 10000 ms exceeded` on roughly two attempts in three and
needed a retry loop to complete; total wall time for 113 frames was ~85 min
against ~10 min unloaded. Gate-two sampling for the second cut should not be
scheduled against the first cut's encode.

## Verdict

One image defect, in the one place the narration cannot survive it. One build
retry remains for this cut.

**NEXT: fin-build must replace `assets/img/s77.jpg` with a Ryoan-ji tsukubai
frame in which the square central opening is visible** (search
`tsukubai` / `chozubachi` / `ryoanji stone basin square hole`, not
`square stone water basin`), keep it held across `#s77-bg` and `#s78-bg`, and
update `s77.jpg.src`, `manifest.json` and `CREDITS.txt`. Then re-run gate two.
