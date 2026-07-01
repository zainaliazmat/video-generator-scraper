<script>
  import { onMount } from 'svelte'
  import { state } from '../lib/store.js'
  import { getHistory, startPredict, watchPredict } from '../lib/api.js'
  import { autoscroll } from '../lib/ui.js'
  import { fmtDate } from '../lib/fmt.js'

  const goHub = () => state.update(s => ({ ...s, view: 'hub' }))

  let dragOver = false
  let fileError = ''            // client-side drop rejection

  const REASONS = {
    cli_missing: { title: "AI prediction needs the Claude CLI", body: "Install it and log in with your Claude subscription, then retry:" },
    not_logged_in: { title: "Claude isn’t logged in", body: "Log in with your Claude subscription, then retry:" },
    parse_failed: { title: "Couldn’t read a prediction from this data", body: "The model didn’t return a usable result. Try again." },
    no_breakout_data: { title: "This file has no breakout data", body: "Prediction reads views ÷ subscribers. This TSV has no subscriber counts (a Fast-mode export), so there’s nothing to analyse." },
    empty: { title: "That file is empty", body: "Pick a snapshot or drop a TSV that has rows in it." },
    bad_columns: { title: "That doesn’t look like a results TSV", body: "Export a snapshot from YouTube Content Research, or drop a tab-separated file with a subscribers column." },
    too_large: { title: "That file is too large", body: "The limit is 10 MB. Pick a snapshot from history instead." },
    error: { title: "Couldn’t generate a prediction", body: "Something went wrong talking to Claude. Try again." },
  }
  $: reason = $state.ai && (REASONS[$state.ai.reason] || REASONS.error)
  $: needsCli = $state.ai && ($state.ai.reason === 'cli_missing' || $state.ai.reason === 'not_logged_in')
  $: canPredict = !!$state.source && $state.aiState !== 'loading'

  onMount(loadHistory)

  async function loadHistory() {
    state.update(s => ({ ...s, historyState: 'loading' }))
    try {
      const { snapshots } = await getHistory()
      state.update(s => ({ ...s, history: snapshots, historyState: 'idle' }))
    } catch (_) {
      state.update(s => ({ ...s, historyState: 'error' }))
    }
  }

  function pickHistory(item) {
    fileError = ''
    state.update(s => ({ ...s, source: { kind: 'history', file: item.file, label: `${fmtDate(item.date)} · ${item.count} videos` } }))
  }

  function onFiles(fileList) {
    const f = fileList && fileList[0]
    if (!f) return
    if (!f.name.toLowerCase().endsWith('.tsv')) { fileError = "That's not a .tsv file."; return }
    if (f.size > 10 * 1024 * 1024) { fileError = 'That file is larger than 10 MB.'; return }
    fileError = ''
    state.update(s => ({ ...s, source: { kind: 'file', file: f, label: f.name } }))
  }

  function onDrop(e) {
    e.preventDefault(); dragOver = false
    onFiles(e.dataTransfer.files)
  }

  const clearSource = () => state.update(s => ({ ...s, source: null }))

  function run() {
    if (!canPredict) return
    const source = $state.source
    state.update(s => ({ ...s, aiState: 'loading', ai: null, predictLog: '' }))
    startPredict(source).then(({ job_id }) => {
      state.update(s => ({ ...s, jobId: job_id }))
      watchPredict(job_id,
        (chunk) => state.update(s => ({ ...s, predictLog: s.predictLog + chunk })),
        (pred) => {
          if (pred && pred.ok) state.update(s => ({ ...s, aiState: 'done', ai: pred }))
          else state.update(s => ({ ...s, aiState: 'error', ai: pred || { reason: 'error' } }))
        })
    }).catch((e) => {
      state.update(s => ({ ...s, aiState: 'error', ai: { reason: e.message || 'error' } }))
    })
  }

  // Regenerate reuses the existing synthetic job (rows already held there).
  function regenerate() {
    if (!$state.jobId) return run()
    state.update(s => ({ ...s, aiState: 'loading', ai: null, predictLog: '' }))
    watchPredict($state.jobId,
      (chunk) => state.update(s => ({ ...s, predictLog: s.predictLog + chunk })),
      (pred) => {
        if (pred && pred.ok) state.update(s => ({ ...s, aiState: 'done', ai: pred }))
        else state.update(s => ({ ...s, aiState: 'error', ai: pred || { reason: 'error' } }))
      })
  }
</script>

