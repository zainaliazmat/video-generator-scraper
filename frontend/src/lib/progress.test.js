import { describe, it, expect } from 'vitest'
import { computeProgress, estimateTimeLeft, STEPS } from './progress.js'

describe('computeProgress', () => {
  it('counts videos from search-phase lines and reaches phase 1', () => {
    const r = computeProgress([
      '[1/2] Searching "ai tools" ...',
      '[1/2] ai tools — 30 videos',
      '[2/2] Searching "ml" ...',
      '[2/2] ml — 20 videos',
    ])
    expect(r.videos).toBe(50)
    expect(r.phaseIndex).toBe(1)
    expect(r.phase).toBe(STEPS[1])
  })

  it('tracks channel lookups as phase 2 with channel counts', () => {
    const r = computeProgress([
      'Looking up 12 channels for subscriber counts + topics ...',
      '[3/12] Some Channel ... ok',
    ])
    expect(r.phaseIndex).toBe(2)
    expect(r.channels).toBe(3)
    expect(r.totalChannels).toBe(12)
  })

  it('derives pct from the most recent [i/n] marker', () => {
    const r = computeProgress(['[1/2] Searching "a" ...', '[1/4] X ... ok'])
    expect(r.pct).toBe(25)
  })
})

describe('estimateTimeLeft', () => {
  it('returns null before the first phase or with too little signal', () => {
    expect(estimateTimeLeft(0, 1000, 0)).toBeNull()
    expect(estimateTimeLeft(5, 1000, 1)).toBeNull()   // pct < 10
    expect(estimateTimeLeft(100, 1000, 2)).toBeNull() // done
  })
  it('extrapolates once past the first phase', () => {
    // 25% took 10s -> total ~40s -> ~30s left
    expect(estimateTimeLeft(25, 10000, 2)).toBe(30000)
  })
})
