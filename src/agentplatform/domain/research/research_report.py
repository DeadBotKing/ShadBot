"""
ShadBot Agent Platform

Research Report Domain Model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID


@dataclass(frozen=True, slots=True)
class ResearchFinding:
    """
    Single research discovery.
    """

    title: str

    description: str

    category: str

    confidence: float = 0.0


@dataclass(frozen=True, slots=True)
class ResearchReport:
    """
    Enterprise research output.

    Produced by Researcher Agent.
    Consumed by Architect Agent.
    """

    report_id: UUID

    task_id: UUID

    findings: tuple[ResearchFinding, ...]

    best_practices: tuple[str, ...]

    patterns: tuple[str, ...]

    documentation_sources: tuple[str, ...]

    summary: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )
