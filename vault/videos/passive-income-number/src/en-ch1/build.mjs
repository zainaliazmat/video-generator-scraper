/* build.mjs — emits index.html + assets/audio.json for CHAPTER 1 of
 * passive-income-number, -en (@moneymavens101, $).
 *
 *   node build.mjs        (or: npm run build)
 *
 * WHY A GENERATOR AND NOT HAND-TYPED HTML. Every data-start, data-duration,
 * data-framings, the JS `S`/`D` maps, every <audio> row and the root duration
 * are FOUR homes for the same number. The failure this project keeps hitting is
 * durations that sum to exactly the right total while every internal cut has
 * drifted, so all four are computed here from ONE source —
 * ../passive-income-number-en/assets/voice/timing.json — and nothing below is
 * typed by hand. A layout pass may not touch a timing (design-chapter-
 * archetypes.md, "Timing is never a design decision"), and the asserts at the
 * bottom of the timing block make a silent re-time throw instead of ship.
 *
 * Chapter 1 is lines 1.1-1.8 = scenes s1-s8. The cut opens on chapter 1, so the
 * rebase constant is 0.000 and the chapter is already frame-exact against the
 * full cut; the rebase is still written as an explicit subtraction so chapters
 * 2-6 inherit the same code path.
 *
 * SPEC, not invention. The arch / ground / art / centred / focal / ken columns
 * below are vault/videos/passive-income-number/storyboard-en.md §7 verbatim, and
 * the kicker / stmt / chip strings are script-en.md's own `[arch …]` cue blocks
 * (one home per fact — the storyboard deliberately does not restate copy).
 */
import fs from "node:fs";

const CH = 1;
const LINES = ["1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"];
const TIMING = JSON.parse(
  fs.readFileSync("../passive-income-number-en/assets/voice/timing.json", "utf8"));
