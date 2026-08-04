"""
Agent Platform

Architect agent implementation.
"""

from __future__ import annotations

from dataclasses import replace

from agentplatform.application.architecture import (
    ArchitectureExecutor,
    ArchitecturePlanner,
)
from agentplatform.application.brain import AgentBrain
from agentplatform.application.memory import MemoryService
from agentplatform.application.tooling import ToolExecutor
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.results import AgentResult

from .base_llm_agent import BaseLLMAgent


class ArchitectAgent(BaseLLMAgent):
    """
    Responsible for architecture analysis and design decisions.
    """

    def __init__(
        self,
        role: AgentRole,
        brain: AgentBrain,
        tool_executor: ToolExecutor | None = None,
        memory_service: MemoryService | None = None,
        architecture_planner: ArchitecturePlanner | None = None,
        architecture_executor: ArchitectureExecutor | None = None,
    ) -> None:
        super().__init__(
            role=role,
            brain=brain,
            tool_executor=tool_executor,
            memory_service=memory_service,
        )

        self._architecture_planner = architecture_planner or ArchitecturePlanner()

        self._architecture_executor = architecture_executor or ArchitectureExecutor()

    @property
    def name(self) -> str:
        """
        Agent unique name.
        """

        return "architect"

    def run(
        self,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute architecture analysis.
        """

        architecture_context = replace(
            context,
            instructions=(
                "You are an Architect Agent.\n"
                "You must design project structure only.\n"
                "Do NOT write implementation code.\n"
                "\n"
                "Return only this format:\n"
                "\n"
                "DIRECTORIES:\n"
                "- path\n"
                "\n"
                "FILES:\n"
                "- path\n"
                "\n"
                "Example:\n"
                "DIRECTORIES:\n"
                "- src/domain\n"
                "- src/application\n"
                "\n"
                "FILES:\n"
                "- src/main.py\n"
                "- README.md\n"
            ),
        )

        response = self.think(
            architecture_context,
        )

        print(response)

        project_name = (
            context.target_project.name if context.target_project else "unknown"
        )

        plan = self._architecture_planner.create_plan(
            project_name=project_name,
            response=response,
        )

        if context.target_project:
            self._architecture_executor.execute(
                plan,
                context.target_project.path,
            )

        return AgentResult(
            success=True,
            message="Architecture analysis and execution completed.",
            data={
                "agent": self.name,
                "analysis": response,
                "architecture_plan": plan,
                "project_context": context.intelligence_context,
            },
        )
