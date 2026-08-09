#!/usr/bin/env python3
"""Voice one cut: slice the script into lines.json, guard the spend, run batch.py.

    python3 tools/tts/prepare.py <slug> --cut hi
    python3 tools/tts/prepare.py <slug> --cut hi --only 1.1 1.2   # the sample pair
    python3 tools/tts/prepare.py <slug> --cut hi --dry-run        # guard + slice only
    python3 tools/tts/prepare.py --selftest

Replaces the `fin-voice` agent (audit/01-capability-matrix.md §5). All four of its
responsibilities were deterministic — slice the lines, refuse to overspend, run one
command, write a three-line shell script — and it cost 318,929 tokens per invocation
across 5 invocations on `passive-income-number` (audit/05-baseline.md) to do them.

WHAT IS NOT HERE, DELIBERATELY
------------------------------
Retries. `batch.py` exit 3 means retryable and exit 2 means a dead key; this file
passes the code straight out. One owner retries and it is the orchestrator
(finance-video.md §3) — an agent that retried its own TTS call is how a run doubles
its bill without anyone deciding to.
"""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import pipeline_check as pc  # noqa: E402


def slice_lines(slug, cut):
    """The VO lines, sliced from the script exactly — never retyped.

    `fin-voice.md:40-43` said "slice the source text exactly; never retype it" to an
    agent that could do neither reliably nor cheaply. The parser is
    `tools/transcript.py`'s, which already reads the same `**N.M**` / `> line`
    convention to build captions, so the ids in lines.json and the ids in the .srt
    cannot disagree about what line 3.2 is."""
    path = os.path.join(pc.vault_dir(slug), f"script-{cut}.md")
    if not os.path.exists(path):
        sys.exit(f"ERROR: missing script: {path}")
    lines = [{"id": lid, "text": text} for lid, _, text in pc.read_vo_lines(path)]
    if not lines:
        sys.exit(f"ERROR: no VO lines found in {path} — expected `**N.M**` "
                 f"followed by a `> ` quoted line")
    return lines


def write_gen_vo(project, slug, cut):
    """The three-line regeneration script, for a human re-running this by hand.

    No `cd`. The archived copies hardcode an absolute cd into a studio directory
    that `archive_cut.py` has since deleted, which `vault/CLAUDE.md` lists as one of
    the two gotchas a re-render hits."""
    path = os.path.join(project, f"gen_vo_{cut}.sh")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("#!/usr/bin/env bash\n"
                 "set -euo pipefail\n"
                 "# run from the repo root\n"
                 f"python3 tools/tts/batch.py --project studio/videos/{slug}-{cut} "
                 f"--cut {cut}\n")
    os.chmod(path, 0o755)
    return path


def write_log(slug, cut, attempt, ran, failed, evidence):
    """The stage log, in the five headings every stage writes.

    `mark` treats a missing log as a failed stage whatever the artifacts look like
    (`stale_log`), and the log is what a resume and an audit read. The agent used to
    write it; the script writes it, from measured numbers rather than from memory."""
    path = os.path.join(pc.vault_dir(slug), "logs", f"fin-voice-{cut}-{attempt}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# fin-voice-{cut} attempt {attempt} — tools/tts/prepare.py\n\n"
                 f"## Ran\n{ran}\n\n## Failed\n{failed or 'nothing'}\n\n"
                 f"## Evidence\n{evidence}\n\n"
                 f"## Changed\n{'nothing — refused before spending' if failed else ''}"
                 f"{'' if failed else 'lines.json, timing.json, the clips, gen_vo_' + cut + '.sh'}\n\n"
                 f"## Owed\nnothing\n")
    return path


def prepare(slug, cut, only=None, dry_run=False, force=False, attempt=1):
    fmt = pc.load_format()
    project = pc.studio_dir(slug, cut)
    vdir = os.path.join(project, "assets", "voice")

    # Guard BEFORE the slice writes anything: a refusal must leave no artifact that
    # a later resume could mistake for a prepared stage.
    problems = pc.voice_cost_guard(slug, cut, fmt)
    if problems:
        for p in problems:
            print(f"  ✗ {p}")
        print(f"FAIL voice-{cut} — refused before spending")
        write_log(slug, cut, attempt, "the cost guard only", "; ".join(problems),
                  "no ElevenLabs call was made")
        return 1

    os.makedirs(vdir, exist_ok=True)
    lines = slice_lines(slug, cut)
    pc.atomic_write_json(os.path.join(vdir, "lines.json"), lines)
    budget = pc.char_budget(slug, cut, fmt)
    chars = sum(len(l["text"]) for l in lines)
    scope = f" (--only {' '.join(only)})" if only else ""
    measured = (f"{len(lines)} VO lines sliced from script-{cut}.md, {chars:,} chars, "
                f"{chars / budget:.2f}× the {budget:,.0f}-char budget "
                f"(ceiling {pc.VOICE_CHAR_CEILING}×)")
    print(f"lines.json: {measured}")
    sh = write_gen_vo(project, slug, cut)
    print(f"wrote {os.path.relpath(sh, ROOT)}")
    if dry_run:
        print("--dry-run: not calling batch.py, no credits spent")
        return 0

    cmd = [sys.executable, os.path.join(ROOT, "tools", "tts", "batch.py"),
           "--project", project, "--cut", cut]
    if only:
        cmd += ["--only", *only]
    if force:
        cmd.append("--force")
    print(f"$ {' '.join(cmd)}", flush=True)
    rc = subprocess.run(cmd, cwd=ROOT).returncode
    write_log(slug, cut, attempt,
              f"cost guard, slice, `{' '.join(cmd[1:])}`{scope}",
              "" if rc == 0 else f"batch.py exited {rc} "
                                 f"(2 = terminal/dead key, 3 = retryable — the "
                                 f"orchestrator owns the retry, not this script)",
              measured + f"; batch.py exit {rc}. Postconditions (clip bytes, "
                         f"ffprobe duration vs chars, silence, scene arithmetic) are "
                         f"asserted by `pipeline_check check voice`.")
    return rc


