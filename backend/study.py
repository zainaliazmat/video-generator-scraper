#!/usr/bin/env python3
"""
study.py - build a competitor-study packet for the knowledge vault.
===================================================================

Given a topic query (matched against the library) or explicit video ids, pick
the TOP / MIDDLE / LOW performers by views, then for each:
  - download the video at <=480p (small files) into research/<slug>/
  - grab YouTube's own captions (auto or manual) and flatten them into a
    readable, timestamped transcript.txt  (no speech-to-text dependency)
  - extract keyframes with ffmpeg (dense over the hook, sparse after) so
    Claude can SEE the visual treatment
  - write manifest.md with the numbers + chapters for the analysis note

Claude then reads the packet and writes the study note into
vault/knowledge/video-studies/ (see vault/workflows/video-study.md).

Usage (from repo root):
    venv/bin/python backend/study.py "faceless ai tools"       # top/mid/low
    venv/bin/python backend/study.py --ids dQw4w9WgXcQ ...     # explicit picks
    ... --skip-video      # captions + metadata only (fast, no big download)

ponytail: transcripts come from YouTube captions only. If a video has none,
the packet says so - add whisper only when that actually blocks a study.
"""
import argparse
import os
import re
import statistics
import subprocess
import sys
from pathlib import Path

import yt_dlp

import library

RESEARCH_DIR = Path(__file__).resolve().parent.parent / "research"
MIN_DURATION_SEC = 240      # comparable long-form only (skip Shorts/clips)
MIN_VIEWS = 100             # below this a "low performer" teaches nothing


def _int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def pick_three(rows):
    """From library rows, pick [(rank, row)] = top/mid/low by views among
    comparable long-form videos. Pure - no I/O."""
    usable = []
    for r in rows:
        views = _int(r.get("views"))
        dur = _int(r.get("duration_sec"))
        if not (r.get("video_id") or "").strip():
            continue
        if views is None or views < MIN_VIEWS:
            continue
        if dur is not None and dur < MIN_DURATION_SEC:
            continue
        usable.append((views, r))
    usable.sort(key=lambda t: t[0], reverse=True)
    if not usable:
        return []
    if len(usable) <= 3:
        ranks = ["top", "mid", "low"]
        return [(ranks[i], r) for i, (_, r) in enumerate(usable)]
    med = statistics.median(v for v, _ in usable)
    mid = min(usable[1:-1], key=lambda t: abs(t[0] - med))
    return [("top", usable[0][1]), ("mid", mid[1]), ("low", usable[-1][1])]


# --------------------------------------------------------------------------
# Captions -> readable transcript
# --------------------------------------------------------------------------
_TS_RE = re.compile(r"(\d+):(\d{2}):(\d{2})[.,]\d+\s+-->")
_TAG_RE = re.compile(r"<[^>]+>")


def vtt_to_transcript(text):
    """Flatten a (possibly auto-generated, rolling-caption) VTT into
    '[m:ss] line' rows, deduping the repeated roll-up lines."""
    out, recent = [], []
    stamp = None
    for raw in text.splitlines():
        m = _TS_RE.match(raw.strip())
        if m:
            h, mnt, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
            total = h * 3600 + mnt * 60 + s
            stamp = f"[{total // 60}:{total % 60:02d}]"
            continue
        line = _TAG_RE.sub("", raw).strip()
        if (not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:"))
                or line.isdigit() or "-->" in line):
            continue
        if line in recent:            # rolling captions repeat the previous line
            continue
        out.append(f"{stamp or '[0:00]'} {line}")
        recent = (recent + [line])[-2:]
    return "\n".join(out)


# --------------------------------------------------------------------------
# Download + frames
# --------------------------------------------------------------------------
COOKIE_HINT = (
    "YouTube bot-check? Set YTAUTO_COOKIES=/path/to/cookies.txt (Netscape format) "
    "or YTAUTO_COOKIES_BROWSER=chrome|chromium|firefox|brave to authenticate yt-dlp."
)


def cookie_opts():
    """yt-dlp auth, opt-in by env. Unauthenticated fetches get 'Sign in to confirm
    you're not a bot' and every study dies at 0/N transcripts (2026-08-07).
    Opt-in rather than auto-reading a browser profile: the cookie jar is the
    user's logged-in session, not ours to open by default."""
    jar = os.environ.get("YTAUTO_COOKIES")
    if jar:
        return {"cookiefile": jar}
    browser = os.environ.get("YTAUTO_COOKIES_BROWSER")
    if browser:
        # ponytail: browser name only. Add profile/keyring/container members to
        # this tuple if a multi-profile setup ever needs them.
        return {"cookiesfrombrowser": (browser,)}
    return {}


