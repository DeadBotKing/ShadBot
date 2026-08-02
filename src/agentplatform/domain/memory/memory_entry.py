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

    memory_id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )
