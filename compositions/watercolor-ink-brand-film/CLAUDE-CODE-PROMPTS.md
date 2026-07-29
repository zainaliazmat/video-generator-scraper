# CLAUDE CODE PROMPTS — Watercolor-Ink Film in Hyperframes

### Copy-paste these into Claude Code **in order**. Each has a GOAL and a "DONE WHEN" check.

> **Golden rules before you start**
>
> 1. Run prompts **in sequence**. Don't skip to scaling (Prompt 5) before the template (Prompt 1) is approved.
> 2. After each prompt, **look at the output** (still or clip) before moving on. The whole Hyperframes + Claude Code model is "render → watch → refine."
> 3. If Claude Code drifts from the spec, paste the relevant **TECH SPEC** block again and say "follow this exactly."
> 4. Keep `assets/` populated as you go — Claude Code references real file paths.

---

## PROMPT 0 — Environment & project scaffold

```
You are helping me build a cinematic watercolor-ink slideshow VIDEO using HeyGen's Hyperframes (HTML → MP4) framework. We'll work iteratively: build one perfect scene template, then scale.

First, set up the project:
1. Confirm Node.js is available (Hyperframes needs it). Install the Hyperframes CLI and its agent skills per the official repo (github.com/heygen-com/hyperframes). Install the /hyperframes skills so you can use the production loop (plan → write HTML → wire seekable GSAP → lint → preview → render).
2. Create a project folder "soul-of-coffee" with this structure:
   soul-of-coffee/
     index.html
     assets/textures/  assets/mattes/  assets/fonts/  assets/images/  assets/audio/  assets/brand/
3. Create a MINIMAL valid Hyperframes composition in index.html: a single 1920x1080, 30fps scene, 3 seconds, dark warm background (#2b2622), with the text "Hyperframes OK" centered, fading in via a PAUSED, seekable GSAP timeline registered to window.__timelines.
4. Run `npx hyperframes lint` and fix any errors. Then run `npx hyperframes preview` and tell me the local URL. Then render a still frame to confirm capture works.

Constraints that apply to EVERYTHING we build (remember these):
- All motion lives on the PAUSED master GSAP timeline that Hyperframes scrubs. NO CSS @keyframes animations, NO requestAnimationFrame loops, NO real-time JS timers. Everything must be deterministic and seekable.
- Target spec: 1920x1080, 30fps.
- Self-hosted fonts only (we'll add .woff2 files to assets/fonts/), never remote font CDNs, so the headless render has them.

Report: Node version, that lint passes, the preview URL, and confirm the still rendered.
```

**DONE WHEN:** lint passes, preview URL works, a still renders showing "Hyperframes OK". You now have a valid skeleton.

---

## PROMPT 1 — THE STYLE SYSTEM (build ONE perfect scene) ⭐ most important step

> This is where the look is won or lost. Spend your time here. Paste the whole thing.