def _selftest():
    """The guard is the whole point of this file: prove it refuses."""
    import json
    import shutil
    import tempfile

    tmp = tempfile.mkdtemp(prefix="ttsprep-")
    keep = pc.ROOT
    try:
        pc.ROOT = tmp
        vault = os.path.join(tmp, "vault", "videos", "s")
        os.makedirs(vault)
        fmt = json.load(open(os.path.join(keep, "tools", "format.json"), encoding="utf-8"))
        tier = fmt["tiers"]["medium"]
        rate = fmt["cuts"]["hi"]["chars_per_second"]
        budget = (tier["target_seconds"]
                  - tier["lines"] * (tier["lead_in_seconds"] + tier["tail_seconds"])) * rate
        with open(os.path.join(vault, "run.json"), "w", encoding="utf-8") as fh:
            json.dump({"tier": "medium", "target_seconds": tier["target_seconds"]}, fh)

        def write_script(total_chars):
            body = ["## Chapter 1 — x"]
            per = max(1, total_chars // 4)
            for i in range(4):
                body += [f"**1.{i + 1}**", "> " + "क" * per]
            with open(os.path.join(vault, "script-hi.md"), "w", encoding="utf-8") as fh:
                fh.write("\n".join(body) + "\n")

        write_script(int(budget * 0.9))
        # no audit note at all -> refuse
        assert pc.voice_cost_guard("s", "hi", fmt), "voiced a script that never passed gate one"
        with open(os.path.join(vault, "audit-hi.md"), "w", encoding="utf-8") as fh:
            fh.write("verdict: FAIL\n")
        assert pc.voice_cost_guard("s", "hi", fmt), "voiced a script whose audit says FAIL"
        with open(os.path.join(vault, "audit-hi.md"), "w", encoding="utf-8") as fh:
            fh.write("verdict: PASS\n")
        assert pc.voice_cost_guard("s", "hi", fmt) == [], "blocked a script inside budget"

        write_script(int(budget * pc.VOICE_CHAR_CEILING) + 400)
        over = pc.voice_cost_guard("s", "hi", fmt)
        assert over and "ceiling" in over[0], over

        # the slice keeps every line, in order, and retypes nothing
        write_script(int(budget * 0.5))
        lines = slice_lines("s", "hi")
        assert [l["id"] for l in lines] == ["1.1", "1.2", "1.3", "1.4"], lines
        raw = open(os.path.join(vault, "script-hi.md"), encoding="utf-8").read()
        for l in lines:
            assert l["text"] in raw, "a line was not sliced verbatim from the script"

        # gen_vo_<cut>.sh carries no absolute cd — the archive gotcha
        proj = os.path.join(tmp, "proj")
        os.makedirs(proj)
        sh = open(write_gen_vo(proj, "s", "hi"), encoding="utf-8").read()
        assert "cd " not in sh and sh.count("\n") == 4, sh
        print("selftest OK")
    finally:
        pc.ROOT = keep
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="slice, guard and voice one cut")
    p.add_argument("slug", nargs="?")
    p.add_argument("--cut", choices=["hi", "en"])
    p.add_argument("--only", nargs="+", metavar="ID",
                   help="regenerate ONLY these line ids (the two-line sample pair)")
    p.add_argument("--force", action="store_true", help="regenerate every clip")
    p.add_argument("--attempt", type=int, default=1, help="names the stage log")
    p.add_argument("--dry-run", action="store_true",
                   help="run the guard and write lines.json, but spend nothing")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    if a.selftest:
        _selftest()
        return 0
    if not (a.slug and a.cut):
        p.error("need <slug> and --cut")
    return prepare(a.slug, a.cut, a.only, a.dry_run, a.force, a.attempt)


if __name__ == "__main__":
    sys.exit(main())
