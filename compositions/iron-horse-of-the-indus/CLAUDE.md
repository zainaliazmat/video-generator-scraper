# Project context — Vintage Archival Documentary (read this; don't re-derive the framework)

HyperFrames turns an HTML composition into an MP4: edit one HTML file, preview in a browser, render with `npx hyperframes render`. The essentials are below; open full skills only when a task needs more.

## Composition contract (must hold or the render fails)
- Root is ONE <div> in <body>: data-composition-id, data-width, data-height, data-duration (s), data-fps; position:relative, sized px, overflow:hidden. Render length = root's data-duration.
- Clips = class "clip" + data-start, data-duration, data-track-index, DIRECT children of the root. <video>/<audio> are direct children too.
- Exactly ONE gsap.timeline({ paused:true }) on window.__timelines["main"].

## Determinism (non-negotiable)
- No Date.now()/performance.now()/unseeded Math.random()/network at render. No repeat:-1.
- Animate ONLY x, y (xPercent/yPercent), scale, rotation, opacity, color, backgroundColor, borderRadius. NEVER width/height/top/left/display/visibility.
- Full-screen fills on a full-bleed child (absolute; inset:0), never the root. Unique ids. Grain = SVG feTurbulence with FIXED seed.

## CLI
`npx hyperframes` → init, add, lint, validate, inspect, snapshot --at <t>, preview, render --output <file>. Always lint+validate+inspect to 0 errors before preview/render.

## Skills
Multi-scene montage: `general-video` spine + `hyperframes-core`, `hyperframes-animation`, `hyperframes-media`, `media-use` as needed. Do NOT use `slideshow` (it outputs an interactive deck, not a video).

## This style's motion idioms
- Ken Burns: scale ~1.0 → ~1.14, ease sine.inOut, whole scene; alternate drift direction per scene.
- Parallax: photo (near plane) drifts MORE than text (~25–35% of photo travel) via xPercent.
- Text entrance order per scene: kicker → numeral(+rule) → title → caption.
- Transitions: slow ~1.0s cross-dissolve on overlapping clips; optional soft white bloom at 2–3 act breaks. No hard cuts.

## Brand truth
`DESIGN.md` is the source of truth for palette, grade recipe, typography, layout, motion, overlays. Precedence: frame.md → design.md → DESIGN.md.

## Audio / voiceover
Free offline voice: `npx hyperframes tts "<line>" --provider kokoro --voice bm_george --speed 0.95 -o assets/audio/vo_sNN.wav`. ElevenLabs/HeyGen are optional paid upgrades (set ELEVENLABS_API_KEY / HEYGEN_API_KEY). Background music/SFX via the media skill; HeyGen library needs `npx hyperframes auth login`, else it falls back to a local generator.
