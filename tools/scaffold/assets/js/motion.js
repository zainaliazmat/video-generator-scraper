/* ===========================================================================
   BLOCKFRAME MOTION — the one motion vocabulary, as ONE file.

   Load AFTER gsap.min.js and BEFORE the composition's own <script>:

     <script src="assets/js/gsap.min.js"></script>
     <script src="assets/js/motion.js"></script>
     ...
     <script>
       var S = { s1: 0, s2: 18.771, ... };          // from timing.json, generated
       sceneTransitions(["s1","s2",...], S);        // cross-dissolves, once
       rise("#s1k", S.s1 + 0.40);                   // then the per-scene cues
       ...
       register();                                  // last line, always
     </script>

   Why this file exists (audit 2026-07-29): each cut used to redefine these
   helpers inline by copying the previous cut. Five videos produced FIVE
   different vocabularies — the newest cut was missing `fill`, `countUp` and
   `drift` entirely, while leaning on `exit` and `popEach`, which were documented
   nowhere. Anything a video needs is here; nothing is redefined per video.

   Determinism (non-negotiable — the renderer walks frames, it does not play):
   no Date.now(), no unseeded Math.random(), no network. Every helper is
   seek-safe: it must render the same at t=X whether X was reached by playing or
   by jumping. That means fromTo() over to(), and no state outside the timeline.
   =========================================================================== */

window.__timelines = window.__timelines || {};
var tl = gsap.timeline({ paused: true });

/* -------------------------------------------------------------- entrances */

/** fade + travel up. The default entrance for a line of type. */
function rise(sel, at, dur, y) {
  tl.fromTo(sel, { opacity: 0, y: y == null ? 40 : y },
    { opacity: 1, y: 0, duration: dur == null ? 0.7 : dur, ease: "expo.out" }, at);
}

/** fade + scale from 0.6. For a thing that ARRIVES — a chip, a card, a stamp. */
function pop(sel, at, dur) {
  tl.fromTo(sel, { opacity: 0, scale: 0.6 },
    { opacity: 1, scale: 1, duration: dur == null ? 0.6 : dur, ease: "back.out(1.7)" }, at);
}

/** pop, staggered across a set. A declared cascade: ≤5 items, 0.6-0.7s apart
    at scene level; the 0.14 default here is for tags INSIDE one card. */
function popEach(sel, at, stagger, dur) {
  tl.fromTo(sel, { opacity: 0, scale: 0.6 },
    { opacity: 1, scale: 1, duration: dur == null ? 0.4 : dur, ease: "back.out(1.7)",
      stagger: stagger == null ? 0.14 : stagger }, at);
}

/** opacity only. The quietest entrance — cut-in photos, footnotes.
 *
 * Fades UP TO THE ELEMENT'S AUTHORED OPACITY, not to 1. This animated to a hardcoded
 * 1 until 2026-08-08, so a layer authored at `opacity="0.22"` rendered at full strength
 * from its first frame and the authored value was dead markup. Found on
 * passive-income-number en ch2 s14, where the reported defect was "the unfilled grey
 * half is 21.7 luma LOUDER than the amber filled half" — the symptom — and the obvious
 * fix, "one opacity line", would have edited a number that was never in effect.
 * A drawn layer over a graded still lives or dies on that value (the ~.2 fill floor),
 * so silently forcing it to 1 is the loudest possible failure of the quietest helper.
 */
function fade(sel, at, dur) {
  gsap.utils.toArray(sel).forEach(function (el) {
    var a = el.getAttribute && el.getAttribute("opacity");
    var to = a != null && a !== "" ? parseFloat(a) : 1;
    tl.fromTo(el, { opacity: 0 },
      { opacity: isNaN(to) ? 1 : to, duration: dur == null ? 0.5 : dur,
        ease: "power1.out" }, at);
  });
}

/* --------------------------------------------------------------- emphasis */

/** scale blip and back. The beat under a spoken number. */
function pulse(sel, at, s) {
  tl.to(sel, { scale: s == null ? 1.12 : s, duration: 0.16, ease: "power2.out", repeat: 1, yoyo: true }, at);
}

/** slow yoyo scale to keep a held focal element alive.
    `dur` is the REAL total run time. It is quantised to whole out-and-back
    pairs so the element always ends exactly where it began — ask for 4s and you
    get 3s, because 4.5s would finish mid-swell and leave a residual scale.
    (The pre-2026-07-29 version took `dur` and ran for 2×dur. It was wrong, and
    one shipped cut breathes an element for 2.6s after `exit` already hid it.) */
