// build-composition.mjs — generate the full "Soul of Coffee" composition (index.html).
// Edit-bay refined: per-scene pacing, easing, reveal turbulence, colour, mid-scene
// life, audio swells, type legibility. Every scene reuses the SAME components/classes.
// Run: node build-composition.mjs   →   writes index.html
import fs from "node:fs";

/* layout: odd n = photo-right/text-left (scene-1) ; even n = mirrored
   reveal: bloom | scatter | sweep | drip   kb: {push:X}|{pull:F}|"panL"|"panR"
   tint:  watercolour bleed "r,g,b,a"   op: selective-colour (photo-color) strength
   base?: per-scene photo-base filter override (e.g. the light vintage map) */
const SCENES = [
  { n: 1, dur: 10, img: "01-highlands.jpg", title: "Where It Begins", sub: "Ethiopian Highlands", line: "1,500 metres above the sea", reveal: "bloom", kb: { push: 1.08 }, tint: "95,120,82,0.20", op: 0.7 },
  { n: 2, dur: 9, img: "02-arabica-shrub.jpg", title: "The First Forest", sub: "Coffea Arabica", line: "Wild beneath the forest canopy", reveal: "scatter", kb: "panL", tint: "74,110,55,0.26", op: 0.84 },
  { n: 3, dur: 10, img: "03-goats-herder.jpg", title: "A Shepherd's Discovery", sub: "The Legend of Kaldi", line: "His goats danced on the crimson cherry", reveal: "sweep", kb: { push: 1.07 }, tint: "150,85,52,0.24", op: 0.66 },
  { n: 4, dur: 8, img: "04-world-map-vintage.jpg", title: "Across the World", sub: "From Kaffa to the Cup", line: "A single seed, carried over oceans", reveal: "drip", kb: { pull: 1.08 }, tint: "150,120,80,0.16", op: 0.55, base: "grayscale(0.28) sepia(0.34) contrast(1.0) brightness(1.16)", vig: 0.24 },
  { n: 5, dur: 10, img: "05-red-cherries.jpg", title: "The Crimson Harvest", sub: "Ripe & Ready", line: "Only the reddest are chosen", reveal: "bloom", kb: { push: 1.10 }, tint: "186,40,34,0.34", op: 0.92 },
  { n: 6, dur: 9, img: "06-hands-picking.jpg", title: "Picked by Hand", sub: "One Cherry at a Time", line: "No machine knows ripeness like a hand", reveal: "scatter", kb: "panR", tint: "176,90,66,0.26", op: 0.8 },
  { n: 7, dur: 8, img: "07-harvest-baskets.jpg", title: "The Day's Gathering", sub: "Baskets Brim Full", line: "A morning's patient work", reveal: "sweep", kb: { push: 1.07 }, tint: "166,70,50,0.28", op: 0.78 },
  { n: 8, dur: 9, img: "08-drying-beds.jpg", title: "Under the Sun", sub: "Raised Drying Beds", line: "Turned by hand for twelve days", reveal: "drip", kb: "panL", tint: "205,170,115,0.22", op: 0.7 },
  { n: 9, dur: 9, img: "09-green-beans.jpg", title: "The Green Heart", sub: "Unroasted Potential", line: "Dense, grassy, and alive", reveal: "bloom", kb: { push: 1.07 }, tint: "110,125,90,0.20", op: 0.62 },
  { n: 10, dur: 10, img: "10-roaster-drum.jpg", title: "Into the Fire", sub: "The Roast Begins", line: "Where sugar becomes aroma", reveal: "scatter", kb: { push: 1.10 }, tint: "212,118,38,0.34", op: 0.9 },
  { n: 11, dur: 9, img: "11-roasted-beans.jpg", title: "First Crack", sub: "Roasted Dark & Bright", line: "Oils rise to the surface", reveal: "bloom", kb: { pull: 1.08 }, tint: "132,74,40,0.28", op: 0.82 },
  { n: 12, dur: 9, img: "12-roaster-hands.jpg", title: "The Roaster's Judgment", sub: "By Sight & Smell", line: "Seconds decide everything", reveal: "sweep", kb: "panR", tint: "146,92,55,0.24", op: 0.76 },
  { n: 13, dur: 8, img: "13-grinder.jpg", title: "Ground to Order", sub: "The Burr Turns", line: "Fragrance, released in an instant", reveal: "bloom", kb: { push: 1.07 }, tint: "120,112,102,0.20", op: 0.6 },
  { n: 14, dur: 10, img: "14-bloom-steam.jpg", title: "The Bloom", sub: "First Pour", line: "It blooms, and breathes", reveal: "scatter", kb: { push: 1.08 }, tint: "176,122,72,0.26", op: 0.8 },
  { n: 15, dur: 10, img: "15-jebena-pour.jpg", title: "The Jebena", sub: "Ethiopian Tradition", line: "Poured high, in a single arc", reveal: "sweep", kb: "panL", tint: "186,98,60,0.28", op: 0.82 },
  { n: 16, dur: 9, img: "16-pour-over.jpg", title: "The Slow Pour", sub: "Patience in a Spiral", line: "Water finds its own way down", reveal: "drip", kb: { push: 1.07 }, tint: "172,122,52,0.26", op: 0.78 },
  { n: 17, dur: 11, img: "17-finished-cup.jpg", title: "The First Sip", sub: "Crema & Calm", line: "Everything led to this", reveal: "bloom", kb: { push: 1.06 }, tint: "182,132,82,0.24", op: 0.82 },
  { n: 18, dur: 9, img: "18-cafe-window.jpg", title: "A Place to Gather", sub: "Warm Light, Cold Morning", line: "The world slows at the window", reveal: "scatter", kb: "panR", tint: "192,142,82,0.24", op: 0.76 },
  { n: 19, dur: 10, img: "19-shared-table.jpg", title: "Shared", sub: "Around One Table", line: "Coffee was never meant for one", reveal: "sweep", kb: { push: 1.07 }, tint: "182,122,82,0.24", op: 0.78 },
  { n: 20, dur: 9, img: "20-hands-cup-closeup.jpg", title: "Held", sub: "Warmth in the Palms", line: "A small, daily comfort", reveal: "bloom", kb: { push: 1.07 }, tint: "186,136,92,0.24", op: 0.8 },
  { n: 21, dur: 9, img: "21-beans-scattered.jpg", title: "From Bean to Cup", sub: "The Whole Journey", line: "Every cup remembers the forest", reveal: "scatter", kb: { pull: 1.08 }, tint: "122,76,46,0.28", op: 0.82 },
  { n: 22, dur: 10, img: "22-barista-portrait.jpg", title: "The Hands Behind It", sub: "The Barista", line: "Craft, passed from hand to hand", reveal: "bloom", kb: { push: 1.08 }, tint: "182,126,82,0.24", op: 0.8 },
];