<div style="max-width:960px;margin:0 auto;padding:30px 24px 60px">
  <a on:click={goHub} style="display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:600;color:#5C6470;margin-bottom:14px;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>All tools</a>
  <h1 style="margin:0;font-weight:600;font-size:1.85rem;letter-spacing:-.025em;color:#1B1D21">AI Prediction</h1>
  <p style="margin:9px 0 0;color:#5C6470;font-size:.96rem;max-width:56ch">Pick a saved research snapshot, or drop a TSV export, and predict your next video.</p>

  {#if $state.aiState === 'idle' || (!$state.ai && $state.aiState !== 'loading')}
    <!-- SOURCE PICKER: history primary, upload secondary -->
    <div style="display:grid;grid-template-columns:1.6fr 1fr;gap:16px;margin-top:22px">
      <!-- history (primary) -->
      <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:20px 22px">
        <div style="font-weight:600;font-size:1rem;color:#1B1D21;margin-bottom:12px">Your snapshots</div>
        {#if $state.historyState === 'loading'}
          <div style="color:#8A93A0;font-size:.88rem;padding:18px 0">Loading history…</div>
        {:else if $state.historyState === 'error'}
          <div style="font-size:.88rem;color:#B23B3B">Couldn't load history. <a on:click={loadHistory} style="color:#1B1D21;font-weight:600;cursor:pointer;text-decoration:underline">Retry</a></div>
        {:else if $state.history.length === 0}
          <div style="color:#8A93A0;font-size:.9rem;line-height:1.55;padding:10px 0">No snapshots yet — run YouTube Content Research, or drop a TSV on the right.</div>
        {:else}
          <div style="display:flex;flex-direction:column;gap:8px;max-height:340px;overflow:auto">
            {#each $state.history as item (item.file)}
              {@const active = $state.source && $state.source.kind === 'history' && $state.source.file === item.file}
              <div on:click={() => pickHistory(item)} role="button" tabindex="0"
                style="cursor:pointer;border-radius:12px;padding:12px 14px;border:1.5px solid {active ? '#121316' : '#E7EBEF'};background:{active ? '#fff' : '#FBFCFE'}">
                <div style="font-weight:600;font-size:.9rem;color:#1B1D21">{fmtDate(item.date)} · {item.count} videos</div>
                <div style="font-size:.76rem;color:#8A93A0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{item.keywords.slice(0, 4).join(', ')}{item.keywords.length > 4 ? ` +${item.keywords.length - 4}` : ''}</div>
              </div>
            {/each}
          </div>
        {/if}
      </div>

      <!-- upload (secondary) -->
      <div>
        <label
          on:dragover|preventDefault={() => dragOver = true}
          on:dragleave={() => dragOver = false}
          on:drop={onDrop}
          style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;height:100%;min-height:160px;cursor:pointer;border-radius:18px;border:2px dashed {dragOver ? '#121316' : '#CBD5E1'};background:{dragOver ? '#F2F6FF' : '#FBFCFE'};padding:22px">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#8A93A0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 16V4M7 9l5-5 5 5M5 20h14"/></svg>
          <span style="font-size:.86rem;font-weight:600;color:#1B1D21">Drop a .tsv here</span>
          <span style="font-size:.76rem;color:#8A93A0">or click to browse</span>
          <input type="file" accept=".tsv" on:change={(e) => onFiles(e.target.files)} style="display:none">
        </label>
        {#if fileError}<p style="margin:8px 2px 0;font-size:.8rem;color:#B23B3B;font-weight:600">{fileError}</p>{/if}
      </div>
    </div>

    <!-- active source chip + predict -->
    <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:18px;flex-wrap:wrap">
      <div style="min-height:34px;display:flex;align-items:center">
        {#if $state.source}
          <span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:7px 8px 7px 14px;font-weight:600;font-size:.84rem;color:#1B1D21">
            {$state.source.label}
            <button on:click={clearSource} title="Clear" style="width:20px;height:20px;border:none;border-radius:50%;background:#F2F4F6;color:#5C6470;cursor:pointer;display:flex;align-items:center;justify-content:center"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
          </span>
        {:else}
          <span style="font-size:.84rem;color:#8A93A0">Pick a snapshot or drop a TSV to enable Predict.</span>
        {/if}
      </div>
      <button on:click={run} disabled={!canPredict} style="display:inline-flex;align-items:center;gap:8px;background:#121316;color:#fff;border:none;border-radius:999px;padding:11px 20px;font-weight:600;font-size:.88rem;cursor:{canPredict ? 'pointer' : 'not-allowed'};opacity:{canPredict ? 1 : .45};box-shadow:0 8px 20px rgba(18,19,22,.25)">Predict <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></button>
    </div>

  {:else if $state.aiState === 'loading'}
    <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:26px 28px;margin-top:22px">
      <div style="display:flex;align-items:center;gap:13px">
        <span style="display:inline-block;width:26px;height:26px;flex:none;border-radius:50%;border:3px solid #E7EBEF;border-top-color:#121316;animation:spin .8s linear infinite"></span>
        <div>
          <div style="font-weight:600;color:#1B1D21">Analysing your snapshot…</div>
          <div style="font-size:.84rem;color:#8A93A0">Live output from Claude as it reads your data</div>
        </div>
      </div>
      <div use:autoscroll style="margin-top:16px;background:#0E1116;border-radius:12px;padding:16px 18px;height:300px;overflow:auto;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.78rem;line-height:1.65;color:#C7D0DA;white-space:pre-wrap;word-break:break-word">{$state.predictLog || 'starting…'}<span style="color:#5B6675">▌</span></div>
    </div>

  {:else if $state.aiState === 'error'}
    <div style="background:#fff;border:1px solid #F3D3D3;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:34px;margin-top:22px">
      <div style="font-weight:700;font-size:1.05rem;color:#B23B3B">{reason.title}</div>
      <p style="margin:8px 0 0;font-size:.9rem;color:#5C6470;line-height:1.55">{reason.body}</p>
      {#if needsCli}
        <pre style="margin:12px 0 0;background:#F7F8FA;border:1px solid #E7EBEF;border-radius:10px;padding:12px 14px;font-size:.8rem;color:#1B1D21;white-space:pre-wrap">npm install -g @anthropic-ai/claude-code
claude        # then /login</pre>
      {/if}
      <button on:click={() => state.update(s => ({ ...s, aiState: 'idle', ai: null }))} style="margin-top:16px;background:#121316;color:#fff;border:none;border-radius:999px;padding:10px 17px;font-weight:600;font-size:.85rem;cursor:pointer">Choose another source</button>
    </div>

  {:else if $state.ai}
    {@const ai = $state.ai}
    <div style="animation:fadeup .4s ease;margin-top:22px">
      <div style="background:#121316;border-radius:22px;padding:30px 32px;color:#fff;position:relative;overflow:hidden">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap">
          <div style="font-size:.68rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#9ED4F8">Predicted next video</div>
          <span style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,255,255,.12);color:#fff;border-radius:999px;padding:6px 13px;font-weight:700;font-size:.8rem">est. breakout ×<b style="color:#9ED4F8">{ai.est}</b></span>
        </div>
        <h2 style="margin:14px 0 0;font-weight:600;font-size:1.72rem;letter-spacing:-.02em;line-height:1.18;color:#fff;max-width:24ch">{ai.topic}</h2>
        <p style="margin:14px 0 0;color:#C7CDD4;font-size:.96rem;line-height:1.6;max-width:64ch">{ai.rationale}</p>
        {#if ai.angle}
        <div style="display:inline-flex;align-items:flex-start;gap:9px;margin-top:18px;background:rgba(207,234,255,.12);border:1px solid rgba(158,212,248,.3);border-radius:12px;padding:12px 15px;max-width:64ch">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#9ED4F8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex:none;margin-top:1px"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg>
          <span style="font-size:.88rem;color:#E7EBEF;line-height:1.5">{ai.angle}</span>
        </div>
        {/if}
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px">
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">Why this will work</h3>
          <div style="display:flex;flex-direction:column;gap:13px">
            {#each ai.evidence as e}
              <div style="display:flex;gap:11px"><span style="flex:none;width:23px;height:23px;border-radius:50%;background:#DFF6EA;color:#1E7A4D;display:flex;align-items:center;justify-content:center;margin-top:1px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span style="font-size:.87rem;color:#5C6470;line-height:1.5">{e}</span></div>
            {/each}
          </div>
        </div>
        <div style="background:#fff;border:1px solid #E7EBEF;border-radius:18px;box-shadow:0 1px 2px rgba(18,19,22,.05),0 8px 22px rgba(18,19,22,.06);padding:22px 24px">
          <h3 style="font-weight:600;font-size:1.04rem;color:#1B1D21;margin:0 0 14px">More ideas to test</h3>
          <div style="display:flex;flex-direction:column;gap:10px">
            {#each ai.ideas as idea}
              <div style="display:flex;align-items:center;gap:12px;background:#FBFCFE;border:1px solid #E7EBEF;border-radius:12px;padding:11px 13px"><span style="flex:1;font-weight:600;font-size:.86rem;color:#1B1D21;line-height:1.35">{idea.title}</span>{#if idea.est}<span style="flex:none;display:inline-flex;align-items:center;background:#121316;color:#fff;font-weight:700;font-size:.74rem;padding:4px 9px;border-radius:999px">×<b style="color:#9ED4F8">{idea.est}</b></span>{/if}</div>
            {/each}
          </div>
        </div>
      </div>
      <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:18px;flex-wrap:wrap">
        <button on:click={() => state.update(s => ({ ...s, aiState: 'idle', ai: null, source: null }))} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:9px 16px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer">Predict another</button>
        <button on:click={regenerate} style="display:inline-flex;align-items:center;gap:8px;background:#fff;border:1.5px solid #E7EBEF;border-radius:999px;padding:9px 16px;font-weight:600;font-size:.85rem;color:#1B1D21;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8M21 4v4h-4"/></svg>Regenerate</button>
      </div>
    </div>
  {/if}
</div>
