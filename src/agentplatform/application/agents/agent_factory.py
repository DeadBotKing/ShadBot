"""
ShadBot Agent Platform

Runtime Agent Factory
"""

from __future__ import annotations

from collections.abc import Iterable

from agentplatform.application.brain import AgentBrain
from agentplatform.domain.agents import (
    AgentCapability,
    AgentRole,
)

from .brain_binding import BrainBinding
from .runtime_agent import RuntimeAgent


class RuntimeAgentFactory:
    """
    Creates runtime agents with attached brain.
    """

    def create(
        self,
        *,
        role: AgentRole,
        brain: AgentBrain,
        capabilities: Iterable[AgentCapability],
    ) -> RuntimeAgent:

        binding = BrainBinding(
            brain=brain,
        )

        return RuntimeAgent(
            role=role,
            brain=binding.brain,
            capabilities=set(
                capabilities,
            ),
        )