// transition OUT of each clip (Intro→1 … 22→Outro): 23 entries
const TRANS = ["ink", "scatter", "ink", "drip", "ink", "scatter", "ink", "drip", "ink", "scatter", "ink", "drip", "ink", "scatter", "ink", "drip", "ink", "scatter", "ink", "drip", "ink", "scatter", "ink-slow"];

const INTRO_DUR = 11;
const OUTRO_DUR = 22;

// ---- timing ----
let t = INTRO_DUR;
for (const s of SCENES) {
  s.start = t;
  s.layout = s.n % 2 === 1 ? "right" : "left";
  t += s.dur;
}
const OUTRO_START = t;
const TOTAL = OUTRO_START + OUTRO_DUR;
const BOUNDARIES = [...SCENES.map((s) => s.start), OUTRO_START];
const ACT_STARTS = [5, 9, 13, 18].map((n) => SCENES.find((s) => s.n === n).start);

// ---- reveal → paint-in mask + turbulence config ----
const REVEAL = {
  bloom: { png: 1, ease: "power2.out", from: 8, pdur: 1.9, pend: 156, fscale: 13, bf: "0.010 0.013" },
  scatter: { png: 2, ease: "power2.out", from: 14, pdur: 2.1, pend: 170, fscale: 23, bf: "0.015 0.019" },
  sweep: { png: 4, ease: "power1.out", from: 10, pdur: 2.0, pend: 162, fscale: 18, bf: "0.012 0.016" },
  drip: { png: 3, ease: "power2.out", from: 12, pdur: 2.0, pend: 172, fscale: 26, bf: "0.013 0.017" },
};
const TRANSCFG = {
  ink: { png: 1, pos: "center", cover: 0.4 },
  scatter: { png: 2, pos: "center", cover: 0.4 },
  drip: { png: 3, pos: "50% -30%", cover: 0.4 },
  "ink-slow": { png: 1, pos: "center", cover: 0.6 },
};

