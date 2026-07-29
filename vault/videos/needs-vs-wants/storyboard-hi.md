---
summary: Gate ② storyboard SPEC for «Needs vs Wants» Hindi/India edition — every VO line → scene DOM, element IDs, GSAP motion calls, Pexels photo slots and the new CSS the emergency-fund design system doesn't already have. Sign off before index.html is written.
updated: 2026-07-27
source: [[videos/needs-vs-wants/script-hi]] + the shipped emergency-fund composition (design system + motion vocabulary)
---

# STORYBOARD — «Needs vs Wants» · Hindi / India

**Project:** `vault/videos/needs-vs-wants/src/hi/` · **Script:** [[videos/needs-vs-wants/script-hi]] · **Research:** [[knowledge/subscription-economics-2026]]
**Runtime target:** ~2:35 · **VO:** ElevenLabs Vikram S `st8o4LADtfxckX2PH08x` · **Grade:** emergency-fund dark blockframe
**Canvas:** 1920×1080 · **Timeline:** single paused GSAP timeline on `window.__timelines["main"]`

## Global guardrails (inherited from the shipped emergency-fund composition)

- One photo per scene behind the block, `.bg` + `.scrim` + `.grain`, `filter: grayscale(.32) brightness(.62) contrast(1.05)` — nine photos must read as one film.
- Every scene gets a `ken()` drift, direction **alternating** in/out scene to scene. Never two pushes in a row.
- Motion vocabulary is fixed — reuse the helpers verbatim: `rise` `pop` `popEach` `countUp` `fill` `fade` `pulse` `breathe` `ken`. No new eases.
- **Every cue lands on the word that says it.** Offsets below are the *design intent*; the real numbers come from faster-whisper word timings after VO generation (see Build order §4).
- Scene 2 and scene 7 carry **no photo** — clean panel. Density needs a rest, and s7's bill IS the visual.
- No product recommended. Platform names appear as price evidence only.

## Colour semantics — one deliberate change from emergency-fund

emergency-fund used red = bad. Here the whole thesis is *wants aren't the enemy*, so:

| token | meaning here |
|---|---|
| `--fund` green | needs, kept things, the correct action |
| `--target` amber | **wants** — legitimate, just labelled |
| `--warn` red | **only** the leak: forgotten charges, the annual number |
| `--pop` orange | the CTA / DO THIS TODAY stamp |

If a want ever renders red, the video argues against its own script.

## New CSS (not in emergency-fund — add to `<style>`)

```css
.bill      { display:flex; flex-direction:column; gap:14px; width:1100px; }
.billrow   { display:flex; justify-content:space-between; font-size:44px; font-weight:800;
             padding:14px 28px; background:var(--panel); border:3px solid #2a3241; border-radius:14px; }
.billrow.total { border-color:var(--warn); color:var(--warn); font-size:56px; }
.rule      { height:5px; background:#2a3241; width:1100px; }
.decision  { display:flex; align-items:center; gap:22px; font-size:40px; font-weight:800; }
.decision .verdict { padding:10px 26px; border-radius:999px; }
.v-cancel  { background:var(--warn);   color:#0d1017; }
.v-down    { background:var(--target); color:#0d1017; }
.v-keep    { background:var(--fund);   color:#0d1017; }
```

---

## Beats

Offsets are seconds **inside** each scene. `Sn` = scene start.

### h1 · HOOK — the auto-debit you don't remember (~15.5s) · photo, ken IN

| # | cue | element | motion | note |
|---|---|---|---|---|
| 1 | +0.4 | `#s1k` "Quick question — be honest" | `rise` | |
| 2 | +1.8 | `#s1q` "WHAT LEFT YOUR ACCOUNT **ON ITS OWN?**" | `pop` | `.huge`, warn span |
| 3 | +3.6 | `#s1amt` `₹ ?` | `pop` + `breathe 3.2s` | the blank sits there taunting |
| 4 | +5.2 | `#s1a` GYM | `pop .45` + `fade #s1bgA` | on «जिम» |
| 5 | +5.9 | `#s1b` OTT | `pop .45` | on «नेटफ्लिक्स» |
| 6 | +6.6 | `#s1c` MUSIC | `pop .45` + `fade #s1bgB` | |
| 7 | +7.3 | `#s1d` CLOUD | `pop .45` | |
| 8 | +8.0 | `#s1e` FOOD PASS | `pop .45` + `fade #s1bgC` | |
| 9 | +9.6 | `#s1amt` → `color:#ef4444` | `tl.to .3` + `pulse` | on «याद है?» — the blank goes red |
| 10 | +14.0 | `#s1stamp` THE LEAK | `pop .6` + `pulse` | on «चुपचाप आपकी सैलरी खा रही है» |