```
Now build the HERO SCENE — one reusable watercolor-ink scene template that all other scenes will copy. Use placeholder assets where I haven't supplied files yet (solid color blocks for missing images), but wire the FULL technique so swapping in real assets "just works."

SCENE CONTENT (scene 1):
- Image: assets/images/01-highlands.jpg (if missing, use a warm green gradient placeholder)
- Title (script font): "Where It Begins"
- Subtitle (uppercase serif): "ETHIOPIAN HIGHLANDS"
- Supporting line (serif): "1,500 metres above the sea"
- Duration: 9 seconds.

DESIGN TOKENS (put on :root):
--paper:#efe7d6; --ink:#2b2622; --ink-soft:#5a5048; --accent:#8c5a3c; --accent-dim:#c9a87f; --bleed-warm:#b5762e; --bleed-cool:#4a6a78;
--font-script:"Pinyon Script",cursive; --font-label:"Marcellus SC",serif; --font-body:"Spectral",serif;
(Add @font-face for the three .woff2 files in assets/fonts/. If files are missing, fall back gracefully but keep the @font-face declarations.)

LAYER STACK (back → front), all inside the .scene.clip → .scene-content structure Hyperframes expects:
1. .paper-bg — full-frame assets/textures/paper.jpg covering the scene (fallback: --paper color). Always visible.
2. .photo-wrap — holds the image, this is what "paints in":
   a. img.photo-base — the image, desaturated/aged: filter: grayscale(0.55) sepia(0.25) contrast(1.05) brightness(0.96).
   b. img.photo-color — the SAME image in full color, stacked exactly on top of photo-base, with mix-blend-mode: multiply and reduced opacity (~0.7) so color "bleeds" selectively through.
   c. .watercolor-tex — assets/textures/watercolor-1.png stretched over the photo, mix-blend-mode: multiply, opacity ~0.5, tinted toward --bleed-warm.
   → THE PAINT-IN: apply a CSS mask to .photo-wrap using an ink shape:
        -webkit-mask-image / mask-image: url(assets/textures/ink-splatter-1.png);
        mask-repeat:no-repeat; mask-position:center; mask-size: 10%;  /* starts tiny */
     GSAP animates mask-size from ~10% to ~150% over --reveal-dur (1.8s) with ease "power2.out" → the ink "spreads open" to reveal the photo. (Animate via a proxy object + onUpdate setting the CSS var, since GSAP can't tween mask-size directly.)
   → WATERY EDGES: define an SVG filter and apply it to .photo-wrap:
        <filter id="watercolor-edge" x="-10%" y="-10%" width="120%" height="120%">
          <feTurbulence type="fractalNoise" baseFrequency="0.012 0.016" numOctaves="3" seed="7" result="noise"/>
          <feDisplacementMap in="SourceGraphic" in2="noise" scale="20" xChannelSelector="R" yChannelSelector="G"/>
        </filter>
     This warps the mask edge into an irregular, bleeding watercolor border. Tune `scale` 12–28 to taste.
3. .text-block — lower-left third, 8% safe margin:
   - h1.title (--font-script, ~110px, --ink)
   - p.subtitle (--font-label, uppercase, letter-spacing .18em, ~30px, --ink-soft)
   - p.line (--font-body, italic, ~22px, --ink-soft)
4. .latin-deco — a few faint decorative serif text fragments floating in the negative space (opacity ~0.12). Optional flavor like the reference.
5. .grain — full-frame assets/textures/grain.png, mix-blend-mode: overlay, opacity ~0.5. Always visible.
6. .vignette — radial gradient, transparent center → ~rgba(20,15,10,0.45) edges. (Or assets/textures/vignette.png.)

ANIMATION (one paused GSAP timeline for the scene, seekable):
- t=0: paper visible; photo-wrap mask-size 10% (hidden); text opacity 0, y+24.
- t=0 → 1.8s: mask-size 10% → 150% (power2.out) — the paint-in.
- t=0 → 9s (whole scene): Ken Burns — photo scale 1.0 → 1.08, slight translate, ease "none".
- t=0.9s → 2.4s: title fades up (opacity 0→1, y 24→0, power3.out).
- t=1.3s → 2.6s: subtitle fades up (stagger after title).
- t=1.6s → 2.8s: line fades up.
- t=7.6s → 9s: gentle fade of text (opacity →0) to prep the transition.

Then:
- `npx hyperframes lint` → fix all errors.
- `npx hyperframes preview` → give me the URL.
- Render a STILL at ~t=3s (after paint-in completes) AND render the full 9s to a clip "scene1.mp4".
- Show me both. Describe what knobs to turn if I want more/less ink spread, more/less color bleed, or a warmer grade.

REMINDER: deterministic only — drive EVERYTHING from the paused timeline. No CSS @keyframes, no rAF, no timers.
```

