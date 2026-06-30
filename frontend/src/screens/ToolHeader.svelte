<script>
  import { state } from '../lib/store.js'
  import { chip } from '../lib/ui.js'
  const goInput = () => state.update(s => ({ ...s, view: 'input' }))
  const goResults = () => state.update(s => ({ ...s, view: 'results' }))
  const goAi = () => state.update(s => ({ ...s, view: 'ai' }))
</script>

<a on:click={goInput} style="display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:600;color:#5C6470;margin-bottom:14px;cursor:pointer"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>New run</a>
<h1 style="margin:0 0 16px;font-weight:600;font-size:1.85rem;letter-spacing:-.025em;color:#1B1D21">YouTube Content Research</h1>
<div style="display:flex;gap:9px;margin-bottom:22px">
  <button on:click={goResults} style={chip($state.view === 'results')}><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 4v16"/></svg>Results</button>
  <button on:click={goAi} style={chip($state.view === 'ai')}><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 4.7L18.5 9l-4.7 1.8L12 15.5l-1.8-4.7L5.5 9l4.7-1.3L12 3z"/></svg>AI prediction</button>
</div>