**Photos** `s1-gym.jpg` → `s1-phone.jpg` → `s1-bill.jpg` (crossfade under the chips).
Pexels: `empty gym treadmill morning` · `indian man phone screen night` · `bank statement paper close up`.

### h2 · ROADMAP (~8.7s) · **no photo**, panel only

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.4 | `#s2k` "By the end you'll know" | `rise` |
| 2 | +1.4 | `#s2a` THE HONEST TEST | `rise .5 y30` |
| 3 | +2.6 | `#s2b` THE 24-HOUR RULE | `rise .5 y30` |
| 4 | +3.9 | `#s2c` THE AUDIT | `rise .5 y30` |
| 5 | +5.1 | `#s2d` CUT WITHOUT PAIN | `rise .5 y30` |
| 6 | +6.8 | `#s2sub` "No big income required" | `rise` |

### h3 · THE HONEST TEST (~17.7s) · photo, ken OUT

Two-column `.cols` block — reuse emergency-fund s3 geometry, recolour per the table above.

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s3k` "Survive vs enjoy" | `rise` |
| 2 | +1.6 | `#s3yl` NEED — TO SURVIVE (`.lbl-yes`) | `rise .5 y20` |
| 3 | +3.0 | `#s3a` RENT | `pop .5` + `fade #s3bgA` |
| 4 | +3.8 | `#s3b` FOOD | `pop .5` |
| 5 | +4.6 | `#s3c` MEDICINE | `pop .5` |
| 6 | +5.4 | `#s3d` COMMUTE | `pop .5` |
| 7 | +7.4 | `#s3nl` WANT — TO ENJOY (**amber**, not red) | `rise .5 y20` + `fade #s3bgB` |
| 8 | +8.8 | `#s3x` STREAMING | `pop .5` |
| 9 | +9.6 | `#s3y` TAKEOUT | `pop .5` |
| 10 | +10.4 | `#s3z` NEW PHONE | `pop .5` |
| 11 | +14.8 | `#s3stamp` WANTS AREN'T THE ENEMY | `pop .55` + `pulse` — on «शौक़ बुरे नहीं हैं» |

**Photos** `s3-need.jpg` `s3-want.jpg`. Pexels: `indian vegetable market basket vendor` · `food delivery bag doorstep`.

### h4 · THE 24-HOUR RULE (~18.1s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +1.2 | `#s4num` `24` (`.mega.glow`, amber not green) | `pop .7` + `countUp 0→24 0.8s` |
| 2 | +2.0 | `#s4l` HOURS BEFORE YOU BUY | `rise` |
| 3 | +3.4 | `breathe #s4num 5.0s` | — | fills the dead air while the rule is explained |
| 4 | +5.6 | `#s4b1` ADD TO CART | `pop .5` |
| 5 | +6.6 | `#s4b2` WAIT | `pop .5` |
| 6 | +8.4 | `#s4b3` DECIDE | `pop .5` |
| 7 | +12.4 | `#s4stat` "7 out of 10 times you'll forget it" | `rise` + `pulse` |
| 8 | +15.8 | `#s4f` "Over ₹10,000? Wait 30 days." | `rise` |

**Photo** `s4.jpg`. Pexels: `hand holding phone online shopping checkout`.

### h5 · THE AUDIT (~16.9s) · photo, ken OUT

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s5k` "Find every recurring charge" | `rise` |
| 2 | +2.2 | `#s5a` BANK — 3 MONTHS BACK | `pop .5` + `fade #s5bgA` |
| 3 | +6.4 | `#s5b` UPI AUTOPAY MANDATES | `pop .5` + `fade #s5bgB` |
| 4 | +8.2 | `#s5c` GOOGLE PLAY SUBS | `pop .5` |
| 5 | +9.8 | `#s5d` TELECOM BUNDLE | `pop .5` |
| 6 | +12.6 | `#s5stamp` WRITE THEM ALL DOWN | `pop .55` |
| 7 | +14.4 | `#s5f` "Annual plans hide — check 12 months too" | `rise` |

**Photos** `s5-bank.jpg` `s5-phone.jpg`. Pexels: `bank statement documents desk pen` · `smartphone settings menu close up`.

> **Why the telecom chip matters:** the Jio/Airtel bundle that already includes an OTT you also pay for separately is the single most common Indian double-pay. It is the one beat this version has and the US version doesn't.

