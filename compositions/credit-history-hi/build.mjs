// Generates index.html. The four homes of every timing number — <section> attrs,
// the JS `S` map, the <audio> rows and the root data-duration — are ALL derived
// here from assets/voice/timing.json, so they cannot drift apart.
//   node build.mjs
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const DIR = path.dirname(fileURLToPath(import.meta.url));
const T = JSON.parse(fs.readFileSync(path.join(DIR, "assets/voice/timing.json"), "utf8"));
const L = T.lines;
const n = (v) => String(Number(v.toFixed(3)));
// timing.json rounds scene_start and scene_duration independently, so start+dur
// can land 1ms past the next start and the linter calls it an overlapping clip.
// Starts are authoritative (the audio rows key off them); durations butt-join.
const dur = (i) => (i + 1 < L.length ? L[i + 1].scene_start : T.total) - L[i].scene_start;

// ---------------------------------------------------------------- s7 math
// Displayed, never spoken. EMI = P·i·(1+i)^n / ((1+i)^n − 1),
// P = ₹30,00,000, n = 240, spread Δ = 0.75 and 1.00 percentage points off a
// 7.40% top-band card. Audit re-derived both ends by hand; do not hard-code.
const INR = new Intl.NumberFormat("en-IN");
const emi = (rate, P = 3000000, months = 240) => {
  const i = rate / 1200;
  return (P * i * Math.pow(1 + i, months)) / (Math.pow(1 + i, months) - 1);
};
const BASE = 7.4;
const dMoLo = emi(BASE + 0.75) - emi(BASE);
const dMoHi = emi(BASE + 1.0) - emi(BASE);
const M = {
  principal: INR.format(3000000),
  moLo: INR.format(Math.round(dMoLo / 10) * 10),
  moHi: INR.format(Math.round(dMoHi / 10) * 10),
  intLo: (dMoLo * 240 / 100000).toFixed(1),
  intHi: (dMoHi * 240 / 100000).toFixed(1),
};

// ---------------------------------------------------------------- scenes
const TINT = {
  s1: "rgba(239, 68, 68, 0.12)", s2: "rgba(245, 158, 11, 0.10)", s3: "rgba(245, 158, 11, 0.12)",
  s4: "rgba(34, 197, 94, 0.10)", s5: "rgba(239, 68, 68, 0.13)", s6: "rgba(34, 197, 94, 0.10)",
  s7: "rgba(239, 68, 68, 0.12)", s8: "rgba(255, 92, 57, 0.12)", s9: "rgba(34, 197, 94, 0.13)",
};
// cut-in overlays: full-bleed .bg layers that fade over the scene photo.
// s3/s4/s6/s7 have none — their scene .bg carries the frame alone. s7's asked for
// a house key and the delivered file was a CAR fob under "SAME HOUSE"; the blueprint
// is the right plate. Do not re-add a cut-in here without looking at the JPG.
const CUTS = {
  s1: ["s1cutA:s1-cutA.jpg", "s1cutB:s1-cutB.jpg"], s5: ["s5cut:s5-cut.jpg"],
  s8: ["s8cut:s8-cut.jpg"],
};
const arr = '<i class="arr"></i>';
const cells = Array.from({ length: 36 }, (_, i) =>
  `<i class="cell${i === 13 ? " miss" : ""}"></i>`).join("");

