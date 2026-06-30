// Number/duration formatting, ported from the Voyara Signal prototype.
export function fmtViews(n) {
  if (n == null) return '—'
  if (n >= 1e6) return (n / 1e6).toFixed(2) + 'M'
  if (n >= 1e3) return Math.round(n / 1e3) + 'K'
  return '' + n
}
export function fmtSubs(n) {
  if (n == null) return '—'
  if (n >= 1e6) return (n / 1e6).toFixed(1) + 'M'
  if (n >= 1e3) return Math.round(n / 1e3) + 'K'
  return '' + n
}
export function fmtK(n) {
  if (n == null) return '—'
  if (n >= 1e6) return (n / 1e6).toFixed(1) + 'M'
  if (n >= 1e3) return (n / 1e3).toFixed(1) + 'K'
  return '' + n
}
export function fmtDate(iso) {
  if (!iso) return ''
  try {
    return new Date(iso).toLocaleDateString(undefined, { day: 'numeric', month: 'short', year: 'numeric' })
  } catch (_) { return iso }
}
// A deterministic gradient per video id, used as a thumbnail fallback.
const GRADIENTS = [
  'linear-gradient(150deg,#FFE3B8,#E8A052 60%,#8E5A1E)',
  'linear-gradient(150deg,#A9D6FF,#4D8FD6 60%,#1F4E86)',
  'linear-gradient(160deg,#9FE5D2,#3FAE8F 55%,#16614D)',
  'linear-gradient(165deg,#8FA7FF,#5468D6 55%,#2C3A8E)',
  'linear-gradient(165deg,#FFC2B0,#E0705E 55%,#8C3140)',
  'linear-gradient(165deg,#D7B6FF,#8E63D8 60%,#4A2E86)',
]
export function gradientFor(id) {
  let h = 0
  for (const c of String(id)) h = (h * 31 + c.charCodeAt(0)) >>> 0
  return GRADIENTS[h % GRADIENTS.length]
}
