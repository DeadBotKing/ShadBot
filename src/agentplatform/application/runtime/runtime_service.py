"""
Agent Runtime Service.

High-level entry point for agent execution.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.application.orchestration import AgentOrchestrator
from agentplatform.application.planning.planner import AgentPlanner
from agentplatform.application.registry import AgentRegistry
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult
from agentplatform.domain.tasks import AgentTask


class AgentRuntimeService:
    """
    Coordinates the complete agent execution lifecycle.

    Flow:

    Task
      |
      v
    Planner
      |
      v
    Registry
      |
      v
    Orchestrator
      |
      v
    Results
    """

    def __init__(
        self,
        planner: AgentPlanner | None = None,
        registry: AgentRegistry | None = None,
        orchestrator: AgentOrchestrator | None = None,
    ) -> None:
        self._planner = planner or AgentPlanner()
        self._registry = registry or AgentRegistry()
        self._orchestrator = orchestrator or AgentOrchestrator()

    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute a task through the agent pipeline.
        """

        plan = self._planner.create_plan(task)

        agents = self._resolve_agents(plan.agents)

        return self._orchestrator.execute_pipeline(
            agents,
            context,
        )

    def _resolve_agents(
        self,
        roles: Sequence[AgentRole],
    ) -> list[AgentContract]:
        """
        Resolve agent implementations from registry.
        """

        agents: list[AgentContract] = []

        for role in roles:
            if self._registry.exists(role):
                agents.append(self._registry.get(role))

        return agents
