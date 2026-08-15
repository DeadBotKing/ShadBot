"""
ShadBot Agent Platform

Reasoning strategy contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext


class ReasoningStrategy(ABC):
    """
    Strategy contract for reasoning approaches.
    """

    @abstractmethod
    def execute(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        raise NotImplementedError
