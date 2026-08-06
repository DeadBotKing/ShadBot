"""
ShadBot Agent Platform

Enterprise QA Agent.
"""

from __future__ import annotations

from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tools import (
    ToolType,
)

from .base_llm_agent import BaseLLMAgent


class QAAgent(BaseLLMAgent):
    """
    Responsible for quality assurance.

    Responsibilities:
    - Test generation
    - Test execution
    - Coverage analysis
    - Regression detection
    - Release validation
    """

    def __init__(
        self,
        role: AgentRole,
        brain,
        tool_executor: ToolExecutor,
        memory_service=None,
    ) -> None:

        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        )

    @property
    def name(self) -> str:
        return "qa"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute QA workflow.
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

        tests = self.tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "path": project_path,
            },
        )

        validation = self.tool_executor.execute(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
            },
        )

        coverage = self.tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "path": project_path,
                "action": "coverage_analysis",
            },
        )

        regression = self.tool_executor.execute(
            ToolType.QUALITY_VALIDATOR,
            {
                "path": project_path,
                "action": "regression_analysis",
            },
        )

        return AgentResult(
            success=True,
            message="QA workflow completed.",
            data={
                "agent": self.name,
                "tests": tests,
                "validation": validation,
                "coverage": coverage,
                "regression_analysis": regression,
            },
        )
