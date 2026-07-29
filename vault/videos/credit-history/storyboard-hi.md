---
summary: Gate ② storyboard SPEC for «Your Credit History — the invisible record» hi cut — 9 scenes, scene DOM + GSAP cue tables built on the measured timing.json (total 177.642s), keyword-matched bg + cut-ins on EVERY scene (photo-free retired). s5's 36-cell grid is the hero animation. This is the MASTER skeleton the -en pass ports.
updated: 2026-07-29
source: videos/credit-history/script-hi.md (audit-PASS, incl. the 3 audit edits) + studio/videos/credit-history-hi/assets/voice/timing.json (measured, total 177.642s) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]] + audit-hi.md checks 3/8 + logs/fin-voice-hi-1.md s1 advisory
---

# STORYBOARD — «Your Credit History» · hi cut

**Project:** `studio/videos/credit-history-hi/` · **Script:** `script-hi.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @cashguruguides ₹ · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **2:57.6** (timing.json total 177.642s) · **VO:** Harsh `HTUuC7…`
**Rate:** Hindi 12.5 chars/s (measured 12.61) · **Grade:** dark blockframe
**Locale:** `en-IN` — `₹30,00,000`, never `₹3,000,000`

## Colour semantics for THIS video (derived from the thesis — mandatory)

Thesis: **an invisible record decides whether you get a loan and at what price.
On-time EMIs build it; one miss shows for 36 months; a low score costs lakhs on
the loan you haven't taken yet. The fix is auto-pay and pulling your report.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green | the **on-time payment** · the clean report · the top score band (700+/750+) · auto-pay and the actions that build the record | everything that *builds* the record — this video's whole constructive path is behavioural, not an instrument |
| `--warn` red | the **missed EMI and the price it charges** — the one red cell in the 36-month grid, the below-700 band, the extra ₹/month and the extra interest | red is the miss and its bill, exposed — never a card, never a lender, never "debt" |
| `--target` amber | the **score / the report under examination** — the 300–900 scale, the three-digit number, the thing the viewer is being asked to look at | it is the object of study, not a verdict |
| `--pop` orange | call to action — the DO THIS TODAY stamp, the subscribe block | (fixed) |

The test: if the **red grid cell** ever renders green, or **ON-TIME EMIs / AUTO-PAY /
the 700+ band** render red, or the **score itself** renders red as though the score
were the villain, the video argues against its own script.

> **Anti-drift note (contract §1).** Do **not** import
> `good-debt-vs-bad-debt`'s semantics, where red = "the minimum payment". Here a
> minimum-only payment is a *caveat*, not the trap being exposed — so s6's
> "not the minimum" renders **`--muted`**, not `--warn`. Reusing another video's
> red is exactly the drift this table exists to stop.

## Global guardrails (from the design system)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together — where a scene has two focal moments (s3 head2s → scale, s5 grid → huge, s7 rows → punch), the first **exits** or is sequenced so they never compete.
- Reveal spacing ≥0.8s except declared cascades (≤5 items @ 0.6–0.7s). Something on screen by +0.5s (every scene opens at **+0.40**).
- ≤6 elements visible at once — scenes that would exceed it declare **exits** below.
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- **Every scene carries a full-bleed bg photo** (creator rule 2026-07-28; `photo_free_scene_ratio` 0). Every scene therefore gets `ken`; `ken` **alternates**: **s1 in · s2 out · s3 in · s4 out · s5 in · s6 out · s7 in · s8 out · s9 in**. No static frame beyond ~2s.
- **Densest scenes get the CALMEST bg** (quiet texture reading of the keyword, never no image): s4 (4-row ladder) → open diary, s5 (grid + counter + huge) → stamp & ink pad, s7 (the math) → blueprint texture.
- **Keyword-matched imagery:** where the VO names a concrete thing it appears — as the bg or as a cut-in timed to its word (per-scene tables + the Image slots table).
- **No phone-screen photos as bg, no faces fighting the type** (§7 — shipped wrong 3×). The script already bars the phone bg on s6 and closes s9 on a doorway, not a person.
- Type steps down the ladder (`290 · 240 · 112 · 96 · 54 · 50 · 46 · 44 · 40 · 32 · 30 · 28 · 26`) — never interpolated to fit.
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger — no reuse from any prior video on either channel.**

## Cue classes

`A` = **anchored** — offset scales with the clip, lands on the noted Hindi word.
Offsets below are char-interpolated design intent (`0.4 + chars_before/total × clip`),
computed against the **measured** clip length; the build refines them with
faster-whisper word timings (script handoff #7 — char interpolation drifts worst on Hindi).
`F` = **fixed** — cascades, arrows, stamp slams, exits — constant regardless of clip length.
Surplus time from a longer clip goes into **holds (breathe/ken), never cascades.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured
`timing.json` values (see Timing table) — never re-derived.

### s1 · HOOK — the report you've never seen · h1 (clip 17.162s) · photo, ken IN · tint red .12

DOM: `#s1k .kicker` (exits) · `#s1q .huge.target` ("YOUR CREDIT REPORT", the focal) · `#s1cutA` closed-file cut-in · `#s1cutB` loan-form cut-in · `#s1d1`/`#s1d2`/`#s1d3 .decision` · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "A file you've never seen" | `rise` | scene open |
| 2 | +3.2 | A | `#s1q` "YOUR CREDIT REPORT" (amber) + `#s1cutA` fade | `pop .7` | «…कभी देखी नहीं» (char 35) — **the visual payoff, +3.2s** |
| 3 | +5.0 | A | `#s1d1` "LOAN?  → it decides" | `rise .4` | «आपको लोन मिलेगा या नहीं» (char 57) |
| 4 | +7.1 | A | `#s1d2` "INTEREST?  → it decides" | `rise .4` | «और किस ब्याज पर» (char 83) |
| 5 | +8.5 | A | `#s1cutB` crossfade over `#s1cutA` | `fade .5` | «बैंक आपसे मिलने से पहले» (char 100) |
| 6 | +10.8 | A | `#s1d3` "YOU'VE SEEN IT?  → probably never" (muted verdict) | `rise .4` | «उसे पढ़ चुका होता है» (char 128) |
| 7 | +14.2 | A | `#s1q` `pulse` + breathe 2.0s | hold | «क्रेडिट रिपोर्ट» (char 170) — the VO catches up to the screen |
| 8 | +14.6 | F | **exit** `#s1k` + `#s1cutB` fade .4 | `fade` | clear for the stamp |
| 9 | +15.5 | A | `#s1stamp` "EVERY MISSED EMI IS IN IT" (warn) | `pop .6` + `pulse` | «हर चूकी हुई किश्त लिखी है» (char 186) |