const BODY = {
  s1: `<div class="stack">
          <p id="s1k" class="kicker">A file you've never seen</p>
          <h1 id="s1q" class="huge targetc">YOUR CREDIT REPORT</h1>
          <div id="s1d1" class="decision">LOAN? ${arr} <span class="targetc">it decides</span></div>
          <div id="s1d2" class="decision">INTEREST? ${arr} <span class="targetc">it decides</span></div>
          <div id="s1d3" class="decision">YOU'VE SEEN IT? ${arr} <span class="mutedc">probably never</span></div>
          <div id="s1stamp" class="stamp warn">EVERY MISSED EMI IS IN IT</div>
        </div>`,
  s2: `<div class="stack">
          <p id="s2k" class="kicker">By the end you'll know</p>
          <div class="row">
            <div id="s2a" class="chip">WHAT THE REPORT IS</div>
            <div id="s2b" class="chip">WHAT BUILDS IT</div>
          </div>
          <div id="s2row2" class="row">
            <div id="s2c" class="chip">WHAT DESTROYS IT</div>
            <div id="s2d" class="chip">WHY IT MATTERS EARLY</div>
          </div>
          <p id="s2sub" class="sub">Then two things to do today</p>
        </div>`,
  // two grid-pinned stacks: phase A fully exits before the scale focal enters,
  // so each self-centres and the exit leaves no reserved hole.
  s3: `<div class="stack" style="grid-area: 1 / 1">
          <p id="s3k" class="kicker">First &mdash; what it actually is</p>
          <div class="row">
            <div id="s3e1" class="chip">EVERY LOAN</div>
            <div id="s3e2" class="chip">EVERY CREDIT CARD</div>
            <div id="s3e3" class="chip">EVERY EMI</div>
          </div>
          <p id="s3rec" class="sub">${arr} recorded at the credit bureau</p>
          <p id="s3ha" class="head2">THE REPORT = <span class="mutedc">the record</span></p>
          <p id="s3hb" class="head2">THE SCORE = <span class="mutedc">the summary</span></p>
        </div>
        <div class="stack" style="grid-area: 1 / 1">
          <div id="s3scale" class="row">
            <span class="mega">300</span>
            <div class="track2"><div id="s3fill" class="fill2"></div></div>
            <span class="mega">900</span>
          </div>
          <div class="row" style="gap: 90px">
            <p id="s3g1" class="collabel fundc">700+ = GENERALLY GOOD</p>
            <p id="s3g2" class="collabel fundc">750+ = BEST PRICING</p>
          </div>
          <p id="s3f" class="foot">TransUnion CIBIL &mdash; score range 300 to 900</p>
        </div>`,
  // Ranked by POSITION only. No percentage weight, no proportional bar — CIBIL
  // publishes no weights, and unequal row lengths would smuggle FICO's back in.
  s4: `<div class="stack">
          <p id="s4k" class="kicker">What builds it</p>
          <div class="bill">
            <div id="s4r1" class="billrow fund"><span><b class="rank">1</b> PAYMENT HISTORY</span><span class="gloss">every EMI, on time</span></div>
            <div id="s4r2" class="billrow fund"><span><b class="rank">2</b> CREDIT UTILISATION</span><span class="gloss">how much of the limit you use</span></div>
            <div id="s4r3" class="billrow fund"><span><b class="rank">3</b> AGE OF CREDIT</span><span class="gloss">how old your accounts are</span></div>
            <div id="s4r4" class="billrow fund"><span><b class="rank">4</b> NEW ENQUIRIES</span><span class="gloss">how often you apply</span></div>
          </div>
          <p id="s4f" class="foot">CIBIL names these factors &mdash; it publishes no percentage weights. Also counted: credit mix.</p>
        </div>`,
  s5: `<div class="stack">
          <p id="s5k" class="kicker">What destroys it</p>
          <div id="s5grid">${cells}</div>
          <p id="s5ctr" class="counter warn">MONTH <span id="s5num">1</span> OF 36</p>
          <p id="s5f" class="foot">CIBIL &mdash; 36-month month-by-month payment history; it will always be a part of your credit history</p>
          <h1 id="s5q" class="huge warn">ONE MISS = 36 MONTHS</h1>
        </div>`,
  s6: `<div class="stack" style="grid-area: 1 / 1">
          <p id="s6k" class="kicker">The fix</p>
          <h1 id="s6h" class="huge fundc">AUTO-PAY<span class="subline">every due date</span></h1>
          <div id="s6flow" class="row">
            <div class="fnode chip fund">EVERY CARD</div>
            <span class="arrow fx"></span>
            <div class="fnode chip fund">EVERY LOAN</div>
            <span class="arrow fx"></span>
            <div class="fnode chip fund">AUTO-DEBIT or ALERT</div>
          </div>
          <div id="s6stamp" class="stamp fund">REMEMBERING SHOULDN'T BE YOUR JOB</div>
        </div>
        <div class="stack" style="grid-area: 1 / 1">
          <p id="s6u" class="sub">Use a <span class="fundc">SMALL</span> share of the limit</p>
          <div id="s6u2" class="decision">PAY THE <span class="fundc">FULL</span> BILL ${arr} <span class="mutedc">not the minimum</span></div>
        </div>`,
  // No bank named, no rate shown — only the spread. Figures are calculator output.
  s7: `<div id="s7stack" class="stack" style="gap: 22px">
          <p id="s7k" class="kicker">Now the math &mdash; what a low score costs</p>
          <div id="s7band1" class="decision">TOP SCORE BAND ${arr} <span class="verdict v-keep">the bank's best price</span></div>
          <p id="s7setup" class="sub">SAME LOAN &middot; SAME BANK</p>
          <div id="s7band2" class="decision">BELOW-700 BAND ${arr} <span class="verdict v-cancel">~1 percentage point higher</span></div>
          <p id="s7loan" class="sub">&#8377;${M.principal} &middot; 20 years</p>
          <div class="bill">
            <div id="s7r1" class="billrow warn"><span>EXTRA EVERY MONTH</span><span>&#8377;${M.moLo} to &#8377;${M.moHi}</span></div>
            <div id="s7r2" class="billrow total warn"><span>EXTRA INTEREST</span><span>&#8377;${M.intLo} to ${M.intHi} lakh</span></div>
          </div>
          <p id="s7f" class="foot">Two lenders' published rate cards, keyed to the CIBIL band &mdash; spread, not rates</p>
          <h1 id="s7q" class="huge warn" style="font-size: 88px">SAME HOUSE.<br>DIFFERENT NUMBER.</h1>
        </div>`,
  s8: `<div class="stack">
          <div id="s8stamp" class="stamp pop">DO THIS TODAY</div>
          <div id="s8b1" class="decision fundc"><b class="rank">1</b> PULL YOUR CREDIT REPORT</div>
          <div class="swap">
            <p id="s8free" class="sub" style="grid-area: 1 / 1">one free full report a year, from each bureau</p>
            <p id="s8disp" class="sub" style="grid-area: 2 / 1">Wrong entry? Raise a dispute.</p>
            <div id="s8b2" class="decision fundc" style="grid-area: 1 / 1 / 3 / 2"><b class="rank">2</b> PUT EVERY DUE DATE ON AUTO-PAY</div>
          </div>
          <p id="s8f" class="foot">A score is built in months, not in a day &mdash; do this long before you need the loan</p>
        </div>`,
  s9: `<div class="stack">
          <p id="s9k" class="kicker">The simple version</p>
          <div class="row">
            <div id="s9a" class="chip">BANK READS IT FIRST</div>
            <div id="s9b" class="chip fund">ON-TIME EMIs BUILD IT</div>
          </div>
          <div class="row">
            <div id="s9c" class="chip warn">ONE MISS = 36 MONTHS</div>
            <div id="s9d" class="chip warn">LOW SCORE COSTS LAKHS</div>
          </div>
          <div id="s9cta" class="cta"><span class="tri"></span>SUBSCRIBE</div>
        </div>`,
};
const TITLE = {
  s1: "HOOK — the report you've never seen", s2: "ROADMAP — four things",
  s3: "CONCEPT — the report and the score", s4: "RULE — what builds it (4-row ladder)",
  s5: "AUDIT — what destroys it (HERO: 36-month grid)", s6: "ACTION — auto-pay every due date",
  s7: "THE MATH — one percentage point on a ₹30 lakh loan (densest)",
  s8: "DO THIS TODAY", s9: "RECAP + CTA",
};

