"""
Agent Platform

Architect agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_llm_agent import BaseLLMAgent


class ArchitectAgent(BaseLLMAgent):
    """
    Responsible for architecture analysis and design decisions.
    """

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "architect"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute architecture analysis.
        """

        response = self.think(
            context,
        )

        return AgentResult(
            success=True,
            message="Architecture analysis completed.",
            data={
                "agent": self.name,
                "analysis": response,
                "project_context": context.intelligence_context,
            },
        )
