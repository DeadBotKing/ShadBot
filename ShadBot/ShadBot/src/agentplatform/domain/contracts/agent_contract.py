"""
ShadBot Agent Platform

Base agent contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult


class AgentContract(ABC):
    """
    Base contract for all agents.

    Every agent must implement execute().
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Agent unique name.
        """

        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute agent task.
        """

        raise NotImplementedError
