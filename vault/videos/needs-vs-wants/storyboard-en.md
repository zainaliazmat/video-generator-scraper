---
summary: Gate ② storyboard SPEC for «Needs vs Wants» US/English edition — every VO line → scene DOM, element IDs, GSAP motion calls, Pexels photo slots. Same composition skeleton as the Hindi cut; s1/s5/s7 differ because the US evidence is a survey gap, not an itemised bill.
updated: 2026-07-27
source: [[videos/needs-vs-wants/script-en]] + the shipped emergency-fund-en composition
---

# STORYBOARD — «Needs vs Wants» · English / USA

**Project:** `vault/videos/needs-vs-wants/src/en/` · **Script:** [[videos/needs-vs-wants/script-en]] · **Research:** [[knowledge/subscription-economics-2026]]
**Runtime target:** ~2:24 · **VO:** ElevenLabs Brian `nPczCjzI2devNBz1zQrb` · **Grade:** emergency-fund-en dark blockframe
**Canvas:** 1920×1080 · **Timeline:** single paused GSAP timeline on `window.__timelines["main"]`

## Relationship to the Hindi cut

Same nine-scene skeleton, same design system, same motion vocabulary, **same
element IDs** — so a fix in one composition ports to the other by hand in
minutes. Three scenes genuinely differ and must not be cloned:

| scene | Hindi | English | why |
|---|---|---|---|
| s1 hook | the blank `₹ ?` goes red | the blank `$ ?` + the **42% stat strip** | US has a hard survey stat; India doesn't |
| s5 audit | UPI AutoPay mandates, telecom bundle | iPhone / Google Play / PayPal | different plumbing entirely |
| s7 math | itemised bill → ₹24,564 | **guess-vs-reality gap** → $1,596 | different evidence shape (see below) |

Everything else is a text swap.

## Global guardrails

Identical to [[videos/needs-vs-wants/storyboard-hi]] §Global guardrails —
photo+scrim+grain per scene, alternating `ken()`, the nine fixed motion helpers,
every cue on its word, s2 and s7 photo-free. Read that section; it is not
repeated here.

## Colour semantics

Identical to the Hindi cut: `--fund` green = needs/keep/action, `--target` amber
= **wants** (legitimate), `--warn` red = **only** the leak, `--pop` = CTA.

## New CSS (beyond emergency-fund-en)

The `.decision` / `.v-*` rows from the Hindi storyboard, plus the gap table
instead of `.bill`:

```css
.gap      { display:flex; flex-direction:column; gap:16px; width:1200px; }
.gaprow   { display:flex; justify-content:space-between; font-size:48px; font-weight:800;
            padding:16px 30px; background:var(--panel); border:3px solid #2a3241; border-radius:14px; }
.gaprow.think  { border-color:var(--muted); }
.gaprow.real   { border-color:var(--target); }
.gaprow.thegap { border-color:var(--warn); color:var(--warn); font-size:60px; }
.statstrip { font-size:34px; font-weight:800; letter-spacing:1px; padding:14px 30px;
             border-radius:12px; background:rgba(239,68,68,.14); border:3px solid var(--warn); }
```

---

## Beats

### en1 · HOOK — the charge you forgot (~20.6s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.4 | `#s1k` "Quick question — be honest" | `rise` |
| 2 | +2.2 | `#s1q` "WHAT LEFT YOUR ACCOUNT **ON ITS OWN?**" | `pop` |
| 3 | +4.4 | `#s1amt` `$ ?` | `pop` + `breathe 3.2s` |
| 4 | +6.0 | `#s1a` GYM | `pop .45` + `fade #s1bgA` |
| 5 | +6.7 | `#s1b` STREAMING | `pop .45` |
| 6 | +7.4 | `#s1c` MUSIC | `pop .45` + `fade #s1bgB` |
| 7 | +8.1 | `#s1d` CLOUD | `pop .45` |
| 8 | +8.8 | `#s1e` DELIVERY PASS | `pop .45` |
| 9 | +10.6 | `#s1stat` "42% found a charge they'd forgotten" (`.statstrip`) | `rise` + `pulse` |
| 10 | +15.0 | `#s1amt` → `color:#ef4444` | `tl.to .3` + `pulse` |
| 11 | +18.4 | `#s1stamp` THE LEAK | `pop .6` + `pulse` — on "That's a leak" |

