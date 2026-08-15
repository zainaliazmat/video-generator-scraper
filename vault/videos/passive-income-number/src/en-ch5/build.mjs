/* build.mjs — emits index.html + assets/audio.json for CHAPTER 5 of
 * passive-income-number, -en (@moneymavens101, $).
 *
 *   node build.mjs        (or: npm run build)
 *
 * WHY A GENERATOR AND NOT HAND-TYPED HTML. Every data-start, data-duration,
 * data-framings, the JS `S`/`D` maps, every <audio> row and the root duration
 * are FOUR homes for the same number, and the failure this project keeps
 * hitting is durations that sum to exactly the right total while every internal
 * cut has drifted. All four are computed here from ONE source —
 * ../passive-income-number-en/assets/voice/timing.json — and the asserts under
 * the timing block compare GAPS, not totals, so a silent re-time throws instead
 * of shipping.
 *
 * Chapter 5 is lines 5.1-5.16 = scenes s53-s68. The rebase constant is
 * timing.json's own scene_start for 5.1 (335.817s), subtracted from every start,
 * exactly as ch1 does with 0.000, ch2 with 46.420, ch3 with 151.938 and ch4 with
 * 248.539.
 *
 * SPEC, not invention. arch / ground / art / ctr / focal / ken / sfx are
 * storyboard-en.md §7 verbatim; the kicker / stmt / num / chip / foot strings are
 * script-en.md's own `[arch …]` cue blocks (one home per fact — the storyboard
 * deliberately does not restate copy). Structure ported from the ch4 generator
 * with hi-ch5's later guards folded in (the settled-figure floor, the motion-cue
 * gap sweep, the JPEG SOF swap geometry, and T read from format.json rather than
 * retyped — see `owed` item 2 of logs/fin-build-hi-ch5-1.md).
 *
 * WHAT THIS CHAPTER CARRIES THAT NO EARLIER en CHAPTER DID:
 *
 *  1. THE CUT'S ONE `.mega` — s55 (5.3), `ABOUT 1%` at 300px. §9c: in a video
 *     arguing that the RATE is the whole answer, the rate is the one enormous
 *     number on screen and the corpus it produces follows it four scenes later.
 *     Measured, not estimated: fontTools on the shipped NotoSansFinance-var at
 *     wght 900 gives 1601.7px raw and `.arch-b .mega`'s letter-spacing:-14px
 *     takes it to 1489.7px against the centred stack's 1500px cap — 10.3px of
 *     margin, so the element is pinned `white-space: nowrap` (see the local
 *     `.v-nowrap`). §3's own estimate was 1392px; the real figure is 100px wider
 *     and would wrap onto two 300px lines on a hair.
 *
 *  2. TWO DECLARED FRAMING SWAPS, s56 and s67, whose derived crops did not exist
 *     when this build started — ffmpeg is not on fin-assets' allowlist and that
 *     stage routed them here (logs/fin-assets-en-ch5-1.md, Owed 1). Both are
 *     1600x900 crops of their own promoted parent, natively 16:9 so `cover`
 *     discards nothing, and never a self-dissolve back to the same file (creator
 *     rule, firaun 2026-07-23). Geometry is asserted against the JPEG SOF
 *     markers at every build.
 *
 *  3. BOTH SWAP POINTS MEASURED AGAINST THE VOICE, NOT THE TEMPLATE
 *     (`chapters.hi.5.s57_swap_point_recut_2026-08-10`). One is RE-CUT and one
 *     is KEPT, by the same rule applied to two different measurements — see the
 *     s56 and s67 notes. §6c's `f` values are character fractions and §5 calls
 *     them a FALLBACK to be resolved against faster-whisper word timings.
 *
 *  4. THE CHAPTER'S SHOVE IS INTERNAL. §12 gives the cut two act changes and one
 *     of them, s58 -> s59, is inside this project — unlike every earlier chapter,
 *     whose shoves sat on a chapter boundary. `sceneTransitions(IDS, S,
 *     { acts: ["s59"] })` is therefore live here, not a declaration for the
 *     assembler.
 *
 *  5. THE INVARIANT (`separation_not_rank_2026-08-09` §1 as amended by
 *     `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`) is discharged on
 *     the CONTENT of the beat that sits at the measured floor. Not "satisfied by
 *     construction" — that phrase quotes the retired converse and is not an
 *     available answer. See the INVARIANT block and the s54 note.
 */
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const CH = 5;
const LINES = ["5.1", "5.2", "5.3", "5.4", "5.5", "5.6", "5.7", "5.8",
               "5.9", "5.10", "5.11", "5.12", "5.13", "5.14", "5.15", "5.16"];
const FIRST = 53;                                   // scene s53 == line 5.1
const TIMING = JSON.parse(
  fs.readFileSync("../passive-income-number-en/assets/voice/timing.json", "utf8"));
/* READ, never retyped. hi ch5 proved by planting a wrong value that a generator
 * whose `dd` is BUILT from T cannot detect a wrong T — both sides of its own
 * overlap assert move together — so the fix is at the correct-default rung:
 * a wrong value is unrepresentable rather than merely detectable. */
const T = JSON.parse(fs.readFileSync("../../../tools/format.json", "utf8"))
            .scene.transition_seconds;
const IMG = "assets-ch5/final";

