"""
ShadBot Agent Platform

Brain planning capability.
"""

from __future__ import annotations

from agentplatform.application.planning import (
    AgentPlanner,
)
from agentplatform.domain.planning import (
    ExecutionPlan,
    PlanningRequest,
)


class BrainPlanning:
    """
    Responsible for task planning decisions.
    """

    def __init__(
        self,
        planner: AgentPlanner | None = None,
    ) -> None:
        self._planner = planner or AgentPlanner()

    def plan(
        self,
        request: PlanningRequest,
    ) -> ExecutionPlan:
        """
        Create execution plan.
        """

        return self._planner.plan(
            request,
        )
