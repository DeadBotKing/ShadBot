"""
ShadBot Agent Platform

Goal domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .goal_status import GoalStatus
from .intent import Intent


@dataclass(frozen=True, slots=True)
class Goal:
    """
    Represents understood agent objective.
    """

    project_id: UUID

    description: str

    intent: Intent

    expected_output: tuple[str, ...]

    constraints: tuple[str, ...]

    success_criteria: tuple[str, ...]

    priority: int = 5

    status: GoalStatus = GoalStatus.CREATED

    goal_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def to_context(
        self,
    ) -> dict[str, object]:
        """
        Convert goal into brain context.
        """

        return {
            "goal_id": str(self.goal_id),
            "description": self.description,
            "intent": self.intent.intent_type.value,
            "confidence": self.intent.confidence,
            "expected_output": list(
                self.expected_output,
            ),
            "constraints": list(
                self.constraints,
            ),
            "success_criteria": list(
                self.success_criteria,
            ),
            "priority": self.priority,
            "status": self.status.value,
        }
