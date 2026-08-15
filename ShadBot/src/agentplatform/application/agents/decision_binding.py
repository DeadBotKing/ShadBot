"""
ShadBot Agent Platform

Agent Decision Binding
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

from agentplatform.application.brain.brain_decision import (
    BrainDecision,
)
from agentplatform.domain.results import (
    AgentResult,
)


@dataclass(frozen=True, slots=True)
class DecisionBinding:
    """
    Decision capability attached to an agent.
    """

    decision: BrainDecision

    def decide(
        self,
        results: Sequence[AgentResult],
    ) -> object:
        """
        Execute decision process.
        """

        return self.decision.decide(
            results,
        )
