---
summary: The durable design system for the finance channels (@cashguruguides ₹ · @moneymavens101 $) — dark blockframe, photographic backgrounds under a single grade, heavy type, chip/stamp motion language. Extracted from the shipped needs-vs-wants pair. Copy into each video's DESIGN.md. **§0 — blockframe-9 is LOCKED by creator decision 2026-07-30 (thirteen styles reviewed side by side); this supersedes every "next cut MUST change architecture" flag in the vault, and moves the sameness budget onto the non-layout levers.**
updated: 2026-08-01
source: distilled from vault/videos/needs-vs-wants/src/hi/index.html + needs-vs-wants-en/index.html (both shipped) and vault/videos/needs-vs-wants/storyboard-hi.md · verified against the rendered output 2026-07-28
stage: ADOPTED — the standing design system for both finance channels
---

# DESIGN — Finance blockframe (dark grade)

> **BOX — the decisions. The CSS below is the authority for every value; this box
> carries only what the CSS cannot say.**
> 1. **blockframe-9 is LOCKED** (creator 2026-07-30, thirteen styles reviewed side
>    by side). This supersedes every "the next cut MUST change architecture" flag
>    in the vault. The sameness budget moves onto the non-layout levers.
> 2. **Every architecture must carry a photograph in every scene.** Machine-enforced:
>    `format.json architectures[*].image_per_scene: true`, and `doctor` refuses one
>    that does not. A style that renders type on flat colour cannot be added, however
>    good the mockup.
> 3. **Live style verdicts** — `x-post`/`reddit-post` usable as a COMPONENT, never an
>    architecture; `swiss-grid`/`vignelli` approved to pursue; `news-ticker`,
>    `code-snippet`, `code-typing` rejected as off-genre. `ledger-rail` was built,
>    rendered and rejected — do not re-propose it.
> 4. **Colour is roles, never meanings. One role colour per scene.**
> 5. **The type ladder is stepped, never interpolated.** Do not substitute Archivo
>    Black, despite [[design-techtooltester]] naming it.
> 6. **`.scene { isolation: isolate }` and the four-layer scrim order are
>    load-bearing** — changing either silently changes every frame.
> 7. **Determinism: everything vendored.** GSAP and fonts self-hosted, no CDN, no
>    `Date.now()`, no unseeded random, no render-time fetch. A slow CDN produces a
>    render that SUCCEEDS with every element frozen at frame 0 and passes `check`.
> 8. **The checker is evidence, not authority.** Fail loudly on a NEW finding; never
>    edit a design token to satisfy a checker.
> 9. **Supersedes [[design-techtooltester]] for all finance work.** MEDIUM/LONG cuts
>    extend this with [[design-chapter-archetypes]], which owns the archetype layer.
>
> **Open the body when:** you need a VALUE (a token, a timing, a component's markup,
> the grade constants) and `blockframe.css` / `format.json` did not answer it — which
> should be rare, because they are the code home and they win.

> **The system now has a code home (2026-07-29). This file is the rationale;
> the implementation is two files and they are linked, never copied:**
>
> - `tools/scaffold/assets/blockframe.css` — tokens, grade, scrim, type
>   ladder, every component, and the `.rail` architecture variant.
> - `tools/scaffold/assets/js/motion.js` — every motion helper, including the
>   scene transitions this doc used to have no answer for.
>
> Where they disagree with the prose below, **the files win** — they are what
> renders.
>
> **Chapter-based (MEDIUM/LONG) cuts extend this with the archetype layer** —
> `tools/scaffold/assets/chapter-design.css`, documented in
> [[design-chapter-archetypes]]. That note owns the four scene layouts, the
> plate, the ground temperature arc and the photograph rules; this note still
> owns the tokens, the grade, the scrim, the type ladder and the watermark. Until now each cut was scaffolded by copying the previous cut's
> `index.html`, which produced five divergent stylesheets, five different motion
> vocabularies, and four cuts that silently lost `@font-face` and rendered in
> Arial Black. Full evidence: [[finance-audit-2026-07-29/index]].

> **This file supersedes [[design-techtooltester]] for all finance work.**
> That note is the **bright** TechToolTester system — white/pastel gradient,
> *"No grain. No vignette. No black."* The finance format is its opposite:
> `#0d1017`, full-bleed photography, grain, four-layer scrim. Pointing a
> scripting or storyboard agent at the wrong one is how drift starts on run #1.