**s1 build advisory (audit check 3 + fin-voice-hi-1 — the video's one timing gate).**
The audit requires the hook's promise paid off **≤15s**. Two things pay it off and
they are deliberately decoupled:

- **On screen:** `#s1q` "YOUR CREDIT REPORT" reveals at **+3.2** — the payoff is
  visual and lands 11.8s inside the gate regardless of delivery rate. This is the
  structural difference from `good-debt`'s s1, where the payoff *was* the number.
- **In VO:** the naming «नाम है — क्रेडिट रिपोर्ट» completes at char 170/212 = 80.2%
  → **≈+14.2** (fin-voice measured h1 at 17.162s, 1.2% slower than the rate estimate;
  its own figure was ≈14.0). **Margin ≈0.8s.**

**At build: whisper-verify the naming word in h1.** If it measures past 15s the
audit's prescribed trim is the «पर वो तय करती है कि» clause — **never the naming**,
and never `#s1q`, which is already early. Cue 7 (`pulse`) is a re-sync, not the payoff;
it may slide without breaking the gate.

Simultaneous peak (+10.8): kicker + huge + cutB + d1 + d2 + d3 = **6** ✓ (cutA crossfaded
out). After +14.6 exit: huge + 3 decisions + stamp = **5** ✓. One focal (`.huge`); the
`.decision` rows are 40px and the `.stamp` 44px — no competition.
bg `s1.jpg` archive file shelves (ken IN). cut-ins on the two concrete things the VO
names: the unopened file «एक रिपोर्ट» and the bank «बैंक».

### s2 · ROADMAP — four things · h2 (clip 11.598s, shortest) · photo (calmest rest beat), ken OUT · tint amber .10

DOM: `#s2k .kicker` · `#s2a`–`#s2d .chip` (2×2 rows: a+b / c+d, neutral ink borders) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +1.3 | A | `#s2a` WHAT THE REPORT IS | `pop .45` | «ये रिपोर्ट है क्या» (char 12) |
| 3 | +2.8 | A | `#s2b` WHAT BUILDS IT | `pop .45` | «इसे बनाता क्या है» (char 32) |
| 4 | +4.2 | A | `#s2c` WHAT DESTROYS IT | `pop .45` | «बिगाड़ता क्या है» (char 51) |
| 5 | +5.5 | A | `#s2d` WHY IT MATTERS EARLY | `pop .45` | «ज़रूरत पड़ने से बहुत पहले» (char 69) |
| 6 | +9.5 | A | `#s2sub` "Then two things to do today" | `rise` | «आज करने वाले दो काम» (char 122) |

Chips are anchored to their spoken beat (gaps 0.9–1.5s, all ≥0.8) — this is **not**
a cascade. Chip char check (≤22): a 18 · b 14 · c 16 · d 20 ✓. Borders are **neutral
ink** — roadmap topics are not colour claims, and colouring "WHAT DESTROYS IT" red
here would spend the red before s5 earns it. Simultaneous: kicker + 4 chips + sub =
**6** ✓. bg `s2.jpg` tied document bundles — the calmest image in the video, slow
ken OUT. **No cut-in:** every noun in h2 is abstract ("four things", "the report"),
and the bg already *is* the report as texture — a cut-in here would be faked (§7
"drop a cut-in rather than fake it"). The scene still carries a photo.

### s3 · CONCEPT — what the report and the score are · h3 (clip 20.193s) · photo, ken IN · tint amber .12

DOM: `#s3k .kicker` (exits) · `#s3e1`–`#s3e3 .chip` (cascade, exit) · `#s3rec .sub` (exits) · `#s3ha`/`#s3hb .head2` (exit) · `#s3cut` printed-number cut-in (exits) · `#s3scale` (**the focal**: `.mega`@240 "300" ├ `.track2` ┤ `.mega`@240 "900") · `#s3g1`/`#s3g2 .collabel.fund` · `#s3f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "First — what it actually is" | `rise` | scene open |
| 2 | +1.5 | F | `#s3e1` EVERY LOAN — **cascade start** | `pop .45` | «आपका हर लोन» (char 11) |
| 3 | +2.2 | F | `#s3e2` EVERY CREDIT CARD | `pop .45` | declared cascade, 0.7s |
| 4 | +2.9 | F | `#s3e3` EVERY EMI | `pop .45` | cascade (3 items ≤5 ✓) |
| 5 | +5.4 | A | `#s3rec` "→ recorded at the credit bureau" | `rise` | «क्रेडिट ब्यूरो के पास दर्ज» (char 59) |
| 6 | +7.4 | F | **exit** `#s3e1`–`#s3e3` fade .4 | `fade` | enumeration's job done |
| 7 | +7.8 | A | `#s3ha` "THE REPORT = the record" | `rise` | «इसी रिकॉर्ड का नाम है क्रेडिट रिपोर्ट» (char 87) |
| 8 | +11.1 | A | `#s3hb` "THE SCORE = the summary" | `rise` | «उसका निचोड़ है» (char 126) |
| 9 | +12.3 | F | **exit** `#s3k` + `#s3rec` fade .4 | `fade` | clear for the focal |
| 10 | +12.7 | A | `#s3cut` three-digit-number cut-in | `fade .5` | «तीन अंकों का एक नंबर» (char 144) |
| 11 | +14.6 | A | `#s3scale` "300 ├──────┤ 900" (mega@240, **the focal**) + `fill` on the amber track | `pop .7` + `fill .8` | «सिबिल स्कोर, तीन सौ से नौ सौ» (char 167) |
| 12 | +15.6 | F | **exit** `#s3ha` + `#s3hb` + `#s3cut` fade .4 | `fade` | one focal only |
| 13 | +17.8 | F | `#s3g1` "700+ = generally good" (fund) — **cascade start** | `pop .5` | «सात सौ के ऊपर अच्छा» (char 204) |
| 14 | +18.4 | F | `#s3g2` "750+ = best pricing" (fund) | `pop .5` | declared cascade, 0.6s (2 items) |
| 15 | +19.4 | F | `#s3f` "TransUnion CIBIL — score range 300–900" | `fade` | source line |

**`#s3g2` reads `750+ = best pricing`, not `750–800`** — audit edit 3. A closed
750–800 range reads as *excluding* 800+, which is the band every re-checked lender
card actually prices best. Do not restore the range at build.
`.mega` is dropped to **240** (a value already on the ladder, as the shipped pair did)
so two 3-digit numerals plus the track fit inside `110px 150px` padding. Do not
interpolate to a value off the ladder — restructure instead.
Colour: the track is **amber** (the score under examination), the 700+/750+ markers
**fund green** (the good bands). Neither "300" nor "900" is coloured — an endpoint is
not a verdict. Simultaneous peaks: +5.4 → kicker + 3 chips + rec = **5** ✓;
+19.4 → scale + g1 + g2 + foot = **4** ✓. bg `s3.jpg` ruled ledger columns, ken IN.

### s4 · RULE — what builds it (4-row ladder, dense) · h4 (clip 19.487s) · photo (calm), ken OUT · tint green .10

DOM: `#s4k .kicker` (exits) · `#s4r1`–`#s4r4 .billrow.fund` (rank numeral `.head2` + label + gloss) · `#s4cut` credit-cards cut-in (exits) · `#s4f .foot.muted`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "What builds it" | `rise` | scene open |
| 2 | +4.2 | A | `#s4r1` "1  PAYMENT HISTORY — every EMI, on time" (fund) | `rise .4` + `pulse` | «पेमेंट हिस्ट्री» (char 48) |
| 3 | +7.5 | A | `#s4r2` "2  CREDIT UTILISATION — how much of the limit you use" (fund) | `rise .4` | «दूसरी है क्रेडिट यूटिलाइज़ेशन» (char 89) |
| 4 | +10.0 | A | `#s4cut` two-credit-cards cut-in | `fade .5` | «लिमिट का कितना हिस्सा» (char 121) |
| 5 | +12.6 | F | **exit** `#s4k` + `#s4cut` fade .4 | `fade` | make room, stay ≤6 |
| 6 | +13.5 | A | `#s4r3` "3  AGE OF CREDIT — how old your accounts are" (fund) | `rise .4` | «फिर आपका क्रेडिट कितना पुराना है» (char 165) |
| 7 | +17.3 | A | `#s4r4` "4  NEW ENQUIRIES — how often you apply" (fund) | `rise .4` | «आप कितनी बार नया लोन माँगते हैं» (char 213) |
| 8 | +18.6 | F | `#s4f` "CIBIL names these factors — it publishes no percentage weights. Also counted: credit mix." | `fade` | the guard-rail |

> **Deliberate divergence from the script's on-screen note.** The script writes the
> four ranked rows as a *"cascade, 0.6s apart"*. **They are anchored instead.** The VO
> spaces the four factors across 13.1s of the clip; a 0.6s cascade would dump all four
> inside 1.8s and leave ~15s with no new motion, which fails §5.2 (no static hold >2s)
> and throws away four perfectly good word anchors. Gaps are 3.3 / 6.0 / 3.8s — all
> ≥0.8, so **no cascade is declared for this scene.** (Same call `good-debt`'s s2 made
> on its chips.) The 6.0s r2→r3 window is filled by the `#s4cut` reveal at +10.0.

**No percentage weight appears anywhere on this scene** — no 35/30/15, no ring chart,
no proportional bar. The rows are ranked by position only, and `#s4f` says so out
loud (script's RED-FLAG guard + audit's "correctly absent" finding). A bar whose
*lengths* differ would smuggle FICO's weights back in visually — rows are equal width.
All four rows are **fund green**: these are the things that build the record.
Simultaneous peaks: +10.0 → kicker + r1 + r2 + cut = **4** ✓; +18.6 → r1–r4 + foot =
**5** ✓. bg `s4.jpg` open desk diary — **calmest bg, densest scene**, ken OUT.
Cut-in re-anchored from «क्रेडिट यूटिलाइज़ेशन» (which collides with r2's own cue) to
the explanation «लिमिट का कितना हिस्सा» 2.5s later — same beat, legal spacing.

### s5 · AUDIT — what destroys it · THE HERO SCENE · h5 (clip 19.540s) · photo (calm), ken IN · tint red .13

DOM: `#s5k .kicker` (exits) · `#s5grid` (**the hero focal**: 3 rows × 12 = 36 `.cell`, fund fill left→right, one `.cell.warn`) · `#s5ctr .counter.warn` ("MONTH 1 → MONTH 36") · `#s5cut` torn-calendar cut-in (exits) · `#s5f .foot` · `#s5q .huge.warn` (the verdict)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "What destroys it" | `rise` | scene open |
| 2 | +2.0 | A | `#s5grid` frame in (36 empty cells) | `pop .6` | «आपकी रिपोर्ट में पिछले छत्तीस महीनों» (char 21) |
| 3 | +2.6→+17.0 | F | `#s5grid` cells fill **fund green** left→right, continuous stagger | `fill`, staggered | the month-by-month record — **runs the whole scene** |
| 4 | **+8.0** | A | one `.cell` **slams `--warn` red** and stays lit; green fill keeps going past it | `pop .35` + `pulse` | «एक चूकी हुई किश्त» (char 98) — script's "~40% of the clip" = 7.8s ✓ |
| 5 | +9.0 | F | `#s5ctr` "MONTH 1 → MONTH 36" begins under the grid | `countUp` (runs to +17.0) | the red cell's age |
| 6 | +10.2 | A | `#s5cut` torn-calendar cut-in | `fade .5` | «वहाँ पूरे तीन साल दिखती है» (char 126) |
| 7 | +11.6 | A | `#s5f` "CIBIL — 36-month month-by-month payment history; \"will always be a part of your credit history\"" | `fade` | «सिबिल के अपने शब्दों में» (char 144) |
| 8 | +13.9 | A | red `.cell` `pulse` (it does not clear) | hold | «वो हमेशा … हिस्सा रहेगी» (char 174) |
| 9 | +15.5 | F | **exit** `#s5k` + `#s5cut` fade .4 | `fade` | clear for the verdict |
| 10 | +17.6 | A | `#s5q` "ONE MISS = 36 MONTHS" (warn) | `pop .7` | «एक चूक, और गिनकर छत्तीस महीने» (char 222) |
| 11 | +18.9 | A | `#s5q` `pulse` + breathe to scene end | hold | «छत्तीस महीने» (char 239) |

**The hero animation (script handoff #6, creator brief).** 3 × 12 cells. Green fills
left→right across the whole scene; the red slam at +8.0 is a **fixed-state change,
not a hold** — the cell stays lit while the remaining cells keep filling *past* it,
which is the argument: the record moves on, the miss doesn't. **The grid must be in
motion at every point in the scene** (§5.2). Surplus from a longer measured clip goes
into the fill stagger and the counter, never into a faster cascade.

**Focal handling (audit check 8):** the grid is the focal; `#s5q` lands **sequentially**
at +17.6, after the grid's fill completes at ~+17.0 — they do not compete, and there is
no `.mega` on this scene. Colour is the whole point here: on-time cells **fund green**,
the miss **warn red**, the counter **warn** (it counts what the miss costs). If the red
cell ever renders green the scene inverts its own thesis.

**`#s5f` quote-marks residual (audit, non-blocking).** The quoted CIBIL string is
substantively confirmed by two source-domain passes but never surfaced as an exact
global phrase match (cibil.com is crawl-hostile) and the two passes differ by one
article. The VO already paraphrases («सिबिल के अपने शब्दों में»). **If the build wants
zero quotation risk, drop the quote marks and render it as reported speech** — the
substance survives. Kept as the audit left it; flagged in Placeholders.

Simultaneous peaks: +11.6 → kicker + grid + counter + cut + foot = **5** ✓;
+17.6 → grid + counter + foot + huge = **4** ✓. bg `s5.jpg` red stamp + ink pad on a
desk — calm and thematic (the mark on the record), the grid carries the scene. ken IN.

### s6 · ACTION — auto-pay every due date · h6 (clip 19.226s) · photo, ken OUT · tint green .10

DOM: `#s6k .kicker` (exits) · `#s6h .huge.fund` ("AUTO-PAY" + inline `.sub` "every due date", the focal, exits) · `#s6flow` (**one** `.row` element, 3 nodes revealed by internal `popEach`, `→` CSS-drawn, exits) · `#s6cut` passbook cut-in (exits) · `#s6stamp .stamp.fund` (exits) · `#s6u .sub` · `#s6u2 .decision`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The fix" | `rise` | scene open |
| 2 | +2.1 | A | `#s6h` "AUTO-PAY" + "every due date" (fund) | `pop .7` | «ऑटो-पे» (char 20) |
| 3 | +3.6 | F | `#s6flow` node 1 "EVERY CARD" — **popEach cascade start** | `pop .5` | «हर कार्ड» (char 28) |
| 4 | +4.3 | F | node 2 "EVERY LOAN" | `pop .5` | declared cascade, 0.7s |
| 5 | +5.0 | F | node 3 "AUTO-DEBIT or CALENDAR ALERT" | `pop .5` | cascade (3 nodes ≤5 ✓) |
| 6 | +6.3 | A | `#s6cut` open-passbook cut-in | `fade .5` | «ड्यू डेट पर … लगा दीजिए» (char 50–82) |
| 7 | +8.0 | F | **exit** `#s6k` fade .4 | `fade` | kicker's job done |
| 8 | +9.3 | F | **exit** `#s6cut` fade .4 | `fade` | stay ≤6 through the stamp |
| 9 | +9.9 | A | `#s6stamp` "REMEMBERING SHOULDN'T BE YOUR JOB" (fund) | `pop .6` + `pulse` | «याद रखना आपका काम नहीं होना चाहिए» (char 114) |
| 10 | +13.4 | F | **exit** `#s6h` + `#s6flow` + `#s6stamp` fade .4 | `fade` | clear for the utilisation beat |
| 11 | +14.2 | A | `#s6u` "Use a **SMALL** share of the limit" (fund span on SMALL) | `rise` | «लिमिट का कम हिस्सा इस्तेमाल कीजिए» (char 167) |
| 12 | +17.2 | A | `#s6u2` "PAY THE FULL BILL → not the minimum" (fund on FULL, **muted** on "not the minimum") | `pop .5` | «बिल पूरा भरिए, मिनिमम नहीं» (char 202) |

> **Layout note (≤6 elements).** The script's flow is `EVERY CARD → EVERY LOAN →
> AUTO-DEBIT or CALENDAR ALERT` = 3 nodes + 2 arrows = 5 elements, which with the
> kicker, huge, cut-in, stamp and two subs blows the cap. `#s6flow` is therefore
> **one `.row` element** whose three nodes reveal via an internal `popEach`
> (counts as 1), with the arrows drawn as CSS `::after` on the nodes per §4 —
> `→` is not typed, it is absent from the font subset. Same collapse `good-debt`'s
> s4 made on its classifier columns.

> **Colour check that matters on this scene.** "not the minimum" is **`--muted`**,
> not `--warn`. In *this* video red belongs to the missed EMI and its price; a
> minimum-only payment is a utilisation caveat, not the trap the script exposes.
> Rendering it red would import `good-debt-vs-bad-debt`'s thesis into a video that
> never argues it — the exact per-video-semantics failure §2 warns about.

Green sits on AUTO-PAY, the flow, the stamp, SMALL and FULL — the whole constructive
path. Simultaneous peaks: +6.3 → kicker + huge + flow + cut = **4** ✓; +9.9 → huge +
flow + stamp = **3** ✓; +17.2 → u + u2 = **2** ✓. bg `s6.jpg` wristwatch on dark wood
(object-led "every due date"), ken OUT. **No phone-screen photo** — the script's
«फ़ोन में … रिमाइंडर» line is carried by the flow node's *text*, never by a screenshot
(§7, shipped wrong 3×). cut-in an open bank passbook on the due-date clause.

### s7 · THE MATH — one percentage point on a ₹30 lakh loan (densest) · h7 (clip 24.424s, longest) · photo (calmest), ken IN · tint red .12

DOM: `#s7k .kicker` (exits) · `#s7band1 .decision.fund` (exits) · `#s7setup .sub` (exits) · `#s7band2 .decision.warn` (exits) · `#s7loan .sub` (exits) · `#s7r1 .billrow.warn` (exits) · `#s7r2 .billrow.total.warn` · `#s7f .foot` · `#s7cut` house-keys cut-in · `#s7q .huge.warn` (the punch, focal)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the math — what a low score costs" | `rise` | scene open |
| 2 | +2.8 | A | `#s7band1` "TOP SCORE BAND → the bank's best price" (fund) | `rise .4` | «बैंक अपने रेट सिबिल बैंड से जोड़ते हैं» (char 30) |
| 3 | +6.1 | A | `#s7setup` "SAME LOAN · SAME BANK" | `rise` | «वही लोन, वही बैंक» (char 71) |
| 4 | +7.7 | A | `#s7band2` "BELOW-700 BAND → ~1 percentage point higher" (warn) | `pop .5` + `pulse` | «नीचे के बैंड में क़रीब एक परसेंट ऊपर» (char 90) |
| 5 | +11.7 | A | `#s7loan` "₹30,00,000 · 20 years" | `rise` | «तीस लाख के बीस साल के लोन» (char 140) |
| 6 | +15.0 | A | `#s7r1` "EXTRA EVERY MONTH  ₹1,390 – ₹1,860" (warn) | `rise .4` | «हर महीने क़रीब पंद्रह सौ रुपये ज़्यादा» (char 181) |
| 7 | +16.4 | F | **exit** `#s7k` + `#s7setup` fade .4 | `fade` | stay ≤6 |
| 8 | +18.3 | A | `#s7r2` "EXTRA INTEREST  ₹3.3 – 4.5 lakh" (warn `.total`) | `pop .5` + `pulse` | «तीन से साढ़े चार लाख ज़्यादा ब्याज» (char 221) |
| 9 | +19.6 | F | `#s7f` "Two lenders' own published rate cards, keyed to the CIBIL band — spread, not rates" | `fade` | source line |
| 10 | +21.2 | F | **exit** `#s7band1` + `#s7band2` + `#s7loan` + `#s7r1` fade .4 | `fade` | clear for the punch |
| 11 | +21.6 | A | `#s7cut` house-keys-on-a-property-document cut-in | `fade .5` | sets up «एक ही घर» |
| 12 | +22.5 | A | `#s7q` "SAME HOUSE. DIFFERENT NUMBER." (warn) | `pop .7` + `pulse` | «एक ही घर, सिर्फ़ एक अलग नंबर» (char 273) |

**No bank is named and no interest rate appears** — only the *spread* (audit: both
recorded rate cards are stale/undated; a third, independently fetched card shows
1.65 pp, so "~1 percentage point" is the conservative side). `#s7band2` says
"~1 percentage point higher", never "8.15%".
**The four integers are build-calculator output, displayed not spoken.** Regenerate
`₹1,390` / `₹1,860` / `₹3.3` / `₹4.5 lakh` from `EMI = P·i·(1+i)ⁿ/((1+i)ⁿ−1)`,
P = ₹30,00,000, n = 240, Δ = 0.75 and 1.00 pp (script handoff #5; audit re-derived by
hand and both ends match). `Intl.NumberFormat("en-IN")` grouping — a plain
`\B(?=(\d{3})+(?!\d))` regex prints `₹3,000,000` and is wrong for India. The VO stays
the round anchor «क़रीब पंद्रह सौ» whatever the calculator returns.
Colour: top band **fund**, below-700 band and both extra-cost rows **warn**, punch
**warn** — the price of the miss, exactly per the table. Simultaneous peaks: +15.0 →
kicker + band1 + setup + band2 + loan + r1 = **6** ✓; +19.6 → band1 + band2 + loan +
r1 + r2 + foot = **6** ✓; +22.5 → r2 + foot + cut + huge = **4** ✓.
bg `s7.jpg` blueprint paper texture — **calmest bg, densest scene**; the numbers carry
it, ken IN, background nearly still.

### s8 · DO THIS TODAY · h8 (clip 17.450s) · photo, ken OUT · tint orange .12

DOM: `#s8stamp .stamp.pop` · `#s8b1 .decision.fund` · `#s8free .sub` (exits) · `#s8disp .sub` (exits) · `#s8cut` checklist cut-in (exits) · `#s8b2 .decision.fund` · `#s8f .foot.muted`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` "DO THIS TODAY" (pop) | `pop .6` + `pulse` | scene-open slam («तो आज दो काम») |
| 2 | +1.5 | A | `#s8b1` "1  PULL YOUR CREDIT REPORT" (fund) | `pop .5` | «पहला — अपनी क्रेडिट रिपोर्ट एक बार देखिए» (char 14) |
| 3 | +4.5 | A | `#s8free` "one free full report a year, from each bureau" | `rise` | «हर ब्यूरो से साल में एक फ़ुल रिपोर्ट मुफ़्त» (char 56) |
| 4 | +8.5 | A | `#s8disp` "Wrong entry? Raise a dispute." | `rise` | «कोई ग़लत एंट्री दिखे» (char 110) |
| 5 | +10.2 | A | `#s8cut` pen-ticking-a-checklist cut-in | `fade .5` | «विवाद दर्ज कीजिए» (char 134) |
| 6 | +11.0 | F | **exit** `#s8free` + `#s8disp` fade .4 | `fade` | clear for action 2 |
| 7 | +11.6 | A | `#s8b2` "2  PUT EVERY DUE DATE ON AUTO-PAY" (fund) | `pop .5` | «दूसरा — हर ड्यू डेट आज ही ऑटो-पे पर डालिए» (char 152) |
| 8 | +13.2 | F | **exit** `#s8cut` fade .4 | `fade` | cut-in's job done |
| 9 | +14.8 | A | `#s8f` "A score is built in months, not in a day — do this long before you need the loan" | `rise` | «स्कोर एक दिन में नहीं, महीनों में बनता है» (char 195) |

`#s8free` is the one figure in the video whose **regulator text was actually fetched**
this run (RBI (CIC) Directions 2025, FFCR clause — audit check 1). The per-bureau
wording is load-bearing: "from **each** bureau", not "one report a year". Do not
compress it at build.
Simultaneous peak (+10.2): stamp + b1 + free + disp + cut = **5** ✓; +14.8 → stamp +
b1 + b2 + foot = **4** ✓. Stamp is **pop orange** (the CTA register), both action
blocks **fund green** (behaviours that build the record). bg `s8.jpg` clipped document
pages on a dark desk, ken OUT — deliberately **not** a magnifying glass, see the
Image-sourcing note.

### s9 · RECAP + CTA · h9 (clip 15.961s) · photo (calm closer), ken IN · tint green .13

DOM: `#s9k .kicker` (exits) · `#s9a`–`#s9d .chip` (2×2 rows: a+b / c+d) · `#s9cta .cta` (`▶` CSS-drawn, pop block)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "The simple version" | `rise` | scene open |
| 2 | +1.5 | A | `#s9a` BANK READS IT FIRST (ink) | `pop .45` | «बैंक आपसे पहले आपकी रिपोर्ट पढ़ता है» (char 14) |
| 3 | +4.4 | A | `#s9b` ON-TIME EMIs BUILD IT (fund) | `pop .45` | «वक़्त पर भरी किश्तें उसे बनाती हैं» (char 52) |
| 4 | +7.1 | A | `#s9c` ONE MISS = 36 MONTHS (warn) | `pop .45` | «एक चूक छत्तीस महीने दिखती है» (char 88) |
| 5 | +9.4 | A | `#s9d` LOW SCORE COSTS LAKHS (warn) | `pop .45` | «कम स्कोर हर बड़े लोन पर लाखों वसूलता है» (char 118) |
| 6 | +12.2 | F | **exit** `#s9k` fade .4 | `fade` | make room for the cta |
| 7 | +12.8 | A | `#s9cta` "▶ SUBSCRIBE" (pop block) | `pop .6` | «पैसे की ऐसी सीधी बात के लिए» (char 162) |
| 8 | +15.1 | A | `#s9cta` `pulse` + breathe to scene end | hold | «सब्सक्राइब कीजिए» (char 192) |

Recap chip char check (≤22): a **19** · b **21** · c **20** · d **21** ✓ — a and d are
the **audit-edited** strings (`THE BANK READS IT FIRST` 23 → `BANK READS IT FIRST`;
`A LOW SCORE COSTS LAKHS` 23 → `LOW SCORE COSTS LAKHS`). Do not restore the articles.
Chip colours track the thesis: b **fund** (on-time builds), c and d **warn** (the miss
and its price), a **neutral ink** (a fact, not a verdict). Video closes on the `.cta` —
no logo outro. Simultaneous: kicker + 4 chips = 5; after exit, 4 chips + cta = **5** ✓.
bg `s9.jpg` sunlit open doorway — calm object-led closer (the door the report opens),
ken IN. **Not a person** — both shipped hi cuts closed on a man-with-phone shot; §7
bars the reuse and a face fights the CTA type.

---

## Timing (measured — `timing.json` values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row,
root `data-duration`) — generate all four from `timing.json`, never hand-edit.
Updating three of four passes every check and ships a broken timeline.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | h1 | 17.162 | 18.562 | 0.0 | 0.4 |
| s2 | h2 | 11.598 | 12.998 | 18.562 | 18.962 |
| s3 | h3 | 20.193 | 21.593 | 31.561 | 31.961 |
| s4 | h4 | 19.487 | 20.887 | 53.153 | 53.553 |
| s5 | h5 | 19.540 | 20.940 | 74.041 | 74.441 |
| s6 | h6 | 19.226 | 20.626 | 94.980 | 95.380 |
| s7 | h7 | 24.424 | 25.824 | 115.607 | 116.007 |
| s8 | h8 | 17.450 | 18.850 | 141.431 | 141.831 |
| s9 | h9 | 15.961 | 17.361 | 160.281 | 160.681 |
| **total** | | | | | **177.642** |

## Image slots (→ `assets/img/manifest.json`)

**17 slots — 9 bg (every scene) + 8 cut-ins.** All object-led — no phone screens, no faces.

| slot | query | scene · role |
|---|---|---|
| `s1.jpg` | rows of archive files on shelves dark | s1 · bg |
| `s1-cutA.jpg` | closed manila folder tied with string | s1 · cut-in «एक रिपोर्ट … कभी देखी नहीं» |
| `s1-cutB.jpg` | bank loan application form with a pen | s1 · cut-in «बैंक आपसे मिलने से पहले» |
| `s2.jpg` | bundles of old documents tied with string | s2 · bg (**calmest in the video**) |
| `s3.jpg` | old ledger book ruled columns handwritten close up | s3 · bg |
| `s3-cut.jpg` | numbers printed on a paper form close up | s3 · cut-in «तीन अंकों का एक नंबर» |
| `s4.jpg` | open desk diary with a pen on dark wood | s4 · bg (**calm, dense**) |
| `s4-cut.jpg` | two credit cards on a dark wooden surface close up | s4 · cut-in «लिमिट का कितना हिस्सा» |
| `s5.jpg` | red rubber stamp and ink pad on a wooden desk | s5 · bg (**calm — the grid carries the scene**) |
| `s5-cut.jpg` | torn paper calendar page on a dark surface | s5 · cut-in «पूरे तीन साल दिखती है» |
| `s6.jpg` | wristwatch lying on a dark wooden table | s6 · bg |
| `s6-cut.jpg` | open bank passbook with printed entries | s6 · cut-in «ड्यू डेट … लगा दीजिए» |
| `s7.jpg` | architectural blueprint paper texture close up | s7 · bg (**calmest, densest**) |
| `s7-cut.jpg` | house keys resting on a property document | s7 · cut-in «एक ही घर» |
| `s8.jpg` | printed document pages clipped together on a dark desk | s8 · bg |
| `s8-cut.jpg` | pen ticking boxes on a paper checklist | s8 · cut-in «विवाद दर्ज कीजिए» |
| `s9.jpg` | sunlit open doorway of a house entrance | s9 · bg (calm closer) |

### Image-sourcing note (design §7 — load-bearing)

- **`s8` bg is deliberately NOT a magnifying glass.** The script asks for
  *"magnifying glass over a printed document"*; `good-debt-vs-bad-debt-hi/s5.jpg` already
  shipped `magnifying glass financial document numbers`. Pixabay's top hit is
  deterministic, so those two queries are a near-certain **hash collision** — the exact
  verified failure mode in §7 (one `s9.jpg` byte-identical across three projects on
  *both* channels). Replaced with clipped document pages.
- **`s5-cut.jpg` is the second-highest collision risk.** `pay-yourself-first` shipped
  `wall calendar dates close up#2` (hi) and `paper monthly calendar planner desk` (en).
  A *torn* page is a different search intent, but **md5 it against both of those
  specifically**; on collision use the `#2`/`#3` result knob, do not re-word into
  another calendar query.
- **`s4.jpg` (diary) vs `pay-yourself-first`'s `old book pages warm lamp light`** —
  check the hash; a diary and a book page collapse easily.
- **No phone-screen photo anywhere**, including s6 where the VO says «फ़ोन में …
  रिमाइंडर». The screen is someone else's brand and the brightest thing in frame; it has
  shipped wrong 3× (most recently `MTN-SA` legible, upside down). The reminder beat is
  carried by flow-node *text*.
- **No faces.** s9 closes on a doorway, not the man-with-phone shot both shipped hi cuts
  used — Pixabay bars unflattering use of identifiable people, and a face fights the CTA type.
- **India-specific people queries are ~20% usable** — every slot here is object-led for
  that reason, and none of them needs to say "India" (the ₹ figures do that).
- **Check what the picture is saying** before it goes in: a *green*-ticked checklist under
  s8 is fine, a red-X form under s4 (which is about what *builds* the score) is not.
- **Snapshot every fetch and md5 it against the asset ledger; refuse any hash used in any
  prior video on either channel.**

## The -en pass

This is the **master skeleton.** The `-en` storyboard ports these scene shapes and
element IDs **verbatim** (`s1q`, `s1d1-3`, `s3scale`, `s4r1-4`, `s5grid`, `s5ctr`,
`s6flow`, `s7band1/2`, `s7q`, `s9a-d`, …) so fixes travel between cuts, and must emit an
explicit **divergence list with a reason per scene**. Expected divergences, none of them
optional:

- **s3 · the whole scale is different.** FICO is **300–850**, not 300–900, and the
  band language is FICO's ("good" starts ~670/700 depending on model), not CIBIL's.
  `#s3scale`'s numerals and both `.collabel` markers change.
- **s4 · FICO *publishes* its weights** (35/30/15/10/10) — the exact figures this hi cut
  is forbidden to carry. The `-en` cut may show them, which means `#s4f`'s guard-rail
  foot is **wrong for `-en`** and the four rows may legitimately become proportional.
  This is the single largest divergence in the video; re-derive it from `fin-script-en`,
  never port the hi foot.
- **s5 · "36 months" is a CIBIL fact and does not travel.** The US rule is the FCRA
  7-year window (§1681c(a)) — which this hi cut is *hard-forbidden* to name. The grid's
  cell count, the counter's range and `#s5q`'s copy all change; the hero *shape*
  (green fill, one red slam, fill continues past it) is what ports.
- **s7 · $ math from scratch.** `$` replaces `₹`, `Intl.NumberFormat("en-US")` replaces
  `en-IN`, and the ₹30 lakh / 20-year model becomes a US mortgage from the `-en` sources.
  Brian runs ~15 c/s vs Harsh's 12.5, so **every anchored offset in the video is different** —
  port the IDs and the cue *classes*, never the numbers.
- **s8 · AnnualCreditReport.com replaces the RBI FFCR clause** — different right,
  different cadence, different source foot.
- **Concrete nouns that change market:** the passbook (s6) barely exists in the US,
  and "EMI" (s4, s9) is "monthly payment".

**Zero divergences = a translation in a layout costume; the audit will flag it.**

## Deliberate placeholders (must be real before publish)

- **Every `A` offset is char-interpolated intent** against the measured clip. Refine with
  faster-whisper word timings at build (script handoff #7 — the drift is worst on Hindi).
  The one that must not slip: **s1's naming ≤15s** (advisory in s1; the on-screen payoff
  at +3.2 is already independent of it).
- **s7's four integers** (`₹1,390` · `₹1,860` · `₹3.3 lakh` · `₹4.5 lakh`) = build-calculator
  output, not storyboard constants. Regenerate from the EMI model, `en-IN` grouping.
- **s5's foot quotation marks** — audit's residual: substance confirmed, exact-phrase match
  never surfaced. Drop the quote marks to reported speech if the build wants zero risk.
- **s5's 36-cell grid** is spec'd here as behaviour, not as markup. The build owns the DOM;
  the invariants are: 3 × 12, green fill left→right across the full scene, one cell slams
  warn at the «एक चूकी हुई किश्त» word and never clears, fill continues past it.
- **Image hashes** — no fetch has run; every slot is unverified against the ledger.

## Sign-off

- [x] Colour semantics table filled and consistent with the script (red = the miss and its price; "not the minimum" deliberately muted, not red)
- [x] Every number traced to a sourced line (script-hi.md fact trace + audit-hi.md check 1)
- [x] No "7 years", no percentage weight, no named lender, no specific rate, no `$` anywhere in this file
- [ ] No image hash reused from any prior video on either channel (check at fetch — 3 known-risk slots flagged)
- [x] Every scene carries a full-bleed bg photo (photo-free retired; 9 bg + 8 cut-ins)
- [x] s1 hook-payoff ≤15s advisory recorded for build (audit check 3 + fin-voice flag)
- [ ] Creator approved (Gate ②) — date: __
