"""
ShadBot Agent Platform

Persistent project knowledge record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .knowledge_type import KnowledgeType


@dataclass(frozen=True, slots=True)
class ProjectKnowledgeRecord:
    """
    A single piece of project intelligence knowledge.
    """

    project_id: UUID

    knowledge_type: KnowledgeType

    content: str

    source: str

    confidence: float = 1.0

    record_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    def to_dict(
        self,
    ) -> dict[str, object]:
        return {
            "record_id": str(
                self.record_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "knowledge_type": self.knowledge_type.value,
            "content": self.content,
            "source": self.source,
            "confidence": self.confidence,
            "created_at": self.created_at.isoformat(),
        }
