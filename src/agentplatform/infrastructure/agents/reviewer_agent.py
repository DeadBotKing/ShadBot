"""
Agent Platform

Reviewer agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):
    """
    Responsible for reviewing implementations and decisions.
    """

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "reviewer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute review task.
        """

        return AgentResult(
            success=True,
            message="Review completed.",
            data={
                "agent": self.name,
                "project_context": context.intelligence_context,
            },
        )