function kbVars(kb) {
  if (kb === "panL") return { from: { s: 1.05, x: 0, y: 0 }, to: { s: 1.055, x: 2.4, y: -0.6 } };
  if (kb === "panR") return { from: { s: 1.05, x: 0, y: 0 }, to: { s: 1.055, x: -2.4, y: -0.6 } };
  if (kb.pull) return { from: { s: kb.pull, x: 0.9, y: 0.6 }, to: { s: 1.0, x: 0, y: 0 } };
  return { from: { s: 1.0, x: 0, y: 0 }, to: { s: kb.push, x: -1.3, y: -1.1 } };
}

const SHARED_CSS = fs.readFileSync(new URL("./_shared.css", import.meta.url), "utf8");

// ============================ CSS ============================
function sceneCss(s) {
  const r = REVEAL[s.reveal];
  const panel =
    s.layout === "right"
      ? "top: 64px; right: 90px; bottom: 90px; left: 600px;"
      : "top: 64px; left: 90px; bottom: 90px; right: 600px;";
  let css =
    `      #scene-${s.n} .photo-wrap {\n` +
    `        ${panel}\n        --paint: ${r.from}%;\n        filter: url(#wc-${s.n});\n` +
    `        -webkit-mask-image: url("assets/textures/ink-splatter-${r.png}.png");\n` +
    `        mask-image: url("assets/textures/ink-splatter-${r.png}.png");\n      }\n` +
    `      #scene-${s.n} .photo-color { background-image: url("assets/images/${s.img}"); opacity: ${s.op}; }\n` +
    `      #scene-${s.n} .watercolor-tex { background-image: linear-gradient(rgba(${s.tint}), rgba(${s.tint})), url("assets/textures/watercolor-1.png"); }\n`;
  if (s.base) css += `      #scene-${s.n} .photo-base { filter: ${s.base}; }\n`;
  if (s.vig) css += `      #scene-${s.n} .vignette { opacity: ${s.vig}; }\n`;
  if (s.layout === "left") css += `      #scene-${s.n} .text-block { left: auto; right: 150px; bottom: 110px; text-align: right; }\n`;
  return css;
}
function transCss(i, type) {
  const c = TRANSCFG[type];
  return (
    `      #trans-${i} .ink-fill {\n` +
    `        -webkit-mask-image: url("assets/textures/ink-splatter-${c.png}.png");\n` +
    `        mask-image: url("assets/textures/ink-splatter-${c.png}.png");\n` +
    `        -webkit-mask-position: ${c.pos};\n        mask-position: ${c.pos};\n      }\n`
  );
}

// ============================ SVG filters ============================
function filterDef(id, bf, seed, scale) {
  return `        <filter id="${id}" x="-12%" y="-12%" width="124%" height="124%"><feTurbulence type="fractalNoise" baseFrequency="${bf}" numOctaves="3" seed="${seed}" result="n" /><feDisplacementMap in="SourceGraphic" in2="n" scale="${scale}" xChannelSelector="R" yChannelSelector="G" /></filter>`;
}
const filterDefs = [
  filterDef("watercolor-edge", "0.012 0.016", 7, 20), // default (intro/outro/transitions)
  ...SCENES.map((s) => {
    const r = REVEAL[s.reveal];
    return filterDef(`wc-${s.n}`, r.bf, s.n * 3 + 1, r.fscale + (s.n % 4));
  }),
].join("\n");

