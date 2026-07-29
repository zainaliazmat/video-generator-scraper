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


def check_voice(slug, cut, fmt):
    return check_voice_dir(os.path.join(studio_dir(slug, cut), "assets", "voice"), cut, fmt)


def check_voice_dir(vdir, cut, fmt):
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
    lead, tail = fmt["scene"]["lead_in_seconds"], fmt["scene"]["tail_seconds"]
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
        expected = len(text) / rate
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


def check_assets(slug, cut, fmt):
    idir = os.path.join(studio_dir(slug, cut), "assets", "img")
    manifest_path = os.path.join(idir, "manifest.json")
    if not os.path.exists(manifest_path):
        return [f"missing manifest: {manifest_path}"]
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    problems = []
    credits = ""
    credits_path = os.path.join(idir, "CREDITS.txt")
    if os.path.exists(credits_path):
        credits = open(credits_path, encoding="utf-8").read()
    for name in manifest:
        path = os.path.join(idir, name)
        if not os.path.exists(path):
            problems.append(f"manifest names {name} but it is not on disk "
                            "(dropped cut-ins must be removed from the manifest)")
        elif os.path.getsize(path) < 10240:
            problems.append(f"{name}: under 10KB, not a usable photo")
        elif name not in credits:
            problems.append(f"{name}: no attribution line in CREDITS.txt (licence requirement)")
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
    root = re.search(r'data-composition-id="main"[^>]*data-duration="([\d.]+)"', html)
    scenes = re.findall(r'<section[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)
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
    return problems


CHECKS = {
    "research": check_research, "facts": check_facts, "script": check_script,
    "audit": check_audit, "voice": check_voice, "storyboard": check_storyboard,
    "assets": check_assets, "build": check_build, "render": check_render,
    "package": check_package,
}
PER_CUT = set(CHECKS) - {"research", "facts"}


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
        lead, tail = fmt["scene"]["lead_in_seconds"], fmt["scene"]["tail_seconds"]
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
    p.add_argument("mode", nargs="?", choices=["check", "mark", "doctor"])
    p.add_argument("stage", nargs="?", choices=sorted(CHECKS))
    p.add_argument("--tier", default="short", choices=["short", "medium", "long"])
    p.add_argument("--slug")
    p.add_argument("--cut", choices=["hi", "en"])
    p.add_argument("--attempt", type=int, default=1)
    p.add_argument("--log", help="path to this attempt's log file, recorded in run.json")
    p.add_argument("--rescue", action="store_true",
                   help="record a documented rescue (stage continues without its artifact)")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)

    if args.selftest:
        _selftest()
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
