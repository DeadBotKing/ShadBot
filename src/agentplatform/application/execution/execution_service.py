"""
Agent execution service.

Application service responsible for coordinating agent execution.
"""

from __future__ import annotations

from agentplatform.application.execution.agent_executor import AgentExecutor
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult


class AgentExecutionService:
    """
    Coordinates execution flow of agents.
    """

    def __init__(
        self,
        executor: AgentExecutor | None = None,
    ) -> None:
        self._executor = executor or AgentExecutor()

    def execute(
        self,
        agent: AgentContract,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute an agent through executor.

        Args:
            agent: Agent implementation.
            context: Agent runtime context.

        Returns:
            Execution result.
        """

        return self._executor.execute(agent, context)
