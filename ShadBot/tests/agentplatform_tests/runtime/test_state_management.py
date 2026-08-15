"""
ShadBot Agent Platform

Unit tests for 7.4 State Management.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.runtime.state_management import (
    RuntimeStateModel,
    RuntimeStateStorage,
    RuntimeStateSynchronizer,
    RuntimeStateTransitionManager,
    StateConsistencyValidator,
    StateManagementServiceLayer,
)


def test_runtime_state_storage_saves_and_loads() -> None:
    store = RuntimeStateStorage()
    pid = uuid4()
    st = RuntimeStateModel(uuid4(), pid, uuid4(), "EXEC", "RUNNING")
    store.save_state(st)
    assert store.load_state(pid) == st


def test_runtime_state_transition_manager_updates_phase() -> None:
    st = RuntimeStateModel(uuid4(), uuid4(), uuid4(), "EXEC", "RUNNING")
    up = RuntimeStateTransitionManager().transition(st, "REVIEW", "COMPLETED")
    assert up.execution_phase == "REVIEW"
    assert up.status == "COMPLETED"


def test_state_consistency_validator_verifies_session() -> None:
    valid_st = RuntimeStateModel(uuid4(), uuid4(), uuid4(), "EXEC", "RUNNING")
    res = StateConsistencyValidator().validate_consistency(valid_st)
    assert res.consistent is True
    invalid_st = RuntimeStateModel(uuid4(), uuid4(), None, "EXEC", "RUNNING")
    res_bad = StateConsistencyValidator().validate_consistency(invalid_st)
    assert res_bad.consistent is False


def test_state_management_service_layer_updates() -> None:
    service = StateManagementServiceLayer()
    pid = uuid4()
    sid = uuid4()
    st = service.init_state(pid, sid)
    up, val, sync = service.update_phase(pid, "PLANNING", "RUNNING")
    assert up.execution_phase == "PLANNING"
    assert val.consistent is True
    assert sync.synchronized is True
