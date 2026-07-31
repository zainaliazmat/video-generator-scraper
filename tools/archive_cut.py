#!/usr/bin/env python3
"""Retire a finished video: archive its source into the vault, delete it from studio.

The rule (vault/CLAUDE.md § the finished-video rule): a YouTube URL means the
video is finished. Its home is YouTube, its knowledge home is the vault. Give
this script the URL and it does the rest.

    tools/archive_cut.py <slug> --hi <url> --en <url> [--dry-run]
    tools/archive_cut.py --self-check

Copies the text that reproduces the video (composition, prompts, VO lines,
thumbnails) into vault/videos/<slug>/src/{hi,en,thumbs}/, verifies every file
landed byte-for-byte, records the URLs in the milestone note, and only then
deletes studio/videos/<slug>*. Nothing under studio/videos is in any git, so
the order matters: copy, verify, then delete.
"""
import argparse
import filecmp
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# What reproduces the video. Globs are relative to a cut dir and non-recursive,
# so node_modules/, assets/img/*.jpg, assets/voice/*.mp3 and the fonts never match.
KEEP = (
    "*.html", "*.json", "*.sh", "*.mjs", "*.py", "*.md", "*.css",
    "thumbnail*.png",
    "assets/voice/*.txt",
    "assets/img/*.src", "assets/img/CREDITS.txt",
    # the re-tinted Lottie, ~400 KB each, capped at 3 per cut. Kept rather than
    # dropped as regenerable: a LottieFiles asset URL can rotate, and the tint is
    # a derivative of whatever tools/lottie/tint.py did that day.
    "assets/lottie/*.js",
)
DROP = {"package-lock.json"}  # regenerable, and big

CHANNEL = {"hi": "@cashguruguides", "en": "@moneymavens101"}

# ponytail: two topics predate the -hi/-en convention. One-off, not a naming system.
ALIAS = {"50-30-20-rule": ["50-30-20-thumbs"]}


def cut_dirs(root, slug):
    """studio dirs for this slug -> {dest_name: src_dir}. Bare dir is the hi cut
    unless an explicit -hi exists, in which case it is an older draft."""
    videos = root / "studio" / "videos"
    found = [d for d in videos.glob(f"{slug}*") if d.is_dir()]
    found += [videos / a for a in ALIAS.get(slug, []) if (videos / a).is_dir()]
    out = {}
    for d in sorted(found, key=lambda p: len(p.name), reverse=True):
        suffix = d.name[len(slug):] if d.name.startswith(slug) else "-thumbs"
        dest = {"-hi": "hi", "-en": "en", "-thumbs": "thumbs"}.get(suffix, "hi")
        out[dest if dest not in out else "legacy"] = d
    return out


def plan(root, slug):
    """[(src_dir, dest_dir, [(src_file, dest_file)])] — what would be copied."""
    steps = []
    for dest, src in sorted(cut_dirs(root, slug).items()):
        dest_dir = root / "vault" / "videos" / slug / "src" / dest
        files = sorted({f for pat in KEEP for f in src.glob(pat)
                        if f.is_file() and f.name not in DROP})
        steps.append((src, dest_dir, [(f, dest_dir / f.relative_to(src)) for f in files]))
    return steps


def record_urls(root, slug, urls, today):
    """Append the URLs to the milestone note — the vault's home for 'this shipped'."""
    note = root / "vault" / "videos" / slug / "index.md"
    note.parent.mkdir(parents=True, exist_ok=True)
    text = note.read_text() if note.exists() else (
        f"---\nsummary: Milestone note for {slug}.\nupdated: {today}\n"
        f"source: tools/archive_cut.py\n---\n\n# {slug}\n"
    )
    if all(url in text for url in urls.values() if url):
        return note  # already recorded — don't append a second block
    # the shipped thumbnail is already copied by the time this runs (copy → verify → note)
    thumbs = root / "vault" / "videos" / slug / "src" / "thumbs"
    def thumb(cut):
        hit = sorted(thumbs.glob(f"thumbnail-{cut}*.png"))
        return f"`src/thumbs/{hit[0].name}`" if hit else ""
    rows = "\n".join(f"| {cut} | {CHANNEL[cut]} | {url} | {thumb(cut)} |"
                     for cut, url in sorted(urls.items()) if url)
    note.write_text(text.rstrip() + f"""

## Published + archived ({today})

**State: LIVE on YouTube · source archived · studio dir deleted.**

| Cut | Channel | URL | Thumbnail |
|---|---|---|---|
{rows}

**Source: `src/`** — composition, meta/package JSON, `gen_vo_*.sh`, the VO lines
(`assets/voice/*.txt`), the image prompts (`assets/img/*.src`), stock CREDITS and the
thumbnail PNGs. `studio/videos/{slug}*` is **deleted** per the finished-video rule
(`vault/CLAUDE.md`). **Re-render is reproducible, not free** — the scene photos and VO
mp3s are gone, so a rebuild re-pays image gens + ElevenLabs off the archived prompts
and lines. `gen_vo_*.sh` still `cd`s into the deleted studio path — repoint it first.

Still owed: analytics after 28 days.
""")
    return note


