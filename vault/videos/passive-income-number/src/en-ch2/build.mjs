/* build.mjs — emits index.html + assets/audio.json for CHAPTER 2 of
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
 * Chapter 2 is lines 2.1-2.15 = scenes s9-s23. The chapter's rebase constant is
 * timing.json's own scene_start for 2.1 (46.420s) and is subtracted from every
 * start, exactly as ch1 does with its 0.000.
 *
 * SPEC, not invention. The arch / ground / art / centred / focal / ken columns
 * below are vault/videos/passive-income-number/storyboard-en.md §7 verbatim, and
 * the kicker / stmt / num / foot strings are script-en.md's own `[arch …]` cue
 * blocks (one home per fact — the storyboard deliberately does not restate copy).
 *
 * TWO RULINGS CARRIED IN FROM THE ch1 CEO GATE, both implemented here:
 *
 *  1. THE TANK (run.json chapters.en.1.ceo_carry_forward_s10). fin-assets could
 *     not source a tank in 6 sheets / 36 candidates; s10 resolves as a row of
 *     brass taps on a steel manifold over a steel trough — the storyboard's OWN
 *     written fallback (§10: "the tap is what carries the rhyme, not the tank's
 *     silhouette"). The live risk was 2.2's VO saying "tank" over a frame with
 *     no vessel. Fixed in the COPY, not by re-fetching: **the noun on screen is
 *     THE TAP**, and #s10-sub names both halves of the metaphor at +1.90 —
 *     within ~0.4s of the spoken word "tank" — so the word and the picture
 *     arrive together instead of contradicting each other.
 *     ⚠ s46 / s47 / s57 (ch4, ch5) INHERIT THIS NOUN. The object family is a
 *     brass tap on plain steel under workshop light. Not a tank silhouette.
 *
 *  2. TONE (run.json chapters.en.1.ceo_carry_forward_tone). ch1 runs one band
 *     end to end. ch2's opening is measurably lighter by three levers that are
 *     all inside the locked grade: the photographs (s9 YHIGH 203 / s10 170 /
 *     s11 211 against ch1's opener), the ground (#2a2113 amber against ch1's
 *     #161f2b cool first light), and the ROLE — s9/s10/s11 are `--target`
 *     scenes, so they carry an amber `--tint` on scrim layer 1 and an amber
 *     `--gl` glow, where seven of ch1's eight scenes carry neither. Measured
 *     p90s are in the build log; there is no per-scene grade override anywhere
 *     in this file and there may not be one.
 */
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const CH = 2;
const LINES = ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8",
               "2.9", "2.10", "2.11", "2.12", "2.13", "2.14", "2.15"];
const FIRST = 9;                                    // scene s9 == line 2.1
const TIMING = JSON.parse(
  fs.readFileSync("../passive-income-number-en/assets/voice/timing.json", "utf8"));
const T = 0.45;                                     // format.json scene.transition_seconds