**Photos** `s1-gym.jpg` `s1-phone.jpg` `s1-bill.jpg`.
Pexels: `empty gym treadmills morning` · `man checking phone dark room` · `credit card statement close up`.

### en2 · ROADMAP (~10.0s) · **no photo**

Beats identical to the Hindi cut h2, chips: `THE HONEST TEST` · `THE 24-HOUR RULE` · `THE AUDIT` · `CUT WITHOUT PAIN`, sub `No big income required`. Cues +0.4 / +1.6 / +3.0 / +4.4 / +5.8 / +7.6.

### en3 · THE HONEST TEST (~14.4s) · photo, ken OUT

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s3k` "Survive vs enjoy" | `rise` |
| 2 | +1.4 | `#s3yl` NEED — TO SURVIVE | `rise .5 y20` |
| 3 | +3.0 | `#s3a` RENT | `pop .5` + `fade #s3bgA` |
| 4 | +3.6 | `#s3b` GROCERIES | `pop .5` |
| 5 | +4.2 | `#s3c` INSURANCE | `pop .5` |
| 6 | +4.8 | `#s3d` GAS | `pop .5` |
| 7 | +5.4 | `#s3e` MEDS | `pop .5` |
| 8 | +6.6 | `#s3nl` WANT — TO ENJOY (**amber**) | `rise .5 y20` + `fade #s3bgB` |
| 9 | +7.6 | `#s3x` STREAMING | `pop .5` |
| 10 | +8.2 | `#s3y` TAKEOUT | `pop .5` |
| 11 | +8.8 | `#s3z` NEW PHONE | `pop .5` |
| 12 | +10.6 | `#s3stamp` WANTS AREN'T THE ENEMY | `pop .55` + `pulse` |

**Photos** Pexels: `grocery cart supermarket aisle` · `takeout delivery bag on doorstep`.

### en4 · THE 24-HOUR RULE (~14.1s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +1.0 | `#s4num` `24` (`.mega.glow`, amber) | `pop .7` + `countUp 0→24 0.8s` |
| 2 | +1.8 | `#s4l` HOURS BEFORE YOU BUY | `rise` |
| 3 | +3.0 | `breathe #s4num 4.0s` | — |
| 4 | +4.4 | `#s4b1` ADD TO CART | `pop .5` |
| 5 | +5.2 | `#s4b2` WAIT | `pop .5` |
| 6 | +6.6 | `#s4b3` DECIDE | `pop .5` |
| 7 | +9.0 | `#s4stat` "7 out of 10 times you'll forget it" | `rise` + `pulse` |
| 8 | +12.0 | `#s4f` "Over $100? Wait 30 days." | `rise` |

**Photo** Pexels: `online shopping cart checkout phone`.

### en5 · THE AUDIT (~16.6s) · photo, ken OUT

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s5k` "Find every recurring charge" | `rise` |
| 2 | +2.0 | `#s5a` STATEMENTS — 3 MONTHS | `pop .5` + `fade #s5bgA` |
| 3 | +8.0 | `#s5b` IPHONE → SUBSCRIPTIONS | `pop .5` + `fade #s5bgB` |
| 4 | +9.6 | `#s5c` GOOGLE PLAY → SUBS | `pop .5` |
| 5 | +11.0 | `#s5d` PAYPAL → AUTO PAYMENTS | `pop .5` |
| 6 | +13.4 | `#s5stamp` WRITE THEM ALL DOWN | `pop .55` — on "that's where the ghosts hide" |
| 7 | +15.0 | `#s5f` "Annual plans hide — scan 12 months too" | `rise` |

