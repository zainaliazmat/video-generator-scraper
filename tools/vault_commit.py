#!/usr/bin/env python3
"""Pre/post-run vault commits for the finance pipeline — explicit paths ONLY.

A bad autonomous run must be one `git revert`, without ever absorbing the
creator's unrelated in-flight work (spec R-2: `git add -A` once found 55
uncommitted files). So this script only ever touches the paths a run writes:

  vault/videos/<slug>/                       run state, scripts, audits, logs
  vault/knowledge/video-studies/<slug>.md    fin-research output
  vault/knowledge/money-facts-2026.md        post-render staging merge only
  vault/index.md                             fin-archive's catalog line

  # before a run — refuse if a previous session left these paths dirty:
  python3 tools/vault_commit.py preflight <slug>

  # after a milestone (post-render, post-archive) — commit them:
  python3 tools/vault_commit.py commit <slug> -m "finance-video: <slug> hi cut rendered"

Exit codes: 0 ok · 1 dirty/refused · 2 usage.
"""
import argparse
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_paths(slug):
    return [
        f"vault/videos/{slug}",
        f"vault/knowledge/video-studies/{slug}.md",
        "vault/knowledge/money-facts-2026.md",
        "vault/index.md",
    ]


def git(*args, repo=ROOT):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)


def existing_paths(slug, repo=ROOT):
    """git errors on pathspecs that match nothing — only pass what's on disk."""
    return [p for p in run_paths(slug) if os.path.exists(os.path.join(repo, p))]


def dirty(slug, repo=ROOT):
    paths = existing_paths(slug, repo)
    if not paths:
        return []
    out = git("status", "--porcelain", "--", *paths, repo=repo)
    return [l for l in out.stdout.splitlines() if l.strip()]


def preflight(slug, repo=ROOT):
    lines = dirty(slug, repo)
    if lines:
        print(f"REFUSED: {len(lines)} uncommitted change(s) in this run's vault paths "
              "— commit or stash them first, otherwise a revert of this run would "
              "revert your work with it:")
        for l in lines:
            print(f"  {l}")
        return 1
    print(f"clean: vault paths for '{slug}'")
    return 0


def commit(slug, message, repo=ROOT):
    if not dirty(slug, repo):
        print("nothing to commit")
        return 0
    paths = existing_paths(slug, repo)
    add = git("add", "--", *paths, repo=repo)
    if add.returncode != 0:
        print(add.stderr.strip() or "git add failed")
        return 1
    res = git("commit", "-m", message, "--", *paths, repo=repo)
    print(res.stdout.strip() or res.stderr.strip())
    return res.returncode


def _selftest():
    import shutil, tempfile
    repo = tempfile.mkdtemp(prefix="vaultcommit-")
    try:
        for cmd in (["init", "-q"], ["config", "user.email", "t@t"],
                    ["config", "user.name", "t"]):
            assert git(*cmd, repo=repo).returncode == 0
        slug = "test-topic"
        vdir = os.path.join(repo, "vault", "videos", slug)
        os.makedirs(vdir)
        with open(os.path.join(vdir, "run.json"), "w") as fh:
            fh.write("{}")
        # creator's unrelated dirty file must never block or be committed
        with open(os.path.join(repo, "unrelated.md"), "w") as fh:
            fh.write("in-flight creator work")

        assert preflight(slug, repo) == 1, "untracked run file should refuse preflight"
        assert commit(slug, "run: initial", repo) == 0
        assert preflight(slug, repo) == 0
        status = git("status", "--porcelain", repo=repo).stdout
        assert "unrelated.md" in status, "creator's file must stay uncommitted"
        assert "run.json" not in status
        print("selftest OK")
    finally:
        shutil.rmtree(repo, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser(description="explicit-path vault commits for pipeline runs")
    p.add_argument("mode", nargs="?", choices=["preflight", "commit"])
    p.add_argument("slug", nargs="?")
    p.add_argument("-m", "--message", default=None)
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        _selftest()
        return 0
    if not (args.mode and args.slug):
        p.error("need: <preflight|commit> <slug>")
    if args.mode == "preflight":
        return preflight(args.slug)
    return commit(args.slug, args.message or f"finance-video: {args.slug} checkpoint")


if __name__ == "__main__":
    sys.exit(main())
