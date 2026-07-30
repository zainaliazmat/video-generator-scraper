#!/usr/bin/env node
// build.mjs — emits index.html from storyboard.mjs + audio_meta.json + audio_request.json.
// Contract-safe: <video> clips are DIRECT children of root (the framework owns
// their playback; nesting them inside timed sections freezes them). Sections
// carry only chrome (frames, chips, cards). Videos alternate tracks 5/6 so
// crossfading neighbors never collide on one track.
// Draft-3 design system (creator audit-2, ref: SaasCendx Pinterest videos):
// BRIGHT white/pastel gradient background (no grain, no vignette, no black),
// floating white panels with soft blue-tinted shadows, kinetic word-by-word
// text (every .big/.sub/.rail-line word scales in staggered, accent words
// glow), chips split on "·" and pop one by one, SFX per scene kind.
// Re-run after any storyboard/audio change:  node build.mjs
import { readFileSync, writeFileSync } from "node:fs";
import { beats } from "./storyboard.mjs";

const meta = JSON.parse(readFileSync("./audio_meta.json", "utf8"));
const req = JSON.parse(readFileSync("./audio_request.json", "utf8"));
const voById = Object.fromEntries(meta.voices.map((v) => [v.id, v]));
const textById = Object.fromEntries(req.lines.map((l) => [l.id, l.text]));

const FPS = 30, XFADE = 0.6, PRE = 0.5, PAD = 0.7, FADE = 0.5;
const r2 = (x) => Math.round(x * 100) / 100;

// ---- geometry: media never full-bleed (60% rule) ----
// screen panel, right side; left rail 96..600 holds the kinetic chip text
const SF = { w: 1152, h: 648, x: 672, y: 216, r: 16 };
// artifact/image panel, centered
const AF = { w: 1152, h: 648, x: 384, y: 186, r: 20 };
// artifact panel, hook variant (left) — icons live on the right
const AL = { x: 96, y: 186 };
// phone, right side
const PH = { h: 780, w: r2(780 * 384 / 832), r: 40, x: 1270, y: 140 };

let t = 0.5, track = 1, vtrack = 5;
const scenes = [], videos = [], audios = [], sfx = [], caps = [], missing = [];
const extraCss = [], extraTl = [];

const railHtml = (chip) => {
  // split chip on separators into stacked kinetic lines; first line amber
  const parts = chip.split(/\s*[—·]\s*/).filter(Boolean);
  return `<div class="rail"><div class="rail-bar"></div>${parts
    .map((p, i) => `<div class="rail-line${i === 0 ? " amber" : ""}">${p}</div>`)
    .join("")}</div>`;
};
// chips split on "·" so each point pops on screen one by one
const badgeHtml = (chip) => `<div class="badgerow">${chip
  .split(/\s*·\s*/).filter(Boolean)
  .map((p) => `<span class="chip">${p}</span>`).join("")}</div>`;