// ============================ HTML ============================
function sceneHtml(s) {
  return `      <!-- ===== SCENE ${s.n} (${s.start}-${s.start + s.dur}s) — ${s.layout} ===== -->
      <section id="scene-${s.n}" class="scene clip" data-start="${s.start}" data-duration="${s.dur}" data-track-index="1">
        <div class="scene-content">
          <div class="paper-bg"></div>
          <div class="photo-wrap">
            <div class="photo-inner">
              <img class="photo-base" src="assets/images/${s.img}" alt="" onerror="this.style.display='none'" />
              <div class="photo-color"></div>
              <div class="watercolor-tex"></div>
            </div>
            <div class="photo-feather"></div>
          </div>
          <div class="text-block">
            <h1 class="title">${s.title}</h1>
            <p class="subtitle">${s.sub}</p>
            <p class="line">${s.line}</p>
          </div>
          <div class="grain"></div>
          <div class="vignette"></div>
        </div>
      </section>`;
}
function transHtml(i) {
  const b = BOUNDARIES[i - 1];
  const dur = TRANS[i - 1] === "ink-slow" ? 1.1 : 0.9;
  return `      <div id="trans-${i}" class="ink-transition clip" data-start="${(b - 0.4).toFixed(2)}" data-duration="${dur}" data-track-index="5"><div class="ink-fill"></div></div>`;
}
function whooshHtml(i) {
  const b = BOUNDARIES[i - 1];
  return `      <audio id="whoosh-${i}" src="assets/audio/sfx-ink-whoosh.wav" data-start="${(b - 0.25).toFixed(2)}" data-duration="0.6" data-track-index="12" data-volume="0.24"></audio>`;
}

// ============================ JS timeline ============================
function sceneJs(s) {
  const r = REVEAL[s.reveal];
  const k = kbVars(s.kb);
  const gap = s.dur >= 10 ? 0.42 : 0.3; // looser stagger on longer scenes
  const tTitle = (s.start + 0.9).toFixed(2);
  const tSub = (s.start + 0.9 + gap).toFixed(2);
  const tLine = (s.start + 0.9 + 2 * gap).toFixed(2);
  const wx = s.layout === "right" ? 2.6 : -2.6; // wash drifts away from the text
  return (
    `      paintIn(document.querySelector("#scene-${s.n} .photo-wrap"), "--paint", ${r.from}, ${r.pend}, ${r.pdur}, "${r.ease}", ${s.start});\n` +
    `      tl.fromTo("#scene-${s.n} .photo-inner", { scale: ${k.from.s}, xPercent: ${k.from.x}, yPercent: ${k.from.y} }, { scale: ${k.to.s}, xPercent: ${k.to.x}, yPercent: ${k.to.y}, ease: "sine.inOut", duration: ${s.dur} }, ${s.start});\n` +
    `      tl.fromTo("#scene-${s.n} .watercolor-tex", { xPercent: 0, yPercent: 0 }, { xPercent: ${wx}, yPercent: -1.8, ease: "sine.inOut", duration: ${s.dur} }, ${s.start});\n` +
    `      tl.fromTo("#scene-${s.n} .grain", { opacity: 0.3 }, { opacity: 0.4, ease: "sine.inOut", duration: ${(s.dur / 2).toFixed(2)}, repeat: 1, yoyo: true }, ${s.start});\n` +
    `      rise("#scene-${s.n} .title", 1.5, ${tTitle});\n` +
    `      rise("#scene-${s.n} .subtitle", 1.3, ${tSub});\n` +
    `      rise("#scene-${s.n} .line", 1.2, ${tLine});`
  );
}
function transJs(i) {
  const b = BOUNDARIES[i - 1];
  const c = TRANS[i - 1] === "ink-slow" ? TRANSCFG["ink-slow"] : TRANSCFG[TRANS[i - 1]];
  return `      inkWipe("trans-${i}", ${(b - 0.4).toFixed(2)}, ${c.cover}, 0.45);`;
}

const sceneCssBlock = SCENES.map(sceneCss).join("");
const transCssBlock = TRANS.map((ty, i) => transCss(i + 1, ty)).join("");
const sceneHtmlBlock = SCENES.map(sceneHtml).join("\n\n");
const transHtmlBlock = TRANS.map((_, i) => transHtml(i + 1)).join("\n");
const whooshBlock = TRANS.map((_, i) => whooshHtml(i + 1)).join("\n");
const sceneJsBlock = SCENES.map(sceneJs).join("\n");
const transJsBlock = TRANS.map((_, i) => transJs(i + 1)).join("\n");
const actSwellJs = ACT_STARTS.map(
  (a) =>
    `      tl.to("#bgm", { volume: 0.94, duration: 1.6, ease: "sine.out" }, ${(a - 1.6).toFixed(2)});\n` +
    `      tl.to("#bgm", { volume: 0.8, duration: 2.8, ease: "sine.inOut" }, ${(a + 0.4).toFixed(2)});`
).join("\n");

