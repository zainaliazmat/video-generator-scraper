---
summary: Gate ② storyboard SPEC for «Pay Yourself First» English/US cut — 9 scenes ported from the hi master skeleton (IDs verbatim), en timing.json measured values (total 177.772s), US hero math $400/mo → $4,800/yr, 2 photo-free scenes (s2, s7), explicit divergence list per scene.
updated: 2026-07-28
source: videos/pay-yourself-first/script-en.md + studio/videos/pay-yourself-first-en/assets/voice/timing.json (measured) + storyboard-hi.md (master skeleton) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]]
---

# STORYBOARD — «Pay Yourself First» · en cut

**Project:** `vault/videos/pay-yourself-first/src/en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @moneymavens101 $ · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **2:57.8** (timing.json total 177.772s) · **VO:** Brian `nPczCj…`
**Rate:** English 15.0 chars/s · **Grade:** dark blockframe · **Locale:** `en-US` (`$4,800`, never `₹` anywhere)

**Skeleton:** ported from [[storyboard-hi]] (master). Element IDs verbatim except
where the divergence list below says otherwise — fixes travel between cuts.

## Colour semantics for THIS video (derived from the thesis)

Thesis (same video, same argument): **paying yourself first is protection, not
sacrifice — the auto-transfer is the hero move; the leak is what's-left-saving.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green | the auto-moved money, the flipped formula, the $4,800 counter, SAVED BY 9 AM | saving-first is the hero, so the saved dollar is always the good outcome |
| `--warn` red | what's-left-saving — the drain to the 20th, 3¢-of-$1, the struck-out old formula, the $400 emergency you can't cover, "credit card at brutal interest" | the leak is the villain, never the spending categories themselves |
| `--target` amber | the rule under examination — "PAY YOURSELF **FIRST**", the 10%/5% steps, the DAY AFTER PAYDAY slot | it's the decision the viewer is being asked to make today |
| `--pop` orange | call to action — DO THIS TODAY stamp, subscribe block | (fixed) |

The test: if the auto-transfer, the counter, or the 5% step ever renders red, or
the empty-account drain renders green, the video argues against its own script.
The `#s7echo` card is the one deliberate warn→fund flip: the same $400 rendered
first as the uncoverable emergency (warn), then as the auto-save (fund).

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together.
- Reveal spacing ≥0.8s except declared cascades (≤5 items @ 0.6–0.7s). Something on screen by +0.5s.
- ≤6 elements visible at once — scenes that would exceed it declare **exits** below (s5, s6, s7, s8, s9).
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- `ken` alternates across photo scenes: **s1 in · s3 out · s4 in · s5 out · s6 in · s8 out · s9 in** (same as hi master).
- **Photo-free scenes: s2 + s7** (2 of 9 ≤ cap from `photo_free_scene_ratio` 0.23) — same rest beats as the hi master. Both get `drift()` — no static frame beyond ~2s. s7 is the hero-math scene and gets the calmest background in the video: densest scene, calmest bed.
- No phone-screen photos, no faces fighting the type — all queries below are object-led (script-en's phone/face suggestions replaced, see Image slots).
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger — no reuse from any prior video on either channel** (queries deliberately re-worded vs the hi cut so Pixabay/Pexels' deterministic top hit doesn't collide).
- No `₹`, lakh grouping, or India institution anywhere on screen (`forbidden_currency` per format.json).

## Cue classes

`A` = **anchored** — offset scales with the clip, lands on the noted English word.
Offsets below are char-interpolated design intent (`0.4 + chars_before/total × clip`);
the build refines them with faster-whisper word timings.
`F` = **fixed** — cascades, arrows, stamp slams, exits — constant regardless of clip length.
Surplus time from a longer clip goes into **holds (breathe/drift), never cascades.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured
`timing.json` values (see Timing table) — never re-derived.

### s1 · HOOK — empty by the 20th · en1 (clip 18.625s) · photo ×3 crossfade, ken IN · tint red .12

DOM (ported + 2 new): `#s1k .kicker` · `#s1q .huge` (warn span on `20TH?`) · `#s1cal .track2+.ticks` (20 ticks, draining) · `#s1stat .statstrip` **(new)** · `#s1f .foot` **(new)** · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "Be honest" | `rise` | scene open |
| 2 | +3.2 | A | `#s1q` EMPTY BY THE **20TH?** | `pop .7` | «empty by the twentieth» |
| 3 | +6.6 | A | `#s1cal` calendar bar `1 → 20` | `fade .5` then `fill` **reversed** (drains) over 2.8s | «save whatever's left» |
| 4 | +9.7 | A | `#s1stat` 1 IN 4 US HOUSEHOLDS — NOTHING LEFT AT MONTH-END | `rise .5` | «Nearly one in four» |
| 5 | +10.5 | F | `#s1f` "Bank of America Institute · Nov 2025" | `rise` | follows its stat |
| 6 | +12.0 | A | `#s1stamp` EVERY MONTH | `pop .6` + `pulse` | «ends the month with nothing» |
| 7 | +14.5 | A | `#s1q` warn span re-`pulse` + `breathe #s1q 3.5s` | hold | «hundred-year-old rule» — hold carries surplus |

Backgrounds crossfade under the block: `s1-a.jpg` (+0.0) → `s1-b.jpg` (+6.5 `fade`, F) → `s1-c.jpg` (+13.0 `fade`, F). Ken IN continues across all three.
Simultaneous max: kicker + huge + cal + statstrip + foot + stamp = **6** ✓.

### s2 · ROADMAP · en2 (clip 9.613s) · **photo-free → `drift()`** · no tint

DOM (ported verbatim): `#s2k .kicker` · `#s2a-d .chip` (2×2 rows: a+b / c+d) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +1.3 | A | `#s2a` SAVE FIRST, NOT LAST | `pop .45` | «saving what's left versus saving first» |
| 3 | +4.0 | A | `#s2b` WHY WILLPOWER LOSES | `pop .45` | «why willpower keeps losing» |
| 4 | +6.1 | A | `#s2c` PAYDAY AUTO-TRANSFER | `pop .45` | «the payday auto-transfer» |
| 5 | +7.6 | A | `#s2d` WHAT IT'S FOR | `pop .45` | «what that money is actually for» |
| 6 | +9.2 | F | `#s2sub` "Works even at 5%" | `rise` | end of clip |

Chips are anchored to their spoken beat (gaps ≥0.8s) — this is **not** a cascade.
`drift()` on the panel from 0 for the full 11.0s.

### s3 · CONCEPT — flip the formula · en3 (clip 19.174s) · photo, ken OUT · tint green .10

DOM (ported verbatim): `#s3k .kicker` · `#s3old .head2` (struck, warn) · `#s3new .huge.fund` (focal) · `#s3stamp .stamp.fund`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "Most people's formula" | `rise` | scene open |
| 2 | +2.6 | A | `#s3old` INCOME − EXPENSES = SAVINGS | `pop .6` | «income minus expenses equals savings» |
| 3 | +9.2 | A | `#s3old` strike-through draws (`scaleX` 0→1) + text → `--warn` | `fill .5` + `tl.to color .3` | «And nothing survives the month» |
| 4 | +11.6 | A | `#s3new` INCOME − SAVINGS = EXPENSES | `pop .7` + `breathe 4.5s` | «Flip it» |
| 5 | +14.9 | A | `#s3stamp` FLIP THE FORMULA | `pop .55` + `pulse` | «Take the savings out first» |
| 6 | +16.5 | F | `breathe #s3new` 3.5s | hold | «run the month on what's left» rides the held flip |

Gap +2.6 → +9.2 held by ken drift + `breathe #s3old` at +5.5 (F, 3.0s) — no static frame >2s.

### s4 · RULE — pay yourself first · en4 (clip 11.964s) · photo, ken IN · tint amber .12

DOM (ported + 1 new): `#s4k .kicker` · `#s4h .huge` (amber span on `FIRST`, focal) · `#s4book .chip.target` · `#s4q .sub` · `#s4t .chip.target` **(new)**

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "A 100-year-old rule" | `rise` | scene open |
| 2 | +1.8 | A | `#s4h` PAY YOURSELF **FIRST** | `pop .7` | «pay yourself first» |
| 3 | +3.5 | A | `#s4h` amber span `pulse` + `breathe 4.0s` | hold | «a hundred years old» |
| 4 | +6.4 | A | `#s4book` THE RICHEST MAN IN BABYLON · 1926 | `rise .5` | «The Richest Man in Babylon» |
| 5 | +8.4 | A | `#s4q` "A part of all you earn is yours to keep" | `rise` | «a part of all you earn» |
| 6 | +11.0 | A | `#s4t` START WITH 10% | `pop .45` + `pulse` | «Start with ten percent» |

Simultaneous max: kicker + huge + book + quote + chip = **5** ✓.

### s5 · AUDIT — why willpower loses · en5 (clip 21.342s) · photo, ken OUT · tint red .12

DOM (ported + 1 new): `#s5k .kicker` · `#s5a-c .chip.warn` · `#s5m .chip` **(new, muted context)** · `#s5stat .huge` (76px override — on ladder; warn span on `3¢ SAVED`, focal) · `#s5f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "Why willpower loses" | `rise` | scene open |
| 2 | +6.1 | A | `#s5a` DOORDASH | `pop .45` | «DoorDash» — cascade start anchors here |
| 3 | +6.75 | F | `#s5b` THE SALE | `pop .45` | declared cascade, 0.65s |
| 4 | +7.4 | F | `#s5c` CARD BALANCE | `pop .45` | declared cascade, 0.65s |
| 5 | +10.6 | A | `#s5m` MEDIAN PAY $1,251/WK | `rise .5` | «median full-time worker» |
| 6 | +14.9 | F | **exit:** `#s5k` fade .4 | `fade` | make room for the stat |
| 7 | +15.4 | A | `#s5stat` $1.00 EARNED → | `rise` | «as a country» |
| 8 | +16.3 | A | `#s5stat` warn span **3¢ SAVED** | `pop .6` + `pulse` | «three cents of every dollar» |
| 9 | +17.9 | F | `#s5f` "BLS Q2 2026 median weekly earnings · BEA personal saving rate 3.0%, May 2026" | `rise` | after the stat lands |

Gap +0.4 → +6.1 held by ken + `breathe #s5k 4.0s` at +2.0 (F). Simultaneous max after exit: 3 chips + context chip + stat + foot = **6** ✓.

### s6 · ACTION — day-after-payday auto-transfer · en6 (clip 19.174s) · photo, ken IN · tint green .10

DOM (ported + 2 new): `#s6k .kicker` · flow row `#s6f1-3 .head2` + `#s6ar1-2 .arrow` (CSS-drawn) · `#s6t1-2 .chip` + `#s6t3 .chip` **(new)** · `#s6x .sub` **(new)** · `#s6sub .sub.fund`

**Phase order inverted vs hi** (flow first, chips second) — the en VO names the
mechanism before the account rails. Same two-phase exit pattern.

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The fix — automation" | `rise` | scene open |
| 2 | +3.8 | A | `#s6f1` PAYDAY | `pop .5` | «morning after payday» — cascade start anchors here |
| 3 | +4.4 | F | `#s6ar1` → | `fade .3` | declared cascade, 0.6s |
| 4 | +5.0 | F | `#s6f2` AUTO-TRANSFER | `pop .5` | cascade |
| 5 | +5.6 | F | `#s6ar2` → | `fade .3` | cascade |
| 6 | +6.2 | F | `#s6f3` SAVED BY 9 AM (`--fund`) | `pop .5` | cascade (5 items total) |
| 7 | +7.4 | F | **exit:** `#s6f1-3 #s6ar1-2` fade out .4 | `fade` | flow beat done; make room for the rails |
| 8 | +7.8 | A | `#s6t1` HIGH-YIELD SAVINGS | `pop .5` | «high-yield savings account» |
| 9 | +9.6 | A | `#s6t2` DIFFERENT BANK | `pop .5` | «a different bank» |
| 10 | +10.7 | A | `#s6t3` FDIC INSURED | `pop .5` | «FDIC insured» |
| 11 | +11.9 | A | `#s6x` "~10× a typical savings account" *(no APY — standing rule)* | `rise` | «ten times the interest» |
| 12 | +14.0 | F | `breathe` chip row 3.0s | hold | «a day away from temptation» rides the hold |
| 13 | +17.2 | A | `#s6sub` "Money you never see, you never spend" | `rise` + `pulse` | «Money you never see» |

Chips t1–t3 are one declared row of 3 (≤22 chars each). Simultaneous max after exit: kicker + 3 chips + 2 subs = **6** ✓.

### s7 · THE MATH — the signature counter · en7 (clip 29.074s) · **photo-free → `drift()`, calmest background in the video** · no tint

The counter IS the visual. Counts $0 → $4,800 in **12 stepped increments of $400**
(= 12 months), `Intl.NumberFormat("en-US")`, tabular-nums, `.track2` filling
12 ticks in parallel. Focal: `#s7c .counter` (96px).

DOM (ported + 1 new): `#s7k .kicker` · `#s7sub .sub` · `#s7head .head2` · `#s7c .counter.fund` + `#s7track .track2/.fill2/.ticks` · `#s7echo` echo card **(new — `.billrow`-style, warn→fund flip)** · `#s7lad` ladder card (target border) · `#s7f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the math" | `rise` | scene open |
| 2 | +1.6 | A | `#s7sub` "Take-home: $4,000/mo" | `rise` | «take-home is four thousand dollars» |
| 3 | +4.4 | A | `#s7head` $400 · every payday · automatic | `rise` | «every payday, four hundred» |
| 4 | +8.5 | A | `#s7c` `$0` + `#s7track` | `fade .5` | «Twelve months later» |
| 5 | +9.0 | A | `countUp #s7c 0→4,800` stepped ×12 over 3.2s + `fill #s7fill 3.2s` | — | lands just after «four thousand eight hundred dollars» |
| 6 | +12.0 | F | **exit** `#s7sub` fade .4 | `fade` | room for the echo |
| 7 | +12.3 | A | `#s7echo` (warn) "$400 — the emergency ~4 in 10 adults can't cover" | `rise .5` | «And notice — four hundred dollars» |
| 8 | +19.3 | A | `#s7echo` flips → (fund) "$400 — your monthly auto-save" | text swap + border `tl.to color .3` + `pulse` | «Same number, two different lives» |
| 9 | +22.5 | F | **exit** `#s7k` fade .4 | `fade` | room for the ladder |
| 10 | +22.8 | A | `#s7lad` "Start at 5% → $200/mo = $2,400/yr" | `rise .5` | «Start at five» |
| 11 | +25.3 | A | `#s7lad` year figure `pulse` | pulse | «two thousand four hundred a year» |
| 12 | +26.5 | F | `#s7f` "Fed SHED 2025 · $4,000/mo take-home example" | `rise` | closing beat — «you're saving zero» rides the held counter (`breathe #s7c` +27.0, F) |

`.ticks` at `calc(100% / 12 - 2px)` — 12 months. **en-US grouping**: the counter
must read `$4,800`, never `$4800` (and never any en-IN grouping).
Simultaneous max after exits: head + counter + track + echo + ladder + foot = **6** ✓.

### s8 · DO THIS TODAY · en8 (clip 17.816s) · photo, ken OUT · tint orange .12

DOM (ported verbatim): `#s8stamp .stamp.pop` · `#s8a-c .chip` · `#s8ar1-2 .arrow` · `#s8sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` DO THIS TODAY | `pop .6` + `pulse` | scene-open slam |
| 2 | +1.9 | A | `#s8a` OPEN BANKING APP | `pop .5` | «Open your banking app» |
| 3 | +2.5 | F | `#s8ar1` → | `fade .3` | follows its chip |
| 4 | +3.5 | A | `#s8b` SCHEDULE THE TRANSFER | `pop .5` | «schedule the transfer» |
| 5 | +4.1 | F | `#s8ar2` → | `fade .3` | follows its chip |
| 6 | +5.4 | A | `#s8c` DAY AFTER PAYDAY (`.target` border) | `pop .5` + `pulse` | «day after your payday» |
| 7 | +7.1 | A | `#s8c` re-`pulse` | pulse | «even five percent starts the machine» |
| 8 | +9.9 | F | **exit:** `#s8stamp` fade .4 | `fade` | job done; room for the payoff |
| 9 | +10.3 | A | `#s8sub` "Even 5% works — first stop: emergency fund, then your goals" | `rise` | «First an emergency fund» |
| 10 | +13.5 | F | `breathe` chip row 3.0s | hold | «lands on savings, not on a credit card» rides the hold |

Simultaneous max after exit: 3 chips + 2 arrows + sub = **6** ✓.
Note: "brutal interest" stays VO-only — no APR number exists in facts-staging (contract rule).

### s9 · RECAP + CTA · en9 (clip 18.390s) · photo, ken IN · tint green .13

DOM (ported verbatim): `#s9k .kicker` · `#s9a-d .chip.fund` (2×2 rows: a+b / c+d) · `#s9sub .sub` · `#s9cta .cta`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "The simple version" | `rise` | scene open |
| 2 | +1.2 | A | `#s9a` SAVE FIRST | `pop .45` | «save first, spend second» |
| 3 | +2.7 | A | `#s9b` TRUST THE SYSTEM | `pop .45` | «Trust the system» |
| 4 | +5.6 | A | `#s9c` AUTOMATE ON PAYDAY | `pop .45` | «Set the auto-transfer today» |
| 5 | +7.7 | A | `#s9d` START AT 5% | `pop .45` | «even at five percent» |
| 6 | +9.4 | A | **exit** `#s9k` fade .4 · `#s9sub` "Next month, the 20th won't scare you" | `rise` | «Next month, the twentieth» |
| 7 | +12.0 | F | `breathe` chip rows 3.0s | hold | «don't say nobody warned you» rides the hold |
| 8 | +17.6 | A | `#s9cta` ▶ SUBSCRIBE (`--pop` block, `▶` CSS-drawn) | `pop .6` + `pulse` | «hit subscribe» |

Video closes on the `.cta` — no logo outro (script-en's "stamp SUBSCRIBE" rendered
as the standing `.cta` block per design system). Simultaneous max after exit:
4 chips + sub + cta = **6** ✓.

---

## Timing (measured — timing.json values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row,
root `data-duration`) — generate all four from `timing.json`, never hand-edit.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | en1 | 18.625 | 20.025 | 0.0 | 0.4 |
| s2 | en2 | 9.613 | 11.013 | 20.025 | 20.425 |
| s3 | en3 | 19.174 | 20.574 | 31.038 | 31.438 |
| s4 | en4 | 11.964 | 13.364 | 51.612 | 52.012 |
| s5 | en5 | 21.342 | 22.742 | 64.976 | 65.376 |
| s6 | en6 | 19.174 | 20.574 | 87.718 | 88.118 |
| s7 | en7 | 29.074 | 30.474 | 108.292 | 108.692 |
| s8 | en8 | 17.816 | 19.216 | 138.767 | 139.167 |
| s9 | en9 | 18.390 | 19.790 | 157.982 | 158.382 |
| **total** | | | | | **177.772** |

