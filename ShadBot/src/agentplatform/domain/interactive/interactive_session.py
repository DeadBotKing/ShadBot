"""
ShadBot Agent Platform

Interactive Session entity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4
from .interactive_message import InteractiveMessage


@dataclass(frozen=True, slots=True)
class InteractiveCoPilotSession:
    session_id: UUID
    project_id: UUID
    project_name: str
    messages: tuple[InteractiveMessage, ...] = ()
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
