"""
ShadBot Agent Platform

Workflow Event Definition component for 8.3 Workflow Events.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class WorkflowEvent:
    event_id: UUID
    workflow_id: UUID
    state: str  # STARTED, RUNNING, COMPLETED, FAILED, PAUSED, RESUMED
    step_number: int
    payload: dict[str, Any]
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