**DONE WHEN:** the still shows a paper-grounded, watercolor-treated photo that revealed through a spreading ink mask with watery edges, script title + uppercase subtitle, grain + vignette over all. The 9s clip plays the paint-in + Ken Burns + text rise. **Get this looking right before anything else.** Iterate here with small follow-ups ("more ink spread," "stronger cherry-red bleed," "warmer grade," "slower text rise").

---

## PROMPT 2 — Intro + Outro bookends

```
Using the EXACT same style system as scene 1 (paper, ink-mask reveal, watercolor edge, grain, vignette, fonts, tokens), build two special scenes:

INTRO (11s) — assets/images/00-hills-dawn.jpg:
- Slow bloom reveal (mask-size 8% → 160% over 2.6s, ease power1.out).
- Title "The Soul of Coffee" (script, large, centered for the intro), then subtitle "A FILM ABOUT ORIGIN, CRAFT & RITUAL".
- Beneath the title, the brand logo (assets/brand/logo.svg) "inks in" — reveal it with its own small ink-mask wipe at t≈3s. If logo missing, leave a placeholder box wired for swap.
- Hold, then fade text/logo slightly at t≈9.5s to prep transition.

OUTRO (22s) — assets/images/23-cup-on-wood.jpg:
- Bloom reveal, very slow Ken Burns push-in 1.0→1.05.
- Title "The Soul of Coffee", logo inks in, subtitle "[BRAND NAME]", supporting line "[website] · [tagline]".
- Final 3s: everything dissolves to just the paper texture (fade photo + text to the --paper background).

Add both to the composition timeline so the running order is: INTRO → scene1 → … → OUTRO (scenes 2+ come later).
Lint, preview, render stills of intro (t≈4s) and outro (t≈3s and the final paper fade). Show me.
Keep it 100% deterministic on the paused timeline.
```

**DONE WHEN:** intro and outro stills match the scene-1 treatment, logo reveal is wired, outro resolves to paper.

---

## PROMPT 3 — Transitions + audio

```
Now wire the connective tissue and sound.

TRANSITIONS between scenes — ink-splatter wipe:
- Between each scene, an ink shape (assets/textures/ink-splatter-2.png) scales up to fully cover the frame in --ink, then the next scene's paint-in reveals through. Duration ~0.7s, overlapping the scene boundary.
- Vary the splatter PNG and direction per the storyboard (bloom/scatter/sweep/drip feel) so transitions don't feel repetitive.
- If Hyperframes' built-in HyperShader transitions give a cleaner result for some cuts, you may use a shader transition (e.g., a soft dissolve or zoom) INSTEAD for variety — but the default is the ink wipe to match the reference. Tell me which you used where.

AUDIO:
- Add assets/audio/music.mp3 as the bed for the whole composition, faded in over the first 2s and out over the last 3s.
- Add assets/audio/sfx-ink-whoosh.wav on each ink-wipe transition, synced to the moment the splatter covers the frame. Keep it subtle (low gain).
- Optional: assets/audio/sfx-paper.wav very quietly under the intro.
- Make sure audio is referenced the Hyperframes way so it ends up in the rendered MP4, and that timing stays deterministic.

Lint, preview, and render a 12-second clip spanning intro → scene1 transition so I can hear + see the ink wipe + whoosh. Show me.
```

**DONE WHEN:** transitions read as ink wipes, the whoosh hits on the cover, music bed plays in the rendered clip.

---

## PROMPT 4 — VERTICAL SLICE (render a real ~40s cut and review) 🎬 first milestone

