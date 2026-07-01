// Pure progress parsing for the scrape run screen. No Svelte — unit-tested.
// Log-line shapes come from backend/youtube_scraper.py run_scrape/helpers:
//   search:   [i/n] Searching "kw" ...      /  [i/n] kw — N videos
//   detail:   "   video N — fetching ..."   (full mode per-video)
//   channels: "Looking up N channels ..."   /  [i/n] name ... ok

export const STEPS = [
  'Searched keywords',
  'Pulled videos',
  'Looking up channels',
  'Score breakout multipliers',
]

export function computeProgress(lines) {
  let phaseIndex = 0
  let videos = 0, channels = 0, totalChannels = 0
  for (const raw of lines) {
    const line = raw || ''
    const v = line.match(/—\s*(\d+)\s*videos?/i)
    if (v) { videos += +v[1]; phaseIndex = Math.max(phaseIndex, 1) }
    if (/^\s*video\s+\d+\s+—/i.test(line)) phaseIndex = Math.max(phaseIndex, 1)
    const lu = line.match(/Looking up\s+(\d+)\s+channels/i)
    if (lu) { totalChannels = +lu[1]; phaseIndex = Math.max(phaseIndex, 2) }
    const ch = line.match(/^\[(\d+)\/(\d+)\].*\.\.\.\s*ok$/i)
    if (ch) { channels = +ch[1]; totalChannels = +ch[2]; phaseIndex = Math.max(phaseIndex, 2) }
  }
  let pct = 0
  for (let i = lines.length - 1; i >= 0; i--) {
    const m = (lines[i] || '').match(/\[(\d+)\/(\d+)\]/)
    if (m) { pct = Math.round((+m[1] / +m[2]) * 100); break }
  }
  return { pct, phaseIndex, phase: STEPS[phaseIndex], videos, channels, totalChannels }
}

// Time-left in ms, or null when we should not show a number yet (D3):
// before the first phase, too little signal, or already complete.
export function estimateTimeLeft(pct, elapsedMs, phaseIndex) {
  if (phaseIndex < 1 || pct < 10 || pct >= 100) return null
  const total = elapsedMs / (pct / 100)
  return Math.max(0, Math.round(total - elapsedMs))
}
