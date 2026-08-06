"""
ShadBot Project Intelligence

Agent context metadata.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AgentContextMetadata:
    """
    Metadata of intelligence handoff package.
    """

    project_id: UUID

    version: str = "1.0"

    context_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    def to_dict(
        self,
    ) -> dict[str, object]:

        return {
            "context_id": str(
                self.context_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "version": self.version,
            "created_at": self.created_at.isoformat(),
        }
