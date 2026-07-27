#!/usr/bin/env python3
"""Batch TTS + measured timing for one cut — the thin script fin-voice invokes.

Reads assets/voice/lines.json (ordered [{"id","text"}], legacy {"h1": …} also
accepted), generates one clip per line via elevenlabs_tts.py (skip-if-exists, so
the resume unit is the clip, not the stage), ffprobes every clip, and writes
assets/voice/timing.json atomically. Durations are MEASURED, never estimated —
this file is the single source the composition's four timing copies derive from.

  python3 tools/tts/batch.py --project studio/videos/<slug>-hi --cut hi
  FIN_FAKE_APIS=1 python3 tools/tts/batch.py --project … --cut hi   # zero-cost

Exit codes: 0 ok · 1 postcondition failed · 2 terminal API error · 3 retryable.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, HERE)
import pipeline_check as pc  # noqa: E402
import elevenlabs_tts as tts  # noqa: E402


def run(project, cut, voice=None, model=None, seed=None, force=False):
    fmt = pc.load_format()
    cutcfg = fmt["cuts"][cut]
    voice = voice or cutcfg["voice_id"]
    model = model or fmt["tts"]["model"]
    vdir = os.path.join(project, "assets", "voice")
    lines = pc.load_lines(vdir)

    fake = os.environ.get("FIN_FAKE_APIS") == "1"
    key = ""
    if not fake:
        tts.load_env()
        key = tts.api_key()

    for line in lines:
        out = os.path.join(vdir, f"{line['id']}.mp3")
        if os.path.exists(out) and os.path.getsize(out) > 0 and not force:
            print(f"skip (exists): {out}")
            continue
        with open(os.path.join(vdir, f"{line['id']}.txt"), "w", encoding="utf-8") as fh:
            fh.write(line["text"])
        print(f"=== {line['id']} ({len(line['text'])} chars) ===")
        tts.synthesize(key, voice, line["text"], out, model,
                       stability=0.5, similarity=0.75,
                       style=fmt["tts"]["style"], seed=seed)

    lead = fmt["scene"]["lead_in_seconds"]
    tail = fmt["scene"]["tail_seconds"]
    entries, start = [], 0.0
    for line in lines:
        dur = pc.ffprobe_duration(os.path.join(vdir, f"{line['id']}.mp3"))
        scene = lead + dur + tail
        entries.append({"id": line["id"], "chars": len(line["text"]),
                        "duration": round(dur, 3),
                        "scene_start": round(start, 3),
                        "scene_duration": round(scene, 3),
                        "audio_start": round(start + lead, 3)})
        start += scene
    pc.atomic_write_json(os.path.join(vdir, "timing.json"),
                         {"generated_by": "tools/tts/batch.py",
                          "cut": cut, "voice_id": voice, "model": model,
                          "lines": entries, "total": round(start, 3)})
    print(f"timing.json: {len(entries)} lines, total {start:.2f}s")

    problems = pc.check_voice_dir(vdir, cut, fmt)
    for p in problems:
        print(f"  ✗ {p}")
    return 1 if problems else 0


def _selftest():
    import json, shutil, tempfile
    os.environ["FIN_FAKE_APIS"] = "1"
    tmp = tempfile.mkdtemp(prefix="ttsbatch-")
    try:
        vdir = os.path.join(tmp, "assets", "voice")
        os.makedirs(vdir)
        lines = [{"id": "h1", "text": "x" * 40}, {"id": "h2", "text": "y" * 80}]
        pc.atomic_write_json(os.path.join(vdir, "lines.json"), lines)
        assert run(tmp, "hi") == 0
        timing = json.load(open(os.path.join(vdir, "timing.json"), encoding="utf-8"))
        assert len(timing["lines"]) == 2 and timing["total"] > 0
        # resume: a second run must not regenerate anything
        mtime = os.path.getmtime(os.path.join(vdir, "h1.mp3"))
        assert run(tmp, "hi") == 0
        assert os.path.getmtime(os.path.join(vdir, "h1.mp3")) == mtime, "clip was regenerated"
        print("selftest OK")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="batch TTS + timing.json for one cut")
    p.add_argument("--project", help="studio/videos/<slug>-<cut> directory")
    p.add_argument("--cut", choices=["hi", "en"])
    p.add_argument("--voice", help="override format.json voice id")
    p.add_argument("--model", help="override format.json model")
    p.add_argument("--seed", type=int, help="fixed seed for reproducible takes")
    p.add_argument("--force", action="store_true", help="regenerate clips that already exist")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if not (args.project and args.cut):
        p.error("need --project and --cut")
    return run(args.project, args.cut, args.voice, args.model, args.seed, args.force)


if __name__ == "__main__":
    sys.exit(main())
