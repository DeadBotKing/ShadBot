"""
Agent workflow executor.
"""

from __future__ import annotations

from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult


class AgentWorkflowExecutor:
    """
    Executes agent workflow with feedback loops.
    """

    def execute(
        self,
        agents: list[AgentContract],
        context: AgentExecutionContext,
        max_iterations: int = 3,
    ) -> list[AgentResult]:
        """
        Execute workflow with limited correction cycles.
        """

        results: list[AgentResult] = []

        for _ in range(max_iterations):
            for agent in agents:
                result = agent.execute(context)

                results.append(result)

                if not result.success:
                    continue

                if agent.name == "reviewer":
                    return results

        return results
