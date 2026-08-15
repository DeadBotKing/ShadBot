"""
ShadBot Agent Platform

Unit tests for 7.2 Brain Runtime.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.brain_runtime import (
    BrainContextRuntime,
    BrainRuntimeServiceLayer,
    BrainStateSynchronizer,
    ReasoningRuntimeManager,
)
from agentplatform.application.runtime.brain_runtime.brain_runtime_instance import (
    BrainRuntimeInstance,
    BrainRuntimeState,
)


def test_reasoning_runtime_manager_prepares_tokens() -> None:
    pkg = ReasoningRuntimeManager().prepare_reasoning("architect", {"key": "value"})
    assert pkg.is_ready is True
    assert pkg.active_role == "architect"


def test_context_runtime_creates_snapshot() -> None:
    pid = uuid4()
    snap = BrainContextRuntime().create_snapshot(pid, {"a": 1})
    assert snap.project_id == pid
    assert snap.context_data == {"a": 1}


def test_state_sync_updates_status() -> None:
    rid = uuid4()
    inst = BrainRuntimeInstance(rid, BrainRuntimeState(rid, "IDLE", ""))
    sync = BrainStateSynchronizer().synchronize(inst, "REASONING")
    assert sync.state.status == "REASONING"


def test_brain_runtime_service_layer_starts_brain() -> None:
    service = BrainRuntimeServiceLayer()
    pid = uuid4()
    inst, pkg, snap = service.start_brain(pid, "architect", {"instructions": "test"})
    assert inst.state.status == "REASONING"
    assert pkg.is_ready is True
    assert snap.project_id == pid
