---
summary: Gate ③ stock-asset pass for credit-history en — 11 images accepted (9 bg + 2 cut-ins), 6 cut-ins dropped after the retry ladder failed; 30 fetches rejected on look or hash across 6 rounds. Every scene keeps its bg photo. Seven hash collisions against the channel grid — the highest yet, and none from the direction the storyboard predicted.
updated: 2026-07-29
source: pixabay_fetch.py runs against studio/videos/credit-history-en/assets/img/manifest.json; every image opened with Read; md5 ledger over studio/videos/*/assets/img/*.jpg (both channels)
---

# fin-assets — credit-history · en · attempt 1

**Result: 11 accepted / 30 rejected across 6 fetch rounds. 6 cut-ins dropped.**
All 9 backgrounds ship (`photo_free_scene_ratio` 0 held — no photo-free scene).

## Accepted (11)

| slot | final query | what it is | hash |
|---|---|---|---|
| `s1.jpg` | `card index` | clear index-card box, A–E tabs, blank cards, **pure black field** | `0d1cf0d4` |
| `s2.jpg` | `cardboard boxes` | stacked corrugated sheets edge-on, warm, no text | `d8142596` |
| `s3.jpg` | `manometer#2` | row of industrial gauges, black faces + yellow needles, dark | `b005ae33` |
| `s4.jpg` | `calendar#5` | spiral week-planner close-up, date grid + wooden pen | `861a2a71` |
| `s5.jpg` | `hourglass#6` | real glass hourglass, gold sand **running**, muted | `b0e95a0c` |
| `s6.jpg` | `sticky notes#3` | pastel note block + pen on a near-black desk | `09263e36` |
| `s6-cut.jpg` | `wall clock#2` | clean clock face, no numerals, no brand, red second hand | `af261113` |
| `s7.jpg` | `car key#2` | one flip car key on plain grey — **calmest bg, densest scene** | `3c780425` |
| `s8.jpg` | `lamp` | lit oil lantern on cobbles at night — **darkest bg in the set** | `9c20f7f6` |
| `s8-cut.jpg` | `red pen` | red fineliner marking a page, writing illegible | `c8f6c811` |
| `s9.jpg` | `highway sunrise` | empty road to a horizon, sun through dark cloud | `fa6f393e` |

Three land better than the storyboard's intent, not merely as recoveries:

- **`s1` (card index)** beats the specified `filing cabinet` outright. Tabs + blank
  cards filed under letters *is* «a file on you», and it arrives on a pure-black
  field — the storyboard asked for "drawers/tabs, dark" and got all three.
- **`s7` (car key)** is one object on an empty field, no badge anywhere. Every other
  car photo this run carried a manufacturer mark (see the structural finding below).
- **`s8` (lantern)** is the only genuinely dark, gradient-rich background in the set.
  Its warm pool of light sits exactly on s8's `--pop` orange tint `.12`, and the dark
  surround gives the CTA stamp and two action blocks clean type contrast.

## Dropped cut-ins (6) — every scene keeps its bg

Authority: a cut-in may be dropped rather than faked; a background may not.
The hi cut set the precedent at 3; this cut needed 6.

- **`s1-cutA`** («a file on you»). Four queries, four misses: `unopened mail` → a
  sunflower bud; `envelopes` → a pink envelope stuffed with roses; `mailbox` → an
  ornate German **`POSTBRIEFKASTEN`** with a collection timetable legible; `junk mail`
  → a rusted blank sign on volcanic gravel. Pixabay's mail library is wedding
  stationery and European street furniture.
- **`s1-cutB`** («The lender reads it»). Four attempts, and the query family is
  structurally people-led: `contract` and `contract#3` both returned **a man in a suit
  signing paper** (person as subject where an object was asked for); `paperwork`
  **collided with `emergency-fund/s1-bill.jpg`**; `documents` returned the identical
  man-signing image as `contract`. There is no object-led hit to walk to.
- **`s3-cut`** («one three-digit number»). `odometer` → a **km/h** instrument cluster
  (metric, in the US cut); `odometer#2` → a **`FORD MUSTANG`** horn cap, brand legible.
  **Dropped on merit as well as failure**, and this is the same call the hi cut made on
  the same slot: `#s3scale` ("300 ├──┤ 850") *is* the three-digit number rendered as
  type, and the storyboard is deliberate that s3 carries **one focal only** (cue 12
  exits everything else). A second number-object competes with it.
- **`s4-cut`** («your available credit»). `leather wallet` → a wallet with
  **`MasterCard` legible** and non-US banknotes; `leather wallet#2` → **collided with
  `pay-yourself-first-hi/s1-a.jpg`**; `leather wallet#3` → a handsome dark bifold with
  **`kalibrado` embossed** on the face. Three attempts, two brand marks. The storyboard
  substituted `leather wallet` for `credit cards` precisely to dodge the hi run's
  MasterCard×4 + Payoneer result, and the minefield extends to plain wallets too.
- **`s5-cut`** («on your report»). `ink blot` → a butterfly on lantana; `ink stain` → an
  orange ink cloud in water on black (brand-free and dark, but an abstract, not "a black
  mark on a **page**" — a pretty photo under a line it does not answer); `ink stain#2` →
  a **`ROYAL`** typewriter collage with dense legible print. Dropping also relieves the
  hero scene, which the storyboard already holds at a peak of 6 with three exits.
- **`s7-cut`** («used car»). `car dealership` → a **RAM** truck console (`PRND`, `4WD
  HIGH/LOW`, `AXLE LOCK`); `used cars` → a tyre dump with **`GOODYEAR`** and
  **`BRIDGESTONE`** legible, which also argues the wrong thing (a scrap heap under
  «a twenty-five-thousand-dollar used car» says the car is worthless — but this scene's
  whole point is that the car is identical and only the score differs); `parking lot` →
  an empty bay at night, no car in frame at all.

### What the build must change

The storyboard's cue tables still reference these IDs. Remove:

- **s1** — cue 2 (`#s1cutA` at +1.7), cue 6 (`#s1cutB` crossfade at +8.1), cue 10
  (exit `#s1cutB` at +12.9). Drop `#s1cutA`/`#s1cutB` from the DOM line. The scene's
  bg is now itself the "unread file", so nothing is lost semantically.
- **s3** — cue 9 (`#s3cut` at +12.8); drop `#s3cut` from cue 12's exit list.
- **s4** — cue 5 (`#s4cut` at +9.9); drop `#s4cut` from cue 8's exit list. The
  storyboard re-anchored this cut-in to +9.9 specifically so it would not collide with
  `#s4r2` at +11.0; with it gone the +8.0→+11.0 window carries no reveal. `ken OUT` is
  continuous so §5.2 still holds, but if the build wants a beat there, `pulse` `#s4r1`
  at ~+9.9 — **do not** substitute an unrelated photo.
- **s5** — cue 5 (`#s5cut` at +5.6) and cue 9 (its exit at +8.2). The +4.2→+6.6 window
  is covered by the continuous `.fill2` sweep (cue 4 runs +4.6→+15.5), which the
  storyboard requires to be in motion at every point in the scene anyway.
- **s7** — cue 4 (`#s7cut` at +8.0); drop `#s7cut` from cue 6's exit list.

**Every simultaneous-element count only decreases; no cap is at risk.** Recomputed
peaks: s1 +9.7 → 4 (was 5) · s3 +12.8 → 4 (was 5) · s4 +11.0 → 4 (was 5) · s5 +8.6 → 4
(was 5) · s7 +9.1 → 4 (was 5). The audit's `≤6` advisories on en5/en7 are closed with
more margin than the storyboard claimed, not less.

## Rejected (30) — by trap

**Readable brand marks (9).** `MasterCard` on the s4-cut wallet; `kalibrado` embossed
on the third s4-cut wallet; `WIKA` on the first manometer dial; **`DB`** (Deutsche Bahn)
on the s6-cut station clock; `FORD MUSTANG` on the s3-cut horn cap; **Apple logo** on
the s8 iMac *and again* on the second s8 flat-lay (iMac + Magic Mouse + EarPods);
`GOODYEAR` + `BRIDGESTONE` on the s7-cut tyre dump; `LAROUSSE` ×2 on the s1 antique
books. Brand marks were the single largest rejection class this run.

**Licensed character IP (1).** Round-1 `hourglass` returned **two Minions** — a
Universal/Illumination character, in focus, twice, as the hero scene's background.

**Hash collision with a shipped image (7).** The largest count on record:
- `s4` (`desk calendar`) ≡ `pay-yourself-first-en/s1-b.jpg` (`74321829`)
- `s4-cut` (`leather wallet#2`) ≡ `pay-yourself-first-hi/s1-a.jpg` (`5f5899d9`)
- `s1-cutB` (`paperwork`) ≡ `emergency-fund/s1-bill.jpg` + `-en` (`9a6fdd20`)
- `s4` (`calendar#2`) ≡ `emergency-fund/s4.jpg` + `-en` (`f1450a38`)
- `s1-cutB` (`contract` r1) ≡ `50-30-20-rule-en/s7.jpg` (`0d48ed1f`) — also the image
  the hi run rejected as its own round-2 `s8`
- `s5` (`sand timer`) ≡ this cut's own already-rejected `hourglass#2` — a **same-slot
  repeat**: two different queries, one image
- `s1-cutB` (`documents`) ≡ this cut's own already-rejected `contract` — same again

**Person as the subject where an object was asked for (4).** The suited man signing
paper (×2, s1-cutB); a woman standing in a bookshop for `reading lamp#2`; a tiny monk
figure composited inside the s5 hourglass.

**Legible headline / cover text (2).** The bookshop shot carried **`SPARE` with Prince
Harry's face on the cover** plus `KATE MORTON HOMECOMING` and `FEVERED STAR` — a
recognisable public figure and readable titles, in the CTA scene. The round-1 s6 sticky-
note case carried a **`2014`** calendar (a twelve-year-old date on screen) in four
languages.

**Wrong-domain / keyword miss (7).** A **sphygmomanometer** (blood-pressure cuff, with
`SPHYGMOMANOMETER` on the dial) for `pressure gauge`; an **Aztec sun stone** for
`calendar#6`; five pastel plastic egg-timers for `sand timer#2`; a sunflower bud for
`unopened mail`; roses in an envelope for `envelopes`; a butterfly on flowers for
`ink blot`; a rusted blank sign for `junk mail`.

**Picture argues against the line (1).** Round-1 `car key` returned a fob marked
`PANIC` held in front of a purple **Dodge Challenger** — a muscle car under a
$25,000-used-car subprime scene, and the busiest, brightest image in the run under the
scene the storyboard designates as needing the *calmest* background.

## The findings that matter

**1. Short queries won again, and `#N` is the wrong knob for a broken query.** The
storyboard shipped 1–3-noun queries per the hi run's lesson, and round 1 landed **3 of
17** anyway — but the failures were traps, not vagueness. Where the noun was right and
only the ranking was wrong, `#N` fixed it (`manometer#2`, `sticky notes#3`, `wall
clock#2`, `car key#2`, `hourglass#6`). Where the noun itself was wrong, `#N` returned
more of the same wrong thing and only a **synonym** moved it: `filing cabinet` →
`archive` → **`card index`**; `desk lamp` → `reading lamp` → **`lamp`**. Three of the
four hardest slots were solved by shortening to a single commoner noun, not by
descending the result list.

**2. Any photo containing an identifiable car carries a manufacturer badge.** This is
structural, not bad luck: Mustang horn cap, Dodge Challenger, RAM console, Goodyear and
Bridgestone sidewalls, a Chevrolet-slugged dealership shot. `s7`'s accepted car key
survives *because* it is a bare key on an empty field with nothing to badge.
**Storyboards for car-market videos should not ask for a car** — ask for the key, the
road, the paperwork. `s7-cut`'s "a row of cars" was unfillable by construction.

**3. The collision risk came from the wrong direction entirely.** The storyboard named
5 collision risks against `credit-history-hi` and all 5 are **clear**: `s1` vs its
archive shelves (`14bc6463`), `s4` vs its calendar (`bb2ac44c`), `s6-cut` vs its pocket
watch (`5153cf85`), `s7` vs its house key (`a43e2d5b`), `s8-cut` vs its checklist pen
(`5b0a0e72`). Every actual collision came from an unflagged project —
`pay-yourself-first` ×2, `emergency-fund` ×2, `50-30-20-rule-en` ×1 — plus two
same-slot repeats inside this run. **Same-slug adjacency is not where the duplicates
live; generic office nouns are.** `calendar`, `wallet`, `paperwork`, `contract` and
`desk lamp` are the saturated tokens across the whole grid, because every finance video
reaches for them. Future storyboards should treat those five as pre-burned and name a
distinctive noun up front.

**4. Two queries returned an image this run had already rejected under a different
name.** `sand timer` → the `hourglass#2` newspaper shot; `documents` → the `contract`
man-signing shot. Hashing every fetch against *this video's own* rejected set, not just
the shipped ledger, is what caught both.

## Ledger check

`md5sum studio/videos/*/assets/img/*.jpg | uniq -w32 -D` across **both** channels
returns no `credit-history-en` path — **all 11 kept hashes are unique**, against every
prior video on either channel and against each other.

`CREDITS.txt` is append-only by design and carries one line per *fetch attempt* (54
lines for 30 rejects + 11 keeps). **Every kept image has its line; the last entry per
filename is the live one.** Do not read the file top-down as the shipping credit list.

Stale files for the 6 dropped slots remain on disk (`s1-cutA.jpg`, `s1-cutB.jpg`,
`s3-cut.jpg`, `s4-cut.jpg`, `s5-cut.jpg`, `s7-cut.jpg` + `.src` sidecars) —
unreferenced by the pruned manifest, so inert. Unlike the hi run's leftovers, **none of
these six collides with anything**, so a future ledger sweep stays clean; they are dead
files, not assets.

## The one filter override (s1)

`s1.jpg` is the only near-black image in the kept set — roughly 70% of the frame is a
**flat, gradient-free black field**, with the white index box confined to the left third.

This is the failure mode the vault describes, in its sharper form. The bright subject
survives `brightness(.62)` fine; the risk is the black field, which has **no tonality to
crush and no gradient to move**. s1 runs `ken IN` for 16.1s over that field, and a
parallax move across a dead-flat black area reads as **no motion at all** (§5.2) — the
same trap the hi cut called on its s8, but worse here because there is no light falloff
anywhere in the frame to betray the movement.

**Set on `#s1 .bg` only:** `filter: grayscale(.32) brightness(.95) contrast(1.05)`.

A gentle lift that brings the black field up to a workable near-black with visible
tonality, deliberately nowhere near `50-30-20-en`'s `brightness(1.45)` (that was
rescuing charred wood with no bright subject). **Ceiling:** this is a judgement from
looking at the image, not a measured mean-luminance figure — there is no image tooling
on this stage's allowlist. If the build has ffmpeg to hand, measure it and adjust; if
the white index cards blow out against the s1 red tint `.12`, come back toward `.78`.
**This is the video's only override — do not add a second.** `s8`'s lantern is dark but
carries a strong light-pool gradient, so it grades normally and needs nothing.

## Residual notes for the build

- **`s4` carries legible German weekday names** — `Dienstag`, `Mittwoch`, `Donnerstag`
  — on a full-bleed background in a US-market cut. It is not a brand mark and the slot's
  substance (the date grid, the numerals `14 15 16`, the hour columns) is exactly right,
  which is why it is kept after four attempts; `calendar#4` and `calendar#5` return the
  same hit, and `#2` and `#6` were a hash collision and an Aztec carving. This is the
  one kept image with foreign-language text a viewer could read — the same call, and the
  same caveat, the hi run recorded for its `s1-cutB`. **If the build wants it gone,
  frame `ken OUT` toward the right two-thirds**, where the numerals dominate and the day
  names fall off the edge.
- **`s5` has a small `QUALITY` seal** on a disc at the base of the lower bulb. It is a
  generic quality roundel, not a company mark — no firm is identifiable — and it sits
  bottom-centre, precisely where `#s5ctr` ("YEAR 1 → YEAR 7") renders over it from +6.6.
  Kept on that basis. Crop the bottom ~8% if the build disagrees.
- **`s6-cut`'s red second hand.** s6 is the green AUTO-PAY scene and red in this video
  means the miss and its price. The hand is a hairline at ~1% of frame area and is not a
  colour claim, but do not enlarge the cut-in past its planned framing.
- **High-key watch items.** `s2`, `s4`, `s6-cut` and `s8-cut` are bright images that will
  land at a light mid-grey under `brightness(.62)` rather than the near-black the system
  usually gets. Lean on the scrim rather than the grade for type contrast on those
  scenes. This is a legibility watch item, not a defect.
- **`s3` shows five gauges, not one.** The storyboard asked for "an analog dial +
  needle"; the accepted image is a diagonal row of them, which reads as instrumentation
  and measurement and is a stronger "score under examination" than a single dial. The
  dials carry scale numerals (10–60, °C/°F) but no readable maker. s3's focal
  `#s3scale` sits centre and the gauges run lower-right, so they do not compete.
- **`s1` is a *better* literal read than the storyboard's plan.** With both s1 cut-ins
  dropped, the scene rests entirely on the bg — and an index-card file with lettered
  tabs answers «there is a file on you» more directly than the filing cabinet the
  storyboard specified, so the hook loses nothing by the drops.

## Sign-off

- [x] Every scene has a full-bleed bg photo (9/9) — `photo_free_scene_ratio` 0 held
- [x] Every image opened with Read and judged on the measured trap list
- [x] md5 checked across both channels **and** against this video's own rejects; 11/11 unique
- [x] All 5 storyboard-flagged `credit-history-hi` collision risks checked by hash and clear
- [x] No brand mark, no face, no phone screen, no licensed character, no `₹`, no metric unit in the kept set
- [x] s7's subject verified as an actual car key, not a fob-with-no-key (the inverse of the hi cut's house-key/car-fob defect)
- [x] Every kept image has a CREDITS.txt line
- [x] One filter override, on s1, with its ceiling recorded
- [ ] Build stage removes the 6 dropped cut-in cues (s1 cues 2/6/10, s3 cue 9, s4 cue 5, s5 cues 5+9, s7 cue 4)
