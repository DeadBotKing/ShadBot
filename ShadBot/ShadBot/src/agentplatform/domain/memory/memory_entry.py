"""
ShadBot Agent Platform

Agent memory entry.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class MemoryEntry:
    """
    Represents learned information from agent execution.
    """

    project_id: UUID

    content: str

    source: str

    confidence: float = 1.0

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
            "content": self.content,
            "source": self.source,
            "confidence": self.confidence,
            "created_at": self.created_at.isoformat(),
        }
