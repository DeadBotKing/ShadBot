"""
ShadBot Agent Platform

Context Item
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .context_source import ContextSource


@dataclass(frozen=True, slots=True)
class ContextItem:
    """
    Single context unit.
    """

    source: ContextSource

    key: str

    value: object

    priority: int = 0

    context_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
