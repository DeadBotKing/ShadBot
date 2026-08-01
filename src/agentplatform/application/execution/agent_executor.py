"""
Agent executor.

Responsible for executing an agent contract inside a workspace context.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult


class AgentExecutor:
    """
    Executes agents using a provided execution context.
    """

    def execute(
        self,
        agent: AgentContract,
        context: AgentExecutionContext,
    ) -> AgentResult:
        """
        Execute an agent.

        Args:
            agent: Agent implementation.
            context: Runtime execution context.

        Returns:
            Agent execution result.
        """

        try:
            return agent.execute(context)

        except Exception as exc:
            return AgentResult(
                success=False,
                message=str(exc),
            )
