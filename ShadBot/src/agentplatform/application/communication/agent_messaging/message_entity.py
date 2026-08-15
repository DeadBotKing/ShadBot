"""
ShadBot Agent Platform

Message Entity model for 8.2 Agent Messaging.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AgentMessage:
    message_id: UUID
    sender: str
    receiver: str
    message_type: str
    payload: dict[str, Any]
    priority: str  # CRITICAL, NORMAL, BACKGROUND
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
