"""
ShadBot Agent Platform

Context Snapshot
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from agentplatform.application.brain.context_assembly.prioritizer import (
    PrioritizedContext,
)


@dataclass(frozen=True, slots=True)
class ContextSnapshot:
    """
    Immutable brain context snapshot.
    """

    goal_id: UUID

    prioritized_context: PrioritizedContext

    snapshot_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
