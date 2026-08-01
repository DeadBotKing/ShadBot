"""
Agent Platform

Engineer agent implementation.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_agent import BaseAgent


class EngineerAgent(BaseAgent):
    """
    Responsible for implementation and code engineering tasks.
    """

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "engineer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute engineering task.
        """

        return AgentResult(
            success=True,
            message="Engineering task completed.",
            data={
                "agent": self.name,
                "project_context": context.intelligence_context,
            },
        )
