"""
Agent Platform

Architect agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class ArchitectAgent(BaseAgent):
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

        return AgentResult(
            success=True,
            message="Architecture analysis completed.",
            data={
                "agent": self.name,
                "project_context": context.intelligence_context,
            },
        )