const TARGET = "245,158,11";   // --target #f59e0b, alpha .12  (§1a)
const FUND   = "34,197,94";    // --fund   #22c55e, alpha .10  (§1a — green reads hotter)
const WARN   = "239,68,68";    // --warn   #ef4444, alpha .12  (§1a)

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`: A plate · B figure · C ledger · D band. The chapter's
 *        sequence is A A B C D D B B B B B D A C B B, §7's own rhythm block,
 *        including the declared `B B B B B` hold at s59-s63 — the answer, the
 *        pair, the gap, the middle route, the middle price: five figures and ONE
 *        argument, with the mechanism changing underneath every time.
 * f1     §7 `ground` (§11's temperature arc). THIS CHAPTER CARRIES BOTH EXTREMES
 *        AND THE CUT'S ONE DECLARED CONTRADICTION: s57/s58/s59 are `--warn`
 *        scenes running deep COOL grounds (#131f2c -> #0e1c2e -> #0c1a2c, the
 *        coldest in the video), which §11 declares in as many words "so a later
 *        pass cannot fix it" — cold is neutral, it asserts nothing, and this is
 *        the drop. Then the chapter snaps back to amber at s60 and hits #3b1219
 *        at s61, the hottest frame in the video.
 * art    §7 `art` — `off` on FOURTEEN of sixteen. §8 gives chapter 5 zero drawn
 *        layers and refuses four candidates by name; TWO scenes now carry one
 *        anyway, and both are rulings dated after the storyboard rather than a
 *        build's taste (attempt 3): s57 the ch4 tank layer, s61 the five marks.
 *        See the density assert for the citations and for what stays refused.
 * ctr    §7 `ctr` — Y on fourteen. The two drawn scenes come OFF centre, and that
 *        is forced rather than chosen: `.scene.centred .plate` is display:none, so
 *        a centred scene cannot hold a drawn layer at all — the trade ch4's 4.7
 *        made. On s57 (arch D, stack top-left either way) no type moves at all; on
 *        s61 the focal moves to archetype B's left column and is hard-broken at a
 *        measured width, with no change to the type ladder. §7 gives s64 `ctr N` and
 *        attempt 1 obeyed it; fin-review measured the result and it is finding
 *        #2 (and, as a retention cost, #4). BOX ITEM 7 OVERRIDES THE COLUMN, and
 *        the reason is that §7's `N` was written against a photograph that does
 *        not ship: the row assumes "three parallel painted lanes converging" —
 *        something for the type to sit BESIDE — and s64.jpg is a top-down of 5–6
 *        lanes carrying a left-turn arrow, two straights and two merges. With
 *        `art: off` the plate side is empty by construction, so the split held
 *        nothing on either count, on the chapter's THESIS line. Nothing on s64
 *        lives in the plate (kicker + one `.row` of three chips, both inside
 *        `.stack`), so `.scene.centred .plate{display:none}` hides nothing that
 *        exists — the ch4 4.7 trap does not apply here.
 * ken    §5: the direction flips at every boundary except a hold, and §6b gives
 *        this chapter no hold. ch4 closed on s52 `i`, so s53 opens `o` —
 *        asserted at the chapter joint as well as inside it.
 * role   §1: amber = a published figure or rate under examination (5.1, 5.3,
 *        5.4, 5.8, 5.10, 5.11, 5.12, 5.14); red = what an assumption costs (5.5,
 *        5.6, 5.7, 5.9, 5.16); green = a division that closed at a sourced rate
 *        (5.15). Two frames carry no role at all.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · 49-89 -> 76.
 *        Computed below, never written here.
 *
 * EVERY LINE BREAK IN A `stmt` OR A `foot` IS TYPOGRAPHIC AND WAS MEASURED, not
 * guessed — fontTools against the shipped NotoSansFinance-var.woff2 instanced at
 * wght 900, at each string's ladder size, with the class's own letter-spacing
 * applied (.huge -2px, .foot +1px, .mega -14px), against the 1500px
 * `.scene.centred .stack` cap (which `.scene.centred.arch-b .huge/.foot` raises
 * to the same 1500):
 *   s53  1057 /  800 @88   (unbroken 1878)      s54   669 /  906 @88 (1598)
 *   s57  1247 /  441 @88   (unbroken 1711)      s58  1201 @112, one line
 *   s60   848 /  853 @88   (unbroken 1722)      s65  1008 @112, one line
 *   s61  1002 @112 · s55 mega 1489.7 @300 · every $ figure 593 @112
 *   feet @26: s55  994 /  667 (unbroken 1683)   s56 1344, one line
 *             s59  767 · s63  767 · s67  976 · s68  767, one line each
 *             s61  714 /  770 (unbroken 1494 — 5.9px of margin, so it BREAKS)
 *             s62 1029 / 1012 / 1367 (three lines)
 *             s66 1228 / 1229
 *   subs @40: s59 568 · s63 352 · s67 615 · s68 568
 * Every break below exists because the string does not fit, not because a line
 * looked long. s61's foot is the interesting one: at 1494.1px it technically fits
 * the 1500px box, and ch4 already rejected an 11px margin as "a frame that
 * re-wraps on a hair" — 5.9px is half that, so it is hard-broken.
 */
const SCENES = [
  { line: "5.1", arch: "a", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "THE TITLE QUESTION",
    stmt: "Spend only what it pays.\nNever sell a share.",
    img: "s53.jpg",
    note: "THE TITLE QUESTION — the chapter opens by naming the thing the title promised, and it is the one beat in the cut where the packaging phrase and the argument are the same sentence. AMBER because §1 makes it a condition under EXAMINATION, not a verdict: 5.1 states the never-sell condition as the viewer's own question and 5.7 is where it gets priced. Archetype A, centred, art off — a hand resting on a closed folder says a question being put, and there is nothing a drawing could add that the photograph does not already carry (rule 8). The focal is fixed at +1.10 per variant A; MEASURED for the record and NOT used, because §5 makes variant A's ladder fixed by design: the words «spend» and «never sell a share» are spoken at scene +3.09 and +5.49, so the type leads the voice by design and holds while the sentence catches up. §10's hand rule: hand only, no face, no wrist mark." },

  { line: "5.2", arch: "a", f1: "#1c2027", art: "off", ctr: true, ken: "i",
    kick: "DIVIDENDS ONLY",
    stmt: "A real strategy.\nWith a real price tag.",
    img: "s54.jpg",
    note: "DIVIDENDS ONLY — NO role and no colour, deliberately: the line's content is that this route is neither wrong nor recommended, and any of the three role colours would claim one of those. ⚠ THIS IS THE CHAPTER'S MEASURED LUMINANCE FLOOR AND IT IS RULED, MEASURED AND DELIBERATELY NOT FIXED — see the INVARIANT block below for the full discharge. Composed median 13.03 on this build's own chain against s62's 20.69, i.e. alone at the bottom by 7.66 points where the next largest adjacent gap in the chapter is 1.57, so the §3 OUTLIER LIMB genuinely fires. It stays. The lever does not exist: the source is 1880x1253 against .bg's 1.778 box, so cover is WIDTH-limited and the only knob is the 195 source rows of vertical slack — swept at five positions it moves the composed median by 0.05 POINTS, from 12.99 to 13.04, because the frame is uniform dark navy card above and below the tag. And the only other lever, a re-fetch, relocates the floor onto s62 (5.10, `ABOUT 3%`, the middle route, a figure frame carrying a three-line published citation), which `outlier_limb_is_subordinate_to_the_invariant_2026-08-10` FORBIDS: a fix that moves a MORE substantive beat to the bottom is not optional, it is forbidden. Sound-off it is exactly the line: a blank paper price tag on a string = a real price tag. p10 11.85 / p90 40.67 is a spread of 27.64, the WIDEST in the chapter — dark and full, not dark and empty, which is the failure mode the floor rule actually predicts." },

  { line: "5.3", arch: "b", f1: "#2e2411", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "TODAY",
    mega: true, num: "ABOUT 1%", numAt: 2.77, popDur: 0.50,
    foot: "S&P 500 dividend yield, 5 Aug 2026 — multpl 1.04%, GuruFocus 1.082%\ntwo reads, so the VO says \"about one percent\"",
    footAt: 1.10,
    img: "s55.jpg",
    note: "TODAY — ⚠ THE CUT'S ONE AND ONLY `.mega`, 300px, and §9c is explicit that this is what makes PEAK 2 land four scenes later: in a video arguing that the rate is the whole answer, the RATE is the one enormous number on screen and the corpus it produces follows it. `one_focal_per_scene`: never .huge and .mega together, asserted below, and the assert also throws if any OTHER scene in this chapter acquires one. WIDTH MEASURED, NOT ESTIMATED: 1601.7px raw at 300px, 1489.7px once `.arch-b .mega`'s letter-spacing:-14px is applied, against the centred stack's 1500px — 10.3px of margin. §3's own estimate was 1392px and is 100px optimistic. 10px is inside the noise of a font rasteriser, and `ABOUT 1%` contains a space, so it CAN break into two 300px lines and blow the frame; it is therefore pinned with the local `.v-nowrap`. That is a one-off box property, not a type token — nothing about the ladder changes. §4: this frame carries a rate AS ITS FOCAL and therefore takes NO separate #s55-rate (printing a rate under itself reads as a defect), which is asserted. §5 EXCEPTION 1 applies — the foot cannot follow an anchored figure on a 4.562s scene, so the order is kick +0.30, foot +1.10, num anchored. ANCHOR MEASURED: faster-whisper puts «about» at 2.520s into 5.3.mp3 => scene +2.77, where §5's character fraction said +3.07 (0.30s late). The pop is 0.50s rather than 0.60 and that is forced by the SETTLED-FIGURE floor, not preferred: at 0.60 the figure is settled for 1.192s before the dissolve starts, 0.008s under the 1.20s floor hi ch5 mechanised from fin-editor's hi-ch2 s18 finding; at 0.50 it is 1.292s. The anchor did not move — a spoken anchor is not a knob. ⚠ DECLARED FOR fin-review, from fin-assets: §10 asks this frame for `the calmest background in the chapter` and the NYSE facade's top ~55% is a dense sculptural frieze. It is a real institution correctly located in the US, the gold STOCK EXCHANGE lettering is a real building's own name rather than a fabricated source, and the composed median is 34.01 (rank 11 of 16) so the .mega is not sitting on a dark frame — but the legibility of a 300px figure over carved stone is a layout call settled on the encode." },

  { line: "5.4", arch: "c", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "TWO READS",
    chips: [["1.04%", "1.082%"]], chipAt: [1.10, 3.30],
    foot: "multpl.com's own series records 1.08% in July 2026 as the all-time minimum of the 1871 series",
    footAt: 4.10,
    framings: [2.500, 5.013], bg2: "s56b.jpg", swapAt: 2.500,
    img: "s56.jpg",
    note: "TWO READS — ladder C, the chips ARE the statement (§5), and §7 row 56 declares the framing `swap`. ⚠ THE SWAP POINT IS RE-CUT FROM §6c's 4.100 TO 2.500 AGAINST A MEASURED WORD ONSET, and this is one of the two decisions this chapter makes against a declared hand-off. §5 states in as many words that its `f` fractions are a FALLBACK and that fin-build resolves each against faster-whisper word timings, using the fraction only if the word FAILS to align. It aligned: «another reads 1.08» runs 2.480-3.920 in 5.4.mp3 => scene +2.730 to +4.170. At §6c's 4.100 the 0.50s cross-dissolve runs 4.100-4.600 with its MIDPOINT AT +4.350, i.e. it would COMPLETE 0.43s after its own phrase had ended and would land in the silence before «and July» — the same family of defect as hi ch5's s57, which completed 0.02s BEFORE its phrase began, and the same rule applied to a miss in the other direction. At 2.500 the midpoint is +2.750, inside «another» (2.730-2.950): the picture changes ON the word that names the second read. INDEPENDENTLY CORROBORATED: tools/tts/clauses.py --cells 2 puts this line's first clause boundary at scene +2.77, 0.02s from the measured word onset. The framings still partition the scene exactly (2.500 + 5.013 = 7.513) and neither exceeds the 9.0 cap; framing 1 now covers exactly «One tracker reads 1.04» and framing 2 covers «another reads 1.082, and July was the lowest on record», which is one framing per read. ⚠ §10's row for this slot («tighter on the second table») DESCRIBES A FILE THAT DOES NOT SHIP — fin-assets' query returned a coiled cloth tape measure, not two printed tables, and the crop was therefore derived against the FILE rather than against the text (the same move that produced `container_ladder_CORRECTION_2026-08-09`). s56b.jpg is ffmpeg crop=1600:900:280:180 on the promoted parent: it drops the dark left margin and the blurred top, and lands the tape's SECOND graduated scale — the numbered 36/35/34 tail — 1.175x larger and near frame centre. Two reads, two framings, one object. ⚠ THE CASCADE IS SPEECH-ANCHORED, two separate pop() calls at two measured word onsets, never popEach at a fixed +1.10/+1.70 (owed.cascade_offsets_ignore_the_voice): «1.04» runs 0.720-1.600 => scene +0.97 to +1.85 and the chip fires at +1.10, INSIDE its own figure and clearing the kicker by the 0.80s floor; «1.08» runs 2.960-4.170 => scene +3.21 to +4.42 and the chip fires at +3.30. Gap 2.20, which is the shape of this sentence and not a template's 0.6. ⚠ clauses.py WAS RUN AND ITS ANSWER WAS REJECTED FOR THE CHIPS, with its own docstring as the reason: --cells 2 returns +2.77 and +4.95, and its first cell is 1.8s late because this sentence's FIRST named item lives in the opening clause it deliberately drops. Word onsets win on this line, the same call ch4 made on 4.6. Two of the chapter's four number frames are macros on warm dark grounds (this and s62, six scenes apart) — different objects, different beats, flagged by fin-assets as a watch rather than a defect." },

  { line: "5.5", arch: "d", f1: "#131f2c", art: "tank", ctr: false, ken: "o", role: WARN,
    band: true, brule: 400, artOpts: { slice: false },
    kick: "SAME TANK, SMALLER TAP",
    stmt: "Take only what it hands you.\nAbout 1%.",
    img: "s57.jpg",
    note: "SAME TANK, SMALLER TAP — the second tank callback, and ⚠ THE FIRST OF §11's THREE DECLARED CONTRADICTIONS: a `--warn` scene on the cool #131f2c. §11 declares s57/s58/s59 deep cool precisely so a later pass cannot 'fix' them — cold is neutral, so it asserts nothing, and this is the drop. ⚠⚠ THE TANK IS NOW DRAWN, ATTEMPT 3, REVERSING ATTEMPT 2's DECLARED NON-APPLICATION. fin-review measured the shipped frame and found the callback ships with NO TANK AND NO VISIBLE STREAM — `chapters._carry_forward_en_ch4_to_ch5_s57`, landing exactly where ch4 predicted — and the orchestrator pulled the fix OUT of `owed.en_preassembly_batch` and into this rebuild, because s61's blocker buys a ch5 draft render anyway and deferring would cost the batch an extra composition. What ships here is en ch4's OWN parameterised layer (`svg.art.v-tank`), re-origined and not redrawn: one constant `TANK` object, one `tank()` function, copied from ../passive-income-number-en-ch4/build.mjs with ONE added option (`slice:false`) and ONE moved origin. Attempt 2's four reasons are answered rather than ignored: (i) §8 refuses a DIAL («one dial moving 4.0 -> 1.08»), which is not what this is — no dial is drawn; (ii) the ruling's scope paragraph named 4.7 and 2.2 because 5.5 had not yet been measured on an encode, and the review that measured it is what re-scoped it; (iii) §8's zero-drawn-layer budget for this chapter is superseded on both scenes by rulings dated after the storyboard, and TWO in a sixteen-scene chapter is half the archetype note's own top-of-range; (iv) the aperture objection stands and is honoured — ONE tap is drawn and NO second tap beside it, so nothing here says a yield and a withdrawal rate are the same kind of thing. ⚠ RULE 8 IS SATISFIED ON THE OBJECT, NOT ARGUED AROUND: the photograph is a tiny wall spigot above a large EMPTY galvanised bucket — a CATCHING vessel and an outlet. What no photograph of a spigot can assert is the SUPPLY behind it, a finite reservoir being metered; that is what the drawing adds, and it is the device 2.2 planted and 4.7 called back. ⚠ THE LEVEL IS DECORATIVE AND ASSERTS NO QUANTITY (`no_return_promise`) and here it does not move AT ALL: this scene emits the tank with `slice:false`, i.e. ONE water rect at the level ch4's 4.7 exit left it on, so there is no tick, no scale, no numeral, NO GHOST of a previous level and no second drop to read as a distance. The ONE state change is the tap CLOSING — `span(#s57-stream, 2.4 -> 1.0)`, the exact reverse of 4.7's widening, on the same rect with the same measured `transform-origin:0% 50%` (ch4 caught a 50%/0% form rendering ~860px left of its own x). GEOMETRY RE-ORIGINED AND MEASURED, not eyeballed: TANK.x moves 600 -> 1000 so the drawn vessel does not land ON the photographed bucket, which occupies screen x 166-889 (source x 260-880 through cover at 1.1847 minus 153.6). At x1000 the mechanism runs screen x1000-1674, y604-960 — clear of the bucket, inside the 970px bottom safe line, left of the watermark box (x1772-1856, y956-1040) and inside the 1770px right safe edge. GROUND MEASURED: that region of the source is the whitewashed wall, src median 128 => graded 77, so it is the light-on-light case rule 9 forbids fixing on the photograph; the `.band` at z-index 0 UNDER the plate darkens BEHIND the mechanism only (alpha .22 at y604 to .63 at y960), taking the ground to ~50 against cream ink at .52 => ~4.3:1. ANCHORS MEASURED on 5.5.mp3 (base.en, word timestamps, +0.25 lead-in): «same tank» 1.480-2.140 => scene +1.73 to +2.39, and the art's 0.60s fade at +1.10 completes at +1.70, the instant the words arrive; «only take what it hands you» 3.420-4.700 => +3.67 to +4.95, and the stream closes over +3.67 to +4.37, inside its own clause. Assembled at +1.70 on a 7.67s scene, so the +2.6 contact sheet shows a finished mechanism and only its state change is later. `.centred` comes OFF for the same reason ch4's 4.7 dropped it — a centred scene display:none's its own plate — and archetype D's stack is top-left either way, so NO type moves and both focal lines (1247.1 / 441.3px at 88) sit inside `.arch-d .huge`'s 1480 cap. ⚠ RESIDUAL, unchanged from fin-assets: the photograph is black-and-white and the spigot is black iron, so it carries neither the brass constant nor the colour of the other three tank frames. ⚠ PRE-ASSEMBLY PASS 2026-08-12, item 4 of owed.en_preassembly_batch, and NOTHING ELSE ON THIS SCENE MOVED — same timings, same photograph, same geometry, same ken, same ground, same band, same anchors. The drawn layer rests at ART_OP 0.74 instead of `.art-forward`'s .52, because the scrim composites OVER the plate. MEASURED ON RENDERED FRAMES at the same time (27.80s) before and after: the vessel wall goes rgb 75-on-37 to rgb 91-on-37, i.e. 1.69:1 -> 2.18:1 and dRGB 39.3 -> 52.7; the floor rail goes 1.60:1 -> 2.06:1. The build's own pre-scrim prediction for this scene was ~4.3:1 and it is NOT reachable at any opacity — see ART_OP. Note also that this scene's cream reads better than the ratio suggests and its WATER does not: the water is `--warn` at fill-opacity .5 over a warm ground, rgb 53-on-40, which is a chroma edge that a luminance ratio cannot see." },

  { line: "5.6", arch: "d", f1: "#0e1c2e", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "SAME DIVISION",
    stmt: "Change only the rate.",
    img: "s58.jpg",
    note: "SAME DIVISION — the frame that cues the cut. 5.6 literally says «watch what happens to the number», which is why §12 makes the NEXT boundary one of the cut's only two shoves. Second of the three declared cool `--warn` grounds, one step colder than 5.5. The focal is 21 chars => 112px on one line at a measured 1201px, the largest type in the chapter after the .mega, and it is the whole frame: a hand on a single dial on a plain instrument panel, hand only, no face. NO drawn layer — §8 refuses 5.5/5.6's dial candidate as depictive, and this photograph IS the dial. ⚠ fin-assets records that this frame carries no hand although §10 lists s58 among the five hand frames; the panel states the beat without one, declared there and unchanged." },

  { line: "5.7", arch: "b", f1: "#0c1a2c", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "THE ANSWER", rate: "AT A 1.08% DIVIDEND YIELD",
    num: "$5,555,556", numTo: 5555556, numPrefix: "$", numAt: 4.95,
    foot: "$60,000 divided by 0.0108 · ILLUSTRATIVE ARITHMETIC",
    img: "s59.jpg",
    note: "THE ANSWER — ⚠ PEAK 2 (§9c), the title's own promise paid in full, at 70.8% of the cut, and the reward beat the whole video is built around. It gets four things PEAK 1 does not: a SHOVE into it (declared below, and unlike every earlier chapter's shove this one is INSIDE the project), the three coldest grounds in the video arriving at #0c1a2c here — the drop is a temperature event before it is a number — the emptiest photograph in the cut, and NO measure bar, deliberately: $5,555,556 is 2,603px against a 920px track, it is off the ladder's scale, and the frame says so by carrying nothing but the number, its yield and its arithmetic. The rate is a first-class 40px .sub arriving at +1.10, 3.85s BEFORE the figure lands: the assumption is on screen first and the number arrives into it (§4). ANCHOR MEASURED: «5» of «five point six million» starts at 4.700s into 5.7.mp3 => scene +4.95, where §5's fraction said +5.12 (0.17s late). ⚠ THE PAYOFF-LEGIBILITY CLAUSE (`payoff_clause_and_metric_2026-08-08`) IS THE ONE OPEN FINDING IN THIS CHAPTER AND IT IS DECLARED, NOT PAPERED OVER. On this build's composed chain s59 measures median 25.01 (rank 13 of 16, i.e. 4th LOWEST), p10 15.43 (also 4th lowest) and a step-in from s58 of -2.21. The clause wants: sound-off pass · top quartile on median (ceil(16/4) = top 4) · #1 or #2 on p10 · non-negative step in. The SOUND-OFF GATE PASSES cleanly — a loading-dock bay: pallet stack, roller door, EXIT sign, fluorescent tubes, concrete pillars, nameable in two words with the type covered — and near-zero spread is not being claimed as a credit either way (p90-p50 is 13.49, 8th of 16). The other three limbs FAIL. NO LEVER EXISTS AT THIS STAGE AND NONE WAS FAKED: the ruling says the lever is ALWAYS the photograph, and assets passed a terminal gate; the bgpos knob was swept at five positions and moves the median 23.83 -> 25.46, i.e. 0.45 points at best and INSIDE the 1.0-point tie band; and the only way to make the step-in non-negative from here is to darken s58 on purpose, which is gaming the metric rather than fixing the frame. fin-assets saw this and said so («s59 is the chapter's most substantive beat and is visibly its lowest-key frame … settle this on the encode, not on my read»), and it lifted s60, s63 and s66 as a side effect of fixing real defects, which raises the floor AROUND s59 without touching it. Per `predictions_missed_a_sixth_time_2026-08-10` this is a SHORTLIST, not a verdict: en ch4's magnitudes reproduced to within 2.45 while its rank ORDER still moved at ranks 4-11, which is exactly the band s59 sits in. THE ENCODE SETTLES IT. If it holds there, the fix is this frame's photograph and nothing else — never the ground, never the scrim, never the grade." },

  { line: "5.8", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "SAME PAYCHECK",
    stmt: "$1,500,000 AT 4.0% ·\n$5,555,556 AT 1.08%",
    rateSpan: "4.0%", rate2Span: "1.08%", rate2At: 4.30,
    img: "s60.jpg",
    note: "SAME PAYCHECK — §4 row 8, the only frame in the cut carrying TWO rate spans, and the one that makes the whole chapter legible: both numbers are true and the only thing between them is an assumption. ⚠ THE FOCAL TAKES NO ROLE CLASS AND THE TWO SPANS DO, and that is §1's own thesis check rather than a style choice: «amber never lands on $5,555,556 — it is a price, not a candidate». Amber here means A RATE UNDER EXAMINATION, so `4.0%` and `1.08%` are amber and the two corpora print in --ink. A build that colours the parent .huge and leaves the spans bare renders amber across a figure the storyboard forbids it on, and passes every check. Both spans are real #sN-rate elements, so the rate assert's `[id^=s60-rate]` sweep finds either. THE PULSES ARE MEASURED: §4 fixes the first at +1.90 and faster-whisper puts «4%» at 1.060-1.740 in 5.8.mp3 => scene +1.31 to +1.99, so the fixed cue lands INSIDE its own words; the second is anchored at +4.30, inside «about 1%» (3.840-4.640 => +4.09 to +4.89), because a comparator that never gets a beat is a node the assert finds and the viewer does not. Gap 2.40. The line break is at the `·`, which stays with the item it follows: unbroken the focal measures 1722px against the 1500px box, and the two lines measure 848 and 853. Two identical kraft envelopes on a white ground — fin-assets re-queried this slot after the shipped version measured source YHIGH 93, under the 110 floor, on a black ground; the material rule it recorded is that matte kraft has no specular ceiling, so the GROUND has to supply the highlights." },

  { line: "5.9", arch: "b", f1: "#3b1219", art: "marks", ctr: false, ken: "o", role: WARN,
    darkGround: "the marks sit on source x1477-1642 / y422-734 of s61.jpg, which measures "
      + "src p10 2 / median 9 / p90 27 => graded p10 0 / median 0 / p90 11 — the darkest ground "
      + "in the frame. Cream ink at .art-forward's .52 reads about 5:1 there, so a .band would "
      + "darken the bottom of a photograph to solve a problem that does not exist (rule 9).",
    kick: "THE GAP",
    num: "ROUGHLY\n4 TIMES", numAt: 4.55,
    foot: "The exact ratio is a quotient of two soft decimals,\nso it is shown rounded and never spoken as a decimal",
    footAt: 1.10,
    img: "s61.jpg",
    note: "THE GAP — ⚠ #3b1219, THE HOTTEST FRAME IN THE VIDEO, spent exactly once (§11 rule 2), on the beat where the identical paycheck is priced at roughly four times. NO countUp: `ROUGHLY 4 TIMES` is a rounded ratio and not a quantity that accumulates, and counting to it would be inventing precision the foot exists to disclaim. NO #s61-rate either — §4 gives a separate rate element only to frames printing a corpus or a derived income, and this frame prints neither; the two rates it compares are on screen one scene earlier and one scene later. ANCHOR MEASURED AND UNCHANGED: «roughly» starts at 4.300s into 5.9.mp3 => scene +4.55, where §5's fraction said +4.86 (0.31s late). The foot takes cue 2 at +1.10 rather than num+0.80, because the disclaimer is the frame's defence and belongs on screen before the rounded figure, not after it. ⚠⚠ ATTEMPT 2's P1 BLOCKER IS CLOSED HERE, BY BOTH HALVES OF `rulings_binding_on_both_cuts.s61_ratio_becomes_a_drawn_device_over_a_consenting_photograph_2026-08-12`, and neither half works without the other. (b) THE PHOTOGRAPH WAS REPLACED UPSTREAM: the 14-crate wall is gone and s61.jpg is now a top-down bowl of eggs, 1880x1253, re-keyed manifest/CREDITS/.src. ⚠ READ AT FULL RESOLUTION AT THIS BUILD, and the file is not quite its own caption: the `.src` says «four eggs in a bowl and one egg beside it on a dark table» and what ships is FIVE eggs ALL INSIDE the bowl — four in a ring plus one lying across them, whitest and plainly on top. The CARDINALITY the ruling turned on is intact and is what matters (four grouped, one distinct = five), and so is the recorded weakness: the picture states the correct ratio and merely lacks SEPARATION. It is not four-beside-one on a table. Recorded rather than re-fetched, per the ruling's own «nobody re-searches». (a) AND THE RATIO IS NOW A MINIMAL DRAWN DEVICE — five identical 56px squares in one column, four grouped at 24px and the fifth 96px apart. It states a COUNT and nothing else: no scale, no ticks, no numerals, no axis, no track, no baseline. It is NOT §9a's measure bar (§10 rules that off this frame) and `no_return_promise` is satisfied because «roughly four times» is an AUDITED figure already in the locked VO — the device restates a sourced comparison and forecasts nothing. Squares, not discs, ON PURPOSE: a disc over a photograph of eggs is a drawing of an egg, which is rule 8's depictive failure; a square can only be a mark. ⚠ PLACEMENT IS MEASURED AGAINST THE BOWL AND THE KEN, because the ruling says that if the marks fight the eggs the MARKS move. The bowl runs source x260-1430 / y110-1223 => screen x154-1541 at ken 1.0, i.e. it fills the frame vertically and leaves only two wood crescents; ken 'o' runs scale 1.16 -> 1.00 with xPercent +2.5 -> -2.5, so the bowl's right edge sweeps 1618 (at the marks' entrance, +2.5s) down to 1483 (scene end). The column sits at screen x1680-1736 — 55px clear of the bowl at its widest moment and 200px clear by the end, on wood that measures src median 9 => GRADED 0, the darkest ground in the frame, so cream ink at `.art-forward`'s .52 reads at about 5:1 with no band and no darkening of the photograph anywhere (rule 9 never comes up). Column y240-688: inside the p-b plate (x1120-1980, y150-760, so vx 560-616 of a 0 0 860 610 viewBox and nowhere near gotcha 8's vx>800 cliff), clear of the 1770 right safe edge and clear of the watermark box (x1772-1856, y956-1040). ⚠ `.centred` COMES OFF, which is what buys the plate: `.scene.centred .plate` is display:none, so a centred scene cannot hold a drawn layer at all — the same trade ch4's 4.7 made. The type therefore moves to archetype B's own left column and the focal is HARD-BROKEN, measured with fontTools on the shipped NotoSansFinance-var at wght 900: `ROUGHLY 4 TIMES` is 1001.9px against `.arch-b .huge`'s 900px split cap, and it breaks as ROUGHLY (544.1) / 4 TIMES (430.6) rather than the greedy ROUGHLY 4 (634.8) / TIMES (339.9) the cap would have produced on its own. Type SIZE is untouched at 112 — the ladder is stepped, and nothing was shrunk to fit. §10's crate rhyme is NOT restored and must not be: it was already one-legged (ch6's s77 shipped as a steel shipping container, not a crate), so with s61 in the egg family the rhyme is s75/s76 only and §10's text is what is wrong. NOTHING ELSE ON THIS SCENE MOVED: no re-timing, same +4.55 anchor, same foot at +1.10, same ken direction, same ground. ⚠ PRE-ASSEMBLY PASS 2026-08-12, item 4 of owed.en_preassembly_batch — fin-review measured the shipped marks at 2.13:1 against this note's own predicted ~5:1, because `.plate` is z-index 0 and `.scrim` is z-index 1, so the scrim composites over the drawn layer while the type above it is untouched. The prediction in the sentence above ('about 5:1 with no band') was computed PRE-SCRIM and that is exactly the error. The marks now rest at ART_OP 0.74 and NOTHING ELSE MOVED — same five 56px squares, same column, same x1680-1736, same 24px/96px grouping, same cardinality, same fade at +2.00, same photograph. MEASURED at 56.50s before and after: mark 3 goes rgb 76-on-15 to rgb 100-on-15, 2.15:1 -> 3.12:1, which CLEARS WCAG 1.4.11's 3:1 for a non-text graphic; mark 1 against the gap between marks goes 1.93:1 -> 2.73:1. Rule 9 is still never reached: the eggs themselves measure L 0.358 against the marks' 0.120, so the photograph is four times the drawing and nothing was darkened." },

  { line: "5.10", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "THE MIDDLE ROUTE",
    num: "ABOUT 3%", numAt: 4.21,
    foot: "A broad US high-dividend-equity ETF, 3.11% trailing-twelve-month yield,\nstockanalysis.com, 6 Aug 2026 · three published reads span 3.11-3.41%,\nso the VO says \"about three percent\" · price evidence for an asset class, not a recommendation",
    footAt: 1.10,
    img: "s62.jpg",
    note: "THE MIDDLE ROUTE — §4 lists this among the nine frames carrying a RATE AS THEIR FOCAL, so it takes no separate #s62-rate. The three-line foot is the whole frame's licence to exist: the persona rule forbids a pick, so an asset class can only appear here as PRICE EVIDENCE, and the last clause says so on screen in the same frame as the figure. ANCHOR MEASURED: «roughly» at 3.960s into 5.10.mp3 => scene +4.21 (§5 published no fallback for this line). The foot takes cue 2 at +1.10, 3.11s before the figure. §2 declares this scene DRY and the reason is the argument rather than the pace: the video refuses to recommend between the three routes, and a bass hit on `ABOUT 3%` recommends one whatever the foot says. ⚠ THIS IS THE FRAME THE FLOOR WOULD RELOCATE ONTO if s54 were ever re-fetched (composed median 20.69, second-lowest, 7.66 above the floor) — see the s54 note and the INVARIANT block: it is a figure frame with a published citation, i.e. MORE substantive than 5.2, which is what makes that fix forbidden rather than merely optional. Orange numerals on a black ground, no logo, no legible fund name — `citation_bearing_document_slots_2026-08-09` binds this slot and is satisfied the strong way: there is no document to resolve." },

  { line: "5.11", arch: "b", f1: "#2e2411", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "THE MIDDLE PRICE", rate: "AT A 3.11% YIELD",
    num: "$1,929,260", numTo: 1929260, numPrefix: "$", numAt: 3.57,
    foot: "$60,000 divided by 0.0311 · ILLUSTRATIVE ARITHMETIC",
    img: "s63.jpg",
    note: "THE MIDDLE PRICE — §4 row 9. The corpus with its yield as a first-class 40px .sub at +1.10, 2.47s before the figure. ANCHOR MEASURED: «$1» of «one point nine million» at 3.320s into 5.11.mp3 => scene +3.57 (no published fallback). Amber, not green: §1's green means a division that closed at a rate the video has SOURCED and is reserved in this chapter for rung five; 3.11% is a trailing yield under examination and the frame is priced, not endorsed. DRY, with s62, for the same reason. ⚠ fin-assets REPLACED this frame during its own gate: it shipped as a corridor of ~15 storage doors and was structurally a near-twin of s59 — same deep one-point perspective, same cool industrial vanishing point — which would have put two of the chapter's number frames on the same picture, one of them PEAK 2. What ships is a single closed red roller door with a padlock, which also honours the slot's own cue («a SINGLE storage-unit door, roller shutter closed, plain»). It carries a small `0004` unit plate, declared there as a facility label." },

  { line: "5.12", arch: "d", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "THREE ROUTES",
    chips: [["4.0%", "3.11%", "1.08%"]], chipAt: [1.18, 2.06, 3.36],
    img: "s64.jpg",
    note: "THREE ROUTES — the chapter's only cascade of three, and as of ATTEMPT 2 it is CENTRED. ⚠ §7's own column says `ctr N` and attempt 1 followed it, reasoning that the declared cascade owned archetype D's band; fin-review measured the shipped frame and that reasoning is wrong on two counts, so BOX ITEM 7 OVERRIDES THE COLUMN. (i) The cascade lives in the `.stack` — the TYPE column — and the side box item 7 names is the PLATE's, which `art: off` empties by construction; a stack cannot occupy the other side of itself. (ii) §7 wrote `N` against a photograph that does not ship: the row assumes three parallel painted lanes converging, i.e. something for type to sit BESIDE, and s64.jpg is a top-down of 5-6 lanes carrying a left-turn arrow, two straights and two merges. What shipped was three ~28px chips in the top-left corner of a ~70%-empty asphalt frame, on the chapter's THESIS line («the rate you assume is the entire difference»), and review named it the chapter's one leaving point (findings #2 and #4). NOTHING ON THIS SCENE LIVES IN THE PLATE — the kicker and the one `.row` of three chips are both inside `.stack`, there is no `.plate`, `.vrule`, `.brule` or `.crule` in this document at all — so `.scene.centred .plate{display:none}` hides nothing that exists and the ch4 4.7 trap (a centred scene erasing its own plate content) cannot fire. Costs no asset, adds no drawn layer, contradicts no declared device, and no cue time moves. The chips ride blockframe's own `.row` inside `.arch-d .stack` — not a hand-rolled flex row and not ch3's absolutely-positioned .v-chiprow — so the row inherits the archetype's own left-aligned top-hung column and nothing is positioned by hand. ⚠ THE CASCADE IS SPEECH-ANCHORED AND TWO INSTRUMENTS AGREE (owed.cascade_offsets_ignore_the_voice): tools/tts/clauses.py --cells 3 returns +1.18 / +2.06 / +3.36, and faster-whisper word onsets independently give «three rates» at scene +1.05, «one paycheck» at +2.15 and «and the rate you assume» at +3.41 — agreement to within 0.08 / 0.09 / 0.05 on all three cells, which is the closest corroboration on this run. clauses.py's answer is TAKEN, unlike on 5.4, and the difference is the one its own docstring names: this sentence's first named item is NOT in the dropped opening clause. Gaps 0.88 / 0.88 / 1.30 — the shape of this sentence, not a template's 0.6, and every gap clears the 0.80s floor without needing the cascade exemption. §2 puts this scene on the `counted` list, so cues.py emits three clicks: the COUNT is the point. ⚠ fin-assets declares that the road carries four-to-five painted arrows under a `three routes` line and that the embedded tram rails read faintly European, with no signage, text, plates or vehicles in frame. Left as declared — the chips carry the count and the photograph carries the idea of divergent routes." },

  { line: "5.13", arch: "a", f1: "#1c2027", art: "off", ctr: true, ken: "o",
    kick: "RUNG FIVE",
    stmt: "The whole month.",
    img: "s65.jpg",
    note: "RUNG FIVE — the hand-off into the last rung, no role and no figure: naming a rung is not a claim about one. Sixteen chars => 112px on one line at 1008px. The chapter's shortest scene at 3.909s, which is why nothing but a kicker and a statement is on it. ⚠ fin-assets kept this frame WITH A KNOWN WEAKNESS and named it: the calendar is a CROPPED part-month under a line that says «the whole month, not one slice of it». All five alternatives were worse — four carried `JUNHO`/`AGOSTO` or bilingual Spanish and French day names on a US cut, and the sixth was a single-day planner page, which argues with the line far harder than a crop does. Declared, not resolved; fin-review's call on the encode." },

  { line: "5.14", arch: "c", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "THE WHOLE HOUSEHOLD",
    num: "$78,535", numTo: 78535, numPrefix: "$", numAt: 1.99,
    foot: "Average annual expenditures per consumer unit, 2024 — BLS Consumer Expenditures,\nreleased 19 Dec 2025, USDL-25-1586. Range $35,046 lowest quintile to $150,342 highest",
    footAt: 1.10,
    img: "s66.jpg",
    note: "THE WHOLE HOUSEHOLD — a published BLS numerator, not a corpus, so §4 gives it NO #s66-rate and the in-page assert's BILL branch is what covers it: $78,535 renders with no rate, and `BLS` in the foot is the provenance MARKER that pays for it. Deleting that foot line would fire the branch, which is the point of the arrangement. ANCHOR MEASURED: «$78» at 1.740s into 5.14.mp3 => scene +1.99, the earliest anchor in the chapter and still clear of the +1.90 floor by 0.09s; the foot goes up first at +1.10 so the provenance precedes the statistic. §2 declares every BLS numerator DRY — these are measurements, not landings. ⚠ fin-assets SPENT FOUR SHEETS ON THIS SLOT and changed the OBJECT rather than the adjective, which is worth carrying: the brief wanted `a thick statistical release, body illegible`, and this slot's subject IS text, so three of four sheets died on legible marks invisible at contact-sheet size — a German `Sparda-Bank` binder with an IBAN, a Polish IKEA fiscal receipt in złoty on a dollar line, and the Postal Square Building whose every legible mark names the National Postal Museum. What ships is a row of identical US new-build suburban houses: naming a subject that CANNOT carry text was the root-cause fix, and sound-off `the average American household` is stronger than the document ever was. ⚠ DECLARED by fin-assets and unchanged: a ~1%-of-frame sliver of Tyvek house wrap at the extreme left edge, two small PRIVATE RESIDENCE yard signs, and the fact that s66 and s67 are adjacent domestic exteriors — daylight/dusk, plural/singular, a deliberate plural->singular move matching 5.14 -> 5.15, and worth one editorial look." },

  { line: "5.15", arch: "b", f1: "#12351f", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "RUNG FIVE", rate: "AT A 4.0% WITHDRAWAL RATE",
    num: "$1,963,375", numTo: 1963375, numPrefix: "$", numAt: 5.77,
    foot: "$78,535 divided by 0.04 · ILLUSTRATIVE ARITHMETIC · $6,545 a month",
    meas: 1.0000, mlab: "THE LADDER",
    framings: [4.800, 3.706], bg2: "s67b.jpg", swapAt: 4.800,
    img: "s67.jpg",
    note: "RUNG FIVE, WORKED — the top of the §9a corpus ladder and the ONLY frame in the cut where the measure bar reaches 1.0000. ONE scale for the whole video: 920px = $1,963,375, so this rung is scaleX 1.0000 = 920.0px exactly. NUMERATOR AND DENOMINATOR ARE A PAIR (gotcha 7) — the assert below recomputes 1963375/1963375 from the rendered string and throws if either half is edited alone, and the component may not be re-used at another scale. GREEN, and it is the chapter's only green: §1's --fund means a division that CLOSED at a rate the video has sourced, which is true of 4.0% and of nothing else here. §9a's label reads `THE LADDER`, never `RUNG 3 OF 5` — a rung count is a counter and counters are what the no-rail rule removed. THIS IS THE CHAPTER'S LONGEST SCENE at 8.506s and therefore its only max_scene_seconds risk; §6c resolves it with two framings and the guard below throws if either exceeds 9.0. ⚠ THE SWAP POINT IS §6c's 4.800, KEPT, WITH THE MEASUREMENT RECORDED BESIDE IT — the mirror of s56's re-cut, same rule, different measurement. faster-whisper puts «at four percent» at 4.500-5.220 in 5.15.mp3 => scene +4.750 to +5.470, so the 0.50s cross-dissolve runs 4.800-5.300 with its MIDPOINT AT +5.050, inside «4» (+4.850 to +5.070): the new framing arrives ACROSS the words it is about. Deviating from a terminal-accepted hand-off that is already correct is not a trade this stage makes. s67b.jpg is ffmpeg crop=1600:900:200:120 on the promoted parent — the lit window pushed to frame centre and 1.175x larger, the foreground stone wall and the top sky cut away, natively 16:9 so cover discards nothing, and a different file rather than the same file pointed at twice. ANCHOR MEASURED: «1» of «one point nine six million» at 5.520s into the clip => scene +5.77 (no published fallback), 0.97s after the swap and settled 1.54s before the dissolve. §2 declares rungs two, three and five DRY: only the first rung and the two peaks ring, or the ladder has no shape, and the measure bar is what gives it one visually instead. ⚠ `owed.cue_rung_5_does_two_jobs` REPRODUCES HERE IN ITS SHARPEST FORM: this scene carries the cut's genuine measure bar, span('#s67-mf'), and the dry list means it emits nothing at all — so the one frame with a bar is silent. Ruled not-to-be-fixed mid-run (the fix is a cue-model change touching every chapter of both cuts); recorded, not corrected." },

  { line: "5.16", arch: "b", f1: "#38151a", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "THE SAME MONTH, DIVIDENDS ONLY", rate: "AT A 1.08% DIVIDEND YIELD",
    num: "$7,271,759", numTo: 7271759, numPrefix: "$", numAt: 4.71, countDur: 1.00,
    foot: "$78,535 divided by 0.0108 · ILLUSTRATIVE ARITHMETIC",
    img: "s68.jpg",
    note: "THE SAME MONTH, DIVIDENDS ONLY — the largest number in the video and §2 declares it DRY on purpose: after the reward beat at s59 the cut must stop escalating, or the answer it just paid out gets outbid. Red, because §1's --warn is the price of an assumption rather than a verdict on a strategy — 5.8 already said both numbers are true. ANCHOR MEASURED: «$7» at 4.460s into 5.16.mp3 => scene +4.71 (no published fallback). ⚠ THE countUp IS 1.00s AND NOT THE 1.20 DEFAULT, and it is forced by the settled-figure floor rather than chosen: at 1.20 the figure is settled for 1.186s before the dissolve, 0.014s under the 1.20s floor; at 1.00 it is 1.386s. The anchor did not move — a spoken anchor is not a knob, and the alternative (anchoring on «over», one word earlier) would land the figure before it is named. An empty commercial lot behind a chain fence, wide, flat light: the last frame of the chapter and deliberately the emptiest thing the argument has bought." },
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
if (TIMING.cut !== "en")
  throw new Error(`timing.json is the ${TIMING.cut} cut, not en`);
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
    /* §6c: emit data-framings on EVERY scene. Two scenes declare a pair (s56,
     * s67); the other fourteen emit one value equal to scene_duration, so an
     * absent attribute never has to be read as "one framing" or "not declared". */
    framings: s.framings || [own],
    /* The focal size is keyed on the COPY's length, so a "\n" — a typographic
     * decision, not copy — is flattened out of the count first. */
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

/* format.json scene.max_scene_seconds, and the framings must PARTITION the
 * scene (check_build asserts the same) so a cosmetic split cannot duck it. */
sc.forEach((s) => {
  const sum = +s.framings.reduce((a, b) => a + b, 0).toFixed(3);
  if (Math.abs(sum - s.dur) > 0.002)
    throw new Error(`${s.id} framings sum to ${sum}, scene holds ${s.dur}`);
  s.framings.forEach((f) => {
    if (f > 9.0) throw new Error(`${s.id} holds one photo for ${f}s (max 9.0)`);
  });
  if (s.dur > 9.0 && s.framings.length < 2)
    throw new Error(`${s.id} runs ${s.dur}s past the 9.0 cap on ONE framing`);
  /* A declared framing swap and its photograph are a PAIR: two framings with one
   * file is a dissolve to nothing, and a second file with one framing would be a
   * §10 cut-in, of which this chapter declares none. */
  if (s.framings.length > 1 && !s.bg2)
    throw new Error(`${s.id} declares ${s.framings.length} framings but only one photograph`);
  if (s.bg2 && s.framings.length === 1)
    throw new Error(`${s.id} carries a second photograph that is not a declared framing swap`);
  if (s.bg2 && Math.abs(s.swapAt - s.framings[0]) > 1e-9)
    throw new Error(`${s.id} swaps at +${s.swapAt} but its first framing holds ${s.framings[0]}`);
});

/* ken parity: every IN-CHAPTER boundary alternates, and so does the CHAPTER
 * JOINT — ch4 closed on s52 `i` (its own SCENES table says so), so s53 must open
 * `o` or the two chapters push the same direction across the seam. §6b gives this
 * chapter no hold to interrupt the alternation. */
if (sc[0].ken !== "o")
  throw new Error(`ch4 closes on s52 'i', so ${sc[0].id} must open 'o' — it opens '${sc[0].ken}'`);
sc.forEach((s, i) => {
  if (s.hold) throw new Error(`${s.id} declares a hold; §6b gives chapter 5 none`);
  if (!i) return;
  if (sc[i - 1].ken === s.ken) throw new Error(`${s.id} repeats ${s.ken} — ken must alternate`);
});

/* §3's build guard, hard.
 *  · no `/` and no `?` as COPY: `·` is this cut's separator and the cut asks no
 *    rhetorical questions on screen. Both glyphs ARE in the subset; the ban is
 *    editorial, from the storyboard's own §3.
 *  · no `× ≈ → ▶ ¢`: not verified in the FinanceSans subset, and a missing glyph
 *    renders as tofu with every check green (pipeline_check's own
 *    uncovered_glyphs() is inert on a chapter project, because it keys off the
 *    literal string "FinanceSans" appearing in the composition HTML and the face
 *    is named only in the LINKED blockframe.css).
 *  · no `₹` and no Devanagari: forbidden_currency on the $ cut, and on-screen
 *    copy is English in both cuts.
 * SUBSET dumped with fontTools from tools/scaffold/assets/fonts/
 * NotoSansFinance-var.woff2 (97 codepoints) and re-verified at this build. */
const SUBSET = new Set(
  " !\"#$%&'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_" +
  "abcdefghijklmnopqrstuvwxyz|£·–—‘’“”€₹");
const chipList = (s) => (s.chips || []).flat();

/* ---------------------------------------------------------- the drawn layers
 * TWO, in a sixteen-scene chapter, and BOTH arrive from rulings dated after the
 * storyboard — §8 budgets this chapter zero and refuses four candidates by name.
 * Two is half the archetype note's "three or four in a twelve-to-fourteen scene
 * chapter is the TOP of the range", and the other fourteen scenes are art-off.
 * WHAT IS STILL DECLINED, so the choice stays on the record:
 *   · 5.6's dial — §8 refuses it and the photograph IS a dial. Having drawn the
 *     tank one scene earlier does not buy it.
 *   · 5.12's three lanes — answered by centring, which needs no art.
 *   · s55 and s59 take NO drawn layer of any kind (§8's closing sentence): the
 *     frames carrying the video's big numbers already have their one focal, and
 *     s59 is PEAK 2, which the encode PASSED. Nothing is added near it.
 *   · a §9a measure bar on 5.9 — §10 rules it off this frame, and a bar carries a
 *     SCALE, which is exactly what makes marks the right device and a bar the
 *     wrong one under `no_return_promise`.
 *
 * THE TANK — en ch4's layer, applied to 5.5 (fin-review en ch5 round 1 +
 * `chapters._carry_forward_en_ch4_to_ch5_s57`). COPIED, not redrawn: the constant
 * and the function below are ../passive-income-number-en-ch4/build.mjs's, with one
 * added option and one moved origin, so the two sites cannot drift into two
 * different tanks. `slice:false` emits the water as ONE rect at the level 4.7's
 * exit left it on — no upper slice, therefore no second drop, no ghost of a
 * previous level, no tick, no scale, no numeral. THE LEVEL IS DECORATIVE
 * (`no_return_promise`); the one thing that moves is the tap.
 *
 * ⚠ ORIGIN MOVED 600 -> 1000, and it is measured rather than preferred: at ch4's
 * x600 the drawn vessel would land on the PHOTOGRAPHED bucket (screen x166-889),
 * which is a drawing of the thing the picture already shows. At x1000 the whole
 * mechanism runs screen x1000-1674 / y604-960 — on the wall, clear of the bucket,
 * above the 970 bottom safe line, left of the 1770 right safe edge and left of the
 * watermark box (x1772-1856, y956-1040), which no scene may paint into.
 *
 * CONSTRUCTION (design-chapter-archetypes, "what a drawn layer has to look like to
 * survive the encode"): solid fills only, nothing thinner than 22px, water at
 * fill-opacity .5 — a fill-opacity, not an opacity, because `.has-photo
 * .art-forward .art`'s 52% is !important and a per-scene inline opacity is a
 * no-op. Authored in the p-d plate's OWN space (0 0 1920 656, 1:1 to screen x,
 * y+424), never in 1920x1080. */
/* ART_OP — THE RESTING LEVEL OF BOTH DRAWN LAYERS IN THIS CHAPTER.
 * `.art-forward`'s .52 is what the stylesheet gives; this is what the frame
 * needs, and the gap is `owed.en_preassembly_batch` item 4, raised by
 * fin-review on this chapter's round 2. `.plate` is z-index 0 and `.scrim` is
 * z-index 1, so THE SCRIM COMPOSITES OVER THE DRAWN ART while `.stack` type
 * sits above the scrim and is unaffected — a contrast computed pre-scrim lands
 * at roughly half its predicted value. It is a known compensation, not a
 * z-order bug (chapter-design.css:96 says so), so the z-order is untouched and
 * the knob is the resting opacity.
 *
 * MEASURED ON RENDERED FRAMES, and the method first reproduced fin-review's
 * own numbers before it was trusted (snapshots/qa/pre1 at .52):
 *   s57 vessel wall  rgb 75 on 37  = 1.69:1  (fin-review measured 1.70:1)
 *   s61 mark 3       rgb 76 on 15  = 2.15:1  (fin-review measured 2.13:1)
 * After the lift (snapshots/qa/b1, same times, same ken) the numbers are in
 * this file's s57 and s61 notes.
 *
 * ⚠ THE PREDICTED 4.3:1 AND 5:1 ARE STRUCTURALLY UNREACHABLE AND THAT IS THE
 * FINDING, not this value. Solving the measured line on s57 for 3.0:1 (WCAG
 * 1.4.11, non-text) needs --art-op ~1.0 and 4.3:1 needs ~1.2 — more than fully
 * opaque cream — because the scrim floors the ground and ceilings the ink at
 * once. So .74 is chosen against the two limits the ruling does leave, both
 * measured on this chapter's own frames: the drawn ink must stay well under
 * the TYPE (at .74 it is L 0.086 on s57 against the focal's 0.229), and it
 * must not overpower the PHOTOGRAPH (rule 9) — on s57 it sits between the
 * picture's p99 0.057 and its p99.9 0.144, and on s61 the eggs themselves
 * reach 0.358, four times the marks. One constant, shared byte-for-byte with
 * ../passive-income-number-en-ch4 and -ch2, so three chapters cannot drift
 * into three different levels of the same device. */
const ART_OP = 0.74;

const TANK = {
  x: 1000, y: 180,                     // origin in the p-d plate's own space
  wall: 22, w: 556, h: 356,            // vessel outer box (open top)
  lvl: 120,                            // interior y where the water surface sits
  slice: 96,                           // the slice 4.7 already spent
};
function tank(id, o) {
  o = o || {};
  const t = TANK, iw = t.w - 2 * t.wall, ix = t.x + t.wall;
  const fl = (x, y, w, h, cls, extra) =>
    `      <rect class="${cls}" ${extra || ""} x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  const floorY = t.y + t.h - t.wall;
  const surf = t.y + t.lvl;
  const water = [
    `      <!-- the water. ONE rect here (slice:false): the level is where 4.7's`,
    `           exit left it and it does not move again. No tick, no scale, no`,
    `           numeral, and NO ghost of the old level — a before/after marker is`,
    `           exactly what turns a decorative level into a measured drop. -->`,
    fl(ix, surf + t.slice, iw, floorY - surf - t.slice, "flw", `id="${id}-lvl" fill-opacity=".5"`),
  ];
  if (o.slice !== false)
    water.push(fl(ix, surf, iw, t.slice, "flw", `id="${id}-lvlx" fill-opacity=".5"`));
  return [
    `<svg class="art v-tank" id="${id}-art" style="--art-op:${ART_OP}" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- the vessel: an open-topped tank you filled. Solid ink, ${t.wall}px walls. -->`,
    fl(t.x, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x + t.w - t.wall, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x, floorY, t.w, t.wall, "fl"),
    ...water,
    `      <!-- one tap, on the vessel's own wall: outlet, down-turn, stem, crossbar.`,
    `           ONE tap and no second tap beside it — §8's refusal stands: two`,
    `           apertures side by side would say a yield and a withdrawal rate are`,
    `           the same kind of thing. -->`,
    fl(t.x + t.w, t.y + 180, 118, 24, "fl"),
    fl(t.x + t.w + 94, t.y + 180, 24, 76, "fl"),
    fl(t.x + t.w + 45, t.y + 136, 22, 44, "fl"),
    fl(t.x + t.w + 13, t.y + 118, 86, 22, "fl"),
    `      <!-- the stream. It CLOSES here (2.4 -> 1.0), the exact reverse of 4.7's`,
    `           widening, from the spout's own left edge. ⚠ transform-origin is`,
    `           "0% 50%" and that is MEASURED, not preferred: ch4 authored it as`,
    `           "50% 0%" and the rect rendered ~860px LEFT of its own x under GSAP's`,
    `           SVG transform handling. Do not "tidy" it to a centred origin. -->`,
    fl(t.x + t.w + 94, t.y + 256, 24, 100, "flw",
      `id="${id}-stream" fill-opacity=".5" style="transform-origin:0% 50%"`),
    `    </svg>`,
  ].join("\n");
}

/* THE FIVE MARKS — 5.9, `rulings_binding_on_both_cuts.s61_ratio_becomes_a_drawn_
 * device_over_a_consenting_photograph_2026-08-12` (a). FIVE identical squares in
 * one column, FOUR grouped and ONE apart. It states a COUNT and only a count:
 * every element is the same size, so nothing here can be read as a magnitude, and
 * there is no scale, no tick, no numeral, no axis, no track and no baseline. That
 * is the whole difference between this and the §9a measure bar §10 rules off the
 * frame, and it is why `no_return_promise` is satisfied — «roughly four times» is
 * an audited figure already in the locked VO.
 *
 * SQUARES, NOT DISCS: over a photograph of eggs a disc is a drawing of an egg,
 * which is rule 8's depictive failure. A square can only be a mark.
 *
 * GEOMETRY, in the p-b plate's OWN space (viewBox 0 0 860 610 => screen x+1120,
 * y+150; gotcha 8's vx>800 cliff is 240px away). The column is at vx 560-616 =>
 * screen x1680-1736, which is measured against the photograph AND the ken: the
 * bowl's right edge sweeps screen 1618 -> 1483 from the marks' entrance to the
 * end of the scene, so the marks clear the eggs by 55px at worst and 200px at
 * best. Ground there is graded 0 (see the 5.9 note's darkGround), which is why
 * there is no band and no darkening of any kind. */
