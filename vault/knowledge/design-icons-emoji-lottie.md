---
summary: How emoji, SVG and Lottie actually behave inside a HyperFrames render — all four paths probed on a real 20s 1080p encode (hyperframes 0.7.66). Includes the two traps that render a silent blank.
updated: 2026-07-31
verified_by: /tmp probe `fxtest` — `hyperframes check` + `snapshot` + full `render`, frames read back with ffmpeg
---

# Icons, emoji and Lottie in a cut

All four paths were probed end-to-end on the blockframe scaffold and survive a
real encode. Ranked by how little can go wrong.

## 1. Inline `<svg>` + GSAP — the default

Fewest moving parts, no new dependency, full motion control, tints from the
palette (`stroke: var(--fund)`). Stroke-draw with `strokeDasharray` /
`strokeDashoffset` passed `hyperframes check` clean (Motion: 0 errors) — those
are non-spatial property tweens, not layout tweens, so the transform-alias rule
in [[design-finance-blockframe]] is not violated.

```html
<svg class="v-ico" viewBox="0 0 100 100"><path id="s2line" d="M8 82 L34 54 L56 66 L92 20"/></svg>
```
```js
tl.fromTo("#s2line", { strokeDasharray: 160, strokeDashoffset: 160 },
          { strokeDashoffset: 0, duration: 0.9, ease: "power2.inOut" }, S.s2 + 0.8);
```

A one-off icon lives in the cut's own inline `<style>` as `.v-ico`. An icon used
by more than one video belongs in `tools/scaffold/assets/` — not copied per cut.

## 2. External `.svg` as `<img>` — for a logo or a fixed mark

Renders correctly, scales cleanly, `pop()`/`rise()` work on it like any element.
Trade-off: it is opaque to CSS — **no recolouring via `currentColor` or a
palette var**, the fill is baked into the file. Use it when the artwork's own
colours are the point (a brand logo); use path 1 when it must take the cut's
accent colour.

## 3. Emoji — works, but it is a font, not an asset

Colour emoji render correctly in the headless renderer (💰 📈 🏦 ⚠️ 🇮🇳 all
verified in the encoded mp4, flag sequence included), inline in a line of type
or standalone. No `@font-face` needed — the glyph falls out of the
`system-ui, sans-serif` tail of `--font` onto the OS font.

Two cautions, both real:

- **Machine-dependent.** It works because this box has
  `/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf`. A render on a machine
  without an emoji font emits tofu boxes and every check still passes. If emoji
  ever become load-bearing, vendor an emoji `.woff2` into
  `tools/scaffold/assets/fonts/` and name it in `--font` — same reasoning that
  put FinanceSans there ("no render-time network fetch, ever").
- **They ignore the grade.** `.bg` carries `grayscale(.32) brightness(.62)`;
  emoji sit in `.stack`, ungraded, so they arrive as the most saturated object
  on screen and read as a WhatsApp sticker on top of a film. That is a design
  decision for [[design-finance-blockframe]], not a technical limit — a
  monochrome SVG icon in a palette colour is the house style. If a cut wants
  emoji, tint them (`filter: saturate(.7) brightness(.9)`) or accept the break
  deliberately.

## 4. Lottie — works, with two traps that render a silent blank

Vendor `lottie-web`'s `lottie.min.js` (306 KB) into `assets/js/`. The pinned
hyperframes 0.7.66 has a real `lottie` runtime adapter, so no wrapper is needed.

**Trap A — the adapter seeks ABSOLUTE composition time.** It calls
`goToAndStop(t * 1000)` where `t` is the timestamp in the *video*, not in the
scene. A 2.7 s asset placed in a scene starting at 10 s is seeked to 10 000 ms,
lands past its last frame, and draws **nothing**. Verified: the identical asset
rendered fine in scene 1 (t = 0.9/1.8/2.6 s) and blank at t = 11.5 s.
So `window.__hfLottie` registration is only usable for a Lottie in the first few
seconds of the cut. For anything later, drive it from the GSAP timeline:

