"""
ShadBot Agent Platform

Decision context provider.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from agentplatform.application.decision import DecisionEngine
from agentplatform.domain.results import AgentResult


class DecisionContextProvider:
    """
    Provides decision context.
    """

    def __init__(
        self,
        decision_engine: DecisionEngine,
        results: Sequence[AgentResult],
    ) -> None:

        self._decision_engine = decision_engine
        self._results = results

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build decision context.
        """

        decision = self._decision_engine.decide(
            self._results,
        )

        return {
            "status": decision.status.value,
            "reason": decision.reason,
            "retry_required": decision.retry_required,
            "metadata": decision.metadata,
        }