const sections = L.map((l, i) => {
  const id = "s" + (i + 1);
  const cuts = (CUTS[id] || []).map((c) => {
    const [cid, file] = c.split(":");
    return `\n        <div data-layout-allow-overflow class="bg" id="${cid}" style="background-image: url(assets/img/${file}); opacity: 0"></div>`;
  }).join("");
  return `      <!-- ${i + 1} · ${TITLE[id]} -->
      <section id="${id}" class="scene clip" data-start="${n(l.scene_start)}" data-duration="${n(dur(i))}" data-track-index="1">
        <div data-layout-allow-overflow class="bg" style="background-image: url(assets/img/${id}.jpg)"></div>${cuts}
        <div class="scrim" style="--tint: ${TINT[id]}"></div>
        <div class="grain"></div>
${BODY[id]}
      </section>`;
}).join("\n\n");

const audio = L.map((l, i) =>
  `      <audio id="vo${i + 1}" src="assets/voice/${l.id}.mp3" data-start="${n(l.audio_start)}" data-duration="${n(l.duration)}" data-track-index="10" data-volume="1"></audio>`
).join("\n");

// s7 lifts its stack when the setup rows clear, so the punch centres over the
// surviving EXTRA INTEREST row. Measured off the max-density snapshot.
const S7LIFT = 290;