**Photos** Pexels: `bank statement documents desk` · `iphone settings screen close up`.

### en6 · CUT WITHOUT MISERY (~20.6s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s6k` "Ask one question" | `rise` |
| 2 | +3.0 | `#s6q` USED IT IN THE LAST **30 DAYS?** | `pop .7` |
| 3 | +4.2 | `breathe #s6q 2.6s` | — |
| 4 | +6.6 | `#s6r1` `ZERO → CANCEL` | `pop .5` |
| 5 | +8.4 | `#s6r2` `ONCE → AD TIER / SHARE` | `pop .5` |
| 6 | +12.6 | `#s6r3` `DAILY → KEEP IT` | `pop .5` + `pulse` — on "guilt free" |
| 7 | +16.6 | `#s6stamp` ONE IN, ONE OUT | `pop .55` + `pulse` |
| 8 | +18.4 | `#s6f` "61% would quit their favorite service over a $5 hike — Deloitte 2026" | `rise` |

**Photo** Pexels: `family watching tv living room evening`.

### en7 · THE MATH (~23.8s) · **no photo** — the gap table is the visual

Different engine from the Hindi cut: not addition, **self-deception**. The two
numbers appear, the audience sees the distance, *then* the gap row lands.

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.4 | `#s7k` "Now the real math" | `rise` |
| 2 | +2.2 | `#s7stream` `STREAMING ALONE $69/mo · 4 SERVICES` | `rise` |
| 3 | +6.4 | `#s7add` "+ gym + apps + cloud" | `fade` |
| 4 | +9.0 | `#s7r1` `YOU THINK YOU SPEND — $86/mo` (`.think`) | `rise .5 y24` |
| 5 | +12.4 | `#s7r2` `YOU ACTUALLY SPEND — $219/mo` (`.real`) | `pop .6` + `pulse` |
| 6 | +14.2 | `.rule` | `fade .4` |
| 7 | +15.0 | `#s7gap` `THE GAP — $133/mo` (`.thegap`) | `pop .6` + `pulse` |
| 8 | +17.6 | `#s7counter` `$0` + `.track2` | `fade .5` |
| 9 | +17.6 | `fill #s7fill 2.6s` + `countUp s7c 0→1596 2.6s` | — | 12 ticks = 12 months |
| 10 | +21.4 | `#s7head` "= about **2 WEEKS** of take-home pay" | `rise` + `fade .targetc` |
| 11 | +22.8 | `#s7cap` "C+R Research · Deloitte Digital Media Trends 2026" | `rise` |

`.ticks` regenerated for **12** segments: `calc(100% / 12 - 2px)`.

> The `$86 → $219 → $133` reveal order is the retention mechanism. Do not show
> all three rows at once, and do not start the counter before the gap row lands.

### en8 · DO THIS TODAY (~11.6s) · photo, ken OUT

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.4 | `#s8stamp` DO THIS TODAY | `pop .6` |
| 2 | +2.0 | `#s8a` OPEN SUBSCRIPTION LIST | `pop .5` |
| 3 | +2.8 | `#s8arrow` → | `fade .3` |
| 4 | +4.0 | `#s8b` PICK THE ONE YOU FORGOT | `pop .5` |
| 5 | +4.8 | `#s8arrow2` → | `fade .3` |
| 6 | +5.6 | `#s8c` CANCEL IT (`.chip.warn`) | `pop .5` + `pulse` |
| 7 | +8.6 | `#s8t` `"someday" → **DONE**` | `rise` |

**Photo** Pexels: `hand tapping phone screen close up`.