const T = 0.45;                                     // format.json scene.transition_seconds

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`            f1     §7 `ground` (the --f1 temperature arc, §11)
 * art    §7 `art`             ctr    §7 `ctr` (centred)
 * ken    §5: s1 starts `i` and the direction flips at every boundary EXCEPT a
 *        hold, where the partner CONTINUES its predecessor's move with chained
 *        plateKen endpoints. ch1 carries the cut's first hold, s3 -> s4.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · 49-89 -> 76.
 *        Computed below, never written here.
 * role   §1: the colour semantics. ch1 has exactly ONE role scene — s7, --warn,
 *        "the question that opens the loop". Seven colourless frames is correct:
 *        colour is a signifier in this cut, not decoration.
 */
const WARN = "239,68,68";

const SCENES = [
  { line: "1.1", arch: "a", f1: "#161f2b", art: "off", ctr: true, ken: "i",
    kick: "IMAGINE ONE DAY", stmt: "The phone does not ring once.",
    img: "s1.jpg",
    note: "THE PHONE THAT DOES NOT RING. Frame 0 of the video. The photograph is up at +0.00 and only the type arrives — a phone alone on a sunlit table, screen black. Cool first light (#161f2b): the day has not started asking for anything yet." },

  { line: "1.2", arch: "d", f1: "#1a1e24", art: "off", ctr: false, ken: "o", brule: 252,
    kick: "NOTHING ASKS FOR YOU",
    chips: ["No alarm", "No call from work", "No debt reminder"],
    img: "s2.jpg",
    note: "NOTHING ASKS FOR YOU. Cue ladder C — the three chips ARE the statement, so there is no stmt. `ctr` is N because the declared cascade owns archetype D's band; that is the storyboard's own rule (a scene is centred unless something REAL occupies the other side), not a second decision. All three named things are type on purpose (§10: the alarm, the call and the debt reminder deliberately get no cut-in; the clock is the bg)." },

  { line: "1.3", arch: "a", f1: "#241d15", art: "off", ctr: true, ken: "i",
    kenFrom: 1.00, kenTo: 1.08,
    kick: "BEFORE NOON", stmt: "Money is deposited.",
    img: "s3.jpg", bgPos: "center 70%",
    note: "BEFORE NOON — the PROMISE, and the first half of the cut's first matched-frame hold (§6b). ONE FILE, one continuous zoom, across 1.3 and 1.4: plateKen 1.00->1.08 here, 1.08->1.30 on s4, which now points at THIS SAME s3.jpg with THIS SAME background-position. Until attempt 3 s4 carried a derived crop=1600:900:280:320 (an exact-16:9 1600x900 file, so its background-position was a no-op) while s3 is 3:2 at `center 70%` — two different RECTANGLES of one photograph, and the dissolve between them showed two phones, two mugs and two vases (editor-en-ch1-2 finding 1, peaking 14.90s). The firaun 2026-07-23 rule bans a self-dissolve that FLICKERS; identical framing across the joint is the no-flicker case and is the only construction in which a hold cannot be mismatched. Warming to #241d15, held across the hold — a temperature step in the middle of a continuous zoom reads as a cut that is not happening." },

  { line: "1.4", arch: "d", f1: "#241d15", art: "lottie", ctr: false, ken: "i", brule: 400,
    kenFrom: 1.08, kenTo: 1.30,
    kick: "ONE BUZZ", stmt: "That one buzz is the money arriving.",
    img: "s3.jpg", bgPos: "center 70%",
    note: "ONE BUZZ — the payoff of the what-if, and the chapter's one drawn layer. SAME FILE as 1.3 and same background-position, so the §6b hold is one image by construction and the joint cannot be mismatched (editor-en-ch1-2 finding 1; assets-ch1/final/s4.jpg is now unused and left on disk). The push continues 1.08->1.30, which is the tighter framing s4.jpg was cropped for — taken by zoom instead of by a second file. The photograph is a phone with a DARK screen (fin-assets deviation 1, argued in its log): the standing rejection is a LIT screen carrying someone's brand, so the picture is still structurally forbidden from saying money ARRIVED. The Lottie banner is the only honest way to state it, and the amount is masked while the currency is not — a banner with no $ says 'a notification arrived', which is the hi cut's own ch1 review finding. `ctr` N because the Lottie stage occupies D's band." },

  { line: "1.5", arch: "a", f1: "#1c2027", art: "off", ctr: true, ken: "o",
    kick: "NOT RICH", stmt: "One specific number.",
    img: "s5.jpg", bgPos: "center 100%",
    note: "NOT RICH. The number is NAMED and WITHHELD — the open loop the whole cold open is built on, closed at 4.2. Sobers from the warm deposit frames to neutral #1c2027. The still is an arrow standing in an archery target's centre (fin-assets attempt 2, replacing the rejected brass table-tent stamped 5): the line names 'one specific number' and the editor's ruling was that the frame must mean ONE EXACT FIGURE without asserting one — a target does, a legible 5 does not, and the reveal at 4.2 stays withheld. The photograph is NOT re-fetched and NOT re-cropped (editor-en-ch1-2 finding 3 and its ruling on the arrow) — only reframed: at the default `center 50%` the mark sat under the kicker and the focal ran through the arrow's shaft. The handoff proposed `center 32%`, which is the WRONG DIRECTION for a `cover` image that overflows vertically — a smaller percentage aligns nearer the source's TOP and pushes the subject DOWN the frame, i.e. further onto the type (the identical trap 1.3 hit at attempt 2). `center 100%` is the far end of the only slack this file has (231.6 box px, ~126 frame px at the scene's mid-scale) and it is what the frame needs: the X ring and the arrow's point clear the stack entirely and the type lands on bare gold and lower red." },

  { line: "1.6", arch: "d", f1: "#291f13", art: "ticks", ctr: false, ken: "i", brule: 252,
    kick: "ITS ONE JOB",
    ticks: [
      // assets/icons/grocery-bag.svg — a CUFFED PAPER BAG, not the white cloth
      // tote in the photograph. Same reason hi ch1's ration mark is a sack and
      // not a jar: the glyph names the category, the photograph keeps the object.
      { label: "Groceries", art:
        `<path d="M24 32 H76 V82 a6 6 0 0 1 -6 6 H30 a6 6 0 0 1 -6 -6 Z"/>` +
        `<path d="M38 32 V26 a12 12 0 0 1 24 0 V32"/>` },
      // assets/icons/fuel-pump.svg — NEW, and the whole reason this row exists.
      // The doorstep photograph carries groceries and the home and nothing at
      // all for "gas and the car"; this is what puts the car on screen.
      { label: "Gas and the car", art:
        `<path d="M24 88 V28 a8 8 0 0 1 8-8 H54 a8 8 0 0 1 8 8 V88"/>` +
        `<path d="M16 88 H70"/>` +
        `<rect x="33" y="32" width="20" height="16" rx="2"/>` +
        `<path d="M62 40 H74 q8 0 8 8 V70 q0 8 -8 8 H68 V60"/>` },
      // assets/icons/house-door.svg — reused verbatim from the library.
      { label: "Rent or the mortgage", art:
        `<path d="M12 48 L50 16 L88 48"/>` +
        `<path d="M22 42 V86 h56 V42"/>` +
        `<path d="M42 86 V62 h16 v24"/>` },
    ],
    img: "s6.jpg",
    note: "ITS ONE JOB. Ladder C, the warmest ground of the chapter (#291f13), and the chapter's second drawn layer — added at attempt 3 (editor-en-ch1-2 finding 2). The line names THREE costs and the doorstep photograph carries groceries and the home and NOTHING for 'gas and the car', so three chips over a flat still were carrying the whole enumeration and one of the three was floating over a doormat. hi ch1's s5 already ruled this exact beat (three named costs, photograph carries one) after five fetch attempts: DRAW the count. Same mechanism here — bag, fuel pump, house, each under a ticking checkbox — so the car is on screen, the row moves, and rule 8 holds because A COUNT BEING PAID is not something the photograph shows. Inline SVG: no re-fetch, no sixth contact sheet, and the Lottie cap (1 of 4) is untouched. The row stays CENTRED: the subject fills the left two-thirds and the door the right, so unlike 1.2 there is no void to move into." },

  { line: "1.7", arch: "a", f1: "#301519", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "THE QUESTION", stmt: "The honest answer costs more than the popular one.",
    img: "s7.jpg",
    note: "THE QUESTION — the packaging promise, verbatim and untouchable (run.json.style_decision.line_1_7_en_is_untouchable). The chapter's ONLY role scene: --warn, because §1 fixes red as 'what an assumption costs', and this is the question that opens the loop closed at 5.7. Its stmt enters with `pop` (back.out) rather than `rise` — that IS the verdict slam, and it is what makes the `stamp` SFX legal without a .stamp pill or one word of new copy (§2). The photograph is a laptop from behind, screen edge-on, hands only." },

  { line: "1.8", arch: "a", f1: "#1f1e1c", art: "off", ctr: true, ken: "i",
    kick: "ONE RUNG AT A TIME", stmt: "Smallest first. One condition on every rung.",
    img: "s8.jpg",
    note: "ONE RUNG AT A TIME. Neutral-warm as the method is named, and the ladder photograph plants the object the measure bar will later draw (§9a). The chapter's LAST scene: it carries its BARE scene_duration, because there is no successor inside this project to cross-dissolve into. tools/cut_assemble.py adds the +0.45 back when the six chapters are folded into one composition." },
];

/* -------------------------------------------------- 1.4's Lottie, and its cue
 * assets/lottie/phone_notify_credit_usd.js -> window.L_phone_notify_credit_usd,
 * 75 frames @ 30 fps = 2.50 s, native 820x300 (fin-assets handoff). The USD twin
 * exists because the library asset's app mark is a ₹ — shipping that into a US
 * cut is the euro-coin defect class by name.
 *
 * WHERE THE CUE COMES FROM. §5 gives +1.85 as a CHARACTER-OFFSET FALLBACK (f
 * 0.26 on "buzzes") and says explicitly that fin-build resolves each anchored
 * cue against faster-whisper WORD timings, using the fraction only if the word
 * fails to align. It aligned: measured on assets/voice/1.4.mp3 (base.en, word
 * timestamps), "buzzes" runs 1.480-1.920 s into the clip, and the clip starts at
 * scene +0.25, so the spoken word occupies scene +1.730 to +1.920.
 *
 * The asset's own buzz is frames 16-24 = +0.533 to +0.800 into it (the position
 * track jitters ~2 px there; the card falls in over frames 5-15 before it). So
 * playLottie starts at 1.73 - 0.60 = +1.13 and the PHYSICAL buzz lands at
 * +1.66..+1.93 — over the spoken word, and over the `buzz` SFX that
 * cues-tables.json declares at +1.85. Starting the asset AT +1.85 instead would
 * have put its jitter at +2.38, half a second after both.
 */
const LOTTIE_AT = 1.13;
const LOTTIE_DUR = 2.50;   // 75 frames @ 30 fps — true speed

/* ------------------------------------------------------------- the timings
 * Read straight off timing.json, rebased by the chapter's own offset. GAPS —
 * not totals — are what a re-time destroys, so the gaps are asserted below
 * against the shipped measurement, one joint at a time. */
const rows = LINES.map((id) => {
  const l = TIMING.lines.find((x) => x.id === id);
  if (!l) throw new Error(`timing.json has no line ${id}`);
  return l;
});
const OFF = rows[0].scene_start;
const last = rows[rows.length - 1];
const ROOT = +(last.scene_start + last.scene_duration - OFF).toFixed(3);

const sc = SCENES.map((s, i) => {
  const r = rows[i];
  if (r.id !== s.line) throw new Error(`spec/timing mismatch at ${i}`);
  const own = r.scene_duration;
  return {
    ...s, i, id: "s" + (i + 1),
    start: +(r.scene_start - OFF).toFixed(3),
    dur: own,                                                // the scene's own hold
    dd: i < SCENES.length - 1 ? +(own + T).toFixed(3) : own,  // + the cross-dissolve overlap
    track: (i + 1) % 2 ? 1 : 2,                              // or overlapping_clips_same_track
    astart: +(r.audio_start - OFF).toFixed(3),
    adur: r.duration,
    size: s.stmt == null ? null
      : s.stmt.length <= 24 ? 112 : s.stmt.length <= 48 ? 88 : 76,
  };
});

/* the asserts that make a silent re-time impossible ---------------------- */
sc.forEach((s, i) => {
  if (i === 0) { if (s.start !== 0) throw new Error("chapter does not start at 0"); return; }
  const gap = +(sc[i - 1].start + sc[i - 1].dd - s.start).toFixed(3);
  if (Math.abs(gap - T) > 0.005) throw new Error(`${s.id} overlaps by ${gap}, expected ${T}`);
  if (sc[i - 1].track === s.track) throw new Error(`${s.id} shares a track with its neighbour`);
  const shipped = +(rows[i].scene_start - rows[i - 1].scene_start).toFixed(3);
  if (Math.abs(shipped - (s.start - sc[i - 1].start)) > 1e-9)
    throw new Error(`${s.id} gap drifted from the shipped cut`);
});
if (Math.abs(sc[sc.length - 1].start + sc[sc.length - 1].dur - ROOT) > 1e-9)
  throw new Error("last scene does not land on the chapter root");
/* format.json scene.max_scene_seconds — no scene in ch1 declares a second
 * framing, so each holds one photograph for its whole length. */
sc.forEach((s) => {
  if (s.dur > 9.0) throw new Error(`${s.id} holds one photo for ${s.dur}s (max 9.0)`);
});
/* §3's build guard: no `/` and no `?` in any on-screen string — neither is in
 * the 97-codepoint font subset, and a missing glyph renders as tofu with every
 * check green. Also sweeps the ₹ this cut is forbidden to show. */
const pills = (s) => [...(s.chips || []), ...(s.ticks || []).map((t) => t.label)];
sc.forEach((s) => {
  [s.kick, s.stmt, ...pills(s)].filter(Boolean).forEach((t) => {
    const bad = t.match(/[/?₹×≈~→▶¢]/);
    if (bad) throw new Error(`${s.id}: on-screen string carries "${bad[0]}" — not in the subset`);
    if (/[ऀ-ॿ]/.test(t)) throw new Error(`${s.id}: Devanagari in the -en cut`);
  });
  pills(s).forEach((c) => {
    if (c.length > 22) throw new Error(`${s.id}: chip "${c}" is ${c.length} chars (max 22)`);
  });
  if (pills(s).length > 3) throw new Error(`${s.id}: more than 3 chips in a row`);
  /* the drawn layer is never the whole scene: a ticks row is a COUNT over a
   * photograph, so the scene keeps its .bg and never becomes art-only. */
  if (s.ticks && s.art !== "ticks") throw new Error(`${s.id}: ticks without art:"ticks"`);
});

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

function scene(s) {
  const cls = ["scene", "clip", "arch-" + s.arch, "has-photo"];
  if (s.art === "off") cls.push("art-off");
  if (s.ctr) cls.push("centred");
  const style = s.role ? ` style="--tint:rgba(${s.role},.12)"` : "";
  const glow = s.role ? ` style="--gl:rgba(${s.role},.16)"` : "";
  const L = [];
  L.push(`\n<!-- ${s.line} · ${s.arch.toUpperCase()} · ${s.f1} · art ${s.art}` +
    `${s.ctr ? " · centred" : ""}${s.role ? " · --warn" : ""}\n     ${s.note} -->`);
  L.push(`<section class="${cls.join(" ")}" id="${s.id}" data-track-index="${s.track}"` +
    ` data-start="${s.start}" data-duration="${s.dd}" data-framings="${s.dur}"${style}>`);
  // bgPos: the ONLY per-scene .bg override this chapter carries, and it is a
  // FRAMING knob, never a grade one (the grade is locked; `brightness` here
  // would be the thing format.json's grade_note forbids). 1.3 is the one scene
  // whose subject is taller than the 16:9 window: s3.jpg is 1880x1253 (1.50),
  // so `cover` into .bg's 1.778 box crops 231.6px of height, and plateKen 1.08
  // then eats 8% more from both ends — which took the phone's bottom rounded
  // corner off the frame for the last second of the scene. `center 70%` moves
  // the crop window DOWN the source by ~40px, which is what puts the corner
  // back. Measured, not reasoned: 40% (the value proposed in the handoff) moves
  // it the OTHER way and cuts more of the phone — snapshots/qa/bg40 vs bg70 at
  // t=14.55 are the two frames. It also closes ~40 of the ~143 source-px
  // vertical offset between s3's and s4's windows at the hold, so §6b's
  // matched frame is tighter, not looser. It costs the mug's top rim, which s4
  // already crops (fin-assets-en-ch1-3 deviation 2).
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(assets-ch1/final/${s.img})` +
    `${s.bgPos ? ";background-position:" + s.bgPos : ""}"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  L.push(`  <div class="scrim"></div>`);
  if (s.art === "lottie" || s.art === "ticks")
    // rule 9: never darken the PHOTOGRAPH to make drawn art readable — darken
    // BEHIND it with .band, which is scoped to the lower band D already owns.
    L.push(`  <div class="band"></div>`);
  if (s.brule)
    // archetype D's own structural rule, separating the type above from the
    // mechanism below. transform-origin so fill() draws it in from the left.
    L.push(`  <div class="brule" id="${s.id}-br" style="top:${s.brule}px;transform-origin:left center"></div>`);
  L.push(`  <div class="stack" id="${s.id}-stack">`);
  L.push(`    <p class="kicker" id="${s.id}-kick">${esc(s.kick)}</p>`);
  if (s.stmt)
    L.push(`    <p class="huge${s.role ? " warnc" : ""}" id="${s.id}-stmt"` +
      ` style="font-size:${s.size}px">${esc(s.stmt)}</p>`);
  L.push(`  </div>`);
  if (s.chips) {
    // Ladder C: the chips ARE the statement, and they own archetype D's band —
    // which is why this is NOT blockframe's .row. .row is a child of .stack, and
    // .arch-d hangs .stack at the TOP of the frame; D's whole point is that the
    // mechanism owns the bottom two-thirds, so the row is positioned into .p-d
    // absolutely, exactly as the Lottie stage is on 1.4.
    L.push(`  <div class="v-chiprow" id="${s.id}-chips">`);
    s.chips.forEach((c) => L.push(`    <div class="chip">${esc(c)}</div>`));
    L.push(`  </div>`);
  }
  if (s.ticks) {
    // The DRAWN COUNT — the same cell hi ch1's 1.5 ships, plus this cut's own
    // chip label so ladder C keeps its copy. Glyph, name, checkbox; the tick
    // path is the only animated element, so the box is up with the cell and the
    // mark strikes through it 0.5s later. Icons are library files
    // (assets/icons/{grocery-bag,fuel-pump,house-door}.svg), pasted in with only
    // the tick carrying a per-scene id, exactly as the icon rule asks.
    L.push(`  <div class="v-ticks" id="${s.id}-ticks">`);
    s.ticks.forEach((t, n) => {
      L.push(`    <div class="v-tickcell">`);
      L.push(`      <svg class="icon" viewBox="0 0 100 100">${t.art}</svg>`);
      L.push(`      <div class="chip">${esc(t.label)}</div>`);
      L.push(`      <svg class="icon sm" viewBox="0 0 100 100"><rect x="14" y="20" width="58" height="58" rx="8"/>` +
        `<path id="${s.id}-tick${n + 1}" d="M28 50 L45 68 L88 16"/></svg>`);
      L.push(`    </div>`);
    });
    L.push(`  </div>`);
  }
  if (s.art === "lottie")
    // A Lottie stage needs PIXEL dimensions (format.json chapter_design.gotchas):
    // lottie-web sizes its <svg> off the container's box at loadAnimation() time,
    // so a stage without them renders the artwork at native size pinned top-left
    // with every check green. 820x300 IS the asset's native box, centred inside
    // archetype D's .p-d band (0,424,1920,656).
    L.push(`  <div class="v-lstage" id="${s.id}l"></div>`);
  L.push(`  <div class="grain"></div>`);
  L.push(`</section>`);
  return L.join("\n");
}

const audio = sc.map((s) =>
  `<audio id="vo-${CH}-${s.i + 1}" class="clip" data-track-index="10" ` +
  `data-start="${s.astart}" data-duration="${s.adur}" src="assets/voice/${s.line}.mp3"></audio>`
).join("\n");

const map = (f) => "{ " + sc.map((s) => `${s.id}: ${f(s)}`).join(", ") + " }";

/* the photograph carries the motion — one move per scene. `i`/`o` are ken's
 * fixed 1.0<->1.16 endpoints; a HOLD pair needs plateKen's EXPLICIT endpoints so
 * the second scene picks up exactly where the first ended. */
const kenJs = sc.map((s) => s.kenFrom != null
  ? `plateKen("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.kenFrom.toFixed(2)}, ${s.kenTo.toFixed(2)});`
  : `ken("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.ken === "i"});`).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 1 · the won morning</title>

