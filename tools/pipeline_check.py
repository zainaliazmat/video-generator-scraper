#!/usr/bin/env python3
"""Machine-checked postconditions for the finance-video pipeline — stdlib only.

A stage is `done` when THIS script says so, never on an agent's say-so (spec E-1).

  # verify one stage's artifacts:
  python3 tools/pipeline_check.py check voice --slug credit-card-trap --cut hi

  # verify AND record the result in vault/videos/<slug>/run.json (the only
  # writer of `done`; the orchestrator calls this, agents never do):
  python3 tools/pipeline_check.py mark voice --slug credit-card-trap --cut hi \
      --attempt 1 --log vault/videos/credit-card-trap/logs/fin-voice-hi-1.md

  # offline fixture test (needs ffmpeg/ffprobe, no network, no credits):
  python3 tools/pipeline_check.py --selftest

Exit codes: 0 = pass · 1 = postcondition failed · 2 = usage / missing input.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORMAT_PATH = os.path.join(ROOT, "tools", "format.json")


def load_format():
    with open(FORMAT_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def vault_dir(slug):
    return os.path.join(ROOT, "vault", "videos", slug)


def studio_dir(slug, cut):
    return os.path.join(ROOT, "studio", "videos", f"{slug}-{cut}")


# Set from --chapter. In the chapter loop (command §3b) a chapter is a standalone
# project whose new files land in <slug>-<cut>-ch<N>/assets-ch<N>/final/, so a
# checker hard-wired to <slug>-<cut>/assets/img/ reports every slot missing and its
# licence assertion reaches nothing — i.e. it goes quiet exactly where the work is.
CHAPTER = None


def project_dir(slug, cut):
    """The HyperFrames project being checked — the chapter's, in chapter mode."""
    if CHAPTER:
        return os.path.join(ROOT, "studio", "videos", f"{slug}-{cut}-ch{CHAPTER}")
    return studio_dir(slug, cut)


def assets_img_dir(slug, cut):
    if CHAPTER:
        return os.path.join(project_dir(slug, cut), f"assets-ch{CHAPTER}", "final")
    return os.path.join(studio_dir(slug, cut), "assets", "img")


# ---------------------------------------------------------------- ffmpeg utils

def ffprobe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", path],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def mean_volume_db(path):
    """SilentClip guard: mean_volume via ffmpeg volumedetect."""
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", path, "-af", "volumedetect",
         "-f", "null", "-"],
        capture_output=True, text=True)
    m = re.search(r"mean_volume:\s*(-?[\d.]+)\s*dB", out.stderr)
    return float(m.group(1)) if m else -999.0


def atomic_write_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)


def load_lines(voice_dir):
    """Canonical lines.json is an ordered [{"id","text"}] array. Legacy shipped
    projects use {"h1": "text", ...} — accept that too, ordered by numeric id."""
    path = os.path.join(voice_dir, "lines.json")
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        def num(k):
            m = re.search(r"\d+", k)
            return int(m.group()) if m else 0
        return [{"id": k, "text": data[k]} for k in sorted(data, key=num)]
    return data


# ---------------------------------------------------------------- stage checks
# Each returns a list of problem strings; empty list = pass.

def check_research(slug, cut, fmt):
    path = os.path.join(ROOT, "vault", "knowledge", "video-studies", f"{slug}.md")
    if not os.path.exists(path):
        return [f"missing study note: {path}"]
    if os.path.getsize(path) < 500:
        return [f"study note suspiciously small (<500 bytes): {path}"]
    return []


def check_facts(slug, cut, fmt):
    path = os.path.join(vault_dir(slug), "facts-staging.md")
    if not os.path.exists(path):
        return [f"missing facts staging file: {path} (fin-facts must never write shared knowledge directly)"]
    text = open(path, encoding="utf-8").read()
    if not re.search(r"https?://", text):
        return ["facts-staging.md contains no source URL — every money claim needs a recorded source"]
    return []


def check_script(slug, cut, fmt):
    path = os.path.join(vault_dir(slug), f"script-{cut}.md")
    if not os.path.exists(path):
        return [f"missing script: {path}"]
    text = open(path, encoding="utf-8").read()
    problems = []
    if len(text) < 500:
        problems.append("script suspiciously small (<500 bytes)")
    bad = fmt["cuts"][cut]["forbidden_currency"]
    if bad in text:
        problems.append(f"currency purity: '{bad}' appears in the -{cut} script")
    return problems


def check_audit(slug, cut, fmt):
    path = os.path.join(vault_dir(slug), f"audit-{cut}.md")
    if not os.path.exists(path):
        return [f"missing audit note: {path}"]
    text = open(path, encoding="utf-8").read()
    if not re.search(r"\bPASS\b", text):
        return [f"audit-{cut}.md does not record PASS"]
    return []


def scene_padding(fmt, slug=None):
    """(lead_in, tail) seconds per scene, with the run's tier allowed to override.

    These are charged PER LINE, so their total scales with line count and a value
    tuned at SHORT's 9 lines is simply wrong at MEDIUM's ~86 — at 0.4+1.0 the first
    MEDIUM cut spent 120.4s of 566s on inter-line padding. The tier owns the value;
    `scene` keeps the SHORT default so an unknown tier still works.
    """
    sc = fmt["scene"]
    lead, tail = sc["lead_in_seconds"], sc["tail_seconds"]
    if slug:
        try:
            tier = json.load(open(os.path.join(vault_dir(slug), "run.json"),
                                  encoding="utf-8")).get("tier")
            t = fmt.get("tiers", {}).get(tier, {})
            lead, tail = t.get("lead_in_seconds", lead), t.get("tail_seconds", tail)
        except (OSError, ValueError):
            pass
    return lead, tail


