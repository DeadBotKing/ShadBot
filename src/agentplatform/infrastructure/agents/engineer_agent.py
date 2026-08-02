"""
Agent Platform

Engineer agent implementation.
"""

from __future__ import annotations

from agentplatform.application.brain import AgentBrain
from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tools import ToolType
from agentplatform.infrastructure.tools import CodeExtractor

from .base_agent import BaseAgent


class EngineerAgent(BaseAgent):
    """
    Responsible for implementation and code engineering tasks.
    """

    def __init__(
        self,
        brain: AgentBrain | None = None,
        extractor: CodeExtractor | None = None,
        tool_executor: ToolExecutor | None = None,
    ) -> None:
        self._brain = brain
        self._extractor = extractor or CodeExtractor()
        self._tool_executor = tool_executor

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

        if self._brain is None:
            return AgentResult(
                success=False,
                message="Agent brain is not configured.",
                data={
                    "agent": self.name,
                },
            )

        response = self._brain.think(
            AgentRole.ENGINEER,
            context,
        )

        code = self._extractor.extract(
            response,
        )

        output_path = context.metadata.get(
            "output_file",
            "generated_output.py",
        )

        if self._tool_executor is None:
            return AgentResult(
                success=False,
                message="Tool executor is not configured.",
                data={
                    "agent": self.name,
                },
            )

        self._tool_executor.execute(
            ToolType.FILE_SYSTEM,
            {
                "action": "write",
                "path": str(output_path),
                "content": code,
            },
        )

        test_result = self._tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "action": "python",
                "path": str(output_path),
            },
        )

        return AgentResult(
            success=True,
            message="Code generated and written.",
            data={
                "agent": self.name,
                "file": str(output_path),
                "code": code,
                "test_result": test_result,
            },
        )
