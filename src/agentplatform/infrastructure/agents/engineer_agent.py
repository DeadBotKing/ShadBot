"""
ShadBot Agent Platform

Enterprise Engineer Agent.
"""

from __future__ import annotations

from pathlib import Path

from agentplatform.application.generation import (
    CodeGenerationService,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.capabilities import (
    Capability,
    CapabilityType,
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
    Responsible for software implementation.
    """

    def __init__(
        self,
        code_generation_service: CodeGenerationService,
        tool_executor: ToolExecutor,
    ) -> None:

        super().__init__(
            capabilities=[
                Capability(
                    CapabilityType.CODE_GENERATION,
                    "Generate production code.",
                ),
                Capability(
                    CapabilityType.CODE_REFACTORING,
                    "Refactor existing implementations.",
                ),
                Capability(
                    CapabilityType.TEST_GENERATION,
                    "Generate automated tests.",
                ),
                Capability(
                    CapabilityType.DEBUGGING,
                    "Analyze and fix software issues.",
                ),
                Capability(
                    CapabilityType.IMPLEMENTATION,
                    "Implement approved architecture plans.",
                ),
                Capability(
                    CapabilityType.REFACTORING,
                    "Improve existing code quality.",
                ),
                Capability(
                    CapabilityType.FAILURE_ANALYSIS,
                    "Analyze implementation failures.",
                ),
                Capability(
                    CapabilityType.PERFORMANCE_ANALYSIS,
                    "Analyze implementation performance.",
                ),
                Capability(
                    CapabilityType.SECURITY_ANALYSIS,
                    "Apply secure coding practices.",
                ),
            ],
        )

        self._code_generation_service = code_generation_service

        self._tool_executor = tool_executor

    @property
    def name(self) -> str:
        return "engineer"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:

        plan = context.metadata.get(
            "architecture_plan",
        )

        if plan is None:
            return AgentResult(
                success=False,
                message="Architecture plan required.",
                data={
                    "agent": self.name,
                },
            )

        generated_files: list[str] = []

        if context.target_project is None:
            return AgentResult(
                success=False,
                message="Target project required.",
                data={
                    "agent": self.name,
                },
            )

        for file_plan in plan.file_plan:

            artifact = self._code_generation_service.generate(
                context=context,
                file_path=(
                    Path(
                        context.target_project.path,
                    )
                    / file_plan.path
                ),
                instructions=("Implement according to " "approved architecture."),
            )

            generated_files.append(
                str(
                    artifact.path,
                ),
            )

        build = self._tool_executor.execute(
            ToolType.BUILD_RUNNER,
            {
                "path": str(
                    context.target_project.path,
                ),
            },
        )

        tests = self._tool_executor.execute(
            ToolType.TEST_RUNNER,
            {
                "path": str(
                    context.target_project.path,
                ),
            },
        )

        return AgentResult(
            success=True,
            message="Engineering completed.",
            data={
                "agent": self.name,
                "capabilities": [
                    capability.capability_type.value for capability in self.capabilities
                ],
                "generated_files": generated_files,
                "build": build,
                "tests": tests,
            },
        )
