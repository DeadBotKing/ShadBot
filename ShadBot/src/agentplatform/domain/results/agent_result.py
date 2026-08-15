"""
ShadBot Agent Platform

Agent execution result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class AgentResult:
    """
    Result produced by an agent execution.
    """

    success: bool

    message: str

    approved: bool = True

    data: dict[str, Any] = field(
        default_factory=dict,
    )

    execution_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )
