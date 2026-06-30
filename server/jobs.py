"""Background scrape jobs.

The web layer runs at most ONE scrape at a time (serialized) so the scraper's
module-global config is never clobbered by overlapping runs. Each Job buffers
progress lines and a terminal event for the SSE/poll endpoints to drain.
"""
import queue
import threading
import uuid
from collections import OrderedDict

BOTCHECK_MSG = (
    "No videos were returned. This usually means a YouTube bot-check "
    "(turn on 'Use browser login' above and re-run) — or yt-dlp is out of date "
    "(run ./run.sh --update), or no results matched your search."
)


class JobBusyError(Exception):
    """Raised when a scrape is started while another is still running."""


class Job:
    def __init__(self, job_id, params):
        self.id = job_id
        self.params = params
        self.status = "pending"   # pending | running | done | error | cancelled
        self.rows = []
        self.error = None
        self.cancelled = False
        self.progress = []
        self.events = queue.Queue()      # drained by the SSE endpoint

    def add_progress(self, msg):
        self.progress.append(msg)
        self.events.put({"type": "progress", "message": msg})


class JobManager:
    def __init__(self, max_jobs=10):
        self._jobs = OrderedDict()
        self._lock = threading.Lock()
        self._running = False
        self._max_jobs = max_jobs

    def create(self, params):
        job = Job(uuid.uuid4().hex[:12], params)
        with self._lock:
            self._jobs[job.id] = job
            while len(self._jobs) > self._max_jobs:
                self._jobs.popitem(last=False)   # evict oldest
        return job

    def get(self, job_id):
        return self._jobs.get(job_id)

    def is_running(self):
        with self._lock:
            return self._running

    def cancel(self, job_id):
        job = self.get(job_id)
        if job:
            job.cancelled = True
        return job

    def run(self, job, scrape_fn):
        """Synchronous core — unit-testable. The HTTP layer runs it in a thread."""
        job.status = "running"
        try:
            rows = scrape_fn(progress=job.add_progress,
                             should_cancel=lambda: job.cancelled)
            if job.cancelled:
                job.rows = rows or []
                job.status = "cancelled"
                job.events.put({"type": "cancelled", "count": len(job.rows)})
            elif not rows:
                job.status = "error"
                job.error = BOTCHECK_MSG
                job.events.put({"type": "error", "message": job.error})
            else:
                job.rows = rows
                job.status = "done"
                job.events.put({"type": "done", "count": len(rows)})
        except Exception as exc:  # capture; never crash the worker thread silently
            job.status = "error"
            job.error = str(exc)
            job.events.put({"type": "error", "message": job.error})
        finally:
            with self._lock:
                self._running = False

    def run_in_thread(self, job, scrape_fn):
        """Start the job in a daemon thread. Refuses if one is already running."""
        with self._lock:
            if self._running:
                raise JobBusyError("A scrape is already running. Wait for it to finish.")
            self._running = True
        t = threading.Thread(target=self.run, args=(job, scrape_fn), daemon=True)
        t.start()
        return t
