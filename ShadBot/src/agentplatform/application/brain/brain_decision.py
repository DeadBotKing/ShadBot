"""
ShadBot Agent Platform

Brain decision capability.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.application.decision import (
    DecisionEngine,
    DecisionResult,
)
from agentplatform.domain.results import (
    AgentResult,
)


class BrainDecision:
    """
    Responsible for execution decisions.
    """

    def __init__(
        self,
        decision_engine: DecisionEngine | None = None,
    ) -> None:
        self._decision_engine = decision_engine or DecisionEngine()

    def decide(
        self,
        results: Sequence[AgentResult],
    ) -> DecisionResult:
        """
        Evaluate execution result.
        """

        return self._decision_engine.decide(
            results,
        )