const smap = L.map((l, i) => `s${i + 1}: ${n(l.scene_start)}`).join(", ");
// ken alternates in/out, never two pushes in a row; every scene carries a photo.
const kens = L.map((l, i) =>
  `      ken("#s${i + 1} .bg", S.s${i + 1}, ${n(dur(i))}, ${i % 2 === 0});`
).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Your Credit History — the invisible record (Hindi)</title>
    <!-- GENERATED by build.mjs from assets/voice/timing.json — edit build.mjs, not this file. -->
    <script src="assets/js/gsap.min.js"><\/script>
    <style>
      /* Self-hosted variable face. Real 100-900 weight axis (no synthetic bold) and
         it carries U+20B9 RUPEE, which Archivo Black does not. Deterministic: no
         render-time network fetch, no dependency on installed system fonts. */
      @font-face {
        font-family: "FinanceSans";
        src: url(assets/fonts/NotoSansFinance-var.woff2) format("woff2-variations");
        font-weight: 100 900;
        font-style: normal;
        font-display: block;
      }
      :root {
        --bg: #0d1017;
        --panel: #161b25;
        --ink: #f5f3ec;
        --muted: #98a2b3;
        --fund: #22c55e;
        --warn: #ef4444;
        --target: #f59e0b;
        --pop: #ff5c39;
        --font: "FinanceSans", system-ui, sans-serif;
      }
      * { box-sizing: border-box; }
      body { margin: 0; background: #000; }
      #root { font-family: var(--font); }

      .scene {
        position: absolute; inset: 0; display: grid; place-items: center;
        padding: 110px 150px; background: var(--bg); color: var(--ink); text-align: center;
        overflow: hidden;
      }
      .bg {
        position: absolute; inset: -8%; z-index: 0; background-size: cover; background-position: center;
        filter: grayscale(0.32) brightness(0.62) contrast(1.05);
      }
      /* s8's photo is >50% pure black field with a bright paper subject. Under the
         orange tint + four-layer scrim the lower-left goes to a dead wash and ken
         reads as no motion at all. One permitted per-scene override (design §1). */
      #s8 .bg { filter: grayscale(0.32) brightness(0.80) contrast(1.05); }
      #s1cutB { background-size: 195%; background-position: 76% 34%; }
      .scrim {
        position: absolute; inset: 0; z-index: 1;
        background:
          radial-gradient(ellipse 72% 64% at 50% 52%, var(--tint, transparent), transparent 72%),
          radial-gradient(ellipse 88% 78% at 50% 53%, rgba(13, 16, 23, 0.46), transparent 80%),
          radial-gradient(ellipse 115% 105% at 50% 54%, rgba(13, 16, 23, 0.14), rgba(13, 16, 23, 0.58)),
          linear-gradient(180deg, rgba(13, 16, 23, 0.40), rgba(13, 16, 23, 0.10) 46%, rgba(13, 16, 23, 0.52));
      }
      .kicker, .huge, .mega, .sub, .foot, .collabel, .counter, .head2, .decision, .gloss {
        text-shadow: 0 2px 22px rgba(0, 0, 0, 0.7), 0 1px 4px rgba(0, 0, 0, 0.55);
      }
      .grain {
        position: absolute; inset: 0; z-index: 1; pointer-events: none;
        background-image: url(assets/img/grain.png); background-size: cover; opacity: 0.05; mix-blend-mode: overlay;
      }
      .stack { position: relative; z-index: 2; display: flex; flex-direction: column; align-items: center; gap: 32px; width: 100%; }
      .row { display: flex; align-items: center; justify-content: center; gap: 22px; flex-wrap: wrap; }
      /* s8 · the two notes and the action that replaces them share one grid cell, so
         the exit leaves no ~300px hole mid-frame. Deterministic — no height tween. */
      .swap { display: grid; justify-items: center; align-items: center; row-gap: 32px; }

      .kicker { font-size: 30px; letter-spacing: 4px; text-transform: uppercase; color: var(--muted); font-weight: 800; margin: 0; }
      .huge { font-size: 112px; line-height: 0.98; font-weight: 900; margin: 0; letter-spacing: -2px; }
      .mega { font-size: 240px; line-height: 0.9; font-weight: 900; margin: 0; letter-spacing: -6px; color: var(--ink); }
      .sub { font-size: 40px; color: var(--muted); font-weight: 800; margin: 0; }
      .subline { display: block; font-size: 40px; color: var(--muted); font-weight: 800; letter-spacing: 0; margin-top: 16px; }
      .foot { font-size: 26px; color: var(--muted); font-weight: 700; letter-spacing: 2px; margin: 0; max-width: 1440px; line-height: 1.35; }
      .collabel { font-size: 28px; font-weight: 900; letter-spacing: 3px; margin: 0; }
      .warn { color: var(--warn); }
      .fundc { color: var(--fund); }
      .targetc { color: var(--target); }
      .mutedc { color: var(--muted); }

      .chip {
        font-size: 32px; font-weight: 800; letter-spacing: 1px; padding: 18px 32px;
        border-radius: 999px; background: var(--panel); border: 3px solid #2a3241; color: var(--ink);
      }
      .chip.fund { border-color: var(--fund); }
      .chip.warn { border-color: var(--warn); }

      .stamp {
        font-size: 44px; font-weight: 900; letter-spacing: 3px; padding: 18px 40px; border-radius: 16px;
        color: #0d1017; transform: rotate(-4deg);
      }
      .stamp.fund { background: var(--fund); }
      .stamp.pop  { background: var(--pop); }
      .stamp.warn { background: var(--warn); }

      /* itemised money block — rows are EQUAL width by design (s4) */
      .bill { display: flex; flex-direction: column; gap: 12px; width: 1240px; }
      .billrow {
        display: flex; justify-content: space-between; align-items: center; gap: 26px;
        font-size: 40px; font-weight: 800; text-align: left;
        padding: 12px 26px; background: var(--panel); border: 3px solid #2a3241; border-radius: 14px;
      }
      .billrow.fund { border-color: var(--fund); color: var(--fund); }
      .billrow.warn { border-color: var(--warn); color: var(--warn); }
      .billrow.total { border-color: var(--warn); color: var(--warn); font-size: 50px; }
      .gloss { font-size: 32px; font-weight: 700; color: var(--muted); text-align: right; }
      .rank { font-size: 54px; font-weight: 900; color: var(--fund); margin-right: 18px; }
      #s7 .bill { width: 1000px; }

      .decision { display: flex; align-items: center; justify-content: center; gap: 18px; font-size: 40px; font-weight: 800; }
      .decision .verdict { padding: 10px 26px; border-radius: 999px; color: #0d1017; font-weight: 900; }
      .v-cancel { background: var(--warn); }
      .v-keep   { background: var(--fund); }

      .head2 { font-size: 54px; font-weight: 900; margin: 0; }
      .counter, .mega, .billrow, .head2, .huge {
        font-variant-numeric: tabular-nums; font-feature-settings: "tnum" 1;
      }
      /* The counter is --warn over a photograph, not over --bg, and red-on-mid-grey
         measured 2.61:1. Fixed with a panel bed (an existing component), NOT by
         lightening --warn — the token is the video's whole "the miss and its price"
         argument and lightening it would degrade every warn element forever. */
      .counter { font-size: 96px; font-weight: 900; color: var(--warn); margin: 0; letter-spacing: 2px;
        background: rgba(13, 16, 23, 0.88); border-radius: 16px; padding: 6px 34px; }

      /* s3 · the 300-900 scale. Track is amber (the score under examination);
         neither endpoint is coloured — an endpoint is not a verdict. */
      .track2 { position: relative; width: 560px; height: 40px; background: var(--panel); border: 3px solid #2a3241; border-radius: 999px; overflow: hidden; }
      .fill2 { position: absolute; inset: 0; background: var(--target); transform: scaleX(0); transform-origin: left center; }

      /* s5 · the hero. 3 rows x 12 = 36 months. Green fills left-to-right across the
         whole scene; one cell slams warn and never clears while the fill runs past it. */
      #s5grid { display: grid; grid-template-columns: repeat(12, 62px); gap: 12px; }
      .cell { width: 62px; height: 62px; border-radius: 10px; background: #161b25; border: 3px solid #2a3241; }

      /* U+2192 and U+25B6 are absent from the self-hosted subset, so they are drawn
         in CSS instead of relying on a system fallback. Em-based, so they scale with
         whatever font-size the host element carries. */
      .arrow, .arr {
        display: inline-block; position: relative; vertical-align: middle;
        width: 0.92em; height: 0.62em; color: var(--muted);
      }
      .arr { width: 0.78em; margin: 0 0.14em; color: var(--muted); }
      .arrow.fx { font-size: 44px; color: var(--fund); }
      .arrow::before, .arr::before {
        content: ""; position: absolute; left: 0; top: 50%;
        width: 100%; height: 0.09em; background: currentColor; transform: translateY(-50%);
      }
      .arrow::after, .arr::after {
        content: ""; position: absolute; right: 0.02em; top: 50%;
        width: 0.3em; height: 0.3em;
        border-top: 0.09em solid currentColor; border-right: 0.09em solid currentColor;
        transform: translateY(-50%) rotate(45deg);
      }
      .tri {
        display: inline-block; width: 0; height: 0; vertical-align: middle;
        margin-right: 0.34em;
        border-left: 0.62em solid currentColor;
        border-top: 0.36em solid transparent; border-bottom: 0.36em solid transparent;
      }
      .cta { font-size: 46px; font-weight: 900; letter-spacing: 2px; padding: 24px 56px; border-radius: 14px; background: var(--pop); color: #0d1017; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="${n(T.total)}" style="position: relative; width: 1920px; height: 1080px; overflow: hidden;">

${sections}

      <!-- voiceover (ElevenLabs "Harsh") — one clip per scene, direct root children -->
${audio}
    </div>

    <script>
      window.__timelines = window.__timelines || {};
      var tl = gsap.timeline({ paused: true });

      // Scene starts (s) — generated from timing.json alongside the <section> attrs,
      // the <audio> rows and the root data-duration. Never hand-typed.
      var S = { ${smap} };

      function rise(sel, at, dur, y) {
        tl.fromTo(sel, { opacity: 0, y: y == null ? 40 : y }, { opacity: 1, y: 0, duration: dur == null ? 0.7 : dur, ease: "expo.out" }, at);
      }
      function pop(sel, at, dur) {
        tl.fromTo(sel, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: dur == null ? 0.6 : dur, ease: "back.out(1.7)" }, at);
      }
      function popEach(sel, at, dur, stag) {
        tl.fromTo(sel, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: dur == null ? 0.4 : dur, ease: "back.out(1.7)", stagger: stag == null ? 0.12 : stag }, at);
      }
      function fade(sel, at, dur, to) {
        tl.fromTo(sel, { opacity: 0 }, { opacity: to == null ? 1 : to, duration: dur == null ? 0.5 : dur, ease: "power1.out" }, at);
      }
      function exit(sel, at, dur) {
        tl.to(sel, { opacity: 0, duration: dur == null ? 0.4 : dur, ease: "power1.out" }, at);
      }
      function pulse(sel, at, s) {
        tl.to(sel, { scale: s == null ? 1.12 : s, duration: 0.16, ease: "power2.out", repeat: 1, yoyo: true }, at);
      }
      function breathe(sel, at, dur) {
        var cyc = 1.5, k = Math.max(1, Math.round(dur / cyc)); if (k % 2 === 0) k += 1;
        tl.to(sel, { scale: 1.035, duration: cyc, ease: "sine.inOut", repeat: k, yoyo: true }, at);
      }
      function fill(sel, at, dur) {
        tl.fromTo(sel, { scaleX: 0 }, { scaleX: 1, duration: dur == null ? 0.8 : dur, ease: "power2.out" }, at);
      }
      // Locale-correct grouping. en-IN gives 1,24,564 (lakh), en-US gives 124,564.
      // Deterministic in Chrome, no network.
      var NUMFMT = new Intl.NumberFormat("en-IN");
      function countUp(id, from, to, at, dur) {
        var el = document.getElementById(id);
        var p = { v: from };
        tl.fromTo(p, { v: from }, {
          v: to, duration: dur == null ? 1.2 : dur, ease: "power1.out",
          onUpdate: function () { el.textContent = NUMFMT.format(Math.round(p.v)); }
        }, at);
      }
      // The background move. Alternates in/out scene to scene — never two pushes in
      // a row. Cut-in overlays run it in the opposite direction to their scene.
      function ken(sel, at, dur, zoomIn) {
        tl.fromTo(sel,
          { scale: zoomIn ? 1.0 : 1.16, xPercent: zoomIn ? -2.5 : 2.5 },
          { scale: zoomIn ? 1.16 : 1.0, xPercent: zoomIn ? 2.5 : -2.5, duration: dur, ease: "none" }, at);
      }
      // s5 grid cells tween colour, not opacity — a filled month stays filled.
      function paint(sel, at, col, dur, stag) {
        tl.to(sel, { backgroundColor: col, borderColor: col, duration: dur == null ? 0.35 : dur, ease: "power2.out", stagger: stag == null ? 0 : stag }, at);
      }

      // Every scene carries a full-bleed .bg under the grade; ken runs the whole
      // scene, so no frame is ever static.  in, out, in, out, in, out, in, out, in
${kens}

      // 1 · HOOK — the on-screen payoff (#s1q) lands at +3.2, independent of delivery
      // rate; the VO's naming lands ~+14.2. Audit check 3 gate is ≤15s.
      rise("#s1k", S.s1 + 0.40, 0.6, 20);
      pop("#s1q", S.s1 + 3.20, 0.7);
      fade("#s1cutA", S.s1 + 3.20, 0.5);
      ken("#s1cutA", S.s1 + 3.20, 11.80, false);
      rise("#s1d1", S.s1 + 5.00, 0.4, 24);
      rise("#s1d2", S.s1 + 7.10, 0.4, 24);
      fade("#s1cutB", S.s1 + 8.50, 0.5);
      ken("#s1cutB", S.s1 + 8.50, 6.50, true);
      rise("#s1d3", S.s1 + 10.80, 0.4, 24);
      pulse("#s1q", S.s1 + 14.20, 1.08);
      breathe("#s1q", S.s1 + 14.60, 1.5);
      exit("#s1k", S.s1 + 14.60, 0.4);
      exit("#s1cutA", S.s1 + 14.60, 0.4);
      exit("#s1cutB", S.s1 + 14.60, 0.4);
      pop("#s1stamp", S.s1 + 15.50, 0.6);
      pulse("#s1stamp", S.s1 + 16.30, 1.06);
      breathe("#s1stamp", S.s1 + 16.80, 1.5);

      // 2 · ROADMAP — chips anchored to their spoken beat (gaps 0.9-1.5s), NOT a cascade
      rise("#s2k", S.s2 + 0.40);
      pop("#s2a", S.s2 + 1.30, 0.45);
      pop("#s2b", S.s2 + 2.80, 0.45);
      pop("#s2c", S.s2 + 4.20, 0.45);
      pop("#s2d", S.s2 + 5.50, 0.45);
      breathe("#s2row2", S.s2 + 6.60, 1.5);
      rise("#s2sub", S.s2 + 9.50);

      // 3 · CONCEPT — enumeration cascade, then the 300-900 scale as the single focal
      rise("#s3k", S.s3 + 0.40);
      pop("#s3e1", S.s3 + 1.50, 0.45);
      pop("#s3e2", S.s3 + 2.20, 0.45);
      pop("#s3e3", S.s3 + 2.90, 0.45);
      rise("#s3rec", S.s3 + 5.40);
      exit("#s3e1", S.s3 + 7.40, 0.4);
      exit("#s3e2", S.s3 + 7.40, 0.4);
      exit("#s3e3", S.s3 + 7.40, 0.4);
      rise("#s3ha", S.s3 + 7.80);
      rise("#s3hb", S.s3 + 11.10);
      exit("#s3k", S.s3 + 12.30, 0.4);
      exit("#s3rec", S.s3 + 12.30, 0.4);
      // storyboard exits the head2s at +15.6, one second AFTER the focal enters —
      // pinned stacks would overlap them over the mega. Exited before it instead.
      exit("#s3ha", S.s3 + 14.20, 0.4);
      exit("#s3hb", S.s3 + 14.20, 0.4);
      pop("#s3scale", S.s3 + 14.60, 0.7);
      fill("#s3fill", S.s3 + 14.60, 0.8);
      pop("#s3g1", S.s3 + 17.80, 0.5);
      pop("#s3g2", S.s3 + 18.40, 0.5);
      fade("#s3f", S.s3 + 19.40);
      breathe("#s3scale", S.s3 + 19.90, 1.5);

      // 4 · RULE — anchored, not cascaded: the VO spaces the four factors over 13.1s.
      // The 6.0s r2->r3 window carries a pulse (its cut-in was dropped at asset stage).
      rise("#s4k", S.s4 + 0.40);
      rise("#s4r1", S.s4 + 4.20, 0.4, 24);
      pulse("#s4r1", S.s4 + 4.80, 1.05);
      rise("#s4r2", S.s4 + 7.50, 0.4, 24);
      pulse("#s4r2", S.s4 + 10.00, 1.05);
      exit("#s4k", S.s4 + 12.60, 0.4);
      rise("#s4r3", S.s4 + 13.50, 0.4, 24);
      rise("#s4r4", S.s4 + 17.30, 0.4, 24);
      fade("#s4f", S.s4 + 18.60);

      // 5 · HERO — 36 months. Green fills left-to-right the whole scene; the miss
      // slams red at the «एक चूकी हुई किश्त» word and the fill runs past it.
      rise("#s5k", S.s5 + 0.40);
      pop("#s5grid", S.s5 + 2.00, 0.6);
      paint("#s5grid .cell:not(.miss)", S.s5 + 2.60, "#22c55e", 0.35, 0.41);
      paint("#s5grid .miss", S.s5 + 8.00, "#ef4444", 0.35);
      pulse("#s5grid .miss", S.s5 + 8.40, 1.35);
      fade("#s5ctr", S.s5 + 9.00, 0.4);
      countUp("s5num", 1, 36, S.s5 + 9.00, 8.00);
      fade("#s5cut", S.s5 + 10.20, 0.5, 0.55);
      ken("#s5cut", S.s5 + 10.20, 5.30, false);
      fade("#s5f", S.s5 + 11.60);
      pulse("#s5grid .miss", S.s5 + 13.90, 1.35);
      exit("#s5k", S.s5 + 15.50, 0.4);
      exit("#s5cut", S.s5 + 15.50, 0.4);
      pop("#s5q", S.s5 + 17.60, 0.7);
      pulse("#s5q", S.s5 + 18.90, 1.06);
      breathe("#s5q", S.s5 + 19.30, 1.5);

      // 6 · ACTION — flow is ONE .row element (3 nodes reveal inside it) to stay ≤6
      rise("#s6k", S.s6 + 0.40);
      pop("#s6h", S.s6 + 2.10, 0.7);
      popEach("#s6flow .fnode", S.s6 + 3.60, 0.5, 0.70);
      fade("#s6flow .arrow", S.s6 + 4.00, 0.3);
      exit("#s6k", S.s6 + 8.00, 0.4);
      pop("#s6stamp", S.s6 + 9.90, 0.6);
      pulse("#s6stamp", S.s6 + 10.60, 1.06);
      breathe("#s6stamp", S.s6 + 11.20, 1.5);
      exit("#s6h", S.s6 + 13.40, 0.4);
      exit("#s6flow", S.s6 + 13.40, 0.4);
      exit("#s6stamp", S.s6 + 13.40, 0.4);
      rise("#s6u", S.s6 + 14.20);
      pop("#s6u2", S.s6 + 17.20, 0.5);
      pulse("#s6u2", S.s6 + 18.20, 1.06);
      breathe("#s6u2", S.s6 + 18.60, 1.5);

      // 7 · THE MATH — densest scene. The stack lifts when the setup rows clear so
      // the punch centres over the surviving EXTRA INTEREST row.
      // ponytail: lift measured off the max-density snapshot, not computed.
      rise("#s7k", S.s7 + 0.40);
      rise("#s7band1", S.s7 + 2.80, 0.4, 24);
      rise("#s7setup", S.s7 + 6.10);
      pop("#s7band2", S.s7 + 7.70, 0.5);
      pulse("#s7band2", S.s7 + 8.30, 1.06);
      rise("#s7loan", S.s7 + 11.70);
      rise("#s7r1", S.s7 + 15.00, 0.4, 24);
      exit("#s7k", S.s7 + 16.40, 0.4);
      exit("#s7setup", S.s7 + 16.40, 0.4);
      pop("#s7r2", S.s7 + 18.30, 0.5);
      pulse("#s7r2", S.s7 + 18.90, 1.08);
      fade("#s7f", S.s7 + 19.60);
      exit("#s7band1", S.s7 + 21.20, 0.4);
      exit("#s7band2", S.s7 + 21.20, 0.4);
      exit("#s7loan", S.s7 + 21.20, 0.4);
      exit("#s7r1", S.s7 + 21.20, 0.4);
      tl.to("#s7stack", { y: -${S7LIFT}, duration: 0.8, ease: "power2.inOut" }, S.s7 + 21.20);
      pop("#s7q", S.s7 + 22.50, 0.7);
      pulse("#s7q", S.s7 + 23.40, 1.05);
      breathe("#s7q", S.s7 + 23.90, 1.5);

      // 8 · DO THIS TODAY
      pop("#s8stamp", S.s8 + 0.40, 0.6);
      pulse("#s8stamp", S.s8 + 1.20, 1.06);
      pop("#s8b1", S.s8 + 1.50, 0.5);
      rise("#s8free", S.s8 + 4.50);
      rise("#s8disp", S.s8 + 8.50);
      fade("#s8cut", S.s8 + 10.20, 0.5);
      ken("#s8cut", S.s8 + 10.20, 3.00, true);
      exit("#s8free", S.s8 + 11.00, 0.4);
      exit("#s8disp", S.s8 + 11.00, 0.4);
      pop("#s8b2", S.s8 + 11.60, 0.5);
      exit("#s8cut", S.s8 + 13.20, 0.4);
      rise("#s8f", S.s8 + 14.80);
      pulse("#s8b2", S.s8 + 16.20, 1.05);
      breathe("#s8stamp", S.s8 + 16.60, 1.5);

      // 9 · RECAP + CTA — closes on the .cta block, no logo outro
      rise("#s9k", S.s9 + 0.40);
      pop("#s9a", S.s9 + 1.50, 0.45);
      pop("#s9b", S.s9 + 4.40, 0.45);
      pop("#s9c", S.s9 + 7.10, 0.45);
      pop("#s9d", S.s9 + 9.40, 0.45);
      exit("#s9k", S.s9 + 12.20, 0.4);
      pop("#s9cta", S.s9 + 12.80, 0.6);
      pulse("#s9cta", S.s9 + 15.10, 1.08);
      breathe("#s9cta", S.s9 + 15.50, 1.5);

      window.__timelines["main"] = tl;
    <\/script>
  </body>
</html>
`;

fs.writeFileSync(path.join(DIR, "index.html"), html, "utf8");
console.log(`index.html · ${L.length} scenes · ${n(T.total)}s · s7 ₹${M.moLo}-${M.moHi}/mo · ₹${M.intLo}-${M.intHi} lakh`);