The channel's visual register: **dark, dense, confident.** Money facts stated
plainly in heavy type over photographic texture. Nothing decorative, nothing cute.

---

## 0. The architecture decision — blockframe-9 is LOCKED (creator, 2026-07-30)

**Standing decision. This supersedes every "the next cut MUST change
architecture" flag in the vault** ([[../videos/good-debt-vs-bad-debt/index]],
[[../videos/credit-history/index]], [[../index]]) — those were written when the
sameness had never been *chosen*, only defaulted into six times.

The creator reviewed thirteen candidate styles side by side as rendered 16:9
mockups — the three costed layout alternatives (`ledger-rail`, `statement-card`,
`split-register`) plus nine new directions backed by real HyperFrames registry
blocks (`data-chart`/`nyt-graph`, `news-ticker`, `kinetic-type`, `swiss-grid`/
`vignelli`, `world-map`, `flowchart`, `x-post`/`reddit-post`, terminal, liquid
glass) — and **chose to keep blockframe-9.**

Mechanically: `tools/format.json` now carries `architecture_lock:
"blockframe-9"`. `pipeline_check.next_architecture()` returns it and the
`architecture` CLI prints `LOCKED`; `doctor` refuses a lock naming an
architecture that does not exist, so a typo cannot degrade to silent rotation.
The rotation code stays — delete the key to resume cycling.

**Why a lock and not just a preference.** The rotation was built because a
warning written in four places changed nothing — only the *default* is a real
control. That argument is symmetric: once a layout is genuinely chosen, a
rotation that varies away from it is the pipeline overriding its owner. So the
decision goes where code reads it.

**What now carries the sameness risk** (real — YouTube's inauthentic-content
policy is about templating, and all ten thumbnails are still one layout):
layout is no longer the variance axis, so the non-layout levers are. Live
already: scene transitions (`dissolve`/`shove`/`sceneTransitions` in
`tools/scaffold/assets/js/motion.js`, asserted by `check_build`) and the
SFX kit (tools/audio/kit.json). **Owed: the music bed** — fully specced in
`tools/audio/kit.json` (two beds, prompts, levels) and mixed by
`tools/audio/mix.py`, but `studio/library/music/` is empty because ElevenLabs
music generation needs the `music_generation` permission on the key. Either add
that permission and run `tools/audio/sfx.py --kit --music`, or drop two mp3s in
by hand from the YouTube Audio Library. **Still open and NOT settled by this
decision: runtime.** The 90–300 s band is the worst-performing one in both
markets ([[finance-audit-2026-07-29/01-performance]]); locking the layout says
nothing about the tier.

### 0a. Style verdicts and the image rule (creator, 2026-07-30, after review)

Having seen the thirteen mockups rendered, the creator gave per-style feedback.
**The rejection was mostly one thing:** *"most of them are without images i dont
want that. images are compulsury even in future i want to use stock videos too."*

| Style | Verdict |
|---|---|
| **blockframe-9** | **Kept** — the lock above |
| `news-ticker` | ✗ *"we are not making news videos so this is irrelevant to finance education videos"* |
| `code-snippet`, `code-typing` | ✗ *"we are not making coding videos"* |
| `x-post` / `reddit-post` | ✓ **as a component, not an architecture** — usable when a real, topical social post exists |
| `swiss-grid` / `vignelli` | ✓ **pursue** — *"lets try this one add this style as a new style"*, pending research |
| the rest | ✗ for now — carried no photograph; any that can be re-cut to carry one may return |

**The image rule is now machine-enforced.** Every entry in `format.json`
`architectures` must declare `image_per_scene: true`, and `doctor` refuses one
that does not. A style that renders type on flat colour cannot be added, however
good it looks in a mockup. This is the "unrepresentable wrong state" tier of
[[../../CLAUDE|fix-defaults-not-gates]] rather than a note somebody has to
remember — which is the whole lesson of §0.

