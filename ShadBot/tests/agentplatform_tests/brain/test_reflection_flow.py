"""
ShadBot Agent Platform

Unit tests for 5.9 Reflection Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.reflection_flow import (
    ExecutionReviewer,
    FailureAnalyzer,
    ImprovementSuggester,
    ReflectionFlowService,
    SelfCritiquer,
)
from agentplatform.domain.results import AgentResult


def test_execution_reviewer_counts_status() -> None:
    res1 = AgentResult(success=True, message="ok")
    res2 = AgentResult(success=False, message="err")
    review = ExecutionReviewer().review([res1, res2])
    assert review.total_executed == 2
    assert review.success_count == 1
    assert review.failure_count == 1
    assert review.overall_status == "PARTIAL"


def test_failure_analyzer_identifies_root_cause() -> None:
    res = AgentResult(success=False, message="Connection timeout")
    ana = FailureAnalyzer().analyze([res])
    assert ana.has_failures is True
    assert "Network" in ana.root_cause_category


def test_improvement_suggester_proposes_action() -> None:
    res = AgentResult(success=False, message="Syntax error")
    ana = FailureAnalyzer().analyze([res])
    prop = ImprovementSuggester().suggest(ana)
    assert prop.priority == "High"
    assert "linting" in prop.suggestion


def test_reflection_flow_service_executes_complete_reflection() -> None:
    service = ReflectionFlowService()
    pkg = service.reflect([AgentResult(success=True, message="done")])
    assert pkg.review.overall_status == "SUCCESS"
    assert pkg.critique.score == 1.0
