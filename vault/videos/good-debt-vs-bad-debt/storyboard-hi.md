---
summary: Gate ② storyboard SPEC for «Good Debt vs Bad Debt — the minimum-payment trap» hi cut — 9 scenes, scene DOM + GSAP cue tables built on measured timing.json values, keyword-matched bg + cut-ins on EVERY scene (photo-free retired). This is the MASTER skeleton the -en pass ports.
updated: 2026-07-28
source: videos/good-debt-vs-bad-debt/script-hi.md (audit-PASS) + assets/voice/timing.json (measured, total 195.17s) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]] + audit-hi.md check 3 + logs/fin-voice-hi-1.md s1 flag
---

# STORYBOARD — «Good Debt vs Bad Debt» · hi cut

**Project:** `studio/videos/good-debt-vs-bad-debt-hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @cashguruguides ₹ · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **3:15.2** (timing.json total 195.17s) · **VO:** Harsh `HTUuC7…`
**Rate:** Hindi 12.5 chars/s · **Grade:** dark blockframe · **Locale:** `en-IN` (`₹88,614`, never `₹88614`)

## Colour semantics for THIS video (derived from the thesis — mandatory)

Thesis: **the minimum payment is a trap that keeps you renting money for 17 years;
good debt buys something that grows, bad debt just spends — the escape is paying
more than the minimum.** On a credit-card video red MUST be the interest trap.

| Token | This video means | Because |
|---|---|---|
| `--fund` green | good debt · the escape (paying MORE than the minimum) · money kept off the principal | the constructive path — anything that grows value or cuts the debt |
| `--warn` red | the interest / minimum-payment **trap** · bad debt · the card revolve · interest > amount borrowed | red is the trap being exposed, never a neutral baseline |
| `--target` amber | the thing under examination — the card, the concept "debt = renting money", the decision | it's what the viewer is being asked to weigh |
| `--pop` orange | call to action — DO THIS TODAY stamp, subscribe block | (fixed) |

The test: if **MINIMUM** ever renders green, or **paying more / good debt** renders
red, or the ₹88,614 interest reads green, the video argues against its own script.
(Audit non-blocking note applied: the s6 green accent sits on **MORE**, the escape —
never on **MINIMUM**, which is the trap.)

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together — where a scene has two focal moments (huge → bill), the first **exits** before the second.
- Reveal spacing ≥0.8s except declared cascades (≤5 items @ 0.6–0.7s). Something on screen by +0.5s (every scene opens at +0.40).
- ≤6 elements visible at once — scenes that would exceed it declare **exits** below.
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- **Every scene carries a full-bleed bg photo** (creator rule 2026-07-28 — `photo_free_scene_ratio` 0; photo-free retired). Every scene therefore gets `ken`; `ken` **alternates**: **s1 in · s2 out · s3 in · s4 out · s5 in · s6 out · s7 in · s8 out · s9 in**. No static frame beyond ~2s (ken always running under every scene).
- **Densest scenes get the CALMEST bg** (quiet texture reading of the keyword, never no image): s4 (classifier) → books, s5 (rule+huge+snow) → bank statement, s7 (the math) → calculator/ledger.
- **Keyword-matched imagery:** when the VO names a concrete thing it appears — as the bg or as a cut-in timed to its word (see per-scene tables + the Image slots table).
- **No phone-screen photos as bg, no faces fighting the type** — see the Image-sourcing note; the script's phone-banking bg (s6/s8) and s9 face query are replaced object-led.
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger — no reuse from any prior video on either channel** (Pixabay's top hit is deterministic; different queries collapse to the same file).

## Cue classes

`A` = **anchored** — offset scales with the clip, lands on the noted Hindi word.
Offsets below are char-interpolated design intent (`0.4 + chars_before/total × clip`);
the build refines them with faster-whisper word timings.
`F` = **fixed** — cascades, arrows, stamp slams — constant regardless of clip length.
Surplus time from a longer clip goes into **holds (breathe/ken), never cascades.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured
`timing.json` values (see Timing table) — never re-derived.

### s1 · HOOK — the minimum is a trap (month-1 split IS the focal shock) · h1 (clip 20.741s) · photo, ken IN · tint red .12

DOM: `#s1k .kicker` · `#s1q .huge.warn` ("MINIMUM PAYMENT", exits) · `#s1cut` card-statement cut-in · `#s1bill .bill` → `#s1r1 .billrow` · `#s1r2 .billrow.warn` · `#s1r3 .billrow` · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "The most dangerous words on a credit card" | `rise` | scene open |
| 2 | +3.7 | A | `#s1q` "MINIMUM PAYMENT" + `#s1cut` fade | `pop .7` | «मिनिमम पेमेंट» |
| 3 | +5.2 | F | `#s1q` breathe 4.0s (holds across «एक जाल है… पचास हज़ार के बिल») | hold | surplus → hold |
| 4 | +9.8 | F | **exit** `#s1q` + `#s1cut` fade .4 | `fade` | clear for the bill (focal handoff) |
| 5 | +10.6 | A | `#s1r1` "YOU PAY  ₹2,583" | `rise .4` | «पचीस सौ तिरासी… भरते हैं» |
| 6 | **+13.1** | A | `#s1r2` "→ INTEREST  ₹1,667" (warn) | `pop .5` + `pulse` | «सोलह सौ सरसठ सिर्फ़ ब्याज» — **the trap-proof, ≤15s (see advisory)** |
| 7 | +14.6 | F | `#s1r2` breathe 2.2s (the interest shock holds) | hold | — |
| 8 | +15.9 | A | `#s1r3` "→ OFF THE DEBT  ₹916" | `rise .4` | «बस नौ सौ रुपये» |
| 9 | +17.5 | F | `#s1stamp` "IT'S A TRAP" | `pop .6` + `pulse` | verdict slam after the split |

