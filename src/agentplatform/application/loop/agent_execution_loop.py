"""
ShadBot Agent Platform

Agent execution loop.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.decision import (
    DecisionEngine,
)
from agentplatform.application.runtime import (
    AgentRuntimeService,
)
from agentplatform.application.runtime.retry_coordinator import (
    RetryCoordinator,
)
from agentplatform.domain.context import (
    AgentExecutionContext,
)
from agentplatform.domain.results import (
    AgentResult,
)
from agentplatform.domain.tasks import (
    AgentTask,
)


@dataclass(slots=True)
class AgentExecutionLoop:
    """
    High-level autonomous execution loop.

    Coordinates:
    - Runtime execution
    - Decision evaluation
    - Retry handling
    """

    runtime: AgentRuntimeService
    decision_engine: DecisionEngine
    retry_coordinator: RetryCoordinator

    def execute(
        self,
        task: AgentTask,
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute task until accepted or retry limit reached.
        """

        results = self.runtime.execute(
            task,
            context,
        )

        decision = self.decision_engine.decide(
            results,
        )

        retry_count = 0

        while self.retry_coordinator.should_retry(
            decision,
            retry_count,
        ):
            context = self.retry_coordinator.prepare_retry_context(
                context,
                decision,
            )

            retry_count += 1

            results = self.runtime.execute(
                task,
                context,
            )

            decision = self.decision_engine.decide(
                results,
            )

        return results
