"""
ShadBot Agent Platform

Unit tests for 7.3 Session Runtime.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.session_runtime import (
    SessionContextStorage,
    SessionLifecycle,
    SessionManager,
    SessionRecoveryHandler,
    SessionRuntimeServiceLayer,
    SessionTerminationManager,
)


def test_session_manager_creates_and_tracks() -> None:
    mgr = SessionManager()
    pid = uuid4()
    sess = mgr.create_session(pid, uuid4())
    assert sess.status == "ACTIVE"
    assert mgr.get_session(sess.session_id) == sess


def test_session_lifecycle_transitions() -> None:
    sess = SessionManager().create_session(uuid4(), uuid4())
    up = SessionLifecycle().transition_status(sess, "INTERRUPTED")
    assert up.status == "INTERRUPTED"


def test_session_context_storage_saves_and_loads() -> None:
    store = SessionContextStorage()
    sid = uuid4()
    store.save_context(sid, "step", 1)
    assert store.load_context(sid)["step"] == 1


def test_session_recovery_recovers_interrupted() -> None:
    sess = SessionManager().create_session(uuid4(), uuid4())
    intr = SessionLifecycle().transition_status(sess, "INTERRUPTED")
    rec = SessionRecoveryHandler().recover(intr)
    assert rec.status == "RECOVERED"


def test_session_runtime_service_layer_orchestrates_all() -> None:
    service = SessionRuntimeServiceLayer()
    sess = service.open_session(uuid4(), uuid4())
    service.store_session_data(sess.session_id, "data", "ok")
    rec = service.recover_session(sess)
    closed = service.close_session(rec)
    assert closed.status == "TERMINATED"
