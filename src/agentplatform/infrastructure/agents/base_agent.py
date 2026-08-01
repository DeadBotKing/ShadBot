"""
Agent Platform

Base agent implementation.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult


class BaseAgent(AgentContract, ABC):
    """
    Base implementation for all agents.
    """

    def execute(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute agent logic.
        """

        try:
            return self.run(context)

        except Exception as exc:
            return AgentResult(
                success=False,
                message=str(exc),
            )

    @abstractmethod
    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Agent-specific implementation.
        """
        raise NotImplementedError
