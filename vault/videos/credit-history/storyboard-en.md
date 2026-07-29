---
summary: Gate ② storyboard SPEC for «Your Credit History» EN / USA cut — 9 scenes, scene DOM + GSAP cue tables built on the MEASURED timing.json (total 173.227s), keyword-matched bg + cut-ins on every scene (photo-free retired). en5's FCRA seven-year timeline is the hero. US rewrite of the hi master skeleton — element IDs ported, one divergence row per scene, all 9 diverge.
updated: 2026-07-29
source: videos/credit-history/script-en.md (post-audit-edit, USD SET) + studio/videos/credit-history-en/assets/voice/timing.json (measured, total 173.227s, Brian 16.11 c/s effective) + [[../../knowledge/design-finance-blockframe]] + [[../../templates/storyboard-template-finance]] + storyboard-hi.md (master skeleton) + audit-en.md advisories (≤6 in en5/en7, undeclared gaps in en1/en7/en8, the FICO-band-next-to-APR standing ban) + logs/fin-voice-en-1.md + logs/fin-assets-hi-1.md (short-query finding)
---

# STORYBOARD — «Your Credit History» · en cut

**Project:** `studio/videos/credit-history-en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` (bright, non-finance) for this format.
**Channel:** @moneymavens101 `$` · **Tier:** SHORT 9-segment blockframe
**Runtime (measured):** **2:53.2** (timing.json total 173.227s) · **VO:** Brian `nPczCj…`
**Rate:** en 15.0 chars/s nominal — **measured 16.11 c/s** (2,587 / 160.627) · **Grade:** dark blockframe
**Locale:** `en-US` — `$25,000`, `$12,400`

> **Every keyframe in this file is derived from the measured `timing.json`, not from
> the script's paced estimates.** Brian read 7.4% faster than `format.json cuts.en`
> records. The scene that moves most is **en5, the hero: 18.798s, not the ~21.7s the
> script paced against** — its whole cue table is re-derived, not scaled.

## Colour semantics for THIS video (derived from the thesis — mandatory)

Thesis: **a file you have never read decides whether you get a loan and what it costs.
On-time payments and a low balance build it; one missed payment can sit there for seven
years, counted from the miss and not from the payoff; a weak score charges roughly three
times the interest on the identical car. The fix is auto-pay and reading your report.**

| Token | This video means | Because |
|---|---|---|
| `--fund` green | the **on-time payment**, the low balance, the clean report, the **top credit tier**, and the auto-pay habits that build the record | everything that *builds* the file — this video's constructive path is behavioural, never an instrument |
| `--warn` red | the **missed payment and the price it charges** — the seven-year mark at year zero, the subprime row, `$172`/`$12,400`, the bankruptcy chip | red is the miss and its bill, exposed — never "a credit card", never "debt", never the score itself |
| `--target` amber | the **report / the score under examination** — `YOUR CREDIT REPORT`, the 300–850 scale, the three-digit number | it is the object of study, not a verdict |
| `--pop` orange | call to action — the `DO THIS TODAY` stamp, the `SUBSCRIBE` block | (fixed) |

The test: if the **year-zero mark** ever renders green, or **AUTO-PAY / ON-TIME / the top
credit tier** render red, or the **score itself** renders red as though a score were the
villain, the video argues against its own script.

> **Anti-drift note (contract §1).** Do **not** import `needs-vs-wants`'s inversion
> (there amber = "wants" and red is the leak alone) or `good-debt-vs-bad-debt`'s
> (there red = "the minimum payment"). Here the minimum payment is a *caveat* inside
> the utilisation beat, so **`#s6u2`'s "not the minimum" renders `--muted`, not
> `--warn`** — same call the hi cut made. Reusing another video's red is exactly the
> drift this table exists to stop.

## Global guardrails (from the design system + `format.json`)

- Dark `#0d1017` · full-bleed photo under `grayscale(.32) brightness(.62) contrast(1.05)` · four-layer scrim + grain `.05`.
- One focal element per scene. Never `.huge` and `.mega` together — s3 is the only `.mega` (the scale) and carries no `.huge`; s5 has neither (the track is the focal).
- Reveal spacing ≥0.8s. **No scene in this cut declares a cascade** — see "Cue classes" below. Something on screen by +0.5s (every scene opens at **+0.40**).
- ≤6 elements visible at once — every scene that would exceed it declares **exits**. Measured peak per scene is stated in each block.
- ≤3 chips/row, ≤22 chars each — rows declared explicitly, never left to `flex-wrap`.
- **Every scene carries a full-bleed bg photo** (`photo_free_scene_ratio` 0). Every scene gets `ken`, alternating: **s1 in · s2 out · s3 in · s4 out · s5 in · s6 out · s7 in · s8 out · s9 in**. No static frame beyond ~2s.
- **Densest scene gets the CALMEST bg:** s7 (the math, 10 elements across the scene) → a single car key; s5 (hero) → an hourglass; s4 → a desk calendar. Density is managed by choosing a quieter image, never by dropping one.
- **No phone-screen photos, no faces** (§7 — shipped wrong 3×). s6's due-date beat is carried by flow-node *text* and a wall clock, never a screenshot; s9 closes on a highway, not a person.
- Type steps down the ladder (`290 · 240 · 112 · 96 · 54 · 50 · 46 · 44 · 40 · 32 · 30 · 28 · 26`) — never interpolated to fit.
- `→` and `▶` are **CSS-drawn**, not typed (absent from the subset). **`×` in `WEAK SCORE = 3× RATE` must be verified in the subset before build** — see Placeholders.
- No SFX. No logo outro — close on `.cta`.
- **Every image hash checked against the asset ledger** — no reuse from any prior video on either channel, and specifically not from `credit-history-hi` (same slug, adjacent queries — 5 named collision risks below).

## Cue classes

