"""
ShadBot Agent Platform

Brain planning capability.
"""

from __future__ import annotations

from agentplatform.application.planning import (
    AgentExecutionPlan,
    AgentPlanner,
)
from agentplatform.domain.tasks import AgentTask


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
        task: AgentTask,
    ) -> AgentExecutionPlan:
        """
        Create execution plan.
        """

        return self._planner.create_plan(
            task,
        )