const MARK = { x: 560, y: 90, s: 56, gap: 24, apart: 96, n: 4 };
function marks(id) {
  const m = MARK;
  const sq = (i, y) =>
    `      <rect class="fl" id="${id}-m${i}" x="${m.x}" y="${y}" width="${m.s}" height="${m.s}"/>`;
  const out = [
    `<svg class="art v-marks" id="${id}-art" style="--art-op:${ART_OP}" viewBox="0 0 860 610" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- the group of ${m.n}: identical squares, ${m.gap}px apart. -->`,
  ];
  let y = m.y;
  for (let i = 1; i <= m.n; i++) { out.push(sq(i, y)); y += m.s + m.gap; }
  y = y - m.gap + m.apart;                       // the separation, and only that
  out.push(`      <!-- and the ONE, ${m.apart}px apart. Same square, same fill: the`,
           `           device says four-and-one, never four-times-bigger. -->`,
           sq(m.n + 1, y));
  out.push(`    </svg>`);
  if (y + m.s > 610) throw new Error("marks: the column runs past the p-b plate's own rect");
  return out.join("\n");
}

const ART = { tank, marks };

/* The absences, asserted on the emitted MARKUP rather than promised in prose.
 * ⚠ COMMENTS ARE STRIPPED FIRST, and that is not tidiness: written naively this
 * fires on the drawing's own comment saying "no tick, no scale, no numeral" —
 * i.e. it punishes the note explaining the rule and is silenced by deleting it
 * (ch4 hit this; so did the Lottie guard that fired on the CSS comment describing
 * the trap it prevents). */
{
  const strip = (svg) => svg.replace(/<!--[\s\S]*?-->/g, "");
  const t = strip(tank("sX", { slice: false })), k = strip(marks("sY"));
  for (const [name, svg] of [["tank", t], ["marks", k]])
    for (const [what, re] of [["a numeral", /<text/], ["a tick or a scale", /tick|scale|gauge|axis/i],
                              ["a ghost of a previous state", /ghost|prev|before/i]])
      if (re.test(svg)) throw new Error(`${name}: the drawn layer must carry no ${what}`);
  if (/lvlx/.test(t)) throw new Error("tank: 5.5 emits slice:false — no second level drop here");
  if (!/id="sX-stream"/.test(t)) throw new Error("tank: the stream is missing");
  const w = [...k.matchAll(/width="(\d+)"/g)].map((m) => +m[1]);
  const h = [...k.matchAll(/height="(\d+)"/g)].map((m) => +m[1]);
  if (new Set([...w, ...h]).size !== 1)
    throw new Error("marks: the five marks are not identical — an unequal mark states a MAGNITUDE, "
      + "which is the one thing this device may not do (no_return_promise)");
  if (w.length !== 5) throw new Error(`marks: ${w.length} marks, not 5`);
}