## Image slots (→ `assets/img/manifest.json`)

All object-led — no phone screens, no faces. 9 slots, 7 photo scenes. US-market
imagery: dollar bills, US paycheck stubs — never ₹ notes, never non-US signage
(sweep every fetch per the style note).

| slot | query | scene |
|---|---|---|
| `s1-a.jpg` | open empty brown wallet dark background | s1 |
| `s1-b.jpg` | desk calendar pages close up shadow | s1 |
| `s1-c.jpg` | scattered one dollar bills on table | s1 |
| `s3.jpg` | paycheck stub pen calculator desk | s3 |
| `s4.jpg` | antique book open warm candle light | s4 |
| `s5.jpg` | cardboard delivery boxes doorstep porch | s5 |
| `s6.jpg` | morning sunlight bedroom alarm clock | s6 |
| `s8.jpg` | hand inserting dollar bill piggy bank | s8 |
| `s9.jpg` | sunrise over american city skyline | s9 |

Script-en suggested phone-screen queries for s1/s6/s8 (`man checking phone bank app`,
`mobile banking transfer phone screen`, `hand tapping phone banking app`) — **replaced**:
the design doc bans phone-screen backgrounds (shipped wrong 3× already). s9 face query
(`young man smiling relieved phone`) replaced with a calm object-led closer. Queries
re-worded vs the hi cut so deterministic top hits don't collide; md5 every fetch
against the asset ledger, no reuse across videos or channels.

