"""
ShadBot Agent Platform

Unit tests for 5.8 Planning Flow.
"""

from __future__ import annotations

from agentplatform.application.brain.planning_flow import (
    AgentAssigner,
    ExecutionPlanner,
    PlanningFlowService,
    TaskDecomposer,
)
from agentplatform.domain.agents import AgentRole


def test_task_decomposer_splits_task() -> None:
    decomposer = TaskDecomposer()
    subtasks = decomposer.decompose("Authentication", "Build auth module")
    assert len(subtasks) == 3
    assert subtasks[0].required_role == "architect"


def test_execution_planner_orders_dependencies() -> None:
    subtasks = TaskDecomposer().decompose("Task", "Desc")
    steps = ExecutionPlanner().plan(subtasks)
    assert len(steps) == 3
    assert steps[0].step_number == 1
    assert steps[1].depends_on == (1,)


def test_agent_assigner_maps_roles() -> None:
    steps = ExecutionPlanner().plan(TaskDecomposer().decompose("Task", "Desc"))
    assigned = AgentAssigner().assign(steps)
    assert len(assigned) == 3
    assert assigned[0].assigned_role == AgentRole.ARCHITECT
    assert assigned[1].assigned_role == AgentRole.ENGINEER


def test_planning_flow_service_creates_tracked_plan() -> None:
    service = PlanningFlowService()
    plan = service.create_tracked("Trader", "Build trading") if hasattr(service, "create_tracked") else service.create_plan("Trader", "Build trading")
    assert plan.total_steps == 3
    assert plan.is_completed is False
