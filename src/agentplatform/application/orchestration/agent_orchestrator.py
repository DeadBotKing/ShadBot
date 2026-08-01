"""
Agent Orchestrator.

Coordinates agent execution flow.
"""

from __future__ import annotations

from collections.abc import Sequence

from agentplatform.application.execution import AgentExecutionService
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult


class AgentOrchestrator:
    """
    Coordinates multiple agents in an execution pipeline.

    The orchestrator does not implement agent logic.
    It only controls execution order and communication.
    """

    def __init__(
        self,
        execution_service: AgentExecutionService | None = None,
    ) -> None:
        self._execution_service = execution_service or AgentExecutionService()

    def execute_pipeline(
        self,
        agents: Sequence[AgentContract],
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute agents sequentially.

        Args:
            agents: Ordered agent pipeline.
            context: Shared execution context.

        Returns:
            Results from every agent.
        """

        results: list[AgentResult] = []

        for agent in agents:
            result = self._execution_service.execute(
                agent,
                context,
            )

            results.append(result)

        return results
