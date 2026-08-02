"""
Agent Platform

Engineer agent implementation.
"""

from __future__ import annotations

from agentplatform.application.brain import AgentBrain
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult
from agentplatform.infrastructure.tools import (
    CodeExtractor,
    FileSystemTool,
    TestRunner,
)

from .base_agent import BaseAgent


class EngineerAgent(BaseAgent):
    """
    Responsible for implementation and code engineering tasks.
    """

    def __init__(
        self,
        brain: AgentBrain | None = None,
        extractor: CodeExtractor | None = None,
        filesystem: FileSystemTool | None = None,
        test_runner: TestRunner | None = None,
    ) -> None:
        self._brain = brain
        self._extractor = extractor or CodeExtractor()
        self._filesystem = filesystem or FileSystemTool()
        self._test_runner = test_runner or TestRunner()

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

        self._filesystem.write_file(
            str(output_path),
            code,
        )

        test_result = self._test_runner.run_python_file(
            str(output_path),
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