## `-en` divergence list (vs storyboard-hi.md, the master)

| scene | diverges how | why |
|---|---|---|
| s1 | adds `#s1stat .statstrip` + `#s1f .foot` (BofA 1-in-4) | the en hook carries a sourced US stat the hi hook doesn't have |
| s2 | none structural — IDs and chip copy identical | same four promises; anchors re-derived from en timing only |
| s3 | stamp lands mid-clip (+14.9 vs hi +22.0); trailing hold added | en VO closes on "run the month on what's left", not on the stamp beat |
| s4 | adds `#s4t` chip START WITH 10% | en VO states the starting rate in this scene; hi defers it to s7 |
| s5 | chips → DOORDASH / THE SALE / CARD BALANCE; adds `#s5m` context chip (Median pay $1,251/wk); stat → 3¢ of $1.00; foot → BLS + BEA; kicker exit added | US shocks replace SALE/FOOD APPS/EMI; BLS median-pay beat has no hi equivalent; 7 elements need an exit to hold the ≤6 cap |
| s6 | phase order inverted (flow first, chips second); chips → HIGH-YIELD SAVINGS / DIFFERENT BANK / FDIC INSURED (adds `#s6t3`); adds `#s6x` ~10× sub; flow f1 SALARY IN → PAYDAY | en VO names the mechanism before the account rails; US rails (HYSA/FDIC/ACH next-day) replace Standing Instruction/UPI Autopay |
| s7 | counter $0→$4,800, 12 steps of $400, en-US grouping; adds `#s7echo` warn→fund flip card (Fed SHED $400); `#s7sub` → take-home example (exits early); ladder → $200/mo = $2,400/yr; foot → Fed SHED; kicker exit added | US hero math from fin-script-en; the $400-emergency echo is the en cut's signature beat and has no hi equivalent |
| s8 | chip copy → OPEN BANKING APP / SCHEDULE THE TRANSFER / DAY AFTER PAYDAY; 5% moves from chip c to the sub | day-after-payday (ACH next-day) is the US action detail; hi's salary-date framing doesn't apply |
| s9 | none structural — IDs, chip copy, and cta identical | same recap; anchors re-derived; sub copy is the US 20th line |

## Deliberate placeholders (must be real before publish)
- Anchored cue offsets are char-interpolated intent — refine with faster-whisper word timings at build.
- `#s7echo` flip copy: both faces must show **$400** exactly (the echo is the point); trace to Fed SHED row in facts-staging.md.
- `#s5m` figure `$1,251/wk` and `#s5f` foot must match the BLS Q2 2026 row verbatim.

## Sign-off
- [x] Colour semantics table filled and consistent with the script
- [x] Every number traced to a sourced line (see script-en.md fact trace)
- [ ] No image hash reused from any prior video on either channel (check at fetch)
- [x] Photo-free scenes ≤2 (s2, s7), each with `drift`
- [x] Divergence list emitted — 7 of 9 scenes diverge, each with a reason
- [ ] Creator approved (Gate ②) — date: __