const html = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>The Soul of Coffee</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
${SHARED_CSS}
      /* ===== generated per-scene overrides ===== */
${sceneCssBlock}      /* ===== generated transition masks ===== */
${transCssBlock}    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="${TOTAL}">
      <!-- ===================== INTRO (0-${INTRO_DUR}s) ===================== -->
      <section id="intro" class="scene clip" data-start="0" data-duration="${INTRO_DUR}" data-track-index="1">
        <div class="scene-content">
          <div class="paper-bg"></div>
          <div class="photo-wrap">
            <div class="photo-inner">
              <img class="photo-base" src="assets/images/00-hills-dawn.jpg" alt="" onerror="this.style.display='none'" />
              <div class="photo-color"></div>
              <div class="watercolor-tex"></div>
            </div>
            <div class="photo-feather"></div>
          </div>
          <div class="paper-veil"></div>
          <div class="text-center">
            <h1 class="title">The Soul of Coffee</h1>
            <div class="brand-logo">
              <img src="assets/brand/logo.svg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='grid'" />
              <div class="logo-fallback" style="display: none">LOGO</div>
            </div>
            <p class="subtitle">A Film About Origin, Craft &amp; Ritual</p>
          </div>
          <div class="grain"></div>
          <div class="vignette"></div>
        </div>
      </section>

${sceneHtmlBlock}

      <!-- ===================== OUTRO (${OUTRO_START}-${TOTAL}s) ===================== -->
      <section id="outro" class="scene clip" data-start="${OUTRO_START}" data-duration="${OUTRO_DUR}" data-track-index="1">
        <div class="scene-content">
          <div class="paper-bg"></div>
          <div class="photo-wrap">
            <div class="photo-inner">
              <img class="photo-base" src="assets/images/23-cup-on-wood.jpg" alt="" onerror="this.style.display='none'" />
              <div class="photo-color"></div>
              <div class="watercolor-tex"></div>
            </div>
            <div class="photo-feather"></div>
          </div>
          <div class="paper-veil"></div>
          <div class="text-center">
            <h1 class="title">The Soul of Coffee</h1>
            <div class="brand-logo">
              <img src="assets/brand/logo.svg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='grid'" />
              <div class="logo-fallback" style="display: none">LOGO</div>
            </div>
            <p class="subtitle">[Brand Name]</p>
            <p class="line">[website] · [tagline]</p>
          </div>
          <div class="grain"></div>
          <div class="vignette"></div>
        </div>
      </section>

      <!-- ===== ink-wipe transition clips ===== -->
