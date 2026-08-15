"""
ShadBot Agent Platform

Unit tests for 6.4 Agent Handoff.
"""

from __future__ import annotations

from uuid import uuid4
from agentplatform.application.orchestration.agent_handoff import (
    AgentHandoffService,
    AgentTransitionManager,
    HandoffContextBuilder,
    HandoffHistoryTracker,
    HandoffRequest,
    HandoffValidator,
)
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


def test_handoff_validator_verifies_success() -> None:
    req = HandoffRequest("architect", "engineer", AgentResult(True, "ok", data={"architecture_plan": "Layered"}), uuid4())
    res = HandoffValidator().validate(req)
    assert res.valid is True
    req_bad = HandoffRequest("architect", "engineer", AgentResult(False, "err"), uuid4())
    res_bad = HandoffValidator().validate(req_bad)
    assert res_bad.valid is False


def test_context_builder_merges_artifacts() -> None:
    context = AgentExecutionContext(uuid4(), uuid4(), "test")
    res = AgentResult(True, "ok", data={"architecture_plan": "Layered"})
    req = HandoffRequest("architect", "engineer", res, uuid4())
    new_ctx = HandoffContextBuilder().build_context(context, req)
    assert "architecture_plan" in new_ctx.metadata


def test_transition_manager_records_record() -> None:
    mgr = AgentTransitionManager()
    req = HandoffRequest("architect", "engineer", AgentResult(True, "ok", data={"architecture_plan": "Layered"}), uuid4())
    rec = mgr.record_transition(req)
    assert rec.from_agent == "architect"
    assert len(mgr.get_transitions()) == 1


def test_handoff_history_tracker_indexes_by_task() -> None:
    tracker = HandoffHistoryTracker()
    tid = uuid4()
    req = HandoffRequest("architect", "engineer", AgentResult(True, "ok"), tid)
    rec = AgentTransitionManager().record_transition(req)
    tracker.add_record(rec)
    assert len(tracker.get_history(tid)) == 1


def test_agent_handoff_service_orchestrates_complete_handoff() -> None:
    service = AgentHandoffService()
    context = AgentExecutionContext(uuid4(), uuid4(), "test")
    res = AgentResult(True, "ok", data={"architecture_plan": "Layered"})
    req = HandoffRequest("architect", "engineer", res, uuid4())
    pkg = service.handoff(context, req)
    assert pkg.validation.valid is True
    assert "architecture_plan" in pkg.context.metadata
