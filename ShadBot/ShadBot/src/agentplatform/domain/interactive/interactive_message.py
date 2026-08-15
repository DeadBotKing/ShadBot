"""
ShadBot Agent Platform

Interactive Message entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class InteractiveMessage:
    message_id: UUID
    sender: str  # "user" or "shadbot"
    text: str
    action_type: str
    target_file: str | None = None
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
