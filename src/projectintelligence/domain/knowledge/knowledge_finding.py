"""
ShadBot Project Intelligence

Knowledge Finding Domain Entity
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from projectintelligence.domain.knowledge.rule_severity import (
    RuleSeverity,
)


@dataclass(slots=True)
class KnowledgeFinding:
    """
    Represents a knowledge discovery generated during project analysis.
    """

    rule_name: str

    category: str

    title: str

    description: str

    severity: RuleSeverity

    finding_id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    source: str | None = None

    entity_id: UUID | None = None