```
Assemble a VERTICAL SLICE to validate the whole pipeline before we scale:
Running order: INTRO → scene1 → scene2 → scene3 → OUTRO.
(Build scene2 = "The First Forest" / "COFFEA ARABICA" / assets/images/02-arabica-shrub.jpg, and scene3 = "A Shepherd's Discovery" / Kaldi line / assets/images/03-goats-herder.jpg, using the scene-1 template with the storyboard's reveal + Ken Burns + selective-color settings for each.)

Then:
1. `npx hyperframes lint` → zero errors.
2. Render the full slice to "slice.mp4" at 1920x1080, 30fps.
3. Play it back yourself using the preview/inspection tools and give me an honest critique: pacing, where it drags, any reveal that looks wrong, any text that's hard to read, audio sync. Propose specific fixes (easing swaps, duration trims, mask-scale tweaks).
4. Apply your top 3 fixes and re-render. Show me before/after stills of anything you changed.

This slice is a deliverable-quality teaser on its own, so make it sing.
```

**DONE WHEN:** `slice.mp4` plays start-to-finish, looks like the reference family, audio synced. **This is your safety-net deliverable** — if the night runs out, you can ship this as a teaser.

---

## PROMPT 5 — SCALE to all scenes (mass-produce from the template)

```
The template is approved. Now build the remaining scenes (4 through 22) by cloning the scene-1 template and swapping content per the storyboard. For EACH scene use:
- the listed image (assets/images/NN-*.jpg),
- the title / subtitle / supporting line from the script,
- the reveal style (bloom/scatter/sweep/drip), Ken Burns move, and selective-color tint from the storyboard,
- the standard 9s duration unless the storyboard says otherwise.

[PASTE THE STORYBOARD TABLE FROM PRODUCTION-PACK.md SECTION 4 HERE, plus the script text for scenes 4–22 from SECTION 3.]

Requirements:
- Reuse the SAME components/classes — no per-scene structural divergence. Only content + a few data values (reveal type, kenburns direction, bleed tint) change.
- Vary the ink-splatter PNG used as the mask across scenes so reveals feel organic, not identical.
- Keep the full running order: INTRO → 1 → 2 → … → 22 → OUTRO with ink-wipe transitions + whoosh between each.
- After building, `npx hyperframes lint` → fix everything. Then preview and render LOW-RES proxy stills (one per scene) in a contact sheet so I can scan all 24 scenes at once for consistency. Flag any scene whose image/treatment looks off.
```

**DONE WHEN:** all 24 scenes exist in order, lint is clean, and a contact sheet of stills shows consistent treatment across the film.

---

## PROMPT 6 — POLISH PASS (the "make it final" step) ✨

```
Do a full refinement pass — this is the edit-bay stage. Watch the entire composition via the preview/inspection tools and refine for cinema quality:

1. PACING: render the full thing; find scenes that drag or rush. Trim/extend durations (the storyboard times are a guide, not law). Aim for a confident, unhurried rhythm.
2. EASING & STAGGER: swap eases where motion feels mechanical (try expo.out / power4.out on text, sine.inOut on Ken Burns). Tighten or loosen text stagger per scene.
3. REVEAL QUALITY: make sure each paint-in feels organic — adjust mask-scale end values and the SVG turbulence `scale` per scene so edges bleed naturally. No two reveals should feel stamped from the same cookie cutter.
4. COLOR: tune the selective-color bleed per scene (stronger reds on cherries, warm amber on the roast, cool blue only on skies). Keep the overall grade warm and consistent — never pure white/black, grain always on top.
5. MID-SCENE LIFE: add subtle continuous motion so no scene is a static slide — a faint drifting watercolor wash, a slow grain shimmer, a 1–2px float on the Latin deco. Keep it deterministic on the timeline.
6. AUDIO: make sure music swells land on the Act transitions (scenes 5, 9, 13, 18) and resolve on the outro; whooshes sit under, not over, the music.
7. TYPOGRAPHY: verify every title/subtitle is readable over its image (add a faint paper/ink scrim behind text where contrast is weak). Consistent positions and margins throughout.

Render 3–4 spot-check clips from different acts and show me. List exactly what you changed.
Reminder: everything stays on the paused, seekable timeline — no real-time animation.
```

**DONE WHEN:** the film feels intentional and consistent end-to-end; reveals look organic; audio swells land; text is always legible.

---

