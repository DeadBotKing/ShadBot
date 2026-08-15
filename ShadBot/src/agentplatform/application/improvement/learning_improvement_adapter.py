"""
ShadBot Agent Platform

Learning to improvement adapter.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from agentplatform.domain.improvement import (
    ImprovementRequest,
)
from agentplatform.domain.learning import (
    LearningResult,
)


@dataclass(slots=True)
class LearningImprovementAdapter:
    """
    Converts learning outcomes into
    self improvement requests.

    Responsibilities:
    - Translate lessons into improvement intent
    - Keep learning and improvement decoupled

    Does not:
    - Execute improvement
    - Modify agents
    """

    def create_request(
        self,
        project_id: UUID,
        learning_result: LearningResult,
        target_component: str,
    ) -> ImprovementRequest:
        """
        Create improvement request from learning result.
        """

        return ImprovementRequest(
            project_id=project_id,
            target_component=target_component,
            objective=("Improve component based on " "learned execution feedback."),
            reason=learning_result.summary,
            current_state=("Derived from learning cycle."),
            requested_by="learning_loop",
            metadata={
                "confidence": learning_result.confidence,
                "learned_items": list(
                    learning_result.learned_items,
                ),
            },
        )