<!-- ===========================================================================
     CHAPTER 1 — the what-if cold open. Eight cuts, ${ROOT}s, second person.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the eight <audio> rows and
     the root duration are computed from that one file and asserted against the
     shipped cut's GAPS — a re-time is exactly what produces a correct total with
     every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is 0.000s — chapter 1 opens the cut — so this concatenates
     frame-exact as-is. The LAST scene carries its bare scene_duration: a chapter
     has no successor to cross-dissolve into, and tools/cut_assemble.py adds the
     +0.45 overlap back when the six chapters are folded into one composition.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Five of eight scenes are art-off + centred: rule 8 (drawn art over a still
     must be ADDITIVE, never depictive) retires the drawn layer wherever the
     photograph already carries the beat, and .centred then re-centres the stack
     so the archetype's empty side is not a hole. Three scenes have something
     real on the other side, all archetype D: 1.2's chip cascade, 1.4's Lottie
     banner — the one thing here a photograph is structurally forbidden from
     saying, because the standing rejection bans a lit phone screen — and 1.6's
     drawn count, which asserts a cost the doorstep photograph does not contain.

     1.3 and 1.4 are ONE FILE. The §6b hold is s3.jpg at "center 70%" under a
     single chained push (1.00 -> 1.08 -> 1.30); a second, differently-cropped
     file is what made the joint ghost in draft 2.

     Every scene carries has-photo and a real full-bleed .bg under the LOCKED
     grade. No per-scene brightness override anywhere: photo_free_scene_ratio is
     0 and the photograph is the only variable there is.
     =========================================================================== -->

