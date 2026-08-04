"""
ShadBot Agent Platform

Project intelligence agent implementation.
"""

from __future__ import annotations

from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tools import ToolType

from .base_agent import BaseAgent


class ProjectIntelligenceAgent(BaseAgent):
    """
    Responsible for project analysis and intelligence extraction.
    """

    def __init__(
        self,
        tool_executor: ToolExecutor | None = None,
    ) -> None:
        self._tool_executor = tool_executor

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "project_intelligence"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Analyze target project.
        """

        if self._tool_executor is None:
            return AgentResult(
                success=False,
                message="Tool executor is not configured.",
                data={
                    "agent": self.name,
                },
            )

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project is not selected.",
                data={
                    "agent": self.name,
                },
            )

        analysis = self._tool_executor.execute(
            ToolType.PROJECT_ANALYZER,
            {
                "path": str(
                    context.target_project.path,
                ),
            },
        )

        context.metadata["intelligence_context"] = analysis

        return AgentResult(
            success=True,
            message="Project intelligence analysis completed.",
            data={
                "agent": self.name,
                "intelligence": analysis,
                "role": AgentRole.PROJECT_INTELLIGENCE.value,
            },
        )