def expected_seconds(text, rate, tts):
    """Predicted clip length for `text` at `rate` chars/sec, plus the silence the
    voice actually takes at pause punctuation.

    A flat chars/rate estimate models speech as uniform, so it under-predicts any
    line built out of fragments and over-flags it as "wrong text or truncated".
    The cold-open hook is the worst case by construction — the winning format in
    this niche puts the payoff number at 0:00 in short punched clauses, e.g.
    "पाँच हज़ार रुपये महीना। पहला एक लाख — बीस महीने।" measured 5.88s against a
    3.84s flat estimate (+53%) purely because ElevenLabs honours the danda and the
    em-dash. Charging each mark its pause makes the estimate match the delivery
    the script is deliberately asking for.

    Safe in the truncation direction: the tolerance is symmetric, so raising the
    estimate for a pause-heavy line makes a SHORT clip easier to catch, not harder.

    Trailing punctuation is charged NOTHING: the engine trims silence off the end
    of a clip, so a line-final full stop buys real pause between scenes (that is
    what scene_padding is for) but no audio. Charging it flagged two -en lines as
    truncated while an unflagged sibling was measurably faster — 244 wpm against
    239 — i.e. the flag was tracking punctuation, not delivery.
    """
    pauses = tts.get("pause_seconds", {})
    body = text.strip()
    while body and body[-1] in pauses:
        body = body[:-1].rstrip()
    return len(text) / rate + sum(
        body.count(mark) * secs for mark, secs in pauses.items())


def check_voice(slug, cut, fmt):
    return check_voice_dir(os.path.join(studio_dir(slug, cut), "assets", "voice"),
                           cut, fmt, slug)


def check_voice_dir(vdir, cut, fmt, slug=None):
    problems = []
    for name in ("lines.json", "timing.json"):
        if not os.path.exists(os.path.join(vdir, name)):
            return [f"missing {name} in {vdir}"]
    try:
        lines = load_lines(vdir)
        timing = json.load(open(os.path.join(vdir, "timing.json"), encoding="utf-8"))
    except (json.JSONDecodeError, KeyError) as e:
        return [f"unparseable lines/timing json: {e}"]

    tlines = timing.get("lines", [])
    if [l["id"] for l in lines] != [t.get("id") for t in tlines]:
        return [f"timing.json ids do not match lines.json ids "
                f"({len(tlines)} vs {len(lines)} entries)"]

    tts = fmt["tts"]
    rate = fmt["cuts"][cut]["chars_per_second"]
    lead, tail = scene_padding(fmt, slug)
    expect_start = 0.0
    for line, t in zip(lines, tlines):
        lid, text = line["id"], line["text"]
        mp3 = os.path.join(vdir, f"{lid}.mp3")
        if not os.path.exists(mp3):
            problems.append(f"{lid}: missing {mp3}")
            continue
        if os.path.getsize(mp3) < tts["min_clip_bytes"]:
            problems.append(f"{lid}: clip under {tts['min_clip_bytes']} bytes")
        real = ffprobe_duration(mp3)
        if real < tts["min_clip_seconds"]:
            problems.append(f"{lid}: ffprobe duration {real:.2f}s < {tts['min_clip_seconds']}s")
        # R-3: timing.json must carry MEASURED durations, not a char estimate.
        if abs(t.get("duration", -1) - real) > tts["timing_ffprobe_tolerance_s"]:
            problems.append(f"{lid}: timing.json says {t.get('duration')}s, ffprobe says {real:.2f}s")
        expected = expected_seconds(text, rate, tts)
        if expected > 0 and abs(real - expected) / expected > tts["duration_tolerance_pct"] / 100:
            problems.append(f"{lid}: duration {real:.2f}s is >{tts['duration_tolerance_pct']}% off "
                            f"chars/rate estimate {expected:.2f}s — wrong text or truncated clip")
        vol = mean_volume_db(mp3)
        if vol < tts["silence_mean_volume_db"]:
            problems.append(f"{lid}: mean volume {vol:.1f} dB — silent clip")
        # scene arithmetic (design doc §6): the four downstream copies derive from this.
        if abs(t.get("scene_start", -1) - expect_start) > 0.02:
            problems.append(f"{lid}: scene_start {t.get('scene_start')} ≠ cumulative {expect_start:.2f}")
        scene_dur = lead + t.get("duration", 0) + tail
        if abs(t.get("scene_duration", -1) - scene_dur) > 0.02:
            problems.append(f"{lid}: scene_duration {t.get('scene_duration')} ≠ {lead}+clip+{tail}={scene_dur:.2f}")
        if abs(t.get("audio_start", -1) - (expect_start + lead)) > 0.02:
            problems.append(f"{lid}: audio_start ≠ scene_start + {lead}")
        expect_start += t.get("scene_duration", scene_dur)
    if abs(timing.get("total", -1) - expect_start) > 0.05:
        problems.append(f"timing total {timing.get('total')} ≠ sum of scenes {expect_start:.2f}")
    return problems


def script_hash(slug, cut):
    path = os.path.join(vault_dir(slug), f"script-{cut}.md")
    if not os.path.exists(path):
        return None
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def stale_script_problems(slug, cut):
    """X-8: audit-edits-script-after-voice is the NORMAL case, so every stage
    downstream of voice compares the current script hash against the one
    recorded when voice was marked done. Mismatch = stale mp3s."""
    run_path = os.path.join(vault_dir(slug), "run.json")
    if not os.path.exists(run_path):
        return []
    voice = json.load(open(run_path, encoding="utf-8")).get(
        "stages", {}).get(f"fin-voice-{cut}", {})
    recorded = voice.get("script_sha256")
    if recorded and recorded != script_hash(slug, cut):
        return [f"script-{cut}.md changed after fin-voice ran — the mp3s and "
                "timing.json are stale; re-run fin-voice before continuing"]
    return []


