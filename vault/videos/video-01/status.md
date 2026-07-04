---
summary: Video #1 ("Best AI Tools for Faceless YouTube Videos — I Tested the Whole Stack") — where it stands, what exists locally vs only in the web project, and the exact next steps.
updated: 2026-07-04
source: Notion decisions log §1, §5, §9 entries 2026-06-30 → 2026-07-04
---

# Video #1 — status

**Stage: MANUAL CAPTURE PENDING.** Script locked at v2 (~12:05 runtime, mid-roll-safe,
delivery-marked). Automation experiment parked 2026-07-03 — creator records the 10
clips + own-voice VO by hand off the recording guide (doubles as the "I tested" pass).

## In the vault (durable, Code-readable)
- [[script-v2]] — the locked v2 script (delivery-score markup, fact-check table,
  affiliate setup). Rescued from ~/Downloads 2026-07-04.

## ONLY in the claude.ai web project (paste here to make durable) ⚠️
- `video-01-DESIGN.md` — HyperFrames design doc (`claude` warm-editorial grade).
- `video-01-STORYBOARD.md` — 12-beat storyboard locked to the v2 script; the ~70%
  reward = the "inauthentic content" + music monetization-protection tip (teased
  1:15, paid 8:25).
- `video-01-RECORDING-GUIDE.md` — the 10-clip shot list (ChatGPT, ElevenLabs, Pexels,
  optional Runway pricing, CapCut, Canva, InVideo, Pictory, Fliki, YouTube Studio) + VO.
- `hyperframes_production.md` — the production skill → [[../../skills/hyperframes_production]].
- (v1 of the script also exists in ~/Downloads; superseded by v2 — not vaulted.)

## Next steps (Notion §5)
1. Creator records the 10 clips + VO per the guide (backs every "I tested" claim).
2. Claude maps clips → storyboard beats, writes the HyperFrames build prompt.
3. Build: sound-design.json → compositions → `npm run check` → render.
4. Day-of re-verify: all tool prices + YouTube policy wording (they drift).
5. Publish: cleared music (YT Audio Library); AI-disclosure toggle ONLY if visuals
   contain realistic synthetic media (own-voice narration does not trigger it).
6. Then Video #2 = full build-along using this stack.

**Open decision:** ship this first, or the reframed HyperFrames honest-review
launch piece first (reps/authority vs direct money — see [[../../knowledge/niches/closed-niches]]).
