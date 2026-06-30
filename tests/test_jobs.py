import threading

import pytest

from server.jobs import JobManager, JobBusyError


def test_run_success_collects_rows_and_progress():
    mgr = JobManager()
    job = mgr.create({"limit": 5})

    def fake_scrape(progress, should_cancel=None):
        progress("[1/1] k ... 2 videos")
        return [{"video_id": "a"}, {"video_id": "b"}]

    mgr.run(job, fake_scrape)
    assert job.status == "done"
    assert len(job.rows) == 2
    assert "[1/1] k ... 2 videos" in job.progress


def test_run_empty_is_botcheck_error():
    mgr = JobManager()
    job = mgr.create({})
    mgr.run(job, lambda progress, should_cancel=None: [])
    assert job.status == "error"
    assert "browser login" in job.error.lower() or "bot" in job.error.lower()


def test_run_exception_is_captured():
    mgr = JobManager()
    job = mgr.create({})

    def boom(progress, should_cancel=None):
        raise RuntimeError("yt-dlp exploded")

    mgr.run(job, boom)
    assert job.status == "error"
    assert "yt-dlp exploded" in job.error


def test_second_run_rejected_while_running():
    mgr = JobManager()
    gate = threading.Event()
    job1 = mgr.create({})

    def blocking(progress, should_cancel=None):
        gate.wait(2)
        return [{"video_id": "a"}]

    mgr.run_in_thread(job1, blocking)
    job2 = mgr.create({})
    with pytest.raises(JobBusyError):
        mgr.run_in_thread(job2, lambda progress, should_cancel=None: [{"video_id": "b"}])
    gate.set()  # let job1 finish


def test_cancel_sets_status_and_keeps_partial_rows():
    mgr = JobManager()
    job = mgr.create({})
    job.cancelled = True  # pre-cancel

    def scrape(progress, should_cancel=None):
        # honours cancel: returns whatever partial it had
        return [{"video_id": "partial"}]

    mgr.run(job, scrape)
    assert job.status == "cancelled"
    assert len(job.rows) == 1  # partial data kept, not treated as bot-check


def test_lru_evicts_oldest_beyond_cap():
    mgr = JobManager(max_jobs=3)
    ids = [mgr.create({}).id for _ in range(4)]
    assert mgr.get(ids[0]) is None      # oldest evicted
    assert mgr.get(ids[3]) is not None  # newest retained