```js
var f = { v: 0 };                                   // seek-safe: frame derived
tl.to(f, { v: 163, duration: 2.733, ease: "none",   // from the tween's progress
  onUpdate: function () { anim.goToAndStop(f.v, true); } }, S.s4 + 0.6);
```

**Trap B — `discover()` sweeps in animations you never registered.** The adapter
calls `lottie.getRegisteredAnimations()` and merges *every* animation into
`window.__hfLottie`, so a GSAP-driven one gets overwritten by trap A anyway and
still draws blank. Pin the registry to only the animations you want
adapter-seeked, right after loading:

```js
lottie.getRegisteredAnimations = function () { return [animEarly]; };
window.__hfLottie = [animEarly];
```

**Also:** load with `animationData` (JSON inlined into a small `.js` file),
never `path:` — an async XHR that resolves after the runtime inspects the page
is a blank scene that passes every check. `autoplay: false`, `loop: false`.

## The library — reuse before you fetch (creator decision 2026-07-31)

`assets/lottie/` and `assets/icons/` are **git-tracked and outside `studio/`**,
because `studio/` is gitignored and a cut is deleted from it the moment the
video ships. Every asset a video has to find gets saved back, so the next video
finds it locally: the collection compounds, the fetching doesn't. Operating
detail lives in `assets/README.md`; the reasoning is here.

Three choices worth keeping:

1. **Stored pristine, never pre-tinted.** The accent is the *scene's* role
   colour, not a property of the artwork — the same illustration is `--fund`
   green in one video and `--target` amber in the next. `tint.py` colours a copy
   into the cut and leaves the original alone.
2. **A still `.png` preview, not the animated `.gif`.** The next video has to
   *look* at the asset to judge it, and a name never suffices for an
   illustration — but the gif previews ran 891 KB each, more than the artwork
   they preview, and they go into git forever. A 320 px mid-frame is 27 KB.
3. **`used_in` is written by the tool, not by an agent.** "Have we leaned on
   this one already?" is the question that stops a library becoming sameness,
   and an agent that has to remember to log it, won't. `tint.py` records the cut
   and warns from the second use on.

**Why this differs from the audio kit.** `tools/audio/sfx.py` keeps the
*prompts* in git and the generated mp3s under the gitignored `studio/library/`,
because a prompt regenerates its audio exactly. A Lottie has no prompt: it is a
third-party file whose URL can rotate and whose author can delete it, so the
artwork itself is the reproducing text and belongs in git. Same instinct, opposite
answer — don't "unify" them.

The icons library needs no index: `ls assets/icons/` with descriptive filenames
IS the catalogue, and a JSON beside it would be a second home for the same fact.
The Lottie index earns its keep because it carries what the filename can't —
source, author, licence, duration, and `used_in`.

## Sourcing a stock Lottie (the flat-illustration kind)

The premium marketplace the creator was browsing
(`app.lottiefiles.com/search?type=premium-assets`) needs a paid plan. The **free**
catalogue is the same house style and is cleared for this use: **Lottie Simple
License** — commercial use ok, modification ok, **no attribution required**; the
only bar is redistributing or reselling the raw animation file, which a rendered
video does not do.

`lottiefiles.com` HTML is Cloudflare-gated, but the search endpoint the site
itself calls is open and returns free animations only:

```bash
tools/lottie/search.py "finance investment" "money savings growth" > cands.json
```

Each hit carries `jsonUrl` **and** `gifUrl` — download the GIFs first, montage
them into a contact sheet, pick with your eyes, then fetch only the two JSONs
you want. 36 candidates cost one search + 32 small GIFs.

Prefer assets whose `assets[]` carry no `"p"` (embedded bitmap) — pure vector
scales to 1080p and can be re-tinted; a Lottie with a baked PNG inside cannot.
Both picks were 340–470 KB of pure vector, 4–5 s, 30 fps.

## Re-tinting a stock illustration into the palette

