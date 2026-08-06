"""
ShadBot Agent Platform

Runtime Agent State
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .runtime_agent_status import RuntimeAgentStatus


@dataclass(slots=True)
class RuntimeAgentState:
    """
    Mutable runtime state of an executing agent.
    """

    agent_instance_id: UUID = field(
        default_factory=uuid4,
    )

    status: RuntimeAgentStatus = RuntimeAgentStatus.IDLE

    current_task_id: UUID | None = None

    started_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )

    iteration: int = 0

    retry_count: int = 0
