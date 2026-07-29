---
summary: Gate ② storyboard SPEC for «Pay Yourself First» Hindi/India cut — 9 scenes, scene DOM + GSAP cue tables built on measured timing.json values, image slots, 2 photo-free scenes (s2, s7). This is the MASTER skeleton the -en pass ports.
updated: 2026-07-28
source: videos/pay-yourself-first/script-hi.md + assets/voice/timing.json (measured) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]]
---

# STORYBOARD — «Pay Yourself First» · hi cut

**Project:** `vault/videos/pay-yourself-first/src/hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @cashguruguides ₹ · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **2:58.9** (timing.json total 178.896s) · **VO:** Harsh `HTUuC7…`
**Rate:** Hindi 12.5 chars/s · **Grade:** dark blockframe · **Locale:** `en-IN` (`₹1,44,000`, never `₹144,000`)

## Colour semantics for THIS video (derived from the thesis)

Thesis: **paying yourself first is protection, not sacrifice — the auto-transfer
is the hero move; the leak is what's-left-saving.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green | the auto-moved money, the flipped formula, the protected path | saving-first is the hero, so the saved rupee is always the good outcome |
| `--warn` red | what's-left-saving — the drain to the 20th, ₹7-of-₹100, the struck-out old formula | the leak is the villain, never the spending categories themselves |
| `--target` amber | the rule under examination — "PAY YOURSELF **FIRST**", the 5% starting step | it's the decision the viewer is being asked to make today |
| `--pop` orange | call to action — DO THIS TODAY stamp, subscribe block | (fixed) |

The test: if the auto-transfer or the 5% step ever renders red, or the empty-account
drain renders green, the video argues against its own script.

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together.
- Reveal spacing ≥0.8s except declared cascades (≤5 items @ 0.6–0.7s). Something on screen by +0.5s.
- ≤6 elements visible at once — scenes that would exceed it declare **exits** below.
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- `ken` alternates across photo scenes: **s1 in · s3 out · s4 in · s5 out · s6 in · s8 out · s9 in**.
- **Photo-free scenes: s2 + s7** (2 of 9 ≤ cap from `photo_free_scene_ratio` 0.23). Both get `drift()` — no static frame beyond ~2s. s7 is the hero-math scene and deliberately gets the calmest background in the video (clean panel, slow drift): densest scene, calmest bed.
- No phone-screen photos, no faces fighting the type — all queries below are object-led.
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger — no reuse from any prior video on either channel.**

## Cue classes

`A` = **anchored** — offset scales with the clip, lands on the noted Hindi word.
Offsets below are char-interpolated design intent (`0.4 + chars_before/total × clip`);
the build refines them with faster-whisper word timings.
`F` = **fixed** — cascades, arrows, stamp slams — constant regardless of clip length.
Surplus time from a longer clip goes into **holds (breathe/drift), never cascades.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured
`timing.json` values (see Timing table) — never re-derived.

### s1 · HOOK — empty by the 20th · h1 (clip 14.341s) · photo ×3 crossfade, ken IN · tint red .12

DOM: `#s1k .kicker` · `#s1q .huge` (warn span on `20TH?`) · `#s1cal .track2+.ticks` (20 ticks, draining) · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "Be honest" | `rise` | scene open |
| 2 | +1.9 | A | `#s1q` "EMPTY BY THE **20TH?**" | `pop .7` | «बीस तारीख़» |
| 3 | +4.1 | A | `#s1cal` calendar bar `1 → 20` | `fade .5` then `fill` **reversed** (drains) over 2.8s | «अकाउंट खाली» |
| 4 | +7.4 | A | `#s1stamp` EVERY MONTH | `pop .6` + `pulse` | «सबसे आख़िर में करते हैं» |
| 5 | +10.6 | A | `#s1q` warn span re-`pulse` + `breathe #s1q 3.1s` | hold | «सौ साल पुराना वो नियम» — hold carries surplus |

Backgrounds crossfade under the block: `s1-a.jpg` (+0.0) → `s1-b.jpg` (+5.0 `fade`, F) → `s1-c.jpg` (+10.0 `fade`, F). Ken IN continues across all three.

### s2 · ROADMAP · h2 (clip 10.527s) · **photo-free → `drift()`** · no tint

DOM: `#s2k .kicker` · `#s2a-d .chip` (2×2 rows: a+b / c+d) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +1.5 | A | `#s2a` SAVE FIRST, NOT LAST | `pop .45` | «आख़िर में बचाने और पहले बचाने» |
| 3 | +3.8 | A | `#s2b` WHY WILLPOWER LOSES | `pop .45` | «विलपावर क्यों हार जाती है» |
| 4 | +5.7 | A | `#s2c` PAYDAY AUTO-TRANSFER | `pop .45` | «ऑटो-ट्रांसफ़र» |
| 5 | +8.2 | A | `#s2d` WHAT IT'S FOR | `pop .45` | «किस काम के लिए» |
| 6 | +9.8 | F | `#s2sub` "Works even at 5%" | `rise` | end of clip |

