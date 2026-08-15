"""
ShadBot Agent Platform

Agent brain factory contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.application.brain.agent_brain import AgentBrain
from agentplatform.domain.agents import AgentRole


class BrainFactory(ABC):
    """
    Creates isolated brains for agents.
    """

    @abstractmethod
    def create(
        self,
        role: AgentRole,
    ) -> AgentBrain:
        raise NotImplementedError