### h6 · CUT WITHOUT MISERY (~23.9s) · photo, ken IN — **longest scene, needs 3 reveals**

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s6k` "Ask one question" | `rise` |
| 2 | +3.4 | `#s6q` USED IT IN THE LAST **30 DAYS?** | `pop .7` |
| 3 | +4.8 | `breathe #s6q 3.0s` | — |
| 4 | +7.6 | `#s6r1` `ZERO → CANCEL` (`.v-cancel`) | `pop .5` |
| 5 | +11.0 | `#s6r2` `ONCE → DOWNGRADE / SHARE` (`.v-down`) | `pop .5` |
| 6 | +16.4 | `#s6r3` `DAILY → KEEP IT` (`.v-keep`) | `pop .5` + `pulse` — on «बिना किसी गिल्ट के» |
| 7 | +20.8 | `#s6stamp` ONE IN, ONE OUT | `pop .55` + `pulse` |

**Photo** `s6.jpg`. Pexels: `family watching television living room india`.

### h7 · THE MATH (~24.7s) · **no photo** — the bill is the visual, ken n/a

The retention beat of the video. The bill assembles line by line **as each item is spoken**, then the total turns red, then the counter runs 12 months.

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.4 | `#s7k` "A normal stack" | `rise` |
| 2 | +2.6 | `#s7r1` `GYM ₹1,500` | `rise .4 y24` |
| 3 | +3.6 | `#s7r2` `NETFLIX (BASIC) ₹199` | `rise .4 y24` |
| 4 | +4.6 | `#s7r3` `MUSIC ₹119` | `rise .4 y24` |
| 5 | +5.6 | `#s7r4` `CLOUD 100GB ₹130` | `rise .4 y24` |
| 6 | +6.6 | `#s7r5` `FOOD PASS ₹99` | `rise .4 y24` |
| 7 | +8.4 | `.rule` + `#s7total` `PER MONTH ₹2,047` | `fade` then `pop .6` + `pulse` |
| 8 | +12.0 | `#s7counter` `₹0` + `.track2` | `fade .5` |
| 9 | +12.0 | `fill #s7fill 2.8s` + `countUp s7c 0→24564 2.8s` | — | 12 ticks = 12 months |
| 10 | +17.6 | `#s7head` "₹35,000/mo salary → that's **3 WEEKS** of pay" | `rise`, then `fade .targetc` at +19.4 |
| 11 | +22.4 | `#s7cap` "Prices as published, July 2026 · example only" | `rise` |

`.ticks` must be regenerated for **12** segments (emergency-fund had 20):
`calc(100% / 12 - 2px)`.

> **Do not round the counter to ₹24,000.** It ends on **₹24,564** — an exact number built from five published price cards is the whole credibility play. The VO says «लगभग पच्चीस हज़ार»; the screen says the real figure. That mismatch is deliberate and correct.

### h8 · DO THIS TODAY (~13.6s) · photo, ken OUT

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.5 | `#s8stamp` DO THIS TODAY (`.stamp.pop`) | `pop .6` |
| 2 | +2.4 | `#s8a` OPEN AUTOPAY LIST | `pop .5` |
| 3 | +3.2 | `#s8arrow` → | `fade .3` |
| 4 | +4.6 | `#s8b` PICK THE ONE YOU FORGOT | `pop .5` |
| 5 | +5.4 | `#s8arrow2` → | `fade .3` |
| 6 | +6.2 | `#s8c` CANCEL IT (`.chip.warn`) | `pop .5` + `pulse` |
| 7 | +10.4 | `#s8t` `"someday" → **DONE**` | `rise` |

**Photo** `s8.jpg`. Pexels: `hand tapping mobile banking app close up`.

### h9 · RECAP + CTA (~16.0s) · photo, ken IN

| # | cue | element | motion |
|---|---|---|---|
| 1 | +0.8 | `#s9a` NEED vs WANT | `pop .45` |
| 2 | +2.4 | `#s9b` WAIT 24H | `pop .45` |
| 3 | +4.2 | `#s9c` AUDIT QUARTERLY | `pop .45` |
| 4 | +5.8 | `#s9d` CANCEL ONE TODAY | `pop .45` |
| 5 | +11.8 | `#s9cta` ▶ SUBSCRIBE | `pop .6` + `pulse` |
| 6 | +12.8 | `#s9sub` "money basics that actually make sense" | `rise` |

**Photo** `s9.jpg`. Pexels: `young indian man smiling relaxed phone outdoors`.

---

## Master timing table (estimates — relock after VO)

| Scene | VO | est. dur | est. start |
|---|---|---|---|
| s1 Hook | h1 | 15.5 | 0:00.0 |
| s2 Roadmap | h2 | 8.7 | 0:16.5 |
| s3 Honest test | h3 | 17.7 | 0:26.2 |
| s4 24-hour rule | h4 | 18.1 | 0:44.9 |
| s5 Audit | h5 | 16.9 | 1:04.0 |
| s6 Cut without misery | h6 | 23.9 | 1:21.9 |
| s7 The math | h7 | 24.7 | 1:46.8 |
| s8 Do this today | h8 | 13.6 | 2:12.5 |
| s9 Recap + CTA | h9 | 16.0 | 2:27.1 |
| **total** | | | **~2:43** |