`A` = **anchored** — offset scales with the clip and lands on the noted English word.
Offsets are char-interpolated design intent (`0.4 + chars_before/total × measured clip`)
computed against the **measured** clip length; the build refines them with faster-whisper
word timings (script handoff #7).
`F` = **fixed** — stamp slams, exits, scene-open kickers — constant regardless of clip length.
Surplus from a longer clip goes into **holds (breathe / ken / fill), never into cascades.**

> **No cascade is declared anywhere in this cut**, and that is deliberate. The script's
> on-screen notes ask for a 0.6s two-item cascade in en4 and the hi skeleton uses 0.7s
> cascades in s3 and s6. Brian spaces every one of those groups **≥0.8s apart in the
> read**, so anchoring lands each item on its own word *and* satisfies
> `layout.cue_min_gap_seconds` without a declaration. Retiring an unnecessary cascade is
> the §6 rule ("surplus into holds, never cascades") applied at storyboard time.
> This closes the audit's "undeclared reveal gaps in en1, en7, en8" advisory: **every
> reveal gap in this file is ≥0.8s and is printed in its scene block.**

---

## Scenes

Offsets are seconds **inside** each scene. Scene starts are the measured `timing.json`
values (Timing table) — never re-derived.

### s1 · HOOK — the file you've never read · en1 (clip 14.707s) · photo, ken IN · tint red .12

DOM: `#s1k .kicker` (exits) · `#s1q .huge.target` ("YOUR CREDIT REPORT", the focal) · `#s1cutA` unopened-mail cut-in · `#s1cutB` contract cut-in (crossfades over cutA, exits) · `#s1d1`/`#s1d2`/`#s1d3 .decision` · `#s1stamp .stamp.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s1k` "A file you've never read" | `rise` | scene open |
| 2 | +1.7 | A | `#s1cutA` unopened-mail cut-in | `fade .5` | «a file on you» (char 21) |
| 3 | +3.0 | A | `#s1q` "YOUR CREDIT REPORT" (amber) | `pop .7` | «you've never read» (char 44) — **the visual payoff, +3.0s** |
| 4 | +5.4 | A | `#s1d1` "THE LOAN?  → it decides" | `rise .4` | «whether you get a loan,» (char 85) |
| 5 | +7.0 | A | `#s1d2` "THE RATE?  → it decides" | `rise .4` | «and what interest you pay.» (char 112) |
| 6 | +8.1 | A | `#s1cutB` crossfade over `#s1cutA` | `fade .5` | «The lender reads it» (char 129) |
| 7 | +8.9 | F | **exit** `#s1k` fade .4 | `fade` | stay ≤6 through the strip |
| 8 | +9.7 | A | `#s1d3` "EVER SEEN IT?  → probably not" (muted verdict) | `rise .4` | «before you ever walk in.» (char 157) |
| 9 | +11.6 | A | `#s1q` `pulse` + breathe 2.0s | hold | «It's called your credit report» (char 189) — **the naming beat** |
| 10 | +12.9 | F | **exit** `#s1cutB` fade .4 | `fade` | clear for the stamp |
| 11 | +13.7 | A | `#s1stamp` "A MISS CAN STAY 7 YEARS" (warn) | `pop .6` + `pulse` | «can sit in it» (char 225); «seven years» lands +14.4 under the stamp |

Reveal gaps: 1.3 · 1.3 · 2.4 · 1.6 · 1.1 · 1.6 · 4.0 — all ≥0.8 ✓ (cue 9 is a `pulse` on
an element already on screen, cues 7/10 are exits; neither is a reveal).

**Hook-payoff clock — CLEARED, twice over.** The audit made ≤15s a gate and fin-voice
measured en1 at 14.707s / **16.86 c/s, faster than 15**, so the prescribed trim
(«and what interest you pay») is **not taken**. The promise is paid off twice:

- **On screen** at **+3.0** (`#s1q`), 12s inside the gate regardless of delivery rate.
- **In VO** at **≈+11.6** on the timeline (char 189/248 = 76.2% × 14.707 + 0.4), which is
  exactly where fin-voice's two independent methods landed. **Margin ≈3.4s.**

Whisper-verify the naming word at build anyway (handoff #7); there is now enough slack
that it is a formality. Cue 9's `pulse` is a re-sync, not the payoff — it may slide.

**Stamp wording is the audit's edit and is load-bearing:** `A MISS CAN STAY 7 YEARS`,
never `EVERY MISS STAYS 7 YEARS`. Both sources say a bureau *generally **can** report*.
Do not restore the stronger form at build.

Simultaneous peak (+9.7): `#s1q` + cutB + d1 + d2 + d3 = **5** ✓ (kicker exited at +8.9,
cutA replaced by cutB). After +12.9: q + 3 decisions + stamp = **5** ✓. One focal
(`.huge`); `.decision` rows are 40px and `.stamp` 44 — no competition.
bg `s1.jpg` filing cabinet (ken IN). Cut-ins on the two concrete things the VO names:
the unread file «a file on you» and the lender's paperwork «The lender reads it».

### s2 · ROADMAP — four things · en2 (clip 9.326s, shortest) · photo (calmest rest beat), ken OUT · tint amber .10

DOM: `#s2k .kicker` · `#s2a`–`#s2d .chip` (2×2 rows: a+b / c+d, neutral ink borders) · `#s2sub .sub`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s2k` "By the end you'll know" | `rise` | scene open |
| 2 | +2.2 | A | `#s2a` WHAT THE REPORT IS | `pop .45` | «what that report actually is» (char 29) |
| 3 | +3.7 | A | `#s2b` WHAT BUILDS IT | `pop .45` | «what builds it,» (char 54) |
| 4 | +4.8 | A | `#s2c` WHAT DESTROYS IT | `pop .45` | «what destroys it,» (char 72) |
| 5 | +6.2 | A | `#s2d` WHY IT MATTERS EARLY | `pop .45` | «why it matters years before» (char 95) |
| 6 | +8.4 | A | `#s2sub` "Then two moves for today" | `rise` | «Then two moves» (char 131) |

Reveal gaps: 1.8 · 1.5 · 1.1 · 1.4 · 2.2 — all ≥0.8 ✓. **Not a cascade** (the hi cut's
chips were anchored here too; Brian is fast but still spaces these four beats ≥1.1s).
Chip char check (≤22): a **18** · b **14** · c **16** · d **20** ✓, 2 per row ✓.
Borders are **neutral ink** — roadmap topics are not colour claims, and colouring
"WHAT DESTROYS IT" red here would spend the red before s5 earns it.
Simultaneous: kicker + 4 chips + sub = **6** ✓ (at cap, held only from +8.4 to scene end).
bg `s2.jpg` cardboard boxes — the calmest image in the video, slow ken OUT.
**No cut-in:** every noun in en2 is abstract ("four things", "that report") and the bg
already *is* the report as texture — a cut-in here would be faked (§7 "drop a cut-in
rather than fake it"). The scene still carries a photo.

### s3 · CONCEPT — the report and the score · en3 (clip 20.062s) · photo, ken IN · tint amber .12

DOM: `#s3k .kicker` (exits) · `#s3e1`–`#s3e3 .chip` (exit) · `#s3rec .sub` (exits) · `#s3ha`/`#s3hb .head2` (exit) · `#s3cut` odometer cut-in (exits) · `#s3scale` (**the focal**: `.mega`@240 "300" ├ `.track2` ┤ `.mega`@240 "850") · `#s3g1 .collabel.fund` · `#s3f .foot`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s3k` "First — what it actually is" | `rise` | scene open |
| 2 | +3.1 | A | `#s3e1` EVERY LOAN | `pop .45` | «Every loan,» (char 40) |
| 3 | +4.3 | A | `#s3e2` EVERY CREDIT CARD | `pop .45` | «every credit card,» (char 59) |
| 4 | +5.2 | A | `#s3e3` EVERY PAYMENT | `pop .45` | «every payment» (char 73) |
| 5 | +7.7 | A | `#s3rec` "→ reported to the credit bureaus" | `rise` | «the credit bureaus.» (char 110) |
| 6 | +9.0 | F | **exit** `#s3e1`–`#s3e3` fade .4 | `fade` | enumeration's job done |
| 7 | +10.0 | A | `#s3ha` "THE REPORT = the record" | `rise` | «That record is your credit report,» (char 145) |
| 8 | +11.3 | A | `#s3hb` "THE SCORE = the summary" | `rise` | «its summary is» (char 164) |
| 9 | +12.8 | A | `#s3cut` odometer cut-in | `fade .5` | «one three-digit number» (char 187) |
| 10 | +13.4 | F | **exit** `#s3k` + `#s3rec` fade .4 | `fade` | clear for the focal |
| 11 | +14.4 | A | `#s3scale` "300 ├──────┤ 850" (mega@240, **the focal**) + `fill` on the amber track | `pop .7` + `fill .8` | «from three hundred to eight hundred fifty» (char 211) |
| 12 | +15.4 | F | **exit** `#s3ha` + `#s3hb` + `#s3cut` fade .4 | `fade` | one focal only |
| 13 | +18.7 | A | `#s3g1` `670+ = "good"` (fund) | `pop .5` | «Six hundred seventy and up» (char 276) |
| 14 | +19.6 | F | `#s3f` "FICO — score range 300–850 · CFPB consumer education" | `fade` | source line |

Reveal gaps: 2.7 · 1.2 · 0.9 · 2.5 · 2.3 · 1.3 · 1.5 · 1.6 · 4.3 · 0.9 — all ≥0.8 ✓.
**The three enumeration chips are anchored, not the hi cut's 0.7s cascade** — Brian
spaces them 1.2s and 0.9s, so each lands on its own noun and no declaration is needed.

**`#s3g2` DOES NOT EXIST in this cut.** The hi skeleton's second band marker
(`750+ = best pricing`) has **no en counterpart**: fin-audit killed `upper 700s = the
best offers` because its recorded source backs the *band names only*, and the only
best-priced-tier evidence is Experian's grid — which is **VantageScore 4.0**, a
different model from the FICO scale this bar draws. `670+ = "good"` is verbatim from the
score owner and stands alone. **Do not restore a second marker at build from any source.**

`.mega` drops to **240** (a value already on the ladder, as the shipped pair did) so two
3-digit numerals plus the track fit inside `110px 150px`. Do not interpolate off the ladder.
Colour: the track is **amber** (the score under examination), `670+` **fund green** (the
good band). Neither `300` nor `850` is coloured — an endpoint is not a verdict.
Simultaneous peaks: +7.7 → k + e1 + e2 + e3 + rec = **5** ✓; +12.8 → k + rec + ha + hb +
cut = **5** ✓; +19.6 → scale + g1 + foot = **3** ✓.
bg `s3.jpg` pressure gauge (the needle-on-a-scale read of a score), ken IN.
Foot says **FICO**, not myFICO — audit edit 5; myFICO is a subscription product and a
product name on screen is what the no-recommendation gate exists to stop.

### s4 · RULE — what builds it (two weights) · en4 (clip 16.300s) · photo (calm), ken OUT · tint green .10

DOM: `#s4k .kicker` (exits) · `#s4r1`/`#s4r2 .billrow.fund` (label + proportional bar + `%`) · `#s4cut` wallet cut-in (exits) · `#s4q .huge.fund` ("65% OF YOUR SCORE") · `#s4sub .sub` · `#s4f .foot.muted`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s4k` "What builds it" | `rise` | scene open |
| 2 | +4.3 | A | `#s4r1` "PAYMENT HISTORY" row frames in (fund) | `rise .4` | «Payment history» (char 66) |
| 3 | +7.1 | A | `#s4r1` bar **fills to 35%** + `35%` counts up | `fill .8` + `countUp` | «is thirty-five percent» (char 113) |
| 4 | +8.0 | F | `#s4f` foot | `fade` | source line, sits low |
| 5 | +9.9 | A | `#s4cut` leather-wallet cut-in | `fade .5` | «your available credit» (char 160) |
| 6 | +11.0 | A | `#s4r2` "AMOUNTS OWED" row frames in (fund) | `rise .4` | «you're using» (char 180) |
| 7 | +12.6 | A | `#s4r2` bar **fills to 30%** + `30%` counts up | `fill .8` + `countUp` | «another thirty percent.» (char 207) |
| 8 | +13.2 | F | **exit** `#s4k` + `#s4cut` fade .4 | `fade` | clear for the punch |
| 9 | +14.2 | A | `#s4q` "65% OF YOUR SCORE" (fund, the focal) | `pop .7` | «That's sixty-five percent» (char 233) |
| 10 | +16.0 | A | `#s4sub` "Two habits: pay on time · keep the balance low" | `rise` | «decided by two habits.» (char 264) |

Reveal gaps: 3.9 · 3.7 · 1.9 · 1.1 · 3.2 · 1.8 — all ≥0.8 ✓ (cues 3 and 7 are `fill`
motions on rows already on screen, not reveals).

> **The script's declared 0.6s two-item cascade is retired.** The audit noted it was
> legal (2 items, inside `cascade.gap_seconds`), but Brian spaces the two factors
> **6.7s apart** in the read. A 0.6s cascade would dump both rows at +4.3 and leave 12s
> with no new motion — a §5.2 failure — and throw away two clean word anchors. Each row
> now **frames in on its name and fills on its number**, which is also what makes the
> `65%` punch land as arithmetic the viewer just watched. Same call the hi cut made on
> its four rows.

**Only 35 and 30 reach the screen** (facts-staging: "Only 35/30 should go on screen").
No `15%`/`10%`/`10%` tail, no ring chart, no fifth row. The foot says other factors
count without asserting a weight the file cannot defend, and cites **FICO's published
category weights** (audit edit 5 — not "myFICO"), corroborated by the Federal Reserve
report to Congress. **Do not re-date the Fed corroboration upward** — it is August 2007
and is true as stated (audit advisory).
Both rows are **fund green** — these are the things that build the record.
Simultaneous peaks: +11.0 → k + r1 + foot + cut + r2 = **5** ✓; +16.0 → r1 + r2 + foot +
huge + sub = **5** ✓. One focal (`.huge`); bars are `.billrow` at 40px.
bg `s4.jpg` desk calendar (on-time payments) — calm under a 5-element scene, ken OUT.
Cut-in re-anchored from «your available credit» (char 160, +9.9) so it does **not**
collide with `#s4r2`'s own cue at +11.0 — same fix the hi cut made on its s4 cut-in.

### s5 · AUDIT — what destroys it · THE HERO SCENE · en5 (clip 17.398s) · photo (calm), ken IN · tint red .13

DOM: `#s5k .kicker` (exits) · `#s5track` (**the hero focal**: `.track2` with **7 year-ticks**, `.fill2` sweeping left→right) · `#s5mark` (the `--warn` slam at year zero) · `#s5ctr .counter.warn` ("YEAR 1 → YEAR 7") · `#s5cut` ink-blot cut-in (exits) · `#s5chip .chip.warn` (exits) · `#s5f .foot` · `#s5fix1 .sub.muted` (struck) · `#s5fix2 .sub.warn`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s5k` "What destroys it" | `rise` | scene open |
| 2 | +2.7 | A | `#s5track` frames in — 7 empty year-ticks | `pop .6` | «Under federal law,» (char 41) |
| 3 | +4.2 | A | `#s5mark` **slams `--warn` at year zero** and stays lit | `pop .35` + `pulse` | «most negative information» (char 67) |
| 4 | +4.6→+15.5 | F | `#s5track` `.fill2` sweeps left→right **past** the lit mark | `fill`, continuous | **runs the whole scene** |
| 5 | +5.6 | A | `#s5cut` ink-blot cut-in (the mark on the page) | `fade .5` | «on your report» (char 91) |
| 6 | +6.0 | F | **exit** `#s5k` fade .4 | `fade` | kicker's job done |
| 7 | +6.6 | A | `#s5ctr` "YEAR 1 → YEAR 7" begins under the track | `countUp` (runs to +15.5) | «for seven years.» (char 108) |
| 8 | +7.6 | A | `#s5chip` "BANKRUPTCY — 10 YEARS" (warn) | `pop .5` | «A bankruptcy, ten.» (char 127) |
| 9 | +8.2 | F | **exit** `#s5cut` fade .4 | `fade` | stay ≤6 |
| 10 | +8.6 | A | `#s5f` "Fair Credit Reporting Act, 15 U.S.C. §1681c(a) · CFPB" | `fade` | source line, holds to scene end |
| 11 | +11.2 | A | `#s5fix1` "clock starts when you pay it off" (muted) | `rise` | «the clock doesn't start» (char 190) |
| 12 | +12.6 | F | **exit** `#s5chip` fade .4 | `fade` | make room for the correction block |
| 13 | +12.9 | A | `#s5fix1` **strike-through draws** left→right | `fill .5` | «when you finally pay it off.» (char 219) |
| 14 | +13.9 | A | `#s5fix2` "CLOCK STARTS AT THE MISSED PAYMENT" (warn) | `pop .5` | «at the original missed payment.» (char 236) |
| 15 | +15.5 | F | fill crosses **YEAR 7**; `#s5mark` clears | `fade .4` | the record moves on — the miss finally does too |
| 16 | +16.5 | A | `#s5ctr` `pulse` on YEAR 7 + `#s5fix2` breathe to scene end | hold | «seven years of consequences.» (char 282) |

Reveal gaps: 2.3 · 1.5 · 1.4 · 1.0 · 1.0 · 1.0 · 2.6 · 2.7 — all ≥0.8 ✓ (cues 4, 13, 15,
16 are motions/state changes on elements already on screen; 6, 9, 12 are exits).

**The hero animation (script handoff #6, creator brief).** Seven year-ticks. The mark
slams at year **zero** — the original delinquency, not the payoff — and stays lit while
the fill sweeps *past* it, which is the entire argument: the record moves on, the miss
doesn't. The mark only clears when the fill crosses YEAR 7. **The track must be in motion
at every point in the scene** (§5.2); the longest gap between motion events is 2.6s and
is covered by the continuous fill + counter. Surplus from a longer clip goes into the
fill stagger and the counter, never into a faster reveal.

**This scene is 18.798s, ~2.9s shorter than the script paced for.** Every offset above is
derived from the measured 17.398s clip. Do **not** scale the script's numbers — fin-voice
measured en5 at −14.4% against the estimate, the largest drift in the video.

**Focal handling:** the track is the focal and there is **no `.huge` and no `.mega`** on
this scene. The correction block reveals **after** the mark lands (+11.2 vs +4.2), per
handoff #6 — one focal moment at a time.

**The `≤6` advisory (audit) is closed by three exits.** Peaks: +8.6 → track + mark + ctr +
chip + foot = **5** ✓; +13.9 → track + mark + ctr + foot + fix1 + fix2 = **6** ✓ (chip
exited at +12.6, kicker at +6.0, cut-in at +8.2). Without those exits this scene sits at
8 elements — do not reinstate any of them at build.

Colour is the whole point here: the mark and the counter **warn red** (they count what the
miss costs), the corrected rule **warn** (it is the trap being exposed), the struck wrong
version **muted**. If the year-zero mark ever renders green the scene inverts its thesis.
Chip char check: `BANKRUPTCY — 10 YEARS` = **21** ✓ ≤22.
bg `s5.jpg` hourglass — calm and thematic, the track carries the scene, ken IN.
**Never "forever", never "seven years from when you pay it off", and never "thirty-six
months"** (that is the India cut's figure and has no US basis).

### s6 · ACTION — auto-pay every due date · en6 (clip 18.704s) · photo, ken OUT · tint green .10

DOM: `#s6k .kicker` (exits) · `#s6h .huge.fund` ("AUTO-PAY" + inline `.sub` "every single due date", exits) · `#s6flow` (**one** `.row` element, 3 nodes revealed by internal `popEach`, `→` CSS-drawn, exits) · `#s6cut` wall-clock cut-in (exits) · `#s6stamp .stamp.fund` (exits) · `#s6u .sub` · `#s6u2 .decision`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s6k` "The fix" | `rise` | scene open |
| 2 | +3.2 | A | `#s6h` "AUTO-PAY" + "every single due date" (fund) | `pop .7` | «auto-pay.» (char 43) |
| 3 | +4.2 | A | `#s6flow` node 1 "EVERY CARD" | `pop .5` | «every card» (char 58) |
| 4 | +5.2 | A | node 2 "EVERY LOAN" | `pop .5` | «every loan» (char 73) |
| 5 | +8.3 | A | node 3 "AUTO-PAY or CALENDAR ALERT" | `pop .5` | «a calendar alert» (char 119) |
| 6 | +9.0 | F | **exit** `#s6k` fade .4 | `fade` | kicker's job done |
| 7 | +10.0 | A | `#s6cut` wall-clock cut-in | `fade .5` | «every single due date.» (char 146) |
| 8 | +11.6 | F | **exit** `#s6cut` fade .4 | `fade` | clear for the stamp |
| 9 | +12.4 | A | `#s6stamp` "REMEMBERING ISN'T YOUR JOB" (fund) | `pop .6` + `pulse` | «Remembering shouldn't be your job.» (char 181) |
| 10 | +14.2 | F | **exit** `#s6h` + `#s6flow` + `#s6stamp` fade .4 | `fade` | clear for the utilisation beat |
| 11 | +14.9 | A | `#s6u` "Use a **SMALL** share of the limit" (fund span on SMALL) | `rise` | «use a small share» (char 219) |
| 12 | +17.4 | A | `#s6u2` "PAY THE FULL BALANCE → not the minimum" | `pop .5` | «pay the full balance,» (char 257) |

Reveal gaps: 2.8 · 1.0 · 1.0 · 3.1 · 1.7 · 2.4 · 2.5 · 2.5 — all ≥0.8 ✓.
**The hi cut's 0.7s `popEach` cascade is retired** — Brian spaces the three flow nodes
1.0s / 3.1s apart, so they anchor to their own words. The 3.1s window before node 3 is
covered by continuous `ken` + the `#s6h` breathe.

> **Layout note (≤6 elements — ported from hi s6).** A literal flow is 3 nodes + 2 arrows
> = 5 elements, which with the kicker, huge, cut-in, stamp and two subs blows the cap.
> `#s6flow` is therefore **one `.row` element** whose three nodes reveal via an internal
> `popEach` (counts as 1), arrows drawn as CSS `::after` per §4 — `→` is not typed, it is
> absent from the font subset.

> **The colour check that matters on this scene.** `#s6u2`'s "not the minimum" is
> **`--muted`**, not `--warn`; green sits on `FULL`. In *this* video red belongs to the
> missed payment and its price. Rendering the minimum red would import
> `good-debt-vs-bad-debt`'s thesis into a video that never argues it.

**The VO says "second habit", not "thirty percent"** (audit edit 4) — the 30% is verified
as a *score weight* (en4), and parking it next to a utilisation instruction silently
asserts the folk "keep utilisation under 30%" rule that no source in this file supports.
**No percentage appears anywhere on s6**, and none may be added at build.
Green sits on AUTO-PAY, the flow, the stamp, SMALL and FULL — the whole constructive path.
Simultaneous peaks: +10.0 → h + flow + cut = **3** ✓; +12.4 → h + flow + stamp = **3** ✓;
+17.4 → u + u2 = **2** ✓.
bg `s6.jpg` sticky notes (object-led "reminders"), ken OUT. **No phone-screen photo** —
the reminder beat is carried by flow-node *text* and the wall-clock cut-in (§7, shipped
wrong 3×).

### s7 · THE MATH — same car, about three times the rate (densest) · en7 (clip 26.749s, longest) · photo (calmest), ken IN · tint red .12

DOM: `#s7k .kicker` (exits) · `#s7setup .sub` (exits) · `#s7loan .sub` (exits) · `#s7cut` dealership cut-in (exits) · `#s7band1 .decision.fund` (exits) · `#s7band2 .decision.warn` (exits) · `#s7r1 .billrow.warn` (exits) · `#s7r2 .billrow.total.warn` (exits) · `#s7f .foot` · `#s7q .huge.warn` (the punch, focal)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s7k` "Now the money" | `rise` | scene open |
| 2 | +2.6 | A | `#s7setup` "SAME CAR · SAME PRICE · TWO SCORES" | `rise` | «same price,» (char 36) |
| 3 | +6.2 | A | `#s7loan` "$25,000 used car · 72 months" | `rise` | «a twenty-five-thousand-dollar» (char 93) |
| 4 | +8.0 | A | `#s7cut` used-car-dealership cut-in | `fade .5` | «used car on a six-year loan.» (char 122) |
| 5 | +9.1 | A | `#s7band1` "TOP CREDIT TIER  ~6%  →  $418/mo" (fund) | `rise .4` | «Top credit tier:» (char 139) |
| 6 | +11.0 | F | **exit** `#s7k` + `#s7cut` fade .4 | `fade` | stay ≤6 |
| 7 | +11.7 | A | `#s7band1` `pulse` on `~6%` | hold | «around six percent.» (char 181) |
| 8 | +13.3 | A | `#s7band2` "SUBPRIME  ~19%  →  $590/mo" (warn) | `pop .5` + `pulse` | «Subprime: around nineteen» (char 207) |
| 9 | +15.5 | A | `#s7band2` `pulse` on `~19%` | hold | «roughly three times the interest» (char 242) |
| 10 | +17.6 | F | **exit** `#s7setup` + `#s7loan` fade .4 | `fade` | clear the deck for the reveals |
| 11 | +18.8 | A | `#s7r1` "EXTRA EVERY MONTH  $172" (warn) | `rise .4` + `countUp` | «a hundred seventy dollars» (char 295) |
| 12 | +21.6 | A | `#s7r2` "EXTRA INTEREST  $12,400" (warn `.total`) | `pop .5` + `countUp` | «around twelve thousand» (char 339) |
| 13 | +23.6 | F | `#s7f` "Experian tier averages — illustrative band, not a quoted rate · payments are model output" | `fade` | source line, holds to scene end |
| 14 | +24.9 | F | **exit** `#s7band1` + `#s7band2` + `#s7r1` + `#s7r2` fade .4 | `fade` | clear for the punch |
| 15 | +25.5 | A | `#s7q` "SAME CAR. DIFFERENT NUMBER." (warn) | `pop .7` | «Same car.» (char 402) |
| 16 | +26.9 | A | `#s7q` `pulse` + breathe to scene end | hold | «Different number.» (char 421) |

Reveal gaps: 2.2 · 3.6 · 1.8 · 1.1 · 4.2 · 5.5 · 2.8 · 2.0 · 1.9 — all ≥0.8 ✓ (cues 7, 9,
16 are `pulse` holds; 6, 10, 14 are exits). This closes the audit's "en7 reveal rows carry
no declared gap" advisory: **the two reveal rows are 2.8s apart, anchored to their own
dollar figures.**

> ### STANDING BAN — no FICO band number anywhere on this scene
> The Experian tier grid these APRs come from is **VantageScore 4.0-based** (its own
> source note), while `#s3scale` draws the **FICO** 300–850 scale. Putting a score
> number next to these rates is a cross-model conflation of the same family as the
> cross-market trap this run exists to stop. The audit killed it once in the script;
> it may not come back through the layout.
> **`#s7band1` says `TOP CREDIT TIER`, `#s7band2` says `SUBPRIME` — no `781+`, no `670`,
> no numeral from the score scale, in copy, in a foot, or in an image.** `#s3g1`'s `670+`
> lives 78 seconds earlier and the two are never on screen together.

**No decimal APR, no quarter label, no lender name** (facts-staging Claim USD-4 on-screen
rule). `~6%` and `~19%` only. **Never present the ~3× multiple as something Experian
said** — the page carries no "three times higher" sentence; the multiple is arithmetic on
its two used-car rows (19.42 ÷ 6.30 = 3.08), and the VO states it as arithmetic.

**The four integers are build-calculator output, displayed not spoken.** Regenerate
`$418` / `$590` / `$172` / `$12,400` from `EMI = P·i·(1+i)ⁿ/((1+i)ⁿ−1)`, P = $25,000,
n = 72, i = APR/12 at 6.30% and 19.42% (handoff #5; the audit re-derived all four by hand
and they match). `Intl.NumberFormat("en-US")` grouping. **Round each payment first
($590 − $418 = $172)** — rounding the *difference* prints $173 and disagrees with the
screen (audit advisory). The VO stays the round anchor whatever the calculator returns.

**The `≤6` advisory (audit) is closed by three exit waves.** Peaks: +9.1 → k + setup +
loan + cut + band1 = **5** ✓; +13.3 → setup + loan + band1 + band2 = **4** ✓; +23.6 →
band1 + band2 + r1 + r2 + foot = **5** ✓; +25.5 → foot + q = **2** ✓. Maximum **5** — the
scene never reaches the cap. Do not remove an exit wave to "let the numbers breathe".
Colour: top tier **fund**, subprime row and both extra-cost rows **warn**, punch **warn**
— the price of the miss, exactly per the table.
bg `s7.jpg` car key — **calmest bg, densest scene**; the numbers carry it, ken IN,
background nearly still. Cut-in `s7-cut.jpg` a used-car lot on «used car».
**Sweep both photos for non-US plates, signage and right-hand-drive vehicles** — a foreign
coin shipped in the first en cut.

### s8 · DO THIS TODAY · en8 (clip 19.174s) · photo, ken OUT · tint orange .12

DOM: `#s8stamp .stamp.pop` · `#s8b1 .decision.fund` · `#s8b2 .decision.fund` · `#s8disp .sub` (exits) · `#s8cut` red-pen cut-in (exits) · `#s8f .foot.muted`

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s8stamp` "DO THIS TODAY" (pop) | `pop .6` + `pulse` | scene-open slam («So, two moves today») |
| 2 | +3.2 | A | `#s8b1` "1  PUT EVERY DUE DATE ON AUTO-PAY" (fund) | `pop .5` | «every due date» (char 45) |
| 3 | +5.4 | A | `#s8b1` `pulse` | hold | «before you close this video.» (char 86) |
| 4 | +7.9 | A | `#s8b2` "2  PULL YOUR CREDIT REPORT AND READ IT" (fund) | `pop .5` | «pull up your credit report» (char 119) |
| 5 | +9.3 | A | `#s8b2` `pulse` | hold | «and actually read it;» (char 141) |
| 6 | +12.7 | A | `#s8disp` "A late mark or an account that isn't yours? Dispute it." | `rise` | «that isn't yours,» (char 196) |
| 7 | +13.6 | A | `#s8cut` red-pen cut-in | `fade .5` | «dispute it.» (char 208) |
| 8 | +15.6 | F | **exit** `#s8cut` fade .4 | `fade` | stay ≤6 |
| 9 | +16.0 | A | `#s8f` "A score is built over months and years — start long before you need the loan" | `rise` | «A score is built over months and years,» (char 248) |
| 10 | +17.0 | F | **exit** `#s8disp` fade .4 | `fade` | close on the two moves + the foot |
| 11 | +18.4 | A | `#s8f` `pulse` | hold | «before you need the loan.» (char 286) |

Reveal gaps: 2.8 · 4.7 · 4.8 · 0.9 · 2.4 — all ≥0.8 ✓. This closes the audit's "en8's two
numbered blocks carry no declared gap" advisory: **they are 4.7s apart**, each anchored to
its own instruction, and the two `pulse` holds (cues 3 and 5) fill the windows so nothing
sits static past ~2s.

**`#s8free` from the hi skeleton is DELETED and may not be reinstated.** The USD SET has
**no free-report line**; the annual-free-report right in the hi cut is an *India regulator*
claim and does not transfer. The VO says "pull up your credit report", full stop — **no
"free", no "once a year", no "weekly", no site name**. No sourced line, no number.

Stamp is **pop orange** (the CTA register); both action blocks **fund green** (behaviours
that build the record). The dispute line is neutral `.sub` — a wrong entry is a
correction, not the trap.
Simultaneous peaks: +13.6 → stamp + b1 + b2 + disp + cut = **5** ✓; +16.0 → stamp + b1 +
b2 + disp + foot = **5** ✓; after +17.0 → stamp + b1 + b2 + foot = **4** ✓.
bg `s8.jpg` desk lamp over paper, ken OUT. Cut-in on the one concrete action the VO names,
«dispute it» → a red pen marking a line.

### s9 · RECAP + CTA · en9 (clip 18.207s) · photo (calm closer), ken IN · tint green .13

DOM: `#s9k .kicker` (exits) · `#s9a`–`#s9d .chip` (2×2 rows: a+b / c+d) · `#s9cta .cta` (`▶` CSS-drawn, pop block)

| # | cue | class | element | motion | lands on |
|---|---|---|---|---|---|
| 1 | +0.40 | F | `#s9k` "Straight talk" | `rise` | scene open |
| 2 | +3.5 | A | `#s9a` READ BEFORE YOU ARE (ink) | `pop .45` | «reads your report» (char 48) |
| 3 | +7.0 | A | `#s9b` ON-TIME BUILDS IT (fund) | `pop .45` | «and a low balance» (char 104) |
| 4 | +9.7 | A | `#s9c` ONE MISS = 7 YEARS (warn) | `pop .45` | «for seven years.» (char 147) |
| 5 | +12.5 | A | `#s9d` WEAK SCORE = 3× RATE (warn) | `pop .45` | «charges you triple» (char 190) |
| 6 | +13.6 | F | **exit** `#s9k` fade .4 | `fade` | make room for the cta |
| 7 | +15.7 | A | `#s9cta` "▶ SUBSCRIBE" (pop block) | `pop .6` | «Then don't say nobody warned you.» (char 241) |
| 8 | +17.9 | A | `#s9cta` `pulse` + breathe to scene end | hold | «hit subscribe.» (char 276) |

Reveal gaps: 3.1 · 3.5 · 2.7 · 2.8 · 3.2 — all ≥0.8 ✓.
Recap chip char check (≤22): a **19** · b **17** · c **18** · d **20** ✓, 2 per row ✓.
Chip colours track the thesis: b **fund** (on-time builds), c and d **warn** (the miss and
its price), a **neutral ink** (a fact, not a verdict).
**`WEAK SCORE = 3× RATE` carries no score number** — it names the *band* in words, per the
standing ban above. The `×` glyph is a build check (Placeholders).
Video closes on the `.cta` — no logo outro.
Simultaneous: kicker + 4 chips = 5; after the exit, 4 chips + cta = **5** ✓.
bg `s9.jpg` highway at sunrise — calm object-led closer (the road the report opens),
ken IN. **Not a person** — both shipped en cuts closed on a young man with a phone; §7
bars the reuse and a face fights the CTA type.

---

## Timing (measured — `timing.json` values VERBATIM, never hand-edited)

`scene_duration = 0.4 (VO lead-in) + clip + 1.0 (tail)` · `audio_start = scene_start + 0.4`
The same numbers live in four places (`<section>` attrs, JS `S` map, `<audio>` row, root
`data-duration`) — generate all four from `timing.json`, never hand-edit. Updating three
of four passes every check and ships a broken timeline.

| scene | VO | clip (s) | scene dur | scene start | audio start |
|---|---|---|---|---|---|
| s1 | en1 | 14.707 | 16.107 | 0.000 | 0.400 |
| s2 | en2 | 9.326 | 10.726 | 16.107 | 16.507 |
| s3 | en3 | 20.062 | 21.462 | 26.833 | 27.233 |
| s4 | en4 | 16.300 | 17.700 | 48.295 | 48.695 |
| s5 | en5 | 17.398 | 18.798 | 65.995 | 66.395 |
| s6 | en6 | 18.704 | 20.104 | 84.793 | 85.193 |
| s7 | en7 | 26.749 | 28.149 | 104.896 | 105.296 |
| s8 | en8 | 19.174 | 20.574 | 133.046 | 133.446 |
| s9 | en9 | 18.207 | 19.607 | 153.620 | 154.020 |
| **total** | | **160.627** | | | **173.227** |

## Image slots (→ `assets/img/manifest.json`)

**17 slots — 9 bg (every scene) + 8 cut-ins.** All object-led — no phone screens, no faces.

> **Queries are 1–3 nouns, deliberately.** `fin-assets-hi-1.md` measured it: the hi cut's
> 6-to-9-word descriptive queries fell back to whatever matched a single weak token
> (`paper`, `book`, `page`) and landed **5 of 17** in round 1; shortening to the one
> strong noun recovered **9 of 12** retries and produced the best images in the set. The
> long phrasing reads well in a storyboard table and is actively harmful as a search
> string, and the `#N` retry knob cannot fix a broken query. **The "what it must show"
> column is the acceptance test; the query column is what goes in the manifest.**

| slot | query | scene · role | must show / must not |
|---|---|---|---|
| `s1.jpg` | `filing cabinet` | s1 · bg | drawers/tabs, dark. **md5 vs hi `s1.jpg` `14bc6463`** |
| `s1-cutA.jpg` | `unopened mail` | s1 · cut-in «a file on you» | stacked envelopes, no hands |
| `s1-cutB.jpg` | `contract` | s1 · cut-in «The lender reads it» | paper + pen. **Reject handshakes/faces** |
| `s2.jpg` | `cardboard boxes` | s2 · bg (**calmest in the video**) | stacked storage boxes, shadowed |
| `s3.jpg` | `pressure gauge` | s3 · bg | an analog dial + needle (the scale read) |
| `s3-cut.jpg` | `odometer` | s3 · cut-in «one three-digit number» | digits close-up, no dashboard brand |
| `s4.jpg` | `desk calendar` | s4 · bg (calm) | a date grid. **md5 vs hi `s5-cut.jpg` `bb2ac44c`** — highest collision risk in the set; fallback `daily planner` |
| `s4-cut.jpg` | `leather wallet` | s4 · cut-in «your available credit» | an unbranded wallet. **Deliberately NOT `credit cards`** — the hi run measured `MasterCard`×4 + `Payoneer` legible on both attempts |
| `s5.jpg` | `hourglass` | s5 · bg (**calm — the track carries the scene**) | glass + sand on a dark surface |
| `s5-cut.jpg` | `ink blot` | s5 · cut-in «on your report» | a black mark on a white page |
| `s6.jpg` | `sticky notes` | s6 · bg | notes on a board. **No phone screen** |
| `s6-cut.jpg` | `wall clock` | s6 · cut-in «every single due date» | a clock face, no brand. **md5 vs hi `s6.jpg` `5153cf85`** |
| `s7.jpg` | `car key` | s7 · bg (**calmest, densest**) | one key on a dark surface. **md5 vs hi `s7-cut.jpg` `a43e2d5b`** (that hit was a keyring *with a car fob*) — real collision risk; fallback `car headlight` |
| `s7-cut.jpg` | `car dealership` | s7 · cut-in «used car» | a row of cars. **Sweep for non-US plates, signage, RHD** |
| `s8.jpg` | `desk lamp` | s8 · bg | lamp over printed pages |
| `s8-cut.jpg` | `red pen` | s8 · cut-in «dispute it» | a pen marking paper. **md5 vs hi `s8-cut.jpg` `5b0a0e72`** |
| `s9.jpg` | `highway sunrise` | s9 · bg (calm closer) | open road, low sun. **Not a person** |

### Image-sourcing notes (design §7 — load-bearing)

- **Five named collision risks against `credit-history-hi`** (same slug, adjacent search
  intent — the hi cut's 14 hashes are listed in `logs/fin-assets-hi-1.md`): `s4` vs its
  `calendar`, `s7` vs its `house key`, `s6-cut` vs its `pocket watch`, `s8-cut` vs its
  checklist pen, `s1` vs its archive shelves. **md5 each against both channels before
  accepting**; fallbacks are named in the table for the two worst.
- **Already burned by the two shipped en cuts** (handoff #4): `hand tapping phone banking
  app`, `young man … phone`, `stack of dollar bills flat-lay`, `dark desk with calculator
  and notepad`. Nothing here goes near them.
- **A cut-in may be dropped rather than faked; a background may not.** If a cut-in slot
  cannot be sourced clean in the retry ladder, drop it and remove its cue — the scene
  keeps its bg. `photo_free_scene_ratio` is 0 and there is no exception.
- **No brand marks.** The wallet substitution for "credit cards" is the direct lesson from
  the hi run; check the odometer and the wall clock for legible makes too.
- **No faces.** `contract` and `car dealership` are the two slots most likely to return
  people — reject and retry rather than crop a face into the frame.
- **Check what the picture is saying** — a *rising* chart under s5 (the destruction scene)
  or a luxury car under a subprime row argues against the script.

## `-en` divergence from the hi master skeleton (one row per scene — mandatory)

Element IDs are ported **verbatim** (`s1k`, `s1q`, `s1cutA/B`, `s1d1–3`, `s1stamp`, `s2a–d`,
`s3k`, `s3e1–3`, `s3rec`, `s3ha/hb`, `s3scale`, `s3g1`, `s4r1/r2`, `s4cut`, `s5k`, `s5ctr`,
`s5cut`, `s5f`, `s6h`, `s6flow`, `s6stamp`, `s6u/u2`, `s7band1/2`, `s7r1/r2`, `s7q`,
`s8stamp`, `s8b1/b2`, `s9a–d`, `s9cta`) so fixes travel between cuts. New IDs appear only
where the element itself is different in kind: **`#s5track`, `#s5mark`, `#s5fix1/2`,
`#s4q`.** Deleted: **`#s3g2`, `#s4r3`, `#s4r4`, `#s5grid`, `#s5q`, `#s8free`.**

| scene | diverges how | why |
|---|---|---|
| s1 | US decision strip (`THE LOAN? / THE RATE? / EVER SEEN IT?` vs `LOAN? / INTEREST? / YOU'VE SEEN IT?`); stamp `A MISS CAN STAY 7 YEARS` vs `EVERY MISSED EMI IS IN IT`; every offset re-derived on a **14.707s** clip (hi h1 = 17.162s) — payoff +3.2→**+3.0**, naming beat +14.2→**+11.6**, stamp +15.5→**+13.7**. | FCRA 7-year window replaces the CIBIL 36-month one; audit edit 3 softened "every miss stays" to the statute's *can*; Brian reads 16.11 c/s vs Harsh's 12.61, so no anchored offset survives the port. |
| s2 | Clip **9.326s vs hi 11.598s** → chip anchors compress to +2.2…+6.2; sub reads `Then two moves for today`; bg cardboard boxes replaces tied document bundles. | Shorter English line; hash distinctness from the hi bg. |
| s3 | Scale is **300–850** (FICO), not 300–900 (CIBIL); **`#s3g2` deleted** — `670+ = "good"` stands alone; the 3 enumeration chips are **anchored, not a 0.7s cascade**; foot cites **FICO + CFPB**, not TransUnion CIBIL. | Different scoring model entirely; fin-audit killed `upper 700s = best offers` (source backs band *names* only, and the only tier evidence is VantageScore-based); Brian spaces the three nouns 1.2/0.9s. |
| s4 | **Largest divergence in the video.** hi's 4 ranked equal-width rows (`#s4r1–r4`, deliberately weightless) become **2 proportional weight bars** (35% / 30%) + a new `#s4q .huge.fund` `65% OF YOUR SCORE`; `#s4r3`/`#s4r4` deleted; the hi foot's "CIBIL publishes no percentage weights" guard is **inverted** — this foot cites FICO's *published* weights + the Fed corroboration. Script's 0.6s cascade retired for two fill-on-the-number anchors. | FICO publishes its category weights and CIBIL does not — the hi cut is *hard-forbidden* to show the exact numbers this scene is built on. Re-derived from `script-en.md`, never ported. |
| s5 | `#s5grid` (3×12 = 36 cells) → **`#s5track`** (7 year-ticks) + a discrete **`#s5mark`**; counter `MONTH 1 → MONTH 36` → **`YEAR 1 → YEAR 7`**; **new `#s5fix1/#s5fix2` correction block**; `#s5q` huge **deleted** (track + correction carry it); new `BANKRUPTCY — 10 YEARS` chip; whole scene re-timed into **18.798s**. | "36 months" is a CIBIL fact that does not travel; the FCRA clock-starts-at-the-delinquency correction is *this* cut's beat and has no hi counterpart; fin-voice measured en5 **−14.4%**, the largest drift in the cut, so scaling the hi offsets would miss by ~3s. Only the hero *shape* ports (fill sweeps past a lit mark). |
| s6 | Flow node 3 `AUTO-PAY or CALENDAR ALERT` (hi: `AUTO-DEBIT`); `#s6cut` is a **wall clock**, not a bank passbook; `#s6u2` reads `PAY THE FULL BALANCE` (hi: `FULL BILL`); the 0.7s `popEach` cascade retired for anchors at +4.2/+5.2/+8.3. | "Auto-debit" and the passbook are India-market words/objects (the hi assets run proved passbooks barely exist on Pixabay); Brian spaces the nodes ≥1.0s. |
| s7 | Full US model — `$25,000 · 72 months · ~6% / ~19% · $418 / $590 / $172 / $12,400` replaces `₹30,00,000 · 20 years · ~1pp`; `#s7band1/2` carry **rate + payment** where hi carried band names only; `en-US` grouping replaces `en-IN`; `#s7cut` re-anchored from the punch to **+8.0** on «used car»; a **third exit wave** added. | Different market and different instrument (used-car loan vs home loan); the hi cut's late cut-in anchor lands inside this cut's densest reveal window; the exits are the audit's `≤6` advisory, closed at a measured peak of 5. |
| s8 | **`#s8free` deleted** — no free-report right, frequency or cost anywhere; `#s8b1`/`#s8b2` **swap meaning** (auto-pay is move 1 here, pulling the report is move 2 — hi is the reverse); foot is the "built over months and years" line, not the RBI FFCR clause. | The USD SET carries no US free-report source and India's right does not transfer; en8's VO orders the two moves the other way round. |
| s9 | US recap chips (`ONE MISS = 7 YEARS`, `WEAK SCORE = 3× RATE` vs `ONE MISS = 36 MONTHS`, `LOW SCORE COSTS LAKHS`); closer bg is a highway at sunrise, not a doorway. | 7 years and the ~3× rate multiple are the US facts; hash distinctness from the hi doorway, and both shipped en cuts already burned the man-with-phone closer. |

**Every scene diverges.** Zero divergences would mean a translation wearing a layout
costume — the two markets have structurally different answers to this video's hero
question (7 years vs 36 months), and s4/s5/s7 are rebuilds, not ports.

## Deliberate placeholders (must be real before publish)

- **Every `A` offset is char-interpolated intent** against the measured clip. Refine with
  faster-whisper word timings at build (handoff #7). The one with a gate attached — s1's
  naming — now clears by ≈3.4s, so its re-check is a formality.
- **s7's four integers** (`$418` · `$590` · `$172` · `$12,400`) are build-calculator output,
  not storyboard constants. Regenerate from the EMI model; **round each payment before
  subtracting** ($590 − $418 = $172, never round(172.6)); `en-US` grouping.
- **s5's timeline is spec'd as behaviour, not markup.** The build owns the DOM; the
  invariants are: **7** year-ticks, fill sweeps left→right across the full scene, the
  mark slams at **year zero** on «most negative information» and stays lit, the fill
  continues *past* it, the mark clears only as the fill crosses YEAR 7, the correction
  block reveals **after** the mark.
- **`×` (U+00D7) in `#s9d`'s `WEAK SCORE = 3× RATE`.** The subset is documented as "Latin +
  punctuation + currency"; `→` and `▶` are confirmed absent and CSS-drawn. **Verify U+00D7
  with fontTools before build** — if missing, render `3x RATE` (chip stays 20 chars). Do
  not substitute a font (Archivo Black is already banned for dropping U+20B9/U+2192).
- **Image hashes** — no fetch has run; all 17 slots are unverified against the ledger, and
  5 carry named collision risks against `credit-history-hi`.

## Sign-off

- [x] Colour semantics table filled and derived from *this* video's thesis (red = the miss and its price; `#s6u2`'s "not the minimum" deliberately muted, not red)
- [x] Every number traced to a sourced line (`script-en.md` fact trace + `audit-en.md` check 1)
- [x] **STANDING BAN honoured** — no FICO band number anywhere near the Experian APRs; s7 names tiers in words only, and `#s3g1`'s `670+` is 78s away and never co-present
- [x] No `₹`, no "lakh", no CIBIL, no RBI, no "thirty-six months" anywhere in this file
- [x] Every scene carries a full-bleed bg photo (9 bg + 8 cut-ins = 17 slots); manifest queries are 1–3 nouns per the hi assets finding
- [x] Every reveal gap ≥0.8s and printed per scene; **no cascade declared anywhere** (audit advisory on en1/en7/en8 closed)
- [x] `≤6` simultaneous elements verified per scene — measured peaks s1 **5** · s2 **6** · s3 **5** · s4 **5** · s5 **6** · s6 **3** · s7 **5** · s8 **5** · s9 **5** (audit advisory on en5/en7 closed by declared exits)
- [x] All keyframes derived from the measured `timing.json` (173.227s), not the script's estimates
- [ ] No image hash reused from any prior video on either channel (check at fetch — 5 known-risk slots flagged)
- [ ] Creator approved (Gate ②) — date: __