function breathe(sel, at, dur, amt) {
  var cyc = 1.5;
  var pairs = Math.max(1, Math.round(dur / (2 * cyc)));
  tl.to(sel, { scale: amt == null ? 1.035 : amt, duration: cyc, ease: "sine.inOut",
    repeat: 2 * pairs - 1, yoyo: true }, at);   // odd repeat ⇒ ends at scale 1
}

/** scaleX from 0. Progress bars, the .fill2 inside a .track2. */
function fill(sel, at, dur) {
  tl.fromTo(sel, { scaleX: 0 }, { scaleX: 1, duration: dur == null ? 0.8 : dur, ease: "power2.out" }, at);
}

/** count a number up, grouped for the cut's locale ("en-US"). Never group with
    a hand-rolled regex — Intl handles the separator rules.
    Seek-safe: the value is derived from the tween's own progress, not accumulated. */
function countUp(sel, at, from, to, locale, dur, prefix, suffix) {
  var fmt = new Intl.NumberFormat(locale || "en-US");
  var box = { v: from };
  tl.to(box, {
    v: to, duration: dur == null ? 1.2 : dur, ease: "power1.out",
    onUpdate: function () {
      var el = typeof sel === "string" ? document.querySelector(sel) : sel;
      if (el) el.textContent = (prefix || "") + fmt.format(Math.round(box.v)) + (suffix || "");
    }
  }, at);
}

/** countUp's mirror — a balance draining, a runway shrinking. */
function countDown(sel, at, from, to, locale, dur, prefix, suffix) {
  countUp(sel, at, from, to, locale, dur, prefix, suffix);
}

/* ------------------------------------------------------------------ exits */

/** fade out. Use it to hand focus over WITHIN a scene — never two focal
    elements on screen at once. */
function exit(sel, at, dur) {
  tl.to(sel, { opacity: 0, duration: dur == null ? 0.4 : dur, ease: "power1.out" }, at);
}

/* -------------------------------------------------------------- the photo */

/** Ken Burns. Alternate `zoomIn` across the video — never two pushes in a row.
    Endpoints are fixed, so a long scene moves more slowly than a short one; on
    a scene over ~22s consider two opposed half-moves instead of one. */
function ken(sel, at, dur, zoomIn) {
  tl.fromTo(sel,
    { scale: zoomIn ? 1.0 : 1.16, xPercent: zoomIn ? -2.5 : 2.5 },
    { scale: zoomIn ? 1.16 : 1.0, xPercent: zoomIn ? 2.5 : -2.5, duration: dur, ease: "none" }, at);
}

/** slow one-way scale for an OVERLAY stack. Not a substitute for a background —
    photo-free scenes are retired (creator rule 2026-07-28). */
function drift(sel, at, dur, amt) {
  tl.fromTo(sel, { scale: 1 }, { scale: amt == null ? 1.035 : amt, duration: dur, ease: "none" }, at);
}

/* ------------------------------------------------------------ transitions
   Before 2026-07-29 every cut hard-cut between all nine scenes. Measured on a
   real master with ffmpeg scdet: boundary frame-delta 5.85-10.72 against a
   mid-scene 0.053-0.377 — 16-200× — and five of eight boundaries tripped a
   generic cut detector.

   HOW IT WORKS. Scenes are position:absolute in DOM order, so scene n+1 paints
   ON TOP of scene n. So we fade the INCOMING scene in; the outgoing one simply
   stays put underneath. For that to be visible, scene n must still be on screen
   during the overlap. Two things are required, and BOTH are asserted by
   `pipeline_check check_build`:

     1. every scene except the last carries  data-duration = its duration + T
     2. adjacent scenes alternate  data-track-index="1" / "2"

   (2) is not optional. `hyperframes check` rejects two overlapping clips on one
   track — verified on a real composition: 8 × `overlapping_clips_same_track`
   with every scene on track 1, and a clean pass once they alternate. Its own
   suggested fix is "move one clip to a different data-track-index". Non-adjacent
   scenes may share a lane; they are nowhere near each other in time.

   Track index is a timing lane, not a paint order — z-order still comes from DOM
   order, so the cross-dissolve is unaffected by which track a scene sits on.

   Root data-duration is UNCHANGED — the last scene is not extended, so the
   video does not get longer. The framework only writes `visibility` on .clip
   elements, so opacity/transform on a <section> is entirely ours. */

/** the default: a cross-dissolve. */
function dissolve(sel, at, dur) {
  tl.fromTo(sel, { opacity: 0 }, { opacity: 1, duration: dur == null ? 0.45 : dur, ease: "power1.inOut" }, at);
}

