"""
ShadBot Agent Platform

Async Task Model component for 8.4 Async Execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AsyncTaskModel:
    task_id: UUID
    name: str
    status: str  # QUEUED, RUNNING, COMPLETED, FAILED, TIMED_OUT
    priority: str
    payload: dict[str, Any]
    result: Any = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