const TARGET = "245,158,11";
const FUND   = "34,197,94";

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`            f1     §7 `ground` (the --f1 temperature arc, §11)
 * art    §7 `art`             ctr    §7 `ctr` (centred)
 * ken    §5: the direction flips at every boundary except a hold. ch1 ended on
 *        s8 `i`, so ch2 opens `o` and alternates. s10's two framings are ONE
 *        push (1.00 -> 1.06 -> 1.16, §6a) and do not flip between themselves.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · 49-89 -> 76.
 *        Computed below, never written here.
 * role   §1: amber = a published figure under examination (2.1-2.9), green = a
 *        division that closed at a sourced rate (2.10-2.15). 2.4, 2.6 and 2.12
 *        carry NO role: a numerator is not an answer and a document is not a
 *        finding. Three colourless frames in fifteen is the §1 count, not a gap.
 */
const SCENES = [
  { line: "2.1", arch: "a", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "START WITH THE RATE", stmt: "A number without a rate is a wish.",
    img: "s9.jpg",
    note: "START WITH THE RATE. The chapter opens amber and BRIGHT — a blank kraft notebook and a sharpened pencil, YHIGH 203, against ch1's cool first light. That step is the ch1 CEO carry-forward (tone) and it is made of the photograph, the ground and the role tint, never of a grade override." },

  { line: "2.2", arch: "d", f1: "#2e2411", art: "tank", ctr: false, ken: "i", role: TARGET,
    band: true, brule: 450,
    kenFrom: 1.00, kenTo: 1.06,
    kick: "THE TAP", stmt: "How much can you draw each year without emptying it",
    sub: "THE TANK IS WHAT YOU SAVED · THE TAP IS WHAT YOU DRAW",
    img: "s10.jpg", img2: "s10b.jpg", swap: 6.810, ken2From: 1.06, ken2To: 1.16,
    note: "THE TAP — 10.596s, the cut's only max_scene_seconds breach, resolved INSIDE the scene by §6a: s10.jpg under plateKen 1.00->1.06, then a 0.40s cross-dissolve to s10b.jpg (a derived crop of the SAME frame, crop=1600:900:132:250) continuing 1.06->1.16. Two framings, 6.810 + 3.786, longest well clear of 9.0. THE SWAP IS MEASURED, not interpolated: §5 anchors it to the word 'draw' and gives f 0.62 (+6.324) only as a fallback, and faster-whisper puts 'draw' at 6.760s into the clip = scene +7.010, so the dissolve starts at +6.810 and its MIDPOINT — the perceptual cut — lands on the word. THE TANK RULING: no tank could be sourced in 6 sheets, the frame is a row of brass taps on a steel manifold, so the kicker names what is actually on screen and #s10-sub names the pair at +1.90 — measured, 'tank' is spoken at scene +2.21 to +2.39 and the sub's 0.5s fade completes at +2.40, so the word and the picture arrive together. s46/s47/s57 inherit THE TAP. ⚠⚠ THE TANK IS NOW DRAWN — `owed.en_ch2_s10_tank_layer`, landed 2026-08-12 in the pre-assembly pass, pre-authorised 2026-08-10 and owed ever since. It is NOT a review round and it does NOT reopen this scene's image decision: the photograph is byte-identical, still full-bleed, still two declared framings, and every data-start, data-duration and data-framings above is untouched. THE POINT IS ORDER, not decoration: 4.7 says «Go back to the tank» and 5.5 calls it back again, and until this landed the device was planted at its own callback and nowhere earlier. The sentence THE TANK RULING above is the record of why it could not be photographed (6 sheets, 36 candidates, then 4 more in ch4) and it stands — what changed is that the ruling of 2026-08-10 authorised DRAWING what could not be found. The kicker still names what is on screen and #s10-sub still names the pair at +1.90, and the sub is now literally true of the frame: THE TANK IS WHAT YOU SAVED sits over a drawn tank, THE TAP IS WHAT YOU DRAW over a drawn tap AND seven photographed ones. ⚠ THE LEVEL IS DECORATIVE AND ASSERTS NO QUANTITY (`no_return_promise`) — no tick, no scale, no numeral and NO GHOST of the previous level, all four asserted on the emitted markup, and the fill is the upper slice ARRIVING rather than a rect sliding, so it is a state and not a distance. That is the exact mirror of 4.7, where the same slice exits. `.centred` COMES OFF and that is the one consequence this drags with it: `.scene.centred .plate` is display:none, so a centred scene structurally cannot hold a drawn layer — the same trade s14, s17, ch4's 4.7 and ch5's 5.5 and 5.9 all made. The type returns to archetype D's own declared layout, top-left under the brule at 400, and NOTHING was resized: the focal is still 76, the ladder floor, and still the same string. `.band` and not `.art-lift`: rule 9 forbids darkening the photograph, and `.art-lift` is a corner-plate mechanism this chapter already ruled off p-c and p-a (see s14) — p-d is the full-width bottom two-thirds, so a lift would be the whole-frame lever by another name. ⚠ THE ART IS LIFTED to ART_OP 0.74 (item 4 of the same batch), MEASURED on rendered frames rather than computed pre-scrim, which is the error that produced the miss elsewhere. See the s10 geometry comment for the region's measured ground and ART_OP for the two limits the value is chosen against. MEASURED ON RENDERED FRAMES (snapshots/qa/b2), and in BOTH declared framings so the swap cannot be hiding a difference: the vessel wall reads rgb 84 on a ground of 16 at 8.56s (framing 1) and rgb 83 on 15 at 13.66s (framing 2) — 2.48:1 and 2.49:1, dRGB 66.0, against the 1.80:1 the same measured line gives at .52. Arrival is measured too, not asserted: at 6.66s the wall region is rgb 17 against a ground of 16, i.e. the layer is genuinely absent before its cue. Rule 9 is never reached — the drawn ink sits at L 0.089, between the photograph's own p99 (0.026) and p99.9 (0.145), and the amber focal above it is L 0.427, so the drawing is a fifth of the type and nothing in the picture was darkened. ⚠ ONE THING THE RATIO CANNOT SEE, recorded so it is not re-measured as a defect: the water is `--target` at fill-opacity .5 over a warm trough, rgb 53 on 33 — a CHROMA edge (+20 red, +13 green, -1 blue) that a luminance ratio scores at 1.19:1 and that is plainly a filled block on the frame. Judge the water on dRGB or on the picture, never on the ratio." },

  { line: "2.3", arch: "a", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "NOT A LAW", stmt: "Four percent is a finding.\nNot a law.",
    img: "s11.jpg",
    note: "NOT A LAW. One rusted nail through a weathered plank with nothing hanging on it — the line's own image of a rule that was never nailed down. Written as words, not as `4.0%`: the rate token belongs to 2.9, where it is the working number." },

  { line: "2.4", arch: "c", f1: "#1a1e24", art: "off", ctr: true, ken: "i",
    kick: "TWO PAPERS", stmt: "Both have names and dates.",
    img: "s12.jpg",
    note: "TWO PAPERS. First of the four-scene C run (§7): the ARTEFACT changes underneath while the layout holds, because the four lines are one evidentiary case. Two blank sheets on walnut. No role — a document is not a finding, and colour is a signifier in this cut. Neutral-cool ground, the first cooling step of the chapter." },

  { line: "2.5", arch: "c", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "PAPER ONE", stmt: "William Bengen, Journal of Financial Planning",
    foot: "\"Determining Withdrawal Rates Using Historical Data\", October 1994, vol. 7 no. 4, pp. 171-180",
    img: "s13.jpg",
    note: "PAPER ONE. An open book, macro, text dissolved by depth of field — §10 forbids a legible title, so the citation lives in the foot and never in the photograph. The straight quotation marks are VERIFIED present in the 97-codepoint subset (dumped at build; see the log)." },

  { line: "2.6", arch: "c", f1: "#191f28", art: "split", ctr: false, ken: "i",
    kick: "WHAT HE TESTED", stmt: "50% stocks\n50% bonds",
    foot: "Retirement start years 1926-1966, withdrawals inflation-linked after year one",
    img: "s14.jpg",
    note: "WHAT HE TESTED. ⚠ REBUILT at fin-editor's blocker #2 (en ch2 r1): the card catalogue says a lookup system exists and cannot say HALF AND HALF, and 50-50 was the only ratio in the chapter with neither a photograph nor a drawing behind it — s16 got the 95/100 grid, s18 got ÷4% = ×25, and the beat that is literally a proportion got a filing cabinet. It now carries the chapter's THIRD drawn layer, `split-bar` on p-c: one track, filled to EXACTLY 0.500. Two consequences the fix drags with it, both deliberate. (1) The scene leaves `.centred`: `.scene.centred .plate` is display:none, so a centred scene structurally cannot hold a drawn layer — and `.centred` exists for a split with NOTHING opposite, which is no longer this scene. It returns to archetype C's own declared layout, type left in the 880px column, artefact right, which is what §7 assigned it in the first place. (2) The 880px column will not hold 22 characters at 112px (~1364px), so the separator becomes a LINE BREAK: `50% stocks` / `50% bonds`, two 10-character lines at the ladder's top step. The focal is not shrunk — the ladder is untouched and the copy is the same two items, typeset as two lines instead of joined by this cut's `·`. NO `.art-lift`, tried and rejected on the frame: the source is pale birch (p50 67 in the plate region before the grade) which is §8's stated trigger for it, but p-c is 934x1200 — a full-height quarter of the frame, not s16's 860x610 corner — so the lift painted a hard-edged near-black panel over the right side and erased the photograph it is required to keep. Snapshotted both ways at +2.95 (snapshots/qa/r2b1 vs r2b2). The graded plate region measures dark enough that the amber half and the .22 ghost both read as an aperture. ⚠ CARRY-FORWARD: `.art-lift` is a corner-plate mechanism. Do not reach for it on p-c or p-a. ⚠ r3: the ghost track moves from a DEAD `opacity=.22` (clobbered by its own `fade`) to a live `fill-opacity` GHOST_A .55, so the UNFILLED half stops out-shouting the FILLED one — see the constant's own note above. Geometry, tick and `art-forward .52` are byte-unchanged." },

  { line: "2.7", arch: "c", f1: "#2e2411", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "PAPER TWO", stmt: "Three Trinity University professors.",
    foot: "Cooley, Hubbard and Walz, \"Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable\", AAII Journal, February 1998, pp. 16-21 — the Trinity Study",
    img: "s15.jpg",
    note: "PAPER TWO. ⚠ RE-FETCHED IN PLACE at the CEO's blocker #2 (en ch2 r1) — the note that stood here described the file this replaced (a closed volume, macro on the corner and page block), which the 1.16x ken push turned into an unidentifiable pale curve and which was the chapter's second sound-off failure inside the 39-second document run. Same filename, so the composition never moved: what changed is the picture. It is now a cloth-bound volume open flat beside three worn volumes with cracked spines, warm window light — the storyboard's own written cue, sourced at last. Fourth artefact, fourth scale, and it now differs from s13 on all three axes the gate asked for (scale, context, colour temperature) rather than only on scale. The foot is the longest string in the chapter and wraps to two 26px lines inside the centred 1500px stack." },

  { line: "2.8", arch: "b", f1: "#372a0c", art: "grid", ctr: false, ken: "i", role: TARGET,
    lift: true, vrule: [150, 300],
    kick: "WHAT THEY FOUND", num: "95%", numTo: 95, numSuffix: "%", numAt: 3.33,
    foot: "4.0%, inflation-adjusted withdrawals, 30-year payout: 95% of periods at 100% stocks and at 50-50 — Trinity Table 3, data 1926-1995",
    note: "WHAT THEY FOUND — the deepest amber in the video (#372a0c, spent exactly once, §11) and the chapter's first drawn layer. `survival-grid`: 95 solid cells of 100, five left as ghosts. Rule 8 holds because the photograph (a stack of paper corners) can say a study exists and cannot say 95 OF 100. `.art-lift` because the p-b plate sits on the BRIGHT right two-thirds of this still — the plate-scoped form of rule 9, which darkens behind the art and cannot touch the photograph outside the rect. The near-black left third is where the type goes.",
    img: "s16.jpg" },

  { line: "2.9", arch: "a", f1: "#2a2113", art: "dates", ctr: false, ken: "o", role: TARGET,
    verdict: true, band: true,
    kick: "THE WORKING NUMBER", stmt: "4.0% — a finding with a date.\nNot a promise.",
    img: "s17.jpg",
    note: "THE WORKING NUMBER — a verdict scene. Its stmt enters with `pop` (back.out(1.7)) rather than `rise`; that IS the slam, and it is what makes the `stamp` SFX legal without a .stamp pill or one word of new copy (§2, §13 D10). ⚠ THE DATE IS NOW DRAWN — fin-editor's blocker #1 (en ch2 r1). The line is 'a finding WITH A DATE' and there was no date, no calendar and no year anywhere in the frame; `format.json vector_art.reach_for_it_when` names 'a date being circled' as a FAIL as a flat photo, verbatim, and a box of rubber stamps additionally connotes STAMPED / APPROVED — the register the second line exists to deny. `date-axis` on p-a rings the two publication dates the chapter has already put on screen (s13's October 1994 foot, s15's February 1998 foot) on a short time line that STOPS after the second one: no photograph can say 'these two dates, and nothing promised after them'. Drawn rather than re-fetched because the fetch was already spent and the assertion is not photographable. The archetype is unchanged (A is a centred stack over a full-bleed motif) — `.centred` comes off only because it would display:none the plate, and A's stack is centred by default, so the type does not move. `.band` and not `.art-lift`: the plate here IS the whole frame, so a lift would darken the entire photograph (rule 9), and the kraft paper under the motif measures p50 97 after the grade — the brightest ground in the chapter." },

  { line: "2.10", arch: "d", f1: "#0f2a1a", art: "division", ctr: false, ken: "i", role: FUND,
    band: true, brule: 400,
    kick: "THE WHOLE METHOD", stmt: "annual bill DIVIDED BY 4.0%\n= the money behind it",
    img: "s18.jpg",
    note: "THE WHOLE METHOD — green begins here: a division that closed at a rate the video has sourced (§1). `division-block` is the shape of the arithmetic the entire cut runs: a bill block, a heavy 12px divisor rule, an equals, and a corpus block EXACTLY 25.00x wider, because dividing by 0.04 IS multiplying by 25. The photograph is a hand writing on a kraft tag; it cannot state a ratio, which is what makes the drawing additive. `.band` under the mechanism (rule 9 — never darken the photograph) and D's own `brule` above it." },

  { line: "2.11", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "FOOD, ONE YEAR", num: "$10,169", numTo: 10169, numPrefix: "$", numAt: 2.21,
    foot: "Average annual food spending per consumer unit, 2024 — BLS Consumer Expenditures, released 19 Dec 2025, USDL-25-1586",
    img: "s19.jpg",
    note: "FOOD, ONE YEAR. The numerator, amber: a published figure under examination, never green — a BLS bill is not an answer (§1 thesis check). The foot carries the full provenance, which is also what satisfies the BILL branch of the assert below AND tools/check_vo_frame.py, whose MAGNITUDE pattern fires on this line's spoken 'ten thousand'. Egg carton and greens on a dark table: owns 'food' without borrowing s20's bag or s21's loaf." },

  { line: "2.12", arch: "b", f1: "#1f1e1c", art: "off", ctr: true, ken: "i",
    kick: "PER MONTH", num: "$847", numTo: 847, numPrefix: "$", numAt: 2.27,
    foot: "$10,169 divided by 12 — arithmetic, not a separate statistic",
    img: "s20.jpg", bgpos: "center bottom",
    note: "PER MONTH. NO role, deliberately: a division of a published statistic by twelve is a measurement, not a landing (§1, §2's dry list). The foot states the derivation on screen, which is what keeps this figure honest and out of the derived-income branch — it is a bill walked down to a month, not income drawn off a corpus (§4, 'what the assert must NOT fire on'). ⚠ `bgpos` is the KEN OFFSET, fin-editor/CEO should-fix #3 (en ch2 r2): the ITALIAN EGGPLANT card's own orange `$5.` ink crossed the kicker's baseline through `R M O`. `.band` was the other offered route and it is GEOMETRICALLY INCAPABLE here — `.band` is bottom:0 height:54%, so it starts at y 497 at alpha 0, and the kicker's glyphs measure y 438-459. It cannot reach the collision, and dropping the type to meet it would move a reviewed layout. The offset is one line and costs no layer: `.bg` is inset -8% with `background-size:cover`, and s20's 1880x1253 source renders 1484px tall inside a 1253px box, so there are 231.6px of VERTICAL slack and exactly ZERO horizontal (the source is 1.50 against the box's 1.78). `center bottom` spends 115.8px of that slack, lifting the whole price-card row 116-134 frame px clear of the kicker across the ken's 1.00-1.16. Nothing else changes: same file, same grade, same ken call, same direction, same stack." },

  { line: "2.13", arch: "b", f1: "#12351f", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "RUNG ONE", rate: "AT A 4.0% WITHDRAWAL RATE",
    num: "$254,225", numTo: 254225, numPrefix: "$", numAt: 2.55,
    foot: "$10,169 divided by 0.04 · ILLUSTRATIVE ARITHMETIC",
    meas: 0.1295, mlab: "THE LADDER",
    img: "s21.jpg",
    note: "RUNG ONE — the chapter's peak and the first corpus in the video. #s21-rate is a first-class 40px .sub in the role colour and it arrives at +1.10, BEFORE the number lands at +2.55: the assumption is on screen first and the figure arrives into it (§4). The measure bar is the §9a corpus ladder at ONE scale for the whole cut — 920px = $1,963,375, so $254,225 is scaleX 0.1295 = 119.1px. Numerator and denominator are a PAIR (gotcha 7): never move one without the other and never re-use this component at another scale. Six countable elements, exactly the ceiling." },

  { line: "2.14", arch: "b", f1: "#12351f", art: "off", ctr: true, ken: "i", role: FUND,
    kick: "WHAT IT REPLACES",
    stmt: "$254,225 at 4.0% · the grocery bill stops costing hours", rateSpan: "4.0%",
    img: "s22.jpg",
    note: "WHAT IT REPLACES. §4's SECOND rate form: the rate is an inline span INSIDE the focal, carrying the role colour and taking a `pulse` at +1.90 — no copy reordered, nothing printed twice, and a real node for the assert to find. A rack of BLANK US time cards: fin-assets got better than the cue asked for, because hours ABSENT under 'stops costing you hours' is the line rather than a decoration of it." },

  { line: "2.15", arch: "a", f1: "#0f2a1a", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "RUNG ONE", stmt: "Same bill. Your hours are free.",
    img: "s23.jpg",
    note: "RUNG ONE, said again as the chapter closes — the kicker repeats because the script's head does (copy has one home). Easing off the deepest green to #0f2a1a. A tight framing on three rungs of a wooden ladder against dark planks: ch1's s8 is the whole outdoor ladder wide and s74 is the full height, so this is the third statement of the object, not a reuse. The chapter's LAST scene, so it carries its BARE scene_duration — there is no successor inside this project to cross-dissolve into, and tools/cut_assemble.py adds the +0.45 back at fold-in." },
];

/* ------------------------------------------------------------- the timings
 * Read straight off timing.json, rebased by the chapter's own offset. GAPS —
 * not totals — are what a re-time destroys, so the gaps are asserted below
 * against the shipped measurement, one joint at a time. */
const flat = (t) => t.replace(/\n/g, " ");

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
  const n = FIRST + i;
  return {
    ...s, i, n, id: "s" + n,
    start: +(r.scene_start - OFF).toFixed(3),
    dur: own,                                                // the scene's own hold
    dd: i < SCENES.length - 1 ? +(own + T).toFixed(3) : own,  // + the cross-dissolve overlap
    track: n % 2 ? 1 : 2,                                    // or overlapping_clips_same_track
    astart: +(r.audio_start - OFF).toFixed(3),
    adur: r.duration,
    // the declared framings — one value per photograph the scene holds
    framings: s.swap ? [s.swap, +(own - s.swap).toFixed(3)] : [own],
    /* The focal size is keyed on the COPY's length, so a "\n" — which is a
     * typographic break decision, not copy — is flattened out of the count
     * first. Three statements carry one: without it the browser breaks
     * "Not a law." across two lines and leaves "law." alone, and splits
     * "Not a promise." between the two lines of 2.9. A break is a build
     * decision (the string is the script's); the SIZE ladder is untouched. */
    size: s.stmt == null ? null
      : flat(s.stmt).length <= 24 ? 112 : flat(s.stmt).length <= 48 ? 88 : 76,
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
/* format.json scene.max_scene_seconds. ch1 could assert on the whole scene
 * because no ch1 scene declared a second framing; 2.2 does, so the thing that
 * must clear 9.0 is the longest SINGLE FRAMING — which is exactly what §6a's
 * resolution buys. Framings must also partition the scene (check_build asserts
 * the same), or a cosmetic split would duck the guard. */
sc.forEach((s) => {
  const sum = +s.framings.reduce((a, b) => a + b, 0).toFixed(3);
  if (Math.abs(sum - s.dur) > 0.002)
    throw new Error(`${s.id} framings sum to ${sum}, scene holds ${s.dur}`);
  s.framings.forEach((f) => {
    if (f > 9.0) throw new Error(`${s.id} holds one photo for ${f}s (max 9.0)`);
  });
  if (s.swap && !s.img2) throw new Error(`${s.id} declares a swap with no second file`);
});
/* §3's build guard: no `/` and no `?` in any on-screen string. Both ARE in the
 * dumped 97-codepoint subset (verified at build with fontTools — so are the
 * curly quotes §14 left open, which settles that item for ch3's s34/s37), but
 * the storyboard bans them as COPY: `·` is this cut's separator and the cut
 * asks no rhetorical questions on screen. It also sweeps the ₹ this cut is
 * forbidden to show and any Devanagari that could arrive from the sibling cut. */
const strings = (s) =>
  [s.kick, s.stmt, s.num, s.rate, s.sub, s.foot, s.mlab].filter(Boolean).map(flat);
sc.forEach((s) => {
  strings(s).forEach((t) => {
    const bad = t.match(/[/?₹×≈~→▶¢]/);
    if (bad) throw new Error(`${s.id}: on-screen string carries "${bad[0]}" — banned in this cut`);
    if (/[ऀ-ॿ]/.test(t)) throw new Error(`${s.id}: Devanagari in the -en cut`);
  });
  if (s.stmt && s.num) throw new Error(`${s.id}: never a stmt AND a num (§3)`);
  if (s.size && s.size < 76) throw new Error(`${s.id}: focal below the ladder floor`);
  if (s.rateSpan && !s.stmt.includes(s.rateSpan))
    throw new Error(`${s.id}: rate span "${s.rateSpan}" is not in the focal`);
  /* the drawn layer never becomes the whole scene, and a centred scene has no
   * plate to put one in (.scene.centred .plate is display:none). */
  if (s.art !== "off" && s.ctr) throw new Error(`${s.id}: drawn art on a centred scene`);
  if (s.art !== "off" && !s.img) throw new Error(`${s.id}: art without a photograph`);
});

/* ---------------------------------------------------------- the drawn layers
 * FIVE, in a fifteen-scene chapter. ⚠ THAT IS ABOVE the archetype note's stated
 * calibration ("three or four in a twelve-to-fourteen scene chapter is the TOP
 * of the range") and it is DECLARED here rather than hidden: the fifth is the
 * tank on 2.2, landed 2026-08-12 by `owed.en_ch2_s10_tank_layer`, which is a
 * standing ruling pre-authorised on 2026-08-10 and owed ever since. Chapters
 * 3-6 must not read five as a new baseline — §8 budgets ch3 1, ch4 1, ch5 0,
 * ch6 3, and the tank is a CUT-LEVEL device planted once, not a chapter's
 * fifth idea. Two were planned in §8; s14's split-bar and s17's date-axis are
 * fin-editor blockers #2 and #1, each added because the beat is a PROPORTION
 * or a DATE that its photograph is structurally unable to state. All five are
 * `art-forward` and all five are authored in the PLATE's own coordinate space,
 * never in 1920x1080.
 *
 * ⚠ ONLY THE TANK CARRIES THE `--art-op` LIFT (item 4 of the same batch). The
 * other four were reviewed and locked ON THEIR ENCODE at `.art-forward`'s .52,
 * and re-lighting a frame nobody complained about is not what a pre-assembly
 * pass is for. */

/* ART_OP — the tank's resting level. `.art-forward` gives .52; this is what the
 * frame needs. `owed.en_preassembly_batch` item 4: `.plate` is z-index 0 and
 * `.scrim` is z-index 1, so THE SCRIM COMPOSITES OVER THE DRAWN ART while
 * `.stack` type sits above it untouched, and a contrast computed pre-scrim
 * lands at roughly half its predicted value. Known compensation, not a z-order
 * bug (chapter-design.css:96), so the z-order is untouched and the resting
 * opacity is the knob. Same constant, byte-for-byte, as ch4 and ch5 — three
 * chapters carrying one device must not carry three levels of it. The measured
 * before/after for this scene is in the s10 note; the reasoning about why the
 * design's 4.3-5:1 predictions are unreachable at ANY opacity is in ch4's
 * ART_OP comment, which is the one home for it. */
const ART_OP = 0.74;

/* s10 · THE TANK — p-d, viewBox 0 0 1920 656, `owed.en_ch2_s10_tank_layer`.
 * ⚠ THIS IS en ch4's OWN PARAMETERISED LAYER, COPIED AND NOT REDRAWN. The
 * constant and the function below are ../passive-income-number-en-ch4/build.mjs's
 * (which ../-ch5 also carries), with ONE moved origin and ONE added option, so
 * the three sites cannot drift into three different tanks. ch4's own comment
 * predicted this drop-in verbatim: "s10 is also arch D (storyboard §7), so the
 * plate rect and the viewBox are identical there and this drops in with
 * {drop:false, widen:false} — at 2.2 the tank is being FILLED and neither the
 * level nor the tap has moved yet."
 *
 * WHY IT IS HERE AT ALL, AND IT IS AN ORDERING ARGUMENT, not a decoration one:
 * the script plants the device at 2.2 ("you filled a tank slowly, over years")
 * and calls it back at 4.7 ("Go back to the tank") and 5.5. Until this landed,
 * en's tank was planted at its own CALLBACK and nowhere earlier — the viewer
 * was told *go back* to a thing they had never been shown. With it the cut
 * reads plant (2.2) -> callback (4.7) -> callback (5.5).
 *
 * RULE 8, ON THE OBJECT: the photograph is seven brass lever valves on a
 * horizontal steel manifold over a copper trough. It is a picture of OUTLETS.
 * What no photograph of a row of taps can assert is the FINITE VESSEL behind
 * them — that what is drawn from is a thing that was filled and can be emptied,
 * which is the whole of line 2.2. That is additive, not depictive. The
 * photograph is untouched and full-bleed; `image_per_scene` is not in play.
 *
 * ⚠ THE LEVEL IS DECORATIVE AND ASSERTS NO QUANTITY (`no_return_promise`; the
 * script says so at 2.2 in the same breath as authorising the drawing). Four
 * things are deliberately absent and asserted absent below: a tick, a scale, a
 * numeral, and a ghost of the previous level. The level does not slide either
 * — it is two rects and the upper slice ARRIVES, so the change reads as a
 * STATE and not as a distance travelled up a scale. That is the exact mirror
 * of 4.7, where the same upper slice EXITS: same markup, opposite cue,
 * opposite direction, no marker of where it was.
 *
 * ORIGIN MOVED 600 -> 150, and it is measured rather than preferred. ch4's x600
 * puts the drawn vessel on the centre of THIS frame, which is where the
 * PHOTOGRAPHED taps are (the bright brass runs screen x950-1350 in framing 1) —
 * a drawn tap over a photographed tap is rule 8's depictive failure. x150 is
 * the type column's own left margin and s18's bill-block edge in this same
 * plate, so the vessel wall, the focal and the chapter's other p-d mechanism
 * all hang off one line; and it puts the vessel over the copper trough, which
 * is the emptiest part of the picture in BOTH declared framings and is the half
 * of the photograph that already reads as a container. MEASURED on rendered
 * frames at 8.0s and 13.0s (snapshots/qa/pre1, before any of this landed): the
 * region screen x150-824 / y604-960 carries p50 L 0.0097 / p90 0.0172 in
 * framing 1 and p50 0.0120 / p90 0.0169 in framing 2 — dark and flat in BOTH,
 * which is what a mechanism needs and what a `data-framings` swap makes hard to
 * get. The centre (x600-1297, ch4's rect) measures no darker, so this is a
 * subject decision and not a luminance one.
 *
 * PLACEMENT ARITHMETIC. The box is 697x356 at plate (150,180) => screen
 * x150-824 (the tap fixture ends at 824), y604-960: below the `.band`'s start,
 * above the 970 bottom safe line, and 948px clear of the watermark box
 * (#root::after, x1772-1856 / y956-1040), which no scene may paint into.
 *
 * ⚠ `brule` IS 450 HERE AND 400 ON s18, and the difference is measured, not
 * taste: D's rule sits UNDER the type, and this stack is three elements deep
 * (kicker, a two-line 76px focal, and the sub) where s18's is two. At the
 * inherited 400 the rule struck through #s10-sub — caught on the first frame
 * of this pass at 8.56s (snapshots/qa/b1), which is the same shape as the
 * `.measure-lab` margin bug the creator caught on the encode. The stack's last
 * baseline measures y412; 450 clears it by 38px and still sits 154px above the
 * vessel.
 *
 * `stream:false` — the ONE added option. At 2.2 nothing is being drawn out
 * yet; the tap is on the vessel and shut. The stream is 4.7's beat (it widens)
 * and 5.5's (it closes), and emitting a rect this scene never animates would be
 * dead markup pretending to be a mechanism. */
const TANK = {
  x: 150, y: 180,                      // origin in the p-d plate's own space
  wall: 22, w: 556, h: 356,            // vessel outer box (open top)
  lvl: 120,                            // interior y where the water surface sits
  slice: 96,                           // the upper slice that ARRIVES as it fills
};
function tank(id, o) {
  o = o || {};
  const t = TANK, iw = t.w - 2 * t.wall, ix = t.x + t.wall;
  const fl = (x, y, w, h, cls, extra) =>
    `      <rect class="${cls}" ${extra || ""} x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  const floorY = t.y + t.h - t.wall;
  const surf = t.y + t.lvl;
  return [
    `<svg class="art v-tank" id="${id}-art" style="--art-op:${ART_OP}" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- the vessel: an open-topped tank you filled. Solid ink, ${t.wall}px walls. -->`,
    fl(t.x, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x + t.w - t.wall, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x, floorY, t.w, t.wall, "fl"),
    `      <!-- the water. TWO rects, not one sliding rect: the upper slice`,
    `           ARRIVES, so the change reads as a state and not as a distance`,
    `           travelled up a scale. No tick, no scale, no numeral, no ghost of`,
    `           the old level. -->`,
    fl(ix, surf + t.slice, iw, floorY - surf - t.slice, "flt", `id="${id}-lvl" fill-opacity=".5"`),
    fl(ix, surf, iw, t.slice, "flt", `id="${id}-lvlx" fill-opacity=".5"`),
    `      <!-- one tap, on the vessel's own wall: outlet, down-turn, stem, crossbar.`,
    `           Shut, and no stream: 2.2 fills, it does not draw. -->`,
    fl(t.x + t.w, t.y + 180, 118, 24, "fl"),
    fl(t.x + t.w + 94, t.y + 180, 24, 76, "fl"),
    fl(t.x + t.w + 45, t.y + 136, 22, 44, "fl"),
    fl(t.x + t.w + 13, t.y + 118, 86, 22, "fl"),
  ].concat(o.stream === false ? [] : [
    fl(t.x + t.w + 94, t.y + 256, 24, 100, "flt",
      `id="${id}-stream" fill-opacity=".5" style="transform-origin:0% 50%"`),
  ]).concat([`    </svg>`]).join("\n");
}
/* The four absences, asserted on the emitted MARKUP rather than promised in
 * prose — ch4's assert, carried over with it. ⚠ COMMENTS ARE STRIPPED FIRST,
 * and that is not tidiness: written naively this fires on the tank's own
 * comment saying "no tick, no scale, no numeral", i.e. it punishes the note
 * explaining the rule and is silenced by deleting it. */
{
  const svg = tank("sX", { stream: false }).replace(/<!--[\s\S]*?-->/g, "");
  for (const [what, re] of [["a numeral", /<text/], ["a tick or scale", /tick|scale|gauge/i],
                            ["a ghost level", /ghost|prev|before/i]])
    if (re.test(svg)) throw new Error(`tank: the level must carry no ${what} — it is decorative`);
  if (!/id="sX-lvlx"/.test(svg)) throw new Error("tank: the level slice is missing");
  if (/id="sX-stream"/.test(svg)) throw new Error("tank: 2.2 fills, it does not draw — no stream");
}


/* s16 · survival-grid — p-b, viewBox 0 0 800 610.
 * THE ARITHMETIC, stated at the point of edit (gotcha 7): 100 equal cells,
 * exactly 95 solid --target, 5 ghost. Trinity Table 3, 4.0% inflation-adjusted
 * withdrawals, 30-year payout.
 * GEOMETRY: cell 52 + gap 8 => 10*52 + 9*8 = 592 square, centred at x104/y9 in
 * the 800x610 window. `meet`, not `slice`: the plate is 860 wide, so slice
 * would scale 1.075x and crop 45px of height off a grid that is deliberately
 * square. 52px cells are far above the 9px floor for a fill over a graded
 * still. */
const GRID_SOLID = 95, GRID_N = 100, CELL = 52, CGAP = 8;
function survivalGrid(id) {
  if (GRID_SOLID !== 95 || GRID_N !== 100) throw new Error("survival-grid: not 95 of 100");
  const x0 = Math.round((800 - (10 * CELL + 9 * CGAP)) / 2);
  const y0 = Math.round((610 - (10 * CELL + 9 * CGAP)) / 2);
  const rowsOut = [];
  let solid = 0;
  for (let r = 0; r < 10; r++) {
    const cells = [];
    for (let c = 0; c < 10; c++) {
      const k = r * 10 + c;
      const x = x0 + c * (CELL + CGAP), y = y0 + r * (CELL + CGAP);
      if (k < GRID_SOLID) { solid++; cells.push(`<rect class="flt" x="${x}" y="${y}" width="${CELL}" height="${CELL}"/>`); }
      else cells.push(`<rect class="fl" opacity=".22" x="${x}" y="${y}" width="${CELL}" height="${CELL}"/>`);
    }
    rowsOut.push(`      <g class="gr" id="${id}-r${r + 1}">${cells.join("")}</g>`);
  }
  if (solid !== 95) throw new Error(`survival-grid drew ${solid} solid cells, not 95`);
  return `<svg class="art" id="${id}-art" viewBox="0 0 800 610" preserveAspectRatio="xMidYMid meet">\n${rowsOut.join("\n")}\n    </svg>`;
}

