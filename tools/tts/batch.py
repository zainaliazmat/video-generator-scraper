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


def run(project, cut, voice=None, model=None, seed=None, force=False, only=None):
    fmt = pc.load_format()
    cutcfg = fmt["cuts"][cut]
    voice = voice or cutcfg["voice_id"]
    model = model or fmt["tts"]["model"]
    vdir = os.path.join(project, "assets", "voice")
    # studio/videos/<slug>-<cut> -> <slug>; lets scene_padding read the run's tier
    slug = os.path.basename(project.rstrip("/")).rsplit("-", 1)[0]
    lines = pc.load_lines(vdir)

    # .env FIRST, then read the flag. Setting FIN_FAKE_APIS in .env is the only way
    # to reach a subagent's Bash call (env does not persist between them), and this
    # used to compute `fake` before .env was parsed: the run stayed free only because
    # the not-fake branch called load_env(), which setdefault()-ed the flag in time
    # for synthesize() to re-check it. Reordering or removing that call turned a
    # rehearsal into a full-price run with no visible difference. Found by the
    # rehearsal of 2026-08-09, reported by fin-voice.
    tts.load_env()
    fake = os.environ.get("FIN_FAKE_APIS") == "1"
    key = "" if fake else tts.api_key()

    # --only: regenerate exactly these ids. A one-line re-voice is the NORMAL
    # outcome of a gate-one audit, and the skip guard is all-or-nothing at the cut
    # level, so without this the only routes are --force (every clip, every credit)
    # or an out-of-band `rm` that the voice stage's allowlist cannot perform.
    # (Blocked fin-voice-en on japanese-money-methods, 2026-08-01.)
    want = None
    if only:
        want = set(only)
        missing = want - {l["id"] for l in lines}
        if missing:
            sys.exit(f"ERROR: --only names ids not in lines.json: {sorted(missing)}")
        print(f"--only: regenerating {len(want)} clip(s): {sorted(want)}")

    # Which VOICE the clips on disk were read by. The <id>.txt sidecar records what
    # each mp3 says and nothing about who said it, so a voice change was invisible to
    # the resume: on passive-income-number-hi the voice moved Harsh -> Amrut while 17
    # style-E lines stayed byte-identical to their style-A take, and a bare resume
    # would have made 64 calls and shipped a cut with chapter 5 more than half in the
    # retired voice. Nothing downstream could catch it — check_voice_dir tests bytes,
    # duration, silence and scene arithmetic, and not one of those is a function of
    # timbre. So the voice is recorded here, and a mismatch makes every clip stale.
    # (2026-08-08. Recording it beats documenting it: the wrong state stops existing.)
    voice_stamp = os.path.join(vdir, ".voice")
    prev_voice = None
    if os.path.exists(voice_stamp):
        with open(voice_stamp, encoding="utf-8") as fh:
            prev_voice = fh.read().strip()
    voice_changed = prev_voice is not None and prev_voice != voice
    if voice_changed:
        print(f"VOICE CHANGED {prev_voice} -> {voice}: every existing clip is stale")
    elif prev_voice is None and any(
            os.path.exists(os.path.join(vdir, f"{l['id']}.mp3")) for l in lines):
        # Clips predating the stamp. Their voice is unknowable, and guessing costs
        # either a silently mixed-voice cut or a full re-spend — so say so and stop.
        sys.exit(
            f"ERROR: {vdir} holds clips but no .voice stamp, so the voice they were "
            f"read by cannot be established.\n"
            f"  If they are already {voice}: printf %s {voice} > {voice_stamp}\n"
            f"  If they are not, or you cannot tell: re-run with --force.")

    # NOTE: `only` scopes GENERATION, never the timing rebuild below. Filtering
    # `lines` itself would write a timing.json containing one entry and silently
    # drop the other 91 — caught by the selftest, 2026-08-01.
    for line in [l for l in lines if want is None or l["id"] in want]:
        out = os.path.join(vdir, f"{line['id']}.mp3")
        # "Already generated" means the mp3 exists AND was generated from the text
        # we are holding now. Existence alone is not enough: an audit rewriting one
        # line left the new text paired with the old audio SILENTLY, because
        # check_voice_dir re-derives the expected duration from the NEW chars at
        # ±35% — a tolerance a one-word edit sails straight through. The <id>.txt
        # sidecar is written immediately before each call, so it is an exact record
        # of what this mp3 actually says. (japanese-money-methods, 2026-08-01.)
        txt = os.path.join(vdir, f"{line['id']}.txt")
        stale = True
        if os.path.exists(txt):
            with open(txt, encoding="utf-8") as fh:
                stale = fh.read() != line["text"]
        if os.path.exists(out) and os.path.getsize(out) > 0 and not force and want is None:
            if not stale and not voice_changed:
                print(f"skip (exists): {out}")
                continue
            print(f"REGEN ({'voice' if voice_changed else 'text'} changed since last "
                  f"take): {line['id']}")
        with open(os.path.join(vdir, f"{line['id']}.txt"), "w", encoding="utf-8") as fh:
            fh.write(line["text"])
        print(f"=== {line['id']} ({len(line['text'])} chars) ===")
        tts.synthesize(key, voice, line["text"], out, model,
                       stability=0.5, similarity=0.75,
                       style=fmt["tts"]["style"], seed=seed)

    # Stamped only after the loop: a run that dies halfway must not leave a stamp
    # claiming a voice the surviving clips do not all share. --only is exempt for
    # the same reason — it deliberately regenerates a subset.
    if want is None:
        with open(voice_stamp, "w", encoding="utf-8") as fh:
            fh.write(voice)

    # tier-aware: this padding is charged per line, so SHORT's value overpays at
    # MEDIUM/LONG line counts. pipeline_check.scene_padding is the same rule.
    lead, tail = pc.scene_padding(fmt, slug)
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

    problems = pc.check_voice_dir(vdir, cut, fmt, slug)
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
        mtime2 = os.path.getmtime(os.path.join(vdir, "h2.mp3"))
        assert run(tmp, "hi") == 0
        assert os.path.getmtime(os.path.join(vdir, "h1.mp3")) == mtime, "clip was regenerated"
        # …but an EDITED line must regenerate, or the new text ships against the old
        # audio and every downstream check still passes. This is the audit-rewrites-
        # one-line case, which is the normal outcome of gate one.
        lines[0]["text"] = "z" * 41
        pc.atomic_write_json(os.path.join(vdir, "lines.json"), lines)
        assert run(tmp, "hi") == 0
        assert os.path.getmtime(os.path.join(vdir, "h1.mp3")) != mtime, \
            "edited line was NOT regenerated — new text is paired with old audio"
        assert open(os.path.join(vdir, "h1.txt"), encoding="utf-8").read() == "z" * 41
        assert os.path.getmtime(os.path.join(vdir, "h2.mp3")) == mtime2, \
            "an untouched line was regenerated"
        # --only regenerates just what it names, and rejects an unknown id
        m1 = os.path.getmtime(os.path.join(vdir, "h1.mp3"))
        assert run(tmp, "hi", only=["h2"]) == 0
        assert os.path.getmtime(os.path.join(vdir, "h1.mp3")) == m1, "--only touched another clip"
        assert os.path.getmtime(os.path.join(vdir, "h2.mp3")) != mtime2, "--only skipped its target"
        try:
            run(tmp, "hi", only=["nope"])
            raise AssertionError("--only accepted an id not in lines.json")
        except SystemExit:
            pass
        # A VOICE change regenerates every clip, including ones whose text did not
        # move. Text-only staleness cannot see this: on passive-income-number-hi 17
        # lines were byte-identical across the restyle, so a bare resume would have
        # shipped them in the retired voice with every downstream check green.
        assert open(os.path.join(vdir, ".voice"), encoding="utf-8").read() \
            == pc.load_format()["cuts"]["hi"]["voice_id"]
        before = {i: os.path.getmtime(os.path.join(vdir, f"{i}.mp3")) for i in ("h1", "h2")}
        assert run(tmp, "hi", voice="SOME_OTHER_VOICE_ID") == 0
        for i in ("h1", "h2"):
            assert os.path.getmtime(os.path.join(vdir, f"{i}.mp3")) != before[i], \
                f"{i} kept its old-voice audio after the voice changed"
        assert open(os.path.join(vdir, ".voice"), encoding="utf-8").read() == "SOME_OTHER_VOICE_ID"
        # …and clips with no stamp at all stop the run rather than guess.
        os.remove(os.path.join(vdir, ".voice"))
        try:
            run(tmp, "hi")
            raise AssertionError("unstamped clips were resumed on an unknown voice")
        except SystemExit:
            pass
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
    p.add_argument("--only", nargs="+", metavar="ID",
                   help="regenerate ONLY these line ids (e.g. --only 7.4); ignores the exists-skip "
                        "for them and leaves every other clip untouched")
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if not (args.project and args.cut):
        p.error("need --project and --cut")
    return run(args.project, args.cut, args.voice, args.model, args.seed, args.force,
               args.only)


if __name__ == "__main__":
    sys.exit(main())
