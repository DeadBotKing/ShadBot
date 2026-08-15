"""
ShadBot Agent Platform

Session Entity component for 7.3 Session Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ExecutionSession:
    session_id: UUID
    project_id: UUID
    task_id: UUID
    status: str  # e.g. ACTIVE, INTERRUPTED, RECOVERED, TERMINATED
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