<link rel="stylesheet" href="assets/blockframe.css">
<link rel="stylesheet" href="assets/chapter-design.css">
<style>
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--bg); }
/* the four plate rects, one per archetype (format.json chapter_design.archetypes) */
.p-a { left: 0;      top: 0;     width: 1920px; height: 1080px; }
.p-b { left: 1120px; top: 150px; width: 860px;  height: 610px;  }
.p-c { left: 1046px; top: -60px; width: 934px;  height: 1200px; }
.p-d { left: 0;      top: 424px; width: 1920px; height: 656px;  }

/* ONE-OFF, this composition only (hence .v-): the Lottie band stage on 1.4.
   PIXELS, not percentages — lottie-web sizes its <svg> from the container's box
   at loadAnimation() time, so a stage without pixel dimensions renders the
   artwork at native size pinned top-left with every check green. 820x300 IS the
   asset's native box, sitting in archetype D's .p-d band (0,424,1920,656):
   top 424 + (656-300)/2 = 602. z 2 so the .scrim and the .band sit UNDER it.

   The left offset is NOT the frame centre. A notification belongs on the DEVICE, and the
   device moved: attempt 3 repointed 1.4 at s3.jpg to make the §6b hold one
   image, so the phone now sits right of centre. Its centre runs x1218-x1236
   across the Lottie's own play window (+1.13 to +3.63, scale 1.116 -> 1.195;
   phone centre = 960 + 231*scale). The card is centred in its 820px stage, so
   left = 1225 - 410 = 815 puts the banner back squarely on the phone — the one
   thing editor-en-ch1-2 said not to lose while fixing the joint. Right edge
   1635, inside the 1810 safe line. */
