---
summary: Gate ② storyboard SPEC for «Good Debt vs Bad Debt — the minimum-payment trap» EN / USA cut — 9 scenes, scene DOM + GSAP cue tables on measured en timing.json (total 178.58s / 2:59), keyword-matched bg + cut-ins on EVERY scene (photo-free retired). US rewrite of the hi master skeleton — element IDs ported verbatim, divergence list per scene.
updated: 2026-07-28
source: videos/good-debt-vs-bad-debt/script-en.md ($ SET, audit-approved) + studio/videos/good-debt-vs-bad-debt-en/assets/voice/timing.json (measured, total 178.582s) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]] + storyboard-hi.md (master skeleton) + fin-voice en1 s1 flag (interest reveal ~13.2s)
---

# STORYBOARD — «Good Debt vs Bad Debt» · en cut (USA)

**Project:** `vault/videos/good-debt-vs-bad-debt/src/en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @moneymavens101 $ · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **2:58.6** (timing.json total 178.582s) · **VO:** Brian `nPczCj…`
**Rate:** English 15 chars/s · **Grade:** dark blockframe · **Locale:** `en-US` (`$9,496`, never `$9496`)
**Currency:** `$` only. **A rupee sign anywhere in this cut is a hard fail** — no ₹, no lakh, no India institution, no cross-market figure.

## Colour semantics for THIS video (derived from the thesis — mandatory)

Thesis: **the minimum payment is a trap that keeps you renting money for the better
part of two decades; good debt buys something that grows, bad debt just spends — the
escape is paying more than the minimum.** On a credit-card video red MUST be the
interest trap (design-finance-blockframe §2 — not reused blindly).

| Token | This video means | Because |
|---|---|---|
| `--fund` green | good debt · the escape (paying **MORE** than the minimum) · money kept off the principal · every extra dollar at the principal | the constructive path — anything that grows value or cuts the debt |
| `--warn` red | the interest / minimum-payment **trap** · bad debt · the card balance · interest > amount borrowed | red is the trap being exposed, never a neutral baseline |
| `--target` amber | the thing under examination — the card, the concept "debt = renting money", the rule/decision | it's what the viewer is being asked to weigh |
| `--pop` orange | call to action — DO THIS TODAY stamp, subscribe block | (fixed) |

The test: if **MINIMUM** ever renders green, or **paying more / good debt** renders
red, or the $9,496 interest reads green, the video argues against its own script.

> **Cross-stage colour correction (this storyboard overrides script-en s6 on-screen note).**
> `script-en.md` §en6 writes *"huge: `PAY MORE THAN THE` + fund span `MINIMUM`"* — that
> paints the **trap** in the **escape** colour. Corrected here: the `--fund` span sits on
> **MORE** (the escape action), never on **MINIMUM**. This carries the hi audit fix
> (storyboard-hi s6: "green on MORE, never MINIMUM") into the en cut. Flagged to the audit.

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together — where a scene has two focal moments (huge → bill), the first **exits** before the second.
- Reveal spacing ≥0.8s except declared cascades (≤5 items @ 0.6–0.7s). Something on screen by +0.5s (every scene opens at +0.40).
- ≤6 elements visible at once — scenes that would exceed it declare **exits** below.
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- **Every scene carries a full-bleed bg photo** (creator rule 2026-07-28 — `photo_free_scene_ratio` 0; photo-free retired). Every scene gets `ken`; `ken` **alternates**: **s1 in · s2 out · s3 in · s4 out · s5 in · s6 out · s7 in · s8 out · s9 in**. No static frame beyond ~2s.
- **Densest scenes get the CALMEST bg** (quiet texture reading of the keyword, never no image): s4 (classifier) → cap+books, s5 (rule block + huge + snowball) → card statement, s7 (the math, 6 elements) → calculator/notepad. Density managed by a quieter image, never by dropping the image.
- **Keyword-matched imagery:** when the VO names a concrete thing it appears — as the bg or as a cut-in timed to its word (see per-scene tables + Image slots).
- **US imagery only** — $ bills, US card art, no ₹/lakh, no foreign signage/vehicles/coins. **No phone-screen photos as bg, no faces fighting the type** — the script's phone-banking bg (s6/s8) and s9 "young man with phone" face+screen are replaced object-led (see Image-sourcing note).
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger — no reuse from any prior video on either channel, and none from the hi cut** (Pixabay's top hit is deterministic; different queries collapse to the same file).

## Cue classes

`A` = **anchored** — offset scales with the clip, lands on the noted English word.
Offsets below are char-interpolated design intent (`0.4 + chars_before/total × clip`);
the build refines them with faster-whisper word timings.
`F` = **fixed** — cascades, arrows, stamp slams — constant regardless of clip length.
Surplus time from a longer clip goes into **holds (breathe/ken), never cascades.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured en
`timing.json` values (see Timing table) — never re-derived.

### s1 · HOOK — the minimum is a trap (month-1 split IS the focal shock) · en1 (clip 17.371s) · photo, ken IN · tint red .12

DOM: `#s1k .kicker` · `#s1q .huge.warn` ("MINIMUM PAYMENT", exits) · `#s1cut` card-statement cut-in (exits) · `#s1bill .bill` → `#s1r1 .billrow` · `#s1r2 .billrow.warn` · `#s1r3 .billrow` · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "The most dangerous words on a credit card" | `rise` | scene open |
| 2 | +3.3 | A | `#s1q` "MINIMUM PAYMENT" + `#s1cut` fade | `pop .7` | «minimum payment» |
| 3 | +5.5 | F | `#s1q` breathe (holds across «It feels safe. It's a trap. On a six-thousand-dollar balance») | hold | surplus → hold |
| 4 | +8.9 | F | **exit** `#s1q` + `#s1cut` fade .4 | `fade` | clear for the bill (focal handoff) |
| 5 | +9.5 | A | `#s1r1` "YOU PAY  $170" | `rise .4` | «the minimum runs about a hundred seventy dollars» |
| 6 | **+13.1** | A | `#s1r2` "→ INTEREST  $110" (warn) | `pop .5` + `pulse` | «a hundred ten of that is pure interest» — **the trap-proof, ≤15s (see advisory)** |
| 7 | +14.3 | A | `#s1r3` "→ OFF THE DEBT  $60" | `rise .4` | «Only sixty dollars comes off what you owe» |
| 8 | +15.8 | F | `#s1stamp` "IT'S A TRAP" | `pop .6` + `pulse` | verdict slam after the split (fixed — not the early spoken «it's a trap») |

**s1 build advisory (fin-voice en1 flag — TIGHTEST in the video).**
en1 is 17.371s; the interest clause «a hundred ten of that is pure interest» measures
~13.2s in (fin-voice). `#s1r2` (INTEREST $110 — the trap-proof) must reveal **on** that
word and be fully readable **≤15s**; char-interpolated here at +13.1. The principal row
`#s1r3` ($60) is synced to its own spoken word «Only sixty dollars» (~+14.3), **not gated
to clip end**. The whole split lands ≤15s (r1 +9.5 · r2 +13.1 · r3 +14.3). **At build:
ffprobe/whisper-verify en1; if the interest clause measures past 15s, tighten r1/r2
forward on the interest word — do not push r3 earlier than spoken.** Simultaneous peak =
kicker + 3 rows + stamp = **5** ✓ (huge + cut-in exited at +8.9).

bg `s1.jpg` credit card + unpaid paper bills on a dark desk (ken IN). cut-in `s1-cut.jpg` paper card statement, minimum-payment-due line, on «minimum payment» (object-led — the script's "phone with card statement" is replaced, design §7).

### s2 · ROADMAP — four things (calm rest beat, tightest clip) · en2 (clip 9.848s) · photo, ken OUT · tint — (transparent wash)

DOM: `#s2k .kicker` · `#s2a-d .chip` (2×2 rows: a+b / c+d) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +1.2 | A | `#s2a` WHAT DEBT REALLY IS | `pop .45` | «what debt really is» |
| 3 | +2.6 | A | `#s2b` GOOD vs BAD DEBT | `pop .45` | «good debt versus bad debt» |
| 4 | +4.4 | A | `#s2c` HOW THE MINIMUM WORKS | `pop .45` | «how the minimum works» |
| 5 | +7.0 | A | `#s2d` COMPOUNDS AGAINST YOU | `pop .45` | «interest compounds against you» |
| 6 | +8.4 | A | `#s2sub` "Then one move for today" | `rise` | «Then one move to make today» |

Chips are anchored to their spoken beat (gaps 1.4 / 1.8 / 2.6 / 1.4 s ≥0.8) — this is
**not** a cascade, just tighter than hi (en2 clip is 9.848s vs hi 13.740s). Chip char
check (≤22): a 19 · b 16 · c 21 · d 21 ✓. Chips carry **neutral ink** borders (roadmap
topics, not colour claims). Simultaneous: kicker + 4 chips + sub = **6** ✓. bg `s2.jpg`
fanned US dollar bills flat-lay texture — the calmest image in the video (roadmap rest
beat), slow ken OUT. No cut-in (abstract).

### s3 · CONCEPT — debt is renting money · en3 (clip 21.682s) · photo, ken IN · tint green .10

DOM: `#s3k .kicker` · `#s3h .huge` ("DEBT =" + `.accent` amber span "RENTING MONEY", focal, exits) · `#s3sub .sub` · `#s3good .row.fund` · `#s3bad .row.warn` · `#s3cutA`/`#s3cutB` cut-ins (crossfade)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "First — what debt really is" | `rise` | scene open |
| 2 | +2.6 | A | `#s3h` "DEBT = **RENTING MONEY**" (amber span) | `pop .7` | «Debt is renting money» |
| 3 | +4.9 | A | `#s3sub` "Interest is the rent" | `rise` | «the interest is the rent» |
| 4 | +6.5 | F | `#s3h` breathe (holds across «Renting money isn't always wrong — it depends what you rent it for») | hold | surplus → hold |
| 5 | +11.3 | F | **exit** `#s3h` + `#s3sub` fade .4 | `fade` | clear for the contrast |
| 6 | +12.1 | A | `#s3good` "A TOOL THAT EARNS → rent worth it" (fund) | `pop .5` | «Rent a tool that earns» |
| 7 | +16.6 | A | `#s3bad` "A DINNER, A SALE → rent on a ghost" (warn) + `#s3cutA` fade | `pop .5` | «Rent it for a dinner» |
| 8 | +17.5 | A | `#s3cutB` crossfade over `#s3cutA` | `fade .5` | «or a sale» |
| 9 | +20.8 | A | `#s3bad` `pulse` + breathe | hold | «it's gone by morning — the rent runs for years» |

Simultaneous peak (+16.6–17.5): kicker + good + bad + cut-in = **4** ✓ (huge/sub exited;
the two cut-ins crossfade so only one is up at a time). bg `s3.jpg` rolled dollar bills
passed hand to hand (renting money), ken IN. cut-ins on the concrete **bad** things the VO
names (a dinner, a sale) — the good side is abstract («a tool that earns»), correctly bg-only.

### s4 · RULE — good debt vs bad debt (two-column classifier, densest) · en4 (clip 24.242s) · photo (calm), ken OUT · tint amber .12

DOM: `#s4k .kicker` (exits) · `#s4good .col.fund` (header + tags A DEGREE / A SKILL / A BUSINESS, popEach inside) · `#s4bad .col.warn` (header + tags CLOTHES / GADGETS / VACATIONS, popEach inside) · `#s4cut` shopping-bags cut-in · `#s4stamp .stamp.warn` · `#s4f .foot`

> **Layout note (≤6 elements — ported from hi s4).** A literal 3+3 chip classifier is 2
> labels + 6 chips = 8 visible → over cap. Each column is therefore **one `.col` card**
> whose three items reveal with a micro `popEach` inside the single entry (counts as 1
> element, not a cascade). Deliberate divergence from the script's word "chips"; the
> good/bad **role colours are preserved** on the card borders.

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "The rule" | `rise` | scene open |
| 2 | +4.9 | A | `#s4good` GOOD DEBT · value grows (+ tags popEach) | `pop .6` | «a degree, a skill, a business» |
| 3 | +7.5 | F | `#s4good` breathe (holds «While you pay it down, it's earning for you») | hold | surplus → hold |
| 4 | +10.6 | A | `#s4bad` BAD DEBT · just spending (+ tags popEach) | `pop .6` | «Bad debt just buys consumption» |
| 5 | +13.0 | A | `#s4cut` shopping-bags cut-in | `fade .5` | «clothes, gadgets, a vacation» |
| 6 | +15.0 | F | **exit** `#s4k` fade .4 | `fade` | kicker's job done |
| 7 | +17.7 | A | `#s4stamp` "CARD BALANCE = WORST" (warn) + breathe | `pop .6` + `pulse` | «Worst of all: a credit-card balance» |
| 8 | +20.4 | A | `#s4f` "Even good debt is only 'good' if the return beats the interest" | `rise` | «debt is only good when the return beats the interest» |

Simultaneous peak (+20.4): good card + bad card + cut-in + stamp + foot = **5** ✓ (kicker
exited). Tag char check (≤22): A DEGREE 8 · A SKILL 7 · A BUSINESS 10 · CLOTHES 7 · GADGETS
7 · VACATIONS 9 ✓. Stamp "CARD BALANCE = WORST" 19 ✓. bg `s4.jpg` mortarboard + diploma on
textbooks — **calmest bg, densest scene**, ken OUT. The honest-caveat foot is load-bearing
(audit): good debt only wins if the return beats the interest.

### s5 · AUDIT — how the minimum works + compounds against you (dense) · en5 (clip 18.651s) · photo (calm), ken IN · tint red .12

DOM: `#s5k .kicker` (exits) · `#s5r1 .billrow` · `#s5r2 .billrow.warn` · `#s5r3 .billrow` (rule block, exits) · `#s5h .huge.warn` ("INTEREST ON INTEREST", focal) · `#s5snow .sub` + `#s5cut` snowball cut-in · `#s5f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "How the minimum actually works" | `rise` | scene open |
| 2 | +3.8 | A | `#s5r1` "MINIMUM = 1% of balance + interest" | `rise .4` | «one percent of the balance, plus that month's interest» |
| 3 | +6.9 | A | `#s5r2` "→ interest is paid FIRST" (warn) | `pop .5` + `pulse` | «and interest is paid first» |
| 4 | +10.1 | A | `#s5r3` "bank's interest covered · principal barely moves" | `rise .4` | «barely one percent of the balance comes off» |
| 5 | +12.3 | F | **exit** `#s5k`+`#s5r1`+`#s5r2`+`#s5r3` fade .4 | `fade` | clear for the focal |
| 6 | +13.0 | A | `#s5h` "INTEREST ON INTEREST" (warn) | `pop .7` | «Then it's interest on the interest» |
| 7 | +14.7 | A | `#s5snow` "COMPOUNDING — for you when you invest, against you on a card" + `#s5cut` fade | `rise` | «Compounding grows your money when you invest» |
| 8 | +16.0 | F | `#s5f` "US min = 1% + interest · Chase / Capital One agreements · CFPB Reg Z · $35 floor" | `fade` | source line |
| 9 | +17.3 | A | `#s5snow` `pulse` (the against-you snap) | hold | «on a card, it runs against you» |

Simultaneous: momentary 5 during the +12.3 exit (kicker + 3 rows + huge); after exit,
huge + snow + cut-in + foot = **4** ✓. `#s5snow` reads the concept both ways — kept
**neutral ink** (green would argue "compounding is good on a card"). bg `s5.jpg` printed
credit-card statement close-up — **calm, dense scene** (paper, not a phone screen — design
§7), ken IN. cut-in `s5-cut.jpg` snowball rolling downhill on «compounding».

### s6 · ACTION — pay more than the minimum · en6 (clip 15.961s) · photo, ken OUT · tint green .10

DOM: `#s6k .kicker` (exits) · `#s6h .huge` ("PAY **MORE** THAN THE MINIMUM", `.fund` span on **MORE**, focal, exits) · flow `#s6f1`/`#s6ar1`/`#s6f2`/`#s6ar2`/`#s6f3` (arrows CSS-drawn) · `#s6cut` paying-gesture cut-in · `#s6sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The only way out" | `rise` | scene open |
| 2 | +1.8 | A | `#s6h` "PAY **MORE** THAN THE MINIMUM" (fund span on MORE) | `pop .7` | «Pay more than the minimum» |
| 3 | +4.0 | F | `#s6h` breathe (holds «that's the whole game. The minimum is built to keep you paying for years») | hold | surplus → hold |
| 4 | +8.0 | F | **exit** `#s6k`+`#s6h` fade .4 | `fade` | clear for the flow |
| 5 | +8.5 | A | `#s6f1` "MINIMUM" + `#s6cut` fade — **cascade start** | `pop .5` | «The day you add even a little on top» |
| 6 | +9.1 | F | `#s6ar1` "→" | `fade .3` | declared cascade, 0.6s |
| 7 | +9.7 | F | `#s6f2` "+ $20/mo" (fund) | `pop .5` | cascade |
| 8 | +10.3 | F | `#s6ar2` "→" | `fade .3` | cascade (4 items total) |
| 9 | +11.0 | A | `#s6f3` "CUTS YEARS OFF" (fund) | `pop .5` + `pulse` | «years of interest start falling away» |
| 10 | +13.0 | F | **exit** `#s6cut` fade .4 | `fade` | make room for the sub |
| 11 | +13.3 | A | `#s6sub` "Every extra dollar hits the principal directly" | `rise` | «every extra dollar goes straight at the principal» |

**Green sits on MORE and on the escape nodes** (+$20/mo, CUTS YEARS OFF) — **never on
MINIMUM** (corrects script-en's on-screen note; see the colour-correction box above).
`#s6f3` stays **qualitative** ("cuts years off") — no fabricated payoff figure (script
build-handoff #6). Simultaneous peak (+11.0): flow(5) + cut-in = **6** ✓ (kicker/huge
exited; cut-in exits at +13.0 before the sub, so sub-phase = flow(5) + sub = 6). bg
`s6.jpg` US dollar banknotes fanned on a dark desk (object-led, no phone screen — the
script's "phone banking app" bg is replaced, design §7), ken OUT. cut-in `s6-cut.jpg`
hand placing a dollar bill on a table, on «add even a little on top».

### s7 · THE MATH — $6,000 @ ~22%, minimum only (the figures ARE the visual, densest) · en7 (clip 26.567s, longest) · photo (calmest), ken IN · tint red .12

DOM: `#s7k .kicker` (exits) · `#s7setup .sub` (scenario card — 3 internal lines: scenario / APR caveat / min formula; caveat lines fade before the rows) · `#s7r1`/`#s7r2 .billrow` · `#s7r3 .billrow.warn` · `#s7f .foot` · `#s7h .huge.warn` (the punch, focal)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the full math" | `rise` | scene open |
| 2 | +1.6 | A | `#s7setup` line 1 "$6,000 · ~22% APR · minimum only" | `rise` | «A six-thousand-dollar balance at around twenty-two percent» |
| 3 | +4.0 | A | `#s7setup` line 2 "~22% — illustrative, typical range" (internal fade) | `fade` | «around twenty-two percent» |
| 4 | +7.7 | A | `#s7setup` line 3 "minimum = 1% of balance + interest (or $35)" (internal fade) | `fade` | «paying only the minimum» |
| 5 | +9.3 | F | `#s7setup` caveat lines 2–3 fade out; scenario header holds | `fade` | clear the caveats for the rows |
| 6 | +11.5 | A | `#s7r1` "AFTER 1 YEAR — still $5,318 owed" | `rise .4` | «you still owe over five thousand dollars» |
| 7 | +18.5 | A | `#s7r2` "TIME TO CLEAR — 215 MONTHS  (~18 years)" | `rise .4` | «the better part of two decades» |
| 8 | +21.8 | A | `#s7r3` "INTEREST PAID — $9,496" (warn) | `pop .5` + `pulse` | «pay more in interest than you borrowed» |
| 9 | +22.8 | F | `#s7f` "$35-floor model · Fed G.19 / WalletHub 2026 · figures build-calculator locked" | `fade` | source line |
| 10 | +24.0 | F | **exit** `#s7k`+`#s7setup`+`#s7r1`+`#s7r2` fade .4 | `fade` | clear for the punch |
| 11 | +24.3 | A | `#s7h` "$9,496 INTEREST **>** $6,000 BORROWED" (warn) | `pop .7` + `pulse` | «over nine thousand in interest» |

Simultaneous peak (+22.8): kicker + setup-header + r1 + r2 + r3 + foot = **6** ✓ (the two
setup caveat lines faded at +9.3, so setup counts as one header element); punch → r3 + foot
+ huge = 3. r1 holds ~7s across «It's barely moved. Keep paying the minimum…» (surplus →
hold, not a cascade). bg `s7.jpg` dark desk with calculator + notepad — **calmest bg,
densest scene**; the numbers carry it, ken IN, no cut-in. **The integers $5,318 / 215 /
$9,496 are build-calculator output, displayed not spoken** — regenerate from the $35-floor
$ model at build, `en-US` grouping (see Deliberate placeholders).

### s8 · DO THIS TODAY · en8 (clip 15.700s) · photo, ken OUT · tint orange .12

DOM: `#s8stamp .stamp.pop` (exits) · flow `#s8a`/`#s8ar1`/`#s8b`/`#s8ar2`/`#s8c .chip` · `#s8cut` card cut-in (exits) · `#s8rule .decision` · `#s8sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` "DO THIS TODAY" (pop) | `pop .6` + `pulse` | scene-open slam |
| 2 | +2.0 | A | `#s8a` "OPEN YOUR CARD APP" + `#s8cut` fade | `pop .5` | «Open your card's app» |
| 3 | +2.6 | F | `#s8ar1` "→" | `fade .3` | follows its chip |
| 4 | +3.6 | A | `#s8b` "PAY MINIMUM + **$20**" (fund span on +$20) | `pop .5` | «pay the minimum plus at least twenty dollars» |
| 5 | +5.0 | F | **exit** `#s8cut` fade .4 | `fade` | cut-in's job done (keeps peak ≤6) |
| 6 | +5.6 | F | `#s8ar2` "→" | `fade .3` | follows its chip |
| 7 | +6.2 | F | `#s8c` "THIS MONTH" | `pop .5` | completes the flow |
| 8 | +8.0 | F | **exit** `#s8stamp`+flow(`#s8a`..`#s8c`) fade .4 | `fade` | clear for the rule |
| 9 | +8.9 | A | `#s8rule` "Can't buy it in full? Don't carry it on the card." | `rise` | «if you can't buy it in full, don't carry it on the card» |
| 10 | +12.6 | A | `#s8sub` "Debt isn't the enemy — thoughtless debt is." | `rise` | «Debt isn't the enemy. Debt you never thought about is» |

Simultaneous peak (+6.2): stamp + a + ar1 + b + ar2 + c = **6** ✓ (cut-in exited at +5.0).
Green accent on **+$20** (the escape action). bg `s8.jpg` credit card on a pocket
calculator, dark table (object-led, no phone screen — the script's "phone banking app" bg
is replaced, design §7), ken OUT. cut-in `s8-cut.jpg` a hand reaching for a credit card on
«Open your card's app» (object-led; the "app" reference is carried by the chip text, not a
bright phone screen).

### s9 · RECAP + CTA · en9 (clip 15.961s) · photo (calm closer), ken IN · tint green .13

DOM: `#s9k .kicker` (exits) · `#s9a-d .chip` (2×2 rows: a+b / c+d) · `#s9cta .cta` (`▶` CSS-drawn, pop block)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "Straight talk" | `rise` | «So — straight talk» |
| 2 | +1.8 | A | `#s9a` DEBT = RENTED MONEY (ink) | `pop .45` | «Debt is renting money» |
| 3 | +3.4 | A | `#s9b` GOOD GROWS, BAD DRAINS (ink) | `pop .45` | «Good debt grows something; bad debt just drains you» |
| 4 | +7.1 | A | `#s9c` THE MINIMUM = A TRAP (warn) | `pop .45` | «The minimum is a trap» |
| 5 | +8.8 | A | `#s9d` ALWAYS PAY MORE (fund) | `pop .45` | «always pay more than it asks» |
| 6 | +11.0 | F | **exit** `#s9k` fade .4 | `fade` | make room for the cta |
| 7 | +15.4 | A | `#s9cta` "▶ SUBSCRIBE" (pop block) | `pop .6` + `pulse` | «hit subscribe» |

Recap chip char check (≤22): a 19 · b 22 · c 20 · d 15 ✓. Chip colours align to the thesis:
c "THE MINIMUM = A TRAP" **warn**, d "ALWAYS PAY MORE" **fund**; a/b neutral ink. Video
closes on the `.cta` — no logo outro (the script's word "stamp" for SUBSCRIBE is rendered
as the `.cta` block per design §4). Simultaneous: kicker + 4 chips = 5; after exit, 4 chips
+ cta = **5** ✓. bg `s9.jpg` open highway to the horizon at sunrise — **calm object-led
closer** (the road out of the trap; the script's "young man with phone" face+screen query
is replaced, design §7), ken IN.

---

## Timing (measured — en timing.json values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row,
root `data-duration`) — generate all four from `timing.json`, never hand-edit.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | en1 | 17.371 | 18.771 | 0.0 | 0.4 |
| s2 | en2 | 9.848 | 11.248 | 18.771 | 19.171 |
| s3 | en3 | 21.682 | 23.082 | 30.02 | 30.42 |
| s4 | en4 | 24.242 | 25.642 | 53.101 | 53.501 |
| s5 | en5 | 18.651 | 20.051 | 78.743 | 79.143 |
| s6 | en6 | 15.961 | 17.361 | 98.794 | 99.194 |
| s7 | en7 | 26.567 | 27.967 | 116.155 | 116.555 |
| s8 | en8 | 15.700 | 17.100 | 144.122 | 144.522 |
| s9 | en9 | 15.961 | 17.361 | 161.221 | 161.621 |
| **total** | | | | | **178.582** |

Runtime 178.582s = **2:58.6** (≈2:59). Band check (short tier 60–300s) ✓.

## Image slots (→ `assets/img/manifest.json`)

**16 slots — 9 bg (every scene) + 7 cut-ins.** All object-led — no phone screens, no
faces, no ₹/foreign signage. **US market:** $ bills / US card art only.

| slot | query | scene · role |
|---|---|---|
| `s1.jpg` | credit card and unpaid paper bills on a dark wooden desk | s1 · bg |
| `s1-cut.jpg` | printed credit card statement showing minimum payment due, close up | s1 · cut-in «minimum payment» |
| `s2.jpg` | fanned stack of US one dollar bills, flat lay texture, dark | s2 · bg (calmest) |
| `s3.jpg` | hand passing rolled US dollar bills to another hand | s3 · bg |
| `s3-cutA.jpg` | restaurant table with wine glasses and a plated meal, evening | s3 · cut-in «a dinner» |
| `s3-cutB.jpg` | retail sale shopping bags held in one hand | s3 · cut-in «a sale» |
| `s4.jpg` | mortarboard and rolled diploma resting on a pile of textbooks, dark | s4 · bg (calm, densest) |
| `s4-cut.jpg` | several retail shopping bags hanging from a forearm | s4 · cut-in «clothes, gadgets, a vacation» |
| `s5.jpg` | printed credit card statement close up on a dark desk | s5 · bg (calm, dense) |
| `s5-cut.jpg` | large snowball rolling down a steep snowy slope | s5 · cut-in «compounding» |
| `s6.jpg` | US dollar banknotes fanned out on a dark wooden desk | s6 · bg |
| `s6-cut.jpg` | hand placing a US dollar bill down on a table | s6 · cut-in «add even a little on top» |
| `s7.jpg` | dark desk with a calculator, a notepad and a pen | s7 · bg (calmest, densest) |
| `s8.jpg` | a credit card resting on a pocket calculator, dark table | s8 · bg |
| `s8-cut.jpg` | a hand reaching for a credit card lying on a wooden desk | s8 · cut-in «Open your card's app» |
| `s9.jpg` | open highway stretching toward the horizon at sunrise | s9 · bg (calm closer) |

### Image-sourcing note (design §7 — load-bearing)
- **Distinct from the hi cut.** Every query above is reworded and $-market so its
  deterministic top hit differs from the shipped hi manifest (hi shipped `s1`=overdue
  bills+envelopes, `s5`=magnifying-glass document, `s7`=calculator keypad, `s8`=alarm
  clock, `s9`=seedling — none reused). **Highest collision risk** on the non-currency
  concepts — `s4` (cap+books), `s5-cut` (snowball), `s7` (calculator/desk), `s8` (card
  +calculator), `s1-cut` (card statement): **md5 every fetch against the full ledger and
  reword further if a hash already exists anywhere on either channel** (deterministic
  top-hit collision is a verified failure — one `s9.jpg` was byte-identical across three
  shipped projects).
- **Phone-screen bg replaced object-led.** The script's s6 (`hand paying with phone
  banking app`) and s8 (`hand tapping phone banking app`) backgrounds are replaced with
  bill/card/dollar objects — a phone screen is someone else's brand and the brightest
  thing in frame; it has shipped wrong 3× (most recently a legible `MTN-SA` carrier
  string, upside down). Same reason s9's `young man confident with phone` (face **and**
  screen) is replaced with the highway-to-horizon closer (dense recap → calmest bg).
- **Cut-ins re-framed object-led too.** s1 names a card statement → paper statement, not
  a phone screen. s8 «card's app» → a hand reaching for a physical card; the "app" word
  lives in the chip text only.
- **US sweep:** reject any photo with a ₹ note, foreign coin, non-US signage or
  right-hand-drive vehicle (a foreign coin shipped in an earlier en cut). Card art must
  be generic US, no legible issuer brand.
- **Snapshot every fetch before trusting it** — Pixabay's first hit matches the words,
  not the meaning (a falling chart under a "this grows" line, dollars answering a card
  query). Check what the picture is *saying*. **Drop a cut-in rather than fake it** —
  single-photo scenes read fine (the hi cut shipped 12 slots, several cut-ins dropped);
  the **bg is never dropped** (photo-free retired).

## `-en` divergence from the hi master skeleton (one row per scene — mandatory)

Element IDs are ported **verbatim** (`s1r2`, `s3h`, `s4good/s4bad`, `s5r1`, `s6f1–3`,
`s7h`, `s8a–c`, `s9cta`) so fixes travel between cuts. Every scene diverges — the two
load-bearing ones are **s5** (mechanism) and **s7** (hero math). Global: all offsets are
re-derived from the en `timing.json` (Brian 15 c/s vs Harsh 12.5 c/s → different clip
lengths → different scene durations and cue placements).

| scene | diverges how | why |
|---|---|---|
| s1 | Split figures **$170 / $110 / $60** replace ₹2,583 / ₹1,667 / ₹916; interest-reveal re-anchored to +13.1 (en1 17.371s) and the ≤15s trap-proof re-verified for Brian's faster delivery. | US hero balance $6,000 @ ~22% (not a rupee conversion); en1 clip is 3.4s shorter than hi h1. |
| s2 | Clip **9.848s vs hi 13.740s** → chip anchors compressed to +1.2…+8.4 (still ≥0.8, not a cascade); bg US dollar-bills texture replaces the ₹500 flat-lay. | Brian is faster **and** the English line is shorter; currency + market swap. |
| s3 | bg/currency US (rolled dollar bills handed over); cut-ins sourced US-neutral; offsets re-derived. *(Lightest divergence — concept identical; still real: currency bg + timing.)* | English rewrite tracks the hi concept 1:1; only the market props + measured timing change. |
| s4 | US register — tags **A DEGREE / VACATIONS** replace EDUCATION / HOLIDAYS; stamp **"CARD BALANCE = WORST"** vs "CARD REVOLVE = WORST"; bg reworded (mortarboard+diploma) for a distinct hash. | US idiom ("vacation", "card balance" not "revolve"); hash-distinctness from the hi cap+books bg. |
| s5 | **Core market divergence** — the rule block reads **"MINIMUM = 1% of balance + interest"** and "interest is paid FIRST", replacing India's **"5% of balance"**; foot cites **Chase / Capital One agreements · CFPB Reg Z · $35 floor** instead of RBI / issuer MITC · ₹100 floor. | The US "1% + interest" minimum is *different math* from India's "5% of total due" — the whole reason this is a rewrite, not a translation (facts-staging Claim $-2). |
| s6 | Flow node **"+ $20/mo"** vs "+ ₹1,000/mo"; bg US dollar banknotes; **COLOUR CORRECTION** — the `--fund` span is on **MORE**, not MINIMUM (script-en's on-screen note put green on MINIMUM). | US action step ($20); colour-safety carries the hi audit fix (green = escape, never the trap). |
| s7 | Full US hero math — **$6,000 / ~22% / $5,318 after 1 yr / 215 mo / $9,496 interest** vs ₹50,000 / ~40% / ₹40,045 / 208 mo / ₹88,614; **added** APR-caveat + min-formula lines folded into `#s7setup` (en has two extra clarifiers, longest clip 26.567s); foot cites **Fed G.19 / WalletHub 2026** vs Federal Bank / ICICI MITC. | US $ model (build-calculator locked) + US sources; en7 carries more spoken content than hi h7. |
| s8 | Chip **"OPEN YOUR CARD APP"** (VO «card's app») vs "OPEN YOUR CARD BILL"; **"+ $20"** vs "+ ₹1,000"; cut-in re-anchored to «Open your card's app» (a hand reaching for a card). | US phrasing ("app"); US action step; the concrete opening-beat noun shifts. |
| s9 | bg **US highway-to-horizon at sunrise** replaces country-road-at-dawn; recap chips English register ("RENTED MONEY", "GOOD GROWS, BAD DRAINS"); `#s9k` copy "Straight talk". | US road/idiom; hash-distinctness from the hi closer; VO opens «straight talk». |

## Deliberate placeholders (must be real before publish)
- **Anchored cue offsets are char-interpolated intent** — refine with faster-whisper word
  timings at build. The one that must not drift: s1 `#s1r2` interest reveal ≤15s (advisory above).
- **s7 on-screen integers $5,318 / 215 months / $9,496** = build-calculator output
  (B₀=$6,000, monthly i=0.0183333, P=max(0.01·B + i·B, $35), stop at B≤0), **not** the
  storyboard's transcribed values. Regenerate at build; `en-US` grouping. The VO stays a
  round range ("over five thousand", "the better part of two decades", "over nine thousand")
  regardless of the exact integers (script build-handoff #5).
- s4 column items render as card `.tag`s, not `.chip` pills (the ≤6 layout divergence noted in s4).
- s6 `#s6f3` "CUTS YEARS OFF" stays qualitative — no `+$20 → saves $X` figure unless the
  build calculator computes it (P = max(0.01·B + i·B, $35) + $20); do not hand-type it.

## Sign-off
- [x] Colour semantics table filled and consistent with the script (red = trap, never MINIMUM green; s6 green-on-MINIMUM script note corrected)
- [x] Every number traced to a sourced line (see script-en.md fact trace, $ SET)
- [ ] No image hash reused from any prior video on either channel, and none from the hi cut (check at fetch — see Image-sourcing note)
- [x] Every scene carries a full-bleed bg photo (photo-free retired; 9 bg + 7 cut-ins)
- [x] s1 interest-reveal ≤15s advisory recorded for build (fin-voice en1 flag)
- [x] Divergence list has one reason per scene (s5 mechanism + s7 hero-math load-bearing — not a translation in a layout costume)
- [ ] Creator approved (Gate ②) — date: __
