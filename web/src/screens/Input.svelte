<script>
  import { state, persistMode, rememberJob } from '../lib/store.js'
  import { startRun, watchJob, getResults } from '../lib/api.js'

  const goHub = () => state.update(s => ({ ...s, view: 'hub' }))
  const setMode = (m) => { persistMode(m); state.update(s => ({ ...s, mode: m })) }

  $: lines = $state.urls.split('\n').map(x => x.trim()).filter(Boolean)
  $: perN = parseInt($state.perLink, 10) || 60
  $: estTotal = lines.length * perN
  $: fullMins = Math.max(1, Math.ceil(estTotal / 30))   // ~30 videos/min incl. channel lookups
  $: canRun = !!$state.mode && lines.length > 0

  async function run() {
    if (!canRun) return
    const full = $state.mode === 'full'
    if (full && !confirm(`This full breakout scrape of ~${estTotal} videos can take ~${fullMins} min. Start?`)) return

    let job
    try {
      job = await startRun({
        inputs: $state.urls, per_link: $state.perLink, date_filter: $state.dateFilter,
        fast: !full, cookies: $state.cookies === 'off' ? null : $state.cookies,
      })
    } catch (e) {
      state.update(s => ({ ...s, error: e.status === 409
        ? 'A scrape is already running. Wait for it to finish.'
        : (e.message || 'Could not start the run.') }))
      return
    }
    rememberJob(job.job_id)
    state.update(s => ({ ...s, view: 'results', running: true, cancelling: false,
      jobId: job.job_id, progress: [], error: null, rows: [], ai: null, aiState: 'idle' }))

    watchJob(job.job_id, async (evt) => {
      if (evt.type === 'progress') {
        state.update(s => ({ ...s, progress: [...s.progress, evt.message] }))
      } else if (evt.type === 'done' || evt.type === 'cancelled') {
        try {
          const res = await getResults(job.job_id)
          state.update(s => ({ ...s, running: false, rows: res.rows, fast: res.fast,
            date: res.date, keywords: res.keywords,
            failedNote: evt.type === 'cancelled' ? 'Run was cancelled — partial data shown.' : '',
            sort: res.fast ? 'views' : 'breakout' }))
        } catch (e) {
          state.update(s => ({ ...s, running: false, error: e.message }))
        }
      } else if (evt.type === 'error') {
        state.update(s => ({ ...s, running: false, error: evt.message || 'The run failed.' }))
      } else {
        state.update(s => ({ ...s, running: false }))
      }
    })
  }
</script>

