"""
Agent Platform

Researcher agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class ResearcherAgent(BaseAgent):
    """
    Responsible for research and information analysis.
    """

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "researcher"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute research analysis.
        """

        return AgentResult(
            success=True,
            message="Research completed.",
            data={
                "agent": self.name,
                "project_context": context.intelligence_context,
            },
        )
