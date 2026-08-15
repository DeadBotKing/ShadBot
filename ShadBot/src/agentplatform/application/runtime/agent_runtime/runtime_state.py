"""
ShadBot Agent Platform

Agent Runtime State model for 7.1 Agent Runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AgentRuntimeState:
    instance_id: UUID
    agent_name: str
    status: str  # e.g. CREATED, RUNNING, COMPLETED, FAILED, STOPPED
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    stopped_at: datetime | None = None