const strings = (s) =>
  [s.kick, s.stmt, s.num, s.rate, s.sub, s.foot, s.mlab, ...chipList(s)]
    .filter(Boolean).map(flat);
sc.forEach((s) => {
  strings(s).forEach((t) => {
    const bad = t.match(/[/?₹×≈~→▶¢]/);
    if (bad) throw new Error(`${s.id}: on-screen string carries "${bad[0]}" — banned in this cut`);
    if (/[ऀ-ॿ]/.test(t)) throw new Error(`${s.id}: Devanagari in the -en cut`);
    for (const ch of t)
      if (!SUBSET.has(ch)) throw new Error(`${s.id}: "${ch}" is not in the font subset — tofu`);
  });
  if (s.stmt && s.num) throw new Error(`${s.id}: never a stmt AND a num (§3)`);
  if (s.size && s.size < 76) throw new Error(`${s.id}: focal below the ladder floor`);
  /* one_focal_per_scene, and §9c: the cut's ONE .mega is s55 and it is never
   * .huge and .mega together. Both halves are asserted, in both directions. */
  if (s.mega && s.id !== "s55")
    throw new Error(`${s.id}: the cut's one .mega is s55 (§9c) — never a second`);
  if (s.mega && s.stmt) throw new Error(`${s.id}: .mega and a .huge stmt in one frame`);
  if (s.id === "s55" && !s.mega) throw new Error("s55 IS the cut's one .mega (§9c) — it lost it");
  if (s.rateSpan && !s.stmt.includes(s.rateSpan))
    throw new Error(`${s.id}: rate span "${s.rateSpan}" is not in the focal`);
  if (s.rateSpan && s.stmt.split("\n").every((l) => !l.includes(s.rateSpan)))
    throw new Error(`${s.id}: rate span straddles a line break — the <br> pass would split it`);
  if (s.rate2Span && s.stmt.split("\n").every((l) => !l.includes(s.rate2Span)))
    throw new Error(`${s.id}: the second rate span straddles a line break`);
  if (s.rate2Span && !s.rateSpan)
    throw new Error(`${s.id}: a -rate2 span with no -rate span is §4 row 8 inverted`);
  if (s.rate && s.rateSpan) throw new Error(`${s.id}: two #${s.id}-rate elements`);
  /* §4's own rule: the nine frames whose FOCAL is a rate carry no separate
     #sN-rate, because printing a rate under itself reads as a defect. Four of
     them are in this chapter — s55 ABOUT 1%, s62 ABOUT 3%, plus s56's two rate
     chips and s64's three — so a `rate` on a scene whose focal already IS a
     percentage is a spec error, not a safety net. */
  if (s.rate && /^(ABOUT )?\d+(\.\d+)?%/.test(s.num || flat(s.stmt) || ""))
    throw new Error(`${s.id}: the focal IS a rate — §4 gives it no separate #${s.id}-rate`);
  /* fin-editor finding #6 (hi ch2 s18), mechanised so it cannot come back. A
     figure still rolling when the cross-dissolve starts has not been READ, and
     the check that matters is SETTLED TIME. 1.20s is the floor, and it is what
     forces s55's popDur and s68's countDur to exist. */
  if (s.numAt != null) {
    const lands = s.numTo == null ? (s.popDur == null ? 0.6 : s.popDur)
                                  : (s.countDur == null ? 1.2 : s.countDur);
    const settled = +(s.dur - (s.numAt + lands)).toFixed(3);
    if (settled < 1.20)
      throw new Error(`${s.id}: the figure is settled for only ${settled}s before the `
        + `dissolve — shorten countDur/popDur (do NOT move the spoken anchor)`);
  }
  if (s.foot) {
    const footEnd = (s.footAt != null ? s.footAt
                     : s.numAt != null ? s.numAt + 0.80
                     : s.chipAt ? s.chipAt[s.chipAt.length - 1] + 0.80 : 1.90) + 0.5;
    if (footEnd > s.dur - 0.80)
      throw new Error(`${s.id}: the foot finishes fading in at +${footEnd.toFixed(2)} of a `
        + `${s.dur}s scene — the bottom of the stack is still assembling as it ends`);
  }
  /* A kicker dropped by accident is invisible in the frame and in every check,
     so an absence has to be declared. This chapter declares none. */
  if (!s.kick) throw new Error(`${s.id}: no kicker and no declared exception`);
  if (s.stamp) throw new Error(`${s.id}: §8 gives chapter 5 no .stamp pill`);
  /* image_per_scene is a hard creator rule and a photograph satisfies it merely
   * by loading, so the file has to exist at build. */
  if (!s.img) throw new Error(`${s.id}: no .bg — image_per_scene is a hard creator rule`);
  [s.img, s.bg2].filter(Boolean).forEach((f) => {
    if (!fs.existsSync(`${IMG}/${f}`)) throw new Error(`${s.id}: ${IMG}/${f} does not exist`);
  });
  /* An `art-off` scene must be `.centred` — a split with nothing opposite is a
   * hole, and `.scene.centred .plate` is display:none so there is nowhere to put
   * art anyway. ⚠ ATTEMPT 1 CARRIED AN EXEMPTION HERE ("a declared cascade owns
   * the archetype's band") AND IT WAS WRONG — fin-review finding #2/#4 on the
   * en ch5 draft. A cascade lives in the `.stack`, i.e. in the TYPE column; the
   * side box item 7 is talking about is the PLATE's, and `.art-off` empties that
   * whatever the stack holds. s64 shipped as three ~28px chips in the top-left
   * corner of a 70%-empty frame and was measured as the chapter's leaving point.
   * The exemption is deleted rather than narrowed: box item 7 has no exception,
   * so neither does this. The converse guard below is kept live even though this
   * chapter has no art, because ch6 copies this file and ch6 HAS drawn layers. */
  if (s.art === "off" && !s.ctr)
    throw new Error(`${s.id}: art-off and not centred — that is a hole (box item 7, no exception)`);
  if (s.art !== "off" && s.ctr)
    throw new Error(`${s.id}: .centred hides .plate — the drawn layer would render into nothing`);
  if (s.art !== "off" && !ART[s.art]) throw new Error(`${s.id}: no art named "${s.art}"`);
  /* Rule 9, mechanised in the only form that is representable here: a drawn layer
   * either sits on a `.band` (darkened BEHIND the art, never the photograph) or
   * declares, with a number, that its own ground is already dark enough. s61 takes
   * the second branch — src median 9 => graded 0 on the wood the marks sit on —
   * and a band there would darken the bottom of a photograph for nothing. The
   * escape hatch is a STRING, so it lands in the file and in review. */
  if (s.art !== "off" && !s.band && !s.darkGround)
    throw new Error(`${s.id}: drawn art with neither a .band nor a measured darkGround (rule 9)`);
  chipList(s).forEach((c) => {
    if (c.length > 22) throw new Error(`${s.id}: chip "${c}" is ${c.length} chars (max 22)`);
  });
  if (s.chips) {
    if (s.chipAt.length !== chipList(s).length)
      throw new Error(`${s.id}: ${chipList(s).length} chips but ${s.chipAt.length} onsets`);
    s.chips.forEach((r) => {
      if (r.length > 3) throw new Error(`${s.id}: more than 3 chips in one row`);
    });
    if (chipList(s).length > 5) throw new Error(`${s.id}: cascade over 5 items`);
    s.chipAt.forEach((t, k) => {
      if (k && t <= s.chipAt[k - 1]) throw new Error(`${s.id}: chip onsets are not monotonic`);
      if (t + 0.6 > s.dur) throw new Error(`${s.id}: chip ${k + 1} finishes past the scene`);
    });
  }
});

/* Density: the scene LIST is asserted rather than the count, so a later edit that
 * adds a third drawn layer — or quietly drops one of these two — has to come back
 * through this line and say why. §8 gives this chapter ZERO and BOTH exceptions
 * are rulings dated after the storyboard, named here so the exception cannot be
 * inherited by a chapter that copies this file:
 *   · s57 — `chapters._carry_forward_en_ch4_to_ch5_s57` + fin-review en ch5 round 1
 *     (the callback shipped with no tank and no visible stream), pulled out of
 *     `owed.en_preassembly_batch` on 2026-08-12.
 *   · s61 — `rulings_binding_on_both_cuts.s61_ratio_becomes_a_drawn_device_over_a_
 *     consenting_photograph_2026-08-12`, after 26 contact-sheet rounds proved no
 *     four-against-one photograph exists in either pool.
 * ⚠ BOTH ARE en-ONLY by the text of both rulings — hi ships zero drawn layers and
 * its photographic container ladder is the thing that REPLACES this device. */
{
  const drawn = sc.filter((s) => s.art !== "off").map((s) => s.id).join(",");
  if (drawn !== "s57,s61")
    throw new Error(`chapter 5's two ruled drawn layers are s57,s61; this build has "${drawn}"`);
}