<div style="max-width:700px;margin:0 auto;padding:34px 24px 70px">
  <a on:click={goHub} style="display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:600;color:#5C6470;margin-bottom:18px;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>All tools</a>
  <h1 style="margin:0;font-weight:600;font-size:2rem;letter-spacing:-.025em;color:#1B1D21;line-height:1.12">YouTube Content Research</h1>
  <p style="margin:10px 0 0;color:#5C6470;font-size:.98rem;max-width:56ch">Paste YouTube search URLs or plain keywords — one per line. We'll pull the top results from each and build a table you can sort, analyse with AI, and download.</p>

  <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:24px;margin-top:26px">
    <label style="display:flex;align-items:baseline;justify-content:space-between;font-size:.8rem;font-weight:700;color:#1B1D21;margin-bottom:8px">Search URLs or keywords<span style="font-weight:500;color:#8A93A0">one per line</span></label>
    <textarea rows="6" spellcheck="false" bind:value={$state.urls} style="width:100%;border:1.5px solid #E7EBEF;border-radius:12px;padding:13px 15px;font-family:ui-monospace,Menlo,monospace;font-size:.84rem;color:#1B1D21;resize:vertical;outline:none;line-height:1.75;background:#FBFCFE"></textarea>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:16px">
      <div style="background:#FBFCFE;border:1.5px solid #E7EBEF;border-radius:12px;padding:10px 14px 9px">
        <label style="display:block;font-size:.74rem;font-weight:700;color:#1B1D21;margin-bottom:3px">Results per link</label>
        <select bind:value={$state.perLink} style="width:100%;border:none;background:none;outline:none;font-size:.92rem;font-weight:600;color:#1B1D21;cursor:pointer"><option>30 videos</option><option>60 videos</option><option>90 videos</option><option>120 videos</option></select>
      </div>
      <div style="background:#FBFCFE;border:1.5px solid #E7EBEF;border-radius:12px;padding:10px 14px 9px">
        <label style="display:block;font-size:.74rem;font-weight:700;color:#1B1D21;margin-bottom:3px">Date filter</label>
        <select bind:value={$state.dateFilter} style="width:100%;border:none;background:none;outline:none;font-size:.92rem;font-weight:600;color:#1B1D21;cursor:pointer"><option>Any time</option><option>This year</option><option>This month</option><option>This week</option></select>
      </div>
    </div>

    <!-- R5: explicit mode choice, no silent default -->
    <div style="margin-top:16px">
      <label style="display:block;font-size:.74rem;font-weight:700;color:#1B1D21;margin-bottom:8px">Choose a mode</label>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
        <div on:click={() => setMode('fast')} role="button" tabindex="0"
          style="cursor:pointer;border-radius:12px;padding:13px 15px;border:1.5px solid {$state.mode==='fast' ? '#121316' : '#E7EBEF'};background:{$state.mode==='fast' ? '#fff' : '#FBFCFE'}">
          <div style="font-weight:700;font-size:.9rem;color:#1B1D21">Fast — titles & views</div>
          <div style="font-size:.78rem;color:#8A93A0;margin-top:3px">seconds · no breakout or AI prediction</div>
        </div>
        <div on:click={() => setMode('full')} role="button" tabindex="0"
          style="cursor:pointer;border-radius:12px;padding:13px 15px;border:1.5px solid {$state.mode==='full' ? '#121316' : '#E7EBEF'};background:{$state.mode==='full' ? '#fff' : '#FBFCFE'}">
          <div style="font-weight:700;font-size:.9rem;color:#1B1D21">Full — breakout + AI</div>
          <div style="font-size:.78rem;color:#8A93A0;margin-top:3px">≈ ~{fullMins} min · the full product</div>
        </div>
      </div>
    </div>

    <!-- R10: cookies control for bot-checks -->
    <div style="display:flex;align-items:center;gap:10px;margin-top:14px">
      <span style="font-size:.84rem;font-weight:600;color:#1B1D21">Use browser login</span>
      <select bind:value={$state.cookies} style="border:1.5px solid #E7EBEF;border-radius:10px;padding:6px 10px;font-size:.82rem;font-weight:600;color:#1B1D21;background:#FBFCFE;cursor:pointer"><option value="off">Off</option><option value="chrome">Chrome</option><option value="firefox">Firefox</option><option value="edge">Edge</option><option value="brave">Brave</option></select>
      <span style="font-size:.78rem;color:#8A93A0">— turn on if YouTube shows a bot-check</span>
    </div>

    {#if $state.error}
      <p style="margin:14px 0 0;font-size:.84rem;color:#B23B3B;font-weight:600">{$state.error}</p>
    {/if}

    <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:22px;padding-top:20px;border-top:1px solid #F2F4F6">
      <span style="font-size:.84rem;color:#5C6470"><b style="color:#1B1D21">{lines.length} links</b> × {perN} results ≈ <b style="color:#1B1D21">{estTotal} videos</b>{#if $state.mode==='full'} · ~{fullMins} min{/if}</span>
      <button on:click={run} disabled={!canRun} style="display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;border:none;border-radius:999px;padding:11px 19px;font-weight:600;font-size:.88rem;cursor:{canRun ? 'pointer' : 'not-allowed'};opacity:{canRun ? 1 : .45};box-shadow:0 8px 20px rgba(18,19,22,.25)">Run research <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></button>
    </div>
  </div>
  <p style="margin:16px 2px 0;font-size:.82rem;color:#8A93A0">Each run is saved as a dated snapshot, so you can re-run weekly and see what changed.{#if !$state.mode} Pick a mode to start.{/if}</p>
</div>