**s1 build advisory (audit check 3 + fin-voice s1 flag — TIGHTEST in the video).**
h1 is 20.74s; the interest clause «सोलह सौ सरसठ सिर्फ़ ब्याज» lands ~13.0–14.5s in.
`#s1r2` (INTEREST ₹1,667 — the trap-proof) must reveal **on** that word and be fully
readable **≤15s**; it is char-interpolated here at +13.1. The principal row `#s1r3`
(₹916) is synced to its own spoken word «नौ सौ रुपये» (~+15.9), **not gated to clip
end** (fin-voice: "reveal the split as the numbers are spoken"). The trap is proven
by r1+r2 ≤15s; r3 confirms the ~₹900 on its word. **At build: ffprobe/whisper-verify
s1; if the interest clause measures past 15s, tighten r1/r2 forward on the interest
word — do not push r3 earlier than spoken.** Simultaneous peak = kicker + 3 rows +
stamp = **5** ✓ (huge + cut-in exited at +9.8).

bg `s1.jpg` credit card + paper bills on dark table (ken IN). cut-in `s1-cut.jpg` on «मिनिमम पेमेंट».

### s2 · ROADMAP — four things · h2 (clip 13.740s) · photo (calm rest beat), ken OUT · tint — (transparent wash)

DOM: `#s2k .kicker` · `#s2a-d .chip` (2×2 rows: a+b / c+d) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +2.9 | A | `#s2a` WHAT DEBT REALLY IS | `pop .45` | «कर्ज़ असल में क्या है» |
| 3 | +4.9 | A | `#s2b` GOOD vs BAD DEBT | `pop .45` | «अच्छा और बुरा कर्ज़ का फ़र्क़» |
| 4 | +7.5 | A | `#s2c` HOW THE MINIMUM WORKS | `pop .45` | «मिनिमम पेमेंट अंदर से कैसे चलता है» |
| 5 | +10.0 | A | `#s2d` COMPOUNDS AGAINST YOU | `pop .45` | «ब्याज कैसे आपके ख़िलाफ़ बढ़ता है» |
| 6 | +12.8 | A | `#s2sub` "Then one thing to do today" | `rise` | «आज करने वाला एक काम» |

Chips are anchored to their spoken beat (gaps 2.0–2.6s ≥0.8) — this is **not** a cascade.
Chip d = "COMPOUNDS AGAINST YOU" (21 chars ✓ — audit-corrected from the 23-char original).
Chips carry **neutral ink** borders (roadmap topics, not colour claims). Simultaneous:
kicker + 4 chips + sub = **6** ✓. bg `s2.jpg` current ₹500 notes flat-lay texture — the
calmest image in the video (roadmap rest beat), slow ken OUT. No cut-in (abstract).

### s3 · CONCEPT — debt is renting money · h3 (clip 22.596s) · photo, ken IN · tint green .10

