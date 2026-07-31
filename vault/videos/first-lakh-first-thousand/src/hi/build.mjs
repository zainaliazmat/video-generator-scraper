/* Build index.html for first-lakh-first-thousand / hi.
 *
 * ONE source of truth for every duration: assets/voice/timing.json.
 * The four homes of the timing numbers (section attrs, the JS `S` map, the
 * <audio> rows, the root data-duration) are all emitted from it here, so they
 * cannot drift apart.
 *
 * Design system is LINKED, never copied: assets/css/blockframe.css owns every
 * token and component, assets/js/motion.js owns every helper. What this file
 * adds is the `.v-*` one-offs that the system genuinely does not have (the
 * aperture programme) — see the <style> block below.
 *
 * Run:  node build.mjs
 */
import fs from "node:fs";

const T = JSON.parse(fs.readFileSync("assets/voice/timing.json", "utf8"));
const TRANS = 0.45;          // format.json scene.transition_seconds
const LADDER = [290, 240, 112, 96, 88, 76, 72, 54, 50, 46, 44, 40, 32, 30, 28, 26];

// ---------------------------------------------------------------- the scenes
// Columns: line, aperture, focal kind, role colour, bar, focal copy, foot copy,
//          image basename, mosaic-minor basename, anchored cue (absolute s).
// Copy is verbatim from script-hi.md's [ap ...] cue blocks; layout/aperture/
// cue columns are from storyboard-hi.md §6. `{>}` renders as the CSS arrow
// (U+2192 is absent from the font subset and would silently fall back).
const A = "{>}";
const SC = [
["1.1","R","num","warn","THE FIRST LAKH","20 MONTHS","ILLUSTRATIVE · ₹5,000/mo · 0% return · monthly compounding","s1",null,4.95],
["1.2","R","num","fund","THE TENTH LAKH","7 MONTHS","ILLUSTRATIVE · ₹5,000/mo · around 12%/yr · monthly compounding","s1",null,10.42],
["1.3","B","stmt","warn","SAME ₹5,000",`20 months ${A} 7 months`,null,"s3",null,null],
["1.4","C-R","stmt","","WHAT CHANGED","The second time, ₹9,00,000 was already standing behind it","Illustrative model — same monthly amount, same rate","s4",null,null],
["1.5","B","stmt","warn","THE HARDEST ONE","The first ₹1,00,000 is the hardest money you will ever save",null,"s5",null,null],
["1.6","B","stmt","","AFTER THAT","The money starts helping",null,"s5",null,null],
["1.7","B","stmt","target","QUESTION ONE","When does the money actually start helping?",null,"s7",null,null],
["1.8","C-L","stmt","target","QUESTION TWO","How much does picking the right scheme change?",null,"s8",null,null],
["1.9","B","stmt","target","QUESTION THREE","And if ₹5,000 a month isn't there?",null,"s9",null,null],
["1.10","B","stmt","","FIRST, THE ARITHMETIC","The sum nobody does at the start",null,"s10",null,null],
["2.1","B","stmt","","THE EXAMPLE","₹30,000 take-home · ₹5,000 set aside","Channel worked-example convention — not a national average","s11",null,null],
["2.2","B","num","","PER YEAR","₹60,000","₹5,000 a month for 12 months — deposits only, no return","s12",null,67.75],
["2.3","M","num","warn","AT 0%","20 MONTHS","ILLUSTRATIVE · ₹5,000/mo · 0% · monthly compounding","s13","s13m",74.18],
["2.4","C-R","num","target","THE RATE","7.1%","PPF and the 3-year post-office time deposit, Q2 FY2026-27 (DEA notification, 30 Jun 2026)","s14",null,82.70],
["2.5","B","num","","AT 7.1%","19 MONTHS","ILLUSTRATIVE · ₹5,000/mo · 7.1% · monthly compounding","s15",null,85.89],
["2.6","B","num","target","AT AROUND 12%","18 MONTHS","ILLUSTRATIVE · ₹5,000/mo · around 12%/yr · long-run Nifty 50 TRI shape — never a precise figure","s16",null,94.78],
["2.7","R","num","warn","WHAT THE MARKET BOUGHT YOU","2 MONTHS",`20 months ${A} 18 months, on the first ₹1,00,000`,"s17",null,101.67],
["2.8","B","stmt","","WHY","There is no balance for a return to act on yet",null,"s18",null,null],
["2.9","B","stamp","warn","THE FIRST LAKH","100% savings · 0% returns",null,"s19",null,112.82],
["3.1","B","stmt","","SAME INPUT","₹5,000 a month · nothing else changes",null,"s20",null,null],
["3.2","M","stmt","","THE SECOND LAKH",`0% ${A} 20 · 7.1% ${A} 17 · around 12% ${A} 15 months`,"ILLUSTRATIVE · ₹5,000/mo · monthly compounding","s21","s21m",null],
["3.3","B","stmt","","THE GAP GROWS",`2 months ${A} 5 months`,null,"s22",null,null],
["3.4","B","stmt","","THE TENTH LAKH",`₹9,00,000 ${A} ₹10,00,000`,null,"s23",null,null],
["3.5","C-L","num","warn","STILL AT 0%","20 MONTHS","ILLUSTRATIVE · ₹5,000/mo · 0% — the interval never shortens","s24",null,138.72],
["3.6","B","stmt","fund","WITH RETURNS",`7.1% ${A} 9 months · around 12% ${A} 7 months`,"ILLUSTRATIVE · ₹5,000/mo · monthly compounding","s25",null,null],
["3.7","R","num","fund","2 vs 13","13 MONTHS","The same return, on the tenth lakh instead of the first","s26",null,153.72],
["3.8","B","stamp","ink","THIS IS THE VIDEO","Two months at the start. Thirteen at the tenth.",null,"s27",null,159.72],
["4.1","B","stmt","","WHERE THE TIME GOES","What do people spend the first months on?",null,"s28",null,null],
["4.2","B","stmt","","THE SEARCH","The right scheme. The right rate. The right app.",null,"s29",null,null],
["4.3","C-R","stmt","warn","THE RESULT","Weeks of research — and the account never opens",null,"s30",null,null],
["4.4","B","num","","WHAT IT WAS WORTH","2 MONTHS","ILLUSTRATIVE · the whole gap between 0% and around 12% on the first ₹1,00,000","s31",null,182.83],
["4.5","B","stmt","warn","THE REAL COST","Six months not starting, to win two",null,"s32",null,null],
["4.6","R","stmt","fund","THE ONE THAT MATTERS","Not the return rate. The savings rate.",null,"s33",null,195.81],
["4.7","B","stmt","","DEFINITION","How much of each month's income leaves and stays out",null,"s34",null,null],
["4.8","B","stmt","fund","YOURS","The only number fully in your control",null,"s35",null,null],
["4.9","C-L","stmt","","WHO DECIDES WHAT","Market: not you · Rate: not you · Amount: you",null,"s36",null,null],
["4.10","M","stmt","target","NOT WORTH WAITING FOR","Small-savings rates: unchanged for nine straight quarters","Dept. of Economic Affairs notification, 30 Jun 2026 — Q2 FY2026-27","s37","s37m",null],
["5.1","B","stmt","","QUESTION ONE, ANSWERED","When does the money start helping?",null,"s38",null,null],
["5.2","B","stmt","","THE POINT","The year your money earns what you save",null,"s39",null,null],
["5.3","R","num","target","THE WORD","CROSSOVER",null,"s39",null,236.77],
["5.4","B","stmt","","THE TEST","When does the balance earn ₹60,000 in a year?","₹5,000/mo for 12 months = ₹60,000 a year in","s41",null,null],
["5.5","B","stmt","target","WHERE IT LANDS","Roughly ₹8,50,000 at 7.1% · roughly ₹4,80,000 at around 12%","ILLUSTRATIVE · ₹60,000/yr contribution · monthly compounding","s42",null,null],
["5.6","C-R","num","target","THE REAL TURN","NEAR ₹5,00,000","Not ₹1,00,000 — the crossover sits roughly five times further out","s43",null,256.26],
["5.7","B","stmt","warn","SAY IT PLAINLY","The internet usually says otherwise",null,"s44",null,null],
["5.8","B","stmt","warn","NOT THAT","The first lakh is not where interest takes over",null,"s45",null,null],
["5.9","R","stamp","fund","THIS","The first lakh is where the HABIT takes over",null,"s46",null,271.97],
["5.10","B","stmt","","THE ONLY ROUTE","There is no path to ₹5,00,000 that skips it",null,"s47",null,null],
["6.1","B","stmt","","QUESTION THREE","And if ₹5,000 a month simply isn't there?",null,"s48",null,null],
["6.2","B","stmt","","THE REAL SPREAD","₹18,353 – ₹24,217 a month","PLFS Annual Report 2025 — regular wage/salaried average: ₹24,217 men, ₹18,353 women","s49",null,null],
["6.3","C-L","stmt","warn","WHAT THE COUNTRY SAVES","₹7 out of every ₹100","RBI Annual Report, May 2026 — net household financial savings, 7.0% of GNDI, FY25","s50",null,null],
["6.4","B","stmt","","NOT AN AVERAGE","₹5,000 is the output of a split",null,"s51",null,null],
["6.5","M","stmt","","THE SPLIT","65 needs · 15 wants · 20 savings","Channel convention — a workable Indian split, not a published statistic","s52","s52m",null],
["6.6","B","num","","20% OF ₹30,000","₹5,000","Every figure in this video runs on this one input","s53",null,311.81],
["6.7","B","stmt","","YOUR 20%","If yours is ₹1,500, you start at ₹1,500",null,"s54",null,null],
["6.8","C-R","stmt","warn","HONESTLY","Then the first lakh is further away. That's the truth.",null,"s55",null,null],
["6.9","B","stmt","target","THE ENTRY TICKET","₹500 a month · ₹250 in some",'AMFI — SIP minimum ₹500/mo; ₹250 "Chhoti SIP". Price evidence, not a recommendation.',"s56",null,null],
["6.10","B","stmt","warn","THE REAL BLOCKER","Not the amount. The date that never arrives.",null,"s57",null,null],
["7.1","B","stmt","","PICTURE THIS","An empty tank on the roof",null,"s58",null,null],
["7.2","B","stmt","","WHAT YOU HAVE","A bucket. And a ladder.",null,"s59",null,null],
["7.3","C-L","stmt","warn","THE ONLY WAY","The first fill is you, the ladder and the bucket",null,"s60",null,null],
["7.4","B","stmt","","WHY THE RAIN CAN'T HELP","The surface catching it is tiny",null,"s61",null,null],
["7.5","B","stmt","fund","AS IT FILLS","A wider surface starts catching the rain",null,"s62",null,null],
["7.6","R","stmt","fund","ONE DAY","The rain puts in what your bucket used to",null,"s63",null,371.76],
["7.7","B","stamp","target","THAT DAY IS THE CROSSOVER","It comes AFTER the first bucket — not in it",null,"s64",null,376.81],
["7.8","B","stmt","warn","WHERE THE ANALOGY BREAKS","Rain isn't the same every year. Neither is the market.","Long-run market returns are a historical shape, not a promise","s65",null,null],
["8.1","B","stmt","","THREE THINGS","All three are boring",null,"s66",null,null],
["8.2","C-R","stmt","fund","ONE — PICK A DATE","A date, not an intention. Salary day.",null,"s67",null,null],
["8.3","B","stmt","warn","WHY NOT LATER","What's left at month end is always zero",null,"s68",null,null],
["8.4","B","stmt","","TWO — THE ESCALATOR","Raise the saving, not the spending",null,"s69",null,null],
["8.5","B","stmt","fund","THE WHOLE RAISE","Add all of the next raise to the same transfer",null,"s70",null,null],
["8.6","C-L","stmt","","NOTHING CHANGES","Your life stays yesterday's. The rate quietly climbs.",null,"s71",null,null],
["8.7","B","stmt","fund","THREE — MAKE IT HARD","A separate account. No card. No shortcut.",null,"s72",null,null],
["8.8","M","stmt","","THE ORDER",`Safety ${A} stability ${A} growth`,"The sequence practitioners describe — ordering, not a product pick","s73","s73m",null],
["8.9","B","stmt","","RUNG ONE","A few months of expenses you can reach the same day",null,"s74",null,null],
["8.10","B","stmt","","RUNGS TWO AND THREE","Only then the part you can shut away for years",null,"s75",null,null],
["8.11","R","stamp","warn","HOW IT ACTUALLY BREAKS","Not by under-saving. By one emergency.",null,"s76",null,455.13],
["9.1","B","stmt","","TODAY","One job. Five minutes.",null,"s77",null,null],
["9.2","C-R","stmt","fund","DO THIS","One auto-transfer, dated to salary day",null,"s78",null,null],
["9.3","B","stmt","","THE AMOUNT","₹1,500 works. ₹500 works.","The size is not the point; the standing instruction is","s79",null,null],
["9.4","B","stmt","fund","WHY IT WORKS","You never have to make the decision again",null,"s80",null,null],
["9.5","B","stmt","warn","RECAP ONE","The first lakh: 100% you · returns buy 2 months",null,"s81",null,null],
["9.6","M","stmt","fund","RECAP TWO","The tenth lakh: the same return buys 13",null,"s23","s26",null],
["9.7","B","stmt","target","RECAP THREE","The crossover is near ₹5,00,000 — not ₹1,00,000",null,"s43",null,null],
["9.8","R","stmt","fund","THE WHOLE VIDEO","Hard because it's all you. After that, the money helps.",null,"s84",null,501.43],
["9.9","B","cta","pop","—","SUBSCRIBE",null,"s85",null,507.17],
["9.10","B","stmt","","NEXT",`The ₹5,00,000 mark — and the speed after it`,null,"s86",null,null],
];

// Continuous-zoom pairs (storyboard §7): the SECOND scene re-uses the first's
// photograph and shares ONE ken tween, so the boundary is phase-matched and the
// 0.45s crossfade is invisible. Creator rule (firaun 2026-07-23).
const HOLDS = { 2: 1, 6: 5, 40: 39 };
// Ken Burns direction, transcribed verbatim from the storyboard §6 `ken` column
// (i = push in, o = pull out). NOT derived from scene parity: the hold pairs
// consume a slot, so the alternation flips phase at 41 and the parity rule
// silently disagrees with the storyboard from there to the end.
const KEN = ("iiioiiioio" + "ioioioioio" + "ioioioioio" + "ioioioioii" +
             "oioioioioi" + "oioioioioi" + "oioioioioi" + "oioioioioi" + "oioioi");
// Per-image crop overrides (a recall or a tighter crop of the same source).
const CROP = { 40: "132%", 82: "120%", 83: "118%" };
// The video's ONE per-scene grade override (fin-assets note 1): s46 is near-black
// by capture and the 0.62 brightness crushes it flat.
const GRADE = { 46: "grayscale(.32) brightness(1.40) contrast(1.05)" };
// Real turns in the argument — a shove instead of the wipe. Two, no more.
const ACTS = ["s46", "s58"];

// SFX cue list (storyboard §2). Absolute seconds; mixed in POST by
// tools/audio/mix.py — never an <audio> row in the composition.
const SFX = [
  [4.95,"hero"],[10.42,"hero"],[101.67,"hero"],[112.82,"stamp"],[153.72,"hero"],
  [159.72,"stamp"],[195.81,"reveal"],[236.77,"reveal"],[256.26,"hero"],
  [269.27,"transition"],[271.97,"stamp"],[311.81,"hero"],[340.08,"transition"],
  [371.76,"reveal"],[376.81,"stamp"],[391.14,"tick"],[396.06,"chip"],
  [411.06,"chip"],[428.64,"chip"],[455.13,"stamp"],[501.43,"reveal"],[507.17,"cta"],
];

// ------------------------------------------------------------------- helpers
const die = (m) => { console.error("BUILD FAIL: " + m); process.exit(1); };
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const arrows = (s) => esc(s).replace(/\{&gt;\}/g, '<span class="arr"></span>');
const f3 = (n) => n.toFixed(3);

// Content column width per aperture (px), from the 12-col grid.
const COLW = { "B": 1720, "M": 1720, "C-R": 1140, "C-L": 1090, "R": 1055 };

/** A bar copy that is empty, or nothing but the storyboard's "none" dash, is the
    script saying THIS SCENE HAS NO TITLE (script-hi.md 9.9 is literally
    `bar: —`). Rendered anyway it becomes a full-width black bar carrying one
    short dash, which reads as a title that failed to load — held here through
    the second-to-last scene, next to the CTA. Suppress the element instead: an
    absent bar is design, a one-dash bar is breakage. Row 2 of the swiss-band
    grid is a fixed 120px and the aperture is absolutely positioned, so the
    layout below does not move. */
const blankBar = (s) => !String(s ?? "").replace(/[—–-]/gu, "").trim();
for (const [s, want] of [["—", true], ["", true], ["-", true], [null, true],
                         ["NEXT", false], ["THE ORDER", false], ["0.5 vs 6.5", false]])
  if (blankBar(s) !== want) die(`blankBar(${JSON.stringify(s)}) should be ${want}`);

/** Step DOWN the type ladder until the line fits its column. Never interpolate,
    never go below `floor`. If nothing on the ladder fits, that is a layout
    failure and the build says so rather than shrinking off the ladder. */
function ladderFit(text, width, start, floor, em, soft) {
  const plain = text.replace(/\{>\}/g, "-");
  for (const px of LADDER) {
    if (px > start || px < floor) continue;
    if (plain.length * em * px <= width) return px;
  }
  if (soft) return floor;   // a stamp may wrap to two lines at the floor size
  die(`"${plain}" (${plain.length} chars) does not fit ${width}px at or above ${floor}px`);
}

// --------------------------------------------------------------------- build
const lines = T.lines;
if (lines.length !== SC.length) die(`timing.json has ${lines.length} lines, scene table has ${SC.length}`);

const sections = [], audio = [], cues = [], S = {}, ids = [];

SC.forEach((row, i) => {
  const [lineId, ap, kind, role, bar, focal, foot, img, minor, cue] = row;
  const t = lines[i];
  if (t.id !== lineId) die(`row ${i + 1}: table says ${lineId}, timing.json says ${t.id}`);

  const n = i + 1, id = "s" + n, last = n === SC.length;
  const start = t.scene_start;
  const own = t.scene_duration;                       // the scene's own span
  const dur = own + (last ? 0 : TRANS);               // + the cross-dissolve overlap
  S[id] = start; ids.push(id);

  // --- apertures ----------------------------------------------------------
  const apCls = { "B": "v-ap-b", "M": "v-ap-m", "C-R": "v-ap-cr", "C-L": "v-ap-cl", "R": "v-ap-r" }[ap];
  if (!apCls) die(`${id}: unknown aperture ${ap}`);
  const typeCls = { "C-R": " v-cr", "C-L": " v-cl", "R": " v-r" }[ap] || "";
  const width = COLW[ap];

  const bgStyle = [`background-image:url(assets/img/${img}.jpg)`]
    .concat(CROP[n] ? [`background-size:${CROP[n]}`] : [])
    .concat(GRADE[n] ? [`filter:${GRADE[n]}`] : []).join(";");

  let apertures = `<div class="v-ap ${apCls}"><div class="bg" id="${id}-img" style="${bgStyle}"></div></div>`;
  if (minor) apertures += `\n    <div class="v-ap v-ap-min"><div class="bg" id="${id}-min" style="background-image:url(assets/img/${minor}.jpg)"></div></div>`;
  if (ap === "R") apertures += `\n    <div class="v-tone" id="${id}-tone"></div>`;

  // --- type ---------------------------------------------------------------
  const noBar = blankBar(bar);
  const barPx = noBar ? 0 : ladderFit(bar, width, 96, 54, 0.64);
  const roleCls = { warn: "warn", fund: "fundc", target: "targetc", ink: "inkc", pop: "" }[role] || "";

  let focalHtml;
  if (kind === "num") {
    const px = ladderFit(focal, width, 112, 76, 0.64);
    focalHtml = `<p class="huge ${roleCls} v-fit" id="${id}-focal" style="font-size:${px}px">${arrows(focal)}</p>`;
  } else if (kind === "stamp") {
    // A verdict that wraps to two lines pushes the foot to the frame edge — the
    // 240px statement zone has room for one stamp line + the foot and no more.
    // 80px is the .stamp horizontal padding. Snapshot-verified on s46.
    const px = ladderFit(focal, width - 80, 44, 40, 0.63, true);
    focalHtml = `<p class="stamp v-stamp ${role === "ink" ? "v-stamp-ink" : role} v-fit" id="${id}-focal" style="font-size:${px}px">${arrows(focal)}</p>`;
  } else if (kind === "cta") {
    focalHtml = `<p class="cta v-fit" id="${id}-focal">${arrows(focal)}</p>`;
  } else {
    focalHtml = `<p class="head2 ${roleCls} v-fit v-stmt" id="${id}-focal">${arrows(focal)}</p>`;
  }

  // Furniture + source line share one 26px row: the mark is the aperture, the
  // foot is the evidence, and merging them keeps the 240px statement zone to
  // the two type sizes the style requires.
  const mark = `CH ${lineId.split(".")[0]} · ${n} / ${SC.length}`;
  const footHtml = `<p class="foot v-fit" id="${id}-foot">${esc(mark)}${foot ? " · " + arrows(foot) : ""}</p>`;

  const barHtml = noBar ? "" :
`<div class="swissbar v-col1"><h2 class="huge v-fit" id="${id}-bar" style="font-size:${barPx}px">${arrows(bar)}</h2></div>
    `;

  sections.push(
`  <section class="scene clip${typeCls}" id="${id}" data-track-index="${n % 2 ? 1 : 2}" data-start="${f3(start)}" data-duration="${f3(dur)}">
    ${apertures}
    <div class="grain"></div>
    ${barHtml}<hr class="swissrule v-ruledraw v-col1" id="${id}-rule">
    <div class="stack v-col1">
      ${focalHtml}
      ${footHtml}
    </div>
  </section>`);

  // id is REQUIRED on <audio>: the renderer discovers media by id and a row
  // without one renders SILENT (hyperframes `media_missing_id`).
  // preload="none" is REQUIRED too, at this line count: with 86 rows preloading,
  // the page does not reach `load` inside the snapshot CLI's fixed 10s
  // navigation timeout and every snapshot fails. Measured both ways.
  audio.push(`  <audio preload="none" id="vo-${lineId.replace(".", "-")}" class="clip" data-track-index="10" data-start="${f3(t.audio_start)}" data-duration="${f3(t.duration)}" src="assets/voice/${lineId}.mp3"></audio>`);

  // --- cues ---------------------------------------------------------------
  // The assembly (bar -> rule -> focal -> foot) is ONE declared gesture, not
  // four reveals — storyboard §4. Anchored focals land on their word instead.
  const c = [];
  // A suppressed bar has no element to animate — a cue on a missing selector is
  // a silent no-op in GSAP, so it must be dropped here, not left to fail quietly.
  if (!noBar) c.push(`rise("#${id}-bar", S.${id} + 0.15, 0.45, 16);`);
  c.push(`fill("#${id}-rule", S.${id} + 0.55, 0.45);`);

  let focalAt = start + 0.70;
  if (cue != null) {
    const rel = cue - start;
    if (rel < 0.3 || rel > own) die(`${id}: anchored cue ${cue}s is outside its scene (${f3(start)}..${f3(start + own)})`);
    focalAt = cue;
  }
  c.push(`rise("#${id}-focal", ${f3(focalAt)}, 0.40, 12);`);
  c.push(`fade("#${id}-foot", S.${id} + 1.10, 0.40);`);
  if (ap === "R") c.push(`fade("#${id}-tone", S.${id} + 0.05, 0.50);`);
  if (minor) c.push(`fade("#${id}-min", S.${id} + 0.85, 0.40);`);

  // Ken Burns. Alternating direction; a hold pair shares ONE tween across both
  // scenes so the zoom is continuous and the matched-frame boundary is invisible.
  if (!HOLDS[n + 1]) {
    const sel = HOLDS[n] ? `#s${HOLDS[n]}-img, #${id}-img` : `#${id}-img`;
    const from = HOLDS[n] ? lines[HOLDS[n] - 1].scene_start : start;
    const zoomIn = KEN[(HOLDS[n] ? HOLDS[n] : n) - 1] === "i";
    c.push(`ken("${sel}", ${f3(from)}, ${f3(start + own - from)}, ${zoomIn});`);
  }
  cues.push(`  // ${id} — ${lineId} · ${ap}\n  ` + c.join("\n  "));
});

const total = T.total;
const lastEnd = lines[lines.length - 1].scene_start + lines[lines.length - 1].scene_duration;
if (Math.abs(total - lastEnd) > 0.05) die(`timing.json total ${total} != last scene end ${lastEnd}`);

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>पहला एक लाख — first-lakh-first-thousand (hi)</title>
<link rel="stylesheet" href="assets/css/blockframe.css">
<style>
/* ---------------------------------------------------------------------------
   One-off components for THIS cut only. Everything else is the system.
   Named .v-* so it is visibly not blockframe.css.

   WHY these exist: blockframe.css ships the swiss-band BAND aperture only.
   The storyboard's aperture programme (§5) needs three more Unigrid picture
   methods — picture column, reversed field, mosaic. Each is a clip-path on an
   UNTRANSFORMED wrapper, so the window stays a fixed aperture while "ken"
   moves the photograph inside it, and the wrapper gives the photo the
   horizontal bleed the system's inset:0 band does not have (without it the
   ken xPercent exposes a 48px strip of --bg at one edge).

   The window is the wrapper's own box + overflow:hidden, NOT a clip-path:
   "hyperframes check" warns that ~40 clip-path/blur/radial-gradient elements
   make the capture layer emit solid black for half a render, and 86 scenes
   would have carried 92 of them. */
.v-ap        { position: absolute; z-index: 0; overflow: hidden; }
.v-ap > .bg  { inset: 0; top: 0; height: 100%; left: -3%; width: 106%; right: auto; }
.v-ap-b      { top: 180px; height: 600px; left: 0; right: 0; }        /* band      */
.v-ap-m      { top: 180px; height: 600px; left: 0; right: 650px; }    /* mosaic major */
.v-ap-min    { top: 180px; height: 600px; left: 1290px; right: 0; }   /* mosaic minor */
.v-ap-cr     { top: 0; bottom: 0; left: 1290px; right: 0; }           /* picture column R */
.v-ap-cl     { top: 0; bottom: 0; left: 0; right: 1290px; }           /* picture column L */
.v-ap-r      { inset: 0; }                                            /* reversed field   */

/* reversed field: a hard-edged tone block on a column line, in place of the
   four-layer radial scrim the swiss variant deletes */
.v-tone { position: absolute; left: 0; top: 0; width: 1155px; height: 100%;
          background: rgba(13, 16, 23, 0.74); z-index: 1; }

/* the type column moves out of the way of the photograph */
.v-cr .swissbar, .v-cr .swissrule { margin-right: 680px; }
.v-cr .stack                      { padding-right: 680px; }
.v-cl .swissbar                   { margin-left: 630px; padding-left: 100px; }
.v-cl .swissrule                  { margin-left: 730px; }
.v-cl .stack                      { padding-left: 730px; }
.v-r  .swissbar, .v-r  .swissrule { margin-right: 765px; }
.v-r  .stack                      { padding-right: 765px; }

