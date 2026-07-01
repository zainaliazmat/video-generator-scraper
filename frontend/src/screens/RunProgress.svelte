<script>
  import { onMount, onDestroy } from 'svelte'
  import { state } from '../lib/store.js'
  import { cancelJob } from '../lib/api.js'
  import { autoscroll } from '../lib/ui.js'
  import { computeProgress, estimateTimeLeft, STEPS } from '../lib/progress.js'

  let now = Date.now()
  const tick = setInterval(() => { now = Date.now() }, 1000)
  onDestroy(() => clearInterval(tick))

  $: p = computeProgress($state.progress)
  $: elapsedMs = $state.runStartMs ? now - $state.runStartMs : 0
  $: leftMs = estimateTimeLeft(p.pct, elapsedMs, p.phaseIndex)

  const fmtClock = (ms) => {
    const s = Math.round(ms / 1000)
    const m = Math.floor(s / 60)
    return `${m}:${String(s % 60).padStart(2, '0')}`
  }

  async function cancel() {
    state.update(s => ({ ...s, cancelling: true }))
    await cancelJob($state.jobId)
  }
</script>

<div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:26px 28px">
  <!-- header: phase + cancel -->
  <div style="display:flex;align-items:center;gap:13px">
    <span style="display:inline-block;width:26px;height:26px;flex:none;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
    <div style="flex:1;min-width:0">
      <div style="font-weight:600;color:#1B1D21">{p.phase}…</div>
      <div style="font-size:.84rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{$state.progress.length ? $state.progress[$state.progress.length - 1] : 'Starting the scrape…'}</div>
    </div>
    <button on:click={cancel} disabled={$state.cancelling} style="flex:none;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:8px 16px;font-weight:600;font-size:.84rem;color:#1B1D21;cursor:pointer">{$state.cancelling ? 'Cancelling…' : 'Cancel run'}</button>
  </div>

  <!-- phase stepper -->
  <div style="display:flex;gap:8px;margin-top:18px;flex-wrap:wrap">
    {#each STEPS as label, i}
      {@const done = i < p.phaseIndex}
      {@const active = i === p.phaseIndex}
      <div style="flex:1;min-width:130px;border-radius:12px;padding:10px 12px;border:1.5px solid {active ? '#121316' : '#E7EBEF'};background:{done ? '#F1FAF4' : (active ? '#fff' : '#FBFCFE')}">
        <div style="display:flex;align-items:center;gap:7px">
          <span style="width:18px;height:18px;flex:none;border-radius:50%;display:flex;align-items:center;justify-content:center;background:{done ? '#DFF6EA' : (active ? '#121316' : '#E7EBEF')};color:{done ? '#1E7A4D' : '#fff'};font-size:.66rem;font-weight:700">{#if done}<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>{:else}{i + 1}{/if}</span>
          <span style="font-size:.76rem;font-weight:600;color:{active || done ? '#1B1D21' : '#8A93A0'}">{label}</span>
        </div>
      </div>
    {/each}
  </div>

  <!-- progress bar -->
  <div style="margin-top:16px;height:7px;border-radius:999px;background:#EEF1F4;overflow:hidden">
    <div style="height:100%;border-radius:999px;background:#121316;width:{p.pct}%;transition:width .4s ease"></div>
  </div>

  <!-- counters -->
  <div style="display:flex;gap:22px;margin-top:14px;flex-wrap:wrap">
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Videos</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{p.videos}</div></div>
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Channels</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{p.channels}{#if p.totalChannels}/{p.totalChannels}{/if}</div></div>
    <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Elapsed</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">{fmtClock(elapsedMs)}</div></div>
    {#if leftMs !== null}
      <div><div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0">Time left</div><div style="font-weight:700;font-size:1.05rem;color:#1B1D21">~{fmtClock(leftMs)}</div></div>
    {/if}
  </div>

  <!-- live feed -->
  <div style="font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8A93A0;margin:18px 0 7px">Live feed</div>
  <div use:autoscroll style="background:#0E1116;border-radius:12px;padding:14px 16px;height:200px;overflow:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.7;color:#C7D0DA">
    {#each $state.progress as line}
      <div><span style="color:#4B5563">$</span> <span style="color:{line.includes('FAILED') ? '#F0A0A0' : (line.includes('Cancelled') ? '#F0C674' : '#9ED4F8')}">{line}</span></div>
    {/each}
    <div style="color:#5B6675">▌</div>
  </div>
</div>