DOM: `#s3k .kicker` · `#s3h .huge` ("DEBT =" + `.accent` amber span "RENTING MONEY", focal, exits) · `#s3sub .sub` · `#s3good .row.fund` · `#s3bad .row.warn` · `#s3cutA`/`#s3cutB` cut-ins

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "First — what debt really is" | `rise` | scene open |
| 2 | +2.7 | A | `#s3h` "DEBT = **RENTING MONEY**" (amber span) | `pop .7` | «कर्ज़ यानी पैसा किराए पर» |
| 3 | +5.8 | A | `#s3sub` "Interest is the rent" | `rise` | «वो उस पैसे का किराया है» |
| 4 | +7.0 | F | `#s3h` breathe 3.5s (holds across «किराया देना हमेशा ग़लत नहीं») | hold | surplus → hold |
| 5 | +12.4 | F | **exit** `#s3h` + `#s3sub` fade .4 | `fade` | clear for the contrast |
| 6 | +12.8 | A | `#s3good` "TOOL THAT EARNS → rent worth it" (fund) | `pop .5` | «किराया वसूल» |
| 7 | +15.8 | A | `#s3bad` "DINNER, SALE BUY → rent on a ghost" (warn) + `#s3cutA` fade | `pop .5` | «बाहर के खाने» |
| 8 | +17.6 | A | `#s3cutB` crossfade over `#s3cutA` | `fade .5` | «सेल की ख़रीदारी» |
| 9 | +20.7 | A | `#s3bad` `pulse` + breathe 2.0s | hold | «चीज़ कल ख़त्म, किराया महीनों चलेगा» |

Simultaneous peak (+17.6): kicker + good + bad + cut-in = **4** ✓ (huge/sub exited; the two
cut-ins crossfade so only one is up at a time). bg `s3.jpg` rolled rupee notes handed over
(renting money), ken IN. cut-ins on the concrete **bad** things the VO names (dinner, sale) —
the good side is abstract («औज़ार»), correctly bg-only.

### s4 · RULE — good debt vs bad debt (two-column classifier, densest) · h4 (clip 26.044s, longest) · photo (calm), ken OUT · tint amber .12

DOM: `#s4k .kicker` (exits) · `#s4good .col.fund` (header + tags EDUCATION/A SKILL/A BUSINESS, popEach inside) · `#s4bad .col.warn` (header + tags CLOTHES/GADGETS/HOLIDAYS) · `#s4cut` shopping-bags cut-in · `#s4stamp .stamp.warn` · `#s4f .foot`

> **Layout note (≤6 elements).** A literal 3+3 chip classifier is 2 labels + 6 chips = 8
> visible → over cap. Each column is therefore **one `.col` card** whose three items
> reveal with a micro `popEach` inside the single entry (counts as 1 element, not a
> cascade). This is a deliberate divergence from the script's word "chips"; the
> good/bad **role colours are preserved** on the card borders.

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "The rule" | `rise` | scene open |
| 2 | +4.0 | A | `#s4good` GOOD DEBT · value grows (+ tags popEach) | `pop .6` | «अच्छा कर्ज़… पढ़ाई, हुनर, अपना काम-धंधा» |
| 3 | +6.0 | F | `#s4good` breathe 4.0s (holds «वो चीज़ ख़ुद आपके लिए कमाती है») | hold | surplus → hold |
| 4 | +13.4 | A | `#s4bad` BAD DEBT · just spending (+ tags popEach) | `pop .6` | «बुरा कर्ज़ सिर्फ़ ख़र्च के लिए» |
| 5 | +15.5 | A | `#s4cut` shopping-bags cut-in | `fade .5` | «कपड़े, गैजेट, छुट्टी» |
| 6 | +17.8 | F | **exit** `#s4k` fade .4 | `fade` | kicker's job done |
| 7 | +18.1 | A | `#s4stamp` "CARD REVOLVE = WORST" (warn) + breathe 3.0s | `pop .6` + `pulse` | «सबसे बुरा, कार्ड का बक़ाया» |
| 8 | +23.3 | A | `#s4f` "Even good debt is only 'good' if the return beats the interest" | `rise` | «कर्ज़ तभी अच्छा, जब फ़ायदा ब्याज से ज़्यादा हो» |

Simultaneous peak (+23.3): good card + bad card + cut-in + stamp + foot = **5** ✓ (kicker exited).
bg `s4.jpg` graduation cap on books — **calmest bg, densest scene**, ken OUT. The honest
caveat foot is load-bearing (audit): good debt only wins if the return beats the interest.

### s5 · AUDIT — how the minimum works + compounds against you (dense) · h5 (clip 22.570s) · photo (calm), ken IN · tint red .12

DOM: `#s5k .kicker` (exits) · `#s5r1 .billrow` · `#s5r2 .billrow.warn` · `#s5r3 .billrow` (rule block, exit) · `#s5h .huge.warn` ("INTEREST ON INTEREST", focal) · `#s5snow .sub` + `#s5cut` snowball cut-in · `#s5f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "How the minimum actually works" | `rise` | scene open |
| 2 | +4.5 | A | `#s5r1` "MINIMUM = 5% of balance" | `rise .4` | «बक़ाया का पाँच परसेंट माँगता है» |
| 3 | +7.2 | A | `#s5r2` "→ pays INTEREST first" (warn) | `pop .5` + `pulse` | «वो रक़म पहले पूरा ब्याज भरती है» |
| 4 | +10.6 | A | `#s5r3` "your principal barely moves" | `rise .4` | «आपका मूल कर्ज़ मुश्किल से घटता है» |
| 5 | +13.1 | F | **exit** `#s5k`+`#s5r1`+`#s5r2`+`#s5r3` fade .4 | `fade` | clear for the focal |
| 6 | +13.5 | A | `#s5h` "INTEREST ON INTEREST" (warn) | `pop .7` | «ऊपर से लगता है ब्याज पर ब्याज» |
| 7 | +16.7 | A | `#s5snow` "COMPOUNDING — for you investing · against you on a card" + `#s5cut` fade | `rise` | «निवेश में यही चक्रवृद्धि» |
| 8 | +18.5 | F | `#s5f` "RBI + issuer MITC 2026 · min must cover 100% of interest · ₹100 floor" | `fade` | source line |
| 9 | +20.3 | A | `#s5snow` `pulse` (the against-you snap) | hold | «कार्ड पर यही आपके ख़िलाफ़ दौड़ती है» |

Simultaneous: momentary 5 during the +13.1 exit (kicker+3 rows+huge); after exit, huge +
snow + cut-in + foot = **4** ✓. `#s5snow` reads the concept both ways — kept **neutral ink**
(green would argue "compounding is good on a card"). bg `s5.jpg` bank-statement close-up —
**calm, dense scene**, ken IN. cut-in snowball rolling downhill on «चक्रवृद्धि».

### s6 · ACTION — pay more than the minimum · h6 (clip 18.939s) · photo, ken OUT · tint green .10

DOM: `#s6k .kicker` (exits) · `#s6h .huge` ("PAY MORE THAN THE MINIMUM", `.fund` span on **MORE**, focal, exits) · flow `#s6f1`/`#s6ar1`/`#s6f2`/`#s6ar2`/`#s6f3` (arrows CSS-drawn) · `#s6cut` paying-gesture cut-in · `#s6sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The only way out" | `rise` | scene open |
| 2 | +3.0 | A | `#s6h` "PAY **MORE** THAN THE MINIMUM" (fund span on MORE) | `pop .7` | «मिनिमम से ज़्यादा भरिए» |
| 3 | +5.5 | F | `#s6h` breathe 3.5s (holds «मिनिमम बना ही इसलिए है कि आप सालों फँसे रहें») | hold | surplus → hold |
| 4 | +9.8 | F | **exit** `#s6k`+`#s6h` fade .4 | `fade` | clear for the flow |
| 5 | +10.2 | A | `#s6f1` "MINIMUM" + `#s6cut` fade — **cascade start** | `pop .5` | «हज़ार रुपये ऊपर भरना शुरू करते हैं» |
| 6 | +10.8 | F | `#s6ar1` "→" | `fade .3` | declared cascade, 0.6s |
| 7 | +11.4 | F | `#s6f2` "+ ₹1,000/mo" (fund) | `pop .5` | cascade |
| 8 | +12.0 | F | `#s6ar2` "→" | `fade .3` | cascade (4 items total) |
| 9 | +13.4 | A | `#s6f3` "CUTS YEARS OFF THE TRAP" (fund) | `pop .5` + `pulse` | «सालों का ब्याज कटने लगता है» |
| 10 | +16.5 | F | **exit** `#s6cut` fade .4 | `fade` | make room for the sub |
| 11 | +17.1 | A | `#s6sub` "Every extra rupee hits the principal directly" | `rise` | «हर बढ़ा हुआ रुपया सीधे मूल कर्ज़ पर चोट» |