/* --------------------------------------------------------------- INVARIANT
 * `separation_not_rank_2026-08-09` §1: a substantive beat must not be left in
 * the chapter's darkest frame. ONE DIRECTION ONLY. The converse — "the darkest
 * longest-held frame must be the most substantive beat" — is RETIRED, and
 * "satisfied by construction" is not an available answer: that phrase quotes the
 * retired sentence and both fin-assets and fin-build have already spent it once
 * each in good faith.
 *
 * THE FLOOR IS s54 (5.2), measured on this build's own composed chain — cover-fit
 * into .bg's inset:-8% box, ken 1.08 at mid-scene, the locked
 * grayscale(.32) brightness(.62) contrast(1.05), .field at .38 carrying the
 * scene's --f1 two-stop ground, then the four .scrim layers including the
 * per-scene --tint, then BT.601 percentiles (.rules, .glow and .grain are not
 * modelled, the same omission the en-ch4 chain made, so the two columns stay
 * comparable). Composed medians, ascending:
 *
 *   s54 13.03 · s62 20.69 · s67 22.26 · s59 25.01 · s63 25.14 · s68 27.05 ·
 *   s58 27.22 · s56 27.81 · s64 31.09 · s53 33.33 · s55 34.01 · s57 35.62 ·
 *   s61 36.66 · s60 38.98 · s66 40.28 · s65 42.43
 *
 * s54 is alone at the bottom by 7.66 points where the next largest adjacent gap
 * is 1.57, so the §3 OUTLIER LIMB fires — and under
 * `outlier_limb_is_subordinate_to_the_invariant_2026-08-10` §1 is the master
 * clause and §3 serves it, so the limb says when a fix may be DEMANDED, never
 * when one is required in spite of §1.
 *
 * THE DISCHARGE IS ON THE CONTENT OF THE BEAT THAT SITS THERE, in two parts, and
 * the second is the one that decides it.
 *
 * (i) MECHANISED, below. The floor frame must carry nothing to read beyond its
 *     statement — no figure, no rate, no sub, no foot, no citation, no cascade,
 *     no drawn layer, no measure bar. 5.2 scores ZERO on that census against a
 *     chapter mean of 2.06, on the second-shortest scene at 5.711s. The assert
 *     re-derives it at every build and throws the moment an edit gives s54
 *     something to read, so the premise the ruling rests on cannot be broken
 *     quietly. It also checks the other two mechanical limbs: the floor must not
 *     be the payoff (s59) and must not be the longest-held (s67, 8.506s).
 *
 * (ii) ⚠ THAT HALF IS NECESSARY AND NOT SUFFICIENT, and this file says so rather
 *     than letting an assert stand in for an argument. THREE scenes tie at zero
 *     on the census — s53, s54, s65 — so counting elements cannot pick out the
 *     least substantive beat. The discriminator is editorial and is stated so it
 *     can be argued with: of those three, 5.1 states the chapter's PREMISE (the
 *     title's own question) and 5.13 names a RUNG, i.e. a structural position in
 *     the ladder the whole video is building; 5.2 does neither. It names the
 *     route and says it has a price — a hand-off sentence whose content the next
 *     five scenes deliver, and which asserts no rate, no figure and no rung. And
 *     there is NO INVERSION anywhere between argumentative weight and legibility
 *     at the bottom: s53 sits at rank 10 of 16 and s65 at rank 16.
 *
 * NO KNOB WAS SPENT ON s54 AND NOTHING WAS RE-ORDERED TO MAKE IT LOOK SAFER. The
 * bgpos lever was swept at five positions and spans 0.05 composed points (12.99
 * to 13.04) — the frame is uniform dark navy above and below the tag and has no
 * brighter part to point at. The only other lever, a re-fetch, relocates the
 * floor onto s62 at 7.66 separation: line 5.10, `ABOUT 3%`, the middle route, a
 * figure frame carrying a three-line published citation. That is a MORE
 * substantive beat, so the fix is not merely optional — it is FORBIDDEN.
 *
 * ⚠ AND THE ONE THING THIS BLOCK DOES NOT CLOSE: the PAYOFF-legibility clause on
 * s59. See that scene's note. It is a different clause with a different subject
 * and it is left open and declared, not folded into this one. */
const FLOOR = "s54", PAYOFF = "s59";
const load = (s) => [s.num, s.rate, s.rateSpan, s.sub, s.foot, s.meas,
                     s.art !== "off" ? 1 : null, s.chips].filter(Boolean).length;
{
  const f = sc.find((s) => s.id === FLOOR);
  if (!f) throw new Error("INVARIANT: the declared floor scene is not in this chapter");
  if (load(f) !== 0)
    throw new Error(`INVARIANT: ${FLOOR} now carries ${load(f)} thing(s) to read; the floor `
      + `was ruled acceptable BECAUSE 5.2 has nothing to read beyond its statement `
      + `(outlier_limb_is_subordinate_to_the_invariant_2026-08-10). Re-argue it.`);
  if (FLOOR === PAYOFF)
    throw new Error("INVARIANT: the floor is the payoff frame — a defect under every reading");
  const longest = sc.reduce((a, b) => (b.dur > a.dur ? b : a));
  if (longest.id === FLOOR)
    throw new Error("INVARIANT: the floor is the chapter's longest-held frame");
  if (Math.max(...sc.map(load)) < 3)
    throw new Error("INVARIANT: the census stopped measuring anything");
}

/* §9a · the measure bar. 920px = $1,963,375 (rung five, the whole household at
 * 4.0%) => 1px = $2,134.10. This is the ONE scale for all six ladder frames in
 * the cut and it may not be re-used at another. Rung five — the top of it — is
 * this chapter's, and it is the only frame in the video that reaches 1.0000. */
const LADDER_TOP = 1963375;
sc.filter((s) => s.meas).forEach((s) => {
  const src = s.num || s.stmt;
  const corpus = Number(src.match(/\$[\d,]+/)[0].replace(/[^0-9]/g, ""));
  const exact = corpus / LADDER_TOP;
  if (Math.abs(exact - s.meas) > 0.0005)
    throw new Error(`${s.id} measure ${s.meas} != ${corpus}/${LADDER_TOP} = ${exact.toFixed(4)}`);
});

/* ⚠ THE TWO FRAMING SWAPS' CROP GEOMETRY, ASSERTED AGAINST THE FILES ON DISK.
 * `method_learned.an_asset_swap_needs_a_REBUILD_not_only_a_re-render_2026-08-09`:
 * on hi ch3 a re-sourced image was followed by a re-render instead of a rebuild,
 * so the guard that would have caught a 1.249x stale crop never ran. The path
 * being unchanged is exactly what makes that invisible, so the check is on the
 * BYTES.
 *
 * What matters for a SWAP (as opposed to a hold) is not scale continuity — both
 * layers take the IDENTICAL ken, so the move never breaks — but that the second
 * file is a genuine PUSH INTO the first and that `cover` does not silently
 * re-crop it. Both b-files are natively 16:9, so cover discards nothing; both
 * parents are 1880x1253 (1.5004), narrower than 16:9, so cover fits them by
 * WIDTH and the horizontal ratio is the whole story. */
function jpegSize(path) {
  const b = fs.readFileSync(path);
  for (let i = 2; i < b.length; ) {
    if (b[i] !== 0xff) throw new Error(`${path} is not a JPEG`);
    const m = b[i + 1];
    if (m >= 0xc0 && m <= 0xcf && m !== 0xc4 && m !== 0xc8 && m !== 0xcc)
      return [b.readUInt16BE(i + 7), b.readUInt16BE(i + 5)];
    i += 2 + b.readUInt16BE(i + 2);
  }
  throw new Error(`${path} has no SOF marker`);
}
sc.filter((s) => s.bg2).forEach((s) => {
  const [aw, ah] = jpegSize(`${IMG}/${s.img}`), [bw, bh] = jpegSize(`${IMG}/${s.bg2}`);
  if (aw / ah >= 16 / 9)
    throw new Error(`${s.id}: ${s.img} is at or past 16:9, so cover fits it by HEIGHT and the `
      + `push ratio below is the wrong axis`);
  if (Math.abs(bw / bh - 16 / 9) > 0.002)
    throw new Error(`${s.id}: ${s.bg2} is ${(bw / bh).toFixed(4)}, not 16:9 — cover would crop `
      + `the derived framing again and the declared push would not be what ships`);
  const push = aw / bw;
  if (push <= 1.02)
    throw new Error(`${s.id}: ${s.bg2} is only a ${push.toFixed(3)}x push on ${s.img} — a swap `
      + `that does not visibly move is a self-dissolve to the same file`);
  console.log(`swap ${s.id}: ${s.bg2} ${bw}x${bh} is a ${push.toFixed(3)}x push into `
    + `${s.img} ${aw}x${ah}; both under cover with no further crop`);
});

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const PLATE = { a: "p-a", b: "p-b", c: "p-c", d: "p-d" };

function scene(s) {
  const cls = ["scene", "clip", "arch-" + s.arch, "has-photo"];
  /* `.art-forward` (52%) rather than the 30% default on both drawn scenes: each
     one's point IS the proportion, and 30% of an ink fill does not survive the
     scrim and the grain on the encode. */
  cls.push(s.art === "off" ? "art-off" : "art-forward");
  if (s.ctr) cls.push("centred");
  const alpha = s.role === FUND ? ".10" : ".12";
  const style = s.role ? ` style="--tint:rgba(${s.role},${alpha})"` : "";
  const glow = s.role ? ` style="--gl:rgba(${s.role},.16)"` : "";
  const rc = s.role === FUND ? " fundc" : s.role === TARGET ? " targetc"
    : s.role === WARN ? " warnc" : "";
  /* §1's thesis check: on the two-span comparator frame the FOCAL takes no role
     class at all — only the declared spans do, because amber means "a rate under
     examination" and may not land on $5,555,556. */
  const frc = s.rate2Span ? "" : rc;
  const L = [];
  L.push(`\n<!-- ${s.line} · ${s.arch.toUpperCase()} · ${s.f1} · art ${s.art}` +
    `${s.ctr ? " · centred" : " · split"}` +
    `${s.role ? (s.role === FUND ? " · --fund" : s.role === TARGET ? " · --target" : " · --warn")
      : " · no role"}` +
    `${s.bg2 ? " · SWAP to " + s.bg2 : ""}\n     ${s.note} -->`);
  L.push(`<section class="${cls.join(" ")}" id="${s.id}" data-track-index="${s.track}"` +
    ` data-start="${s.start}" data-duration="${s.dd}" data-framings="${s.framings.join(",")}"${style}>`);
  // No per-scene grade override anywhere in this cut: the grade is LOCKED at
  // grayscale(.32) brightness(.62) contrast(1.05) and the chapter archetype
  // layer closes that escape hatch, so the photograph is the only variable.
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(${IMG}/${s.img})"></div>`);
  if (s.bg2)
    // The second photograph. Same class, so the SAME LOCKED GRADE; same z-index,
    // later in document order, so it paints over the first; opacity 0 until its
    // own fade. It takes an IDENTICAL ken to the layer under it, which is what
    // makes the cross-fade a change of FRAMING rather than a jump in motion.
    L.push(`  <div class="bg" id="${s.id}-bg2" style="background-image:url(${IMG}/${s.bg2})` +
      `;opacity:0"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  if (s.band)
    // z-index 0 inline and BEFORE the plate in DOM order, so it paints UNDER the
    // drawn layer. `.band`'s own z-index is 1 (the scrim's band), which would put
    // it OVER a z-0 plate and darken the ART instead of the ground behind it.
    L.push(`  <div class="band" id="${s.id}-band" style="z-index:0"></div>`);
  if (s.art !== "off") {
    L.push(`  <div class="plate ${PLATE[s.arch]}" id="${s.id}-plate">`);
    L.push(`    <div class="plate-in" id="${s.id}-pin"><div class="hatch"></div>`);
    L.push(`      ${ART[s.art](s.id, s.artOpts || {})}`);
    L.push(`    </div>`);
    L.push(`  </div>`);
  }
  L.push(`  <div class="scrim"></div>`);
  if (s.brule)
    L.push(`  <div class="brule" id="${s.id}-br" style="top:${s.brule}px"></div>`);
  L.push(`  <div class="stack" id="${s.id}-stack">`);
  L.push(`    <p class="kicker" id="${s.id}-kick">${esc(s.kick)}</p>`);
  if (s.rate)
    // §4's FIRST form: a first-class .sub at 40px in the scene's role colour,
    // never a 26px foot a density pass can drop. ABOVE the figure on a variant-B
    // scene, because the assumption goes up first and the number arrives into it.
    L.push(`    <p class="sub${rc}" id="${s.id}-rate">${esc(s.rate)}</p>`);
  if (s.sub)
    L.push(`    <p class="sub" id="${s.id}-sub">${esc(s.sub)}</p>`);
  if (s.num)
    // §9c's one .mega. `.v-nowrap` is a one-off BOX property, not a type token:
    // the string measures 1489.7px against a 1500px cap and contains a space.
    // A `\n` in a num is a MEASURED hard break, exactly as in a stmt: 5.9's focal
    // is 1001.9px against `.arch-b .huge`'s 900px split cap, and left to wrap the
    // cap would break it greedily as "ROUGHLY 4 / TIMES" (634.8 / 339.9).
    L.push(`    <p class="${s.mega ? "mega" : "huge"}${rc}${s.mega ? " v-nowrap" : ""}" ` +
      `id="${s.id}-num">${esc(s.num).replace(/\n/g, "<br>")}</p>`);
  if (s.stmt) {
    // §4's SECOND form: the rate as an inline span INSIDE the focal, so no copy
    // is reordered and nothing is printed twice.
    let body = esc(s.stmt);
    if (s.rateSpan)
      body = body.replace(esc(s.rateSpan),
        `<span class="v-rate${rc}" id="${s.id}-rate">${esc(s.rateSpan)}</span>`);
    if (s.rate2Span)
      body = body.replace(esc(s.rate2Span),
        `<span class="v-rate${rc}" id="${s.id}-rate2">${esc(s.rate2Span)}</span>`);
    body = body.replace(/\n/g, "<br>");
    L.push(`    <p class="huge${frc}" id="${s.id}-stmt" style="font-size:${s.size}px">${body}</p>`);
  }
  if (s.chips) {
    // Ladder C. blockframe's own `.row` inside `.stack`, NOT a hand-rolled flex
    // row and NOT ch3's absolutely-positioned `.v-chiprow`. Rows are declared
    // EXPLICITLY because `.row` wraps and a silent orphan is flagged by nothing.
    s.chips.forEach((row, r) => {
      L.push(`    <div class="row" id="${s.id}-crow${r + 1}">`);
      row.forEach((c, k) => L.push(
        `      <div class="chip${rc ? " " + rc.trim().slice(0, -1) : ""}"` +
        ` id="${s.id}-c${r * 3 + k + 1}">${esc(c)}</div>`));
      L.push(`    </div>`);
    });
  }
  if (s.foot)
    L.push(`    <p class="foot" id="${s.id}-foot">${esc(s.foot).replace(/\n/g, "<br>")}</p>`);
  L.push(`  </div>`);
  if (s.meas) {
    // §9a. OUTSIDE .stack on purpose: .measure / .measure-lab position themselves
    // at left calc(50% - 460px), which is why `.centred` does not hide them and
    // why the device survives on a photo-led cut.
    L.push(`  <p class="measure-lab under" id="${s.id}-mlab">${esc(s.mlab)}</p>`);
    L.push(`  <div class="measure under" id="${s.id}-meas">` +
      `<div class="measure-fill fund" id="${s.id}-mf"></div></div>`);
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
 * competing with a ken. A scene with a second photograph gives that layer the
 * IDENTICAL call, so the swap changes the framing and not the movement. */
const kenJs = sc.map((s) => {
  const one = (sel) => `ken("${sel}", S.${s.id}, D.${s.id}, ${s.ken === "i"});`;
  return [one(`#${s.id}-bg`)].concat(s.bg2 ? [one(`#${s.id}-bg2`)] : []).join("\n");
}).join("\n");

