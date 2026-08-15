"""
Agent Platform

Trader agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_llm_agent import BaseLLMAgent


class TraderAgent(BaseLLMAgent):
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

        response = self.think(
            context,
        )

        return AgentResult(
            success=True,
            message="Trading analysis completed.",
            data={
                "agent": self.name,
                "analysis": response,
                "project_context": context.intelligence_context,
            },
        )