def check_storyboard(slug, cut, fmt):
    problems = stale_script_problems(slug, cut)
    sb = os.path.join(vault_dir(slug), f"storyboard-{cut}.md")
    if not os.path.exists(sb):
        problems.append(f"missing storyboard: {sb}")
    manifest = os.path.join(studio_dir(slug, cut), "assets", "img", "manifest.json")
    if not os.path.exists(manifest):
        problems.append(f"missing image manifest: {manifest}")
    else:
        try:
            json.load(open(manifest, encoding="utf-8"))
        except json.JSONDecodeError as e:
            problems.append(f"manifest.json unparseable: {e}")
    return problems


# Calibrated on the 20 promoted images of passive-income-number-hi ch1+ch2, not
# on one bad frame: s4 = 93 (failed by eye TWICE, in both directions), then a
# 30-point gap to s11b = 123 (looked at and passed), then everything else >= 134.
# 110 sits in that gap with margin on both sides. ONE-SIDED ON PURPOSE — the
# opposite failure (a high-key flat TEXTURE reading as a UI panel, e.g. ch2's s16
# at 242) is real but luma does not predict it: ch2's s10 measures 246 and reads
# fine, because numerals and red pins give it structure. That one still needs eyes.
MIN_SOURCE_YHIGH = 110


