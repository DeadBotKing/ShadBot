"""
ShadBot Agent Platform

Retry coordinator.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.decision import DecisionResult
from agentplatform.application.retry import RetryEngine
from agentplatform.domain.context import AgentExecutionContext


@dataclass(slots=True)
class RetryCoordinator:
    """
    Coordinates retry decisions and retry context updates.
    """

    retry_engine: RetryEngine

    def should_retry(
        self,
        decision: DecisionResult,
        retry_count: int,
    ) -> bool:
        """
        Decide whether another execution attempt is allowed.
        """

        if not decision.retry_required:
            return False

        return self.retry_engine.can_retry(
            retry_count,
        )

    def prepare_retry_context(
        self,
        context: AgentExecutionContext,
        decision: DecisionResult,
    ) -> AgentExecutionContext:
        """
        Prepare next execution context after rejection.
        """

        metadata = dict(
            context.metadata,
        )

        metadata["retry_reason"] = decision.reason
        metadata["retry_metadata"] = decision.metadata

        return AgentExecutionContext(
            project_id=context.project_id,
            task_id=context.task_id,
            instructions=context.instructions,
            intelligence_context=context.intelligence_context,
            metadata=metadata,
            task_title=context.task_title,
            task_description=context.task_description,
            task_type=context.task_type,
        )
