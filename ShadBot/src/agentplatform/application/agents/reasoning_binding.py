"""
ShadBot Agent Platform

Agent Reasoning Binding
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.brain import (
    BrainReasoning,
)
from agentplatform.domain.agents import (
    AgentRole,
)


@dataclass(frozen=True, slots=True)
class ReasoningBinding:
    """
    Reasoning capability attached to an agent.
    """

    reasoning: BrainReasoning

    role: AgentRole

    def reason(
        self,
        context: object,
    ) -> str:
        """
        Execute agent reasoning.
        """

        return self.reasoning.reason(
            self.role,
            context,
        )