Green sits on **MORE** and on the escape nodes (+₹1,000, CUTS YEARS OFF) — **never on MINIMUM**
(audit-preferred fix). `#s6f3` stays **qualitative** ("cuts years off") — no fabricated payoff
figure (script build-handoff #6). Simultaneous peak (+17.1): flow(5) + sub = **6** ✓. bg
`s6.jpg` rupee banknotes fanned on desk (object-led, no phone screen), ken OUT. cut-in a
hand-paying-with-a-rupee-note gesture on «भरना शुरू करते हैं».

### s7 · THE MATH — ₹50,000 @ ~40%, 5% min (the figures ARE the visual, densest) · h7 (clip 25.156s) · photo (calmest), ken IN · tint red .12

DOM: `#s7k .kicker` (exits) · `#s7setup .sub` (scenario header) · `#s7r1`/`#s7r2 .billrow` · `#s7r3 .billrow.warn` · `#s7f .foot` · `#s7h .huge.warn` (the punch, focal)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the full math" | `rise` | scene open |
| 2 | +2.4 | A | `#s7setup` "₹50,000 · ~40% APR (illustrative range) · 5% minimum only" | `rise` | «पचास हज़ार… चालीस परसेंट… पाँच परसेंट मिनिमम» |
| 3 | +5.0 | F | `#s7setup` breathe 4.0s (holds «भारत में आम बात») | hold | surplus → hold |
| 4 | +10.5 | A | `#s7r1` "AFTER 1 YEAR — still ₹40,045 owed" | `rise .4` | «क़रीब चालीस हज़ार बाक़ी» |
| 5 | +15.0 | A | `#s7r2` "TIME TO CLEAR — 208 MONTHS · 17+ years" | `rise .4` | «सत्रह साल से भी ज़्यादा» |
| 6 | +18.5 | A | `#s7r3` "INTEREST PAID — ₹88,614" (warn) | `pop .5` + `pulse` | «क़रीब नब्बे हज़ार रुपये» |
| 7 | +19.8 | F | `#s7f` "₹100-floor model · Federal Bank/ICICI MITC 2026 · build-calculator locked" | `fade` | source line |
| 8 | +22.6 | F | **exit** `#s7k`+`#s7setup`+`#s7r1`+`#s7r2` fade .4 | `fade` | clear for the punch |
| 9 | +23.0 | A | `#s7h` "₹88,614 INTEREST **>** ₹50,000 BORROWED" (warn) | `pop .7` + `pulse` | «जितना उधार लिया, उससे भी ज़्यादा» |

Simultaneous peak (+19.8): kicker + setup + r1 + r2 + r3 + foot = **6** ✓; punch → r3 + foot +
huge = 3. bg `s7.jpg` calculator + ledger on dark desk — **calmest bg, densest scene**; the
numbers carry it, ken IN, no cut-in. **The integers ₹40,045 / 208 / ₹88,614 are
build-calculator output, displayed not spoken** — they must equal the ₹100-floor model run
at build, `en-IN` grouping (see Deliberate placeholders).

### s8 · DO THIS TODAY · h8 (clip 17.319s) · photo, ken OUT · tint orange .12

DOM: `#s8stamp .stamp.pop` (exits) · flow `#s8a`/`#s8ar1`/`#s8b`/`#s8ar2`/`#s8c .chip` · `#s8cut` card-bill cut-in · `#s8rule .decision` · `#s8sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` "DO THIS TODAY" (pop) | `pop .6` + `pulse` | scene-open slam |
| 2 | +2.5 | A | `#s8a` "OPEN YOUR CARD BILL" + `#s8cut` fade | `pop .5` | «इसी महीने कार्ड का बिल खोलिए» |
| 3 | +3.1 | F | `#s8ar1` "→" | `fade .3` | follows its chip |
| 4 | +5.0 | F | **exit** `#s8cut` fade .4 | `fade` | cut-in's job done |
| 5 | +5.6 | A | `#s8b` "PAY MINIMUM + **₹1,000**" (fund span on +₹1,000) | `pop .5` | «हज़ार रुपये ज़्यादा भरिए» |
| 6 | +6.2 | F | `#s8ar2` "→" | `fade .3` | follows its chip |
| 7 | +6.8 | F | `#s8c` "THIS MONTH" | `pop .5` | completes the flow |
| 8 | +10.5 | F | **exit** `#s8stamp`+flow(`#s8a`..`#s8c`) fade .4 | `fade` | clear for the rule |
| 9 | +11.1 | A | `#s8rule` "Can't buy it in full? Don't revolve it on the card." | `rise` | «कार्ड पर घुमाइए मत» |
| 10 | +15.1 | A | `#s8sub` "Debt isn't bad — thoughtless debt is." | `rise` | «बिना सोचे लिया कर्ज़ बुरा है» |

Simultaneous peak (+6.8): stamp + a + ar1 + b + ar2 + c = **6** ✓ (cut-in exited at +5.0).
Green accent on **+₹1,000** (the escape action). bg `s8.jpg` credit card + calculator on
dark desk (object-led, no phone screen), ken OUT. cut-in an opened paper card bill on «कार्ड का बिल».

### s9 · RECAP + CTA · h9 (clip 15.464s) · photo (calm closer), ken IN · tint green .13

DOM: `#s9k .kicker` (exits) · `#s9a-d .chip` (2×2 rows: a+b / c+d) · `#s9cta .cta` (`▶` CSS-drawn, pop block)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "The simple version" | `rise` | scene open |
| 2 | +2.7 | A | `#s9a` DEBT = RENTED MONEY (ink) | `pop .45` | «कर्ज़ यानी पैसा किराए पर» |
| 3 | +5.8 | A | `#s9b` GOOD GROWS, BAD DRAINS (ink) | `pop .45` | «अच्छा कर्ज़ कुछ बढ़ाता है, बुरा सिर्फ़ ख़र्च» |
| 4 | +8.9 | A | `#s9c` MINIMUM = A TRAP (warn) | `pop .45` | «मिनिमम पेमेंट एक जाल है» |
| 5 | +10.9 | A | `#s9d` ALWAYS PAY MORE (fund) | `pop .45` | «हमेशा उससे ज़्यादा भरिए» |
| 6 | +13.0 | F | **exit** `#s9k` fade .4 | `fade` | make room for the cta |
| 7 | +14.6 | A | `#s9cta` "▶ SUBSCRIBE" (pop block) | `pop .6` + `pulse` | «सब्सक्राइब कीजिए» |

Recap chip char check (≤22): a 18 · b 20 · c 15 · d 15 ✓. Chip colours align to the thesis:
c "MINIMUM = A TRAP" **warn**, d "ALWAYS PAY MORE" **fund**; a/b neutral ink. Video closes on
the `.cta` — no logo outro. Simultaneous: kicker + 4 chips = 5; after exit, 4 chips + cta = **5** ✓.
bg `s9.jpg` open country road to the horizon at dawn — **calm object-led closer** (the road out
of the trap; the script's face+phone query is replaced, see Image-sourcing note), ken IN.

---

## Timing (measured — timing.json values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row,
root `data-duration`) — generate all four from `timing.json`, never hand-edit.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | h1 | 20.741 | 22.141 | 0.0 | 0.4 |
| s2 | h2 | 13.740 | 15.140 | 22.141 | 22.541 |
| s3 | h3 | 22.596 | 23.996 | 37.282 | 37.682 |
| s4 | h4 | 26.044 | 27.444 | 61.278 | 61.678 |
| s5 | h5 | 22.570 | 23.970 | 88.722 | 89.122 |
| s6 | h6 | 18.939 | 20.339 | 112.691 | 113.091 |
| s7 | h7 | 25.156 | 26.556 | 133.030 | 133.430 |
| s8 | h8 | 17.319 | 18.719 | 159.586 | 159.986 |
| s9 | h9 | 15.464 | 16.864 | 178.305 | 178.705 |
| **total** | | | | | **195.17** |

## Image slots (→ `assets/img/manifest.json`)

**16 slots — 9 bg (every scene) + 7 cut-ins.** All object-led — no phone screens, no faces.

| slot | query | scene · role |
|---|---|---|
| `s1.jpg` | credit card and paper bills on dark wooden table | s1 · bg |
| `s1-cut.jpg` | credit card statement showing minimum payment due close up | s1 · cut-in «मिनिमम पेमेंट» |
| `s2.jpg` | indian rupee 500 notes flat lay texture dark | s2 · bg (calmest) |
| `s3.jpg` | rolled rupee notes handed from one hand to another | s3 · bg |
| `s3-cutA.jpg` | restaurant dinner table with plates dark | s3 · cut-in «बाहर के खाने» |
| `s3-cutB.jpg` | shopping sale bags held in hand | s3 · cut-in «सेल की ख़रीदारी» |
| `s4.jpg` | graduation cap on stack of books dark | s4 · bg (calm, densest) |
| `s4-cut.jpg` | shopping bags hanging on arm | s4 · cut-in «कपड़े, गैजेट, छुट्टी» |
| `s5.jpg` | printed bank statement close up dark | s5 · bg (calm, dense) |
| `s5-cut.jpg` | snowball rolling down snowy hill | s5 · cut-in «चक्रवृद्धि» |
| `s6.jpg` | rupee banknotes fanned on dark wooden desk | s6 · bg |
| `s6-cut.jpg` | hand placing a rupee note on a table | s6 · cut-in «भरना शुरू करते हैं» |
| `s7.jpg` | dark desk with calculator and ledger book | s7 · bg (calmest, densest) |
| `s8.jpg` | credit card and calculator on dark wooden table | s8 · bg |
| `s8-cut.jpg` | hand opening a paper credit card bill | s8 · cut-in «कार्ड का बिल» |
| `s9.jpg` | empty open country road to the horizon at dawn | s9 · bg (calm closer) |

### Image-sourcing note (design §7 — load-bearing)
- **Phone-screen bg replaced.** The script's s6 (`hand paying bill on phone banking app`)
  and s8 (`hand tapping phone banking app`) backgrounds are **replaced object-led** — a
  phone screen is someone else's brand and the brightest thing in frame; it has shipped
  wrong **3×** (most recently a legible `MTN-SA` carrier string, upside down). Same reason
  s9's `young indian man confident with phone` (face **and** screen) is replaced with a
  calm road-to-horizon closer (dense recap scene → calmest bg).
- **Cut-ins re-framed object-led too.** s1/s6/s8 name digital/paper things — sourced as
  paper statements and hand-with-object gestures, no bright screen, no legible brand.
- **₹500 notes must be the current post-2016 design** (demonetised notes have shipped before).
- **Snapshot every fetch before trusting it** — Pixabay's first hit matches the words, not the
  meaning. **md5 every asset against the ledger; refuse any hash used in any prior video on
  either channel** (deterministic top-hit collision is a verified failure mode).

## The -en pass

This is the **master skeleton.** The `-en` storyboard ports these scene shapes and
element IDs **verbatim** (`s1r2`, `s3h`, `s4good/s4bad`, `s6f1-3`, `s7h`, …) so fixes
travel between cuts, and must emit an explicit **divergence list with a reason per
scene** — expect: US hero-math from `fin-script-en` ($ balance / APR / payoff, ~15
c/s Brian rate → different clip lengths → different offsets), `$` currency, US
institution/source foots replacing RBI + Federal Bank/ICICI MITC, and any beat whose
concrete noun changes market (₹500-note textures → US equivalents). **Zero divergences
= a translation in a layout costume; the audit will flag it.**

## Deliberate placeholders (must be real before publish)
- **Anchored cue offsets are char-interpolated intent** — refine with faster-whisper word
  timings at build. The one that must not drift: s1 `#s1r2` interest reveal ≤15s (advisory above).
- **s7 on-screen integers ₹40,045 / 208 months / ₹88,614** = build-calculator output
  (B₀=₹50,000, i=0.033333/mo, P=max(5%·statement, ₹100), stop at B≤0), **not** the
  storyboard's transcribed values. Regenerate at build; `en-IN` grouping.
- s4 column items render as card `.tag`s, not `.chip` pills (the ≤6 layout divergence noted in s4).

## Sign-off
- [x] Colour semantics table filled and consistent with the script (red = trap, never MINIMUM green)
- [x] Every number traced to a sourced line (see script-hi.md fact trace + audit-hi.md)
- [ ] No image hash reused from any prior video on either channel (check at fetch)
- [x] Every scene carries a full-bleed bg photo (photo-free retired; 9 bg + 7 cut-ins)
- [x] s1 interest-reveal ≤15s advisory recorded for build (audit check 3)
- [ ] Creator approved (Gate ②) — date: __
