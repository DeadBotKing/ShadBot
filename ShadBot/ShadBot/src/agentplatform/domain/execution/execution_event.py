"""
ShadBot Agent Platform

Execution event domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ExecutionEvent:
    """
    Represents one execution lifecycle event.
    """

    execution_id: UUID

    event_type: str

    agent_name: str

    message: str

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )
