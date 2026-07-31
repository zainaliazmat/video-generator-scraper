/* Build index.html for first-lakh-first-thousand / en.
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
 * Sibling of first-lakh-first-thousand-hi/build.mjs: storyboard-en.md §3/§4
 * ports the hi cut's DOM, ID scheme and cue ladder verbatim, so a fix made
 * here should travel there. Only the DATA below is a US rewrite.
 *
 * Run:  node build.mjs
 */
import fs from "node:fs";

const T = JSON.parse(fs.readFileSync("assets/voice/timing.json", "utf8"));
const TRANS = 0.45;          // format.json scene.transition_seconds
const LADDER = [290, 240, 112, 96, 88, 76, 72, 54, 50, 46, 44, 40, 32, 30, 28, 26];
const LOCALE = "en-US";      // $100,000 — NOT the hi cut's en-IN (1,00,000)

// ---------------------------------------------------------------- the scenes
// Columns: line, aperture, focal kind, role colour, bar, focal copy, foot copy,
//          image basename, mosaic-minor basename, anchored cue (absolute s).
// Copy is verbatim from script-en.md's [ap ...] cue blocks; layout/aperture/
// cue/role columns are from storyboard-en.md §6. `{>}` renders as the CSS arrow
// (U+2192 is absent from the font subset and would silently fall back).
//
// GLYPHS NOT IN THE SUBSET, rewritten here (asserted below, not trusted):
//   →  -> {>}      ~  -> "around" / "NEAR"      ×  -> "for"
//   ½  -> 0.5      ≈  -> "around"               …  -> unused
// Rewriting ½/6½ as 0.5/6.5 also matches storyboard §6's rounding rule, which
// already renders 12.5 as a decimal and never as 13.
const A = "{>}";
const SC = [
["1.1","B","num","warn","THE FIRST $10,000","12.5 MONTHS","ILLUSTRATIVE · $800/mo · 0% return · monthly compounding","s1",null,3.36],
["1.2","B","num","fund","THE TENTH $10,000","6 MONTHS","ILLUSTRATIVE · $800/mo · around 10%/yr · monthly compounding","s2",null,9.47],
["1.3","M","stmt","warn","SAME $800",`12.5 months ${A} 6 months`,null,"s3","s3m",null],
["1.4","C-R","stmt","","WHAT CHANGED","The second time, $90,000 was already standing behind it","Illustrative model — same monthly amount, same rate","s4",null,null],
["1.5","R","stmt","warn","THE HARDEST ONE","The first $10,000 is the hardest money you will ever save",null,"s5",null,null],
["1.6","B","stmt","","AFTER THAT","The money starts doing some of the work",null,"s6",null,null],
["1.7","B","stmt","target","QUESTION ONE","When does that help actually show up?",null,"s7",null,null],
["1.8","C-L","stmt","target","QUESTION TWO","How much does picking the right account change it?",null,"s8",null,null],
["1.9","B","stmt","target","QUESTION THREE","And if $800 a month isn't there?",null,"s9",null,null],
["1.10","B","stmt","","FIRST, THE ARITHMETIC","The sum nobody does at the start",null,"s10",null,null],
["2.1","B","stmt","","THE EXAMPLE","$4,000 take-home · $800 set aside","Channel worked-example convention — not a national average","s11",null,null],
["2.2","C-R","num","","PER YEAR","$9,600","$800 a month for 12 months — deposits only, no return","s12",null,58.63],
["2.3","B","num","warn","AT 0%","12.5 MONTHS","ILLUSTRATIVE · $800/mo · 0% · monthly compounding","s13",null,66.11],
["2.4","B","stmt","target","AT AROUND 10%/YR","The long-run shape of the US market","S&P 500 around 10% nominal / around 7% after inflation since 1957 — a shape, never a decimal","s14",null,null],
["2.5","B","num","","AT AROUND 10%","12 MONTHS","ILLUSTRATIVE · $800/mo · around 10%/yr · monthly compounding","s15",null,77.55],
["2.6","M","num","warn","WHAT THE MARKET BOUGHT YOU","0.5 MONTHS",`12.5 months ${A} 12 months, on the first $10,000`,"s16","s15",84.72],
["2.7","B","stmt","","WHY","There is no balance for a return to act on yet",null,"s17",null,null],
["2.8","B","stmt","","SAY IT PLAINLY","Model output — not a statistic, not a promise","Every math frame in this video carries its monthly amount and its rate","s18",null,null],
["2.9","R","stamp","warn","THE FIRST $10,000","100% savings · 0% returns",null,"s19",null,100.87],
["2.10","C-L","stmt","","NOT AN ACCOUNT PROBLEM","Nothing you can open fixes this part",null,"s20",null,null],
["3.1","B","stmt","","SAME INPUT","$800 a month · nothing else changes",null,"s21",null,null],
["3.2","M","stmt","","THE SECOND $10,000",`0% ${A} 12.5 months · around 10% ${A} 11 months`,"ILLUSTRATIVE · $800/mo · monthly compounding","s22","s22m",null],
["3.3","B","stmt","","THE GAP GROWS",`0.5 months ${A} 1.5 months`,null,"s23",null,null],
["3.4","C-R","stmt","","THE TENTH $10,000",`$90,000 ${A} $100,000`,null,"s24",null,null],
["3.5","B","num","warn","STILL AT 0%","12.5 MONTHS","ILLUSTRATIVE · $800/mo · 0% — the interval never shortens","s25",null,131.83],
["3.6","B","num","fund","WITH RETURNS","6 MONTHS","ILLUSTRATIVE · $800/mo · around 10%/yr · monthly compounding","s26",null,139.84],
["3.7","B","stmt","","WHY","The market didn't change. The balance did.",null,"s27",null,null],
["3.8","R","num","fund","0.5 vs 6.5","6.5 MONTHS","The same return, on the tenth $10,000 instead of the first","s28",null,151.73],
["3.9","M","stamp","ink","THIS IS THE VIDEO","0.5 months at the start. 6.5 at the tenth.","ILLUSTRATIVE — figures rounded to the nearest month","s29","s28",157.44],
["3.10","C-L","stmt","","THE PART NOBODY SAYS","Nobody runs this sum for you at the start",null,"s30",null,null],
["4.1","B","stmt","","WHERE THE TIME GOES","What do people spend the first months on?",null,"s31",null,null],
["4.2","B","stmt","","THE SEARCH","The right app. The right rate. The right fund.",null,"s32",null,null],
["4.3","C-R","num","","WHAT IT WAS WORTH","0.5 MONTHS","ILLUSTRATIVE — the entire gap between 0% and around 10%/yr on the first $10,000","s33",null,180.76],
["4.4","B","stmt","warn","THE REAL COST","Six months not starting, to win half of one",null,"s34",null,null],
["4.5","B","stmt","","THE DECIDING NUMBER","And this one is published, not modelled",null,"s35",null,null],
["4.6","B","num","warn","NATIONAL SAVING RATE","2.7%","BEA, Personal Income and Outlays, June 2026 (released 30 Jul 2026)","s36",null,194.21],
["4.7","C-L","num","","WHAT THAT IS","$108/mo","2.7% of the $4,000 worked example — illustrative arithmetic on a published rate","s37",null,199.38],
["4.8","M","stmt","warn","AT 2.7%","7.7 years · 5.7 years with the market","ILLUSTRATIVE · $108/mo · monthly compounding","s38","s13",null],
["4.9","R","stmt","fund","THE ONLY VARIABLE","Not the return rate. The savings rate.",null,"s39",null,213.10],
["4.10","B","stmt","target","NOT WORTH WAITING FOR","The federal funds target range: unchanged","Federal Reserve, open market operations — 3.50–3.75%, last changed 11 Dec 2025","s40",null,null],
["4.11","C-R","stmt","fund","YOURS","The only number fully in your control",null,"s41",null,null],
["5.1","B","stmt","","QUESTION ONE, ANSWERED","When does the money start helping?",null,"s42",null,null],
["5.2","B","stmt","","THE POINT","The year your money earns what you save",null,"s43",null,null],
["5.3","B","num","target","THE WORD","CROSSOVER",null,"s43",null,235.50],
["5.4","C-L","stmt","","THE TEST","When does the balance earn $9,600 in a year?","$800/mo for 12 months = $9,600 a year in","s45",null,null],
["5.5","M","num","target","WHERE IT LANDS","NEAR $96,000","ILLUSTRATIVE · $9,600/yr contribution · around 10%/yr · monthly compounding","s46","s43",246.79],
["5.6","R","num","target","THE REAL TURN","NEAR $100,000","Not $10,000 — the crossover sits roughly ten times further out","s47",null,249.97],
["5.7","B","stmt","","THE LINE","A number a lot of people have heard before",null,"s48",null,null],
["5.8","B","stmt","","WIDELY REPORTED","Munger's line: the first $100,000 is the hardest — after that, ease off the gas","Charlie Munger, as widely reported. PARAPHRASE — no quotation marks, no year, no venue: no primary source is reachable","s49",null,null],
["5.9","C-R","stmt","","NOT A SLOGAN","The quote and the sum land on the same number",null,"s50",null,null],
["5.10","R","stamp","fund","THIS","The first $10,000 is where the HABIT takes over",null,"s51",null,277.05],
["5.11","B","stmt","","THE ONLY ROUTE","There is no path to $100,000 that skips it",null,"s52",null,null],
["6.1","B","stmt","","QUESTION THREE","And if $800 a month simply isn't there?",null,"s53",null,null],
["6.2","B","num","","THE REAL SPREAD","$1,251/wk","BLS, median usual weekly earnings, full-time wage and salary workers, Q2 2026","s54",null,291.36],
["6.3","C-L","stmt","warn","THE MARGIN","Around 4 in 10 couldn't cover $400 in cash or its equivalent","Federal Reserve, Survey of Household Economics and Decisionmaking 2025 — 63% could, using cash, savings or a card paid in full","s55",null,null],
["6.4","B","stmt","","NOT AN AVERAGE","$800 is the output of a split",null,"s56",null,null],
["6.5","B","num","","20% OF $4,000","$800","Every figure in this video runs on this one input","s57",null,309.16],
["6.6","B","stmt","","BE HONEST ABOUT IT","A target for the math — not a statistic","Compare: the actual national saving rate is 2.7% (BEA, June 2026)","s58",null,null],
["6.7","M","stmt","","YOUR 20%","If yours is $200, you start at $200",null,"s59","s11",null],
["6.8","B","stmt","warn","HONESTLY","Then the first $10,000 is further away. That's the truth.",null,"s60",null,null],
["6.9","C-R","stmt","warn","THE REAL BLOCKER","Not the amount. The date that never arrives.",null,"s61",null,null],
["6.10","B","stmt","","THE COMPARISON THAT MATTERS","Small and running beats perfect and unbuilt",null,"s62",null,null],
["7.1","B","stmt","","PICTURE THIS","A cold fire pit and a cold morning",null,"s63",null,null],
["7.2","B","stmt","","WHAT YOU HAVE","Matches. Kindling. That's it.",null,"s64",null,null],
["7.3","C-L","stmt","warn","THE ONLY WAY","The first heat is you, kneeling, one stick at a time",null,"s65",null,null],
["7.4","B","stmt","","WHY IT GIVES NOTHING BACK","There is nothing there yet to hold heat",null,"s66",null,null],
["7.5","B","stmt","fund","AS IT BUILDS","The coals start doing the lighting",null,"s67",null,null],
// s68 demoted R -> B: fin-assets measured its left third well above the 25%
// luminance ceiling (storyboard §9's own fallback — ship 8 R scenes, not 9).
["7.6","B","stmt","fund","ONE LOG, LATER","The same log. Far more heat.",null,"s68",null,367.33],
["7.7","B","stamp","target","THAT MOMENT IS THE CROSSOVER","It comes long AFTER the first armful — never in it",null,"s69",null,375.99],
["7.8","B","stmt","warn","WHERE THE ANALOGY BREAKS","Fires go out. Markets have bad years.","Long-run market returns are a historical shape, not a promise","s70",null,null],
["8.1","B","stmt","","THREE THINGS","All three are boring",null,"s71",null,null],
["8.2","C-R","stmt","fund","ONE — PICK A DATE","A date, not an intention. The day after payday.",null,"s72",null,null],
["8.3","B","stmt","warn","WHY NOT LATER","What's left at month end is always zero",null,"s73",null,null],
["8.4","B","stmt","","TWO — THE ESCALATOR","Raise the saving, not the spending",null,"s74",null,null],
["8.5","B","stmt","fund","THE WHOLE RAISE","Add all of the next raise to the same transfer",null,"s75",null,null],
["8.6","B","stmt","","NOTHING CHANGES","Your life stays yesterday's. The rate quietly climbs.",null,"s76",null,null],
["8.7","C-L","stmt","fund","THREE — MAKE IT HARD","A different bank. No debit card. A day or two away.",null,"s77",null,null],
["8.8","B","num","target","THE ACCOUNT QUESTION","0.38%","FDIC national rate, savings deposits, as of 20 Jul 2026. Price evidence, not a recommendation — no product APY appears in this video","s78",null,424.45],
["8.9","B","stmt","","FIVE MINUTES","That's the whole account question",null,"s79",null,null],
["8.10","B","stmt","","THE ORDER",`Safety ${A} stability ${A} growth`,"An ordering, not a product pick","s80",null,null],
["8.11","C-R","stmt","","RUNG ONE FIRST","A few months of expenses, one day away","FDIC-insured, ordinary transfer speed — a category, not a product","s81",null,null],
["8.12","R","stamp","warn","HOW IT ACTUALLY BREAKS","Not by under-saving. By one emergency.",null,"s82",null,449.85],
["9.1","B","stmt","","TODAY","One job. Five minutes.",null,"s83",null,null],
["9.2","C-L","stmt","fund","DO THIS","One automatic transfer, dated the day after payday",null,"s84",null,null],
["9.3","B","stmt","","THE AMOUNT","$200 works. So does less.","$200 = the twenty-percent example from Chapter 6. The size is not the point — the standing instruction is","s85",null,null],
["9.4","B","stmt","fund","WHY IT WORKS","You never make the decision again",null,"s86",null,null],
["9.5","B","stmt","warn","RECAP ONE","The first $10,000: 100% you · the market buys 0.5 months",null,"s87",null,null],
["9.6","M","stmt","fund","RECAP TWO","The tenth $10,000: the same market buys 6.5",null,"s88","s28",null],
["9.7","B","stmt","target","RECAP THREE","The crossover is near $100,000 — not $10,000",null,"s89",null,null],
["9.8","R","stmt","fund","THE WHOLE VIDEO","Hard because it's all you. After that, the money pulls.",null,"s90",null,493.85],
["9.9","B","cta","pop","—","SUBSCRIBE",null,"s91",null,496.69],
["9.10","B","stmt","","NEXT","Past $100,000 — and the speed after it",null,"s92",null,null],
];

// Continuous-zoom pair (storyboard §7): the SECOND scene re-uses the first's
// photograph and shares ONE ken tween, so the boundary is phase-matched and the
// 0.45s crossfade is invisible. Creator rule (firaun 2026-07-23).
// Exactly one pair in this cut — s44 (5.3) holds s43 (5.2).
const HOLDS = { 44: 43 };
// Ken Burns direction, transcribed verbatim from storyboard §6's `ken` column
// (i = push in, o = pull out). NOT derived from scene parity: the hold pair
// consumes a slot, so the alternation flips phase at 44.
const KEN = ("ioioioioio" + "ioioioioio" + "ioioioioio" + "ioioioioio" +
             "ioiioioioi" + "oioioioioi" + "oioioioioi" + "oioioioioi" +
             "oioioioioi" + "oi");
// Per-image crop overrides (a recall or a tighter crop of the same source).
const CROP = {};
// The video's ONE per-scene grade override (fin-assets note 1): s90 is
// near-pure black by capture and brightness(.55) crushes it to nothing.
const GRADE = { 90: "grayscale(.85) brightness(1.25) contrast(1.15)" };
// Real turns in the argument — a shove instead of the wipe. Two, no more.
// 5.9 -> 5.10 (not interest, the habit) and 6.10 -> 7.1 (into the fire pit).
const ACTS = ["s51", "s63"];

