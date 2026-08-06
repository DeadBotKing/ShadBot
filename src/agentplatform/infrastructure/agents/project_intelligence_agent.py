"""
ShadBot Agent Platform

Project Intelligence Agent implementation.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.domain.agents import (
    AgentRole,
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
from projectintelligence.domain.handoff import (
    AgentContextMetadata,
    AgentContextPackage,
)

from .base_llm_agent import BaseLLMAgent


class ProjectIntelligenceAgent(BaseLLMAgent):
    """
    Shared vision agent.

    Responsibilities:
    - Analyze project state
    - Build project vision
    - Persist project vision
    - Create handoff package
    - Provide context for all agent brains
    """

    def __init__(
        self,
        role: AgentRole,
        brain,
        tool_executor: ToolExecutor,
        vision_builder: ProjectVisionBuilder,
        vision_service: ProjectVisionService,
        memory_service=None,
    ) -> None:

        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        )

        self._intelligence_lifecycle = intelligence_lifecycle

    @property
    def name(
        self,
    ) -> str:
        return "project_intelligence"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Analyze project and create shared vision.
        """

        if self.tool_executor is None:
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

        project_path = context.target_project.path

        raw = self.tool_executor.execute(
            ToolType.PROJECT_ANALYZER,
            {
                "path": project_path.as_posix(),
            },
        )

        vision = self._intelligence_lifecycle.initialize(
            project_id=context.project_id,
            project_path=project_path,
            intelligence_data=raw,
        )

        package = self._build_package(
            context,
            raw,
        )

        context.metadata["project_vision"] = vision

        context.metadata["agent_context_package"] = package

        return AgentResult(
            success=True,
            message=("Project intelligence " "vision generated."),
            data={
                "agent": self.name,
                "role": (AgentRole.PROJECT_INTELLIGENCE.value),
                "vision": vision,
                "intelligence": package,
            },
        )

    def _build_package(
        self,
        context: AgentExecutionContext,
        data: dict[str, Any],
    ) -> AgentContextPackage:
        """
        Build downstream agent handoff.
        """

        metadata = AgentContextMetadata(
            context_id=context.project_id,
            version="1.0",
        )

        return AgentContextPackage(
            project_id=context.project_id,
            metadata=metadata,
            summary=str(
                data.get(
                    "summary",
                    "",
                ),
            ),
            technologies=self._string_tuple(
                data.get(
                    "technologies",
                    [],
                ),
            ),
            frameworks=self._string_tuple(
                data.get(
                    "frameworks",
                    [],
                ),
            ),
            languages=self._string_tuple(
                data.get(
                    "languages",
                    [],
                ),
            ),
            dependencies=self._string_dict(
                data.get(
                    "dependencies",
                    {},
                ),
            ),
            architecture_description=(
                self._optional_string(
                    data.get(
                        "architecture_description",
                        data.get(
                            "architecture",
                        ),
                    ),
                )
            ),
            conventions=self._string_tuple(
                data.get(
                    "conventions",
                    [],
                ),
            ),
            constraints=self._string_tuple(
                data.get(
                    "constraints",
                    [],
                ),
            ),
            recommendations=self._string_tuple(
                data.get(
                    "recommendations",
                    [],
                ),
            ),
            current_state=self._optional_string(
                data.get(
                    "current_state",
                ),
            ),
        )

    @staticmethod
    def _string_tuple(
        value: object,
    ) -> tuple[str, ...]:

        if not isinstance(
            value,
            list,
        ):
            return ()

        return tuple(str(item) for item in value)

    @staticmethod
    def _string_dict(
        value: object,
    ) -> dict[str, str]:

        if not isinstance(
            value,
            dict,
        ):
            return {}

        return {str(key): str(item) for key, item in value.items()}

    @staticmethod
    def _optional_string(
        value: object,
    ) -> str | None:

        if value is None:
            return None

        return str(value)