The real problem with these assets is not technical, it is that they arrive in
someone else's colours (purple/teal/orange flat-vector) and land on top of a
graded film as clip-art. `tools/lottie/tint.py` walks the JSON and maps every
solid colour and gradient stop onto one `panel → accent → ink` ramp by
luminance, so the artwork keeps its own light/dark structure but wears the cut's
colour:

```bash
tools/lottie/tint.py stock.json tinted.json "#22c55e"    # --fund
tools/lottie/tint.py stock.json tinted.json "#f59e0b"    # --target
```

Rendered side by side (probe `fxtest2`, 2026-07-31): as-downloaded reads as a
stock illustration dropped on the film; re-tinted reads as part of it. Use the
accent that carries the scene's role, per [[design-finance-blockframe]].

**Cost.** Two heavy illustration Lotties running at once took a 20 s 1080p
render from 1 m 27 s to 3 m 56 s (~2.7×) — `lottie-web`'s SVG renderer redraws
the whole illustration every frame. At MEDIUM tier that is real time. Use them
on a handful of scenes, not as the every-scene visual.

## When to reach for which

Icon, arrow, chart mark, rupee sign, anything that should take a palette
colour → **inline SVG**. Brand logo → **`.svg` as `<img>`**. Something
genuinely pre-animated that would take an hour to rebuild in GSAP (a confetti
burst, a coin flip, an AE export someone handed you) → **Lottie**. Emoji →
only as a deliberate tonal break, never as the icon system.

## Where it lives now (wired 2026-07-31, creator go-ahead)

No new agent. Vector art has no artifact of its own — it is a storyboard
decision, an asset fetch and three lines of composition — so a twelfth stage
would have added a handoff, a run.json entry and a gate for nothing. It went
into the three stages that already own those jobs:

| Piece | Home |
|---|---|
| Constants, licence, caps | `tools/format.json` → `vector_art` |
| `.icon` · `.lottie` · `.aside` components | `tools/scaffold/assets/blockframe.css` |
| `draw` · `loadLottie` · `playLottie` helpers | `tools/scaffold/assets/js/motion.js` |
| Vendored player | `tools/scaffold/assets/js/lottie.min.js` (306 KB, lottie-web 5.12.2) |
| The shared library (git, outside `studio/`) | `assets/lottie/` · `assets/icons/` · `assets/README.md` |
| Search library-first, contact sheets, save-back | `tools/lottie/search.py "<phrase>" --sheet` · `--save "<cell>=<name>" --tags …` |
| Re-tint a library asset into one cut | `tools/lottie/tint.py <name> studio/…/assets/lottie/<n>.js "#<accent>"` |
| Decides *whether* a scene gets art | `fin-storyboard` §4d |
| Picks and tints the asset | `fin-assets` "Lottie slots" |
| Places it | `fin-build` step 1 "Vector art" |
| The three traps, made failures | `pipeline_check check_build` (+ selftest) |
| Archived with the cut | `archive_cut.py` KEEP `assets/lottie/*.js` |

`loadLottie()` pins the registry itself, so a build that uses the helper cannot
hit trap A or B — the check exists for a build that goes around it.
`.icon` deliberately declares **no `color`**: it would out-order `.fundc` /
`.warnc` / `.targetc` (same specificity, later in the file) and silently paint
every icon white. Verified on the scaffold, not just the probe: `fxtest3`
renders `.icon.fundc` green and a tinted `.lottie` in `.aside`.

## The two assets used in the demo (Lottie Simple License, free tier)

| Asset | Author | jsonUrl |
|---|---|---|
| "investment" — person + finance app + coin stack, 4.0 s | `/mswq6u9ykp` | `assets-v2.lottiefiles.com/a/5f1892aa-117c-11ee-b2de-672f0e0499a7/GybiFaTSLk.json` |
| "growth chart" — person on coin stacks + magnifier, 5.0 s | `/shturma` | `assets-v2.lottiefiles.com/a/6e55457e-116d-11ee-a091-ef1bd4874750/haqa8jbgYV.json` |

No attribution is required by the licence; recording the author here is so a
future run can find more from the same hand — style consistency across a video
matters more than the individual asset.