// SFX cue list (storyboard §2, 23 cues). Absolute seconds; mixed in POST by
// tools/audio/mix.py — never an <audio> row in the composition.
const SFX = [
  [3.36,"hero"],[9.47,"hero"],[84.72,"hero"],[100.87,"stamp"],[151.73,"hero"],
  [157.44,"stamp"],[194.21,"hero"],[213.10,"reveal"],[235.50,"reveal"],
  [249.97,"hero"],[272.49,"transition"],[277.05,"stamp"],[309.16,"hero"],
  [340.71,"transition"],[367.33,"reveal"],[375.99,"stamp"],[385.98,"tick"],
  [389.19,"chip"],[400.71,"chip"],[416.51,"chip"],[449.85,"stamp"],
  [493.85,"reveal"],[496.69,"cta"],
];
const MUSIC = "bed-resolve";

// ------------------------------------------------------------------- helpers
const die = (m) => { console.error("BUILD FAIL: " + m); process.exit(1); };
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const arrows = (s) => esc(s).replace(/\{&gt;\}/g, '<span class="arr"></span>');
const f3 = (n) => n.toFixed(3);

// Every glyph that reaches the page must exist in the FinanceSans subset, or the
// browser silently falls back to a system face for that one character. Verified
// against the woff2 cmap: ½ ~ × ≈ … → ° ¼ ¾ are all ABSENT. This is the check
// that fails if a future copy edit reintroduces one.
const OK_GLYPH = /^[A-Za-z0-9 .,:;!?'’"“”()/%$&+=_·—–-]*$/;
const glyphCheck = (s, where) => {
  const plain = String(s).replace(/\{>\}/g, "");
  if (!OK_GLYPH.test(plain))
    die(`${where}: glyph(s) not in the FinanceSans subset: ` +
        JSON.stringify([...plain].filter((c) => !OK_GLYPH.test(c))));
};

// Content column width per aperture (px), from the 12-col grid.
const COLW = { "B": 1720, "M": 1720, "C-R": 1140, "C-L": 1090, "R": 1055 };

/** A bar copy that is empty, or nothing but the storyboard's "none" dash, is the
    script saying THIS SCENE HAS NO TITLE (script-en.md 9.9 is literally
    `bar: —`). Rendered anyway it becomes a full-width black bar carrying one
    short dash, which reads as a title that failed to load — held here through
    the whole CTA. Suppress the element instead: an absent bar is design, a
    one-dash bar is breakage. Row 2 of the swiss-band grid is a fixed 120px and
    the aperture is absolutely positioned, so the layout below does not move. */
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
if (KEN.length !== SC.length) die(`KEN has ${KEN.length} entries, scene table has ${SC.length}`);

// Storyboard §6: a months-to-milestone figure without its ILLUSTRATIVE foot is
// a model output spoken as a statistic. Fail the build, never fix it downstream.
const MUST_FOOT = [1,2,13,15,16,22,25,26,28,29,33,37,38,46];

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

  const noBar = blankBar(bar);
  if (!noBar) glyphCheck(bar, `${id} bar`);
  glyphCheck(focal, `${id} focal`);
  if (foot) glyphCheck(foot, `${id} foot`);
  if (MUST_FOOT.includes(n) && !foot) die(`${id} (${lineId}) must carry its ILLUSTRATIVE foot`);

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
  const barPx = noBar ? 0 : ladderFit(bar, width, 96, 54, 0.64);
  const roleCls = { warn: "warn", fund: "fundc", target: "targetc", ink: "inkc", pop: "" }[role] || "";

  let focalHtml;
  if (kind === "num") {
    const px = ladderFit(focal, width, 112, 76, 0.64);
    focalHtml = `<p class="huge ${roleCls} v-fit" id="${id}-focal" style="font-size:${px}px">${arrows(focal)}</p>`;
  } else if (kind === "stamp") {
    // A verdict that wraps to two lines pushes the foot to the frame edge — the
    // 240px statement zone has room for one stamp line + the foot and no more.
    // 80px is the .stamp horizontal padding.
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
  // preload="none" is REQUIRED too, at this line count: with 92 rows preloading,
  // the page does not reach `load` inside the snapshot CLI's fixed 10s
  // navigation timeout and every snapshot fails (measured on the hi cut).
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

  // Ken Burns. Alternating direction; the hold pair shares ONE tween across both
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
// every image the table names must actually be on disk
for (const [, , , , , , , img, minor] of SC)
  for (const f of [img, minor].filter(Boolean))
    if (!fs.existsSync(`assets/img/${f}.jpg`)) die(`missing image assets/img/${f}.jpg`);
// no two SFX cues inside layout.cue_min_gap_seconds
SFX.forEach(([at], i) => { if (i && at - SFX[i - 1][0] < 0.8) die(`SFX cues ${i}/${i + 1} are ${(at - SFX[i - 1][0]).toFixed(2)}s apart`); });

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The First $10,000 Is The Hardest — first-lakh-first-thousand (en)</title>
<link rel="stylesheet" href="assets/css/blockframe.css">
<style>
/* ---------------------------------------------------------------------------
   One-off components for THIS cut only. Everything else is the system.
   Named .v-* so it is visibly not blockframe.css. Identical to the hi cut's
   block — storyboard-en.md §3 ports that DOM verbatim, so a fix travels.

   WHY these exist: blockframe.css ships the swiss-band BAND aperture only.
   The storyboard's aperture programme (§5) needs three more Unigrid picture
   methods — picture column, reversed field, mosaic. Each is an UNTRANSFORMED
   wrapper with overflow:hidden, so the window stays a fixed aperture while
   "ken" moves the photograph inside it, and the wrapper gives the photo the
   horizontal bleed the system's inset:0 band does not have (without it the
   ken xPercent exposes a 48px strip of --bg at one edge).

   The window is the wrapper's own box + overflow:hidden, NOT a clip-path:
   "hyperframes check" warns that ~40 clip-path/blur/radial-gradient elements
   make the capture layer emit solid black for half a render, and 92 scenes
   would have carried 100 of them. */
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
   bar wraps. Pinning the column is a layout correction, not a token change.
   (System defect, reported by the hi build; still unfixed in tools/scaffold.) */
.v-col1     { grid-column: 1; }

.v-fit      { max-width: 100%; }         /* .stack is a flex column: without a
                                            cap a long line sizes to max-content
                                            and runs off the frame            */
.v-stmt     { line-height: 1.06; }
.v-ruledraw { transform-origin: left center; }   /* so "fill" draws the rule   */
.v-stamp-ink{ background: var(--ink); }          /* the one verdict with no
                                                    role colour (s29)          */
/* A class list of stamp+warn IS .stamp.warn, so the fill modifier also matches the
   .warn TEXT-colour modifier — which is declared after .stamp in
   blockframe.css and wins, painting the verdict red on red. Restore the stamp's
   dark ink at a specificity the role class cannot beat. (System defect too.) */
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
// Figures on screen are pre-formatted for ${LOCALE} ($100,000, $9,600) and the
// system puts tabular-nums on .huge/.head2, so no counter tween is needed here.
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
  { music: MUSIC, sfx: SFX.map(([at, name]) => ({ at, name })) }, null, 1) + "\n");

console.log(`index.html: ${SC.length} scenes, ${f3(total)}s, ${SFX.length} sfx cues`);
