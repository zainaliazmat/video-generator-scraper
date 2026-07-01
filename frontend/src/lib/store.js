import { writable, derived } from 'svelte/store'

const LS_MODE = 'voyara.mode'
const LS_JOB = 'voyara.jobId'

const savedMode = (typeof localStorage !== 'undefined' && localStorage.getItem(LS_MODE)) || null

export const state = writable({
  view: 'hub',                 // hub | input | results | predict
  // input
  urls: 'https://www.youtube.com/results?search_query=best+ai+tools\nhow to make money with ai',
  perLink: '60 videos',
  dateFilter: 'Any time',
  mode: savedMode,             // null = not chosen yet | 'fast' | 'full'
  cookies: 'off',
  // run
  jobId: null,
  running: false,
  cancelling: false,
  progress: [],
  runStartMs: 0,               // Date.now() when the scrape started (for time-left)
  error: null,
  // results
  rows: [],
  fast: false,
  date: '',
  keywords: [],
  failedNote: '',
  sort: 'breakout',
  keyword: 'all',
  verifiedOnly: false,
  query: '',
  page: 1,
  // predict tool (standalone)
  history: [],                 // [{file,date,count,keywords}]
  historyState: 'idle',        // idle | loading | error
  source: null,                // {kind:'file',file:File,label} | {kind:'history',file,label}
  aiState: 'idle',             // idle | loading | done | error
  ai: null,
  predictLog: '',              // streamed Claude text (live AI session)
})

export function persistMode(mode) {
  try { localStorage.setItem(LS_MODE, mode) } catch (_) {}
}
export function rememberJob(id) {
  try { id ? localStorage.setItem(LS_JOB, id) : localStorage.removeItem(LS_JOB) } catch (_) {}
}
export function lastJob() {
  try { return localStorage.getItem(LS_JOB) } catch (_) { return null }
}

const PAGE_SIZE = 50

const keyFns = {
  breakout: v => v.breakout ?? -1,
  views: v => v.views ?? 0,
  likes: v => v.likes ?? 0,
  comments: v => v.comments ?? 0,
  newest: v => Date.parse(v.upload_date || 0) || 0,
  longest: v => v.duration_sec ?? 0,
}

// Filtered + sorted rows (before paging).
export const filteredRows = derived(state, ($s) => {
  let r = $s.rows.slice()
  if ($s.keyword !== 'all') r = r.filter(v => v.keyword === $s.keyword)
  if ($s.verifiedOnly) r = r.filter(v => v.verified)
  const q = $s.query.trim().toLowerCase()
  if (q) r = r.filter(v => (`${v.title} ${v.channel}`).toLowerCase().includes(q))
  const k = keyFns[$s.sort] || keyFns.views
  return r.sort((a, b) => k(b) - k(a))
})

// Page slice for the table.
export const pagedRows = derived([state, filteredRows], ([$s, $rows]) => {
  if ($rows.length <= PAGE_SIZE) return $rows
  const start = ($s.page - 1) * PAGE_SIZE
  return $rows.slice(start, start + PAGE_SIZE)
})

export const pageInfo = derived([state, filteredRows], ([$s, $rows]) => ({
  total: $rows.length,
  pages: Math.max(1, Math.ceil($rows.length / PAGE_SIZE)),
  page: $s.page,
  showPager: $rows.length > PAGE_SIZE,
}))
