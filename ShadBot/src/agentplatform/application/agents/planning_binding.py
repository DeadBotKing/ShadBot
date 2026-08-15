"""
ShadBot Agent Platform

Agent Planning Binding
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.brain.brain_planning import (
    BrainPlanning,
)
from agentplatform.domain.planning import (
    ExecutionPlan,
    PlanningRequest,
)


@dataclass(frozen=True, slots=True)
class PlanningBinding:
    """
    Planning capability attached to an agent.
    """

    planning: BrainPlanning

    def create_plan(
        self,
        request: PlanningRequest,
    ) -> ExecutionPlan:
        """
        Create execution plan.
        """

        return self.planning.plan(
            request,
        )
