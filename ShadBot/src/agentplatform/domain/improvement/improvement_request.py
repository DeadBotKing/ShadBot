"""
ShadBot Agent Platform

Self improvement request model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .improvement_status import ImprovementStatus


@dataclass(frozen=True, slots=True)
class ImprovementRequest:
    """
    Represents a request to improve
    an agent capability or system behavior.

    This model only describes intent.
    It does not execute improvement.
    """

    project_id: UUID

    target_component: str

    objective: str

    reason: str

    current_state: str

    requested_by: str

    status: ImprovementStatus = ImprovementStatus.REQUESTED

    request_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    def to_dict(
        self,
    ) -> dict[str, object]:
        """
        Convert request into serializable structure.
        """

        return {
            "request_id": str(
                self.request_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "target_component": self.target_component,
            "objective": self.objective,
            "reason": self.reason,
            "current_state": self.current_state,
            "requested_by": self.requested_by,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
        }
