#!/usr/bin/env python3
"""
ideas.py - turn the scraped data into a content plan with Claude.
=================================================================

Reads youtube_results.tsv, summarises what's working (top videos, breakout
outliers, channel leaders, title/length patterns), sends that digest to Claude,
and writes a content-strategy report:

    youtube_content_ideas.md

  - Theme clusters across all the videos
  - Content gaps (high interest, weak/!thin coverage = your opening)
  - Ready-to-use video ideas (title + angle + hook + why)
  - Competitor notes (what the dominant channels do well)

Uses your Claude subscription through the Claude Agent SDK - the same auth the
Claude Code CLI uses - so no separate API key / billing is needed. Make sure:
  - Node.js + the Claude Code CLI are installed and you're logged in
    (the `claude` command works on its own), and
  - ANTHROPIC_API_KEY is NOT set in your environment (so it bills your
    subscription instead of the pay-as-you-go API).
Then:
    python ideas.py            # uses youtube_results.tsv
    python ideas.py other.tsv
"""

import sys
from pathlib import Path

import analyze  # reuse the metric helpers

MODEL = "claude-opus-4-8"
FALLBACK_MODEL = "claude-sonnet-4-6"   # used if your plan can't reach Opus
OUT_PATH = "youtube_content_ideas.md"


def _fmt_int(n):
    try:
        return f"{int(n):,}"
    except (TypeError, ValueError):
        return str(n)


def build_digest(rows, max_titles_per_kw=15):
    """Compact, information-dense summary of the dataset for the model."""
    analyze.score_rows(rows)
    lines = []

    kw_stats = analyze.per_keyword_stats(rows)
    lines.append(f"DATASET: {len(rows)} videos across {len(kw_stats)} keywords, "
                 f"{len({r.get('channel','') for r in rows})} unique channels.\n")

    # Per-keyword: stats + top titles by views
    by_kw = {}
    for r in rows:
        by_kw.setdefault(r.get("keyword", ""), []).append(r)
    for st in kw_stats:
        kw = st["keyword"]
        items = sorted(by_kw.get(kw, []), key=lambda x: x["_views"], reverse=True)
        lines.append(f"## KEYWORD: {kw}")
        lines.append(f"   videos={st['videos']} avg_views={_fmt_int(st['avg_views'])} "
                     f"median_views={_fmt_int(st['median_views'])}")
        lines.append("   Top videos (views | subs | likes | title):")
        for r in items[:max_titles_per_kw]:
            lines.append(f"     {_fmt_int(r['_views'])} | {_fmt_int(r['_subs'])} | "
                         f"{_fmt_int(r.get('likes') or 0)} | {r.get('title','')}")
        lines.append("")

    # Breakout outliers (real traction, beat their channel size)
    outliers = sorted([r for r in rows if r["views_per_sub"] is not None
                       and r["_views"] >= analyze.MIN_OUTLIER_VIEWS],
                      key=lambda x: x["views_per_sub"], reverse=True)[:15]
    lines.append("## BREAKOUT OUTLIERS (views >> channel size):")
    for r in outliers:
        lines.append(f"   x{r['views_per_sub']} ({_fmt_int(r['_views'])} views, "
                     f"{_fmt_int(r['_subs'])} subs): {r.get('title','')}")
    lines.append("")

    # Channel leaders
    lines.append("## TOP CHANNELS (by presence in results):")
    for c in analyze.channel_stats(rows)[:15]:
        lines.append(f"   {c['channel']} - {c['videos_in_results']} videos, "
                     f"{_fmt_int(c['subscribers'])} subs, "
                     f"avg {_fmt_int(c['avg_views'])} views")
    lines.append("")

    # Patterns
    lines.append("## WHAT WINS (avg views by bucket):")
    for title, recs in analyze.pattern_stats(rows):
        lines.append(f"   {title}:")
        for rec in recs:
            lines.append(f"     {rec['bucket']}: {rec['videos']} videos, "
                         f"avg {_fmt_int(rec['avg_views'])} views")
    lines.append("")
    return "\n".join(lines)


