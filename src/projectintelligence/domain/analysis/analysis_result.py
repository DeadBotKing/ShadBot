"""
ShadBot Project Intelligence

Analysis Result Domain Model
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(slots=True)
class AnalysisResult:
    """
    Enterprise analysis execution result.
    """

    project_id: UUID

    analyzer_name: str

    result_id: UUID = field(
        default_factory=uuid4
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    success: bool = False

    score: float | None = None

    findings: list[str] = field(
        default_factory=list
    )

    warnings: list[str] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )

    metrics: dict[str, object] = field(
        default_factory=dict
    )

    metadata: dict[str, object] = field(
        default_factory=dict
    )