### en9 · RECAP + CTA (~12.5s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.6 | `#s9a` NEED vs WANT | `pop .45` |
| 2 | +2.0 | `#s9b` WAIT 24H | `pop .45` |
| 3 | +3.4 | `#s9c` AUDIT QUARTERLY | `pop .45` |
| 4 | +4.8 | `#s9d` CANCEL ONE TODAY | `pop .45` |
| 5 | +8.6 | `#s9cta` ▶ SUBSCRIBE | `pop .6` + `pulse` |
| 6 | +9.6 | `#s9sub` "money basics that actually make sense" | `rise` |

**Photo** Pexels: `young man smiling relieved outdoors phone`.

---

## Master timing table (estimates — relock after VO)

| Scene | VO | est. dur | est. start |
|---|---|---|---|
| s1 Hook | en1 | 20.6 | 0:00.0 |
| s2 Roadmap | en2 | 10.0 | 0:21.6 |
| s3 Honest test | en3 | 14.4 | 0:32.6 |
| s4 24-hour rule | en4 | 14.1 | 0:48.0 |
| s5 Audit | en5 | 16.6 | 1:03.1 |
| s6 Cut without misery | en6 | 20.6 | 1:20.7 |
| s7 The math | en7 | 23.8 | 1:42.3 |
| s8 Do this today | en8 | 11.6 | 2:07.1 |
| s9 Recap + CTA | en9 | 12.5 | 2:19.7 |
| **total** | | | **~2:32** |

Same rule as the Hindi cut: +1.0s breath between scenes, VO audio at scene start
+ 0.4s, `data-track-index="10"`.

## Pattern-interrupt check

The hook runs 20.6s — the longest single scene before s7 and the highest-risk
stretch in the video. The chip cascade (beats 4–8) and the stat strip carry it,
but if watch-time dies anywhere it dies here. If the draft render feels slow,
**cut the hook VO, not the motion** — the fix is fewer words, not more animation.

## BUILT — 2026-07-27 · what changed from this spec

`index.html` is live and `npm run check` passes (0 errors). Deltas:

- **Real VO durations replaced every estimate.** Total **2:49.6** (spec guessed 2:32). `S = {…}` in `index.html` is the source of truth.
- **Cues computed from character position inside each line**, same method as the Hindi cut.
- **`en7` runs 29.7s — the longest scene in either video**, 6s over spec. It carries five reveals ($69 → +extras → $86 → $219 → the gap) before the counter, so it holds, but it is the first place to trim if the audit flags a sag.
- **Take-home anchor is $4,000/mo**, matching [[knowledge/money-facts-2026]]. Payoff is **12 DAYS of pay** — exact, replacing the spec's rounded "about 2 weeks".
- **`s3` gained a fifth need chip (MEDS)** to match the VO's five spoken items.
- Photos are **Pixabay**, not Pexels — see the Hindi storyboard's build note.

### The localization catch this cut needed
`s1-bill.jpg` came back as an **Australian bank statement** — `.com.au` and
"Teller use Only" legible through the grade. That is precisely the failure
[[knowledge/us-english-script-style]] was written about after the first
emergency-fund-en shipped with rupees in it. Refetched to "dollar bills money
cash". **Every `-en` photo needs a currency/signage sweep at frame level, not
at query level** — the query said nothing about Australia.

### Render — 2026-07-27
**UPLOAD MASTER: `renders/FINAL-1080p-en.mp4`** — 250.8 MB · **2:49.6** · 1920×1080 · H.264 High
yuv420p · **12.22 Mbps** · 30fps · AAC-LC 48 kHz stereo · peak −3.4 dBFS / mean −24.9. Rendered
with `-q high --video-bitrate 12M` in 12m 58s. First pass at default quality was 2.9 Mbps — see
the Hindi storyboard's render note for why that isn't good enough to upload.

## Known non-issue

Same `✗ #s3stamp` contrast warning as the Hindi cut, same cause, same verdict —
the frames show it legible. Don't lighten the stamp text.

## Still open

- BGM not chosen.
- Thumbnail not made.
- [[workflows/video-audit]] pass on the finished render.

## Sign-off

- [x] Built and checked — 2026-07-27
- [ ] Creator approved the render
