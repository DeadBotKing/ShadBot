"""
ShadBot Agent Platform

Enterprise Reviewer Agent.
"""

from __future__ import annotations

from agentplatform.application.brain import (
    AgentBrain,
)
from agentplatform.application.memory import (
    MemoryService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_agent import BaseAgent


class ReviewerAgent(BaseAgent):
    """
    Responsible for enterprise review.

    Responsibilities:
    - Code review
    - Architecture consistency
    - Security analysis
    - Performance analysis
    - Style analysis
    - Regression validation
    """

    def __init__(
        self,
        brain: AgentBrain,
        memory_service: MemoryService,
        tool_executor: ToolExecutor,
    ) -> None:
        self._brain = brain
        self._memory_service = memory_service
        self._tool_executor = tool_executor

    @property
    def name(self) -> str:
        return "reviewer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute review workflow.
        """

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project is required.",
                data={
                    "agent": self.name,
                },
            )

        project_path = str(
            context.target_project.path,
        )

        quality = self._tool_executor.execute(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
            },
        )

        security = self._tool_executor.execute(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
                "action": "security_analysis",
            },
        )

        performance = self._tool_executor.execute(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
                "action": "performance_analysis",
            },
        )

        architecture = self._tool_executor.execute(
            ToolType.PROJECT_ANALYZER,
            {
                "path": project_path,
                "action": "architecture_validation",
            },
        )

        review = self._brain.reason(
            context,
        )

        return AgentResult(
            success=True,
            message="Review workflow completed.",
            data={
                "agent": self.name,
                "quality": quality,
                "security": security,
                "performance": performance,
                "architecture": architecture,
                "review": review,
            },
        )
