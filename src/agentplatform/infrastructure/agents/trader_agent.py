"""
Agent Platform

Trader agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class TraderAgent(BaseAgent):
    """
    Responsible for trading analysis tasks.
    """

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "trader"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute trading analysis.
        """

        return AgentResult(
            success=True,
            message="Trading analysis completed.",
            data={
                "agent": self.name,
                "project_context": context.intelligence_context,
            },
        )