Chips are anchored to their spoken beat (gaps ≥0.8s) — this is **not** a cascade.
`drift()` on the panel from 0 for the full 11.9s.

### s3 · CONCEPT — flip the formula · h3 (clip 23.719s) · photo, ken OUT · tint green .10

DOM: `#s3k .kicker` · `#s3old .head2` (struck, warn) · `#s3new .huge.fund` (focal) · `#s3stamp .stamp.fund`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "Most people's formula" | `rise` | scene open |
| 2 | +3.0 | A | `#s3old` INCOME − EXPENSES = SAVINGS | `pop .6` | «कमाई, माइनस ख़र्चा, बराबर बचत» |
| 3 | +12.1 | A | `#s3old` strike-through draws (`scaleX` 0→1) + text → `--warn` | `fill .5` + `tl.to color .3` | «कुछ बचता ही नहीं» |
| 4 | +16.4 | A | `#s3new` INCOME − SAVINGS = EXPENSES | `pop .7` + `breathe 4.5s` | «कमाई, माइनस बचत, बराबर ख़र्चा» |
| 5 | +22.0 | A | `#s3stamp` FLIP THE FORMULA | `pop .55` + `pulse` | «बचे हुए पैसों में महीना चलाइए» |

Long gaps (+3.0 → +12.1) are held by ken drift + `breathe` on `#s3old` at +6.0 (F, 5.0s) — no static frame >2s.

### s4 · RULE — pay yourself first · h4 (clip 14.655s) · photo, ken IN · tint amber .12

DOM: `#s4k .kicker` · `#s4h .huge` (amber span on `FIRST`, focal) · `#s4book .chip.target` · `#s4q .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "A 100-year-old rule" | `rise` | scene open |
| 2 | +2.3 | A | `#s4h` PAY YOURSELF **FIRST** | `pop .7` | «पे योरसेल्फ़ फ़र्स्ट» |
| 3 | +3.4 | A | `#s4h` amber span `pulse` + `breathe 4.6s` | hold | «अपने आप को पैसे दीजिए» |
| 4 | +9.1 | A | `#s4book` THE RICHEST MAN IN BABYLON · 1926 | `rise .5` | «किताब» |
| 5 | +11.6 | A | `#s4q` "A part of all you earn is yours to keep" | `rise` | «जो कमाते हो» |

### s5 · AUDIT — why willpower loses · h5 (clip 20.323s) · photo, ken OUT · tint red .12

DOM: `#s5k .kicker` · `#s5a-c .chip.warn` · `#s5stat .huge` (76px override — on ladder; warn span on `₹7 SAVED`, focal) · `#s5f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "Why willpower loses" | `rise` | scene open |
| 2 | +7.7 | A | `#s5a` SALE | `pop .45` | «सेल» — cascade start anchors here |
| 3 | +8.35 | F | `#s5b` FOOD APPS | `pop .45` | declared cascade, 0.65s |
| 4 | +9.0 | F | `#s5c` EMI | `pop .45` | declared cascade, 0.65s |
| 5 | +14.7 | A | `#s5stat` ₹100 EARNED → | `rise` | «हर सौ रुपये में से» |
| 6 | +15.9 | A | `#s5stat` warn span **₹7 SAVED** | `pop .6` + `pulse` | «सात रुपये» |
| 7 | +17.5 | F | `#s5f` "RBI FY25 · net household financial savings, 7% of GNDI" | `rise` | after the stat lands |

Gap +0.4 → +7.7 held by ken + `breathe #s5k 4.0s` at +2.0 (F). Simultaneous max: kicker + 3 chips + stat + foot = **6** ✓.

### s6 · ACTION — payday-morning auto-transfer · h6 (clip 20.323s) · photo, ken IN · tint green .10