for (const [bi, b] of beats.entries()) {
  const vo = b.vo ? voById[b.vo] : null;
  if (b.vo && !vo) { missing.push(b.vo); continue; }
  const pre = b.pre ?? PRE, pad = b.pad ?? PAD;
  const dur = vo ? pre + vo.duration_s + pad : (b.dur ?? 4);
  const start = t;
  if (vo) {
    audios.push({ id: b.vo, src: vo.path, start: r2(start + pre), dur: r2(vo.duration_s) });
    // ---- captions: chunk the line text across its duration ----
    const words = (textById[b.vo] ?? "").split(/\s+/).filter(Boolean);
    if (words.length) {
      const chunks = [];
      for (let i = 0; i < words.length; i += 6) chunks.push(words.slice(i, i + 6));
      if (chunks.length > 1 && chunks[chunks.length - 1].length < 3)
        chunks[chunks.length - 2].push(...chunks.pop());
      let cum = 0;
      chunks.forEach((c, ci) => {
        const cs = start + pre + (cum / words.length) * vo.duration_s;
        const cd = (c.length / words.length) * vo.duration_s;
        cum += c.length;
        caps.push({ id: `cap-${b.vo}-${ci}`, start: r2(cs), dur: r2(cd + 0.08), text: c.join(" ") });
      });
    }
  }

  const vis = b.visuals ?? [];
  const fsum = vis.reduce((a, v) => a + (v.frac ?? 1 / vis.length), 0);
  let vt = start;
  vis.forEach((v, vi) => {
    const share = (v.frac ?? 1 / vis.length) / fsum;
    const vdur = dur * share + (vi < vis.length - 1 ? XFADE : 0);
    const id = `b${String(bi + 1).padStart(2, "0")}v${vi}`;
    const s = { id, start: r2(vt), dur: r2(vdur), track: (track = track === 1 ? 2 : 1),
                kind: v.v, anim: v.anim ?? "fade", chrome: "" };

    if (v.v === "screen" || v.v === "phone" || v.v === "artifact") {
      const vid = { id: `${id}-vid`, src: v.src, start: s.start, dur: s.dur,
                    track: (vtrack = vtrack === 5 ? 6 : 5), kind: v.v };
      videos.push(vid);
      if (v.v === "screen") s.chrome = `<div class="frame-ring sf"></div>`;
      if (v.v === "phone")  s.chrome = `<div class="phone-bezel"><div class="notch"></div></div>`;
      if (v.v === "artifact" && v.pos === "left")
        extraCss.push(`#${vid.id}{left:${AL.x}px;top:${AL.y}px}`);
      // kinetic rail (screens + phone) vs top badge (artifact)
      if (v.chip) s.chrome += (v.v === "artifact") ? badgeHtml(v.chip) : railHtml(v.chip);
      // per-scene zoom into the recording. Videos are root-level (framework
      // contract), so a plain scale overflows the panel — a clip-path inset
      // must track the scale to keep the zoom inside the panel bounds. The
      // required inset is NONLINEAR in scale, so a single clip tween lags the
      // transform and the video leaks outside the panel mid-zoom; instead the
      // clip follows dense keyframes sampled along the exact eased curve.
      // Callback-free on purpose: the renderer seeks with suppressEvents=true,
      // so an onUpdate-based clip would never run in the final render.
      if (v.zoom) {
        const z = v.zoom;
        const [ox, oy] = (z.origin ?? "50% 50%").split(/\s+/).map((p) => parseFloat(p) / 100);
        const sc = z.scale, tx = z.x ?? 0, ty = z.y ?? 0, D = z.dur ?? 1.3;
        const easeIO = (u) => (u < 0.5 ? 4 * u ** 3 : 1 - 4 * (1 - u) ** 3); // power2.inOut (gsap power2 = cubic)
        const pc = (x) => r2(Math.max(0, x) * 100);
        const clipAt = (p) => {
          const s = 1 + (sc - 1) * p, x = tx * p, y = ty * p;
          const L = pc((-ox * (1 - s) - x / SF.w) / s), R = pc(1 - (1 - ox * (1 - s) - x / SF.w) / s);
          const T = pc((-oy * (1 - s) - y / SF.h) / s), B = pc(1 - (1 - oy * (1 - s) - y / SF.h) / s);
          return `inset(${T}% ${R}% ${B}% ${L}% round ${r2(SF.r / s)}px)`;
        };
        const N = 24; // ponytail: chord error ≈1-2px, hidden under the 10px frame ring
        const kf = Array.from({ length: N }, (_, i) => ({ clipPath: clipAt(easeIO((i + 1) / N)), duration: D / N, ease: "none" }));
        const props = { scale: sc, transformOrigin: z.origin ?? "50% 50%", duration: D, ease: "power2.inOut" };
        if (z.x != null) props.x = z.x;
        if (z.y != null) props.y = z.y;
        const at = r2(s.start + (z.at ?? 0.5));
        extraTl.push(`tl.fromTo("#${vid.id}",{scale:1,x:0,y:0},${JSON.stringify(props)},${at});`);
        extraTl.push(`tl.set("#${vid.id}",{clipPath:${JSON.stringify(clipAt(0))}},${at});`);
        extraTl.push(`tl.to("#${vid.id}",{keyframes:${JSON.stringify(kf)}},${at});`);
        s.noDrift = true;
      }
      // pinterest highlight brackets after the zoom lands
      if (v.brackets) {
        s.chrome += `<div class="brackets" id="${id}-brk"><i></i><i></i><i></i><i></i><span class="brk-tag">THE REFERENCE</span></div>`;
        const at = r2(s.start + (v.zoom?.at ?? 0.5) + (v.zoom?.dur ?? 1.3) + 0.15);
        extraTl.push(`tl.fromTo("#${id}-brk",{opacity:0,scale:1.12},{opacity:1,scale:1,duration:.45,ease:"back.out(1.8)"},${at});`);
        extraTl.push(`tl.to("#${id}-brk",{scale:1.03,duration:1.1,ease:"sine.inOut",repeat:3,yoyo:true},${r2(at + 0.5)});`);
      }
    } else if (v.v === "image") {
      s.chrome = `<div class="imgpanel"><img class="fullimg" src="${v.src}">${v.ring ? `<div class="flaw-ring"></div>` : ""}</div>`;
      if (v.chip) s.chrome += badgeHtml(v.chip);
    } else {
      s.chrome = v.html ?? "";
      if (v.chip) s.chrome += badgeHtml(v.chip);
    }
    scenes.push(s);
    // ---- SFX by scene kind: whoosh = media slides in, pop = card words,
    // boom = slam. Media whooshes alternate two variants to avoid fatigue. ----
    if (s.anim === "slam")
      sfx.push({ src: "assets/sfx/boom.wav", start: Math.max(0, r2(s.start - 0.05)), dur: 2.5, vol: 0.5 });
    else if (["screen", "phone", "artifact", "image"].includes(s.kind))
      sfx.push({ src: `assets/sfx/whoosh${scenes.length % 2 ? "" : "2"}.wav`, start: Math.max(0, r2(s.start - 0.1)), dur: 1.0, vol: 0.2 });
    else
      sfx.push({ src: "assets/sfx/pop.wav", start: r2(s.start + 0.15), dur: 0.6, vol: s.anim === "pop" ? 0.3 : 0.22 });
    // ---- kinetic-type ticks: one tick per popping element, timed to the GSAP
    // staggers in the kin block below (cap 8/scene so busy cards don't rattle) ----
    const tick = (n, at, stag, vol) => {
      for (let i = 0; i < Math.min(n, 8); i++)
        sfx.push({ src: "assets/sfx/tick.wav", start: r2(s.start + at + i * stag), dur: 0.32, vol });
    };
    const bigTxt = (s.chrome.match(/class="big"[^>]*>([\s\S]*?)<\/div>/) || [])[1];
    if (bigTxt) tick(bigTxt.replace(/<[^>]+>/g, " ").trim().split(/\s+/).length, 0.1, 0.13, 0.14);
    const nChips = (s.chrome.match(/class="chip"/g) || []).length;
    if (nChips) tick(nChips, 0.35, 0.16, 0.12);
    const nPipe = ((s.chrome.match(/class="(?:pipe|years)"[^>]*>([\s\S]*?)<\/div>/) || [""])[0].match(/<span/g) || []).length;
    if (nPipe) tick(nPipe, 0.2, 0.14, 0.12);
    const nCards = (s.chrome.match(/class="tcard/g) || []).length;
    if (nCards) for (let i = 0; i < nCards; i++)
      sfx.push({ src: "assets/sfx/pop.wav", start: r2(s.start + 0.3 + i * 0.5), dur: 0.6, vol: 0.22 });
    vt += vdur - (vi < vis.length - 1 ? XFADE : 0);
  });
  t = start + dur - XFADE;
}
const TOTAL = Math.ceil(t + XFADE + 1);
if (missing.length) console.warn("⚠ missing VO ids (beats skipped):", missing.join(","));

// ---- hook icon overlay (Claude vs Premiere vs DaVinci) across b01v0+v1 ----
const hookA = scenes.find((s) => s.id === "b01v0"), hookB = scenes.find((s) => s.id === "b01v1");
let iconHtml = "", iconTl = "";
if (hookA && hookB) {
  const io = r2(hookA.start + 0.4), iend = r2(hookB.start + hookB.dur - 0.4);
  iconHtml = `
      <div id="ov-icons" class="scene clip" data-start="${io}" data-duration="${r2(iend - io)}" data-track-index="9">
        <div class="icons">
          <div class="icon-tile" id="ic-claude"><svg viewBox="0 0 24 24"><path fill="#fff" d="M12 2 L13.8 8.2 L20 6 L15.6 11 L22 12 L15.6 13 L20 18 L13.8 15.8 L12 22 L10.2 15.8 L4 18 L8.4 13 L2 12 L8.4 11 L4 6 L10.2 8.2 Z"/></svg><span>CLAUDE</span></div>
          <div class="icon-tile pr" id="ic-pr"><b>Pr</b><span>PREMIERE</span><i class="strike"></i></div>
          <div class="icon-tile dv" id="ic-dv"><div class="dv-ring"><div class="dv-core"></div></div><span>DAVINCI</span><i class="strike"></i></div>
        </div>
      </div>`;
  iconTl = `
      tl.fromTo("#ov-icons",{opacity:0},{opacity:1,duration:.4},${io});
      tl.fromTo("#ic-claude",{x:120,opacity:0},{x:0,opacity:1,duration:.5,ease:"back.out(1.6)"},${r2(io + 0.5)});
      tl.fromTo("#ic-pr",{x:120,opacity:0},{x:0,opacity:1,duration:.5,ease:"back.out(1.6)"},${r2(io + 0.8)});
      tl.fromTo("#ic-dv",{x:120,opacity:0},{x:0,opacity:1,duration:.5,ease:"back.out(1.6)"},${r2(io + 1.1)});
      tl.fromTo("#ic-pr .strike",{scaleX:0},{scaleX:1,duration:.3,ease:"power3.in"},${r2(io + 5.0)});
      tl.to("#ic-pr",{opacity:.45,duration:.3},${r2(io + 5.1)});
      tl.fromTo("#ic-dv .strike",{scaleX:0},{scaleX:1,duration:.3,ease:"power3.in"},${r2(io + 6.2)});
      tl.to("#ic-dv",{opacity:.45,duration:.3},${r2(io + 6.3)});
      tl.to("#ic-claude",{boxShadow:"0 0 70px rgba(217,119,87,.65)",scale:1.06,duration:.5,ease:"sine.inOut"},${r2(io + 3.2)});
      tl.to("#ic-claude",{scale:1,duration:2.2,ease:"sine.inOut",repeat:${Math.max(1, Math.floor((iend - io) / 2.2))},yoyo:true},${r2(io + 3.7)});
      tl.to("#ov-icons",{opacity:0,duration:.4},${r2(iend - 0.4)});`;
  sfx.push({ src: "assets/sfx/pop.wav", start: r2(io + 5.0), dur: 0.6, vol: 0.28 });
  sfx.push({ src: "assets/sfx/pop.wav", start: r2(io + 6.2), dur: 0.6, vol: 0.28 });
  sfx.push({ src: "assets/sfx/shimmer.wav", start: r2(io + 3.2), dur: 2.0, vol: 0.22 });
}

// ---- outro overlay: channel logo + SUBSCRIBE over the last scene ----
const last = scenes[scenes.length - 1];
let outroHtml = "", outroTl = "";
if (last) {
  const os = r2(last.start + 1.2), oe = r2(last.start + last.dur);
  outroHtml = `
      <div id="ov-outro" class="scene clip" data-start="${os}" data-duration="${r2(oe - os)}" data-track-index="9">
        <div class="outro"><img src="assets/images/brand/logo-transparent.png" class="outro-logo"><span class="sub-pill">SUBSCRIBE</span></div>
      </div>`;
  outroTl = `
      tl.fromTo("#ov-outro",{opacity:0},{opacity:1,duration:.3},${os});
      tl.fromTo(".outro-logo",{scale:.2,opacity:0,rotation:-12},{scale:1,opacity:1,rotation:0,duration:.6,ease:"back.out(2)"},${r2(os + 0.2)});
      tl.fromTo(".sub-pill",{scale:.3,opacity:0,y:20},{scale:1,opacity:1,y:0,duration:.5,ease:"back.out(2.2)"},${r2(os + 0.7)});
      tl.to(".sub-pill",{scale:1.06,duration:.9,ease:"sine.inOut",yoyo:true,repeat:${Math.max(1, Math.floor((oe - os - 1.6) / 0.9))}},${r2(os + 1.3)});`;
  sfx.push({ src: "assets/sfx/pop.wav", start: r2(os + 0.7), dur: 0.6, vol: 0.3 });
}

const sceneHtml = scenes.map((s) =>
  `      <section id="${s.id}" class="scene clip" data-start="${s.start}" data-duration="${s.dur}" data-track-index="${s.track}">
        <div class="scene-inner" id="${s.id}-inner">${s.chrome}</div>
      </section>`).join("\n\n");

const videoHtml = videos.map((v) =>
  `      <video id="${v.id}" class="clip vid-${v.kind}" src="${v.src}" muted data-start="${v.start}" data-duration="${v.dur}" data-track-index="${v.track}"></video>`).join("\n");

const capHtml = caps.map((c) =>
  `      <section id="${c.id}" class="scene clip capline" data-start="${c.start}" data-duration="${c.dur}" data-track-index="12"><span class="cap">${c.text}</span></section>`).join("\n");

const voHtml = audios.map((a) =>
  `      <audio id="vo-${a.id}" src="${a.src}" data-start="${a.start}" data-duration="${a.dur}" data-track-index="31" data-volume="1"></audio>`).join("\n");

// ticks get their own track band (36-41), round-robined in TIME order —
// push order interleaves stagger groups, so index-based rotation collided
sfx.filter((x) => x.src.includes("tick")).sort((a, b) => a.start - b.start)
  .forEach((x, i) => { x.trk = 36 + (i % 6); });
const sfxHtml = sfx.map((x, i) =>
  `      <audio id="sfx-${i}" src="${x.src}" data-start="${x.start}" data-duration="${x.dur}" data-track-index="${x.trk ?? 32 + (i % 4)}" data-volume="${x.vol}"></audio>`).join("\n");

// GSAP: fade scene chrome AND its video together
const vidBySection = Object.fromEntries(videos.map((v) => [v.id.replace(/-vid$/, ""), v.id]));
const tlLines = scenes.map((s) => {
  const targets = [`#${s.id}-inner`, vidBySection[s.id] ? `#${vidBySection[s.id]}` : null].filter(Boolean);
  const sel = targets.join(",");
  const isCard = s.chrome.includes('class="card"');
  const enter =
    s.anim === "slam" ? `tl.fromTo("${sel}",{opacity:0,scale:1.45},{opacity:1,scale:1,duration:.4,ease:"back.out(2)"},${s.start});`
  // cards enter with a plain fade — the kinetic word stagger below is the show
  : isCard              ? `tl.fromTo("${sel}",{opacity:0},{opacity:1,duration:.3,ease:"power1.out"},${s.start});`
  : s.anim === "pop"  ? `tl.fromTo("${sel}",{opacity:0,y:26,scale:.97},{opacity:1,y:0,scale:1,duration:.55,ease:"back.out(1.6)"},${s.start});`
  : s.kind === "screen"   ? `tl.fromTo("${sel}",{opacity:0,x:90},{opacity:1,x:0,duration:.6,ease:"power3.out"},${s.start});`
  : s.kind === "phone"    ? `tl.fromTo("${sel}",{opacity:0,y:70},{opacity:1,y:0,duration:.6,ease:"power3.out"},${s.start});`
  : s.kind === "artifact" ? `tl.fromTo("${sel}",{opacity:0,scale:1.07},{opacity:1,scale:1,duration:.7,ease:"power2.out"},${s.start});`
  : s.kind === "image"    ? `tl.fromTo("${sel}",{opacity:0,scale:1.05},{opacity:1,scale:1,duration:.6,ease:"power2.out"},${s.start});`
  :                     `tl.fromTo("${sel}",{opacity:0,y:18},{opacity:1,y:0,duration:${FADE},ease:"power1.out"},${s.start});`;
  const exit = `tl.to("${sel}",{opacity:0,duration:${FADE},ease:"power1.in"},${r2(s.start + s.dur - FADE)});`;
  const drift = (s.kind === "screen" && !s.noDrift)
    ? `tl.fromTo("#${vidBySection[s.id]}",{scale:1},{scale:1.015,duration:${r2(s.dur)},ease:"sine.inOut"},${s.start});`
    : "";
  // ---- kinetic type: words scale in one by one (ref: SaasCendx pindown) ----
  const kin = [];
  if (s.chrome.includes('class="big"'))
    kin.push(`tl.fromTo("#${s.id}-inner .big .kw",{opacity:0,scale:.3,y:30},{opacity:1,scale:1,y:0,duration:.55,stagger:.13,ease:"back.out(2.4)"},${r2(s.start + 0.1)});`);
  if (s.chrome.includes('class="sub"'))
    kin.push(`tl.fromTo("#${s.id}-inner .sub .kw",{opacity:0,scale:.55,y:16},{opacity:1,scale:1,y:0,duration:.4,stagger:.055,ease:"back.out(1.8)"},${r2(s.start + 0.6)});`);
  if (s.chrome.includes('class="rail"'))
    kin.push(`tl.fromTo("#${s.id}-inner .rail .kw",{opacity:0,scale:.4,y:16},{opacity:1,scale:1,y:0,duration:.45,stagger:.07,ease:"back.out(2.2)"},${r2(s.start + 0.3)});
      tl.fromTo("#${s.id}-inner .rail-bar",{scaleY:0},{scaleY:1,duration:.6,ease:"power3.out",transformOrigin:"top"},${r2(s.start + 0.15)});`);
  if (s.chrome.includes('class="tline"'))
    kin.push(`tl.fromTo("#${s.id}-inner .tcard",{opacity:0,scale:.2,y:70},{opacity:1,scale:1,y:0,duration:.6,stagger:.5,ease:"back.out(1.9)"},${r2(s.start + 0.3)});
      tl.to("#${s.id}-inner .tcard",{y:-10,duration:1.7,ease:"sine.inOut",yoyo:true,repeat:${Math.max(1, Math.floor(Math.max(0, s.dur - 4.5) / 1.7))},stagger:.28},${r2(s.start + 3.8)});`);
  if (s.chrome.includes('class="pipe"') || s.chrome.includes('class="years"'))
    kin.push(`tl.fromTo("#${s.id}-inner .pipe span,#${s.id}-inner .years span",{opacity:0,scale:.3,y:24},{opacity:1,scale:1,y:0,duration:.5,stagger:.14,ease:"back.out(2.2)"},${r2(s.start + 0.2)});`);
  if (s.chrome.includes('class="badgerow"'))
    kin.push(`tl.fromTo("#${s.id}-inner .badgerow .chip",{opacity:0,scale:.4,y:-16},{opacity:1,scale:1,y:0,duration:.45,stagger:.16,ease:"back.out(2.2)"},${r2(s.start + 0.35)});`);
  return [enter, exit, drift, ...kin].filter(Boolean).join("\n      ");
}).join("\n      ");

const capTl = caps.map((c) =>
  `tl.fromTo("#${c.id}",{opacity:0,y:14},{opacity:1,y:0,duration:.22,ease:"power2.out"},${c.start});tl.to("#${c.id}",{opacity:0,duration:.18},${r2(c.start + c.dur - 0.18)});`
).join("\n      ");

const html = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080">
    <title>Claude Code Just Edited This Entire Video</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=JetBrains+Mono:wght@400;600&display=block">
    <style>
      :root{--bg:#f6f8fd;--ink:#101623;--ink-soft:rgba(16,22,35,.62);--amber:#cf5a2e;--red:#d23b26;--green:#12855c;--panel:#ffffff;--line:rgba(16,22,35,.12)}
      *{margin:0;padding:0;box-sizing:border-box}
      body{background:var(--bg);color:var(--ink);width:1920px;height:1080px;overflow:hidden;font-family:"Archivo Black",system-ui,sans-serif}
      .scene{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
      .scene-inner{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0}
      .mono{font-family:"JetBrains Mono",ui-monospace,monospace}
      .amber{color:var(--amber)}.red{color:var(--red)}.green{color:var(--green)}

      /* ---- living background: bright, airy, pastel (no grain, no vignette) ---- */
      #bg{position:absolute;inset:0;background:linear-gradient(160deg,#fdfeff 0%,#f3f6fd 46%,#eef0fb 100%)}
      #bg .grid{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(16,22,35,.05) 1.5px,transparent 1.5px);background-size:56px 56px}
      .glow{position:absolute;border-radius:50%;filter:blur(100px)}
      #glow-a{width:900px;height:900px;left:-180px;top:-220px;background:radial-gradient(circle,rgba(244,160,118,.30),transparent 65%)}
      #glow-b{width:1100px;height:1100px;right:-260px;bottom:-320px;background:radial-gradient(circle,rgba(126,164,244,.32),transparent 65%)}
      #glow-c{width:800px;height:800px;left:34%;top:30%;background:radial-gradient(circle,rgba(178,150,236,.20),transparent 65%)}

      /* ---- kinetic words ---- */
      .kw{display:inline-block;font-style:normal;white-space:pre;transform-origin:50% 78%}
      .big .amber{text-shadow:0 0 36px rgba(207,90,46,.45)}
      .big .red{text-shadow:0 0 36px rgba(210,59,38,.40)}
      .big .green{text-shadow:0 0 36px rgba(18,133,92,.40)}
      .rail-line.amber .kw{text-shadow:0 0 26px rgba(207,90,46,.35)}

      /* ---- media panels (60% rule): white mat + soft shadow, ref style ---- */
      video.clip{position:absolute;opacity:0}
      .vid-artifact{left:${AF.x}px;top:${AF.y}px;width:${AF.w}px;height:${AF.h}px;object-fit:cover;border-radius:${AF.r}px;box-shadow:0 34px 90px rgba(45,65,120,.28)}
      .vid-screen{left:${SF.x}px;top:${SF.y}px;width:${SF.w}px;height:${SF.h}px;object-fit:cover;border-radius:${SF.r}px}
      .vid-phone{left:${PH.x}px;top:${PH.y}px;width:${PH.w}px;height:${PH.h}px;object-fit:cover;border-radius:${PH.r}px}
      /* scene chrome paints ABOVE root-level videos — the mat must be a hollow
         border ring, never a filled box (a background here hides the video) */
      .frame-ring{position:absolute}
      .frame-ring.sf{left:${SF.x - 10}px;top:${SF.y - 10}px;width:${SF.w + 20}px;height:${SF.h + 20}px;border-radius:${SF.r + 10}px;border:10px solid #fff;box-shadow:0 0 0 1.5px var(--line),0 34px 90px rgba(45,65,120,.28)}
      .phone-bezel{position:absolute;left:${PH.x - 12}px;top:${PH.y - 12}px;width:${PH.w + 24}px;height:${PH.h + 24}px;border-radius:${PH.r + 12}px;border:12px solid #22262e;box-shadow:0 34px 90px rgba(45,65,120,.35),inset 0 0 0 2px rgba(255,255,255,.10)}
      .notch{position:absolute;left:50%;top:10px;transform:translateX(-50%);width:120px;height:22px;border-radius:12px;background:#22262e}
      .imgpanel{position:absolute;left:${AF.x}px;top:${AF.y}px;width:${AF.w}px;height:${AF.h}px;border-radius:${AF.r}px;overflow:hidden;box-shadow:0 34px 90px rgba(45,65,120,.28);background:#fff}
      .fullimg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
      .flaw-ring{position:absolute;left:8%;top:52%;width:33%;height:16%;border:5px solid var(--red);border-radius:50%/40%;box-shadow:0 0 40px rgba(210,59,38,.35)}

      /* ---- kinetic left rail ---- */
      .rail{position:absolute;left:96px;top:0;bottom:0;width:520px;display:flex;flex-direction:column;justify-content:center;gap:18px;padding-left:34px}
      .rail-bar{position:absolute;left:0;top:50%;transform:translateY(-50%);width:6px;height:320px;border-radius:3px;background:linear-gradient(var(--amber),rgba(207,90,46,.15))}
      .rail-line{font-size:48px;line-height:1.12;letter-spacing:.01em;text-transform:uppercase;color:var(--ink)}
      .rail-line.amber{color:var(--amber)}

      /* ---- badges / chips ---- */
      .chip{display:inline-block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:24px;letter-spacing:.14em;color:var(--amber);border:1.5px solid var(--amber);border-radius:999px;padding:10px 26px;background:rgba(255,255,255,.85);box-shadow:0 10px 34px rgba(45,65,120,.14)}
      .badgerow{position:absolute;top:64px;left:0;right:0;display:flex;justify-content:center;gap:14px;flex-wrap:wrap;padding:0 120px;z-index:4}

      /* ---- captions ---- */
      .capline{align-items:flex-end;justify-content:center;opacity:0}
      .cap{margin-bottom:46px;max-width:1480px;font-family:system-ui,sans-serif;font-weight:650;font-size:37px;line-height:1.3;text-align:center;color:var(--ink);background:rgba(255,255,255,.9);padding:10px 30px;border-radius:14px;box-shadow:0 10px 40px rgba(45,65,120,.16)}

      /* ---- hook icons ---- */
      .icons{position:absolute;right:120px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:44px}
      .icon-tile{position:relative;width:240px;height:150px;border-radius:24px;background:#fff;border:1.5px solid var(--line);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;box-shadow:0 24px 70px rgba(45,65,120,.22)}
      .icon-tile svg{width:64px;height:64px}
      .icon-tile#ic-claude{background:#d97757;border-color:transparent}
      .icon-tile span{font-size:19px;letter-spacing:.18em;color:var(--ink-soft)}
      .icon-tile#ic-claude span{color:rgba(255,255,255,.92)}
      .icon-tile.pr b{font-family:system-ui,sans-serif;font-weight:800;font-size:52px;color:#d6bcfa}
      .icon-tile.pr{background:#1a0b2e}
      .icon-tile.pr span{color:rgba(255,255,255,.6)}
      .dv-ring{width:64px;height:64px;border-radius:50%;background:conic-gradient(#e74c3c,#f39c12,#f1c40f,#2ecc71,#3498db,#9b59b6,#e74c3c);display:flex;align-items:center;justify-content:center}
      .dv-core{width:34px;height:34px;border-radius:50%;background:#fff}
      .strike{position:absolute;left:8%;top:50%;width:84%;height:7px;border-radius:4px;background:var(--red);transform:rotate(-14deg);transform-origin:left center;box-shadow:0 0 24px rgba(210,59,38,.5)}

      /* ---- pinterest brackets ---- */
      .brackets{position:absolute;left:${SF.x + 110}px;top:${SF.y + 140}px;width:640px;height:385px;opacity:0}
      .brackets i{position:absolute;width:56px;height:56px;border:6px solid var(--amber);border-radius:4px}
      .brackets i:nth-child(1){left:-6px;top:-6px;border-right:none;border-bottom:none}
      .brackets i:nth-child(2){right:-6px;top:-6px;border-left:none;border-bottom:none}
      .brackets i:nth-child(3){left:-6px;bottom:-6px;border-right:none;border-top:none}
      .brackets i:nth-child(4){right:-6px;bottom:-6px;border-left:none;border-top:none}
      .brk-tag{position:absolute;left:0;top:-56px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:24px;letter-spacing:.2em;color:var(--amber)}

      /* ---- cards ---- */
      .card{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;text-align:center;max-width:1480px;padding:0 80px}
      .big{font-size:92px;line-height:1.14;letter-spacing:-.01em}
      .sub{font-size:33px;color:var(--ink-soft);font-family:"JetBrains Mono",ui-monospace,monospace;line-height:1.5;max-width:1200px}
      .stamp{font-size:120px;color:var(--red);border:6px solid var(--red);padding:30px 70px;transform:rotate(-4deg);letter-spacing:.04em;text-transform:uppercase;border-radius:10px;background:rgba(255,255,255,.7);box-shadow:0 0 0 6px rgba(210,59,38,.14),0 30px 80px rgba(45,65,120,.2)}
      .bars{display:flex;gap:8px;align-items:flex-end;height:110px;justify-content:center}
      .bars i{display:block;width:14px;background:var(--amber);border-radius:4px}
      ${Array.from({ length: 24 }, (_, i) => `.bars i:nth-child(${i + 1}){height:${18 + Math.abs(((i * 37) % 89) - 44)}px;opacity:${i % 3 === 0 ? ".95" : ".65"}}`).join("")}
      .years{display:flex;gap:44px;font-size:74px}
      .years span:nth-child(odd){color:var(--amber)}
      /* ---- year timeline: polaroid cards pop over each year ---- */
      .tline{display:flex;gap:22px;align-items:flex-end}
      .tcard{display:flex;flex-direction:column;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:12px 12px 10px;box-shadow:0 18px 50px rgba(45,65,120,.20)}
      .tcard:nth-child(odd){transform:rotate(-2deg)}
      .tcard:nth-child(even){transform:rotate(2deg)}
      .tcard img{width:200px;height:130px;object-fit:cover;border-radius:10px}
      .tyear{font-size:40px}
      /* ---- outro: channel logo + subscribe ---- */
      .outro{position:absolute;right:110px;bottom:130px;display:flex;align-items:center;gap:26px;background:rgba(255,255,255,.92);border-radius:24px;padding:14px 32px;box-shadow:0 24px 70px rgba(45,65,120,.25)}
      .outro-logo{width:110px;height:110px;object-fit:contain}
      .sub-pill{font-size:34px;letter-spacing:.08em;color:#fff;background:#e11d2e;border-radius:14px;padding:16px 30px}
      .pipe{display:flex;flex-wrap:wrap;gap:26px;justify-content:center;max-width:1500px}
      .pipe span{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:34px;border:1.5px solid var(--line);border-radius:12px;padding:20px 34px;background:var(--panel);color:var(--ink);box-shadow:0 14px 44px rgba(45,65,120,.14)}
      .pipe span.amber{border-color:var(--amber);color:var(--amber)}
      ${extraCss.join("\n      ")}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="${TOTAL}" data-fps="${FPS}">

      <div id="bg" class="scene clip" data-start="0" data-duration="${TOTAL}" data-track-index="1">
        <div class="glow" id="glow-a"></div>
        <div class="glow" id="glow-b"></div>
        <div class="glow" id="glow-c"></div>
        <div class="grid"></div>
      </div>

${videoHtml}

${sceneHtml}
${iconHtml}
${outroHtml}

${capHtml}

${voHtml}

${sfxHtml}
    </div>

    <script>
      // split every .big/.sub/.rail-line text node into .kw word spans so the
      // timeline can scale words in one by one (skips .bars <i> elements).
      const kSplit = (el) => {
        [...el.childNodes].forEach((n) => {
          if (n.nodeType === 3) {
            const frag = document.createDocumentFragment();
            n.textContent.split(/(\\s+)/).forEach((part) => {
              if (!part) return;
              if (/^\\s+$/.test(part)) frag.appendChild(document.createTextNode(part));
              else { const w = document.createElement("i"); w.className = "kw"; w.textContent = part; frag.appendChild(w); }
            });
            el.replaceChild(frag, n);
          } else if (n.nodeType === 1 && !["kw", "bars", "pipe", "years"].some((c) => n.classList.contains(c))) kSplit(n);
        });
      };
      document.querySelectorAll(".scene-inner .big,.scene-inner .sub,.scene-inner .rail-line").forEach(kSplit);

      window.__timelines = window.__timelines || {};
      const tl = gsap.timeline({ paused: true });
      tl.to("#glow-a",{x:260,y:140,scale:1.18,duration:22,ease:"sine.inOut",repeat:${Math.ceil(TOTAL / 22)},yoyo:true},0);
      tl.to("#glow-b",{x:-240,y:-160,scale:1.14,duration:26,ease:"sine.inOut",repeat:${Math.ceil(TOTAL / 26)},yoyo:true},0);
      tl.to("#glow-c",{x:180,y:-120,scale:1.2,duration:24,ease:"sine.inOut",repeat:${Math.ceil(TOTAL / 24)},yoyo:true},0);
      ${tlLines}
      ${extraTl.join("\n      ")}
      ${iconTl}
      ${outroTl}
      ${capTl}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
`;
writeFileSync("./index.html", html);
writeFileSync("./timing.txt",
  scenes.map((s) => `${s.id}  ${s.start}s +${s.dur}s  t${s.track} ${s.kind}`).join("\n") +
  `\n\nTOTAL ${TOTAL}s (${Math.floor(TOTAL / 60)}:${String(TOTAL % 60).padStart(2, "0")}) · ${audios.length} VO · ${videos.length} videos · ${caps.length} captions · ${sfx.length} sfx\n`);
console.log(`index.html · ${scenes.length} scenes · ${videos.length} videos · ${audios.length} VO · ${caps.length} captions · ${sfx.length} sfx · total ${TOTAL}s (${Math.floor(TOTAL / 60)}:${String(TOTAL % 60).padStart(2, "0")})`);