SYSTEM = (
    "You are a sharp YouTube content strategist specialising in the AI-tools / "
    "make-money-with-AI niche. You are given real scraped data about what is "
    "currently ranking for a set of search keywords: view counts, subscriber "
    "counts, engagement, title patterns, and which channels dominate. Your job "
    "is to turn this into an actionable content plan for someone who wants to "
    "make videos (or affiliate/SEO content) in this niche and win. Be specific "
    "and concrete - cite real numbers and real titles from the data. Avoid "
    "generic advice."
)

PROMPT_TEMPLATE = """Here is the scraped YouTube data digest:

{digest}

Using ONLY what this data supports, write a content-strategy report in Markdown
with these sections:

# YouTube Content Strategy — AI Tools Niche

## 1. Theme map
Cluster the videos into the main themes you see. For each theme: a name, a
one-line description, which keyword(s) it spans, and 2-3 example titles from the
data. Note which themes are crowded vs. underserved.

## 2. What's working (evidence-based)
The concrete patterns that correlate with high views here — title style, video
length, channel size effects, engagement. Cite the bucket numbers.

## 3. Content gaps & opportunities
Where is there clear audience interest but weak, thin, or repetitive coverage?
For each gap: the evidence from the data, and why it's an opening. Rank them by
opportunity (strongest first).

## 4. Video ideas (10)
Ten specific, ready-to-make video ideas tailored to the gaps and winning
patterns above. For each: a click-worthy **title**, the **angle**, a one-line
**hook**, the **target keyword**, and **why it should work** (tie to the data).

## 5. Competitor notes
The 3-5 dominant channels and what specifically they do well that's worth
learning from (and where they leave room).

Keep it tight and skimmable. Lead with the actionable conclusion in each section.
"""


async def _generate_async(digest, on_text):
    """Run one Claude turn through the Agent SDK and collect the report text."""
    from claude_agent_sdk import (query, ClaudeAgentOptions, AssistantMessage,
                                  TextBlock, ResultMessage)
    options = ClaudeAgentOptions(
        system_prompt=SYSTEM,
        model=MODEL,
        fallback_model=FALLBACK_MODEL,
        allowed_tools=[],        # pure text generation - no file/tool access
        max_turns=1,
        setting_sources=None,    # don't load this project's CLAUDE.md / settings
    )
    parts = []
    result_text = ""
    async for message in query(prompt=PROMPT_TEMPLATE.format(digest=digest),
                               options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    parts.append(block.text)
                    on_text(block.text)
        elif isinstance(message, ResultMessage):
            if message.is_error:
                raise RuntimeError(message.result or "Claude returned an error.")
            result_text = message.result or ""
    return "".join(parts) or result_text


def generate(rows):
    try:
        from claude_agent_sdk import CLINotFoundError, ClaudeSDKError
    except ImportError:
        sys.exit("The 'claude-agent-sdk' package is needed for AI ideas. Run:\n"
                 "   pip install -r requirements.txt   (or: pip install claude-agent-sdk)\n"
                 "It also needs the Claude Code CLI: npm install -g @anthropic-ai/claude-code")
    import anyio

    digest = build_digest(rows)
    print(f"Asking Claude ({MODEL}) via your Claude subscription "
          f"(Claude Code auth - no API key) ...\n")

    def on_text(t):
        print(t, end="", flush=True)

    try:
        report = anyio.run(_generate_async, digest, on_text)
    except CLINotFoundError:
        sys.exit("\nClaude Code CLI not found. Install it and log in first:\n"
                 "   npm install -g @anthropic-ai/claude-code\n"
                 "   claude        # then /login with your subscription")
    except ClaudeSDKError as exc:
        sys.exit(f"\nClaude Agent SDK error: {exc}")
    print()
    return report


def run(data_path="youtube_results.tsv", out_path=OUT_PATH):
    rows = analyze.load_rows(data_path)
    if not rows:
        sys.exit(f"'{data_path}' has no rows. Run the scraper first.")
    report = generate(rows)
    Path(out_path).write_text(report, encoding="utf-8")
    print(f"\nContent plan saved:\n   {Path(out_path).resolve()}")
    return out_path


if __name__ == "__main__":
    data_in = sys.argv[1] if len(sys.argv) > 1 else "youtube_results.tsv"
    run(data_in)