/* s18 · division-block — p-d, viewBox 0 0 1920 656.
 * THE ARITHMETIC, stated at the point of edit (gotcha 7): the corpus block is
 * 1 / 0.04 = 25.00 times the bill block, because dividing a yearly bill by a
 * 4.0% withdrawal rate IS multiplying it by twenty-five. Numerator and
 * denominator are one arithmetic; never move one without the other.
 *   bill 56 wide -> corpus 56 * 25 = 1400 wide, x 390..1790 inside 1920. */
const BILL_W = 56, RATE_DIV = 0.04, MULT = 1 / RATE_DIV;
function divisionBlock(id) {
  const corpusW = BILL_W * MULT;
  if (Math.abs(corpusW - 1400) > 1e-9) throw new Error("division-block: 25x is not 1400px");
  if (390 + corpusW > 1920) throw new Error("division-block: corpus leaves the plate");
  return [
    `<svg class="art" id="${id}-art" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`,
    `      <rect class="fl"  id="${id}-bill" x="150" y="260" width="${BILL_W}" height="96"/>`,
    `      <rect class="fl"  id="${id}-div"  x="130" y="376" width="96" height="12"/>`,
    `      <g id="${id}-eq"><rect class="fl" x="290" y="290" width="60" height="12"/>` +
      `<rect class="fl" x="290" y="326" width="60" height="12"/></g>`,
    `      <rect class="flf" id="${id}-corp" x="390" y="260" width="${corpusW}" height="96"` +
      ` style="transform-origin:0% 50%"/>`,
    `    </svg>`,
  ].join("\n");
}