/* blockframe.css puts .swissbar (row 2), .swissrule (row 4) and .stack (row 4)
   in the same one-column grid but never names a COLUMN. Two items declaring only
   grid-row 4 are auto-placed into two implicit COLUMNS, so the rule and the
   statement end up side by side, the black title bar stops mid-frame and every
   bar wraps. First swiss-band build, so this had never rendered. Pinning the
   column is a layout correction, not a token change. */
.v-col1     { grid-column: 1; }

.v-fit      { max-width: 100%; }         /* .stack is a flex column: without a
                                            cap a long line sizes to max-content
                                            and runs off the frame            */
.v-stmt     { line-height: 1.06; }
.v-ruledraw { transform-origin: left center; }   /* so "fill" draws the rule   */
.v-stamp-ink{ background: var(--ink); }          /* the one verdict with no
                                                    role colour (s27)          */
/* A class list of stamp+warn IS .stamp.warn, so the fill modifier also matches the
   .warn TEXT-colour modifier — which is declared after .stamp in
   blockframe.css and wins, painting the verdict red on red (verified in a
   snapshot: s19 rendered as an empty red block). Restore the stamp's dark ink
   at a specificity the role class cannot beat. */
.stamp.v-stamp { color: #0d1017; }
</style>
</head>
<body>
<div id="root" class="swiss-band" data-composition-id="main" data-start="0" data-duration="${f3(total)}" data-width="1920" data-height="1080" style="position:relative;width:1920px;height:1080px;overflow:hidden">

${sections.join("\n")}

${audio.join("\n")}

</div>

<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/motion.js"></script>
<script>
// Generated by build.mjs from assets/voice/timing.json — do not hand-edit.
var S = ${JSON.stringify(S, (k, v) => (typeof v === "number" ? Number(v.toFixed(3)) : v), 0)};

sceneTransitions(${JSON.stringify(ids)}, S, { acts: ${JSON.stringify(ACTS)} });

${cues.join("\n\n")}

register();
// motion.js's register() already runs window.__timelines["main"] = tl. Restating
// it here is not redundancy: "hyperframes check" fails missing_timeline_registry
// when the assignment lives in a linked file, and an unregistered timeline renders
// every element static from frame 0 while still passing every other check.
window.__timelines = window.__timelines || {};
window.__timelines["main"] = tl;
</script>
</body>
</html>
`;

fs.writeFileSync("index.html", html);
fs.writeFileSync("assets/audio.json", JSON.stringify(
  { music: "bed-resolve", sfx: SFX.map(([at, name]) => ({ at, name })) }, null, 1) + "\n");

console.log(`index.html: ${SC.length} scenes, ${f3(total)}s, ${SFX.length} sfx cues`);