def fetch(video_id, dest, skip_video=False):
    """Download <=480p video + English captions into dest. Returns info dict."""
    dest.mkdir(parents=True, exist_ok=True)
    opts = {
        "quiet": True, "no_warnings": True,
        "format": "bv*[height<=480]+ba/b[height<=480]/b",
        "merge_output_format": "mp4",
        "outtmpl": str(dest / "video.%(ext)s"),
        "writesubtitles": True, "writeautomaticsub": True,
        "subtitleslangs": ["en", "en-orig", "en-US", "en-GB", "hi", "hi-orig"],
        "subtitlesformat": "vtt",
        "skip_download": skip_video,
    }
    opts.update(cookie_opts())
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}",
                                download=True)
    # Flatten whichever caption file landed
    vtts = sorted(dest.glob("*.vtt"))
    if vtts:
        (dest / "transcript.txt").write_text(
            vtt_to_transcript(vtts[0].read_text(encoding="utf-8", errors="replace")),
            encoding="utf-8")
    return info or {}


def extract_frames(dest):
    """Keyframes: one per 5s over the first 30s (the hook), one per 30s after."""
    video = next((p for p in dest.glob("video.*")
                  if p.suffix in (".mp4", ".webm", ".mkv", ".m4v")), None)
    if not video:
        return
    frames = dest / "frames"
    frames.mkdir(exist_ok=True)
    base = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    subprocess.run(base + ["-t", "30", "-i", str(video), "-vf", "fps=1/5,scale=480:-1",
                           str(frames / "hook-%02d.jpg")], check=False)
    subprocess.run(base + ["-ss", "30", "-i", str(video), "-vf", "fps=1/30,scale=480:-1",
                           str(frames / "body-%02d.jpg")], check=False)


def _fmt(n):
    n = _int(n)
    return f"{n:,}" if n is not None else "?"


def manifest_entry(rank, row, info, has_transcript):
    lines = [f"## {rank.upper()} — {info.get('title') or row.get('title', '')}",
             f"- id: {row.get('video_id')}  |  https://www.youtube.com/watch?v={row.get('video_id')}",
             f"- channel: {info.get('channel') or row.get('channel', '')} "
             f"({_fmt(info.get('channel_follower_count') or row.get('subscribers'))} subs)",
             f"- views: {_fmt(info.get('view_count') or row.get('views'))}"
             f"  |  likes: {_fmt(info.get('like_count') or row.get('likes'))}"
             f"  |  uploaded: {info.get('upload_date') or row.get('upload_date', '?')}"
             f"  |  duration: {row.get('duration') or info.get('duration_string', '?')}",
             f"- transcript: {'yes' if has_transcript else 'NO CAPTIONS (flag for whisper)'}"]
    chapters = info.get("chapters") or []
    if chapters:
        lines.append("- chapters: " + " | ".join(
            f"{int(c.get('start_time', 0)) // 60}:{int(c.get('start_time', 0)) % 60:02d} {c.get('title', '')}"
            for c in chapters))
    return "\n".join(lines) + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(description="Build a top/mid/low competitor study packet.")
    p.add_argument("query", nargs="?", help="topic - matched against the library (title/channel/keyword)")
    p.add_argument("--ids", nargs="+", help="explicit video ids instead of a query")
    p.add_argument("--skip-video", action="store_true", help="captions + metadata only")
    args = p.parse_args(argv)

    if args.ids:
        picks = [(f"pick-{i}", {"video_id": vid}) for i, vid in enumerate(args.ids, 1)]
        slug = args.ids[0]
    elif args.query:
        conn = library.connect()
        rows = library.search(conn, args.query, limit=500)
        conn.close()
        picks = pick_three(rows)
        slug = re.sub(r"[^a-z0-9]+", "-", args.query.lower()).strip("-")
        if not picks:
            sys.exit(f"No usable videos in the library for '{args.query}' "
                     f"(need >={MIN_VIEWS} views, >={MIN_DURATION_SEC}s). Scrape first.")
    else:
        p.error("give a topic query or --ids")

    out = RESEARCH_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    manifest = [f"# Study packet: {args.query or slug}\n"]
    for rank, row in picks:
        vid = row["video_id"]
        dest = out / f"{rank}-{vid}"
        print(f"[{rank}] {vid} — downloading{' (captions only)' if args.skip_video else ' 480p'} ...")
        try:
            info = fetch(vid, dest, skip_video=args.skip_video)
        except Exception as exc:
            print(f"[{rank}] FAILED: {exc}")
            manifest.append(f"## {rank.upper()} — {vid} FAILED: {exc}\n")
            continue
        if not args.skip_video:
            extract_frames(dest)
        manifest.append(manifest_entry(rank, row, info, (dest / "transcript.txt").exists()))
        print(f"[{rank}] done -> {dest}")
    (out / "manifest.md").write_text("\n".join(manifest), encoding="utf-8")
    print(f"\nPacket ready: {out}/manifest.md\nNext: analyze per vault/workflows/video-study.md")
    # A study without transcripts is a study of thumbnails — fail loudly rather
    # than let a downstream note degrade silently (needs 2 of 3 picks readable).
    got = sum(1 for rank, row in picks
              if (out / f"{rank}-{row['video_id']}" / "transcript.txt").exists())
    if got < min(2, len(picks)):
        sys.exit(f"ERROR: only {got}/{len(picks)} picks produced a transcript — "
                 f"not enough to ground a study note.\n{COOKIE_HINT}")


if __name__ == "__main__":
    main()