/* s14 · split-bar — p-c, viewBox 0 0 934 1200.
 * THE ARITHMETIC, stated at the point of edit (gotcha 7): the filled part is
 * EXACTLY 0.500 of the track, because Bengen tested 50% stocks against 50%
 * bonds. It is one number and it is the scene's whole content, so it is written
 * once, here, and the same constant drives both the drawn rect and the span()
 * endpoint below — a bar that agrees with its own animation by construction.
 * GEOMETRY: the p-c rect is x 1046..1980, i.e. its right 60px are off-canvas by
 * design (the archetype is "cropped by the frame edge"). The track is plate
 * x 40..840 => screen 1086..1886, which is s16's own right edge, so the whole
 * mechanism is on canvas. 120px tall and solid: §8's floor is 9px and ghost
 * tracks are FILLED rects at ~.2, never outlines.
 *
 * GHOST_A: fin-editor/CEO should-fix #4 (en ch2 r2) — and the ROOT CAUSE, which
 * is not the number anybody was arguing about. The ghost carried `opacity=".22"`
 * and `fade("#s14-track")` animates OPACITY 0 -> 1, so GSAP overwrote the
 * attribute on its first frame and the track has been rendering at 1.0 since it
 * was drawn. The ".22" was dead the moment the cue ran. That is the whole
 * defect: `--ink` at full weight against `--target`, which is a dark gold, so
 * the EMPTY half out-shouted the FILLED half on the one frame whose job is to
 * say the two are equal (measured at 41.0s: grey 82.1, amber 60.0, local ground
 * 32.5). The fix is therefore FILL-opacity, which `fade()` does not touch and
 * cannot clobber; the entrance still fades. Compositing is linear in alpha over
 * a fixed backdrop, so the value is a ratio, not a guess: (60.0-32.5) /
 * (82.1-32.5) = .554. Still a SOLID FILLED rect, never an outline, which is
 * what format.json's "~.2" line actually protects — a 27-luma step across
 * 800x120px survives any encode; a 3px stroke at .4 does not.
 * ⚠ CHECKED FOR SIBLINGS: s16's grid ghosts also carry `opacity=".22"`, but the
 * cue there targets their parent `<g id="s16-r10">`, so those are live and
 * correct. s14-track is the only element in the chapter faded on itself.
 * The SPLIT, the tick and `art-forward .52` are untouched. */
const SPLIT = 0.5, GHOST_A = 0.55,
  TRACK_X = 40, TRACK_W = 800, TRACK_Y = 540, TRACK_H = 120;
function splitBar(id) {
  if (SPLIT !== 0.5) throw new Error("split-bar: the tested portfolio is 50-50");
  const mid = TRACK_X + TRACK_W * SPLIT;
  if (TRACK_X + TRACK_W > 874) throw new Error("split-bar: the track leaves the canvas");
  return [
    `<svg class="art" id="${id}-art" viewBox="0 0 934 1200" preserveAspectRatio="xMidYMid meet">`,
    `      <rect class="fl" id="${id}-track" fill-opacity="${GHOST_A}" x="${TRACK_X}" y="${TRACK_Y}"` +
      ` width="${TRACK_W}" height="${TRACK_H}"/>`,
    `      <rect class="flt" id="${id}-fill" x="${TRACK_X}" y="${TRACK_Y}"` +
      ` width="${TRACK_W}" height="${TRACK_H}" style="transform-origin:0% 50%"/>`,
    `      <rect class="fl" id="${id}-mid" x="${mid - 5}" y="${TRACK_Y - 34}"` +
      ` width="10" height="${TRACK_H + 68}"/>`,
    `    </svg>`,
  ].join("\n");
}

/* s17 · date-axis — p-a, viewBox 0 0 1920 1080 (the plate IS the frame).
 * THE TRUTH BAR: both dates are the chapter's own published citations, already
 * on screen at s13 and s15 — October 1994 (Bengen, JFP vol. 7 no. 4) and
 * February 1998 (Cooley/Hubbard/Walz, AAII Journal). Nothing is invented and no
 * source document is depicted; two real publication months are ringed.
 * GEOMETRY: the motif lives BELOW the centred stack (which occupies roughly
 * y 420-660 at this focal), inside `.band`'s darker half. The line stops 120px
 * past the second date and nothing follows it — that emptiness is the second
 * sentence, "Not a promise". Ellipse perimeters are Ramanujan-approximated and
 * rounded UP for draw(): over-declaring the dash length is safe, under-declaring
 * leaves a gap in the ring. */
const RING = [
  { cx: 640,  rx: 238, len: 1040, rot: -1.5, txt: "OCTOBER 1994" },
  { cx: 1280, rx: 250, len: 1090, rot: 1.5,  txt: "FEBRUARY 1998" },
];
function dateAxis(id) {
  const L = [`<svg class="art" id="${id}-art" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid meet">`];
  L.push(`      <g id="${id}-axis">`);
  L.push(`        <rect class="fl" x="400" y="902" width="1000" height="9"/>`);
  RING.forEach((r) => {
    L.push(`        <rect class="flt" x="${r.cx - 5}" y="880" width="10" height="52"/>`);
    L.push(`        <text class="flt" x="${r.cx}" y="838" font-size="46" text-anchor="middle">${r.txt}</text>`);
  });
  L.push(`      </g>`);
  RING.forEach((r, i) => L.push(
    `      <ellipse class="stt" id="${id}-r${i + 1}" cx="${r.cx}" cy="822" rx="${r.rx}" ry="58"` +
    ` transform="rotate(${r.rot} ${r.cx} 822)" style="stroke-width:12"/>`));
  L.push(`    </svg>`);
  return L.join("\n");
}