def luma_high(path):
    """90th-percentile luma of a still. None if ffprobe can't read it."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-f", "lavfi", "-i", f"movie={path},signalstats",
         "-show_entries", "frame_tags=lavfi.signalstats.YHIGH", "-of", "csv=p=0"],
        capture_output=True, text=True).stdout.strip().splitlines()
    try:
        return float(out[0])
    except (IndexError, ValueError):
        return None


def check_assets(slug, cut, fmt):
    idir = assets_img_dir(slug, cut)
    manifest_path = os.path.join(idir, "manifest.json")
    if not os.path.exists(manifest_path):
        return [f"missing manifest: {manifest_path}"]
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    problems = []
    credits = ""
    credits_path = os.path.join(idir, "CREDITS.txt")
    if os.path.exists(credits_path):
        credits = open(credits_path, encoding="utf-8").read()
    # The manifest is the provenance record, so it must cover the library, not a
    # prefix of it. Iterating only the manifest means a stage that dies part-way
    # through writing it leaves a SHORT manifest next to a full img/ dir, and every
    # unlisted photo goes unchecked while the stage reports green. Hit for real on
    # japanese-money-methods-en (2026-08-01): 1 manifest entry, 93 images on disk.
    on_disk = {f for f in os.listdir(idir)
               if f.startswith("s") and f.endswith((".jpg", ".png"))}
    for orphan in sorted(on_disk - set(manifest)):
        problems.append(f"{orphan}: on disk but absent from manifest.json — the "
                        "manifest must name every image, or it is not provenance")
    for name in manifest:
        path = os.path.join(idir, name)
        if not os.path.exists(path):
            problems.append(f"manifest names {name} but it is not on disk "
                            "(dropped cut-ins must be removed from the manifest)")
        elif os.path.getsize(path) < 10240:
            problems.append(f"{name}: under 10KB, not a usable photo")
        elif name not in credits:
            problems.append(f"{name}: no attribution line in CREDITS.txt (licence requirement)")
        elif CHAPTER:
            # Under the chapter archetype layer the grade is locked
            # (grayscale .32 / brightness .62) and per-scene overrides are
            # forbidden, so a source with no highlights has nothing for the grade
            # to leave behind. HIGHLIGHT CEILING predicts survival, not average
            # brightness: on passive-income-number ch1, s3 (YAVG 56.5, YHIGH 134)
            # read fine while s4 (YAVG 59.4, YHIGH 93) rendered as a black slab
            # — s4 was the BRIGHTER of the two on average. Two review rounds and
            # a re-fetch missed it; one ffprobe call catches it before the render.
            # Chapter mode only: plain blockframe still permits an inline filter:
            # override, which is the documented escape hatch for near-black stock.
            y = luma_high(path)
            if y is not None and y < MIN_SOURCE_YHIGH:
                problems.append(
                    f"{name}: source YHIGH {y:.0f} < {MIN_SOURCE_YHIGH} — no "
                    f"highlights to survive the locked grade; it will render as a "
                    f"flat slab. Pick a frame with light falling on the subject.")

    # The loop above is anchored on the MANIFEST, and that is the hole: a late image round
    # that writes new files without updating manifest.json does not merely go unlisted, it
    # goes UNCHECKED — `for name in manifest` never reaches it, so the licence assertion
    # silently does not apply to the one thing being shipped. The orphan message above then
    # reads as bookkeeping ("absent from manifest") rather than as "this photograph is on
    # screen with no attribution". Hit for real on japanese-money-methods (2026-08-06): the
    # -en image round reused 34 -hi photographs under new `sNN-hi.jpg` filenames and carried
    # none of their credit rows, and -hi's own s28-fix.jpg had the same gap; all 35 were on
    # screen in a rendered master, and every stage reported green.
    #
    # So assert against the COMPOSITION, which is the artifact that actually carries the
    # licence exposure and cannot go stale the way a side-file can. Rendered images only —
    # `*-original.jpg` and rejected candidates sit on disk on purpose and are not published.
    # Chapter mode has to redirect BOTH halves. Redirecting only assets_img_dir()
    # left this assertion opening a whole-cut index.html that does not exist yet in
    # a chapter-first run, so it skipped — and its regex could not have matched
    # `url(assets-ch1/final/sN.jpg)` even if it had opened the right file. The
    # manifest half above still passed, so the check reported green over exactly the
    # assertion it exists for. Caught by fin-render on ch1, 2026-08-07, one round
    # after the chapter flag was added to fix the same shape of blindness.
    index = os.path.join(project_dir(slug, cut), "index.html")
    if os.path.exists(index):
        html = open(index, encoding="utf-8").read()
        for name in sorted(set(re.findall(
                r"url\((?:assets/img|assets-ch\d+/final)/([^)]+)\)", html))):
            if name not in credits:
                problems.append(f"{name}: rendered by index.html with no attribution line "
                                "in CREDITS.txt (licence requirement)")
    return problems


def check_build(slug, cut, fmt):
    sdir = studio_dir(slug, cut)
    index = os.path.join(sdir, "index.html")
    if not os.path.exists(index):
        return [f"missing {index}"]
    html = open(index, encoding="utf-8").read()
    problems = stale_script_problems(slug, cut)
    # determinism: no render-time network fetches (E-3 class of silent corruption)
    for m in re.finditer(r'(?:src|href)="(https?://[^"]+)"', html):
        problems.append(f"network fetch in composition: {m.group(1)}")
    # Channel watermark. blockframe.css paints it on #root::after, keyed off the
    # `cut-<cut>` class — so the whole video carries the mark for the price of
    # one class, and a build that forgets it renders an invisible empty box
    # rather than an obviously broken frame. Hence the assert.
    root_tag = re.search(r'<div id="root"[^>]*>', html)
    if root_tag and f"cut-{cut}" not in root_tag.group(0):
        problems.append(
            f'#root is missing the `cut-{cut}` class — that is what selects the '
            f'channel watermark in blockframe.css, and without it the video '
            f'ships unbranded with every other check green')
    root = re.search(r'data-composition-id="main"[^>]*data-duration="([\d.]+)"', html)
    scenes = re.findall(r'<section[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)
    # Per-scene framings, for the dead-frame guard below. A section may declare
    # `data-framings="5.20,3.99"` — the durations of the successive photographs it
    # panel-swaps through. The whole <section> tag is captured so a framing list can
    # be matched back to the scene it belongs to by data-start.
    framings = {}
    for tag in re.findall(r"<section[^>]*>", html):
        st = re.search(r'data-start="([\d.]+)"', tag)
        fr = re.search(r'data-framings="([\d.,\s]+)"', tag)
        if st and fr:
            framings[st.group(1)] = [float(x) for x in fr.group(1).split(",") if x.strip()]
    if not root:
        problems.append("no root data-duration found")
    if not scenes:
        problems.append("no <section> scenes with timing found")
    timing_path = os.path.join(sdir, "assets", "voice", "timing.json")
    if root and scenes and os.path.exists(timing_path):
        timing = json.load(open(timing_path, encoding="utf-8"))
        last_end = float(scenes[-1][0]) + float(scenes[-1][1])
        if abs(float(root.group(1)) - last_end) > 0.5:
            problems.append(f"root data-duration {root.group(1)} ≠ last scene end {last_end:.2f}")
        n = len(timing.get("lines", []))
        if len(scenes) != n:
            problems.append(f"{len(scenes)} scenes but timing.json has {n} lines")
        if abs(float(root.group(1)) - timing.get("total", -1)) > 0.5:
            problems.append(f"root data-duration {root.group(1)} ≠ timing.json total {timing.get('total')}")
    # Dead-frame guard (creator, 2026-07-31: "9 scenes are too low for medium
    # size video ... not dead"). Scene count is emergent — one VO line is one
    # scene — so the thing to bound is how long a single photograph is allowed to
    # sit on screen, not the count. A tier's `lines` figure is guidance an agent
    # can miss; this makes a 57-second held still unrepresentable instead.
    max_hold = fmt.get("scene", {}).get("max_scene_seconds", 0)
    if max_hold and scenes:
        T = fmt.get("scene", {}).get("transition_seconds", 0)
        for i, (start, dur) in enumerate(scenes):
            # every scene but the last is padded by the cross-dissolve overlap
            own = float(dur) - (T if i < len(scenes) - 1 else 0)
            # A scene that panel-swaps to a second photograph does not hold ONE
            # photo for its whole length, so measure the longest framing instead of
            # the section — that is the quantity this guard's own comment describes.
            # Added 2026-08-01 after japanese-money-methods-hi resolved three
            # over-length scenes with declared second framings and s25 still failed
            # by 0.002s; a gate rejecting a frame for two milliseconds is measuring
            # the wrong thing. The sum check is what stops a build from declaring
            # cosmetic framings to duck the guard.
            fr = framings.get(start)
            if fr:
                if abs(sum(fr) - own) > 0.15:
                    problems.append(
                        f"scene {i + 1} data-framings sum to {sum(fr):.2f}s but the "
                        f"scene holds {own:.2f}s — framings must partition the scene")
                    continue
                if max(fr) > max_hold:
                    problems.append(
                        f"scene {i + 1}'s longest framing is {max(fr):.1f}s (max "
                        f"{max_hold}s) — the panel swap does not save it; split the VO line")
                continue
            if own > max_hold:
                problems.append(
                    f"scene {i + 1} holds {own:.1f}s (max {max_hold}s) — split the "
                    f"VO line, or declare a real panel swap with data-framings; one "
                    f"photo on screen this long reads as a dead frame")
    # Transitions: every scene but the last is held `transition_seconds` past its
    # own end, so the incoming scene cross-dissolves over a live frame instead of
    # fading up from black. The overlap IS the transition — if the build writes a
    # bare scene duration the fade still runs and still passes every other check,
    # it just plays against nothing. See tools/scaffold/assets/js/motion.js.
    T = fmt.get("scene", {}).get("transition_seconds", 0)
    if T and len(scenes) > 1:
        for i in range(len(scenes) - 1):
            gap = (float(scenes[i][0]) + float(scenes[i][1])) - float(scenes[i + 1][0])
            if abs(gap - T) > 0.05:
                problems.append(
                    f"scene {i + 1} overlaps the next by {gap:.3f}s, expected {T}s — "
                    f"data-duration must be the scene's duration + transition_seconds")
        # The overlap is only legal if adjacent scenes sit on DIFFERENT tracks.
        # `hyperframes check` fails with `overlapping_clips_same_track` otherwise
        # — verified: 8 errors on a real composition with every scene on track 1,
        # clean once they alternate. Non-adjacent scenes may share a lane; they
        # are nowhere near each other in time.
        tracks = re.findall(r'<section[^>]*data-track-index="(\d+)"', html)
        if len(tracks) == len(scenes):
            for i in range(len(tracks) - 1):
                if tracks[i] == tracks[i + 1]:
                    problems.append(
                        f"scenes {i + 1} and {i + 2} are both on data-track-index="
                        f"{tracks[i]} but overlap by {T}s — alternate 1/2 down the "
                        f"video or `hyperframes check` fails overlapping_clips_same_track")
        else:
            problems.append(f"{len(scenes)} scenes but {len(tracks)} data-track-index "
                            f"attributes — every <section> needs one")
    # Lottie. Three ways to render a blank scene with every check green, so they
    # are checked here rather than trusted to a prose rule. `loadLottie` and
    # `playLottie` (motion.js) do the right thing; these catch a build that went
    # around them. See vault/knowledge/design-icons-emoji-lottie.md.
    if "lottie.min.js" in html:
        va = fmt.get("vector_art", {}).get("lottie", {})
        if "__hfLottie" in html:
            problems.append(
                "composition registers on window.__hfLottie — the runtime adapter "
                "seeks it to ABSOLUTE composition time, so anything past its own "
                "length draws nothing. Use playLottie() instead")
        if re.search(r"loadAnimation\s*\(", html):
            problems.append(
                "calls lottie.loadAnimation() directly — use loadLottie() from "
                "motion.js, which pins the global registry the adapter sweeps")
        if re.search(r"path\s*:\s*['\"][^'\"]*\.json", html):
            problems.append(
                "loads a Lottie by path: — that fetch resolves after the runtime "
                "has inspected the page. Inline the JSON as assets/lottie/<n>.js")
        cap = va.get("max_per_chapter", va.get("max_per_video", 0))
        n = len(re.findall(r"loadLottie\s*\(", html))
        if cap and n > cap:
            problems.append(
                f"{n} Lotties in one cut (max {cap}) — lottie-web redraws the whole "
                f"illustration every frame and it starts reading as a template deck")
    return problems


def check_render(slug, cut, fmt):
    mp4 = os.path.join(studio_dir(slug, cut), "renders", f"FINAL-1080p-{cut}.mp4")
    if not os.path.exists(mp4):
        return [f"missing render: {mp4}"]
    problems = stale_script_problems(slug, cut)
    if os.path.getsize(mp4) < 1_000_000:
        problems.append(f"render under 1MB — almost certainly a failed encode: {mp4}")
    timing_path = os.path.join(studio_dir(slug, cut), "assets", "voice", "timing.json")
    if os.path.exists(timing_path):
        total = json.load(open(timing_path, encoding="utf-8")).get("total", 0)
        real = ffprobe_duration(mp4)
        if abs(real - total) > 1.0:
            problems.append(f"render runs {real:.1f}s, timing.json total is {total:.1f}s")
    # The master is not the upload. ElevenLabs returns clips near -24 LUFS and
    # nothing stages gain, so an un-normalised master ships 7-8 dB under the feed
    # — YouTube attenuates loud uploads but never lifts quiet ones. PUBLISH is the
    # master run through tools/loudnorm.py; it is the file that gets uploaded.
    pub = os.path.join(studio_dir(slug, cut), "renders", f"PUBLISH-1080p-{cut}.mp4")
    if not os.path.exists(pub):
        problems.append(f"missing {os.path.basename(pub)} — run: tools/loudnorm.py {mp4}")
    return problems


def check_package(slug, cut, fmt):
    problems = []
    meta = os.path.join(vault_dir(slug), f"youtube-metadata-{cut}.md")
    if not os.path.exists(meta):
        problems.append(f"missing publish pack: {meta}")
    thumbs = glob.glob(os.path.join(ROOT, "studio", "videos", f"{slug}-thumbs",
                                    f"thumbnail-{cut}*.png"))
    if len(thumbs) < 1:
        problems.append(f"expected at least 1 thumbnail for -{cut}, found {len(thumbs)}")

    # Captions ship with every video (creator rule 2026-08-06). Both halves are
    # asserted: the .srt is the upload and the narration .md is the readable
    # record, and `tools/transcript.py` writes them together — one present without
    # the other means someone hand-made a file instead of running the tool.
    srt = os.path.join(studio_dir(slug, cut), "renders", f"captions-{cut}.srt")
    if not os.path.exists(srt):
        problems.append(f"missing captions: {srt} — run: "
                        f"python3 tools/transcript.py {slug} --cut {cut}")
    narration = os.path.join(vault_dir(slug), f"narration-{cut}.md")
    if not os.path.exists(narration):
        problems.append(f"missing narration file: {narration} — run: "
                        f"python3 tools/transcript.py {slug} --cut {cut}")
    return problems


CHECKS = {
    "research": check_research, "facts": check_facts, "script": check_script,
    "audit": check_audit, "voice": check_voice, "storyboard": check_storyboard,
    "assets": check_assets, "build": check_build, "render": check_render,
    "package": check_package,
}
PER_CUT = set(CHECKS) - {"research", "facts"}


# -------------------------------------------------------------- architecture

def recent_architectures(limit=8):
    """Architectures of the most recent runs, newest first."""
    runs = []
    for path in glob.glob(os.path.join(ROOT, "vault", "videos", "*", "run.json")):
        try:
            name = json.load(open(path, encoding="utf-8")).get("architecture")
        except (ValueError, OSError):
            continue
        if name:
            runs.append((os.path.getmtime(path), name))
    return [name for _, name in sorted(runs, reverse=True)][:limit]


def architecture_lock_problems(fmt):
    """A lock that names nothing real would silently degrade to rotation — i.e.
    quietly ship the layout the creator did NOT pick. Surfaced by `doctor`, so a
    typo costs five seconds at preflight instead of a whole run."""
    problems = []
    lock = fmt.get("architecture_lock")
    arches = fmt.get("architectures", {})
    if lock and lock not in arches:
        problems.append(f"architecture_lock '{lock}' is not in format.json "
                        f"`architectures` — fix the name or delete the lock")
    # HARD creator rule, 2026-07-30: "images are compulsury". Most of the
    # thirteen candidate styles were rejected for rendering type on flat colour.
    # Requiring the flag here means a new style CANNOT be added that quietly
    # drops the photograph — the wrong state is unrepresentable rather than
    # merely discouraged.
    for name, spec in arches.items():
        if spec.get("image_per_scene") is not True:
            problems.append(
                f"architecture '{name}' does not declare image_per_scene: true — "
                f"every frame must carry a photograph (creator rule 2026-07-30)")
    return problems


def next_architecture(fmt=None):
    """The architecture the NEXT run should use: the least recently used one,
    unless format.json pins one with `architecture_lock`.

    Six consecutive blockframe-9 cuts shipped on both channels. The warning had
    been written four times — three milestone notes and a structured `owed` entry
    in run.json — and no code read any of them. A note cannot change what the
    next run does; the DEFAULT can. So the rotation lives here, the orchestrator
    writes the answer into run.json before fin-script, and varying costs nobody
    a decision. Add an entry to format.json `architectures` to widen the cycle.

    The lock is the same principle pointed the other way: once the creator has
    actually chosen a layout, rotating away from it is the pipeline overriding a
    decision. `doctor` rejects a lock naming an unknown architecture, so a typo
    fails at preflight instead of quietly falling through to rotation.
    """
    fmt = fmt or load_format()
    names = list(fmt.get("architectures", {}))
    if not names:
        return None
    if fmt.get("architecture_lock") in names:
        return fmt["architecture_lock"]
    recent = recent_architectures(len(names))
    unused = [n for n in names if n not in recent]
    if unused:
        return unused[0]
    return max(names, key=recent.index)   # the one used longest ago


# --------------------------------------------------------------------- doctor

def doctor(tier):
    """X-11: fail in five seconds with the fix command, not at minute 95."""
    import shutil
    fmt = load_format()
    problems = []
    for exe in ("ffmpeg", "ffprobe", "node"):
        if not shutil.which(exe):
            problems.append(f"{exe} not on PATH")
    env = {}
    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        for line in open(env_path, encoding="utf-8"):
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"').strip("'")
    for key in ("ELEVENLABS_API_KEY", "PIXABAY_API_KEY", "PEXELS_API_KEY"):
        if not (os.environ.get(key) or env.get(key)):
            problems.append(f"{key} missing — add it to .env")
    whisper = subprocess.run(
        [os.path.join(ROOT, "venv", "bin", "python"), "-c", "import faster_whisper"],
        capture_output=True)
    if whisper.returncode != 0:
        problems.append("faster-whisper not importable in venv — "
                        "fix: venv/bin/pip install faster-whisper")
    problems += architecture_lock_problems(fmt)
    need_gb = 2 * fmt["tiers"][tier]["disk_gb_per_pair"]  # R-9: 2× headroom
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < need_gb:
        problems.append(f"only {free_gb:.1f} GB free, tier '{tier}' needs "
                        f"{need_gb:.1f} GB headroom — run post-delivery cleanup first")
    return problems


# ------------------------------------------------------------------- run.json

def mark(stage, slug, cut, problems, attempt, log, rescue=False):
    """Record the checked result in run.json — {status, reason, log, at} per DX X-3,
    retry counter as its own field. Atomic; the only writer of `done`.
    rescue=True records `rescued` (a documented no-artifact rescue path, e.g.
    research's EmptyStudyPacket) — terminal like done, so --resume skips it."""
    path = os.path.join(vault_dir(slug), "run.json")
    run = {}
    if os.path.exists(path):
        run = json.load(open(path, encoding="utf-8"))
    key = f"fin-{stage}" + (f"-{cut}" if stage in PER_CUT else "")
    entry = {
        "status": "rescued" if rescue else ("done" if not problems else "failed"),
        "reason": "" if not problems else "; ".join(problems)[:500],
        "attempt": attempt,
        "log": log or "",
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    if stage == "voice" and not problems:
        # X-8: freeze the script the clips were generated from, so any later
        # edit invalidates every downstream stage
        entry["script_sha256"] = script_hash(slug, cut)
    run.setdefault("stages", {})[key] = entry
    os.makedirs(vault_dir(slug), exist_ok=True)
    atomic_write_json(path, run)


# ------------------------------------------------------------------- selftest

def _selftest():
    import tempfile, shutil
    fmt = load_format()
    tmp = tempfile.mkdtemp(prefix="pipecheck-")
    global ROOT
    real_root = ROOT
    try:
        ROOT = tmp
        slug, cut = "selftest-topic", "hi"
        vdir = os.path.join(studio_dir(slug, cut), "assets", "voice")
        os.makedirs(vdir)

        # voice fixtures: two audible clips whose length matches chars/rate
        rate = fmt["cuts"][cut]["chars_per_second"]
        lead, tail = scene_padding(fmt, slug)
        lines, tlines, start = [], [], 0.0
        for i, dur in enumerate((3.0, 4.0), 1):
            lid = f"h{i}"
            subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-f", "lavfi",
                 "-i", "sine=frequency=440:sample_rate=44100",
                 "-t", str(dur), "-q:a", "2", os.path.join(vdir, f"{lid}.mp3")],
                check=True)
            real = ffprobe_duration(os.path.join(vdir, f"{lid}.mp3"))
            lines.append({"id": lid, "text": "x" * int(real * rate)})
            tlines.append({"id": lid, "chars": int(real * rate), "duration": round(real, 3),
                           "scene_start": round(start, 3),
                           "scene_duration": round(lead + real + tail, 3),
                           "audio_start": round(start + lead, 3)})
            start += lead + real + tail
        atomic_write_json(os.path.join(vdir, "lines.json"), lines)
        atomic_write_json(os.path.join(vdir, "timing.json"),
                          {"lines": tlines, "total": round(start, 3)})
        assert check_voice(slug, cut, fmt) == [], check_voice(slug, cut, fmt)

        # R-3: a hand-fabricated duration must fail the ffprobe cross-check
        bad = json.load(open(os.path.join(vdir, "timing.json"), encoding="utf-8"))
        bad["lines"][0]["duration"] += 1.0
        atomic_write_json(os.path.join(vdir, "timing.json"), bad)
        assert any("ffprobe says" in p for p in check_voice(slug, cut, fmt))
        atomic_write_json(os.path.join(vdir, "timing.json"),
                          {"lines": tlines, "total": round(start, 3)})

        # SilentClip: a silent mp3 must fail
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=44100",
             "-t", "3.0", "-q:a", "2", os.path.join(vdir, "h1.mp3")], check=True)
        assert any("silent" in p for p in check_voice(slug, cut, fmt))

        # currency purity: ₹ in an -en script must fail
        os.makedirs(vault_dir(slug))
        with open(os.path.join(vault_dir(slug), "script-en.md"), "w", encoding="utf-8") as fh:
            fh.write("x" * 600 + " costs ₹500 ")
        assert any("currency purity" in p for p in check_script(slug, "en", fmt))

        # mark: failed check must never write done; passing one must
        mark("script", slug, "en", ["bad"], 1, "")
        run = json.load(open(os.path.join(vault_dir(slug), "run.json"), encoding="utf-8"))
        assert run["stages"]["fin-script-en"]["status"] == "failed"
        with open(os.path.join(vault_dir(slug), "script-hi.md"), "w", encoding="utf-8") as fh:
            fh.write("original script " + "x" * 600)
        mark("voice", slug, cut, [], 2, "logs/fin-voice-hi-2.md")
        run = json.load(open(os.path.join(vault_dir(slug), "run.json"), encoding="utf-8"))
        assert run["stages"]["fin-voice-hi"] == {**run["stages"]["fin-voice-hi"],
                                                "status": "done", "attempt": 2}
        assert run["stages"]["fin-voice-hi"]["script_sha256"]

        # transitions: a scene must be held `transition_seconds` past its own end,
        # or the incoming cross-dissolve fades up from black instead of from the
        # previous frame — and every other check still passes.
        T = fmt["scene"]["transition_seconds"]
        sdir, total = studio_dir(slug, cut), round(start, 3)

        def write_html(first_duration, tracks=(1, 2), extra=""):
            open(os.path.join(sdir, "index.html"), "w", encoding="utf-8").write(
                extra +
                f'<div id="root" class="cut-{cut}" data-composition-id="main" data-duration="{total}">'
                f'<section data-start="{tlines[0]["scene_start"]}" data-duration="{first_duration}"'
                f' data-track-index="{tracks[0]}"></section>'
                f'<section data-start="{tlines[1]["scene_start"]}" data-duration="{tlines[1]["scene_duration"]}"'
                f' data-track-index="{tracks[1]}"></section>'
                f'</div>')

        write_html(round(tlines[0]["scene_duration"] + T, 3))
        assert check_build(slug, cut, fmt) == [], check_build(slug, cut, fmt)
        write_html(tlines[0]["scene_duration"])   # the pre-2026-07-29 hard-cut build
        assert any("overlaps" in p for p in check_build(slug, cut, fmt))
        # overlapping scenes on ONE track is what `hyperframes check` rejects
        write_html(round(tlines[0]["scene_duration"] + T, 3), tracks=(1, 1))
        assert any("same_track" in p or "both on data-track-index" in p
                   for p in check_build(slug, cut, fmt)), check_build(slug, cut, fmt)

        # Lottie: each trap renders a blank scene that passes every other check.
        good = round(tlines[0]["scene_duration"] + T, 3)
        ok = '<script src="assets/js/lottie.min.js"></script><script>loadLottie("#a", L_x);</script>'
        write_html(good, extra=ok)
        assert check_build(slug, cut, fmt) == [], check_build(slug, cut, fmt)
        for bad, want in [
                ('<script>window.__hfLottie = [a];</script>', "__hfLottie"),
                ('<script>lottie.loadAnimation({});</script>', "loadAnimation"),
                ('<script>loadLottie("#a", {path: "assets/x.json"});</script>', "path:"),
                ('<script>' + 'loadLottie("#a", L_x);' * 9 + '</script>', "max")]:
            write_html(good, extra='<script src="assets/js/lottie.min.js"></script>' + bad)
            assert any(want in p for p in check_build(slug, cut, fmt)), (want, check_build(slug, cut, fmt))
        # …and none of it fires for a cut that never loads lottie at all
        write_html(good, extra='<script>window.__hfLottie = [a];</script>')
        assert check_build(slug, cut, fmt) == [], check_build(slug, cut, fmt)

        # data-framings: a panel swap is measured per framing, not per section.
        # An over-long scene fails; the same scene split into real framings passes;
        # framings that do not add up to the scene, or that are individually still
        # too long, both fail — so the attribute cannot be used to duck the guard.
        max_hold = fmt.get("scene", {}).get("max_scene_seconds", 0)
        long_own = max_hold + 1.0                      # 1s past the limit
        def write_framed(framings_attr=""):
            open(os.path.join(sdir, "index.html"), "w", encoding="utf-8").write(
                f'<div id="root" class="cut-{cut}" data-composition-id="main" data-duration="{total}">'
                f'<section data-start="{tlines[0]["scene_start"]}"'
                f' data-duration="{round(long_own + T, 3)}"'
                f' data-track-index="{tracks_default[0]}"{framings_attr}></section>'
                f'<section data-start="{tlines[1]["scene_start"]}"'
                f' data-duration="{tlines[1]["scene_duration"]}"'
                f' data-track-index="{tracks_default[1]}"></section>'
                f'</div>')
        tracks_default = (0, 1)
        half = round(long_own / 2, 3)
        write_framed()
        assert any("dead frame" in p for p in check_build(slug, cut, fmt))
        write_framed(f' data-framings="{half},{round(long_own - half, 3)}"')
        assert not any("dead frame" in p or "framing" in p
                       for p in check_build(slug, cut, fmt)), check_build(slug, cut, fmt)
        write_framed(' data-framings="0.5,0.5"')       # cosmetic, does not partition
        assert any("partition" in p for p in check_build(slug, cut, fmt))
        write_framed(f' data-framings="{round(long_own - 0.5, 3)},0.5"')   # still too long
        assert any("longest framing" in p for p in check_build(slug, cut, fmt))

        # rotation: the next run must not repeat the architecture just used
        assert next_architecture() in load_format()["architectures"]

        # the lock beats the rotation, and a lock naming nothing real fails
        # preflight instead of falling through to rotation (which would ship a
        # layout the creator did not choose). Pure — FORMAT_PATH is absolute, so
        # writing a fixture here would edit the real repo config.
        names = list(fmt["architectures"])
        assert len(names) > 1, "need ≥2 architectures to prove the lock beats rotation"
        for pinned in names:
            locked = dict(fmt, architecture_lock=pinned)
            assert next_architecture(locked) == pinned, f"lock '{pinned}' lost to rotation"
            assert architecture_lock_problems(locked) == []
        bogus = dict(fmt, architecture_lock="no-such-layout")
        assert architecture_lock_problems(bogus), "unknown lock must fail doctor"
        assert next_architecture(bogus) in names, "bogus lock must not return itself"
        assert next_architecture(dict(fmt, architecture_lock=None)) in names

        # X-8: editing the script after voice ran must invalidate downstream stages
        assert stale_script_problems(slug, cut) == []
        with open(os.path.join(vault_dir(slug), "script-hi.md"), "a", encoding="utf-8") as fh:
            fh.write("\naudit rewrote this line")
        assert any("stale" in p for p in stale_script_problems(slug, cut))
        print("selftest OK")
    finally:
        ROOT = real_root
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="finance-pipeline stage postconditions")
    p.add_argument("mode", nargs="?", choices=["check", "mark", "doctor", "architecture"])
    p.add_argument("stage", nargs="?", choices=sorted(CHECKS))
    p.add_argument("--tier", default="short", choices=["short", "medium", "long"])
    p.add_argument("--slug")
    p.add_argument("--cut", choices=["hi", "en"])
    p.add_argument("--attempt", type=int, default=1)
    p.add_argument("--chapter", type=int,
                   help="chapter-loop mode: check the standalone chapter project "
                        "<slug>-<cut>-ch<N>/assets-ch<N>/final/ instead of the whole cut")
    p.add_argument("--log", help="path to this attempt's log file, recorded in run.json")
    p.add_argument("--rescue", action="store_true",
                   help="record a documented rescue (stage continues without its artifact)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)

    if args.selftest:
        _selftest()
        return 0
    if args.mode == "architecture":
        name = next_architecture()
        if not name:
            print("no architectures defined in tools/format.json")
            return 1
        fmt = load_format()
        arch = fmt["architectures"][name]
        print(name)
        if fmt.get("architecture_lock") == name:
            print("  LOCKED — rotation is off (creator decision 2026-07-30). "
                  "Delete `architecture_lock` in tools/format.json to resume rotating.")
        print(f"  body_class: {arch.get('body_class') or '(none — the default centred stack)'}")
        print(f"  {arch.get('summary', '')}")
        print(f"  spec: {arch.get('reference', '')}")
        print(f"  recent runs (newest first): {', '.join(recent_architectures()) or '(none)'}")
        return 0
    if args.mode == "doctor":
        problems = doctor(args.tier)
        for pr in problems:
            print(f"  ✗ {pr}")
        print("FAIL doctor" if problems else "PASS doctor")
        return 1 if problems else 0
    if not (args.mode and args.stage and args.slug):
        p.error("need: <check|mark> <stage> --slug <slug> [--cut hi|en]")
    if args.stage in PER_CUT and not args.cut:
        p.error(f"stage '{args.stage}' needs --cut")
    if args.chapter:
        if args.stage != "assets":
            p.error("--chapter is only implemented for 'assets'; the other chapter "
                    "artifacts are verified by `hyperframes check` and the draft render")
        globals()["CHAPTER"] = args.chapter

    problems = CHECKS[args.stage](args.slug, args.cut, load_format())
    if args.mode == "mark":
        mark(args.stage, args.slug, args.cut, problems, args.attempt, args.log,
             rescue=args.rescue)
        if args.rescue:
            print(f"RESCUED {args.stage}: " + ("; ".join(problems) or "no artifact"))
            return 0
    if problems:
        print(f"FAIL {args.stage}" + (f"-{args.cut}" if args.cut else ""))
        for pr in problems:
            print(f"  ✗ {pr}")
        return 1
    print(f"PASS {args.stage}" + (f"-{args.cut}" if args.cut else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