const swapJs = sc.filter((s) => s.bg2)
  .map((s) => `fade("#${s.id}-bg2", S.${s.id} + ${s.swapAt.toFixed(2)}, 0.5);`).join("\n");

const kickJs = sc.map((s) => `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 24);`).join("\n");
const stmtJs = sc.filter((s) => s.stmt)
  .map((s) => `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 40);`).join("\n");
const spanJs = sc.filter((s) => s.rateSpan).map((s) => {
  const o = [`pulse("#${s.id}-rate", S.${s.id} + 1.90);`];
  if (s.rate2Span) o.push(`pulse("#${s.id}-rate2", S.${s.id} + ${s.rate2At.toFixed(2)});`);
  return o.join("\n");
}).join("\n");

/* Variant B's cue 2 is whichever qualifier this scene actually has: the rate
 * .sub, else a non-rate .sub, else the foot. */
const cue2 = (s) => (s.rate ? "rate" : s.sub ? "sub" : s.foot ? "foot" : null);
const numJs = sc.filter((s) => s.num).map((s) => {
  const o = [];
  const c2 = cue2(s);
  if (c2) o.push(`rise("#${s.id}-${c2}", S.${s.id} + 1.10, 0.7, 24);`);
  o.push(`pop("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, `
    + `${(s.popDur == null ? 0.6 : s.popDur).toFixed(2)});`);
  if (s.numTo != null)
    o.push(`countUp("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0, ${s.numTo}, "en-US", `
      + `${(s.countDur == null ? 1.2 : s.countDur).toFixed(2)}, `
      + `${JSON.stringify(s.numPrefix || "")}, ${JSON.stringify(s.numSuffix || "")});`);
  if (s.meas)
    o.push(`span("#${s.id}-mf", S.${s.id} + ${s.numAt.toFixed(2)}, 1.2, 0, ${s.meas});`);
  if (s.foot && c2 !== "foot")
    o.push(`fade("#${s.id}-foot", S.${s.id} + `
      + `${(s.footAt == null ? s.numAt + 0.80 : s.footAt).toFixed(2)}, 0.5);`);
  return o.join("\n");
}).join("\n");
/* Ladder A puts the foot at +1.90, or +2.70 when a rate span already took +1.90;
 * ladder C puts it at LAST CHIP + 0.80 (§5's own table). One home for that rule,
 * shared by the emitter and by the cue-gap sweep below. */
const footAt = (s) => s.footAt != null ? s.footAt
  : s.numAt != null ? s.numAt + 0.80
  : s.chipAt ? s.chipAt[s.chipAt.length - 1] + 0.80
  : s.rateSpan ? 2.70 : 1.90;
const footJs = sc.filter((s) => s.foot && !s.num)
  .map((s) => `fade("#${s.id}-foot", S.${s.id} + ${footAt(s).toFixed(2)}, 0.5);`).join("\n");
const chipJs = sc.filter((s) => s.chips).map((s) => chipList(s)
  .map((_c, k) => `pop("#${s.id}-c${k + 1}", S.${s.id} + ${s.chipAt[k].toFixed(2)}, 0.45);`)
  .join("\n")).join("\n");

/* Every authored cue in the chapter, in time order, against
 * format.json cue_min_gap_seconds (0.80) and layout.first_cue_by_seconds (0.5).
 * cues.py validates the SOUND list; this validates the MOTION list it is derived
 * from, which is where a crowded pair is actually authored. It is what forced
 * s55's and s61's feet to take cue 2 and what fixes s56's swap between its two
 * chips rather than beside one of them. */
{
  sc.forEach((s) => {
    const c = [];
    c.push([0.30, `${s.id}-kick`]);
    if (s.stmt) c.push([1.10, `${s.id}-stmt`]);
    if (s.rate) c.push([1.10, `${s.id}-rate`]);
    if (s.sub) c.push([1.10, `${s.id}-sub`]);
    if (s.rateSpan) c.push([1.90, `${s.id}-rate pulse`]);
    if (s.rate2Span) c.push([s.rate2At, `${s.id}-rate2 pulse`]);
    if (s.numAt != null) c.push([s.numAt, `${s.id}-num`]);
    (s.chipAt || []).forEach((t, k) => c.push([t, `${s.id}-c${k + 1}`]));
    if (s.foot) c.push([footAt(s), `${s.id}-foot`]);
    if (s.bg2) c.push([s.swapAt, `${s.id}-bg2`]);
    c.sort((a, b) => a[0] - b[0]);
    if (c[0][0] > 0.5)
      throw new Error(`${s.id}: first authored cue at +${c[0][0]} — layout.first_cue_by_seconds `
        + `is 0.5 and the photograph alone does not satisfy it`);
    for (let i = 1; i < c.length; i++) {
      const g = +(c[i][0] - c[i - 1][0]).toFixed(3);
      if (g < 0.80)
        throw new Error(`${c[i - 1][1]} -> ${c[i][1]} is ${g}s, under the 0.80s floor`);
    }
  });
}

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 5 · what dividends alone actually cost</title>

<!-- ===========================================================================
     CHAPTER 5 — the title's promise, paid in full. The index pays about one
     percent, so the same five thousand a month costs roughly four times what a
     total-return withdrawal needs; then the middle route, then rung five, the
     whole BLS household. SIXTEEN cuts, ${ROOT}s, s53-s68.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the sixteen <audio> rows
     and the root duration are computed from that one file and asserted against
     the shipped cut's GAPS — a re-time is exactly what produces a correct total
     with every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is ${OFF}s (timing.json's own scene_start for line 5.1),
     which is ch4's offset 248.539 plus ch4's declared root 87.279 to within the 1ms
     each chapter's own rounding introduces,
     so the five built chapters abut frame-exact. The LAST scene carries its bare
     scene_duration: a chapter has no successor to cross-dissolve into, and
     tools/cut_assemble.py adds the +${T} overlap back at fold-in.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Sequence A A B C D D B B B B B D A C B B, storyboard section 7's own rhythm
     block, including the declared B B B B B run at s59-s63: the answer, the
     pair, the gap, the middle route, the middle price — five figures and ONE
     argument, with the mechanism changing underneath each time.

     FOURTEEN of the sixteen scenes are art-off and centred. s64 shipped in
     attempt 1 as the one split on storyboard section 7's "ctr N"; fin-review
     measured it and box item 7 wins — a cascade sits in the type column, not on
     the plate's side, so "art: off" had left the split holding nothing. There is
     no exemption in box item 7 and there is none here.

     TWO SCENES CARRY A DRAWN LAYER, both added at attempt 3 by rulings dated
     after the storyboard. Section 8 budgets this chapter ZERO and refuses four
     candidates by name; two of those refusals rested on a premise the shipped
     photographs never carried, and both were settled upstream rather than here:

       s57 (5.5) THE TANK — fin-review found the callback shipping with no tank
           and no visible stream (chapters._carry_forward_en_ch4_to_ch5_s57,
           predicted by ch4). What renders is en ch4's OWN parameterised layer,
           re-origined so the drawn vessel does not land on the photographed
           bucket, with the level frozen where 4.7 left it and ONE state change:
           the tap closes. The level is decorative and asserts no quantity.
       s61 (5.9) THE FIVE MARKS — four grouped, one apart, over a photograph that
           was itself replaced upstream (the 14-crate wall is gone; s61.jpg is a
           bowl of five eggs). Twenty-six contact-sheet rounds proved no
           four-against-one photograph exists in either pool, so the ratio is
           drawn: it states a COUNT and never a magnitude, with no scale, no
           ticks, no numerals and no axis. It is NOT section 9a's measure bar,
           which section 10 rules off this frame.

     Both are en-only by the text of both rulings — the hi cut ships zero drawn
     layers and its photographic container ladder is what replaces this device.
     Section 10's three-beat crate rhyme s61 -> s75/s76 -> s77 is NOT restored and
     must not be: it was already one-legged (ch6's s77 shipped as a steel shipping
     container, not a crate), so the rhyme is s75/s76 and section 10's text is
     what is wrong.

     THE CUT'S ONE .mega IS s55 — ABOUT 1% at 300px, the only time the video
     prints a number that size, and it is the RATE rather than a corpus. Measured
     at 1489.7px against the centred stack's 1500px cap, hence the local
     .v-nowrap.

     TWO SCENES CARRY A SECOND PHOTOGRAPH, both section 6c framing swaps, and
     both b-files are 1600x900 crops derived here with ffmpeg from their own
     promoted parent:
       s56 7.513s split 2.500 + 5.013, swapping across "another reads" — RE-CUT
           from section 6c's 4.100, which would have completed 0.43s after its
           own phrase ended;
       s67 8.506s split 4.800 + 3.706, swapping across "at four percent" — KEPT
           at section 6c's own value, whose midpoint already lands on the words.
     Same rule, two measurements, two different answers. Each is a second .bg
     under the same locked grade, kenned identically to the layer beneath, so the
     change is of FRAMING and never of movement.

     THE CUT'S SECOND SHOVE IS INSIDE THIS PROJECT — s58 -> s59, section 12, the
     reward beat. It is wired below and is not a declaration for the assembler.

     Every scene carries has-photo and a real full-bleed .bg under the LOCKED
     grade. No per-scene brightness override and no background-position anywhere:
     photo_free_scene_ratio is 0 and the photograph is the only variable there is.
     =========================================================================== -->

<link rel="stylesheet" href="assets/blockframe.css">
<link rel="stylesheet" href="assets/chapter-design.css">
<style>
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--bg); }
/* the four plate rects, one per archetype (format.json chapter_design.archetypes).
   TWO are on screen in this chapter — p-d on s57 and p-b on s61, the two drawn
   layers — and each drawing is authored in ITS OWN plate's coordinate space
   (viewBox 0 0 1920 656 and 0 0 860 610), never in 1920x1080. The other two are
   declared because the next chapter of this cut copies this block, and a missing
   rect is how art silently renders at 0x0. Under .has-photo a plate is an
   APERTURE, not a panel (.plate-in gets background:none), so neither rect paints
   anything of its own over the photograph. */
.p-a { left: 0;      top: 0;     width: 1920px; height: 1080px; }
.p-b { left: 1120px; top: 150px; width: 860px;  height: 610px;  }
.p-c { left: 1046px; top: -60px; width: 934px;  height: 1200px; }
.p-d { left: 0;      top: 424px; width: 1920px; height: 656px;  }

/* ONE-OFF, this composition only (hence .v-): storyboard section 4's SECOND rate
   form, an inline span inside the focal, on 5.8. It exists because pulse is a
   TRANSFORM and transforms do not apply to a non-replaced inline box — the span
   would carry the role colour, the assert would find it, and the beat under the
   spoken rate would simply never happen, with every check green. The system has
   no class for this form; blockframe.css owns the colour, this owns the box.
   Ported verbatim from ch4, which ported it from ch3 and ch2. */
.v-rate { display: inline-block; vertical-align: baseline; }

/* ONE-OFF, and it guards a MEASUREMENT rather than a taste. \`ABOUT 1%\` at
   .arch-b .mega (300px, letter-spacing -14px) measures 1489.7px on the shipped
   NotoSansFinance-var at wght 900, against the 1500px .scene.centred .stack cap
   — 10.3px of margin, and the string contains a space, so it can break into two
   300px lines and blow the frame on a rasteriser's rounding. This pins the box;
   it changes no type token and nothing else in the cut uses it. */
.v-nowrap { white-space: nowrap; }

/* NO OTHER LOCAL CSS, and one thing deliberately NOT re-declared: the
   \`class="stamp warn"\` red-on-red defect that hi ch5 found and patched in its
   own <style> block was FIXED UPSTREAM on 2026-08-12 —
   tools/scaffold/assets/blockframe.css now re-states the dark ink on all four
   .stamp.<role> rules at (0,2,0). Re-patching it locally is how a fixed bug
   comes back, so this chapter links the fix and adds nothing. (It carries no
   .stamp in any case; section 8 gives chapter 5 none.) The centred-arch-b
   max-width patch and the centred padding reset live in
   tools/scaffold/assets/chapter-design.css for the same reason. Checked once
   more for a new member of that family, because that note asks every chapter to
   look: ".arch-c .stack { width: 880px }" is already covered by
   ".scene.centred .stack" resetting width to auto on source order, ".arch-d"'s
   1480/1420 caps are line-length rather than plate-avoidance and sit inside the
   centred stack's 1500, and ".sub" carries no per-archetype cap at all — which
   matters here because s67's qualifier is 615px on an arch-b scene. Nothing to
   patch. */
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

/* Cross-dissolves, one call, before the per-scene cues.

   ⚠ THE SHOVE IS REAL HERE, unlike in every earlier chapter of this cut.
   Section 12 gives the cut exactly two act changes: s39 -> s40 (a chapter
   boundary, and therefore the assembler's) and s58 -> s59 (5.6 -> 5.7, at 70.8%
   of the cut) — "watch what happens to the number" is a cut, spoken. That
   boundary is INTERNAL to this project, so motion.js's shove lands on the
   INCOMING section s59 and actually plays. A dissolve there would smuggle the
   title's own answer in as a continuation instead of announcing it. */
sceneTransitions(IDS, S, { acts: ["s59"] });

/* THE PHOTOGRAPH CARRIES THE MOTION — one move per scene, never two. Direction
   alternates at every boundary; section 6b gives this chapter no hold pair to
   interrupt it, and s53 opens 'o' because chapter 4 closed on 'i'. The two
   scenes with a second photograph give that layer the IDENTICAL call, so the
   cross-fade changes the framing and not the movement. */
${kenJs}

/* THE TWO PHOTOGRAPH CROSS-FADES. Both are a real change, so tools/audio/cues.py
   binds a "transition" to each — a framing swap IS a dissolve, and section 6a
   says so in as many words. Both scenes are on the cut's dry list and both still
   emit that transition: dry silences DERIVED CONTENT cues, and a photograph
   changing is a joint-class event.

     s56 +2.50  RE-CUT from section 6c's 4.100. faster-whisper puts
                "another reads 1.08" at scene +2.730 to +4.170, so at 4.100 the
                0.50s fade would run 4.100-4.600 and COMPLETE 0.43s after its own
                phrase had ended, in the silence before "and July". At 2.500 the
                midpoint is +2.750, inside "another". Corroborated independently:
                tools/tts/clauses.py --cells 2 puts this line's first clause
                boundary at +2.77.
     s67 +4.80  section 6c's own value, KEPT. "at four percent" runs scene +4.750
                to +5.470 and the fade's midpoint is +5.050, inside "4". The
                measurement was taken before the value was trusted; it agreed. */
${swapJs}

/* THE TYPE — cue ladder variant A (storyboard section 5) on the statement
   scenes: kicker +0.30 rise y24, statement +1.10 rise y40. Fixed offsets,
   constant whatever a clip's length; every gap is 0.80s and the photograph is
   already up at +0.00, so first_cue_by_seconds (0.5) is met by the kicker.
   Variant A is fixed BY DESIGN — section 5 lists the kicker, the stmt, the
   rate/sub, the foot and every cascade item as fixed, and only the ken, the
   figures, the swaps and the drawn beats as anchored. */
