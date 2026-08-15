"""
ShadBot Agent Platform

Runtime State Model component for 7.4 State Management.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class RuntimeStateModel:
    state_id: UUID
    project_id: UUID
    active_session_id: UUID | None
    execution_phase: str
    status: str
    state_metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