DOM: `#s6k .kicker` · `#s6t1-2 .chip` · flow row `#s6f1-3 .head2` + `#s6ar1-2 .arrow` (CSS-drawn) · `#s6sub .sub.fund`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The fix — automation" | `rise` | scene open |
| 2 | +3.8 | A | `#s6t1` STANDING INSTRUCTION | `pop .5` | «स्टैंडिंग इंस्ट्रक्शन» |
| 3 | +5.7 | A | `#s6t2` UPI AUTOPAY | `pop .5` | «यूपीआई ऑटोपे» |
| 4 | +8.2 | F | **exit:** `#s6k #s6t1 #s6t2` fade out .4 | `fade` | make room for the flow |
| 5 | +8.4 | A | `#s6f1` SALARY IN | `pop .5` | «सैलरी आने के अगले ही मिनट» — cascade start anchors here |
| 6 | +9.0 | F | `#s6ar1` → | `fade .3` | declared cascade, 0.6s |
| 7 | +9.6 | F | `#s6f2` AUTO-TRANSFER | `pop .5` | cascade |
| 8 | +10.2 | F | `#s6ar2` → | `fade .3` | cascade |
| 9 | +10.8 | F | `#s6f3` SAVED BY 9 AM (`--fund`) | `pop .5` | cascade (5 items total) |
| 10 | +14.8 | A | `#s6f3` `pulse` + `breathe` row 3.0s | hold | «नींद खुलने से पहले बचत हो चुकी होगी» |
| 11 | +17.3 | A | `#s6sub` "Money you don't see, you don't spend" | `rise` | «जो पैसा दिखता नहीं» |

Simultaneous max after exits: 3 flow blocks + 2 arrows + sub = **6** ✓.

### s7 · THE MATH — the signature counter · h7 (clip 25.913s) · **photo-free → `drift()`, calmest background in the video** · no tint

The counter IS the visual. Counts ₹0 → ₹1,44,000 in **12 stepped increments**
(= 12 months), `Intl.NumberFormat("en-IN")`, tabular-nums, `.track2` filling
12 ticks in parallel. Focal: `#s7c .counter` (96px).

DOM: `#s7k .kicker` · `#s7sub .sub` · `#s7head .head2` · `#s7c .counter.fund` + `#s7track .track2/.fill2/.ticks` · `#s7lad` ladder card (`.billrow`-style, target border) · `#s7f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the math" | `rise` | scene open |
| 2 | +3.3 | A | `#s7sub` "Higher-income example — ₹60–70k in-hand" | `rise` | «साठ-सत्तर हज़ार» |
| 3 | +7.7 | A | `#s7head` ₹12,000 · on the 1st · every month | `rise` | «बारह हज़ार अपने आप» |
| 4 | +10.1 | A | `#s7c` `₹0` + `#s7track` | `fade .5` | «बारह महीने बाद» |
| 5 | +10.6 | A | `countUp #s7c 0→1,44,000` stepped ×12 over 3.2s + `fill #s7fill 3.2s` | — | lands just after «एक लाख चौवालीस हज़ार» |
| 6 | +14.8 | A | **exit** `#s7sub` fade .4 · `#s7lad` "Avg salary ₹24,000 → 5% = ₹1,200/mo" | `rise .5` | «सैलरी औसत है — क़रीब चौबीस हज़ार» |
| 7 | +21.4 | A | `#s7lad` year line "= ₹14,400/yr" | `pop .5` + `pulse` | «चौदह हज़ार चार सौ» |
| 8 | +23.5 | F | `#s7f` "PLFS 2025 · avg salaried earnings (men) ₹24,217/mo" | `rise` | closing beat — «अभी आप शून्य बचा रहे हैं» rides the held counter |

`.ticks` at `calc(100% / 12 - 2px)` — 12 months. **Do not round the counter's
en-IN grouping**: it must read `₹1,44,000`, never `₹144,000`.
Simultaneous max after exit: kicker + head + counter + track + ladder + foot = **6** ✓.

### s8 · DO THIS TODAY · h8 (clip 17.319s) · photo, ken OUT · tint orange .12

DOM: `#s8stamp .stamp.pop` · `#s8a-c .chip` · `#s8ar1-2 .arrow` · `#s8sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` DO THIS TODAY | `pop .6` + `pulse` | scene-open slam |
| 2 | +1.9 | A | `#s8a` OPEN BANK APP | `pop .5` | «बैंक ऐप खोलिए» |
| 3 | +2.5 | F | `#s8ar1` → | `fade .3` | follows its chip |
| 4 | +5.6 | A | `#s8b` SET THE AUTO-TRANSFER | `pop .5` | «स्टैंडिंग इंस्ट्रक्शन सेट» |
| 5 | +6.2 | F | `#s8ar2` → | `fade .3` | follows its chip |
| 6 | +7.8 | A | `#s8c` SALARY DATE, EVEN 5% (`.target` border) | `pop .5` + `pulse` | «पाँच परसेंट से ही सही» |
| 7 | +12.6 | F | **exit:** `#s8stamp` fade .4 | `fade` | job done; room for the payoff |
| 8 | +13.4 | A | `#s8sub` "First stop: emergency fund → then your goals" | `rise` | «पहले इमरजेंसी फंड» |

Simultaneous max after exit: 3 chips + 2 arrows + sub = **6** ✓.

### s9 · RECAP + CTA · h9 (clip 19.174s) · photo, ken IN · tint green .13

DOM: `#s9k .kicker` · `#s9a-d .chip.fund` (2×2 rows: a+b / c+d) · `#s9sub .sub` · `#s9cta .cta`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "The simple version" | `rise` | scene open |
| 2 | +2.1 | A | `#s9a` SAVE FIRST | `pop .45` | «बचत पहले» |
| 3 | +5.1 | A | `#s9b` TRUST THE SYSTEM | `pop .45` | «सिस्टम पर भरोसा» |
| 4 | +7.8 | A | `#s9c` AUTOMATE ON PAYDAY | `pop .45` | «स्टैंडिंग इंस्ट्रक्शन सेट कीजिए» |
| 5 | +9.8 | A | `#s9d` START AT 5% | `pop .45` | «पाँच परसेंट से ही» |
| 6 | +13.3 | A | **exit** `#s9k` fade .4 · `#s9sub` "Next month, the 20th looks different" | `rise` | «बीस तारीख़ को अकाउंट खाली नहीं» |
| 7 | +18.3 | A | `#s9cta` ▶ SUBSCRIBE (`--pop` block, `▶` CSS-drawn) | `pop .6` + `pulse` | «सब्सक्राइब कीजिए» |

Video closes on the `.cta` — no logo outro. Simultaneous max: 4 chips + sub + cta = **6** ✓.

---

## Timing (measured — timing.json values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row,
root `data-duration`) — generate all four from `timing.json`, never hand-edit.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | h1 | 14.341 | 15.741 | 0.0 | 0.4 |
| s2 | h2 | 10.527 | 11.927 | 15.741 | 16.141 |
| s3 | h3 | 23.719 | 25.119 | 27.669 | 28.069 |
| s4 | h4 | 14.655 | 16.055 | 52.788 | 53.188 |
| s5 | h5 | 20.323 | 21.723 | 68.842 | 69.242 |
| s6 | h6 | 20.323 | 21.723 | 90.566 | 90.966 |
| s7 | h7 | 25.913 | 27.313 | 112.289 | 112.689 |
| s8 | h8 | 17.319 | 18.719 | 139.602 | 140.002 |
| s9 | h9 | 19.174 | 20.574 | 158.322 | 158.722 |
| **total** | | | | | **178.896** |

## Image slots (→ `assets/img/manifest.json`)

All object-led — no phone screens, no faces. 9 slots, 7 photo scenes.

| slot | query | scene |
|---|---|---|
| `s1-a.jpg` | empty leather wallet on table dark | s1 |
| `s1-b.jpg` | wall calendar dates close up | s1 |
| `s1-c.jpg` | indian rupee coins scattered table | s1 |
| `s3.jpg` | salary payslip desk calculator india | s3 |
| `s4.jpg` | old book pages warm lamp light | s4 |
| `s5.jpg` | crowded indian market shopping bags | s5 |
| `s6.jpg` | sunrise alarm clock bedside morning | s6 |
| `s8.jpg` | hand putting coin into piggy bank dark | s8 |
| `s9.jpg` | sunrise over city skyline india | s9 |

Script suggested phone-screen queries for s5/s6/s8 (`food delivery app phone hand`,
`upi payment phone screen`, `hand tapping phone banking app`) — **replaced**: the
design doc bans phone-screen backgrounds (shipped wrong 3× already). s9 face query
replaced with a calm object-led closer (dense recap scene → calm background).
Snapshot every fetch before trusting it; md5 against the asset ledger, no reuse.

## The -en pass

This is the **master skeleton**. The -en storyboard ports these scene shapes and
element IDs verbatim (`s1q`, `s7c`, `s6f1-3`, …) so fixes travel between cuts, and
lists its divergences (US hero-math from fin-script-en, $ figures, US institutions
replacing RBI/PLFS/UPI beats) with a reason per scene. Zero divergences = red flag.

## Deliberate placeholders (must be real before publish)
- Anchored cue offsets are char-interpolated intent — refine with faster-whisper word timings at build.
- `#s7lad` exact avg-salary figure on screen: use the sourced ₹24,217 (foot) vs rounded ₹24,000 (card) exactly as script-hi.md specifies.

## Sign-off
- [x] Colour semantics table filled and consistent with the script
- [x] Every number traced to a sourced line (see script-hi.md fact trace)
- [ ] No image hash reused from any prior video on either channel (check at fetch)
- [x] Photo-free scenes ≤2 (s2, s7), each with `drift`
- [ ] Creator approved (Gate ②) — date: __