/** the act change: dissolve + a short directional push. Use at most twice per
    video, on a real turn in the argument — otherwise it stops meaning anything. */
function shove(sel, at, dur, dir) {
  var d = dur == null ? 0.42 : dur;
  tl.fromTo(sel, { opacity: 0, xPercent: (dir === "left" ? -4 : 4) },
    { opacity: 1, xPercent: 0, duration: d, ease: "power2.out" }, at);
}

/** Wire every boundary in one call. `ids` in scene order, `S` the start map.
    `acts` optionally names the scene ids that get a `shove` instead.
      sceneTransitions(["s1","s2","s3"], S, { acts: ["s5"] })
    Scene 1 is never faded — it is the first frame of the video. */
function sceneTransitions(ids, S, opts) {
  var o = opts || {}, acts = o.acts || [], dur = o.duration == null ? 0.45 : o.duration;
  for (var i = 1; i < ids.length; i++) {
    var id = ids[i];
    if (acts.indexOf(id) !== -1) shove("#" + id, S[id], dur, o.dir);
    else dissolve("#" + id, S[id], dur);
  }
}

/* ------------------------------------------------------------ vector art
   Two ways a non-photographic graphic gets on screen. Both are OPTIONAL and
   neither replaces the photograph — `image_per_scene` is a hard creator rule,
   so these sit ON a graded still, never instead of one.
   Full rationale + sourcing: vault/knowledge/design-icons-emoji-lottie.md */

/** stroke-draw an inline <svg> path. The in-house icon animation: no player,
    no asset, and the stroke takes a palette colour. `len` is the path length —
    over-estimate it freely, a too-long dash just starts further off-screen. */
function draw(sel, at, dur, len) {
  var L = len == null ? 400 : len;
  tl.fromTo(sel, { strokeDasharray: L, strokeDashoffset: L },
    { strokeDashoffset: 0, duration: dur == null ? 0.9 : dur, ease: "power2.inOut" }, at);
}

/** Load a Lottie into `el`. ALWAYS use this, never lottie.loadAnimation direct.
    `data` is the animation object from its own vendored assets/lottie/*.js —
    never a `path:` URL: that fetch resolves after the runtime has inspected the
    page and the scene renders blank with every check green.

    It also pins lottie's global registry empty. HyperFrames ships a `lottie`
    runtime adapter that seeks every registered animation to ABSOLUTE
    composition time — a 4s asset in a scene starting at 200s gets seeked to
    200 000ms, lands past its last frame and draws NOTHING. Its discover() pass
    sweeps in every animation lottie knows about, not just ones you register, so
    opting out has to happen here. Verified 2026-07-31 on a real encode. */
function loadLottie(el, data) {
  var anim = lottie.loadAnimation({
    container: typeof el === "string" ? document.querySelector(el) : el,
    renderer: "svg", loop: false, autoplay: false, animationData: data });
  lottie.getRegisteredAnimations = function () { return []; };
  return anim;
}

/** Play a Lottie inside its scene. `at` is absolute, `dur` is how long the
    asset gets — its own length plays it at true speed, less is a faster cut.
    Seek-safe: the frame is derived from the tween's own progress, so a render
    that jumps straight to t=X draws exactly what playback would. */
function playLottie(anim, at, dur) {
  var f = { v: 0 }, last = anim.totalFrames - 1;
  tl.to(f, { v: last, duration: dur, ease: "none",
    onUpdate: function () { anim.goToAndStop(f.v, true); } }, at);
}


/** scaleX between two fractions, linear. The rail's progress fill and B's
    measure bar both need a partial->partial span; `fill` only does 0->1. */
function span(sel, at, dur, from, to) {
  tl.fromTo(sel, { scaleX: from == null ? 0 : from },
    { scaleX: to == null ? 1 : to, duration: dur, ease: "none" }, at);
}

/** The plate's push. `ken` has fixed 1.0<->1.16 endpoints and an xPercent drift
    tuned for a full-bleed photograph; a plate needs EXPLICIT endpoints so a zoom
    can CONTINUE across a cut — the same image across two lines is one move, not
    two (creator rule, firaun-video-motion-card-rules). Scene n ends at `to`,
    scene n+1 starts at exactly that value. */
function plateKen(sel, at, dur, from, to) {
  tl.fromTo(sel, { scale: from == null ? 1 : from },
    { scale: to == null ? 1.08 : to, duration: dur, ease: "none" }, at);
}

/* --------------------------------------------------------------- register */

/** ALWAYS the last line of the composition's script. */
function register() { window.__timelines["main"] = tl; }
