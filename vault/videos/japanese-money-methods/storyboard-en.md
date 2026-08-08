---
summary: Storyboard for «Japanese Money Methods» en cut — LONG tier, 92 scenes (one VO line = one clip = one scene), **blockframe-9** (centred stack over a full-bleed graded photo), US market. Declares the colour semantics, the per-scene tint ladder, the ported element IDs + a 4-cue ladder, transitions (2 shoves, 3 continuous-zoom holds), one music bed + 24 SFX cues, 5 icons / 0 lotties, and 96 image slots backed by the 93 files already on disk. Zero `max_scene_seconds` breaches (longest scene 8.349s); 3 declared `data-framings`. Emits a 26-row divergence list against storyboard-hi.md.
updated: 2026-08-01
source: script-en.md (fin-script attempt 1 + fin-audit-en-1 edits) + studio/videos/japanese-money-methods-en/assets/voice/timing.json (freshly measured, 626.743s, 92 lines) + storyboard-hi.md (skeleton + element IDs) + knowledge/design-finance-blockframe.md + tools/format.json + tools/audio/kit.json + tools/scaffold/assets/blockframe.css
stage: fin-storyboard, cut en, **attempt 3 — full rewrite for `blockframe-9`**
---

# STORYBOARD — «Japanese Money Methods» · **en** cut

**Project:** `studio/videos/japanese-money-methods-en/` · **Script:** `script-en.md`
**Design:** [[../../knowledge/design-finance-blockframe]] — the **dark** system.
Do **not** use `design-techtooltester` — that is the bright, non-finance system.
**Channel:** @moneymavens101 $ · **Tier:** LONG, per-line chapters
**Architecture:** **`blockframe-9`** — centred stack over a full-bleed graded photo (`run.json`; creator decision 2026-08-01 after rejecting a rendered ledger-rail frame, and the same architecture as the `format.json architecture_lock`).
**Runtime:** **626.743s (10:26.7)** measured — `timing.json` is the only home for every duration.
**VO:** Brian `nPczCjzI2devNBz1zQrb` · **Scenes:** 92 · **Image slots:** 96 (92 bg + 4 cut-ins), **93 files** on disk (3 bg slots re-use a hold partner's file).

> **This file replaces the `ledger-rail` storyboard of attempts 1–2 in full.** What
> survived the rewrite, because it was sound and the creator's objection was to the
> *layout*: the beat structure, the SFX placement, the image assignments, the colour
> semantics, the transition classes, the hold pairs, the icon set. What was re-derived
> from scratch: every scene's type treatment, the cue ladder, the per-scene tint (which
> `.rail` had retired), and the anti-sameness device.

---

## 1. Colour semantics for THIS video (derived from the thesis — mandatory)

The thesis: *Japan's famous saving number contradicts Japan's own other number; the three
(four) methods are real behaviour, but they were never the reason — and the only place they
can be started is your own kitchen, tonight.*

Roles are fixed; meanings are per-video.

| Token | This video means | Because |
|---|---|---|
| `--warn` red `#ef4444` | **the thing that is draining or false** — money going a little everywhere (1.3, 1.7, 1.9), the number that travels because it sells (2.7, 2.10), culture-as-cause (3.7, 3.10), the decline after the peak (3.9), value already bought and never used (4.4, 4.8), month-end zero (5.6), bills eating the whole paycheck (5.11), the four categories being a later addition (6.7), a $400 surprise becoming a card balance (6.14), the moving finish line (7.7), the market that makes what you have feel like less (7.9) | this video's obstacle is **a leak plus a lie about the leak** — so red carries both the drain and the misused figure. Never a method, never a viewer action |
| `--fund` green `#22c55e` | **the behaviour that works once you start it** — the promise (2.1), the three physical checks (4.5, 4.6, 4.7), the one question (4.10), day-one two-parts-out and its $800/$3,200 split (5.4, 5.5), automate-and-separate (5.7), the $200 floor (5.10), divide-by-twelve saving-first (6.5), the four questions and their order (6.10, 6.11), the answer you write yourself (7.10), the recap actions (8.2, 8.3, 8.5), the honest line (3.12) | green marks **what the viewer does**, never what Japan is. 3.12 is green on purpose: "the methods work" is the constructive half of the debunk |
| `--target` amber `#f59e0b` | **a figure or a definition under examination** — 37.8% (2.3, 2.5), ABOUT 1% (2.6), the deposit/securities split (3.2), 51.0% and the BOJ US column (3.4, 3.5), 1961–1986 (3.8), 62.2% (5.9), the accounting re-frame (5.12), 1904 (6.2), 4 IN 10 (6.15), the fourth method being introduced (7.1, 7.4), TARU WO SHIRU in recap (8.4) | amber is the thing being **weighed**, never the thing being recommended. Every price-evidence beat is amber precisely because the persona rule forbids a pick |
| `--pop` orange `#ff5c39` | the call to action | fixed — **exactly once**, scene 91 (8.7) |

**The inversion trap — three prior videos, three different systems, none of them applies.**
`needs-vs-wants` ran amber = "wants" and red = "the leak alone". `first-lakh-first-thousand`
ran red = "the stretch nobody helps you with". **Here red is falsity-and-drain and green is
the viewer's own hand.** Any element that renders 37.8% in red (it is real), or a method in
amber (they are not under examination — only the figures are), argues against the script.

**The one red number, declared.** `23.2%` at 3.9 (s30) is a real figure rendered `--warn`.
That is deliberate and it is not the inversion trap: the frame's argument is the **fall after
the peak**, which the `foot` states ("no higher than 5% since 2002"). The figure is not being
called false; the trajectory is the leak. `6.14 OVER 20%` is red for the same reason — it is
the cost, not a discredited statistic. Every other `num` in the cut is amber.

**One role colour visible per scene, ever.** On 47 of 92 scenes no role colour appears at all
— `--ink` kicker + `--ink` focal + `--muted` foot — and that is correct: colour is a
signifier here, not decoration.

### 1a. Per-scene `--tint` is BACK (it was retired under `.rail`; blockframe-9 has a scrim)

`blockframe-9` restores the four-layer scrim on every scene, and scrim layer 1 carries
`--tint`. The tint is **derived from the scene's role colour, not chosen per scene** — one
rule, 92 applications, so it cannot drift:

| scene's role | `--tint` | alpha |
|---|---|---|
| `--fund` | green | `.10` |
| `--warn` | red | `.12` |
| `--target` | amber | `.12` |
| `--pop` (s91 only) | orange | `.13` |
| no role (47 scenes) | **none** — `--tint` unset, layer 1 renders `transparent` | — |

Design doc §2 caps tint at 0.10–0.13; above ~0.15 it reads as a colour wash. A scene with no
role colour gets no tint, which keeps the tint a signifier rather than decoration. The seven
SOLO scenes (§3a) take the top of their role's band.

**Role classes, and the silent-white trap.** `.fundc` `.targetc` `.warnc` `.popc` all now
exist in `assets/blockframe.css`. **A role token with no colour class paints `--ink` white and
fails every check silently** — that is what put the s24 icon in white on the hi cut and
SUBSCRIBE in white on the last en build. Two hard consequences for fin-build:
- **s24's icon is `<svg class="icon warnc">`** — not `.warn`, which is the component modifier.
- **s91's SUBSCRIBE is a `.cta` block**, not pop-coloured text: `.cta` sets
  `background: var(--pop); color: #0d1017`, so it is structurally incapable of the white
  failure. `.popc` exists and is available for pop-coloured *text*; this cut has no such text.

---

## 2. Audio — one bed, 24 cues

**Music bed: `bed-resolve`.** The argument is **a habit / a fix**, not a trap or a cost.
Chapters 1–3 run in a cost register and Chapter 3 is an outright debunk, but the thesis those
chapters serve is constructive: it ends on one page, one pen, four questions, tonight. The
bed is chosen for the video, not for a chapter.

> **Bed length is not a storyboard concern and is not flagged here.** `tools/audio/mix.py`
> feeds the ~248s bed in `laps` times with a 3s `acrossfade` at each joint and trims to the
> master's duration; there is no dip at 248s or 496s. Both storyboards on this video
> previously escalated this as a decision. It is not one, and the escalation is retracted.