## PROMPT 6b — (USE ONLY IF SHORT ON TIME) the 90-second hero cut

```
Time is tight — produce a polished 75–90 second HERO CUT instead of the full 4 minutes, so I have a flawless deliverable:
Running order: INTRO → scenes [1, 5, 10, 14, 16, 17] → OUTRO. (Origin → cherry → roast → bloom → pour → cup — the emotional highlights.)
Apply the full Prompt 6 polish to ONLY these scenes. Render the final hero cut at 1920x1080, 30fps to "hero-cut.mp4". Make every second perfect.
```

**DONE WHEN:** a flawless ~90s cut exists. Ship this; deliver the full 4:00 as a follow-up.

---

## PROMPT 7 — FINAL QA + full render + export

```
Final delivery pass:
1. `npx hyperframes lint` → must be zero errors.
2. Snapshot/visual QA: render stills at the start, middle, and end of every scene; scan for any broken mask, missing asset, or text overflow. Fix anything.
3. Confirm all fonts are embedded/self-hosted and render correctly headless (no fallback fonts in the output).
4. Render the FULL film to "soul-of-coffee_1080p.mp4" at 1920x1080, 30fps, high quality. Verify audio is present and in sync across the whole runtime.
5. Report final duration, file size, and resolution. If render time is very long, tell me and offer a 1080p draft + an optional 4K final.
6. Give me a 1-paragraph "delivery notes" summary I can send the client (what it is, runtime, format, how to request changes).
```

**DONE WHEN:** `soul-of-coffee_1080p.mp4` is a clean, audio-synced, full-length export ready to send.

---

## TROUBLESHOOTING PROMPTS (paste as needed)

**Paint-in not spreading / mask not animating**

```
The ink-mask paint-in isn't animating. Confirm: (a) mask-image points to a valid transparent PNG where the INK is opaque and the rest transparent; (b) you're tweening a proxy value in GSAP and writing it to a CSS variable used by mask-size (GSAP can't tween mask-size directly); (c) the tween is on the paused master timeline, not a CSS animation. Fix and render a still mid-reveal to prove it works.
```

**Watercolor edges look hard/digital**

```
The photo edges look too clean — not watercolor. Strengthen the SVG filter on .photo-wrap: raise feDisplacementMap scale to ~24–28, set feTurbulence baseFrequency around "0.01 0.014" with numOctaves 3–4. Make sure the filter is actually applied to the masked wrapper. Show a close-up still of an edge.
```

**Render is too slow / times out**

```
Full render is too slow. Options: render at 1920x1080 (not 4K) for the deliverable; reduce SVG filter complexity on static frames; render acts separately and concatenate; or cut to the 90s hero cut (Prompt 6b). Recommend the fastest path to a clean export and do it.
```

**Fonts wrong in the render**

```
The rendered MP4 shows fallback fonts. Self-host the three .woff2 files in assets/fonts/ with @font-face, remove any Google Fonts CDN link, and ensure the render waits for fonts to load before capturing. Re-render a text-heavy still to confirm Pinyon Script / Marcellus SC / Spectral all show.
```

**Scenes feel repetitive**

```
The scenes feel stamped from one mold. Vary: the ink-splatter PNG used as each mask, the reveal direction (bloom/scatter/sweep/drip), the Ken Burns direction, and the text position occasionally (alternate lower-left / lower-right within the safe margin). Keep the SYSTEM identical but break the visual monotony. Show a fresh contact sheet.
```

---

## QUICK REFERENCE — Hyperframes commands

- Preview (browser studio, hot reload): `npx hyperframes preview`
- Lint (structural validity): `npx hyperframes lint`
- Render to MP4: `npx hyperframes render index.html --output out.mp4`
- Use the installed `/hyperframes` skill in Claude Code to drive the plan → write → wire → lint → preview → render loop.

> If a command differs in your installed version, ask Claude Code to check `npx hyperframes --help` and the repo docs, then proceed.