.v-lstage { position: absolute; z-index: 2; left: 815px; top: 602px; width: 820px; height: 300px; }
.v-lstage svg { width: 100% !important; height: 100% !important; }

/* ONE-OFF, this composition only: the declared chip cascade on 1.2 and 1.6.
   Not blockframe's .row — that is a child of .stack, which .arch-d hangs at the
   TOP of the frame, and D's whole point is that the mechanism owns the bottom
   two-thirds. Absolutely positioned into .p-d exactly as .v-lstage is, so the
   cascade genuinely occupies the archetype's other side (which is why these two
   scenes are not .centred). Top 660 keeps the row clear of the watermark box
   (y956-1040) and well inside the 110px safe padding. */
.v-chiprow { position: absolute; z-index: 2; left: 0; right: 0; top: 660px;
             display: flex; align-items: center; justify-content: center; gap: 22px; }

/* ONE-OFF, this composition only: 1.6's drawn count, added at attempt 3. Same
   component as hi ch1's 1.5 (glyph over a ticking checkbox) with this cut's chip
   label between them, because -en carries its three costs as ladder-C chips and
   the copy is the script's, not the layout's. Positioned into .p-d like
   .v-chiprow and .v-lstage — D's mechanism owns the bottom two-thirds and .row
   is a child of .stack, which D hangs at the TOP. Cell height is
   220 + 14 + ~80 + 14 + 130 = 458, so at top 462 the row ends at y920: inside
   the 110px bottom safe padding and clear of the watermark box (y956-1040).
   gap 150 keeps the widest two labels ("Gas and the car", "Rent or the
   mortgage") from touching at 32px. */
