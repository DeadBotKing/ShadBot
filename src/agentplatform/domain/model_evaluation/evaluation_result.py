"""
ShadBot Agent Platform

Model evaluation result.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    """
    Represents model evaluation output.
    """

    model_name: str

    metrics: dict[str, float]

    issues: list[str] = field(
        default_factory=list,
    )

    recommendation: str = ""

    id: UUID = field(
        default_factory=uuid4,
    )
