"""
ShadBot Agent Platform

Persistent memory record.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .memory_type import MemoryType


@dataclass(frozen=True, slots=True)
class MemoryRecord:
    """
    Enterprise persistent memory record.

    Represents:
    - Agent experience
    - Project knowledge
    - Decisions
    - Lessons learned
    - Execution history
    """

    project_id: UUID

    memory_type: MemoryType

    content: dict[str, object]

    source_agent: str

    confidence: float = 1.0

    tags: tuple[str, ...] = ()

    memory_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    def to_dict(
        self,
    ) -> dict[str, object]:
        return {
            "memory_id": str(
                self.memory_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "memory_type": self.memory_type.value,
            "content": self.content,
            "source_agent": self.source_agent,
            "confidence": self.confidence,
            "tags": list(
                self.tags,
            ),
            "created_at": self.created_at.isoformat(),
        }