.v-ticks { position: absolute; z-index: 2; left: 0; right: 0; top: 462px;
           display: flex; justify-content: center; align-items: flex-start; gap: 150px; }
.v-tickcell { display: flex; flex-direction: column; align-items: center; gap: 14px; }

/* 1.2 ONLY (editor-en-ch1-1 finding 5). Centred, the row landed ON the alarm
   clock — the one object in the frame that serves its FIRST chip, "No alarm" —
   while the right 55% of the photograph was empty near-black: the picture and
   the mechanism fighting for the same third of the frame with a void beside
   them. Right-aligned to the scene's OWN safe padding (.scene is 110/150), so
   the row is flush at x1770 and starts at x761. The ken pushes the clock LEFT
   across the scene (ken out: xPercent +2.5 -> -2.5), so its right edge runs
   x715 -> x657 from the first chip's pop to the cut — 46px of clearance at the
   worst instant, widening to ~104px. 1.6 stays centred: its re-fetched
   photograph is a top-down flat-lay with no left-weighted subject to clear. */
#s2-chips { justify-content: flex-end; padding-right: 150px; }
</style>
</head>
<body>
<div id="root" class="cut-en" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="${ROOT}">
${sc.map(scene).join("\n")}

<!-- Voice only. The bed and the SFX are the post-mix step (assets/audio.json ->
     tools/audio/mix.py): the renderer does not guarantee in-page volume
     automation, and a bed that silently failed to duck would bury the voice in a
     video that still passed every check. -->
${audio}

</div>