def archive(root, slug, urls, dry_run=False, today=None):
    today = today or date.today().isoformat()
    steps = plan(root, slug)
    if not steps:
        sys.exit(f"no studio/videos/{slug}* directories — nothing to archive")
    if not any(urls.values()):
        sys.exit(f"refusing: no YouTube URL given for {slug}. A URL is what makes it finished.")

    for src, dest_dir, files in steps:
        print(f"{src.relative_to(root)} -> {dest_dir.relative_to(root)}  ({len(files)} files)")
        for f, _ in files:
            print(f"    {f.relative_to(src)}")
    if dry_run:
        print("\n(dry run — nothing copied or deleted)")
        return

    for _, dest_dir, files in steps:
        for f, target in files:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, target)

    # Verify before deleting. Nothing here is in git; a bad copy is unrecoverable.
    for _, _, files in steps:
        for f, target in files:
            if not target.exists() or not filecmp.cmp(f, target, shallow=False):
                sys.exit(f"verify failed for {target} — nothing deleted")

    record_urls(root, slug, urls, today)
    for src, _, _ in steps:
        shutil.rmtree(src)
        print(f"deleted {src.relative_to(root)}")
    print(f"archived {slug} -> vault/videos/{slug}/src/")


def self_check():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        cut = root / "studio" / "videos" / "demo-hi"
        (cut / "assets" / "img").mkdir(parents=True)
        (cut / "assets" / "voice").mkdir(parents=True)
        (cut / "node_modules" / "junk").mkdir(parents=True)
        (cut / "index.html").write_text("<html>")
        (cut / "package-lock.json").write_text("{}")
        (cut / "assets" / "img" / "s1.jpg.src").write_text("a prompt")
        (cut / "assets" / "img" / "s1.jpg").write_bytes(b"\xff" * 99)
        (cut / "assets" / "voice" / "h1.txt").write_text("a line")
        (cut / "assets" / "voice" / "h1.mp3").write_bytes(b"\x00" * 99)
        (cut / "node_modules" / "junk" / "readme.md").write_text("noise")
        thumbs = root / "studio" / "videos" / "demo-thumbs"
        thumbs.mkdir()
        (thumbs / "thumbnail-hi-v2.png").write_bytes(b"\x89PNG")

        archive(root, "demo", {"hi": "https://youtu.be/X", "en": ""}, today="2026-01-01")

        src = root / "vault" / "videos" / "demo" / "src"
        kept = {str(p.relative_to(src)) for p in src.rglob("*") if p.is_file()}
        assert kept == {"hi/index.html", "hi/assets/img/s1.jpg.src",
                        "hi/assets/voice/h1.txt", "thumbs/thumbnail-hi-v2.png"}, kept
        assert not cut.exists() and not thumbs.exists(), "studio dirs not deleted"
        note = (root / "vault" / "videos" / "demo" / "index.md").read_text()
        assert "https://youtu.be/X" in note and "@cashguruguides" in note, note
        assert "`src/thumbs/thumbnail-hi-v2.png`" in note, note

        # a URL is mandatory: no URL, no deletion
        cut.mkdir(parents=True)
        (cut / "index.html").write_text("<html>")
        try:
            archive(root, "demo", {"hi": "", "en": ""})
            raise AssertionError("archived without a URL")
        except SystemExit:
            pass
        assert cut.exists(), "deleted a cut that had no URL"
    print("self-check ok")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("slug", nargs="?")
    p.add_argument("--hi", default="", help="YouTube URL of the Hindi cut")
    p.add_argument("--en", default="", help="YouTube URL of the English cut")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--self-check", action="store_true")
    a = p.parse_args()
    if a.self_check:
        self_check()
    elif a.slug:
        archive(ROOT, a.slug, {"hi": a.hi, "en": a.en}, a.dry_run)
    else:
        p.error("give a slug, or --self-check")