**Style is now ASKED at intake**, as a second question beside the tier (creator:
*"ask when i start a new finance video run as you ask question for length as for
style"*). The lock is the pre-selected default, not an imposition — see
`.claude/commands/finance-video.md` §2 step 2a.

**Two open threads**, both under research 2026-07-30:
- **Swiss/Vignelli with compulsory photography.** The tension is real: that
  tradition as popularly imitated is image-sparse, which is exactly what got the
  other styles rejected. The research question is how the tradition *actually*
  places photographs in a grid (Müller-Brockmann's photographic posters,
  Vignelli's Knoll and Rizzoli work), and whether that yields a direction here.
- **Stock video behind the frames.** Wanted "even in future"; blocked on whether
  the deterministic frame-walking renderer can seek a `<video>` element per
  frame. Do not put `<video>` in a composition until `format.json`
  `_stock_video_note` says it is proven.

**`social-quote` rules** (`format.json _components`): a real post only — an
invented one is a fabricated fact and breaks the never-invent rule. Prefer
institutional or public accounts; do not put a private individual's handle in a
monetised video that criticises their money decisions.

---

## 1. Stage and grade

### ledger-rail was built, rendered and rejected (creator, 2026-08-01)

`ledger-rail` (300px left rail carrying the scene index + beat label, content
ragged right, photo in a 740px panel) was chosen at intake for
japanese-money-methods, built to completion on both cuts, and **rejected by the
creator on sight of one rendered hi frame** — *"i have seen the ledger frame hi and
honestly i dont like it"*. Both cuts were regenerated on `blockframe-9`.

Three things this cost, worth knowing before anyone offers a non-default style again:

1. **Storyboards and compositions are architecture-specific; nothing else is.**
   Research, facts, scripts, audits, voice and images all survived the switch
   untouched. The rebuild was two storyboards and two builds — real, but bounded.
2. **A finished master had to be discarded.** The hi cut was already encoded,
   mixed and normalised to −14 LUFS when the rejection came. **Show the creator a
   rendered frame before the first encode, not after** — snapshotting costs about
   two minutes against ~35 per encode.
3. **Full-bleed changes the image-resolution economics.** In `ledger-rail` a
   1280px Pixabay file sat in a 740px panel and was oversampled. Under
   `blockframe-9` every photo is full-bleed at `inset:-8%` ⇒ roughly **1.63× on the
   long edge**. The Pixabay key has no full-HD access (`fullHDURL`/`imageURL`
   absent — verified against the API 2026-08-01), so 1280px is its ceiling and
   Pexels `large2x` at 1880px is the only upgrade path. **Route every hero, SOLO and
   closing frame to Pexels**; Pixabay is fine for texture under a scrim, where the
   grade plus 5% grain reads as soft focus. See [[stock-photo-sourcing]].

⚠ **Untested at length:** the three blockframe-9 cuts shipped before this one were
9-scene SHORTs. A 92-scene LONG puts ~92 `.scrim` divs in one document and trips
`composition_heavy_overlay_count_high`, whose field signal is that ~40 overlays can
make the capture layer emit solid black for the first half of a render. Probe the
first finalised chunk of any long blockframe-9 encode before trusting the master.

### `.scene { isolation: isolate; }` is load-bearing (found 2026-08-01)

`.scene` is `position:absolute` with `z-index:auto`, which does **not** create a
stacking context. So `.stack` (z 2) and `.rail .railcol` (z 3) escaped into the
**root** stacking context and outranked the *incoming* section, which paints in
the z-0 band. For the whole `transition_seconds` (0.45s) cross-dissolve, the
**outgoing** scene's headline and rail number painted on top of the incoming
scene — two scenes' words legible at once, at every one of the 91 boundaries.

Found by boundary forensics on frames 550/551/552 of `japanese-money-methods-hi`
(frame 551 shows rail "04" carrying scene 03's words). **Every cut shipped before
2026-08-01 carries this defect** — it is in the shared section of
`blockframe.css`, not in any one architecture. `isolation: isolate` creates the
stacking context without changing paint order inside the scene.

Why nothing caught it for six cuts: `hyperframes check` is static and per-frame,
and the frame check sampled one frame per scene at that scene's last cue — which
lands *between* transitions by construction. A defect that exists only during a
dissolve needs a frame sampled during a dissolve; `fin-render` now requires three
such samples per cut.

| Property | Value |
|---|---|
| Stage | 1920 × 1080, `#root` with `data-composition-id="main"` |
| Scene padding | `110px 150px` |
| Base | `--bg: #0d1017` |
| Photo layer | `.bg`, `inset: -8%` (bleed for the Ken Burns move), `background-size: cover` |
| **The grade** | `filter: grayscale(0.32) brightness(0.62) contrast(1.05)` |
| Grain | `.grain`, opacity `0.05`, `mix-blend-mode: overlay` |
| Track index | scenes `1`, audio `10` |
| Watermark | `#root::after`, avatar bottom-right, `84px`, `right: 64px / bottom: 40px`, opacity `0.5` |

**The grade is load-bearing.** It is the single reason nine unrelated stock photos
read as one film. A per-scene `filter:` override is permitted only for a near-black
texture that the grade crushes flat, and **never more than once per video** — past
that the unity is gone.

### The watermark (creator, 2026-08-01)

The channel avatar rides the bottom-right corner for the **whole** video, every
cut, every architecture. Three decisions worth keeping:

- **It hangs off `#root`, not off a scene.** A mark inside `.scene` dissolves
  with the scene it lives in and has to be repeated ~86 times. As a `::after` on
  the root it is painted once, above every scene, and a build cannot forget it
  on scene 43. The composition's entire share of the work is the `cut-<cut>`
  class on `#root` — which `check build` asserts, because the failure mode is a
  fully green run that ships an unbranded video.
- **Alpha, not `border-radius`.** The avatars are circles on a *white* JPEG
  field; CSS rounding cannot clip the source's own corners on a dark frame. The
  circle is cut into the PNG (`tools/make_watermark.py`, originals in
  `assets/brand/`), so the derivative is a real transparent disc.
- **Bottom-right is also where YouTube paints its own branding watermark.**
  Leave that channel feature switched off, or the corner carries two marks.

`hi` ⇒ `wm-hi.png` (@cashguruguides, green) · `en` ⇒ `wm-en.png`
(@moneymavens101, pink) — [[channels]].

### The scrim (four layers, in order)

```css
.scrim {
  position: absolute; inset: 0; z-index: 1;
  background:
    radial-gradient(ellipse 72% 64% at 50% 52%, var(--tint, transparent), transparent 72%),
    radial-gradient(ellipse 88% 78% at 50% 53%, rgba(13,16,23,0.46), transparent 80%),
    radial-gradient(ellipse 115% 105% at 50% 54%, rgba(13,16,23,0.14), rgba(13,16,23,0.58)),
    linear-gradient(180deg, rgba(13,16,23,0.40), rgba(13,16,23,0.10) 46%, rgba(13,16,23,0.52));
}
```

Layer 1 carries the per-scene `--tint`. Layers 2-4 are fixed: they pull the centre
down so type reads, then vignette the frame.

---

## 2. Colour — roles, never meanings

```css
--bg     #0d1017    --panel  #161b25    --ink   #f5f3ec    --muted #98a2b3
--fund   #22c55e    --warn   #ef4444    --target #f59e0b   --pop   #ff5c39
```

| Token | Role | Not |
|---|---|---|
| `--fund` green | the good outcome, the kept thing, the safe path | "needs" |
| `--warn` red | the loss, the leak, the trap being exposed | "wants" |
| `--target` amber | the thing under examination, the decision point | "wants" |
| `--pop` orange | the call to action, the do-this-now stamp | — |
| `--muted` grey | kickers, feet, subtitles — never a focal element | — |

**Semantics are per-video, derived from the thesis — not a channel rule.** The
shipped needs-vs-wants deliberately inverted the emergency-fund system: there,
wants render amber and red is reserved for the leak alone, because that video's
argument is *"wants aren't the enemy."* Reuse the inversion blindly on a
credit-card video and red should be the interest trap, not a subscription.

**Every storyboard must open with a four-line colour table for that video**, and
the audit stage checks each coloured element against it. The check that matters:
*does any element render in a colour that argues against the script?*

### Per-scene tint (shipped reference)

```
s1 red .12   s2 —(photo-free)  s3 green .10   s4 amber .12   s5 green .10
s6 green .10 s7 —(photo-free)  s8 orange .12  s9 green .13
```
*(Historical reference — needs-vs-wants shipped with photo-free s2/s7. As of
2026-07-28 every scene carries a `.bg`; the tint ladder still applies.)*

Tint tracks the scene's emotional register, at 0.10-0.13 alpha. Above ~0.15 it
stops reading as light and starts reading as a colour wash.

---

## 3. Typography

Self-hosted variable face — no system-font dependency, no network fetch:

```css
@font-face {
  font-family: "FinanceSans";
  src: url(assets/fonts/NotoSansFinance-var.woff2) format("woff2-variations");
  font-weight: 100 900; font-style: normal; font-display: block;
}
--font: "FinanceSans", system-ui, sans-serif;
```

Noto Sans, subset to Latin + punctuation + currency, width axis pinned, **weight
axis live at 100-900**. 32 KB. Carries `₹` U+20B9.

> **Do not substitute Archivo Black**, despite [[design-techtooltester]] naming it.
> Verified with fontTools: Archivo Black has **no U+20B9 (₹)** and no U+2192 (→).
> Using it breaks the rupee sign in the Hindi channel's hero number.

### The ladder — step down it, never interpolate

| Class | px | Use |
|---|---|---|
| `.mega` | 290 | the one enormous number (a rule, a count) |
| `.huge` | 112 | the scene's single focal statement |
| `.counter` | 96 | a running/animated figure |
| `.arrow` | 72 | standalone flow arrow |
| `.head2` | 54 | secondary headline |
| `.billrow.total` | 50 | the summed line |
| `.cta` | 46 | subscribe block |
| `.stamp` | 44 | the rotated verdict |
| `.sub` `.billrow` `.decision` | 40 | supporting statement, bill lines |
| `.chip` `.statstrip` | 32 | enumerated items |
| `.kicker` | 30 | the scene's opening whisper |
| `.collabel` | 28 | column headers |
| `.foot` | 26 | source line, caveat |

Overriding inline is allowed **only to a value already on the ladder** (the shipped
pair drops `.huge` to 88 and 76, `.mega` to 240). Shrinking a focal element below
76 to make it fit is a layout failure, not a type decision — restructure instead.

**Numerals:** `font-variant-numeric: tabular-nums` on `.counter .mega .billrow
.head2 .huge`, so animated figures do not shimmy. Grouping is locale-bound —
`Intl.NumberFormat("en-IN")` for `-hi` (gives `1,24,564`), `"en-US"` for `-en`.
A plain `\B(?=(\d{3})+(?!\d))` regex is **wrong for India** and prints `124,564`.

**Text shadow** on every text class: `0 2px 22px rgba(0,0,0,.7), 0 1px 4px rgba(0,0,0,.55)`.

---

## 4. Components

- **`.chip`** — pill, `--panel` fill, 3px border, `999px` radius. Border colour
  carries the role (`.fund` `.warn` `.target`). Max **3 per row**, **≤22 chars
  each**; rows declared explicitly in the storyboard. `.row` has `flex-wrap: wrap`,
  so four long chips silently wrap 3+1 into a ragged orphan that no checker flags.
- **`.stamp`** — the verdict. Solid role-colour fill, `#0d1017` text,
  `rotate(-4deg)`, `back.out` entry. One per scene at most.
- **`.bill` / `.billrow`** — the itemised money block, 780px wide,
  `justify-content: space-between`, `.total` bordered in `--warn`.
- **`.decision`** — `LABEL → verdict-pill` rows (`.v-cancel` `.v-down` `.v-keep`).
- **`.track2` / `.fill2` / `.ticks`** — 740px progress bar; ticks are a repeating
  gradient at `100%/12` for a twelve-month read.
- **`.statstrip`** — a cited statistic on a translucent `--warn` bed.
- **`.cta`** — `--pop` block, `#0d1017` text, closes the video.
- **`.arrow` / `.arr` / `.tri`** — `→` and `▶` are **drawn in CSS**, not typed.
  Both are absent from the subset; em-based so they scale with the host font-size.

**Audio: one bed + the SFX kit** (`tools/audio/kit.json` — count lives there, not here) (creator rule 2026-07-30, supersedes
"No SFX — voice + motion only", which the audit found was a fork artefact from
the bright TechToolTester system rather than a tested decision, and which never
mentioned music at all).

- Kit + prompts: `tools/audio/kit.json`. Generate once with
  `tools/audio/sfx.py --kit` — cached by name, so it costs ~7 API calls **ever**,
  not per video. Files land in `studio/library/sfx/`, peak-normalised to the
  level named in the kit.
- Seven sounds, each bound to ONE motion helper: `chip`→pop · `reveal`→rise ·
  `tick`→pulse · `stamp`→the verdict slam · `hero`→the big number ·
  `transition`→a scene boundary · `cta`→the closing block. **A sound with no
  helper does not belong in the kit.** Budget ≤10 cues per short cut; a sound is
  punctuation, and if every reveal has one then none of them means anything.
- One music bed per video, ducked ~6 dB under speech (≈18 LU below the voice).
  Deliberately featureless — anything with a melody competes with a spoken number.
- **Mixed in post, never in the composition.** `tools/audio/mix.py` reads the
  cue list at `assets/audio.json` and mixes with ffmpeg's sidechain compressor;
  `tools/loudnorm.py` then takes the result to −14 LUFS. The renderer does not
  guarantee in-page volume automation, and a bed that silently fails to duck
  would bury the voice in a video that passes every check. The composition stays
  voice-only: one `<audio>` row per line.
- ⚠️ ElevenLabs **music** generation needs the `music_generation` permission on
  the API key; the SFX endpoint does not. Until that is enabled, `mix.py` runs
  SFX-only and says so. Free fallback with no channel-count limit: the YouTube
  Audio Library — drop a file at `studio/library/music/<bed-name>.mp3`.
**No logo outro.** Neither finance channel has a brand mark yet
([[channels]] D/E) — the video closes on the `.cta` block. Build the wordmarks
before reinstating the standing logo rule.

---

## 5. Motion

**Implemented in `tools/scaffold/assets/js/motion.js`** — that file is the list.
The table below is the intent; it drifted from what shipped (the newest cut was
missing `fill`, `countUp` and `drift`, and leaned on `exit` and `popEach`, which
appear nowhere here). `countDown`, `dissolve`, `shove` and `sceneTransitions`
are also in the file.

> ⚠️ `breathe(sel, at, dur)` used to run for **2× `dur`**. Fixed 2026-07-29 —
> `dur` is now the real total, quantised to whole out-and-back pairs so the
> element always ends where it began. Shipped cuts were built against the old
> behaviour; do not "correct" their timings.

All helpers live on one paused GSAP timeline registered to `window.__timelines`:

| Helper | Motion | Default |
|---|---|---|
| `rise` | fade + travel up | `y:40`, `0.7s`, `expo.out` |
| `pop` | fade + scale from 0.6 | `0.6s`, `back.out(1.7)` |
| `fade` | opacity only | `0.5s`, `power1.out` |
| `pulse` | scale blip, yoyo | `1.12×`, `0.16s` |
| `fill` | `scaleX` from 0 | `0.8s`, `power2.out` |
| `countUp` | number tween, locale-formatted | `1.2s`, `power1.out` |
| `breathe` | slow yoyo scale, **odd repeat count** so it ends where it began | `1.035×`, `1.5s` cycles |
| `ken` | the background move | `1.0 ↔ 1.16` scale, `∓2.5 xPercent` |
| `drift` | slow one-way scale for photo-free scenes | `1.035×`, `ease:"none"` |

### Rules

0. **Every boundary is a transition** (2026-07-29). The first six videos hard-cut
   between all nine scenes — measured on a real master with `ffmpeg scdet`, the
   boundary frame-delta was 5.85–10.72 against a mid-scene 0.053–0.377, and five
   of eight boundaries tripped a generic cut detector. `dissolve` (0.45s) is the
   default; `shove` is for at most two real turns in the argument.
   The mechanism has **two** parts, both asserted by `pipeline_check check_build`:
   (i) every scene but the last carries
   `data-duration = scene_duration + scene.transition_seconds`, so it stays on
   screen while the next fades in over it (root duration unchanged) — without it
   the dissolve plays against black and every other check still passes; and
   (ii) **adjacent scenes alternate `data-track-index` 1/2**, because
   `hyperframes check` rejects two overlapping clips on one track. Verified
   2026-07-30 on the real `credit-history-en` composition: butt-joined → check
   passes; +0.45s overlap on one track → **8 × `overlapping_clips_same_track`**;
   +0.45s overlap with alternating tracks → **check passes, 22/22 contrast**.
   Track index is a timing lane, not paint order, so z-order is unaffected.
1. **Alternate `ken` direction.** Never two pushes in a row. Shipped order across
   the photo scenes: `in, out, in, out, in, out, in`.
2. **Every scene carries a full-bleed `.bg` photo under the grade — photo-free
   scenes are RETIRED** (creator rule 2026-07-28, supersedes the earlier
   2-per-video rest-beat cap; `format.json photo_free_scene_ratio` is now 0).
   Every scene therefore gets `ken`; `drift` survives only as the motion for
   overlay stacks, not as a substitute for a background. **No scene may hold a
   static frame beyond ~2s.**
3. **Keyword-matched imagery** (creator rule 2026-07-28): when the VO names a
   concrete thing (gym, bill, phone, bank, family), the frame shows that thing —
   either as the scene's `.bg` or as a cut-in timed to the word's cue. The
   storyboard lists per scene: the bg keyword + each cut-in keyword with the VO
   word it lands on. Dense scenes still get the *calmest* background (texture
   reading of the keyword, not a busy literal shot) — density is managed by
   choosing a quieter image, never by dropping the image.
4. **One focal element per scene.** Never `.huge` and `.mega` together.
5. **Reveal spacing ≥0.8s** between consecutive cues, except a declared cascade
   (≤5 items at fixed 0.6-0.7s). Something must be on screen by scene start +0.5s.
6. **≤6 elements visible simultaneously.**

---

## 6. Timing contract

```
scene_duration = 0.4 (VO lead-in) + clip_duration + 1.0 (tail)
scene_start    = previous scene_start + previous scene_duration
audio start    = scene_start + 0.4
```

Verified across both shipped cuts (hi s1: `0.4 + 17.74 + 1.0 = 19.14` ✓;
en s4: `0.4 + 14.65 + 1.0 = 16.05` ✓).

The same numbers appear in **four** places — the `<section>` attributes, the JS
`S` map, the `<audio>` row, and the root `data-duration`. They must be generated
from one source, never hand-edited: updating three of four passes every check and
ships a video whose animations fire against the old timeline.

**Cue placement.** The shipped pair interpolates by character offset
(`0.4 + chars_before/total × clip_duration`). That is a stopgap — it drifts most
on Hindi, where delivery rate swings across a 26s clip. Anchor cues to **word-level
timings** from faster-whisper instead. Split offsets into two classes:

- **anchored** — scales with the clip, lands on its word
- **fixed** — cascades, arrows, stamp slams: constant regardless of clip length

Surplus time from a longer clip goes into **holds, never into a cascade**.

---

## 7. Imagery

Full rules in [[stock-photo-sourcing]]. The load-bearing ones:

- **Object-led, not scene-led.** Photos sit under `grayscale(.32) brightness(.62)`
  with heavy type on top — they are texture, not information. ₹500 notes carry
  "India" more reliably than any photo of a person, and they actually exist in the
  library (India-with-people queries are ~20% usable).
- **The densest scene gets the calmest background.** Reach for a texture first on
  any scene carrying more than ~4 stacked elements.
- **Never a phone-screen photo as a background.** The screen is someone else's
  brand and it is the brightest thing in frame. This has now shipped **three**
  times undetected — most recently `s8` of the Hindi cut, upside down, with the
  carrier string `MTN-SA` legible.
- **Faces fight the typography; hands and objects don't.** Also a licence issue:
  Pixabay bars unflattering use of identifiable people, and a recognisable face
  under a voiceover about wasted money is exactly that.
- **Check what the picture is saying** — a falling chart under a "this grows your
  money" line, demonetised pre-2016 ₹500 notes, dollars answering a ₹ query.
- **Drop a cut-in rather than fake it.** Single-photo scenes read fine.
- **No image may repeat across videos or channels.** Verified failure: one
  `s9.jpg` is byte-identical in three shipped projects across *both* channels,
  because Pixabay's top hit is deterministic and different queries collapse to it.
  Key an asset ledger by md5 and refuse a hash already used anywhere.

---

## 8. Determinism

- GSAP is **vendored** at `assets/js/gsap.min.js`. Never a CDN: if the fetch is
  slow past first paint, `gsap` is undefined, no timeline registers, and the render
  **succeeds** — producing a video with every element static from frame 0, which
  `npm run check` will not catch because it hits the same network.
- Font is self-hosted. No `Date.now()`, no unseeded `Math.random()`, no
  render-time fetches.
- Pin the CLI with a committed lockfile, not `npx --yes`.

## 9. The checker is evidence, not authority

`npm run check` is a gate, but a finding is not automatically a defect. The
rotated `.stamp` construct reports a false contrast failure when it sits on a
bright fill; the storyboard's standing instruction is *"do not fix it by lightening
the text."* An agent told to "fix until clean" will edit a design token and degrade
the signature element on every future video.

Carry a `known_benign` list of `{selector, rule, reason}`. Fail loudly on a **new**
finding; never edit a token to satisfy a checker.

> Note: after moving to a real 900 weight the shipped pair went from one failing
> contrast check to **41/41 passing** — that entry is no longer needed. Faux-bold
> on a 400-weight fallback was part of the original problem.

---

## Related

[[channels]] · [[stock-photo-sourcing]] · [[niches/india-finance-market]] ·
[[us-english-script-style]] · [[../workflows/voiceover-tts]] ·
[[design-techtooltester]] (the *other* system — bright, non-finance)


---

## Records drained from `tools/format.json` (2026-08-09)

Provenance and resolved incidents. `format.json` is the constants file; its own
`_comment` says rationale belongs here, and 47% of it was rationale.

### `_architecture_lock_note`

When set, this WINS over the rotation above and every run uses it — no per-run override, nothing to remember. Creator decision 2026-07-30: the creator reviewed all thirteen candidate styles side by side (nine of them registry-backed) and chose to keep blockframe-9, so the rotation would otherwise hand the next run ledger-rail and silently contradict a decision that was actually made. A lock is the honest representation of 'we picked one'. Delete this key to resume rotating; `doctor` refuses a lock that names an architecture that does not exist, so a typo cannot degrade to silent rotation. The sameness risk this rotation existed to manage is now carried by the non-layout levers instead — transitions (live), the SFX kit (present), and the music bed (see tools/audio/kit.json).

### `_architectures_note`

The pipeline ROTATES these — `pipeline_check.py architecture` returns the one least recently used, and the orchestrator writes it into run.json before fin-script runs. Six consecutive blockframe-9 cuts shipped because the only control was a warning written into notes that no code read; the fix is that the default now varies by construction rather than being flagged after the fact. Add an entry here to put a new layout into the rotation.

### `_styles_rejected_note`

Reviewed and rejected 2026-07-30 — do not re-propose without new reason. 'news-ticker': we are not making news videos, irrelevant to finance education. 'code-snippet' and 'code-typing': we are not making coding videos. The other registry directions were rejected for carrying no photograph; the ones that can be re-cut to carry one may return. 'x-post'/'reddit-post' was ACCEPTED as an occasional component (not an architecture) — usable only when a real, topical social post exists; see _components.

### `_image_per_scene_note`

HARD creator rule, restated 2026-07-30 while rejecting most of the thirteen candidate styles: 'images are compulsury'. Every architecture MUST declare image_per_scene: true and actually carry a photograph in EVERY frame — a style that renders type on flat colour is out of scope no matter how good it looks. `doctor` refuses an architecture without the flag, so a new style cannot be added that quietly drops the image. Pairs with layout.photo_free_scene_ratio = 0.

### `_known_benign_note`

Empty is the correct state. The one entry ever added — invalid_parent_traversal_in_asset_path — was WRONG, and cost four cuts their browser checks: it reasoned the ../ urls were a static-analysis false positive because the render looked right, which was true. What it missed is that a lint ERROR makes `hyperframes check` SKIP the layout and contrast passes entirely, so those four cuts shipped with WCAG and layout never actually run. Fixed at the root 2026-08-01 by moving blockframe.css to assets/blockframe.css so the urls need no ../ at all. Lesson: 'the output looks fine' does not establish that a finding is benign — check what the finding SUPPRESSES.

### `_stock_video_note`

SUPPORTED — corrected 2026-07-30 (an earlier version of this note said the opposite; it was wrong). HyperFrames does not play video in real time: it pre-extracts the clip to frames with ffmpeg and injects the right one as an <img> before each capture (studio/packages/engine/src/services/videoFrameInjector.ts), so rendering stays deterministic. We have already shipped it — compositions/video-02-claude-edits-video/index.html has eight root <video> clips. The grade survives: `filter` and `transform` are in MEDIA_VISUAL_STYLE_PROPERTIES and are copied onto the injected frame.