${kickJs}
${stmtJs}

/* Section 4's second rate form — the span inside the focal. 5.8 is the only
   frame in the cut carrying TWO of them, and both take a beat, because a
   comparator that never pulses is a node the assert finds and the viewer does
   not. MEASURED: "4%" runs scene +1.31 to +1.99, so the fixed +1.90 lands inside
   its own words; "about 1%" runs +4.09 to +4.89, so the second pulse is anchored
   at +4.30. The parent .huge carries NO role class on that frame — section 1's
   thesis check forbids amber landing on $5,555,556 — so the two spans are the
   only amber in the frame and the corpora print in --ink. */
${spanJs}

/* THE FIGURE SCENES — cue ladder variant B: kicker +0.30, then the rate or the
   qualifier at +1.10, then the number ANCHORED on its own spoken word with a
   +1.90 floor, then the foot. THE RATE IS ON SCREEN BEFORE THE FIGURE LANDS —
   the assumption is up first and the number arrives into it (section 4).

   EVERY ANCHOR IS MEASURED, not interpolated. Section 5 gives character-offset
   fractions as a FALLBACK and says fin-build resolves each against
   faster-whisper WORD timings. Run on this cut's own clips (base.en, word
   timestamps), the figure's first spoken word starts at:
     5.3   "about"    2.520s into the clip -> scene +2.77  (fallback said 3.07)
     5.7   "5"        4.700s               -> scene +4.95  (fallback said 5.12)
     5.9   "roughly"  4.300s               -> scene +4.55  (fallback said 4.86)
     5.10  "roughly"  3.960s               -> scene +4.21  (none published)
     5.11  "$1"       3.320s               -> scene +3.57  (none published)
     5.14  "$78"      1.740s               -> scene +1.99  (none published)
     5.15  "1"        5.520s               -> scene +5.77  (none published)
     5.16  "$7"       4.460s               -> scene +4.71  (none published)
   Clips start at scene +0.25 (MEDIUM lead_in_seconds), which is the +0.25 in
   each figure above. All three published fallbacks were LATE, by 0.17 to 0.31s.
   Nothing here needed the +1.90 floor; 5.14 is the closest at +1.99.

   TWO DURATIONS ARE SHORTENED AND BOTH ARE FORCED BY THE SETTLED-FIGURE FLOOR,
   not chosen: 5.3's pop is 0.50s (at 0.60 the .mega is settled 1.192s before the
   dissolve, 0.008s under the 1.20s floor) and 5.16's countUp is 1.00s (at 1.20 it
   is settled 1.186s). Neither ANCHOR moved — a spoken anchor is not a knob.

   countUp is for MONEY, in "en-US" (western grouping; en-IN would print
   $5,55,555). ABOUT 1%, ROUGHLY 4 TIMES and ABOUT 3% take a bare pop(): they are
   rounded statements rather than quantities that accumulate, and counting to
   them would invent precision the feet exist to disclaim. */
${numJs}

/* The foot on a STATEMENT scene, and on s55/s61/s62/s66 where it takes cue 2 at
   +1.10 instead: on a figure frame whose foot is the provenance or the
   disclaimer, the defence belongs on screen BEFORE the number, exactly as
   section 4 orders the rate. */
${footJs}

/* 5.4 and 5.12 · THE TWO CASCADES, BOTH SPEECH-ANCHORED — separate pop() calls
   at measured onsets, never popEach at a fixed +1.10/+1.70
   (owed.cascade_offsets_ignore_the_voice).
     5.4  "1.04" runs scene +0.97 to +1.85 and "1.08" runs +3.21 to +4.42, so the
          chips fire at +1.10 and +3.30, each inside its own figure. clauses.py
          --cells 2 was run and REJECTED for this line with its own docstring as
          the reason: it returns +2.77 / +4.95 and its first cell is 1.8s late,
          because this sentence's first named item lives in the opening clause it
          deliberately drops.
     5.12 clauses.py --cells 3 returns +1.18 / +2.06 / +3.36 and is TAKEN, because
          here the first named item is NOT in the dropped clause. Word onsets
          corroborate to within 0.08 / 0.09 / 0.05 ("three rates" +1.05, "one
          paycheck" +2.15, "and the rate you assume" +3.41) — the closest
          agreement between the two instruments on this run. */
${chipJs}

/* 5.5 · THE TANK (en ch4's layer, applied here by fin-review en ch5 round 1 +
   chapters._carry_forward_en_ch4_to_ch5_s57). The band lifts first so the
   mechanism has darkened ground to read against — rule 9, never the photograph —
   then the vessel, then the tap CLOSES. MEASURED on 5.5.mp3 (+0.25 lead-in):
   "same tank" runs scene +1.73 to +2.39 and the 0.60s fade at +1.10 completes at
   +1.70, the instant the words arrive; "only take what it hands you" runs +3.67
   to +4.95 and the stream closes over +3.67 to +4.37, inside its own clause.
   ⚠ THE LEVEL DOES NOT MOVE AT ALL and there is no exit() here: the water is one
   rect at the level 4.7 already left it on. A second drop would be a distance
   travelled down a scale, and the level is DECORATIVE (no_return_promise).
   Assembled at +1.70 on a 7.67s scene, so the +2.6 contact sheet shows a finished
   mechanism and only its state change is later.
   ⚠ THE FADE TARGETS THE RECTS, NOT THE <svg>, AND THAT IS MEASURED RATHER THAN
   styled: .has-photo.art-forward .art sets opacity .52 !important, so an inline
   opacity written onto the svg by GSAP is beaten by the sheet and the tween is a
   SILENT NO-OP — the layer simply stands there from the scene's first frame with
   every check green. Caught on this build's own max-density snapshots
   (snapshots/qa3/b3 at 53.30s, where s61's marks were already up 1.7s before
   their cue). The rects carry no !important of their own, and their fill-opacity
   is a separate property, so element opacity is free to run 0 -> 1. ⚠ en ch4's
   s46 carries the same no-op on its own fade of the svg — reported upward, not patched
   here: that chapter is locked and its band and stream still animate. */
fade("#s57-band", S.s57 + 0.90, 0.50);
fade("#s57-art rect", S.s57 + 1.10, 0.60);
span("#s57-stream", S.s57 + 3.67, 0.70, 2.4, 1);

/* 5.9 · THE FIVE MARKS (s61_ratio_becomes_a_drawn_device_over_a_consenting_
   photograph_2026-08-12). ONE fade, on purpose: the photograph already carries
   the scene's motion (ken), the device is a STATEMENT rather than a mechanism,
   and staggering five marks would be the frame counting them out under a figure
   the foot exists to keep rounded. Up at +2.00, complete at +2.60 — the contact
   sheet's own sample time, so it sheets built — and 1.95s before the figure lands
   on its measured anchor at +4.55, which is the same ordering §4 gives the rate:
   the comparison is on screen first and the number arrives into it. The selector
   is the RECTS for the reason spelled out on s57 above — .art's 52% is
   !important and a fade on the <svg> renders nothing at all. */
fade("#s61-art rect", S.s61 + 2.00, 0.60);

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE RATE ASSERTS — run.json.constraints, mechanised. Carried forward VERBATIM
   from chapters 2, 3 and 4, including the BILL branch, because a per-chapter
   copy that drifts is worse than no assert: tools/check_vo_frame.py reads RATE
   and MARKER back out of THIS block, so the frame-side and the VO-side checks
   can never disagree about what a rate is.

   CHAPTER 5 IS THE DENSEST EXERCISE OF THESE BRANCHES IN THE CUT — five derived
   or corpus figures in sixteen scenes:

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number."
       LIVE on s59 (\\$5,555,556 with a 40px #s59-rate .sub reading "AT A 1.08%
       DIVIDEND YIELD"), s60 (BOTH corpora, with #s60-rate and #s60-rate2 as
       inline spans inside the focal), s63 (\\$1,929,260 + "AT A 3.11% YIELD"),
       s67 (\\$1,963,375 + "AT A 4.0% WITHDRAWAL RATE") and s68 (\\$7,271,759 +
       "AT A 1.08% DIVIDEND YIELD").

   (2) derived_income_carries_assumption (run.json, EXTENDED 2026-08-07): a
       DERIVED INCOME figure — the corpus's own OUTPUT — is the promise the video
       actually makes, so it carries the rate in frame or an explicit ILLUSTRATIVE
       marker, exactly like a corpus. LIVE on s67, whose foot renders
       "\\$6,545 a month" beside a first-class rate AND the ILLUSTRATIVE marker.

   (3) THE BILL BRANCH, added in ch2. (1) is deliberately narrow — it fires only
       on the eight CORPUS tokens, so a published numerator could render
       completely bare and pass. \\$78,535 on s66 is exactly that shape: a BLS
       statistic, not income derived from a corpus, so it must NOT be made to
       carry a withdrawal rate — but "must not demand a rate" is not "may be
       bare". It carries its published provenance in frame, and "BLS" is the
       MARKER that pays for it. Deleting that foot line fires the branch.

   ⚠ THE FOUR RATE-AS-FOCAL FRAMES ARE NOT SOMETHING THIS ASSERT CAN DEMAND AN
   ELEMENT FOR, and that is section 4's own rule: nine frames in the cut carry a
   rate AS THEIR FOCAL and carry no separate sN-rate, because printing a rate
   under itself reads as a defect. Four are here — s55 ABOUT 1%, s56's two chips,
   s62 ABOUT 3%, s64's three chips. None prints a dollar figure, so the assert
   never fires on them, which is honest behaviour rather than a suppression.

   THIS ASSERT IS FRAME-ONLY BY CONSTRUCTION. It reads rendered text, so it
   cannot see a VO line that SPEAKS a figure over a bare frame
   (owed.derived_income_assert_is_frame_only). That half is
   tools/check_vo_frame.py, run against this file at build:
     python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 5

   Throwing is the point: the runtime pass of "hyperframes check" fails on an
   uncaught page error, and a silent console.warn is what let this ship twice.
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

/* forbidden_currency on the $ cut, over the WHOLE emitted document — a comment is
 * shipped text too, and the archive keeps this file. */
if (/₹/.test(html)) throw new Error("a `₹` appears in index.html — forbidden_currency on the $ cut");
if (/[ऀ-ॿ]/.test(html)) throw new Error("Devanagari appears in index.html");
if (/https?:\/\//.test(html.replace(/multpl\.com|stockanalysis\.com/g, "")))
  throw new Error("a network reference appears in index.html — everything is vendored");

fs.writeFileSync("index.html", html);

/* ------------------------------------------------------------- the sound pass
 * DERIVED, never hand-typed (storyboard §2): tools/audio/cues.py reads the file
 * this script just wrote and emits one cue per REAL motion call, at that call's
 * own time, bound through tools/audio/kit.json's helper column. Running it from
 * here rather than as a second command is what guarantees the cue list and the
 * markup came from the same derivation of timing.json.
 *
 * The special cases cues.py cannot derive live in the CUT's own
 * studio/videos/passive-income-number-en/assets/cues-tables.json, written from
 * storyboard §2 by the ch1 build. It ALREADY carries this chapter's entries —
 * s64 on the `counted` list (three routes, three rates: the COUNT is the point)
 * and seven of these sixteen scenes on the `dry` list (s56, s62, s63, s65, s66,
 * s67, s68) — and it is NOT touched here.
 *
 * ONE correction the tool cannot make: cues.py defaults `music` to bed-resolve,
 * and §2/D12 chooses **bed-tension** for this cut — its argument is a COST, not
 * a habit. The bed is a per-video fact, overridden here rather than hand-edited
 * into the generated artefact. */
/* cues.py validates the SHIPPED assets/audio.json as well as the list it just
 * derived, and exits 1 on a `cue_min_gap_seconds` breach in either. Left in
 * place, last build's file is what gets validated — so the run that FIXES a gap
 * dies on the artefact it is fixing. Drop it first. */
fs.rmSync("assets/audio.json", { force: true });
const derived = JSON.parse(execFileSync("python3",
  ["../../../tools/audio/cues.py", "."], { encoding: "utf8" }));
derived.music = "bed-tension";
derived._bed = "bed-tension (storyboard §2 / §13 D12) — cues.py defaults to "
  + "bed-resolve; this cut's argument is a cost, not a habit. Overridden by "
  + "build.mjs, not hand-edited into the generated file.";
derived._hero = "storyboard §7's sfx column asks for a `hero` on s55, s59 and s61 and for "
  + "nothing on s62, s63, s66, s67 and s68. No correction is applied here and none is needed: "
  + "the cut's own dry table already silences those five, so the three heroes that survive are "
  + "exactly the three the storyboard names — §2's rule that only the first rung and the two "
  + "peaks ring. Unlike hi ch5, no hero had to be dropped by hand.";
derived._tick = "⚠ owed.cue_rung_5_does_two_jobs reproduces here in BOTH of its forms, and "
  + "neither is corrected. (a) s60 emits `tick` at 47.389 where §7 row 60's sfx column says "
  + "`reveal`: cues.py's rung 5 is `span('#sN-mf') or pulse('#sN-.*')` and it is reached before "
  + "the fallback reveal, so the rate-span pulse wins. fin-editor has already ruled this shape "
  + "CORRECT where the tick is bound to a real pulse on a rate token — it is, on `4.0%` — and "
  + "ch4's s40 and hi ch5's s42 are the same row. (b) The INVERSE, and it is sharper here than "
  + "anywhere else on the run: s67 carries the cut's one genuine measure bar, span('#s67-mf'), "
  + "and is on the dry list, so the one frame in this chapter that HAS a bar emits nothing at "
  + "all. The fix for both is one cue-model change — a measure bar is a second, non-competing "
  + "event, not a rung in a single-pick ladder — which the run declined to make with chapters in "
  + "flight.";
fs.writeFileSync("assets/audio.json", JSON.stringify(derived, null, 1) + "\n");

const nCues = derived.sfx.filter((c) => c.at != null).length;
console.log(`assets/audio.json: ${nCues} cues (derived by tools/audio/cues.py), music ${derived.music}`);
console.log(`index.html: ${sc.length} scenes, root ${ROOT}s, offset ${OFF}s`);
sc.forEach((s) => console.log(
  `  ${s.id} ${s.line}  start ${String(s.start).padStart(7)}  dur ${String(s.dur).padStart(6)}` +
  `  d-dur ${String(s.dd).padStart(6)}  track ${s.track}  ${s.arch.toUpperCase()}` +
  ` ${s.ctr ? "centred" : "SPLIT  "} ken ${s.ken}  load ${load(s)}` +
  `${s.size ? "  focal " + s.size : s.mega ? "  MEGA 300" : ""}` +
  `${s.numAt != null ? "  num +" + s.numAt.toFixed(2) : ""}` +
  `${s.bg2 ? "  swap +" + s.swapAt.toFixed(2) : ""}` +
  `${s.meas ? "  meas " + s.meas.toFixed(4) : ""}` +
  `${s.role ? (s.role === FUND ? "  fund" : s.role === TARGET ? "  target" : "  warn") : ""}`));
