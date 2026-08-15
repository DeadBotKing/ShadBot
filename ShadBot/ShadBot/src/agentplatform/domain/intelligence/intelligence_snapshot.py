"""
ShadBot Agent Platform

Project intelligence snapshot.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class IntelligenceSnapshot:
    """
    Complete project vision snapshot.

    Represents what Project Intelligence currently sees.
    """

    project_id: UUID

    summary: str

    data: dict[str, Any] = field(
        default_factory=dict,
    )

    snapshot_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    version: str = "1.0"

    def to_dict(
        self,
    ) -> dict[str, object]:
        return {
            "snapshot_id": str(
                self.snapshot_id,
            ),
            "project_id": str(
                self.project_id,
            ),
            "summary": self.summary,
            "data": self.data,
            "version": self.version,
            "created_at": self.created_at.isoformat(),
        }
