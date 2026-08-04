"""
Agent Platform

Engineer agent implementation.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.application.generation import (
    CodeGenerationService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.architecture import (
    ArchitecturePlan,
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


class EngineerAgent(BaseAgent):
    """
    Responsible for implementation and code engineering tasks.
    """

    def __init__(
        self,
        code_generation_service: CodeGenerationService,
        tool_executor: ToolExecutor,
    ) -> None:
        self._code_generation_service = code_generation_service
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

        generated_files: list[str] = []

        for architecture_file in plan.files:
            file_path = Path(context.target_project.path) / architecture_file.path

            artifact = self._code_generation_service.generate(
                context=context,
                file_path=file_path,
                instructions=(
                    "You are Engineer Agent.\n"
                    "Generate production quality code.\n"
                    f"Create only this file:\n"
                    f"{architecture_file.path}\n"
                    "Do not explain.\n"
                    "Return only code."
                ),
            )

            generated_files.append(
                str(artifact.path),
            )

        test_result = self._tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "action": "pytest",
                "path": str(
                    context.target_project.path,
                ),
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