Scene start = previous start + previous duration + **1.0s breath** (emergency-fund used
0.9–1.1s between VO clips; keep it). VO `<audio>` sits at scene start + **0.4s** lead-in,
`data-track-index="10"`.

## Pattern-interrupt check

Density changes at 0:16 (photo→panel), 1:46 (photo→panel + the bill build) and 2:12
(stamp slam). Longest stretch without a format change is s3→s4→s5 at ~53s — s4's
`.mega 24` count-up and s5's chip cascade carry it, but **if the draft render sags
anywhere it will be there.** Watch that stretch first.

## BUILT — 2026-07-27 · what changed from this spec

`index.html` is live and `npm run check` passes (0 errors). Deltas worth knowing:

- **Voice is Harsh `HTUuC7OeeEt6OL5fViVe`**, not Vikram S — creator direction 2026-07-27.
- **Real VO durations replaced every estimate.** Total **2:58.7** (spec guessed 2:43 — Hindi ran ~10% long across the board). Scene starts now live in `S = {…}` inside `index.html`; that map is the source of truth, not the table above.
- **Cues were computed from character position inside each line** (`offset = 0.4 + chars_before/total × clip_duration`), not from whisper. The narration rate is steady enough that this lands on the word; whisper is the upgrade if any beat reads late.
- **Chip order in s1 changed to OTT · GYM · MUSIC · CLOUD · FOOD PASS** — the VO says «नेटफ्लिक्स» first, so the storyboard's gym-first order would have desynced.
- **Salary anchor moved ₹35,000 → ₹30,000 in-hand**, matching the locked worked example in [[knowledge/money-facts-2026]] so the finance videos agree with each other. The payoff line is now **25 DAYS of pay** (was "3 weeks").
- **s7 is a two-column layout**, not the single stack the spec drew — the bill plus the counter/track/payoff wouldn't fit vertically at 1080p.
- Photos are **Pixabay** (`tools/stock/pixabay_fetch.py` + `assets/img/manifest.json`), not Pexels — that's the fetcher this repo actually has, and the key is already in `.env`. Credits land in `assets/img/CREDITS.txt`.

### Photo swaps forced by frame review
Two of the eleven first-hit images were wrong and were caught only by looking at
rendered frames, not by the checker:
- `s1-phone.jpg` — "man using smartphone night dark" returned **an open book with flowers**. Refetched with "man worried looking at smartphone".
- `s3-want.jpg` — first hit was a **Bolt Food**-branded courier bag (European brand in the India cut). Refetched to "burger fries table dark".

**Standing lesson: always snapshot before trusting a stock query.** Pixabay's
first hit matches the words, not the meaning.

### Render — 2026-07-27
**UPLOAD MASTER: `renders/FINAL-1080p-hi.mp4`** — 265.8 MB · **2:58.7** · 1920×1080 · H.264 High
yuv420p · **12.29 Mbps** · 30fps · AAC-LC 48 kHz stereo · peak −4.6 dBFS / mean −25.6 (no limiter
needed, unlike Firaun). Rendered with `-q high --video-bitrate 12M` in 12m 50s (5,361 frames).
Frame-verified: s3 columns top-align, s7 counter lands exactly on ₹24,564 with all 12 ticks filled.

The first pass (`needs-vs-wants_2026-07-27_02-48-46.mp4`, 66.5 MB) used the default `standard`
quality and came out at **2.9 Mbps** — under YouTube's 8 Mbps recommendation for 1080p30. With
film grain over flat dark panels that's where banding appears after YouTube's own re-encode.
**Standing rule: always render the upload master with `-q high --video-bitrate 12M`;** the default
is a preview setting. Bonus — rendering the two cuts sequentially rather than in parallel roughly
halved wall-clock (23 min → 13 min each).

## Known non-issue

`npm run check` reports `✗ #s3stamp 1.7:1 (need 3:1)`. The rendered frames show
dark text on bright green, plainly legible — the contrast pass mis-reads the
rotated `.stamp` against the scene background instead of its own fill. Same
construct shipped in emergency-fund. Do not "fix" it by lightening the text.

## Still open

- BGM not chosen. Match emergency-fund's bed or ship dry.
- Thumbnail not made.
- [[workflows/video-audit]] pass on the finished render.

## Sign-off

- [x] Built and checked — 2026-07-27
- [ ] Creator approved the render
