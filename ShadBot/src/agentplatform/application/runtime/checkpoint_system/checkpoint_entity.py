"""
ShadBot Agent Platform

Checkpoint Entity component for 7.5 Checkpoint System.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class CheckpointEntity:
    checkpoint_id: UUID
    project_id: UUID
    session_id: UUID
    step_number: int
    version: int
    snapshot_data: dict[str, Any]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
