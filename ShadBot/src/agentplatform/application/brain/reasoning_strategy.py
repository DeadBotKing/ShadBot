"""
ShadBot Agent Platform

Agent reasoning strategy.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext


class ReasoningStrategy(ABC):
    """
    Base reasoning strategy.
    """

    @abstractmethod
    def reason(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        raise NotImplementedError
