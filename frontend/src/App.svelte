<script>
  import { onMount } from 'svelte'
  import { state, lastJob, rememberJob } from './lib/store.js'
  import { getStatus, getResults } from './lib/api.js'
  import Hub from './screens/Hub.svelte'
  import Input from './screens/Input.svelte'
  import Results from './screens/Results.svelte'
  import Predict from './screens/Predict.svelte'

  const goHub = () => state.update(s => ({ ...s, view: 'hub' }))

  // R3: on load, try to reattach to a previous run.
  onMount(async () => {
    const id = lastJob()
    if (!id) return
    try {
      const s = await getStatus(id)
      if (s.status === 'running') {
        state.update(v => ({ ...v, view: 'results', running: true, jobId: id, progress: s.progress || [] }))
      } else if (s.status === 'done' || s.status === 'cancelled') {
        const res = await getResults(id)
        state.update(v => ({ ...v, view: 'results', jobId: id, rows: res.rows, fast: res.fast,
          date: res.date, keywords: res.keywords,
          failedNote: res.cancelled ? 'Run was cancelled — partial data shown.' : '' }))
      } else { rememberJob(null) }
    } catch (_) { rememberJob(null) }
  })
</script>

<div style="min-height:100vh;background:linear-gradient(180deg,#DCF1FF 0%,#EFF8FF 380px,#FFFFFF 820px)">
  <nav style="position:sticky;top:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:14px 30px;background:rgba(223,241,255,.74);backdrop-filter:blur(14px);border-bottom:1px solid rgba(255,255,255,.6)">
    <a on:click={goHub} style="display:flex;align-items:center;gap:10px;cursor:pointer">
      <span style="width:36px;height:36px;border-radius:50%;background:#121316;display:flex;align-items:center;justify-content:center;flex:none"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h3l2.5-7 5 16 2.5-9H21"/></svg></span>
      <span style="line-height:1.04"><strong style="display:block;font-weight:700;font-size:1.06rem;color:#1B1D21">Signal</strong><small style="font-size:.54rem;font-weight:700;letter-spacing:.34em;color:#5C6470;text-transform:uppercase">Toolkit</small></span>
    </a>
    <div style="display:flex;gap:24px;align-items:center">
      <a on:click={goHub} style="font-weight:600;font-size:.9rem;color:#1B1D21;cursor:pointer">Tools</a>
      <a style="font-weight:500;font-size:.9rem;color:#5C6470;cursor:pointer">Docs</a>
      <a style="font-weight:500;font-size:.9rem;color:#5C6470;cursor:pointer">Changelog</a>
      <span style="display:inline-flex;align-items:center;gap:7px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:8px 15px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer">Feedback</span>
    </div>
  </nav>

  {#if $state.view === 'hub'}
    <Hub />
  {:else if $state.view === 'input'}
    <Input />
  {:else if $state.view === 'results'}
    <Results />
  {:else if $state.view === 'predict'}
    <Predict />
  {/if}
</div>
