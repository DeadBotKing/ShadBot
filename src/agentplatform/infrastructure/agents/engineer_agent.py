"""
Agent Platform

Engineer agent implementation.
"""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from agentplatform.application.brain import AgentBrain
from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.architecture import (
    ArchitecturePlan,
)
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

        plan = context.metadata.get(
            "architecture_plan",
        )

        if plan is None:
            architect_result = context.metadata.get(
                "agent_results",
                {},
            ).get(
                "architect",
                {},
            )

            plan = architect_result.get(
                "architecture_plan",
            )

        if plan is None:
            return AgentResult(
                success=False,
                message="Architecture plan not found in execution context.",
                data={
                    "agent": self.name,
                    "metadata": context.metadata,
                },
            )

        if not isinstance(
            plan,
            ArchitecturePlan,
        ):
            return AgentResult(
                success=False,
                message="Invalid architecture plan type.",
                data={
                    "agent": self.name,
                    "plan_type": type(plan).__name__,
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

        if self._tool_executor is None:
            return AgentResult(
                success=False,
                message="Tool executor is not configured.",
                data={
                    "agent": self.name,
                },
            )

        generated_files: list[str] = []

        for architecture_file in plan.files:
            file_path = Path(context.target_project.path) / architecture_file.path

            file_context = replace(
                context,
                instructions=(
                    "You are Engineer Agent.\n"
                    "Generate production quality code.\n"
                    f"Create only this file:\n"
                    f"{architecture_file.path}\n"
                    "Do not explain.\n"
                    "Return only code."
                ),
            )

            response = self._brain.think(
                AgentRole.ENGINEER,
                file_context,
            )

            code = self._extractor.extract(
                response,
            )

            self._tool_executor.execute(
                ToolType.FILE_SYSTEM,
                {
                    "action": "write",
                    "path": str(file_path),
                    "content": code,
                },
            )

            generated_files.append(
                str(file_path),
            )

        test_result = self._tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "action": "pytest",
                "path": str(context.target_project.path),
            },
        )

        return AgentResult(
            success=True,
            message="Project implementation completed.",
            data={
                "agent": self.name,
                "generated_files": generated_files,
                "test_result": test_result,
            },
        )