/* §9a · the measure bar. 920px = $1,963,375 (rung five, the whole household at
 * 4.0%) => 1px = $2,134.10. This is the ONE scale for all six ladder frames in
 * the cut and it may not be re-used at another. */
const LADDER_TOP = 1963375;
sc.filter((s) => s.meas).forEach((s) => {
  const corpus = Number(s.num.replace(/[^0-9]/g, ""));
  const exact = corpus / LADDER_TOP;
  if (Math.abs(exact - s.meas) > 0.0005)
    throw new Error(`${s.id} measure ${s.meas} != ${corpus}/${LADDER_TOP} = ${exact.toFixed(4)}`);
});

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const PLATE = { a: "p-a", b: "p-b", c: "p-c", d: "p-d" };
const ART = { grid: survivalGrid, division: divisionBlock, split: splitBar, dates: dateAxis,
              tank: (id) => tank(id, { stream: false }) };

function scene(s) {
  const cls = ["scene", "clip", "arch-" + s.arch, "has-photo"];
  if (s.art === "off") cls.push("art-off"); else cls.push("art-forward");
  if (s.ctr) cls.push("centred");
  if (s.lift) cls.push("art-lift");
  const style = s.role ? ` style="--tint:rgba(${s.role},${s.role === FUND ? ".10" : ".12"})"` : "";
  const glow = s.role ? ` style="--gl:rgba(${s.role},.16)"` : "";
  const L = [];
  L.push(`\n<!-- ${s.line} · ${s.arch.toUpperCase()} · ${s.f1} · art ${s.art}` +
    `${s.ctr ? " · centred" : ""}${s.role ? (s.role === FUND ? " · --fund" : " · --target") : ""}\n     ${s.note} -->`);
  L.push(`<section class="${cls.join(" ")}" id="${s.id}" data-track-index="${s.track}"` +
    ` data-start="${s.start}" data-duration="${s.dd}" data-framings="${s.framings.join(",")}"${style}>`);
  // `bgpos` is the KEN OFFSET knob: `.bg` is `background-size: cover` inside an
  // inset:-8% box, so a source whose aspect is narrower than 16:9 carries real
  // vertical slack that `background-position: center` throws away symmetrically.
  // Spending it moves the PHOTOGRAPH out from under the type instead of moving
  // the type, which is why it is legal where `.band` is not (see s20's note).
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(assets-ch2/final/${s.img})` +
    `${s.bgpos ? `;background-position:${s.bgpos}` : ""}"></div>`);
  if (s.img2)
    // The SECOND framing. A real second FILE (a tighter crop of the same source
    // frame), never the same file pointed at twice — cross-fading a file onto
    // itself flickers (creator rule, firaun 2026-07-23). It sits after #sN-bg in
    // DOM order at the same z, so fading it in reveals it over the first.
    L.push(`  <div class="bg" id="${s.id}-bg2" style="opacity:0;background-image:url(assets-ch2/final/${s.img2})"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  if (s.band)
    // rule 9: never darken the PHOTOGRAPH to make drawn art readable — darken
    // BEHIND it. z-index 0 so it stays UNDER the plate it exists to serve; the
    // stylesheet's default z 1 would paint it straight over the mechanism.
    L.push(`  <div class="band" id="${s.id}-band" style="z-index:0"></div>`);
  if (s.art !== "off") {
    L.push(`  <div class="plate ${PLATE[s.arch]}" id="${s.id}-plate">`);
    L.push(`    <div class="plate-in" id="${s.id}-pin"><div class="hatch"></div>`);
    L.push(`      ${ART[s.art](s.id)}`);
    L.push(`    </div>`);
    L.push(`  </div>`);
  }
  L.push(`  <div class="scrim"></div>`);
  if (s.brule)
    L.push(`  <div class="brule" id="${s.id}-br" style="top:${s.brule}px"></div>`);
  if (s.vrule)
    L.push(`  <div class="vrule" id="${s.id}-vr" style="top:${s.vrule[0]}px;height:${s.vrule[1]}px"></div>`);
  L.push(`  <div class="stack" id="${s.id}-stack">`);
  L.push(`    <p class="kicker" id="${s.id}-kick">${esc(s.kick)}</p>`);
  const rc = s.role === FUND ? " fundc" : s.role === TARGET ? " targetc" : "";
  if (s.rate)
    L.push(`    <p class="sub${rc}" id="${s.id}-rate">${esc(s.rate)}</p>`);
  if (s.num)
    L.push(`    <p class="huge${rc}" id="${s.id}-num">${esc(s.num)}</p>`);
  if (s.stmt) {
    const body = (s.rateSpan
      ? esc(s.stmt).replace(esc(s.rateSpan),
          `<span class="v-rate${rc}" id="${s.id}-rate">${esc(s.rateSpan)}</span>`)
      : esc(s.stmt)).replace(/\n/g, "<br>");
    L.push(`    <p class="huge${rc}" id="${s.id}-stmt" style="font-size:${s.size}px">${body}</p>`);
  }
  if (s.sub)
    L.push(`    <p class="sub" id="${s.id}-sub">${esc(s.sub)}</p>`);
  if (s.foot)
    L.push(`    <p class="foot" id="${s.id}-foot">${esc(s.foot)}</p>`);
  L.push(`  </div>`);
  if (s.meas) {
    // §9a. OUTSIDE .stack on purpose: .measure/.measure-lab position themselves
    // at left calc(50% - 460px), which is why `.centred` does not hide them and
    // why the device survives on a photo-led cut.
    L.push(`  <p class="measure-lab under" id="${s.id}-mlab">${esc(s.mlab)}</p>`);
    L.push(`  <div class="measure under" id="${s.id}-meas"><div class="measure-fill fund" id="${s.id}-mf"></div></div>`);
  }
  L.push(`  <div class="grain"></div>`);
  L.push(`</section>`);
  return L.join("\n");
}

const audio = sc.map((s) =>
  `<audio id="vo-${CH}-${s.i + 1}" class="clip" data-track-index="10" ` +
  `data-start="${s.astart}" data-duration="${s.adur}" src="assets/voice/${s.line}.mp3"></audio>`
).join("\n");

const map = (f) => "{ " + sc.map((s) => `${s.id}: ${f(s)}`).join(", ") + " }";

/* the photograph carries the motion — one move per scene, never a plate push
 * competing with a ken. `i`/`o` are ken's fixed 1.0<->1.16 endpoints; the two
 * framings of 2.2 need plateKen's EXPLICIT endpoints so the second picks up
 * exactly where the first ended and the swap reads as a push, not a flash. */
const kenJs = sc.map((s) => {
  if (s.kenFrom == null) return `ken("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.ken === "i"});`;
  return [
    `plateKen("#${s.id}-bg", S.${s.id}, ${s.swap.toFixed(3)}, ${s.kenFrom.toFixed(2)}, ${s.kenTo.toFixed(2)});`,
    `plateKen("#${s.id}-bg2", S.${s.id} + ${s.swap.toFixed(3)}, ${(s.dur - s.swap).toFixed(3)}, ` +
      `${s.ken2From.toFixed(2)}, ${s.ken2To.toFixed(2)});`,
    `fade("#${s.id}-bg2", S.${s.id} + ${s.swap.toFixed(3)}, 0.40);`,
  ].join("\n");
}).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 2 · the rate, and the first rung</title>

<!-- ===========================================================================
     CHAPTER 2 — the rate is staged as a finding with a date, then the first
     corpus is worked. Fifteen cuts, ${ROOT}s, s9-s23.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the fifteen <audio> rows
     and the root duration are computed from that one file and asserted against
     the shipped cut's GAPS — a re-time is exactly what produces a correct total
     with every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is ${OFF}s (timing.json's own scene_start for line 2.1), so
     this concatenates frame-exact. The LAST scene carries its bare
     scene_duration: a chapter has no successor to cross-dissolve into, and
     tools/cut_assemble.py adds the +0.45 overlap back at fold-in.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Eleven of fifteen scenes are art-off + centred. Rule 8 retires the drawn
     layer wherever the photograph already carries the beat, and .centred then
     re-centres the stack so the archetype's empty side is not a hole. The four
     that keep a drawn layer each assert something no photograph can: 2.6's
     50-50 split bar, 2.8's 95-of-100 survival grid, 2.9's two ringed
     publication dates and 2.10's 25x division block. 2.6 and 2.9 are
     fin-editor's r1 blockers — the ratio and the date were being asserted by
     type over a photograph that argued with neither.

     2.2 is the cut's only max_scene_seconds breach (10.596s) and it is resolved
     INSIDE the scene: two declared framings of one source frame — 6.324 + 4.272
     — under a single continuous push, 1.00 -> 1.06 -> 1.16.

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

/* ONE-OFF, this composition only (hence .v-): §4's SECOND rate form, an inline
   span inside the focal, on 2.14. It exists because \`pulse\` is a TRANSFORM and
   transforms do not apply to a non-replaced inline box — the span would carry
   the role colour, the assert would find it, and the beat under the spoken rate
   would simply never happen, with every check green. The system has no class
   for this form; blockframe.css owns the colour, this owns the box.
   \`baseline\` keeps the inline-block on the focal's own baseline. */
.v-rate { display: inline-block; vertical-align: baseline; }

/* BOTH LOCAL PATCHES THAT USED TO SIT HERE ARE GONE (2026-08-08). \`.scene.centred
   .stack { padding-left: 0 }\` and \`.arch-b .v-widefocal { max-width: 1500px }\`
   were reported as system gaps by this build and by hi ch2 independently, and
   both were ported into tools/scaffold/assets/chapter-design.css the same day —
   verified byte-identical against assets/chapter-design.css here. Re-emitting
   them would hand chapters 3-6 a redundant declaration plus a comment claiming a
   gap that no longer exists, which is the thing the next reviewer chases.
   The upstream rules are \`.scene.centred .stack { padding-left: 0 }\` and
   \`.scene.centred.arch-b .huge, .foot { max-width: 1500px }\` — the second is
   selector-scoped where the local one keyed off a \`.v-widefocal\` class, so that
   class is gone from the markup too rather than left as an unstyled hook. */
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
<script src="assets/js/motion.js"></script>
<script>
/* S = scene starts · D = each scene's OWN hold (not its dissolve-padded
   data-duration), so the photograph's push finishes exactly as the next scene
   begins to fade up. Both generated from timing.json. */
var S = ${map((s) => s.start)};
var D = ${map((s) => s.dur)};
var IDS = ${JSON.stringify(sc.map((s) => s.id))};

/* Cross-dissolves, one call, before the per-scene cues. No shove in chapter 2:
   the cut's two act changes are s39 -> s40 and s58 -> s59 (§12), both
   downstream. s9's dissolve is against the incoming chapter boundary and is
   correct here — in the assembled cut it dissolves out of s8. */
sceneTransitions(IDS, S);

/* THE PHOTOGRAPH CARRIES THE MOTION — one move per scene. Direction alternates
   from s9's pull-back (ch1 ended on s8 pushing in) and does NOT flip inside
   2.2, whose two framings chain 1.00 -> 1.06 -> 1.16 so they read as one
   uninterrupted push on one image. */
${kenJs}

/* THE TYPE — cue ladder variant A (storyboard §5) on the statement scenes:
   kicker +0.30, statement +1.10, then the sub or the foot at +1.90 and the foot
   at +2.70 when the sub took cue 3. Fixed offsets, constant whatever a clip's
   length; every gap is 0.80s and the photograph is already up at +0.00, so
   first_cue_by_seconds (0.5) is met by the kicker. */
${sc.map((s) => `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 14);`).join("\n")}
${sc.filter((s) => s.stmt && !s.verdict).map((s) => `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 18);`).join("\n")}

/* 2.9 · THE VERDICT SLAM. §2: the five verdict scenes take pop() (back.out(1.7))
   on their stmt instead of rise(). That IS the slam — it needs no .stamp pill
   and no new copy, and it is what makes the "stamp" SFX legal here. */
${sc.filter((s) => s.verdict).map((s) => `pop("#${s.id}-stmt", S.${s.id} + 1.10, 0.6);`).join("\n")}

/* 2.2 · THE PAIR NAMED. The sub is cue 3 on a statement scene (+1.90 fade) and
   it is the ch1 CEO ruling made concrete. Measured on 2.2.mp3 (base.en, word
   timestamps): "tank" runs 1.960-2.140s into the clip, and the clip starts at
   scene +0.25, so the word occupies scene +2.21 to +2.39 — and the sub's 0.5s
   fade completes at +2.40. The word TANK is legible on screen as it is spoken,
   over a photograph that has no tank in it and says so. */
${sc.filter((s) => s.sub).map((s) => `fade("#${s.id}-sub", S.${s.id} + 1.90, 0.5);`).join("\n")}

/* 2.14 · the rate INSIDE the focal — §4's second form, a pulse at +1.90 fixed. */
${sc.filter((s) => s.rateSpan).map((s) => `pulse("#${s.id}-rate", S.${s.id} + 1.90);`).join("\n")}

/* THE FIGURE SCENES — cue ladder variant B: kicker +0.30, then the rate (or,
   where there is no rate, the foot) at +1.10, then the number ANCHORED on its
   own spoken word, then the foot at num + 0.80 if the foot did not take cue 2.
   The rate is on screen BEFORE the corpus lands: the assumption is up first and
   the number arrives into it (§4).

   EVERY ANCHOR BELOW IS MEASURED, not interpolated. §5 gives character-offset
   fractions as a FALLBACK and says fin-build resolves each against
   faster-whisper WORD timings. Run on this cut's own clips (base.en, word
   timestamps), the figure's first spoken word starts at:
     2.8  "95"    3.080s into the clip -> scene +3.33   (§5's fallback said 3.25)
     2.11 "$10"   1.960s                -> scene +2.21   (no fallback published)
     2.12 "$847"  2.020s                -> scene +2.27   (no fallback published)
     2.13 "$254"  2.300s                -> scene +2.55   (§5's fallback said 2.62)
   Clips start at scene +0.25 (MEDIUM lead_in_seconds), which is the +0.25 in
   each figure above. All four clear variant B's +1.90 floor. */
${sc.filter((s) => s.num).map((s) => {
  const o = [];
  o.push(`rise("#${s.id}-${s.rate ? "rate" : "foot"}", S.${s.id} + 1.10, 0.7, 18);`);
  o.push(`pop("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0.6);`);
  o.push(`countUp("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0, ${s.numTo}, "en-US", 1.2, ` +
    `${JSON.stringify(s.numPrefix || "")}, ${JSON.stringify(s.numSuffix || "")});`);
  if (s.meas)
    o.push(`span("#${s.id}-mf", S.${s.id} + ${s.numAt.toFixed(2)}, 1.2, 0, ${s.meas});`);
  if (s.rate)
    o.push(`fade("#${s.id}-foot", S.${s.id} + ${(s.numAt + 0.80).toFixed(2)}, 0.5);`);
  return o.join("\n");
}).join("\n")}

/* The foot on a STATEMENT scene is cue 3 (+1.90), not cue 4 — variant A puts
   the foot at +2.70 only when the rate or the sub already took +1.90. */
${sc.filter((s) => s.foot && s.stmt).map((s) => `fade("#${s.id}-foot", S.${s.id} + 1.90, 0.5);`).join("\n")}

/* 2.8 · THE SURVIVAL GRID assembles by +2.49, well inside chapter_design's
   "about +3.3", so the contact sheet's +2.6 sample shows a finished mechanism
   and the number then lands on it at +3.33. Ten row groups on a 0.11 cascade. */
popEach("#s16-art .gr", S.s16 + 1.10, 0.11, 0.40);

/* 2.10 · THE DIVISION. No pop() anywhere in this scene on purpose: the sound
   generator reads pop/popEach as a chip cascade, and this beat is a "reveal"
   bound to the band (§7). The band comes up first, then the bill, the divisor
   rule, the equals, and the corpus block wipes open from its LEFT edge —
   transform-origin 0% 50%, so the 25x resolves rightwards instead of growing
   out of its own middle. Assembled at +3.30, inside chapter_design's "about
   +3.3", so the contact sheet's +2.6 sample still shows a mechanism mid-build
   rather than a blank plate.

   ⚠ THE BAND MOVED +0.60 -> +1.10 (fin-editor should-fix #6, en ch2 r1). The
   band fade IS this scene's derived content cue (\`reveal\`), so at +0.60 it sat
   0.600s behind the scene's own joint \`transition\` — under
   \`format.json layout.cue_min_gap_seconds\` 0.8, and at the chapter's biggest
   semantic step (amber finding -> green method), where two sounds inside 0.6s
   blur the arrival that three simultaneous changes are carrying. +1.10 is the
   ladder position every other reveal in this chapter uses. The four mechanism
   cues below shifted with it so the band still precedes what it exists to
   darken behind; none of them emits a sound (one content cue per scene). */
fade("#s18-band", S.s18 + 1.10, 0.50);
fade("#s18-bill", S.s18 + 1.60, 0.40);
fade("#s18-div",  S.s18 + 1.95, 0.35);
fade("#s18-eq",   S.s18 + 2.25, 0.35);
fill("#s18-corp", S.s18 + 2.50, 0.80);

/* 2.6 · THE SPLIT (fin-editor blocker #2). The track is the portfolio; the fill
   is the half that is stocks, and it stops at EXACTLY ${SPLIT.toFixed(3)} — the
   endpoint is the same constant the rect is drawn from, so the drawing and the
   animation cannot disagree. \`span\`, not \`fill\`: fill() always runs to scaleX 1
   and a half-filled bar needs a declared endpoint. The midpoint marker lands
   last, on the boundary the fill just stopped at. Assembled at +2.95.
   2.6 is on the storyboard's DRY list, so none of this emits a sound — the
   scene keeps its joint transition and nothing else, which is right for the
   evidence run. */
/* 2.2 · THE TANK IS FILLED (owed.en_ch2_s10_tank_layer). The band lifts first
   so the mechanism has darkened ground to read against (rule 9 — never the
   photograph), then the VESSEL arrives with the base water in it, and then the
   upper slice of water ARRIVES: the tank filling. Three cues, in the order the
   sentence is spoken.

   ANCHORED ON THIS SCENE'S OWN MEASURED WORD, not on a template offset: the
   sub's note above records "tank" measured at 1.960-2.140s into 2.2.mp3, i.e.
   scene +2.21 to +2.39. The vessel's 0.55s fade at +1.65 therefore COMPLETES at
   +2.20 — the drawn tank is finished on screen at the instant the word arrives,
   and the sub naming it lands 0.20s later. "slowly, over years" follows the
   word, so the level's own 0.70s rise runs +2.60 to +3.30, inside its clause.

   ⚠ THE FILL IS A STATE CHANGE AND NOT A DISTANCE. #s10-lvlx is a second rect
   that ARRIVES; nothing slides, and nothing marks where the level was. That is
   the exact mirror of 4.7, where this same rect EXITS — same markup, opposite
   cue — and it is what keeps a decorative level from reading as a measured
   quantity (\`no_return_promise\`). The vessel selector excludes it by id, so the
   slice fades exactly once instead of arriving with the walls and then blinking
   back to zero at its own fromTo.

   Assembled at +3.30, and this scene's contact-sheet cell settles late anyway
   because the svg carries the \`v-\` class chapter_sheet.py keys off. 2.2 keeps
   its declared joint transition and emits no new sound: the band is the only
   thing here a cue rung could bind to and this scene already has its cue. */
fade("#s10-band", S.s10 + 1.10, 0.50);
fade("#s10-art rect:not(#s10-lvlx)", S.s10 + 1.65, 0.55);
fade("#s10-lvlx", S.s10 + 2.60, 0.70);

fade("#s14-track", S.s14 + 1.60, 0.45);
span("#s14-fill", S.s14 + 2.10, 0.90, 0, ${SPLIT});
fade("#s14-mid",  S.s14 + 2.55, 0.40);

/* 2.9 · THE DATE, RINGED (fin-editor blocker #1). The band lifts first, then
   the time line with both dates on it, then each ring is DRAWN around its own
   date — the circling is the motion, which is the half a photograph of a
   calendar could never have. Both rings are struck by +3.20. The scene's one
   sound is still the \`stamp\` on the verdict pop at +1.10 (a scene takes one
   content cue and \`stamp\` outranks every rung below it), so four new calls add
   exactly zero cues and the s17 ladder is unchanged. */
fade("#s17-band", S.s17 + 1.60, 0.50);
fade("#s17-axis", S.s17 + 1.90, 0.45);
${RING.map((r, i) => `draw("#s17-r${i + 1}", S.s17 + ${(2.10 + i * 0.45).toFixed(2)}, 0.65, ${r.len});`).join("\n")}

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE RATE ASSERTS — run.json.constraints, mechanised. Carried forward from
   chapter 1, where they were vacuously true because the cold open renders no
   figure. CHAPTER 2 IS WHERE THEY GO LIVE: it is the first chapter with a
   corpus, a numerator and a derived month on screen.

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number. A number
       without its assumption visible is a fabricated promise."

   (2) derived_income_carries_assumption (EXTENDED 2026-08-07 during hi ch2
       review): a DERIVED INCOME figure — "what \$X buys", i.e. the corpus's own
       OUTPUT — is the promise the video actually makes, so it carries the rate in
       frame or an explicit ILLUSTRATIVE marker, exactly like a corpus.
       A BLS bill divided by twelve is NOT derived income — it is arithmetic on a
       published statistic — so the marker branch accepts a stated provenance
       (BLS / CONSUMER EXPENDITURE) as well as ILLUSTRATIVE.

   (3) NEW HERE, and it is the branch this chapter needed. (1) is deliberately
       narrow: it fires only on the eight CORPUS tokens, so a published
       numerator could render completely bare and pass. \$10,169 and \$847 are
       exactly that shape. §4 says the corpus branch must NOT fire on them —
       correctly, a numerator is not an answer and demanding a withdrawal rate
       beside it would be dishonest — but "must not demand a rate" is not the
       same as "may be bare". A BILL therefore has to carry, in frame, either a
       rate, the published provenance, or its own derivation. Today all three of
       this chapter's bills do; the point of the assert is that a density pass
       that drops a foot line cannot silently make one of them a bare number.
       Extend BILL, not CORPUS, as chapters 3-6 land their own numerators.

   Throwing is the point: "hyperframes check"'s runtime pass fails on an uncaught
   page error, and a silent console.warn is what let this ship twice.

   ⚠ THIS ASSERT IS FRAME-ONLY BY CONSTRUCTION. It reads rendered text, so it
   cannot see a VO line that SPEAKS a figure over a bare frame
   (run.json.owed.derived_income_assert_is_frame_only). That half is
   tools/check_vo_frame.py, run against this file at build:
     python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 2
   It reads RATE and MARKER back out of THIS block, so the two can never drift.
   =========================================================================== */
(function () {
  var CORPUS  = /\\$(?:254,225|332,950|656,650|1,500,000|1,929,260|1,963,375|5,555,556|7,271,759)/;
  var RATE    = /4\\.0%|3\\.11%|1\\.08%/;
  var DERIVED = /\\$[\\d,]+\\s*(?:a month|A MONTH|per month|PER MONTH)/;
  var MARKER  = /ILLUSTRATIVE|BLS|CONSUMER EXPENDITURE/;
  var BILL    = /\\$(?:10,169|847|13,318|26,266|2,189|1,110|6,545|78,535)/;
  var DERIVATION = /divided by/i;
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
    var b = txt.match(BILL);
    if (b && !rated && !MARKER.test(txt) && !DERIVATION.test(txt))
      bad.push(s.id + " renders the published figure " + b[0] +
               " with no rate, no provenance and no derivation in frame");
  });
  if (bad.length) throw new Error("RATE ASSERT FAILED — " + bad.join(" · "));
})();
</script>
</body>
</html>
`;

fs.writeFileSync("index.html", html);

/* ------------------------------------------------------------- the sound pass
 * DERIVED, never hand-typed (storyboard §2): tools/audio/cues.py reads the file
 * this script just wrote and emits one cue per REAL motion call, at that call's
 * own time, bound through tools/audio/kit.json's helper column. Running it from
 * here rather than as a second command is what guarantees the cue list and the
 * markup came from the same derivation of timing.json — ch1 reproduced the
 * generator's rules by hand and had to diff them afterwards.
 *
 * The special cases cues.py cannot derive (holds, the diegetic buzz, counted
 * cascades, the declared DRY list) live in the CUT's own
 * studio/videos/passive-income-number-en/assets/cues-tables.json, written from
 * storyboard §2. ch2's dry scenes are s12, s14, s16, s19 and s20 — the papers'
 * evidence run and every BLS numerator; a `hero` on 95% makes a survival
 * statistic sound like a prize.
 *
 * ONE correction the tool cannot make: cues.py hardcodes `music: bed-resolve`,
 * and §2/D12 chooses **bed-tension** for this cut — its argument is a COST, not
 * a habit. The bed is a per-video fact. */
/* cues.py validates the SHIPPED assets/audio.json as well as the list it just
 * derived, and exits 1 on a `cue_min_gap_seconds` breach in either. Left in
 * place, last build's file is what gets validated — so the run that FIXES a gap
 * dies on the artefact it is fixing, before it can write the replacement. Drop
 * it first: the next two lines regenerate it unconditionally. */
fs.rmSync("assets/audio.json", { force: true });
const derived = JSON.parse(execFileSync("python3",
  ["../../../tools/audio/cues.py", "."], { encoding: "utf8" }));
derived.music = "bed-tension";
derived._bed = "bed-tension (storyboard §2 / §13 D12) — cues.py defaults to "
  + "bed-resolve; this cut's argument is a cost, not a habit. Overridden by "
  + "build.mjs, not hand-edited into the generated file.";
fs.writeFileSync("assets/audio.json", JSON.stringify(derived, null, 1) + "\n");

const nCues = derived.sfx.filter((c) => c.at != null).length;
console.log(`assets/audio.json: ${nCues} cues (derived by tools/audio/cues.py)`);
console.log(`index.html: ${sc.length} scenes, root ${ROOT}s, offset ${OFF}s`);
sc.forEach((s) => console.log(
  `  ${s.id} ${s.line}  start ${String(s.start).padStart(7)}  dur ${String(s.dur).padStart(6)}` +
  `  d-dur ${String(s.dd).padStart(6)}  track ${s.track}  ${s.arch.toUpperCase()}` +
  `${s.ctr ? " centred" : ""} ${s.art}${s.size ? "  focal " + s.size : ""}` +
  `${s.numAt ? "  num +" + s.numAt.toFixed(2) : ""}`));
