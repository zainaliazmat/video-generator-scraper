// storyboard.mjs — beat spec for video-02. build.mjs turns this + audio_meta.json
// into index.html. Edit HERE, then: node build.mjs
//
// Beat: { vo:"01", pre:0.5, pad:0.7, visuals:[V, ...] }  (fracs split the beat)
// V (visual) shapes:
//   { v:"screen",   src, chip?, frac? }   — 16:9 framed screen recording (video hoisted to root)
//   { v:"phone",    src, chip?, frac? }   — portrait phone-framed recording
//   { v:"artifact", src, chip?, frac? }   — full-bleed cinematic excerpt
//   { v:"image",    src, chip?, ring?, frac? } — full-bleed still (may get the red flaw ring)
//   { v:"card",     html, chip?, anim?, frac? } — typographic card (anim: fade|pop|slam)

const card = (big, sub = "") =>
  `<div class="card">${big ? `<div class="big">${big}</div>` : ""}${sub ? `<div class="sub">${sub}</div>` : ""}</div>`;

const A = "assets";
const BARS = `<span class="bars">${"<i></i>".repeat(24)}</span>`;

export const beats = [
  // ---------- HOOK ----------
  { vo: "01", pre: 0.3, pad: 0.4, visuals: [
    { v: "artifact", src: `${A}/excerpts/ex-1907.mp4`, pos: "left", frac: 0.42 },
    { v: "artifact", src: `${A}/excerpts/ex-1970.mp4`, pos: "left", frac: 0.30 },
    { v: "card", html: card(`<span class="mono">$ npx hyperframes render</span>`, "one command. no timeline."), anim: "pop", frac: 0.28 },
  ]},
  { vo: "02", pad: 0.6, visuals: [
    { v: "card", html: card(`DOCUMENTARY VOICE = <span class="amber">AI</span>`, BARS), chip: "FREE · OPEN SOURCE · YOU'LL GENERATE ONE YOURSELF", anim: "pop" },
  ]},
  { vo: "03", pad: 0.5, visuals: [{ v: "screen", src: `${A}/sub/runbook-click.mp4`, chip: "~5 HOURS · A REAL WORKFLOW — NOT ONE PROMPT", zoom: { at: 7.2, dur: 1.4, scale: 1.7, origin: "100% 40%" } }] },
  { vo: "04", pad: 0.7, visuals: [{ v: "card", html: card("THE EXACT WORKFLOW"), chip: "THE TOOL · THE BUILD · THE SHOCKS · 8:25 — WHERE IT BREAKS" }] },

  // ---------- ANSWER FAST ----------
  { vo: "05", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/pinterest.mp4`, chip: "STEP 1 — THE REFERENCE", zoom: { at: 5.8, dur: 1.3, scale: 2.1, origin: "0% 0%", y: -145 }, brackets: true }] },
  { vo: "06", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/runbook-doc-a.mp4`, chip: "STEP 2 — THE BLUEPRINT · 2–3 HOURS", zoom: { at: 0.6, dur: 1.2, scale: 1.6, origin: "100% 40%" } }] },
  { vo: "07", pad: 0.4, visuals: [{ v: "card", html: card("STEP 3 — THE ASSETS", "archival photographs · public domain · downloaded by hand") }] },
  { vo: "08", pad: 0.4, visuals: [
    { v: "screen", src: `${A}/sub/prompt-typing.mp4`, chip: "STEP 4 — SCENES AS CODE", frac: 0.55 },
    { v: "artifact", src: `${A}/excerpts/ex-title.mp4`, chip: "4:00 · 1080p", frac: 0.45 },
  ]},
  // ---------- WHAT IT IS ----------
  { vo: "10", pad: 0.5, visuals: [{ v: "card", html: card("HYPERFRAMES", "open-sourced by HeyGen — April 2026") }] },
  { vo: "11", pad: 0.4, visuals: [{ v: "phone", src: `${A}/clips-trimmed/clip-03-timeline.mp4`, chip: "THE OLD WAY — EVERY CUT BY HAND" }] },
  { vo: "12", pad: 0.4, visuals: [{ v: "screen", src: `${A}/clips-trimmed/clip-05-scene-code.mp4`, chip: "WRITE IT ONCE — data-start · data-duration · ZERO GALTI" }] },
  { vo: "13", pad: 0.4, visuals: [{ v: "card", html: card(`<span class="mono">PREVIEW → ADJUST → RE-RENDER</span>`, "you don't hear the music while you write it") }] },
  { vo: "14", pad: 0.6, visuals: [{ v: "card", html: card(`DRAG A PLAYHEAD <span class="red">✗</span><br>WRITE STRUCTURED TEXT <span class="green">✓</span>`, "video editing becomes something an AI is naturally good at") }] },

  // ---------- STAGE 1: BLUEPRINT ----------
  { vo: "15", pad: 0.5, visuals: [{ v: "card", html: card(`STAGE 1 — <span class="amber">THE BLUEPRINT</span>`, "the part every other video skips"), anim: "pop" }] },
  { vo: "16", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/runbook-doc-b.mp4`, chip: "2–3 HOURS OF BACK-AND-FORTH — THIS IS THE WORK", zoom: { at: 0.6, dur: 1.2, scale: 1.6, origin: "100% 40%" } }] },
  { vo: "17", pad: 0.7, visuals: [{ v: "screen", src: `${A}/sub/runbook-doc-c.mp4`, chip: "THE BLUEPRINT IS WORTH MORE THAN THE RENDER", zoom: { at: 0.6, dur: 1.2, scale: 1.6, origin: "100% 40%" } }] },

  // ---------- STAGE 2: DESIGN ----------
  { vo: "18", pad: 0.4, visuals: [{ v: "screen", src: `${A}/clips-trimmed/clip-02-design.mp4`, chip: "STAGE 2 — DESIGN.md" }] },
  { vo: "19", pad: 0.4, visuals: [{ v: "artifact", src: `${A}/excerpts/ex-1907-long.mp4`, chip: "KEN BURNS + PARALLAX — TEXT AT ⅓ PHOTO SPEED" }] },
  { vo: "20", pad: 0.6, visuals: [{ v: "card", html: card(`DESIGN AS LAW <span class="green">✓</span>`, "change it once — the whole video regrades itself") }] },

  // ---------- STAGE 3: RESEARCH ----------
  { vo: "21", pad: 0.4, visuals: [{ v: "card", html: `<div class="card"><div class="tline">${[["1841", "s01_1841_cook"], ["1869", "s02_1869_suez"], ["1883", "s03_1883_orient"], ["1907", "s05_1907_mauretania"], ["1927", "s07_1927_aviation"], ["1970", "s11_1970_747"]].map(([y, img], i) => `<div class="tcard"><img src="${A}/images/years/${img}.jpg"><span class="tyear${i % 2 ? "" : " amber"}">${y}</span></div>`).join("")}</div><div class="sub">the verified timeline came first</div></div>` }] },
  { vo: "22", pad: 0.6, visuals: [{ v: "card", html: card(`AUDIO FIRST <span class="amber">→</span> THEN VISUALS`, "14 segments · ~160 seconds · timed before any visuals existed") }] },

  // ---------- STAGE 4: ASSETS ----------
  { vo: "23", pad: 0.4, visuals: [{ v: "card", html: card(`STAGE 4 — <span class="amber">THE ASSETS</span>`, "downloaded by hand · public domain · safe to monetize") }] },
  { vo: "24", pad: 0.6, visuals: [{ v: "card", html: card("BUDGET ~45 MINUTES", "source hunting separates cinematic from stock-slideshow") }] },

  // ---------- STAGE 5: VOICE ----------
  { vo: "25", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/kokoro-gen.mp4`, chip: "STAGE 5 — KOKORO · FREE · RUNS LOCALLY" }] },
  { vo: "26", pad: 0.6, visuals: [{ v: "card", html: card(`THIS VOICE = <span class="green">MINE</span><br>DOCUMENTARY VO = <span class="amber">KOKORO</span>`, BARS), chip: "THE DEMO SPEAKS FOR ITSELF", anim: "pop" }] },
  { vo: "27", pad: 0.6, visuals: [{ v: "card", html: card(`“Altered content?” — <span class="green">YES</span>`, "disclosed. it costs nothing — viewers respect it more than they punish it") }] },

  // ---------- STAGE 6: SCENES + RENDER ----------
  { vo: "28", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/prompt-typing.mp4`, chip: "STAGE 6 — ONE PROMPT PER SCENE" }] },
  { vo: "29", pad: 0.4, visuals: [{ v: "screen", src: `${A}/sub/scene-written.mp4`, chip: "THE 1907 SCENE — WRITTEN, NOT CUT" }] },
  { vo: "30", pad: 1.8, visuals: [
    { v: "screen", src: `${A}/clips-trimmed/clip-06-render.mp4`, chip: "ONE COMMAND · ~20 MIN", frac: 0.6 },
    { v: "artifact", src: `${A}/excerpts/ex-1907.mp4`, chip: "734 MB · 1080p · 4:00", frac: 0.4 },
  ]},

  // ---------- WHERE IT BREAKS ----------
  { vo: "31", pre: 0.6, pad: 0.8, visuals: [{ v: "card", html: `<div class="card"><div class="stamp">WHAT THEY SKIP</div></div>`, anim: "slam" }] },
  { vo: "32", pad: 1.4, visuals: [{ v: "card", html: card(`<span class="red">STOP.</span>`), anim: "pop" }] },
  { vo: "33", pad: 0.5, visuals: [{ v: "card", html: card(`ASKED <span class="mono">5:00</span> → GOT <span class="mono red">9:38</span>`, "11 / 11 cuts landed mid-sentence — independent testing, 2026") }] },
  { vo: "34", pad: 0.6, visuals: [{ v: "card", html: card(`CUTTING REAL FOOTAGE <span class="red">✗</span><br>WRITING MOTION <span class="green">✓</span>`, "nothing is ever cut — so nothing is ever miscut") }] },
  { vo: "35", pad: 0.5, visuals: [{ v: "card", html: card("RECORD REAL SCREENS BY HAND", "my automated capture came out frozen and lurching — render everything else") }] },
  { vo: "36", pad: 0.6, visuals: [{ v: "card", html: card("FIRST VIDEO? BUDGET A FULL DAY", "treat it as learning, not losing") }] },
  // ---------- PAYOFF ----------
  { vo: "39", pad: 0.4, visuals: [{ v: "card", html: card("THE WHOLE PIPELINE", "honestly. end to end.") }] },
  { vo: "40", pad: 0.5, visuals: [{ v: "card", html: card(`<div class="pipe"><span>REFERENCE</span><span>BLUEPRINT</span><span>ASSETS</span><span>14 VOICE LINES</span><span>14 SCENES</span><span class="amber">1 COMMAND</span></div>`), anim: "pop" }] },
  { vo: "41", pad: 0.6, visuals: [{ v: "artifact", src: `${A}/excerpts/ex-1970.mp4`, chip: "~5 HONEST HOURS · I AM NOT AN EDITOR — THAT'S THE POINT" }] },
  { vo: "42", pad: 0.8, visuals: [{ v: "card", html: card(`TAKE THE <span class="amber">BLUEPRINT</span> — FREE`, "runbook template · design file · exact prompts — link below · no email gate"), anim: "pop" }] },

  // ---------- VERDICT ----------
  { vo: "43", pad: 0.4, visuals: [{ v: "card", html: card("SHOULD YOU USE THIS?") }] },
  { vo: "44", pad: 0.4, visuals: [{ v: "card", html: card(`REAL-FOOTAGE CREATORS → <span class="red">SKIP ✗</span>`, "vlogs · gameplay · interviews — a timeline editor is still faster") }] },
  { vo: "45", pad: 1.6, visuals: [{ v: "card", html: card(`MOTION-GRAPHIC CREATORS → <span class="green">TRY IT ✓</span>`, "explainers · documentaries · data stories · faceless channels — come with a blueprint, not a wish") }] },
  { vo: "46", pad: 0.6, visuals: [{ v: "card", html: card(`100% FREE — <span class="amber">NO CATCH.</span>`), anim: "pop" }] },
  { vo: "47", pad: 0.5, visuals: [{ v: "artifact", src: `${A}/excerpts/ex-outro.mp4`, chip: "THE SISTER CHANNEL — EVERY VIDEO, BLUEPRINT FIRST" }] },

  // ---------- CTA ----------
  { vo: "48", pad: 0.4, visuals: [{ v: "card", html: card("NEXT: THE FULL FACELESS STACK", "script · voice · visuals · edit — start to finish") }] },
  { vo: "49", pad: 0.5, visuals: [{ v: "card", html: card(`WHICH ONE TOOL IS WORTH <span class="amber">PAYING</span> FOR?`, "not the one you think · subscribe — weekly, no hype") }] },
  { vo: "50", pad: 2.2, visuals: [{ v: "artifact", src: `${A}/excerpts/ex-title.mp4`, chip: "the full documentary — link below" }] },
];
