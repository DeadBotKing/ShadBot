"""
Agent Runtime Service.

High-level entry point for agent execution.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import replace

from agentplatform.application.monitoring import (
    ExecutionTracker,
)
from agentplatform.application.orchestration import (
    AgentOrchestrator,
)
from agentplatform.application.planning.planner import (
    AgentPlanner,
)
from agentplatform.application.registry import (
    AgentRegistry,
)
from agentplatform.application.tooling import (
    ToolExecutor,
)
from agentplatform.application.workspace import (
    WorkspaceRegistry,
)
from agentplatform.domain.agents import (
    AgentRole,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.contracts import (
    AgentContract,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tasks import (
    AgentTask,
)


class AgentRuntimeService:
    """
    Coordinates complete agent execution lifecycle.
    """

    def __init__(
        self,
        planner: AgentPlanner | None = None,
        registry: AgentRegistry | None = None,
        orchestrator: AgentOrchestrator | None = None,
        tool_executor: ToolExecutor | None = None,
        execution_tracker: ExecutionTracker | None = None,
        workspace_registry: WorkspaceRegistry | None = None,
    ) -> None:
        self._planner = planner or AgentPlanner()

        self._registry = registry or AgentRegistry()

        if orchestrator is None:
            raise ValueError("AgentOrchestrator must be provided.")

        self._orchestrator = orchestrator

        self._tool_executor = tool_executor

        self._execution_tracker = execution_tracker or ExecutionTracker()

        self._workspace_registry = workspace_registry or WorkspaceRegistry()

    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute complete agent pipeline.
        """

        execution = self._execution_tracker.create(
            task.title,
        )

        plan = self._planner.create_plan(
            task,
        )

        agents = self._resolve_agents(
            plan.agents,
        )

        print("PLANNED ROLES:", [role.value for role in plan.agents])
        print("RESOLVED AGENTS:", [agent.name for agent in agents])

        context = replace(
            context,
            metadata={
                **context.metadata,
                "agent_execution": execution,
                "planned_agents": [agent.name for agent in agents],
            },
        )

        workspace_name = context.metadata.get(
            "workspace",
        )

        project_name = context.metadata.get(
            "project",
        )

        if workspace_name and project_name:
            workspace = self._workspace_registry.get(
                workspace_name,
            )

            if workspace is None:
                raise ValueError(
                    f"Workspace not found: {workspace_name}",
                )

            project = next(
                (item for item in workspace.projects if item.name == project_name),
                None,
            )

            if project is None:
                raise ValueError(
                    f"Project not found: {project_name}",
                )

            context = replace(
                context,
                workspace=workspace,
                target_project=project,
            )

        return self._orchestrator.execute_pipeline(
            agents,
            context,
        )

    def _resolve_agents(
        self,
        roles: Sequence[AgentRole],
    ) -> list[AgentContract]:
        """
        Resolve agent implementations.
        """

        agents: list[AgentContract] = []

        for role in roles:
            if self._registry.exists(role):
                agents.append(
                    self._registry.get(role),
                )

        return agents
