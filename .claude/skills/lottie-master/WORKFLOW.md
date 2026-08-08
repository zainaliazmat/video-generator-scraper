# Making Lotties locally — a workflow for Claude Code

This is the exact process used to build `phone-on-counter-night.json`: a 640×420,
6-second, 22 KB vector scene with animated light, built entirely in Python with no
design tool. It generalizes to any Lottie work.

The single most important idea: **you can render frames to PNG and look at them.**
Lottie work is visual, and writing keyframes blind is guessing. Build → rasterize →
open the image → fix. Three or four passes gets you something good.

---

## 1. Setup

### Install the skill

The generator, optimizer, references, and a worked scene example ship in
`lottie-master-skill.zip`. Unzip it to wherever skills live:

```bash
# personal, available in every project
unzip lottie-master-skill.zip -d ~/.claude/skills/

# or project-local, checked into the repo
unzip lottie-master-skill.zip -d .claude/skills/
```

You'll get:

```
lottie-master/
├── SKILL.md                        # decision tree — read this first
├── scripts/
│   ├── lottie_gen.py               # generator + builder API (stdlib only)
│   ├── lottie_optimize.py          # shrink and clean
│   ├── fetch_lottie.py             # download / inspect / validate
│   └── make_dotlottie.mjs          # bundle to .lottie (needs npm i @dotlottie/dotlottie-js)
├── references/                     # 6 deep dives, read on demand
│   ├── creating-animations.md      # ← the four build routes
│   ├── json-format.md              # ← decoder ring for the raw JSON
│   ├── integration.md              # ← players for every framework
│   ├── optimization.md
│   ├── dotlottie-and-bundling.md
│   └── inspiration-and-sources.md
└── assets/
    ├── templates/                  # 9 ready presets, all <3 KB
    └── example-scene.py            # the full night-kitchen scene, commented
```

### Install the preview toolchain

This is what makes the loop work. `python-lottie` parses Lottie JSON and rasterizes
it through cairo:

```bash
pip install lottie cairosvg
python3 -c "import lottie, cairosvg; print('ok')"
```

If cairo won't build on the machine (uncommon on macOS/Linux, painful on some Windows
setups), fall back to the browser harness in §7 — but try hard to get this working
first. Rendering to PNG is worth more than any other tool in this workflow.

---

## 2. Pick the route before writing code

From `SKILL.md`, in order of effort:

| Want | Do this |
|---|---|
| Loader, spinner, checkmark, progress bar, any standard UI motion | `python scripts/lottie_gen.py <preset> --color "#hex" -o out.json` — one command, done |
| A custom scene or illustration | Builder API in `lottie_gen.py` (this document) |
| Precomps, masks, SVG import, GIF export | `python-lottie` directly — Route B in `creating-animations.md` |
| Recolor or retime an existing file | Edit the JSON with `json-format.md` open |
| Hand-crafted designer motion | Lottie Creator or After Effects + Bodymovin — you can't drive a GUI, so recommend it |

Don't hand-write Lottie JSON from scratch. Generate, then edit.

---

## 3. The build–look–fix loop

Write two files and iterate between them.

**`scene.py`** — the build:

```python
import sys
sys.path.insert(0, "/path/to/lottie-master/scripts")
from lottie_gen import (Lottie, ellipse, rect, fill, stroke, group,
                        transform, animated, static, hex)

a = Lottie(width=640, height=420, fps=30, duration_frames=180, name="scene")
# ... layers ...
a.save("out.json", minify=False)     # keep it readable while iterating
```

**`preview.py`** — the look:

```python
from lottie.parsers.tgs import parse_tgs
from lottie.exporters.cairo import export_png

an = parse_tgs("out.json")
for f in [0, 30, 55, 100, 114, 160]:      # pick your key beats
    export_png(an, f"frame_{f:03d}.png", frame=f, dpi=96)
```

Then:

```bash
python3 scene.py && python3 preview.py
```

…and **open the PNGs with the Read tool.** Actually look. Every real problem in the
night-kitchen scene was invisible in the JSON and obvious in the image within two
seconds: the screen was black, the glow looked like pond ripples, the mug handle was
painted over the mug.

Pick preview frames at the beats that matter — rest state, peak, the transitions
between them, and the last frame if the animation loops.

For motion rather than composition, export a GIF:

```python
from lottie.exporters.gif import export_gif
export_gif(an, "preview.gif", skip_frames=2)
```

---

