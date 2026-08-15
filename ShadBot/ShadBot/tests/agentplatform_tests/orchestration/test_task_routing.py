"""
ShadBot Agent Platform

Unit tests for 6.1 Task Routing.
"""

from __future__ import annotations

from agentplatform.application.orchestration.task_routing import (
    RoutingStrategy,
    RoutingValidator,
    TaskCapabilityAnalyzer,
    TaskClassifier,
    TaskRoutingService,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.tasks import AgentTask, TaskType


def test_task_classifier_identifies_architecture() -> None:
    task = AgentTask(title="Design enterprise architecture", description="Desc", task_type=TaskType.IMPLEMENTATION)
    res = TaskClassifier().classify(task)
    assert res.category == "architecture"
    assert res.requires_multi_agent is True


def test_task_capability_analyzer_returns_capabilities() -> None:
    task = AgentTask(title="Review code", description="Desc", task_type=TaskType.IMPLEMENTATION)
    cls = TaskClassifier().classify(task)
    caps = TaskCapabilityAnalyzer().analyze(task, cls)
    assert caps.primary_capability == "code_review"


def test_routing_strategy_maps_category_to_roles() -> None:
    task = AgentTask(title="Design DB", description="Desc", task_type=TaskType.IMPLEMENTATION)
    cls = TaskClassifier().classify(task)
    caps = TaskCapabilityAnalyzer().analyze(task, cls)
    role, cands, strat = RoutingStrategy().select_route(cls, caps)
    assert role == AgentRole.ARCHITECT
    assert strat == "ARCHITECTURE_FIRST"


def test_routing_validator_verifies_decision() -> None:
    val, notes = RoutingValidator().validate(AgentRole.ARCHITECT, (AgentRole.ARCHITECT,))
    assert val is True


def test_task_routing_service_creates_decision() -> None:
    service = TaskRoutingService()
    task = AgentTask(title="Design API", description="Desc", task_type=TaskType.IMPLEMENTATION)
    decision = service.route_task(task)
    assert decision.is_valid is True
    assert decision.required_role == AgentRole.ARCHITECT