**SFX budget: 24 cues across 10:26** — one per **26.1s**. The kit's stated ceiling (≤10) is a
**SHORT-cut** figure; scaling it by runtime would give ~42, which is exactly the "every reveal
has one, so none of them means anything" failure. 24 is a deliberate ceiling, not a
derivation, and it matches the hi cut's so a fix travels. **No two cues inside 0.8s — the
closest pair in the whole cut is 6.31s** (#12→#13).

**Every cue is bound to a helper that actually runs on that element** (kit.json `_discipline`).
Under `.rail` three of these sounds had no helper on their scene; §4 fixes that at the ladder
rather than by dropping the cue — see the `pop`-entry rule for `stamp` and `chip`.

| # | scene | line | sound | helper it fires with | absolute t | why this beat |
|---|---|---|---|---|---|---|
| 1 | s1 | 1.1 | `reveal` | `rise` on `s1-stmt` | **0.60** | `The deposit is in.` — frame one, sets the register, then Ch1 goes dry |
| 2 | s9 | 1.9 | `reveal` | `rise` on `s9-stmt` | **48.79** | "Not one place. A little everywhere." — the cold open's thesis |
| 3 | s13 | 2.3 | `hero` | `countUp`+`pop` on `s13-num` | **73.87** | `37.8%` on "thirty-seven" — the figure the video exists to test |
| 4 | s16 | 2.6 | `hero` | `pop` on `s16-num` | **94.83** | `ABOUT 1%` on "about one percent" — the contradiction |
| 5 | s17 | 2.7 | `hero` | `pop` on `s17-num` (`.mega` 240) | **102.14** | `30 TIMES` — the one enormous number in the video |
| 6 | s23 | 3.2 | `reveal` | `rise` on `s23-stmt` | **140.10** | "About 90% into deposits" — where the surplus actually goes |
| 7 | s25 | 3.4 | `hero` | `countUp`+`pop` on `s25-num` | **154.39** | `51.0%` on "fifty-one percent" |
| 8 | s30 | 3.9 | `hero` | `countUp`+`pop` on `s30-num` | **191.96** | `23.2%` on "twenty-three" — the peak before the fall |
| 9 | s31 | 3.10 | `stamp` | **`pop` verdict entry** on `s31-stmt` | **199.45** | "Culture, tradition and national character are not a major determinant" — the premise correction, stated |
| 10 | s33 | 3.12 | `stamp` | **`pop` verdict entry** on `s33-stmt` | **214.98** | "The methods work. They were never the reason." — the video's most honest line |
| 11 | s33→s34 | 3.12→4.1 | `transition` | **shove** | **220.725** | **SHOVE #1** — out of the debunk, into the methods |
| 12 | s38 | 4.5 | `chip` | **`pop`** on `s38-icon` | **250.55** | CHECK ONE |
| 13 | s39 | 4.6 | `chip` | **`pop`** on `s39-icon` | **256.86** | CHECK TWO |
| 14 | s40 | 4.7 | `chip` | **`pop`** on `s40-icon` | **263.93** | CHECK THREE — the three icons are ONE set; that is why repeating is legible here and nowhere else |
| 15 | s43 | 4.10 | `stamp` | **`pop` verdict entry** on `s43-stmt` | **281.81** | "If the answer is MAYBE, the answer is NO." — SOLO |
| 16 | s51 | 5.5 | `hero` | `rise` on `s51-stmt` (the split figure) | **335.74** | `$800 out · $3,200 to live on` on "eight hundred dollars" |
| 17 | s55 | 5.9 | `hero` | `countUp`+`pop` on `s55-num` | **365.76** | `62.2%` on "sixty-two percent" — Japan's own figure, alone |
| 18 | s57 | 5.11 | `reveal` | `rise` on `s57-stmt` | **379.34** | "If the bills already eat the whole paycheck, this fails in month one" — the honesty beat |
| 19 | s65 | 6.7 | `stamp` | **`pop` verdict entry** on `s65-stmt` | **436.08** | the admission — the four categories came later |
| 20 | s69 | 6.11 | `tick` | `pulse` on `s69-icon` (after `draw`) | **465.50** | "Question two comes before question three" — the order IS the method |
| 21 | s73→s74 | 6.15→7.1 | `transition` | **shove** | **497.989** | **SHOVE #2** — into the unpromised fourth |
| 22 | s77 | 7.4 | `reveal` | `rise` on `s77-stmt` | **518.77** | the shared part — **the emptiness at the centre of the basin** |
| 23 | s90 | 8.6 | `stamp` | **`pop` verdict entry** on `s90-stmt` | **608.92** | "What you heard is information. What you start is understanding." — SOLO, the close |
| 24 | s91 | 8.7 | `cta` | the `.cta` block landing | **616.61** | the single `--pop` block (7.69s after #23 ✓) |

⚠ **Cues #23 and #24 moved +0.157s** from the previous build (608.76→608.92, 616.45→616.61)
because 7.4 was re-voiced and every scene from 7.5 onward shifted. Every other cue is
unchanged: scenes s1–s77 carry identical `scene_start` values in the new `timing.json`.

**Declared DRY beats** (silence is the choice, not an omission):
- **Chapter 1 except 1.1 and 1.9** — the pain-mirror is paid in recognition; punctuating a
  car-insurance renewal makes it a joke.
- **2.5** — the 37.8% *restatement*. The first statement got the `hero`; hitting the repeat
  would make a restatement sound like new evidence.
- **3.5 (the BOJ US column)** — deliberately unhit. A `tick` on the American figures turns a
  neutral asset-mix table into a gotcha, which is the one thing the script's guardrail #2
  forbids by name.
- **2.8–2.11 and 3.6–3.8** — the "who is counted / how" reasoning runs on voice.
- **5.10 ($200)** — the de-escalation. A `hero` on the smaller number would make it sound
  like a lesser prize, immediately after 5.9 got one.
- **6.14 (OVER 20%) and 6.15 (4 IN 10)** — the loudest silence in the cut, and **32 dry
  seconds running straight into SHOVE #2**. These are the two Federal Reserve figures; a
  `hero` on a card APR *recommends against* a product, which is the mirror image of the
  placement the persona rule forbids, and the audit already stripped a product category out
  of 5.7 for exactly that reason.
- **7.5–7.11 and 8.1–8.5** — twelve scenes and ~90s dry, so the `stamp` at 608.92 is the
  first sound the viewer has heard since 518.77 and the `cta` lands into a cleared room.

**Mixed in post, never in the composition.** `assets/audio.json` cue list →
`tools/audio/mix.py` (sidechain duck) → `tools/loudnorm.py` to −14 LUFS. The composition stays
voice-only: one `<audio>` row per line, track index 10.

---

## 3. The `blockframe-9` frame — DOM and the ported element IDs

`<div id="root" class="cut-en">` — **no body class**; `blockframe-9` is the bare system
(`format.json architectures.blockframe-9.body_class` is `""`). The `cut-en` class is
load-bearing: it is the only thing the composition owes the @moneymavens101 watermark, and
`check build` asserts it, because the failure mode is a fully green run that ships an
unbranded video.

Stage 1920 × 1080. `.scene` padding `110px 150px`, `display:grid; place-items:center`,
`isolation:isolate`. Usable content width ≈ **1620px**, centred.

```html
<section class="scene" id="s25" data-track-index="1"
         data-start="152.451" data-duration="7.754" style="--tint:rgba(245,158,11,.12)">
  <div class="bg"    id="s25-bg"></div>      <!-- assets/img/s25.jpg, full-bleed, inset -8% -->
  <div class="bg"    id="s25-bg2"></div>     <!-- 2nd framing, opacity 0 — 3 scenes only (§6) -->
  <div class="scrim"></div>                  <!-- four layers; layer 1 takes --tint -->
  <div class="grain"></div>                  <!-- opacity .05, mix-blend overlay -->
  <div class="stack">
    <p  class="kicker"       id="s25-head">JAPAN</p>          <!-- 30px/800 --muted, tracked -->
    <p  class="huge targetc" id="s25-num">51.0%</p>           <!-- 112px/900 tabular -->
    <!-- OR <p class="huge" id="s25-stmt" style="font-size:76px">…</p> -->
    <p  class="foot"         id="s25-foot">…</p>              <!-- 26px/200 --muted -->
    <svg class="icon fundc"  id="s25-icon">…</svg>            <!-- icon scenes only -->
  </div>
</section>
```

**ID scheme ported verbatim from `storyboard-hi.md`: `s<n>-<part>`, n = 1…92 in script
order.** `-bg`, `-bg2`, `-head`, `-stmt`, `-num`, `-foot`, `-icon` all keep their names, so a
fix in either cut travels. The `.rail`-only parts — `-idx`, `-hair`, `-beat`, `-panel` — are
**deleted architecture-wide** (divergence D0); there is no rail and no photo panel.
`s91-cta` is the one new ID in the cut.

⚠ **`sN-head` now carries `class="kicker"`, not `class="head2"`.** The ID is stable, the class
is not. In `.rail` the beat name lived in the rail and `head` was a 54px `head2`; with the rail
gone, the script's `head:` field is the scene's opening whisper and that is what `.kicker` is
for. `format.json layout` requires the kicker first, and it is cue #1 on 84 of 92 scenes.

**Copy is NOT restated here.** `head:`, `stmt:`/`num:` and `foot:` strings live in each line's
`[rail …]` / `[RAIL OFF …]` cue block in `script-en.md` and have exactly one home. **Those cue
blocks keep their names**; `rail`/`RAIL OFF` is now read as *scene type*, mapped here:

| script cue block | blockframe-9 scene type |
|---|---|
| `[rail N.N \| head: … \| stmt: …]` | **A — statement** |
| `[rail N.N \| head: … \| num: …]` | **B — figure** |
| `[RAIL OFF \| …]` | **SOLO** (§3a) |
| 8.7 (`num: SUBSCRIBE`, `colour: --pop`) | **C — CTA** |

This storyboard owns the DOM, the type treatment, the cues, the transitions, the audio, the
vector art and the images.

### 3a. Re-derived type treatment — the anti-sameness device replaces RAIL OFF

`.rail` varied the seven signature scenes by **retracting the rail**. With no rail there is
nothing to retract, so the same seven scenes are varied by **emptying the stack** instead.
Same seven scenes, same job, different mechanism.

| type | count | stack | focal size | tint | ken |
|---|---|---|---|---|---|
| **A — statement** | 75 | `kicker` → `stmt` → optional `foot` | `.huge` **@76px** | per role | 1.0↔1.16 |
| **B — figure** | 9 | `kicker` → `num` → `foot` | `.huge` **112px** (ladder default) | per role | 1.0↔1.16 |
| **SOLO** | 7 | **focal alone** — no kicker; `foot` only where it carries a citation (s17) | `.huge` **@88px**, or `.mega` **@240px** on s17 | top of the role's band | 1.0↔1.16, slower ease |
| **C — CTA** | 1 (s91) | `.cta` block → `foot` | `.cta` 46px | orange .13 | 1.0↔1.16 |

- **Every size is a ladder value.** 290 / 240 / 112 / 96 / 88 / 76 / 46 / 26 are all on the
  `type_ladder_px` list. Nothing is interpolated to fit; the design doc's own precedent is the
  shipped pair dropping `.huge` to 88 and 76.
- **`.mega` is used exactly once in the video** — s17 `30 TIMES` — which is what "the one
  enormous number" means. Never `.huge` and `.mega` together (`one_focal_per_scene`).
- **SOLO is 7 of 92, evenly spread** (s1, s17, s33, s43, s65, s77, s90 — every 12–14 scenes),
  so the device reads as punctuation. It is also the only place a kicker is absent, which is
  what makes its absence legible.
- **Every scene now sits on a full-bleed graded photo**, so the four-layer scrim and the
  two-part `text-shadow` are **ON everywhere** — not conditional as they were in `.rail`. This
  is the single biggest mechanical difference and it applies to all 92 scenes.

**Element budget.** Max content elements per scene: `kicker`, focal, and **one** of
`foot` / `icon` — **3**, against the `max_simultaneous_elements` ceiling of 6 ✓. `.bg`,
`.scrim`, `.grain` are stage, not elements. **Never `stmt` and `num` together.**
**No chip rows anywhere in this cut**, so `max_chips_per_row` / `max_chip_chars` are vacuous.

**Font subset, restated because it bites here.** 97 codepoints, **no CJK**. On-screen Japanese
is **romaji only** — `MOTTAINAI`, `HARA HACHI BU`, `KAKEIBO`, `TARU WO SHIRU`, `RYOAN-JI`.
The only kanji in this video live **inside the s76 / s77 / s88 photographs** of the Ryoan-ji
tsukubai and are never composition text. `~` `×` `→` `¥` `>` are absent; `·` is present and is
the separator. The `🇺🇸` and `◆` marks in §7 are **storyboard notation in this file** and
never reach the composition.

---

## 4. The cue ladder — four cues, and it is the same four on every scene

Offsets are **relative to `scene_start`** (§7 column `start`, verbatim from `timing.json`), so
every absolute cue time is `scene_start + offset` and is derived, never hand-typed.

| # | element | offset | class | helper | spec |
|---|---|---|---|---|---|
| — | `sN-bg` | **+0.00 → scene end** | **anchored** | `ken` | 1.0↔1.16 scale, ∓2.5 xPercent; direction per §7 |
| 1 | `sN-head` (`.kicker`) | **+0.30** | fixed | `rise` | `y:24`, 0.50s `expo.out` |
| 2 | focal — `sN-stmt` | **+1.10** | fixed | `rise` | `y:40`, 0.70s `expo.out` |
| 2′ | focal — `sN-num` | **anchored** | **anchored** | `countUp` / `pop` | lands on its own digit in the VO |
| 2″ | focal — verdict scenes | **anchored** | **anchored** | **`pop`** | scale from 0.6, 0.60s `back.out(1.7)` — the slam |
| 3 | `sN-foot` **or** `sN-icon` | **+2.10** | fixed | `fade` / `draw` | foot 0.40s `power1.out`; icon stroke-draws over 0.70s |
| — | `sN-bg2` | **anchored** | **anchored** | `fade` cross-dissolve, 0.40s | 3 scenes only (§6) |

**Spacing.** `first_cue_by_seconds` 0.5 — the kicker is on screen at **+0.30** on 84 scenes,
and on the 8 that have no kicker (7 SOLO + s91) the focal is at **+0.40**, so something is on
screen by +0.5 on all 92 ✓. `cue_min_gap_seconds` 0.8: +0.30 → +1.10 = **0.80** ✓ ·
+1.10 → +2.10 = **1.00** ✓. **There is no cascade in this cut** — the `.rail` five-item
assembly was furniture that no longer exists, and nothing here needs a declared exception to
the 0.8s rule. That is a real simplification, not an omission.

**Anchored vs fixed.** The kicker, the `stmt` focal and the foot/icon are **fixed**: constant
regardless of clip length. The `ken` push, every `num` arrival, every verdict `pop` and every
`bg2` swap are **anchored**: they land on a word and scale with the clip.
**Surplus time from a longer clip goes into the hold after cue 3 — never into a cascade.**
Concretely: the stack always finishes at **+2.50s**; s79 (8.349s) then holds a finished frame
for 5.8s with only the ken push and one bg swap running, and that is correct.

**The 9 type-B scenes take an anchored arrival instead of the +1.10 fixed rise** — putting
`51.0%` on screen five seconds before the voice reaches it spoils the line. Type-A `stmt`
scenes keep the fixed +1.10 because a statement paraphrases the whole line and cannot spoil it.

**The verdict `pop` (cue 2″) is new, and it is why the `stamp` SFX is legal.** Five scenes
(s31, s33, s43, s65, s90) carry a `stamp` cue. Under `.rail` their focal entered with `rise`,
which meant a *stamp* sound was firing against a *rise* helper — a sound with no helper, which
kit.json forbids by name. There is no `.stamp` element available because the script writes no
stamp copy, and inventing copy here would put a second home under a fact. **The fix is at the
ladder**: on those five scenes the focal enters with `pop` (`back.out(1.7)`) at its anchored
word instead of `rise`. That IS the verdict slam, it needs no new copy and no new element, and
the sound now has the helper it is bound to. Same reasoning binds the three `chip` cues to a
`pop` entry on the s38/s39/s40 icons (rather than `draw`), and the `tick` on s69 to a `pulse`
that fires after that icon has drawn.

**Anchored cue resolution.** The absolute times in §2 and §7 are computed as
`audio_start + f × duration` with the target word named. **`f` is a fallback.** Per script
handoff §11, fin-build resolves each against **faster-whisper word timings** and uses the
fraction only if the word fails to align. ⚠ **Not one `f` is ported from the hi cut** — every
hi fraction is a Hindi word position at 13.03 c/s, and Brian delivers at ~17.4 c/s with the
figures landing in different clause positions (divergence D3).

**Track index alternates 1 / 2 by scene parity** (odd → 1, even → 2), because `hyperframes
check` rejects two overlapping clips on one track and every non-final scene overlaps its
successor by 0.45s.

**`data-duration` = `timing.json` `scene_duration` + 0.45** on scenes 1–91; s92 carries its
`scene_duration` bare. **This includes the three `hold` boundaries** — see §5. Root duration is
unaffected: **626.743s**.

---

## 5. Transitions

`dissolve` (0.45s) is the default on every boundary. 91 boundaries, three classes:

| class | count | where |
|---|---|---|
| `dissolve` | 86 | everything not named below |
| **`shove`** | **2** | s33→s34 (3.12→4.1) and s73→s74 (6.15→7.1) |
| `hold` | 3 | s1→s2, s65→s66, s77→s78 |

**The two shoves are the only two turns in the argument.**
- **s33→s34** ends the debunk ("the methods work — they were simply never the reason") and
  opens Method One. Everything before it is *why the story you were told is wrong*; everything
  after is *what to do anyway*. The video has exactly one hinge and this is it.
- **s73→s74** is the promise break — "the promise at the top was three methods; there is a
  fourth, and it is the hardest of them." A dissolve here would smuggle the fourth in as a
  continuation instead of announcing it as a reversal.

**`hold` = a matched-frame boundary inside a continuous-zoom pair, NOT a missing dissolve.**
The three pairs share one photograph across two scenes (creator rule, firaun 2026-07-23: same
image across both lines = **ONE continuous zoom, never a self-dissolve**). Mechanics, which
fin-build must get exactly right:

1. The 0.45s overlap **stays** — `data-duration = scene_duration + 0.45` on the outgoing scene,
   as on every other boundary. `pipeline_check` asserts this on *every* pair and has no
   exception; a butt-joined hold would fail the check for a reason unrelated to holds.
2. The incoming scene's `ken` **starts at the scale the outgoing scene's ken has reached at
   that instant and continues in the SAME direction.** With identical pixels moving on the same
   trajectory the cross-dissolve is invisible — that is what makes it a hold and not a flicker.
   Direction does **not** alternate across a hold pair (§7 `ken` column).
3. The incoming scene uses a **tighter crop** of the same source (`background-size` /
   `background-position`), so each scene is its own framing and neither exceeds 9.0s:
   s1 4.039 + s2 7.435; s65 7.252 + s66 6.965; **s77 7.304 + s78 7.200**. **No `data-framings`
   attribute is needed on a hold pair** — the crop change happens at the section boundary, so
   the sections already partition the framings.
4. **Under blockframe-9 the photo is full-bleed on both halves**, so a hold is now purely
   photographic: the image never stops moving and the *stack* is the only thing that changes.
   The `.rail` `railIn` helper (the panel edge sliding 1920→1180) is **deleted** — there is no
   panel edge. One less helper.

⚠ **s77→s78 is the pair the run directive names, and it is intact**: both scenes point at the
single file `assets/img/s77.jpg`, s78 has no file of its own, and both push `i`. Do not give
s78 its own image.

---

## 6. `max_scene_seconds` — ZERO breaches, and three declared `data-framings`

**The longest scene in this cut is s79 (7.6) at 8.349s.** Every one of the 92 sits under
`scene.max_scene_seconds` 9.0, so no `known_benign` entry is owed. Brian's ~17.4 c/s against
Harsh's 13.03 is the whole reason.

`data-framings` is now checked, and a framing list that does not partition its own scene fails.
**Re-derived under the new timing from scratch, not ported.** The result is the same three
scenes the previous build declared — but for a re-derived reason, and every sum re-checked
against the fresh `timing.json`:

| scene | line | scene dur | swap(s) at scene_start + | anchored to | `data-framings` | sum |
|---|---|---|---|---|---|---|
| **s32** | 3.11 | 8.140 | **+5.66** | "and a government savings campaign" (f 0.737) | `"5.66,2.48"` | 8.140 ✓ |
| **s36** | 4.3 | 7.801 | **+2.74**, **+4.77** | "a farmer's crop" (f 0.355) · "a truck's diesel" (f 0.645) | `"2.74,2.03,3.031"` | 7.801 ✓ |
| **s79** | 7.6 | 8.349 | **+5.50** | "the phone, the car, the apartment" (f 0.695) | `"5.50,2.849"` | 8.349 ✓ |

None of the three durations changed in the new `timing.json` (only s79's *start* moved,
531.716 → 531.873), so all three attributes are numerically unchanged.

**Why these three and no others.** Each names more concrete things than one photograph can
hold, and each swap is anchored to its own word. **No scene needs a framing to clear the 9.0s
gate**, and no other scene gets a cosmetic one — a `data-framings="6.0,2.0"` on a scene whose
image never changes is precisely what the new check exists to reject. Longest single framing
anywhere in the cut: **8.167s** (s47, 5.1, one photograph, no swap) — 0.833s of headroom.

**Under blockframe-9 a swap is a full-frame cross-dissolve, not a panel swap.** `sN-bg2` sits
directly on top of `sN-bg`, both full-bleed, and fades in over 0.40s **with the ken continuing
in the same direction on both layers**, so it reads as a cut-in rather than as a new scene.
s36's middle framing is 2.03s — a real framing at the middle beat of a three-item enumeration
delivered in 2.0s of voice, not a flash. **The mill is deliberately dropped** rather than faked
into a 0.98s cell (design-finance-blockframe §7, "drop a cut-in rather than fake it").

---

## 7. Scenes

One row per VO line. `start` / `dur` = `scene_start` / `scene_duration`, **verbatim from
`timing.json`** (the only home); every fixed cue is `start + offset` from §4. `focal` names
which of `stmt` / `num` carries the frame and its single role colour — `—` means no role
colour and therefore **no tint** on that scene. **Copy lives in the script.** The `bg` column
quotes the query already recorded in `assets/img/manifest.json` — **all 93 files are on disk
and pass the asset gate; nothing here is a new spec.**

**Legend.** `T`: scene type per §3a (**A** statement · **B** figure · **◆** SOLO · **C** CTA) ·
`ken`: `i` = push in, `o` = pull out — flips at every boundary **except** a hold, where the
second scene continues its partner's push · `trk` = `data-track-index` · `Trans`: `dis` = 0.45s
dissolve, **`SHOVE`**, `hold` = matched-frame continuous zoom (§5) ·
`🇺🇸` = mandatory-American act-now frame (script handoff §7) · `tint` per §1a.

| # | line | start | dur | T | ken | trk | Trans | focal · role | bg file — manifest query | anchored cue · SFX |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.1 | 0.000 | 4.039 | ◆ 🇺🇸 | i | 1 | **hold** | stmt @88 · — | `s1.jpg` — dark empty kitchen counter at night@pexels | `reveal` **0.60** |
| 2 | 1.2 | 4.039 | 7.435 | A 🇺🇸 | i | 2 | dis | stmt · fund | *holds `s1.jpg`* — tighter crop, zoom continues | — |
| 3 | 1.3 | 11.474 | 5.946 | A 🇺🇸 | o | 1 | dis | stmt · warn | `s3.jpg` — pile of paper bills and envelopes on a table | — |
| 4 | 1.4 | 17.420 | 6.312 | A 🇺🇸 | i | 2 | dis | stmt · — | `s4.jpg` — auto insurance renewal letter half out of its envelope | — |
| 5 | 1.5 | 23.732 | 6.730 | A 🇺🇸 | o | 1 | dis | stmt · — | `s5.jpg` — gift bag and paper shopping bags on a table | — |
| 6 | 1.6 | 30.462 | 6.547 | A 🇺🇸 | i | 2 | dis | stmt · — | `s6.jpg` — crumpled paper on a dark wooden desk@pexels | — |
| 7 | 1.7 | 37.009 | 4.379 | A 🇺🇸 | o | 1 | dis | stmt · warn | `s7.jpg` — wall calendar page with dates@pexels | — |
| 8 | 1.8 | 41.388 | 5.998 | A 🇺🇸 | i | 2 | dis | stmt · — | `s8.jpg` — hands holding a printed document at a desk | — |
| 9 | 1.9 | 47.386 | 5.659 | A 🇺🇸 | o | 1 | dis | stmt · warn | `s9.jpg` — metal colander in a kitchen sink | `reveal` **48.79** |
| 10 | 1.10 | 53.045 | 4.144 | A 🇺🇸 | i | 2 | dis | stmt · — | `s10.jpg` — empty chair at a wooden table@pexels | — |
| 11 | 2.1 | 57.189 | 7.200 | A | o | 1 | dis | stmt · fund | `s11.jpg` — traditional japanese house at dusk@pexels | — |
| 12 | 2.2 | 64.389 | 6.416 | A | i | 2 | dis | stmt · — | `s12.jpg` — hand holding a phone silhouette at sunset@pexels | — |
| 13 | 2.3 | 70.805 | 6.312 | **B** | o | 1 | dis | **num** · target | `s13.jpg` — printed spreadsheet with rows of numbers close up@pexels | num `37.8%` **73.87** · `hero` |
| 14 | 2.4 | 77.117 | 5.659 | A | i | 2 | dis | stmt · — | `s14.jpg` — government publication cover with an official embossed seal | — |
| 15 | 2.5 | 82.776 | 6.913 | **B** | o | 1 | dis | **num** · target | `s15.jpg` — spreadsheet with rows of numbers printed on paper | num `37.8%` **87.31** *(dry)* |
| 16 | 2.6 | 89.688 | 6.364 | **B** | i | 2 | dis | **num** · target | `s16.jpg` — two thick bound reference volumes stacked on a desk@pexels | num `ABOUT 1%` **94.83** · `hero` |
| 17 | 2.7 | 96.052 | 7.513 | **◆** | o | 1 | dis | **num `.mega` 240** · warn | `s17.jpg` — two brass weights of different size on an old balance scale@pexels | num `30 TIMES` **102.14** · `hero` |
| 18 | 2.8 | 103.566 | 7.304 | A | i | 2 | dis | stmt · — | `s18.jpg` — two clipboards with paper on a table | — |
| 19 | 2.9 | 110.870 | 7.853 | A | o | 1 | dis | stmt · — | `s19.jpg` — crowded osaka pedestrian crossing wide shot faces indistinct | — |
| 20 | 2.10 | 118.723 | 6.077 | A | i | 2 | dis | stmt · warn | `s20.jpg` — stack of newspapers on a table@pexels | — |
| 21 | 2.11 | 124.800 | 7.252 | A 🇺🇸 | o | 1 | dis | stmt · — | `s21.jpg` — four twenty dollar bills laid flat on a plain grey card@pexels | — |
| 22 | 3.1 | 132.052 | 6.651 | A | i | 2 | dis | stmt · — | `s22.jpg` — vintage bank ledger book open on a table@pexels | — |
| 23 | 3.2 | 138.704 | 6.834 | A | o | 1 | dis | stmt · target | `s23.jpg` — bank branch interior counter@pexels | `reveal` **140.10** |
| 24 | 3.3 | 145.538 | 6.913 | A | i | 2 | dis | stmt · — | `s24.jpg` — row of closed steel safe deposit boxes all shut | **ICON** closed padlock, **`warnc`**, +2.10 |
| 25 | 3.4 | 152.451 | 7.304 | **B** | o | 1 | dis | **num** · target | `s25.jpg` — printed central bank chart page under a desk lamp@pexels | num `51.0%` **154.39** · `hero` |
| 26 | 3.5 | 159.755 | 8.036 | A | i | 2 | dis | stmt · target | `s26.jpg` — printed bar chart on white paper close up@pexels | *(deliberately dry — §2)* |
| 27 | 3.6 | 167.791 | 7.722 | A | o | 1 | dis | stmt · — | `s27.jpg` — sealed glass jar full with the lid still on | — |
| 28 | 3.7 | 175.513 | 7.566 | A | i | 2 | dis | stmt · warn | `s28.jpg` — vintage black and white street photograph@pexels | — |
| 29 | 3.8 | 183.079 | 7.069 | A | o | 1 | dis | stmt · target | `s29.jpg` — tree rings cross section | — |
| 30 | 3.9 | 190.149 | 7.905 | **B** | i | 2 | dis | **num** · warn | `s30.jpg` — line graph drawn on graph paper@pexels | num `23.2%` **191.96** · `hero` |
| 31 | 3.10 | 198.054 | 7.383 | A | o | 1 | dis | stmt · warn | `s31.jpg` — thick academic working paper, one paragraph in focus | **verdict `pop`** · `stamp` **199.45** |
| 32 | 3.11 | 205.437 | **8.140** | A | i | 2 | dis | stmt · — | `s32.jpg` — **weathered painted plaster wall texture flat evenly lit** — CALMEST bg, densest scene · cut-in **`s32b.jpg`** japanese street wall covered with posters@pexels | swap **+5.66** · `data-framings="5.66,2.48"` |
| 33 | 3.12 | 213.577 | 7.148 | **◆** | o | 1 | **SHOVE** | stmt @88 · fund | `s33.jpg` — single lit paper lantern in a dark street at night wide@pexels | **verdict `pop`** · `stamp` **214.98** · `transition` **220.725** |
| 34 | 4.1 | 220.725 | 7.252 | A | i | 2 | dis | stmt · — | `s34.jpg` — japanese ceramic bowl on wood@pexels | — |
| 35 | 4.2 | 227.977 | 7.331 | A | o | 1 | dis | stmt · — | `s35.jpg` — hand sewing a patch on fabric with a needle | — |
| 36 | 4.3 | 235.308 | **7.801** | A | i | 2 | dis | stmt · — | `s36.jpg` — single white shirt on a wooden hanger@pexels · cut-ins **`s36b.jpg`** cotton field at dawn · **`s36c.jpg`** semi truck on a highway@pexels | swaps **+2.74**, **+4.77** · `data-framings="2.74,2.03,3.031"` |
| 37 | 4.4 | 243.109 | 5.241 | A | o | 1 | dis | stmt · warn | `s37.jpg` — wall clock in an empty office corridor in the evening | — |
| 38 | 4.5 | 248.349 | 6.312 | A 🇺🇸 | i | 2 | dis | stmt · fund | `s38.jpg` — open american closet, dense hangers, price tags attached | **ICON** checkbox+tick `fundc`, **`pop`** · `chip` **250.55** |
| 39 | 4.6 | 254.661 | 7.069 | A 🇺🇸 | o | 1 | dis | stmt · fund | `s39.jpg` — printed bill invoice on a table@pexels | **ICON** checkbox+tick `fundc`, **`pop`** · `chip` **256.86** |
| 40 | 4.7 | 261.731 | 5.528 | A 🇺🇸 | i | 2 | dis | stmt · fund | `s40.jpg` — open refrigerator with fresh vegetables inside@pexels | **ICON** checkbox+tick `fundc`, **`pop`** · `chip` **263.93** |
| 41 | 4.8 | 267.259 | 6.364 | A | o | 1 | dis | stmt · warn | `s41.jpg` — stack of unopened cardboard delivery boxes in a room corner | — |
| 42 | 4.9 | 273.623 | 6.782 | A | i | 2 | dis | stmt · — | `s42.jpg` — hand picking up a product in a shop | — |
| 43 | 4.10 | 280.405 | 5.398 | **◆** | o | 1 | dis | stmt @88 · fund | `s43.jpg` — single object on a bare wooden table with hard side light@pexels | **verdict `pop`** · `stamp` **281.81** |
| 44 | 4.11 | 285.802 | 6.887 | A 🇺🇸 | i | 2 | dis | stmt · — | `s44.jpg` — empty shopping cart in a supermarket aisle@pexels | — |
| 45 | 4.12 | 292.689 | 7.749 | A | o | 1 | dis | stmt · — | `s45.jpg` — worn resoled leather boot beside a new boot in its box | — |
| 46 | 4.13 | 300.438 | 5.241 | A | i | 2 | dis | stmt · — | `s46.jpg` — japanese meal in small bowls on a tray | — |
| 47 | 5.1 | 305.678 | **8.167** | A | o | 1 | dis | stmt · — | `s47.jpg` — elderly people walking a coastal path at sunrise, silhouettes | *(longest single framing in the cut, no swap)* |
| 48 | 5.2 | 313.845 | 6.495 | A | i | 2 | dis | stmt · — | `s48.jpg` — bowl of white rice with chopsticks | — |
| 49 | 5.3 | 320.340 | 6.181 | A | o | 1 | dis | stmt · — | `s49.jpg` — chopsticks and a bowl on a table | — |
| 50 | 5.4 | 326.521 | 6.495 | A 🇺🇸 | i | 2 | dis | stmt · fund | `s50.jpg` — american kitchen counter@pexels | — |
| 51 | 5.5 | 333.016 | 7.148 | A 🇺🇸 | o | 1 | dis | stmt · fund | `s51.jpg` — two unequal stacks of twenty dollar bills squared on a table@pexels | stmt **335.74** anchored · `hero` |
| 52 | 5.6 | 340.163 | 7.304 | A | i | 2 | dis | stmt · warn | `s52.jpg` — open wallet without money | — |
| 53 | 5.7 | 347.468 | 6.965 | A 🇺🇸 | o | 1 | dis | stmt · fund | `s53.jpg` — manila envelopes on a wooden desk ⚠ **no bank UI** (D14) | — |
| 54 | 5.8 | 354.433 | 8.088 | A | i | 2 | dis | stmt · — | `s54.jpg` — old light switch in the on position with dust on the plate | — |
| 55 | 5.9 | 362.521 | 8.088 | **B** | o | 1 | dis | **num** · target | `s55.jpg` — printed table of numbers on paper@pexels | num `62.2%` **365.76** · `hero` |
| 56 | 5.10 | 370.609 | 7.331 | **B** 🇺🇸 | i | 2 | dis | **num** · fund | `s56.jpg` — one twenty dollar bill on a wooden table@pexels | num `$200` **376.28** *(dry — §2)* |
| 57 | 5.11 | 377.940 | 8.088 | A | o | 1 | dis | stmt · warn | `s57.jpg` — long straight american highway disappearing at the horizon | `reveal` **379.34** |
| 58 | 5.12 | 386.028 | 7.670 | A | i | 2 | dis | stmt · target | `s58.jpg` — old bound ledger with a cracked spine on a shelf | — |
| 59 | 6.1 | 393.698 | 7.069 | A | o | 1 | dis | stmt · — | `s59.jpg` — hand ruled household ledger open on a low table with a pen | — |
| 60 | 6.2 | 400.767 | 6.547 | A | i | 2 | dis | stmt · target | `s60.jpg` — antique letterpress printing type | — |
| 61 | 6.3 | 407.314 | 6.181 | A | o | 1 | dis | stmt · — | `s61.jpg` — shelf of identical bound annual editions with spines aligned | — |
| 62 | 6.4 | 413.496 | 6.469 | A | i | 2 | dis | stmt · — | `s62.jpg` — blank ruled notebook page close up no headings | — |
| 63 | 6.5 | 419.964 | 7.566 | A | o | 1 | dis | stmt · fund | `s63.jpg` — stacks of american coins on a table@pexels | — |
| 64 | 6.6 | 427.530 | 7.148 | A | i | 2 | dis | stmt · — | `s64.jpg` — glass inkwell and dip pen nib on a wooden desk low light | — |
| 65 | 6.7 | 434.678 | 7.252 | **◆** 🇺🇸 | o | 1 | **hold** | stmt @88 · warn | `s65.jpg` — twenty dollar bills spread top down on a dark wooden table@pexels | **verdict `pop`** · `stamp` **436.08** |
| 66 | 6.8 | 441.930 | 6.965 | A | o | 2 | dis | stmt · — | *holds `s65.jpg`* — tighter crop on the printed panel of one note, zoom continues | — |
| 67 | 6.9 | 448.895 | 7.252 | A | i | 1 | dis | stmt · — | `s67.jpg` — open blank diary page with a date | — |
| 68 | 6.10 | 456.147 | 7.148 | A 🇺🇸 | o | 2 | dis | stmt · fund | `s68.jpg` — handwritten notes on lined paper@pexels | — |
| 69 | 6.11 | 463.295 | 6.887 | A | i | 1 | dis | stmt · fund | `s69.jpg` — handwritten note with the second line underlined in ink | **ICON** two rules, lower lifting past upper, `fundc` · `tick` **465.50** (`pulse`) |
| 70 | 6.12 | 470.181 | 7.435 | A 🇺🇸 | o | 2 | dis | stmt · — | `s70.jpg` — phone lying face down beside an open notebook and a pen | — |
| 71 | 6.13 | 477.616 | 6.077 | A | i | 1 | dis | stmt · — | `s71.jpg` — printed paper document beside an open notebook on a desk@pexels | — |
| 72 | 6.14 | 483.693 | 7.331 | **B** 🇺🇸 | o | 2 | dis | **num** · warn | `s72.jpg` — mechanic working under a car in a repair garage@pexels | num `OVER 20%` **489.10** *(dry — §2)* |
| 73 | 6.15 | 491.024 | 6.965 | **B** 🇺🇸 | i | 1 | **SHOVE** | **num** · target | `s73.jpg` — long shop receipt on a table | num `4 IN 10` **493.62** *(dry)* · `transition` **497.989** |
| 74 | 7.1 | 497.989 | 5.946 | A | o | 2 | dis | stmt · target | `s74.jpg` — moss edged stone path in mist kyoto | — |
| 75 | 7.2 | 503.935 | 7.069 | A | i | 1 | dis | stmt · — | `s75.jpg` — zen rock garden raked gravel@pexels | — |
| 76 | 7.3 | 511.004 | 6.364 | A | o | 2 | dis | stmt · — | `s76.jpg` — japanese stone water basin tsukubai with bamboo ladle@pexels — the kanji live **in the photograph** | — |
| 77 | 7.4 | 517.368 | **7.304** | **◆** | i | 1 | **hold** | stmt @88 · target | `s77.jpg` — square stone water basin japanese garden@pexels | `reveal` **518.77** |
| 78 | 7.5 | 524.673 | 7.200 | A | i | 2 | dis | stmt · — | *holds `s77.jpg`* — tighter crop on the still water at the centre, zoom continues | — |
| 79 | 7.6 | 531.873 | **8.349** | A 🇺🇸 | o | 1 | dis | stmt · — | `s79.jpg` — framed diploma and car keys on an american kitchen counter · cut-in **`s79b.jpg`** used sedan outside an american apartment building at dusk | swap **+5.50** · `data-framings="5.50,2.849"` |
| 80 | 7.7 | 540.222 | 6.077 | A 🇺🇸 | i | 2 | dis | stmt · warn | `s80.jpg` — chalk finish line on asphalt half rubbed out and redrawn | — |
| 81 | 7.8 | 546.299 | 6.730 | A | o | 1 | dis | stmt · — | `s81.jpg` — two near identical jackets on hangers one newer | — |
| 82 | 7.9 | 553.029 | 6.364 | A | i | 2 | dis | stmt · warn | `s82.jpg` — blurred neon city lights at night bokeh | — |
| 83 | 7.10 | 559.393 | 7.905 | A | o | 1 | dis | stmt · fund | `s83.jpg` — empty chair by a window | — |
| 84 | 7.11 | 567.298 | 6.834 | A | i | 2 | dis | stmt · — | `s84.jpg` — japanese rock garden at last light wide | — |
| 85 | 8.1 | 574.132 | 6.260 | A | o | 1 | dis | stmt · — | `s85.jpg` — bare empty wooden shelf@pexels | — |
| 86 | 8.2 | 580.392 | 6.260 | A 🇺🇸 | i | 2 | dis | stmt · fund | `s86.jpg` — stack of twenty dollar bills squared on a wooden table@pexels | — |
| 87 | 8.3 | 586.651 | 7.148 | A 🇺🇸 | o | 1 | dis | stmt · fund | `s87.jpg` — handwritten ledger page filled with entries | — |
| 88 | 8.4 | 593.799 | 6.233 | A | i | 2 | dis | stmt · target | `s88.jpg` — japanese temple water basin bamboo ladle | — |
| 89 | 8.5 | 600.033 | 7.487 | A 🇺🇸 | o | 1 | dis | stmt · fund | `s89.jpg` — notebook and pen on a table under a lamp | — |
| 90 | 8.6 | 607.520 | 6.678 | **◆** 🇺🇸 | i | 2 | dis | stmt @88 · — | `s90.jpg` — handwritten to do list on paper@pexels | **verdict `pop`** · `stamp` **608.92** |
| 91 | 8.7 | 614.198 | 6.651 | **C** | o | 1 | dis | **`.cta` block** · **pop** | `s91.jpg` — closed leather notebook on a desk | `.cta` `SUBSCRIBE` **616.61** · `cta` |
| 92 | 8.8 | 620.849 | 5.894 | A 🇺🇸 | i | 2 | *(last)* | stmt · — | `s92.jpg` — two coffee mugs on a porch rail at night no people | — |

**Row checks.** 92 scenes ✓ · last scene ends 620.849 + 5.894 = **626.743** = `timing.json`
total ✓ · **7 SOLO** (s1, s17, s33, s43, s65, s77, s90) = exactly the seven `RAIL OFF` scenes
the script names (1.1, 2.7, 3.12, 4.10, 6.7, 7.4, 8.6) ✓ · 29 🇺🇸 act-now frames = the script
handoff §7 list ✓ · 2 SHOVE ✓ · 3 hold pairs ✓ · 11 `num`/CTA focals, never with a `stmt` ✓ ·
`.mega` exactly once (s17) ✓ · `--pop` exactly once (s91) ✓ · ken never repeats a direction
except across a hold ✓ · trk alternates by parity ✓ · max `dur` 8.349 < 9.0 ✓ ·
3 `data-framings`, each partitioning its own scene ✓ · every scene ≤ 3 content elements ✓.

---

## 8. Vector art — 5 icons, 0 Lotties

**Zero Lotties, deliberately.** `lottie-web` redraws its whole illustration every frame and
measured **2.7×** on a 20s render; at 626.7s that is the single most expensive thing this
storyboard could ask for, and nothing in this argument is a person, a device or a scene that a
photograph does not carry better. `max_per_video` is 3; this cut spends 0 and says so.

**Five icons**, all inline `<svg class="icon …">` at cue slot 3 (+2.10). Free,
palette-coloured, no asset to fetch. **None sits on a type-B (`num`) scene** — that scene
already has its focal element and `one_focal_per_scene` caps it at one. None sits adjacent to
another except the declared s38–s40 set.

| scene | line | shape (one line, for fin-build to draw) | role class | motion |
|---|---|---|---|---|
| s24 | 3.3 | a closed padlock, shackle down | **`warnc`** | `draw` |
| s38 | 4.5 | an empty square with a tick struck through it | `fundc` | **`pop`** (§4) |
| s39 | 4.6 | the same square and tick | `fundc` | **`pop`** |
| s40 | 4.7 | the same square and tick | `fundc` | **`pop`** |
| s69 | 6.11 | two short horizontal rules, the lower one lifting past the upper on a curved arrow | `fundc` | `draw`, then `pulse` at 465.50 |

⚠ **s24 must carry `warnc`, not `warn`.** `.warn` is the *component modifier* (`.chip.warn`,
`.stamp.warn`); an `<svg class="icon warn">` matches no colour rule, inherits `--ink`, and
paints a **white** padlock that passes every check. That is the exact defect found on the hi
cut's s24. `.warnc` now exists in `assets/blockframe.css` — use it.

The three checkboxes on s38–s40 are **one declared set**, the visual half of the same gesture
as SFX cues 12–14. Repeating a mark three consecutive times is legible precisely because the VO
is enumerating three checks; it happens nowhere else in the cut.

**Five, not the hi cut's six.** The hi cut's sixth icon (a pen nib drawing one line, `fundc`)
sat on hi 7.11 "WHY IT MATTERS" — **a line the US rewrite does not contain.** Adding a
replacement icon elsewhere to keep the count matching would be decoration chasing symmetry.
Divergence D20.

**Emoji: none, and it is a decision.** The tonal break one would buy would land as a sticker on
a dark documentary grade, and it renders from an OS font outside the grade. The two places
tempted (the 🇺🇸 markers, the ⚠ flags) are *storyboard notation in this file*, never
composition text.

---

## 9. Imagery — 96 slots, 93 files, all already on disk

- **92 bg slots**, of which **3 re-use a hold partner's file** (s2←s1, s66←s65, s78←s77) →
  **89 bg files**.
- **4 cut-in / second-framing files**: `s32b`, `s36b`, `s36c`, `s79b`.
- **Total files: 93 — all fetched, all passing the asset gate.** Nothing in this rewrite
  re-specs an image; §7's `bg` column quotes `assets/img/manifest.json` verbatim, and the
  manifest is **unchanged by this attempt** (byte-identical to the file fin-assets wrote).
- **Zero photo-free scenes** (`photo_free_scene_ratio` = 0, creator rule 2026-07-28).

**Densest scene gets the calmest background.** s32 (3.11) carries the five actual reasons Japan
saved as one 76px statement. Its bg is a **flat weathered-plaster wall texture**, with the
poster wall arriving as the second framing at +5.66 — density managed by choosing a quieter
image, never by dropping one.

**Cut-in budget, stated plainly.** The creator rule asks for a cut-in per concrete thing the VO
names. This cut spends its cut-ins on the three scenes that name **more objects than one frame
can hold** (s32, s36, s79). Everywhere else **the background image *is* the named object** —
the colander, the calendar, the closet, the refrigerator, the basin — which is the same rule
satisfied with one photograph instead of two, and is the design doc's own "drop a cut-in rather
than fake it".

**Localisation.** Japan owns the story frames (s11, s19, s28, s34, s46–s49, s60, s74–s78, s84,
s88). **Every frame where the viewer is asked to act is American** — all 29 🇺🇸 rows. The trap
fin-research named is *a beautiful video about Japan*; the counter-measure is that the beats
which cost the viewer something (4.5–4.7, 5.4–5.5, 8.5–8.6) are shot in an American closet,
kitchen and refrigerator.

### 9a. ⚠ The 1280px upscale, and the five slots the creator should rule on

**52 of the 93 files are 1280px wide** — every Pixabay promotion except `s34.jpg` (1880px, the
re-encoded one). The Pixabay key has no full-HD access; verified. The other 41 are Pexels at
1880px. Under `blockframe-9` every photo is **full-bleed at `inset:-8%`**, so a 1280px source
is drawn at roughly **1.63× on the long edge** (2227px of canvas across the bleed box) — worse
than the `.rail` panel's 1.5×, because the panel only occupied 740px.

**This is the same trade the three prior blockframe-9 cuts shipped, so nothing is re-sourced.**
Two things make it survivable and they are not luck: the grade
(`grayscale .32 · brightness .62 · contrast 1.05`) plus 5% grain over an upscale is a
soft-focus treatment, and heavy 76–240px type is what the eye reads.

**Every `hero` cue in the video lands on an 1880px Pexels file** — s13, s16, s17, s25, s30,
s51, s55. Not one big number sits on an upscale. So does every SOLO frame except none:
s1, s17, s33, s43, s65, s77, s90 are **all** Pexels 1880px.

**Named for a decision, in the order I would rank them** (all 1280px, all carrying a punctuated
or terminal beat):

| slot | beat | why it is on this list |
|---|---|---|
| **`s91.jpg`** | 8.7 · the `.cta` block, `SUBSCRIBE`, the **last full frame of the video** | the closing frame is the one a viewer looks at longest and the one a thumbnail-adjacent still gets pulled from. Highest value per pixel in the cut |
| **`s31.jpg`** | 3.10 · `stamp` — "not a major determinant", the premise correction | the argument's turn, and it is a *paper* photograph, where an upscale shows as mushy print texture |
| **`s73.jpg`** | 6.15 · `num 4 IN 10`, dry, 2.0s before SHOVE #2 | a receipt is fine print; fine print is the worst subject for a 1.63× upscale |
| **`s9.jpg`** | 1.9 · `reveal` — "a little everywhere", the cold open's thesis | the colander's holes are the whole image and they are small |
| **`s38.jpg`** | 4.5 · `chip` — CHECK ONE, first of the three-icon set | price tags are the readable detail; least critical of the five |

**My recommendation is to ship all five.** The four beats besides s91 are carried by type and
by sound, and the photograph is texture under a scrim. If exactly one is re-sourced, make it
**`s91.jpg`** — a closed notebook on a desk is a trivially common Pexels subject and it is the
frame that closes the video. This is the creator's call, not this stage's.

**Standing rejections for fin-assets** (already satisfied by the files on disk; restated so a
re-fetch cannot regress):
- **Never a phone or laptop screen as a background.** Four slots are screen-adjacent by script
  (s1, s8, s12, s39) and all four dodge it: glow-only with the phone edge-on, a paper document
  at the desk, a silhouetted handset, and a **printed** invoice standing in for 4.6's
  subscriptions list. This defect has shipped three times undetected.
- **$ slots must be current US Federal Reserve notes and must not be prop money** — s21, s51,
  s56, s65, s86; read at FULL resolution, because repeated serial numbers become legible in
  exactly the stacked framings a contact sheet hides.
- **No non-US currency, signage, plugs, licence plates or vehicles.** No ₹, lakh, UPI,
  passbook, two-wheeler or wedding envelope — those are the hi cut's props and script guardrail
  #1 bars them from this file.
- **s30's chart must peak and then fall.** A rising line under "hardly ever above five percent
  since two thousand two" is the picture arguing against the script.
- **md5 across ALL projects, both channels**, including the hi cut of this video.

**Image prompts have one home: `assets/img/manifest.json`.** `tools/stock/pixabay_fetch.py`
writes each slot's query to `assets/img/<slot>.src` on promotion, so the `.src` sidecars **are**
the reproducible photography record the finished-video rule requires. s2/s66/s78 are absent
from the manifest because they are crops of s1/s65/s77, and a second file for them would be a
second photograph — the one thing a hold forbids.

---

## 10. Timing

`scene_duration = 0.25 (VO lead-in) + clip_duration + 0.55 (tail)` — the **LONG** override
(`format.json tiers.long`), not the `scene.*` 0.4/1.0 SHORT defaults.
`data-duration = scene_duration + 0.45` on s1–s91; s92 bare. Root = **626.743s**.

Generated from `timing.json` — **never hand-edited**. The same numbers live in four places
(`<section>`, the JS `S` map, the `<audio>` row, root `data-duration`); updating three of four
passes every check and ships a video whose animations fire against the old timeline.

Per-scene figures are the `start` / `dur` columns of §7 — not restated, one home per fact.

**What the re-voice moved.** 7.4 was re-recorded (the "square hole" claim is gone from the VO
and from the on-screen text). Its `scene_duration` went 7.148 → **7.304**, its `scene_start`
did **not** move (517.368), and every scene from **7.5 (s78) onward shifted +0.157s**. Total
626.586 → **626.743**. Consequences, all of them already applied above: §2 cues #23 and #24,
and the `start` column of rows 78–92. Nothing else in the cut changes.

**Measured delivery rate, for `format.json`'s owed fix.** 9,619 chars / 626.743s = **15.35 c/s
including all inter-line padding**, or **9,619 / 553.143s of actual audio = 17.39 c/s flat.**
Third independent measurement above 17.3 against a 16.1 key. Per
`cuts.en._chars_per_second_trap` the fix is BOTH-OR-NEITHER (budget formula first, then the
key) and neither is this stage's to write.

---

## 11. Divergences from `storyboard-hi.md` (mandatory — a zero-divergence port is a red flag)

**What ported:** the element ID scheme (`s<n>-<part>`, with `-bg`/`-bg2`/`-head`/`-stmt`/
`-num`/`-foot`/`-icon` keeping their names), the beat structure, the transition classes and
their mechanics (§5), the `hold` = continuous-zoom rule, the icon shapes, the SFX ceiling of
24 and its placement, and the colour semantics. A fix to any of those in one cut is a fix in
both.

⚠ **D0 is architecture-level and will apply to the hi cut too once it is re-storyboarded.**
`storyboard-hi.md` is still the `ledger-rail` version as of this writing; the creator's
2026-08-01 decision moves **both** cuts to `blockframe-9`.

| # | scene(s) | diverges how | why |
|---|---|---|---|
| **D0** | **all** | **Architecture: `blockframe-9`, not `ledger-rail`.** The rail column, the 300px index/beat furniture, the hard-edged photo panel, `panelOpen`, `hairDraw`, `panelSwap` and `railIn` are all deleted; the photo is full-bleed and the stack is centred | creator decision 2026-08-01 after seeing a rendered ledger-rail frame. Not a per-cut choice — both cuts move |
| **D0a** | all | **Scrim + `text-shadow` ON everywhere** (`.rail`: off on 85 scenes, on for 7) | type sits on the photograph in every frame now |
| **D0b** | all | **`ken` is the full 1.0↔1.16 on all 92** (`.rail`: 1.0↔1.06 inside the panel, full only on 7) | full-bleed photo, so the full move is the one the design doc specifies |
| **D0c** | all | **Per-scene `--tint` is restored** and derived from the role colour (§1a); `.rail` retired it | `blockframe-9` has the four-layer scrim, and scrim layer 1 is the tint's host |
| **D0d** | 7 scenes | **`RAIL OFF` becomes `SOLO`** — the same seven scenes vary by emptying the stack (no kicker, focal @88 / `.mega` 240) rather than by retracting a rail | the device has to be re-derived because its mechanism no longer exists; the *job* is unchanged |
| **D0e** | all | **The 5-item `.rail` assembly cascade is gone; the ladder is 4 cues** and needs no declared cascade exception | the furniture it assembled does not exist. Every cue now clears `cue_min_gap_seconds` 0.8 outright |
| **D0f** | s31, s33, s43, s65, s90 + s38–s40, s69 | **Verdict/chip/tick cues are re-bound to real helpers** — focal enters with `pop` on the five stamp scenes, the three checkbox icons `pop` instead of `draw`, s69's icon `pulse`s after drawing | under `.rail` a `stamp` sound fired against a `rise`, which is a sound with no helper (kit.json `_discipline`). Fixed at the ladder, not by dropping cues |
| **D1** | **s59–s84** | **The `#` ↔ line-id mapping is rebuilt, not renumbered.** s1–s58 and s85–s92 carry the same line ids as the hi cut; s59–s73 shift by one and s74–s84 shift back | en Chapter 6 has **15** lines to hi's 14 (6.15, the Fed SHED figure, is new) and en Chapter 7 has **11** to hi's 12. Both cuts still total 92, and the ids realign at s85 |
| **D2** | all | **Every `start` / `dur` is a different number.** 626.743s against 659.709s | Brian delivers at 17.39 c/s flat; Harsh at 13.03. Not one timing figure may be carried across |
| **D3** | 9 type-B scenes + 5 verdicts + 3 swaps | **Not one anchored `f` fraction is ported** | every hi fraction is a Hindi word position. `37.8%` lands at f 0.51 here and f 0.68 there |
| **D4** | **§6** | **Zero `max_scene_seconds` breaches** — the hi cut's s19/s25/s32 findings (9.185, 9.002, 9.760) do not exist. No `known_benign` entry is owed | the faster delivery rate. The `data-framings` this cut emits are about **enumeration**, not about clearing a gate |
| **D5** | **s1, s2** | phone **face-UP**, glow-only, screen never legible (hi: face-down) | en 1.1 is a direct-deposit notification landing; hi 1.1 opened on the phone already put down |
| **D6** | s4 | a six-month auto-insurance renewal letter (hi: a bank statement with a pen circling an auto-debit) | en 1.4 is about the renewal that bills twice a year |
| **D7** | s5 | takeout bag + gift bag (hi: a red-and-gold Indian wedding envelope) | US market. Guardrail #1 bars the envelope from this file |
| **D8** | s8 | a paper document at the desk (hi: a hand writing in a notebook) | en 1.8 says "scroll back through the statement"; the screen is kept out of frame |
| **D9** | s19 | **single framing, no swap** (hi s19 carried one to survive a 9.185s scene) | en 2.9 is 7.853s. A swap here would be cosmetic and would fail the new check |
| **D10** | s21, s44, s51, s56, s86 | dollars, US grocery aisle (hi: ₹500 notes, an Indian shop counter, a two-note ₹ stack) | currency and market |
| **D11** | s25 | **no swap** (hi s25 had one for a 9.002s scene — the "fails by two milliseconds" case) | en 3.4 is 7.304s |
| **D12** | s27 | a sealed full jar (hi: a clay pot with cloth tied over its mouth) | the pot is an Indian household object; a sealed jar carries "the half nobody shows" in a US frame |
| **D13** | s36 | **bg is the shirt, cut-ins are the field and the truck** (hi: bg was the field, cut-ins the handloom and a truck) | en 4.3 opens on "The shirt hanging in your closet". The handloom is replaced by a US interstate semi; **the mill is deliberately dropped** |
| **D14** | **s53** | **New scene with no hi counterpart.** en 5.7 is automate-and-separate. Its image is **manila envelopes**, not a transfer screen | fin-audit-en-1 stripped "a federally insured savings account" out of 5.7 as a product-category placement. A bank-UI photograph would put the recommendation back through the picture |
| **D15** | *(no scene)* | **hi's 5.10 "ENTRY TICKET" (₹500 SIP / ₹250) has no en counterpart** | those instruments do not exist in the US cut and naming an equivalent would be the account pick the persona rule forbids. en 5.10 is the $200 floor |
| **D16** | s55, s56 | **two adjacent type-B scenes** (62.2%, then $200). hi separated its two with a statement | the en line order puts Japan's consumption share directly before the de-escalation. Each still carries one focal, and 5.10 is DRY so only one is punctuated |
| **D17** | s72 | a car on a shop lift (hi s72: a post-office counter and a brass grille) | en 6.14 is the Fed G.19 card APR against a $400 car repair; hi 6.14 was India Post / PPF |
| **D18** | **s73**, and SHOVE #2 | **New scene** (6.15, Fed SHED, `4 IN 10`); the second shove sits on **s73→s74** rather than hi's s72→s73 | the US cut has a second Fed figure the Indian cut has no equivalent for. Same turn, one scene later |
| **D19** | s77, s78 | the third hold pair is **s77→s78** (hi: s76→s77) | same D1 index shift |
| **D20** | *(no scene)* | **5 icons, not 6** — the pen-nib icon is gone | it lived on hi 7.11 "WHY IT MATTERS", a line the US rewrite does not contain |
| **D21** | s79 | **swap to the car-and-apartment frame**; hi's equivalent (s78) had none | en 7.6 is the **longest scene in the cut** (8.349s) and enumerates six things. Its hi counterpart was 7.200s |
| **D22** | s57, s89, s92 | a US interstate, an American kitchen table, two coffee mugs on a porch rail (hi: an Indian road, a wooden table at night, two steel cups of chai) | the closing image of each cut is that market's own late-night object |
| **D23** | **§2** | **the `bed-resolve` loop-dip escalation is retracted in this cut** | `mix.py` crossfade-loops the bed; there is no dip. The hi storyboard still carries the flag and it should be struck there too |
| **D24** | **s65, s66** | **the s65 photograph is $ notes on a dark table with no ledger** (hi: ₹ notes on an open ruled account book), and **s66's crop lands on one note's printed panel** rather than on ruled column headings | currency and market, plus this cut's promoted file is the rung-3 fallback of the attempt-2 retry ladder. It passes the gate; s66's crop is weaker than the hi cut's and this row is the record of that |
| **D25** | **s77, and §2 cue 22** | **the on-screen text no longer says "square"** — 7.4's stmt is "All four share one part — the emptiness at the centre" | VO 7.4 was re-voiced 2026-08-01 and dropped the "square hole" claim. The *image* is still a square basin, which is fine; the *text* must not promise what the VO no longer says. The old storyboard's cue-22 note ("the empty square at the centre") is deleted |
| **D26** | **§9a** | **the upscale ledger is new** — 52 of 93 files at 1280px against a full-bleed frame, with five slots named for a creator decision | `.rail` confined the photo to a 740px panel, so the upscale never had to be argued. Full-bleed makes it a real number and it is stated rather than absorbed |

---

## 12. Deliberate placeholders (must be real before publish)

1. **The five 1280px slots of §9a await a creator ruling.** Default, and my recommendation:
   **ship all five unchanged.** If exactly one is re-sourced, `s91.jpg` (the closing frame).
   Nothing downstream is blocked either way — the files pass the gate today.
2. **`format.json cuts.en.chars_per_second` is owed a raise from 16.1** (§10) — third
   measurement above 17.3, and the budget-formula fix must land first. `tools/` is not writable
   from this stage.

*(The attempt-2 s65 recut is closed: the rung-3 file is on disk, passes the gate, and its
weaker s66 crop is recorded as divergence D24. The bed-length item is deleted, not deferred —
see §2 and D23.)*

---

## Sign-off

- [x] Colour semantics table filled and consistent with the script (§1) — inversion trap named, the one red `num` declared, and every role backed by a colour class that exists in `blockframe.css` (§1a)
- [x] Every number traced to a sourced line — all figures come from `script-en.md`'s fact trace; this file adds none
- [x] Architecture is the one in `run.json` (**`blockframe-9`**) — centred stack, full-bleed photo, scrim + text-shadow on all 92, `ken` 1.0↔1.16, `#root class="cut-en"` for the watermark
- [x] Type treatment re-derived for this architecture, not ported (§3a) — every size is a `type_ladder_px` value, `.mega` used once
- [x] Every scene ≤ 9.0s, and every `data-framings` partitions its own scene (§6)
- [x] The s77+s78 hold is intact — one file, one continuous zoom, both `i`, s78 has no file
- [x] 7.4's on-screen text no longer promises a square (§11 D25)
- [x] Zero photo-free scenes (92/92 carry a bg) — `photo_free_scene_ratio` 0 ✓
- [x] SFX = the declared 24 on `bed-resolve`, no two inside 0.8s (closest 6.31s), dry beats declared, every cue bound to a helper that runs (§4 D0f)
- [x] Bed length not flagged — `mix.py` crossfade-loops it (§2)
- [x] On-screen Japanese is romaji only; kanji only inside the s76/s77/s88 photographs
- [x] No ₹, lakh, crore, UPI, PPF, SIP, passbook or Indian prop anywhere in a query or a cue
- [x] Explicit divergence list, 26 rows, one reason each (§11)
- [ ] No image hash reused from any prior video on either channel — **fin-assets** verified at fetch; manifest unchanged by this attempt
- [ ] Creator approved (Gate ②) — date: __
