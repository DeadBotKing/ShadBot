"""
Agent Orchestrator.

Coordinates agent execution flow.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import replace
from typing import Any

from agentplatform.application.execution import AgentExecutionService
from agentplatform.domain.context import AgentExecutionContext
from agentplatform.domain.contracts import AgentContract
from agentplatform.domain.results import AgentResult
from agentplatform.domain.review import ReviewResult


class AgentOrchestrator:
    """
    Coordinates multiple agents in an execution pipeline.

    The orchestrator controls execution order
    and manages improvement iterations.
    """

    def __init__(
        self,
        execution_service: AgentExecutionService | None = None,
        max_iterations: int = 3,
    ) -> None:
        self._execution_service = execution_service or AgentExecutionService()
        self._max_iterations = max_iterations

    def execute_pipeline(
        self,
        agents: Sequence[AgentContract],
        context: AgentExecutionContext,
    ) -> list[AgentResult]:
        """
        Execute agents with feedback iterations.
        """

        results: list[AgentResult] = []

        current_context = context

        for _ in range(self._max_iterations):
            iteration_results: list[AgentResult] = []

            for agent in agents:
                result = self._execution_service.execute(
                    agent,
                    current_context,
                )

                iteration_results.append(result)

                if self._extract_feedback(result) is not None:
                    feedback = self._extract_feedback(result)

                    current_context = replace(
                        current_context,
                        metadata={
                            **current_context.metadata,
                            "review_feedback": feedback,
                        },
                    )

            results.extend(iteration_results)

            if not self._needs_retry(iteration_results):
                break

        return results

    def _extract_feedback(
        self,
        result: AgentResult,
    ) -> str | None:
        """
        Extract reviewer feedback.
        """

        review: Any = result.data.get(
            "review",
        )

        if isinstance(review, ReviewResult):
            return "\n".join(
                review.suggestions,
            )

        return None

    def _needs_retry(
        self,
        results: Sequence[AgentResult],
    ) -> bool:
        """
        Determine whether another iteration is needed.
        """

        for result in results:
            review: Any = result.data.get(
                "review",
            )

            if isinstance(review, ReviewResult):
                return not review.approved

        return False
