#!/usr/bin/env python3
"""
ideas.py - "predict my next video" for the TUI's Predict screen.
================================================================

Summarises the scraped data (top videos, breakout outliers, channel leaders,
title/length patterns) into a compact digest, sends it to Claude, and returns a
structured prediction: the single best NEW video to make next plus 4 alternatives.

Uses your Claude subscription through the Claude Agent SDK - the same auth the
Claude Code CLI uses - so no separate API key / billing is needed. It needs the
Claude Code CLI installed and logged in, and ANTHROPIC_API_KEY must NOT be set
(so it bills your subscription, not the pay-as-you-go API).

On failure it returns an HONEST error result (no fabricated numbers) so the UI
can show a real "couldn't generate / log in" state instead of fiction.
"""

import json
import re

import analyze  # reuse the metric helpers

MODEL = "claude-opus-4-8"
FALLBACK_MODEL = "claude-sonnet-4-6"   # used if your plan can't reach Opus


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


PREDICTION_SYSTEM = (
    "You are a sharp YouTube content strategist. You are given real scraped "
    "data about what is currently ranking for a set of search keywords. Predict "
    "the single best NEW video a small/mid creator should make next to maximise "
    "breakout (views relative to channel size), plus 4 alternatives. Cite real "
    "numbers and titles from the data."
)

PREDICTION_INSTRUCTION = (
    "Do not write any preamble, explanation, or commentary. Your entire reply "
    "must be the JSON object and nothing else.\n"
    "Return ONLY minified JSON, no prose: "
    '{"topic":string,"angle":string (one sentence, why now),'
    '"est_breakout":string (like "x12"),"rationale":string (2 sentences),'
    '"evidence":[3-4 short strings citing the data/patterns],'
    '"ideas":[{"title":string,"est":string}] (exactly 4)}.\n\nDATA DIGEST:\n'
)


def parse_prediction_json(text):
    if not text:
        return None
    a, b = text.find("{"), text.rfind("}")
    if a < 0 or b < 0 or b < a:
        return None
    try:
        return json.loads(text[a:b + 1])
    except (ValueError, TypeError):
        return None


def _digits(x):
    return re.sub(r"[^0-9.]", "", str(x if x is not None else "")) or ""


def normalize_prediction(obj):
    ev = obj.get("evidence") if isinstance(obj.get("evidence"), list) else []
    ideas_in = obj.get("ideas") if isinstance(obj.get("ideas"), list) else []
    ideas = []
    for it in ideas_in[:4]:
        it = it if isinstance(it, dict) else {}
        ideas.append({"title": str(it.get("title", "")), "est": _digits(it.get("est"))})
    return {
        "topic": str(obj.get("topic", "")),
        "angle": str(obj.get("angle", "")),
        "est": _digits(obj.get("est_breakout")) or "10",
        "rationale": str(obj.get("rationale", "")),
        "evidence": [str(e) for e in ev[:4]],
        "ideas": ideas[:4],
    }


async def _prediction_async(digest, on_text=None):
    """Run one Claude turn and return its text. If on_text(chunk) is given, each
    text chunk is streamed to it as it arrives (used by the live run log)."""
    from claude_agent_sdk import (query, ClaudeAgentOptions, AssistantMessage,
                                  TextBlock, ResultMessage)
    options = ClaudeAgentOptions(
        system_prompt=PREDICTION_SYSTEM, model=MODEL, fallback_model=FALLBACK_MODEL,
        allowed_tools=[], max_turns=1, setting_sources=None,
    )
    parts, result_text, err = [], "", None
    async for message in query(prompt=PREDICTION_INSTRUCTION + digest, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    parts.append(block.text)
                    if on_text:
                        on_text(block.text)
        elif isinstance(message, ResultMessage):
            if message.is_error:
                err = message.result or "Claude error"
            else:
                result_text = message.result or ""
    text = "".join(parts) or result_text
    if err and not text:
        raise RuntimeError(err)
    return text


def _classify_prediction_error(exc, CLINotFoundError):
    if CLINotFoundError is not None and isinstance(exc, CLINotFoundError):
        return "cli_missing"
    if any(w in str(exc).lower() for w in ("login", "log in", "auth", "unauthor")):
        return "not_logged_in"
    return "error"


def generate_prediction(rows, on_text=None):
    """Return {"ok": True, "source": "ai", ...prediction} on success, or
    {"ok": False, "reason": ..., "detail": ...} on any failure. Never fabricates.

    If on_text(chunk) is given, the model's text is streamed to it as it arrives.
    """
    try:
        from claude_agent_sdk import CLINotFoundError
    except ImportError:
        CLINotFoundError = None
    try:
        import anyio
        digest = build_digest(rows)
        # Safe: called from a worker thread (no running event loop).
        text = anyio.run(_prediction_async, digest, on_text)
        obj = parse_prediction_json(text)
        if not obj or not obj.get("topic"):
            return {"ok": False, "reason": "parse_failed",
                    "detail": "Claude returned no usable prediction."}
        return {"ok": True, "source": "ai", **normalize_prediction(obj)}
    except Exception as exc:
        return {"ok": False, "reason": _classify_prediction_error(exc, CLINotFoundError),
                "detail": str(exc)}
