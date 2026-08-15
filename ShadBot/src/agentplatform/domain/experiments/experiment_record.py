"""
ShadBot Agent Platform

Experiment record model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ExperimentRecord:
    """
    Represents a tracked experiment.
    """

    name: str

    hypothesis: str

    parameters: dict[str, object]

    metrics: dict[str, float]

    result: str

    id: UUID = field(
        default_factory=uuid4,
    )
