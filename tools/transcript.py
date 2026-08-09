#!/usr/bin/env python3
"""Build the YouTube caption pack for a rendered cut: narration .md + .srt.

The two inputs are the two things that already exist and are already the
authority — nothing is retyped:

  vault/videos/<slug>/script-<cut>.md   the VO lines, verbatim (`**N.M**` then `> line`)
  studio/videos/<slug>-<cut>/index.html the real clip times (`<audio id="vo-N-M">`)

They are joined on the line id, so a caption cannot drift from the audio: every
cue starts exactly where its clip starts. Mismatched ids are a hard error.

    python3 tools/transcript.py japanese-money-methods --cut en

Writes vault/videos/<slug>/narration-<cut>.md (the human/YouTube-paste file)
and studio/videos/<slug>-<cut>/renders/captions-<cut>.srt (the upload).
"""
import argparse
import html
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# YouTube renders at most two ~42-char lines. Longer cues get split once, at the
# clause boundary nearest the middle, with the duration shared out by length.
MAX_CUE_CHARS = 84
SPLIT_MARKS = ("—", "–", ";", ",", "।", "|")


def read_script(path):
    """[(line_id, chapter_title, text)] in file order."""
    out, chapter, pending = [], None, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("## Chapter "):
            # "## Chapter 4 — Mottainai (METHOD ONE · ...)" -> "Mottainai"
            title = line[len("## Chapter "):]
            title = re.sub(r"^\d+\s*[—-]\s*", "", title)
            chapter = re.sub(r"\s*\(.*$", "", title).strip()
            continue
        # `**3.5**`, and also `**3.5** ★ *expanded +45*` — fin-script annotates a line
        # it has rewritten, and matching the WHOLE line dropped every annotated one.
        # Ten of passive-income-number-hi's 81 lines carry a marker; a slicer built on
        # the strict form found 71 and would have voiced a cut missing ten lines, with
        # timing.json derived from the same short list so nothing downstream disagreed.
        # Anchored at the start on purpose: the script also carries budget TABLES whose
        # rows open `| **3.5** | 65 | …`, and those are not lines.
        m = re.match(r"\*\*(\d+\.\d+)\*\*(?:\s|$)", line)
        if m:
            pending = m.group(1)
            continue
        if pending and line.startswith(">"):
            out.append((pending, chapter, line.lstrip("> ").strip()))
            pending = None
    return out


def read_times(path):
    """{line_id: (start, duration)} from the composition's own <audio> rows."""
    times = {}
    for tag in re.findall(r"<audio\b[^>]*>", path.read_text(encoding="utf-8")):
        m = re.search(r'id="vo-(\d+)-(\d+)"', tag)
        if not m:
            continue
        start = float(re.search(r'data-start="([\d.]+)"', tag).group(1))
        dur = float(re.search(r'data-duration="([\d.]+)"', tag).group(1))
        times[f"{m.group(1)}.{m.group(2)}"] = (start, dur)
    return times


def split_cue(text, start, dur):
    """One cue, or two split at the clause boundary nearest the middle."""
    if len(text) <= MAX_CUE_CHARS:
        return [(start, dur, text)]
    # Only the middle 60% is a candidate: a mark at either end (a trailing danda,
    # a leading "So,") leaves one side empty and the cue would not split at all.
    mid, best = len(text) // 2, None
    lo, hi = int(len(text) * 0.2), int(len(text) * 0.8)
    for i in range(lo, hi):
        if text[i] in SPLIT_MARKS and (best is None or abs(i - mid) < abs(best - mid)):
            best = i
    if best is None:  # no punctuation to lean on — break at the nearest space
        best = text.rfind(" ", lo, mid) or mid
    head, tail = text[: best + 1].strip(), text[best + 1:].strip()
    if not head or not tail:
        return [(start, dur, text)]
    cut = dur * len(head) / (len(head) + len(tail))
    # An uneven split can leave one half still over the cap; recurse on both.
    # This terminates: each half is shorter, and an unsplittable one returns itself.
    return split_cue(head, start, cut) + split_cue(tail, start + cut, dur - cut)


def ts(seconds):
    ms = round(seconds * 1000)
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def clock(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m}:{s:02d}"


