"""
ShadBot Agent Platform

Unit tests for 7.6 Resume System.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.checkpoint_system import CheckpointCreator, CheckpointSystemServiceLayer
from agentplatform.application.runtime.resume_system import (
    ExecutionContinuationManager,
    ExecutionRecoveryEngine,
    ResumeContextLoader,
    ResumeRequest,
    ResumeSystemServiceLayer,
    ResumeValidator,
    StateRestoration,
)


def test_context_loader_injects_version_step() -> None:
    cp = CheckpointCreator().create(uuid4(), uuid4(), 3, 2, {"data": "ok"})
    loaded = ResumeContextLoader().load_context(cp)
    assert loaded["resumed_from_version"] == 2
    assert loaded["resumed_from_step"] == 3


def test_recovery_engine_recovers_step() -> None:
    cp = CheckpointCreator().create(uuid4(), uuid4(), 3, 2, {"data": "ok"})
    state = ExecutionRecoveryEngine().recover_execution(cp, {"k": 1})
    assert state.is_recovered is True
    assert state.resumed_step == 4


def test_state_restoration_sets_running() -> None:
    res = StateRestoration().restore_state(uuid4(), uuid4())
    assert res.restored is True
    assert res.state.status == "RUNNING"


def test_resume_system_service_layer_executes_resume() -> None:
    cp_service = CheckpointSystemServiceLayer()
    pid = uuid4()
    cp_service.create_and_save(pid, uuid4(), 5, {"step": "five"})
    service = ResumeSystemServiceLayer(cp_service)
    cont = service.resume(ResumeRequest(pid))
    assert cont is not None
    assert cont.can_continue is True
    assert cont.next_step == 6