## 4. Builder API, condensed

Everything below is in `lottie_gen.py`. Full details in
`references/creating-animations.md`.

**Shapes** — `ellipse(size, position)`, `rect(size, position, roundness)`,
`star(points, outer, inner, polygon=)`, `path(vertices, in_tangents, out_tangents, closed)`

**Paint** — `fill(color, opacity)`, `stroke(color, width, opacity, cap, join)`,
`gradient_fill(stops, start, end, radial=)`

**Modifiers** — `trim(start, end, offset)` for draw-on strokes, `repeater(copies, …)`
for radial or grid copies, `group(shapes, tr=)` to bundle and move together

**Transform** — `transform(anchor, position, scale, rotation, opacity)`. Any argument
takes a plain value *or* an `animated()` dict.

**Keyframes**:

```python
animated([(0, 0, "easeOut"), (27, 100), (66, 94, "easeInOut"), (180, 0)])
```

`(frame, value, easing)`, where the easing governs the segment *leaving* that
keyframe. Values are numbers or lists. Easings: `linear, ease, easeIn, easeOut,
easeInOut, easeInOutSine, easeOutCubic, easeInCubic, easeOutBack, easeOutElastic`,
plus `"hold"` for a stepped change.

**Layers** — `a.shape_layer(shapes, tr=, name=, in_frame=, out_frame=)`. Last layer
added renders on top; `to_dict()` handles the reversal for you.

---

## 5. The five things that will bite you

These cost real debugging time. Internalize them.

### 5.1 Within a shape list, the FIRST item paints on top

This is inverted from CSS and from most drawing APIs, and it is the single biggest
time-waster. An opaque background rect at index 0 hides everything after it.

```python
# WRONG — the black body covers the screen, the banner, everything
phone = [body, screen, banner, edge_glow]

# RIGHT — list from front to back
phone = [edge_glow, banner, screen, body]
# or write it naturally and reverse:
phone = list(reversed([body, screen, banner, edge_glow]))
```

The failure looks like a bug in something else entirely. In this build the symptom
was "animated opacity on a group transform doesn't render" — it rendered fine, it was
just underneath an opaque rectangle. Suspect paint order before you suspect the
renderer.