def build(slug, cut):
    script = ROOT / "vault" / "videos" / slug / f"script-{cut}.md"
    comp = ROOT / "studio" / "videos" / f"{slug}-{cut}" / "index.html"
    for p in (script, comp):
        if not p.exists():
            sys.exit(f"missing: {p}")

    lines, times = read_script(script), read_times(comp)
    ids, timed = [i for i, _, _ in lines], set(times)
    missing, extra = set(ids) - timed, timed - set(ids)
    if missing or extra:
        sys.exit(f"line ids do not match — script-only {sorted(missing)}, "
                 f"composition-only {sorted(extra)}")

    srt, md, plain, chapter = [], [], [], None
    for line_id, chap, text in lines:
        start, dur = times[line_id]
        if chap != chapter:
            chapter = chap
            md.append(f"\n## {clock(start)} — {chapter}\n")
        md.append(f"**{line_id}** · `{clock(start)}`  \n{text}\n")
        plain.append(text)
        for c_start, c_dur, c_text in split_cue(text, start, dur):
            srt.append((c_start, c_start + c_dur, c_text))

    srt_out = "\n".join(
        f"{n}\n{ts(a)} --> {ts(b)}\n{html.unescape(t)}\n"
        for n, (a, b, t) in enumerate(srt, 1)
    )
    end = max(b for _, b, _ in srt)
    head = (
        "---\n"
        f"summary: Full narration for the {cut} cut of «{slug}» — {len(lines)} VO lines, "
        f"{len(srt)} caption cues, {clock(end)} of speech. Joined from script-{cut}.md "
        f"(text) and the shipped composition's own <audio> data-start values (times), so "
        "every cue sits exactly on its clip. Upload the .srt named below; the plain block "
        "at the foot is the no-timecode fallback for YouTube's auto-sync.\n"
        "updated: 2026-08-06\n"
        f"source: generated by tools/transcript.py from vault/videos/{slug}/script-{cut}.md "
        f"+ studio/videos/{slug}-{cut}/index.html. Never hand-edited — re-run the tool.\n"
        "---\n\n"
        f"# Narration — {slug} ({cut} cut)\n\n"
        f"**Upload this file to YouTube:** `studio/videos/{slug}-{cut}/renders/"
        f"captions-{cut}.srt`\n"
        "(YouTube Studio → the video → Subtitles → Add language → **Upload file** → "
        "*With timing*.)\n"
    )
    foot = (
        "\n---\n\n## Plain transcript (no timecodes)\n\n"
        "Only for YouTube's *Transcript → auto-sync* path, if the .srt is not used. "
        "Auto-sync guesses the timing; the .srt already knows it, so prefer the .srt.\n\n"
        "```\n" + "\n".join(plain) + "\n```\n"
    )
    return head + "\n".join(md) + foot, srt_out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--cut", required=True, choices=["hi", "en"])
    a = ap.parse_args()

    md, srt = build(a.slug, a.cut)
    md_path = ROOT / "vault" / "videos" / a.slug / f"narration-{a.cut}.md"
    srt_path = (ROOT / "studio" / "videos" / f"{a.slug}-{a.cut}" / "renders"
                / f"captions-{a.cut}.srt")
    srt_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md, encoding="utf-8")
    srt_path.write_text(srt, encoding="utf-8")
    print(f"wrote {md_path.relative_to(ROOT)}")
    print(f"wrote {srt_path.relative_to(ROOT)}  ({srt.count(' --> ')} cues)")


def demo():
    """Self-check: the split shares time by length and never loses text."""
    long = "a" * 50 + ", " + "b" * 50
    cues = split_cue(long, 10.0, 10.0)
    assert len(cues) == 2, cues
    assert cues[0][0] == 10.0 and abs(cues[0][1] + cues[1][1] - 10.0) < 1e-9
    assert abs(cues[1][0] - (cues[0][0] + cues[0][1])) < 1e-9
    assert cues[0][2] + " " + cues[1][2] == "a" * 50 + ", " + "b" * 50
    assert split_cue("short one", 0.0, 2.0) == [(0.0, 2.0, "short one")]
    # no punctuation at all still splits rather than overflowing
    assert len(split_cue(" ".join(["word"] * 30), 0.0, 5.0)) == 2
    assert ts(3661.5) == "01:01:01,500"

    # An annotated id is still an id, a table row is still not one.
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8",
                                     delete=False) as fh:
        fh.write("## Chapter 3 — x\n"
                 "| **3.9** | 65 | 110 | a budget table row, not a line |\n"
                 "**3.1**\n> plain\n"
                 "**3.2** ★ *expanded +45*\n> annotated\n")
        p = fh.name
    got = read_script(pathlib.Path(p))
    os.unlink(p)
    assert [(i, t) for i, _, t in got] == [("3.1", "plain"), ("3.2", "annotated")], got
    print("ok")


if __name__ == "__main__":
    if "--demo" in sys.argv:
        demo()
    else:
        main()
