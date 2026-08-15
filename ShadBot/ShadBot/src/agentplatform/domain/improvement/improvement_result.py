"""
ShadBot Agent Platform

Self improvement result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .improvement_status import ImprovementStatus


@dataclass(frozen=True, slots=True)
class ImprovementResult:
    """
    Represents the outcome of a self improvement cycle.

    This model stores:
    - what was improved
    - why it was improved
    - validation state
    - generated knowledge

    It does not:
    - apply code changes
    - modify agents
    - persist data
    """

    request_id: UUID

    project_id: UUID

    target_component: str

    status: ImprovementStatus

    improvements: tuple[str, ...]

    validation_report: dict[str, object]

    confidence: float

    summary: str

    result_id: UUID = field(
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
        Convert result into serializable structure.
        """

        return {
            "result_id": str(
                self.result_id,
            ),
            "request_id": str(
                self.request_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "target_component": self.target_component,
            "status": self.status.value,
            "improvements": list(
                self.improvements,
            ),
            "validation_report": self.validation_report,
            "confidence": self.confidence,
            "summary": self.summary,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
        }
