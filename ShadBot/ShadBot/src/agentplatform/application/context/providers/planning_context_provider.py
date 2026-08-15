"""
ShadBot Agent Platform

Planning context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.planning import AgentPlanner
from agentplatform.domain.planning import PlanningRequest


class PlanningContextProvider:
    """
    Provides execution planning context.
    """

    def __init__(
        self,
        planner: AgentPlanner,
        request: PlanningRequest,
    ) -> None:

        self._planner = planner
        self._request = request

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build planning context.
        """

        plan = self._planner.plan(
            self._request,
        )

        return {
            "agents": [agent.value for agent in plan.agents],
            "metadata": plan.metadata,
        }