<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/lottie.min.js"></script>
<!-- The UNDERSCORED file. A hyphen in the basename emits
     window.L_phone-notify-credit=… , which is a syntax error that leaves the
     global undefined and renders a blank scene with every check green (the trap
     that hit this run's hi ch1). Loaded BEFORE motion.js. -->
<script src="assets/lottie/phone_notify_credit_usd.js"></script>
<script src="assets/js/motion.js"></script>
<script>
/* S = scene starts · D = each scene's OWN hold (not its dissolve-padded
   data-duration), so the photograph's push finishes exactly as the next scene
   begins to fade up. Both generated from timing.json. */
var S = ${map((s) => s.start)};
var D = ${map((s) => s.dur)};
var IDS = ${JSON.stringify(sc.map((s) => s.id))};

/* Cross-dissolves, one call, before the per-scene cues. No shove in chapter 1:
   the cut's two act changes are s39 -> s40 and s58 -> s59, both far downstream.
   s3 -> s4 is a HOLD, which is mechanically a dissolve — what makes it a hold is
   that both scenes are one photograph under one continuous zoom and the joint
   takes no "transition" SFX. */
sceneTransitions(IDS, S);

/* THE PHOTOGRAPH CARRIES THE MOTION — one move per scene, never a plate push
   competing with a ken. Direction alternates from s1's push-in and does NOT flip
   across the s3 -> s4 hold: plateKen chains 1.00->1.08->1.16 so the two scenes
   read as one uninterrupted push on one image. */
${kenJs}

/* THE TYPE — cue ladder variant A (storyboard §5): kicker +0.30, statement
   +1.10. Fixed offsets, constant whatever a clip's length; every gap is 0.80s,
   and the photograph is already up at +0.00 so first_cue_by_seconds (0.5) is
   met by the kicker. Chapter 1 carries no rate, sub or foot line, so variant A's
   cues 3 and 4 are absent by design, not dropped. */
${sc.map((s) => `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 14);`).join("\n")}
${sc.filter((s) => s.stmt && s.art !== "lottie" && !s.role)
    .map((s) => `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 18);`).join("\n")}

/* 1.7 · THE VERDICT SLAM. §2: the five verdict scenes take pop() (back.out(1.7))
   on their stmt instead of rise(). That IS the slam — it needs no .stamp pill
   and no new copy, and it is what makes the "stamp" SFX legal here. */
pop("#s7-stmt", S.s7 + 1.10, 0.6);

/* 1.2 / 1.6 · the declared cascades, ladder variant C. The chips ARE the
   statement, so there is no stmt cue: +1.10 / +1.70 / +2.30, a fixed 0.6s gap
   (format.json layout.cascade), all three landed by +2.75. D's own rule draws
   in first, under the kicker. */
${sc.filter((s) => s.brule).map((s) => `fill("#${s.id}-br", S.${s.id} + 0.15, 0.6);`).join("\n")}
${sc.filter((s) => s.chips)
    .map((s) => `popEach("#${s.id}-chips .chip", S.${s.id} + 1.10, 0.60, 0.45);`).join("\n")}

/* 1.6 · THE COUNT BEING PAID. The three cells ride the SAME 0.6s cascade the
   chips did (+1.10 / +1.70 / +2.30), and each tick strikes 0.5s after its own
   cell lands, so the row reads item -> paid, item -> paid. The last mark
   completes at +3.25 — inside chapter_design's "assemble by about +3.3", so the
   contact sheet's +2.6 sample shows a row mid-build rather than a broken one,
   and the scene's own 5.711s hold leaves it settled for 2.5s. */
${sc.filter((s) => s.ticks).map((s) =>
  [`popEach("#${s.id}-ticks .v-tickcell", S.${s.id} + 1.10, 0.60, 0.45);`]
    .concat(s.ticks.map((t, n) =>
      `draw("#${s.id}-tick${n + 1}", S.${s.id} + ${(1.60 + n * 0.60).toFixed(2)}, 0.45, 110);`))
    .join("\n")).join("\n")}

/* 1.4 · THE BUZZ. An undefined global is the exact shape of the bug this asset
   already shipped once: lottie draws nothing, no error, every check green. Make
   it loud. The stmt follows the banner at +2.75 — the words are the consequence
   of the buzz, not its caption. */
if (!window.L_phone_notify_credit_usd)
  throw new Error("window.L_phone_notify_credit_usd is undefined — the Lottie DATA file did not load");
var s4art = loadLottie("#s4l", window.L_phone_notify_credit_usd);
playLottie(s4art, S.s4 + ${LOTTIE_AT}, ${LOTTIE_DUR.toFixed(2)});
rise("#s4-stmt", S.s4 + 2.75, 0.7, 18);

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE TWO RATE ASSERTS — run.json.constraints, mechanised.

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number. A number
       without its assumption visible is a fabricated promise."

   (2) derived_income_carries_assumption (EXTENDED 2026-08-07 during hi ch2
       review): a DERIVED INCOME figure — "what \$X buys", i.e. the corpus's own
       OUTPUT — is the promise the video actually makes, so it carries the rate in
       frame or an explicit ILLUSTRATIVE marker, exactly like a corpus. The
       letter of (1) let the hi cut's bare "WHAT 2,500 A MONTH BUYS" through;
       this closes it.
       A BLS bill divided by twelve is NOT derived income — it is arithmetic on a
       published statistic — so the marker branch accepts a stated provenance
       (BLS / CONSUMER EXPENDITURE) as well as ILLUSTRATIVE.

   Chapter 1 renders no figure at all, so both are vacuously true here. They are
   wired NOW so chapters 2-6 inherit them rather than bolting one on after the
   first bare number has already rendered — which is exactly how this shipped
   twice. Throwing is the point: "hyperframes check"'s runtime pass fails on an
   uncaught page error, and a silent console.warn is what let it through before.
   =========================================================================== */
(function () {
  var CORPUS  = /\\$(?:254,225|332,950|656,650|1,500,000|1,929,260|1,963,375|5,555,556|7,271,759)/;
  var RATE    = /4\\.0%|3\\.11%|1\\.08%/;
  var DERIVED = /\\$[\\d,]+\\s*(?:a month|A MONTH|per month|PER MONTH)/;
  var MARKER  = /ILLUSTRATIVE|BLS|CONSUMER EXPENDITURE/;
  var bad = [];
  Array.prototype.forEach.call(document.querySelectorAll("section.scene"), function (s) {
    var txt = s.textContent;
    var rated = Array.prototype.some.call(
      s.querySelectorAll('[id^="' + s.id + '-rate"]'),
      function (el) { return RATE.test(el.textContent); });
    var c = txt.match(CORPUS);
    if (c && !rated)
      bad.push(s.id + " renders " + c[0] + " with no #" + s.id + "-rate carrying a rate");
    var d = txt.match(DERIVED);
    if (d && !rated && !MARKER.test(txt))
      bad.push(s.id + " renders the derived income " + d[0] +
               " with neither a rate nor an ILLUSTRATIVE marker in frame");
  });
  if (bad.length) throw new Error("RATE ASSERT FAILED — " + bad.join(" · "));
})();
</script>
</body>
</html>
`;

fs.writeFileSync("index.html", html);

/* ------------------------------------------------------------- the sound pass
 * Emitted here, from the SAME scene starts as the markup, so a cue can never
 * drift off the joint it is bound to. Times are CHAPTER-LOCAL; the bed and the
 * SFX are mixed in post by tools/audio/mix.py, never as <audio> rows.
 *
 * This reproduces tools/audio/cues.py's derivation exactly (verified by running
 * it read-only against this file and diffing), with one correction the tool
 * cannot make: cues.py hardcodes `music: bed-resolve`, and storyboard §2/D12
 * chooses **bed-tension** for this cut — its argument is a COST, not a habit.
 * The bed is a per-video fact.
 *
 * The rules, from tools/audio/kit.json's helper column + storyboard §2:
 *   · a `transition` at every scene joint EXCEPT the chapter's own first scene
 *     (there is no joint to announce at t=0) and EXCEPT a HOLD — s3 -> s4 is one
 *     object under one continuous zoom, and a whoosh there announces a change
 *     that is deliberately not happening.
 *   · `buzz` on s4, the kit's ONLY diegetic sound, legal precisely because the
 *     frame shows the object making the noise. Declared at +1.85 in the cut's
 *     cues-tables.json; the Lottie's own jitter is timed to cover it (above).
 *   · `stamp` on s7, bound to the pop() on its stmt.
 *   · everything else in ch1 is a DECLARED DRY beat (§2: "the what-if is paid in
 *     recognition, not punctuation"). Punctuating a coffee mug makes it a joke.
 */
const HOLDS = [["s3", "s4"]];
const cues = [
  ...sc.slice(1)
    .filter((s) => !HOLDS.some(([, b]) => b === s.id))
    .map((s) => ({ at: s.start, name: "transition", _: `${s.id} joint` })),
  { at: +(sc[3].start + 1.85).toFixed(3), name: "buzz",
    _: "s4 · the frame SHOWS the phone making the noise and the Lottie banner is "
      + "jittering on this offset — the kit's one diegetic cue, and one of only "
      + "two sounds in the cold open" },
  { at: +(sc[6].start + 1.10).toFixed(3), name: "stamp",
    _: "s7 · the verdict slam — pop() on the stmt, the packaging promise landing" },
].sort((a, b) => a.at - b.at);

fs.writeFileSync("assets/audio.json", JSON.stringify({
  _comment: "Chapter 1 sound pass, -en. Times are CHAPTER-LOCAL. Generated by "
    + "build.mjs from the same scene starts as index.html, and diffed against "
    + "tools/audio/cues.py's derivation. Merge into the full cut by adding this "
    + "chapter's offset (0.000s) to every `at`.",
  _density: `${cues.length} cues over s1-s8 / ${ROOT}s`,
  _dry: "s1-s6 and s8 are DECLARED DRY (storyboard §2): they take their joint "
    + "transition and no content cue. s7's stamp and s4's buzz are the only two "
    + "sounds in the cold open.",
  music: "bed-tension",
  sfx: cues,
}, null, 1) + "\n");

console.log(`assets/audio.json: ${cues.length} cues`);
console.log(`index.html: ${sc.length} scenes, root ${ROOT}s, offset ${OFF}s`);
sc.forEach((s) => console.log(
  `  ${s.id} ${s.line}  start ${String(s.start).padStart(7)}  dur ${String(s.dur).padStart(6)}` +
  `  d-dur ${String(s.dd).padStart(6)}  track ${s.track}  ${s.arch.toUpperCase()}` +
  `${s.ctr ? " centred" : ""} ${s.art}${s.size ? "  focal " + s.size : ""}`));
