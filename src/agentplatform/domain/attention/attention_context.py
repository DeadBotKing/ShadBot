"""
ShadBot Agent Platform

Attention context model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from .attention_priority import AttentionPriority


@dataclass(frozen=True, slots=True)
class AttentionContext:
    """
    Context item selected for reasoning.
    """

    project_id: UUID

    source: str

    category: str

    content: dict[str, object]

    priority: AttentionPriority

    score: float = 0.0

    context_id: UUID = field(
        default_factory=uuid4,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc,
        ),
    )
