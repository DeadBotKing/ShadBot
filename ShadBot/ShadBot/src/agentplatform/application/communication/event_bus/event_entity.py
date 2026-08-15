"""
ShadBot Agent Platform

Event Entity model for 8.1 Event Bus.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class SystemEvent:
    event_id: UUID
    event_type: str
    source_component: str
    payload: dict[str, Any]
    correlation_id: UUID = field(default_factory=uuid4)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
