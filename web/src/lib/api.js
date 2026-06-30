// Thin fetch + SSE helpers around the FastAPI backend.

async function jsonOrThrow(r) {
  if (!r.ok) {
    let detail = `${r.status}`
    try { detail = (await r.json()).detail || detail } catch (_) {}
    const err = new Error(detail)
    err.status = r.status
    throw err
  }
  return r.json()
}

export async function startRun(params) {
  return jsonOrThrow(await fetch('/api/run', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  }))
}

export async function getStatus(jobId) {
  return jsonOrThrow(await fetch(`/api/jobs/${jobId}`))
}

export async function getResults(jobId) {
  return jsonOrThrow(await fetch(`/api/jobs/${jobId}/results`))
}

export async function cancelJob(jobId) {
  return fetch(`/api/jobs/${jobId}/cancel`, { method: 'POST' })
}

export const downloadUrl = (jobId) => `/api/jobs/${jobId}/download`

// Streaming AI prediction. onText(chunk) fires as Claude writes; onResult(pred)
// fires once with the parsed prediction (or {ok:false,...}).
export async function watchPredict(jobId, onText, onResult) {
  await fetch(`/api/jobs/${jobId}/predict-start`, { method: 'POST' })
  const es = new EventSource(`/api/jobs/${jobId}/predict-events`)
  es.onmessage = (e) => {
    let evt
    try { evt = JSON.parse(e.data) } catch (_) { return }
    if (evt.type === 'text') onText(evt.chunk)
    else if (evt.type === 'result') { es.close(); onResult(evt.prediction) }
  }
  es.onerror = () => {}  // let it retry; the result frame closes it
  return () => es.close()
}

// Live progress. onEvent receives {type, message?, count?}. Completion is also
// guaranteed via a status poll (R2) so a dropped/late SSE never strands the UI.
export function watchJob(jobId, onEvent) {
  let settled = false
  const finish = (evt) => {
    if (settled) return
    settled = true
    es && es.close()
    clearInterval(poll)
    onEvent(evt)
  }
  const es = new EventSource(`/api/jobs/${jobId}/events`)
  es.onmessage = (e) => {
    let evt
    try { evt = JSON.parse(e.data) } catch (_) { return }
    if (evt.type === 'progress') onEvent(evt)
    else finish(evt)            // done | error | cancelled
  }
  // Do NOT permanently close on error — EventSource auto-reconnects, and the
  // poll below is the real safety net.
  const poll = setInterval(async () => {
    try {
      const s = await getStatus(jobId)
      if (['done', 'error', 'cancelled'].includes(s.status)) {
        finish({ type: s.status, count: s.count, message: s.error })
      }
    } catch (_) {}
  }, 2000)
  return () => finish({ type: 'closed' })
}
