"""
ShadBot Agent Platform

Unified service for 5.8 Planning Flow.
"""

from __future__ import annotations

from .agent_assignment import AgentAssigner
from .execution_planning import ExecutionPlanner
from .plan_tracking import PlanTracker, TrackedPlan
from .task_decomposition import TaskDecomposer


class PlanningFlowService:
    """
    Orchestrates task decomposition, execution planning, assignment, and tracking.
    """

    def __init__(
        self,
        decomposer: TaskDecomposer | None = None,
        planner: ExecutionPlanner | None = None,
        assigner: AgentAssigner | None = None,
    ) -> None:
        self._decomposer = decomposer or TaskDecomposer()
        self._planner = planner or ExecutionPlanner()
        self._assigner = assigner or AgentAssigner()

    def create_plan(self, task_title: str, task_description: str) -> TrackedPlan:
        subtasks = self._decomposer.decompose(task_title, task_description)
        steps = self._planner.plan(subtasks)
        assigned = self._assigner.assign(steps)
        tracker = PlanTracker()
        return tracker.create_tracked(assigned)
