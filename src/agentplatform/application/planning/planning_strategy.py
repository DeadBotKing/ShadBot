"""
ShadBot Agent Platform

Planning strategy contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.planning import (
    ExecutionPlan,
    PlanningRequest,
)


class PlanningStrategy(ABC):
    """
    Base planning strategy.
    """

    @abstractmethod
    def plan(
        self,
        request: PlanningRequest,
    ) -> ExecutionPlan:
        raise NotImplementedError
