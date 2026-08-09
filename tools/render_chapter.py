#!/usr/bin/env python3
"""Draft-render one chapter and build its contact sheet.

    python3 tools/render_chapter.py <slug> --cut hi --chapter 3
    python3 tools/render_chapter.py <slug> --cut hi --chapter 3 --check   # gate first
    python3 tools/render_chapter.py --selftest

Replaces `fin-render --chapter N` (its §0). That stage was an agent wrapping two
commands with no decision between them: it cost 318,807 tokens per invocation across
21 invocations on `passive-income-number` (audit/05-baseline.md) to run

    npx hyperframes render . -c index.html -o renders/DRAFT-ch<N>.mp4 -q draft -f <fps>
    python3 tools/chapter_sheet.py <project> <mp4> -o <project>/renders/SHEET-ch<N>.jpg

`fin-render`'s other steps are NOT here and the agent is not deleted yet: its gate-two
frame check is a vision pass that moves to `fin-review` (migration step 8), and its
master QA is numeric and moves into `pipeline_check check render`. This file owns only
the part that was never judgement.

WHY THE FLAGS ARE FIXED
-----------------------
`-q draft` only, and `-f` at the FINAL fps. Both are load-bearing and neither is a
knob (finance-video.md:294-300):

  * A draft rendered at a different fps produces frame counts that do not sum, and the
    chapters drift at every joint. `-f` is read from the composition's `data-fps`,
    defaulting to 30, so it can never disagree with what the final render will use.
  * `--resolution` / `--gpu` / chunked encode are deliberately absent. A draft exists to
    judge images, motion and timing, all of which are identical at draft quality.
"""

import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FPS = 30


def project_dir(slug, cut, chapter):
    return os.path.join(ROOT, "studio", "videos", f"{slug}-{cut}-ch{chapter}")


def composition_fps(html_path):
    """The composition's own data-fps, else 30.

    Read rather than passed, so the draft cannot be rendered at an fps the final render
    will not use — the failure that makes chapters fail to concatenate frame-exact."""
    try:
        with open(html_path, encoding="utf-8", errors="replace") as fh:
            head = fh.read(20000)
    except OSError:
        return DEFAULT_FPS
    m = re.search(r'data-fps="(\d+(?:\.\d+)?)"', head)
    return int(float(m.group(1))) if m else DEFAULT_FPS


def _run(cmd, cwd, what, timeout):
    print(f"$ {' '.join(cmd)}", flush=True)
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        sys.exit(f"ERROR: {what} failed (exit {r.returncode}) — nothing was marked done")
    return r


def probe(mp4):
    """(seconds, frames) from the encoded file, or (None, None)."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=nb_read_packets,duration",
             "-count_packets", "-of", "json", mp4],
            capture_output=True, timeout=120)
        s = json.loads(out.stdout.decode())["streams"][0]
        return float(s.get("duration") or 0), int(s.get("nb_read_packets") or 0)
    except (OSError, ValueError, KeyError, IndexError, subprocess.SubprocessError):
        return None, None


def render_chapter(slug, cut, chapter, run_check=False, timeout=3600):
    proj = project_dir(slug, cut, chapter)
    html = os.path.join(proj, "index.html")
    if not os.path.isdir(proj):
        sys.exit(f"ERROR: no chapter project at {os.path.relpath(proj, ROOT)}")
    if not os.path.exists(html):
        sys.exit(f"ERROR: no index.html in {os.path.relpath(proj, ROOT)}")

    # The composition must be newer than the generator, or this renders a stale file.
    # This is the defect that cost two drafts and an editor pass on hi ch3 (2026-08-09,
    # notes.md `method_learned.an_asset_swap_needs_a_REBUILD_not_only_a_re-render`):
    # the swap kept the same path, so nothing looked wrong.
    build = os.path.join(proj, "build.mjs")
    if os.path.exists(build) and os.path.getmtime(build) > os.path.getmtime(html):
        sys.exit(f"ERROR: build.mjs is newer than index.html — run `node build.mjs` in "
                 f"{os.path.relpath(proj, ROOT)} first, or you will render a stale composition")

    if run_check:
        _run(["npm", "run", "check"], proj, "hyperframes check", timeout)

    fps = composition_fps(html)
    out_rel = os.path.join("renders", f"DRAFT-ch{chapter}.mp4")
    os.makedirs(os.path.join(proj, "renders"), exist_ok=True)
    _run(["npx", "hyperframes", "render", ".", "-c", "index.html",
          "-o", out_rel, "-q", "draft", "-f", str(fps)], proj, "draft render", timeout)

    mp4 = os.path.join(proj, out_rel)
    if not os.path.exists(mp4) or os.path.getsize(mp4) < 100_000:
        sys.exit(f"ERROR: {out_rel} missing or under 100 KB — the render did not produce a file")

    sheet = os.path.join(proj, "renders", f"SHEET-ch{chapter}.jpg")
    _run([sys.executable, os.path.join(ROOT, "tools", "chapter_sheet.py"),
          proj, mp4, "-o", sheet], ROOT, "contact sheet", timeout)
    if not os.path.exists(sheet):
        sys.exit("ERROR: contact sheet was not written")

    secs, frames = probe(mp4)
    print(f"\nDRAFT  {os.path.relpath(mp4, ROOT)}")
    print(f"SHEET  {os.path.relpath(sheet, ROOT)}")
    print(f"fps={fps}  seconds={secs if secs is not None else '?'}  frames={frames or '?'}"
          f"  size={os.path.getsize(mp4) // 1024} KB")
    return {"draft": os.path.relpath(mp4, ROOT), "sheet": os.path.relpath(sheet, ROOT),
            "fps": fps, "seconds": secs, "frames": frames}


def selftest():
    import tempfile, shutil
    tmp = tempfile.mkdtemp()
    try:
        p = os.path.join(tmp, "index.html")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write('<div id="root" data-fps="24" data-duration="10">x</div>')
        assert composition_fps(p) == 24, composition_fps(p)

        with open(p, "w", encoding="utf-8") as fh:
            fh.write('<div id="root" data-duration="10">x</div>')
        assert composition_fps(p) == DEFAULT_FPS, "a composition with no data-fps must default to 30"

        assert composition_fps(os.path.join(tmp, "nope.html")) == DEFAULT_FPS

        # the stale-composition guard is the point of this file existing
        proj = os.path.join(tmp, "studio", "videos", "s-hi-ch1")
        os.makedirs(proj)
        for name in ("index.html", "build.mjs"):
            with open(os.path.join(proj, name), "w") as fh:
                fh.write("x")
        os.utime(os.path.join(proj, "index.html"), (1, 1))
        os.utime(os.path.join(proj, "build.mjs"), (2, 2))
        global ROOT
        keep, ROOT = ROOT, tmp
        try:
            render_chapter("s", "hi", 1)
        except SystemExit as e:
            assert "build.mjs is newer" in str(e), e
        else:
            raise AssertionError("stale composition was not caught")
        finally:
            ROOT = keep
        print("selftest ok")
    finally:
        shutil.rmtree(tmp)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--cut", choices=("hi", "en"))
    ap.add_argument("--chapter", type=int)
    ap.add_argument("--check", action="store_true", help="run `npm run check` first")
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not (a.slug and a.cut and a.chapter):
        ap.error("slug, --cut and --chapter are required")
    render_chapter(a.slug, a.cut, a.chapter, a.check, a.timeout)


if __name__ == "__main__":
    main()