Note the two orderings that differ:
- **Between** groups/shapes in a list → first is on top
- **Inside** a group → geometry first, then its `fill`/`stroke` (painter's order)

### 5.2 Soft glows need a gradient with an alpha ramp, not stacked circles

Stacking translucent ellipses to fake falloff produces visible concentric banding —
it reads as ripples, not light. Use a radial gradient whose alpha ramps to zero. The
Lottie gradient array is colors first, then alpha stops:

```python
def radial(color, radius, stops, opacity=100):
    """stops: [(offset_0_to_1, alpha_0_to_1), ...]"""
    r, g, b = hex(color)
    flat = []
    for off, _ in stops:
        flat += [off, r, g, b]          # colour stops: off, r, g, b
    for off, alpha in stops:
        flat += [off, alpha]            # then alpha stops: off, alpha
    return {"ty": "gf", "nm": "glow", "t": 2, "r": 1,     # t=2 radial, t=1 linear
            "o": opacity if isinstance(opacity, dict) else static(opacity),
            "s": static([0, 0]),                          # centre, shape-local
            "e": static([radius, 0]),                     # a point at the outer edge
            "g": {"p": len(stops), "k": static(flat)}}     # p = COLOUR stop count only
```

Used like:

```python
group([ellipse(size=(680, 750)),
       radial("#4B79D8", 360, [(0, 0.62), (0.3, 0.32), (0.66, 0.09), (1, 0)])])
```

`p` counts colour stops only; the alpha pairs follow them in the same flat array.
`lottie-web` and the dotLottie players both honour this, and python-lottie renders
it, so it previews accurately.

### 5.3 One curve should drive every lit element

A scene where the screen, the spill on the counter, the rim light and the reflection
each have their own hand-tuned keyframes will drift out of sync and look wrong in a
way that's hard to name. Define the light *once* and scale it per element:

```python
CURVE = [(0, 0), (24, 0, "easeOut"), (27, 100), (66, 94, "easeInOut"),
         (96, 34), (108, 34, "easeOut"), (111, 92), (122, 86, "easeInOut"),
         (150, 26), (170, 0), (180, 0)]

def light(curve, peak):
    """Same shape, different ceiling."""
    return animated([(kf[0], round(kf[1] * peak / 100, 2), *kf[2:]) for kf in curve])

fill("#1C3055", opacity=light(CURVE, 100))    # screen
stroke("#7CA6FF", width=2.4, opacity=light(CURVE, 36))   # light off the phone's edge
stroke("#7CA6FF", width=2, opacity=light(CURVE, 30))     # mug rim across the counter
```

Retiming the whole scene then means editing one list.

### 5.4 Animate opacity where it actually works

Animated `fill(opacity=…)`, `stroke(opacity=…)`, and **layer** transform opacity are
all reliable. If you need a whole group to fade, either put it on its own layer or
animate the opacity of each paint inside it. Cheap to do, avoids renderer-specific
surprises.

### 5.5 Loop by making the last frame equal the first

Set `duration_frames` to the loop length and give every animated property an explicit
keyframe at frame 0 and at the final frame with identical values. A loop that snaps
is almost always a property that was never keyed back to its starting value.

---

## 6. Composition notes that made this scene work

Craft, not API. Worth copying.

- **Break the symmetry.** The phone sits at −14° and off-centre. A rectangle centred
  and square to the frame reads as a mockup; the same rectangle rotated reads as an
  object someone dropped.
- **Sub-pixel motion sells physical events.** The buzz is ~1.5px of jitter over six
  keyframes. Without it the screen merely turns on. With it, the phone vibrates
  against stone.
- **Give the light something to hit.** The mug rim, the counter, the phone's own
  edges all brighten on the same curve. Light with nothing to illuminate looks like a
  glow filter.
- **Imperfections carry realism.** A dried coffee ring at 10% opacity, four crumbs,
  faint grain in the stone. Individually invisible; collectively the difference
  between a scene and a diagram.
- **One warm source against a cold one.** A sliver of hall light at the top edge makes
  the blue read as genuinely cold.
- **Structure the beats, don't just fade in and out.** Buzz → bloom → hold → dim →
  second buzz → fade. The dim between buzzes is what implies a second message rather
  than one long one.

---

## 7. Preview in a browser

Once the composition is right, check it in the actual runtime — `lottie-web` is what
will play it in production, and cairo is only an approximation.

```html
<div id="stage" style="width:640px;height:420px"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.12.2/lottie.min.js"></script>
<script>
  fetch("out.json").then(r => r.json()).then(data => {
    const anim = lottie.loadAnimation({
      container: document.getElementById("stage"),
      renderer: "svg", loop: true, autoplay: true, animationData: data
    });
    anim.addEventListener("enterFrame", () =>
      console.log(Math.round(anim.currentFrame)));
  });
</script>
```

Serve it (`python3 -m http.server`) rather than opening the file directly, or `fetch`
will trip CORS. Inline the JSON into the HTML if you want a single portable file.

A scrubber that maps clicks to `anim.goToAndStop(frame, true)` is worth the ten lines
— stepping frame by frame is how you catch a keyframe that lands two frames late.

---

## 8. Finish

```bash
# shrink: rounds precision, strips names and metadata, minifies
python scripts/lottie_optimize.py out.json -o final.json

# validate and report
python scripts/fetch_lottie.py final.json --info
```

The night-kitchen scene went 147 KB → 22 KB (85% smaller) at precision 3, with no
visible difference. Always re-render a frame after optimizing.

Bundle only if you need multiple animations, themes, or state machines in one file —
modern players load plain `.json` happily:

```bash
npm i @dotlottie/dotlottie-js
node scripts/make_dotlottie.mjs --out bundle.lottie a.json b.json --loop --autoplay
```

Then embed per `references/integration.md`. Short version: use the
`@lottiefiles/dotlottie-*` family for new work (`DotLottieReact`, `DotLottieVue`,
`<dotlottie-wc>`), `lottie-web` when you need the widest legacy footprint, and import
client-side only in Next.js — the player touches `window`.

---

## 9. Checklist

- [ ] Read `SKILL.md`; confirm a preset doesn't already solve it
- [ ] `pip install lottie cairosvg` so you can see your work
- [ ] Build with `minify=False` while iterating
- [ ] Render key frames to PNG **and look at them** after every meaningful change
- [ ] Shape lists ordered front-to-back
- [ ] Glows are gradients with alpha ramps
- [ ] One light curve, scaled per element
- [ ] Frame 0 and the final frame identical
- [ ] Verify in `lottie-web`, not just cairo
- [ ] Optimize, validate, re-render one frame to confirm nothing broke