${transHtmlBlock}

      <!-- ===== audio (direct children of #root) ===== -->
      <audio id="bgm" src="assets/audio/music.mp3" data-start="0" data-duration="${TOTAL}" data-track-index="10" data-volume="0.8"></audio>
      <audio id="sfx-paper" src="assets/audio/sfx-paper.wav" data-start="0" data-track-index="11" data-volume="0.16"></audio>
${whooshBlock}
    </div>

    <svg class="svg-defs" aria-hidden="true">
      <defs>
${filterDefs}
      </defs>
    </svg>

    <script>
      window.__timelines = window.__timelines || {};
      var tl = gsap.timeline({ paused: true });

      function paintIn(el, varName, from, to, dur, ease, at) {
        var p = { v: from };
        el.style.setProperty(varName, from + "%");
        tl.fromTo(p, { v: from }, { v: to, duration: dur, ease: ease, onUpdate: function () { el.style.setProperty(varName, p.v + "%"); } }, at);
      }
      function rise(sel, dur, at) {
        tl.fromTo(sel, { opacity: 0, y: 26 }, { opacity: 1, y: 0, duration: dur, ease: "expo.out" }, at);
      }
      function inkWipe(transId, start, coverDur, fadeDur) {
        var el = document.querySelector("#" + transId + " .ink-fill");
        var p = { v: 0 };
        el.style.setProperty("--tx-paint", "0%");
        tl.fromTo(p, { v: 0 }, { v: 260, duration: coverDur, ease: "power2.in", onUpdate: function () { el.style.setProperty("--tx-paint", p.v + "%"); } }, start);
        tl.fromTo(el, { opacity: 1 }, { opacity: 0, duration: fadeDur, ease: "power1.out" }, start + coverDur);
      }

      /* ---------------- INTRO ---------------- */
      paintIn(document.querySelector("#intro .photo-wrap"), "--paint", 8, 160, 2.6, "power1.out", 0);
      tl.fromTo("#intro .photo-inner", { scale: 1, xPercent: 0, yPercent: 0 }, { scale: 1.06, xPercent: -0.6, yPercent: -0.4, ease: "sine.inOut", duration: ${INTRO_DUR} }, 0);
      tl.fromTo("#intro .watercolor-tex", { xPercent: 0, yPercent: 0 }, { xPercent: 1.6, yPercent: -1.2, ease: "sine.inOut", duration: ${INTRO_DUR} }, 0);
      rise("#intro .title", 1.7, 1.0);
      rise("#intro .subtitle", 1.3, 1.7);
      paintIn(document.querySelector("#intro .brand-logo"), "--logo-paint", 0, 150, 1.2, "power2.out", 3.0);
      tl.fromTo("#intro .text-center", { opacity: 1 }, { opacity: 0, duration: 1.5, ease: "power2.inOut" }, ${INTRO_DUR - 1.5});
      tl.set("#intro .text-center", { opacity: 0 }, ${INTRO_DUR});

      /* ---------------- CONTENT SCENES (1–22) ---------------- */
${sceneJsBlock}

      /* ---------------- OUTRO ---------------- */
      paintIn(document.querySelector("#outro .photo-wrap"), "--paint", 8, 160, 2.6, "power1.out", ${OUTRO_START});
      tl.fromTo("#outro .photo-inner", { scale: 1, xPercent: 0, yPercent: 0 }, { scale: 1.05, xPercent: -0.8, yPercent: -0.5, ease: "sine.inOut", duration: ${OUTRO_DUR} }, ${OUTRO_START});
      tl.fromTo("#outro .watercolor-tex", { xPercent: 0, yPercent: 0 }, { xPercent: 1.4, yPercent: -1.0, ease: "sine.inOut", duration: ${OUTRO_DUR} }, ${OUTRO_START});
      rise("#outro .title", 1.7, ${OUTRO_START + 1});
      paintIn(document.querySelector("#outro .brand-logo"), "--logo-paint", 0, 150, 1.2, "power2.out", ${OUTRO_START + 3});
      rise("#outro .subtitle", 1.3, ${OUTRO_START + 1.7});
      rise("#outro .line", 1.2, ${OUTRO_START + 2.2});
      tl.fromTo("#outro .photo-wrap", { opacity: 1 }, { opacity: 0, duration: 6, ease: "power2.inOut" }, ${TOTAL - 6});
      tl.fromTo("#outro .text-center", { opacity: 1 }, { opacity: 0, duration: 6, ease: "power2.inOut" }, ${TOTAL - 6});
      tl.fromTo("#outro .paper-veil", { opacity: 1 }, { opacity: 0, duration: 6, ease: "power2.inOut" }, ${TOTAL - 6});

      /* ---------------- INK-WIPE TRANSITIONS ---------------- */
${transJsBlock}

      /* ---------------- MUSIC BED + act swells ---------------- */
      tl.fromTo("#bgm", { volume: 0 }, { volume: 0.8, duration: 2, ease: "sine.out" }, 0);
${actSwellJs}
      tl.to("#bgm", { volume: 0, duration: 4, ease: "sine.in" }, ${TOTAL - 4});
      tl.to("#sfx-paper", { volume: 0, duration: 0.5, ease: "sine.in" }, 0.8);

      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
`;

fs.writeFileSync(new URL("./index.html", import.meta.url), html);
console.log(`Wrote index.html — ${SCENES.length} scenes, ${TRANS.length} transitions, total ${TOTAL}s; act swells @ ${ACT_STARTS.join(", ")}s`);
