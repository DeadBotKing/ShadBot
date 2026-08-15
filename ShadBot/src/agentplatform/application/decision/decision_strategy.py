"""
ShadBot Agent Platform

Decision strategy contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.decision import (
    DecisionRequest,
    DecisionResult,
)


class DecisionStrategy(ABC):
    """
    Base decision strategy.
    """

    @abstractmethod
    def decide(
        self,
        request: DecisionRequest,
    ) -> DecisionResult:
        raise NotImplementedError
