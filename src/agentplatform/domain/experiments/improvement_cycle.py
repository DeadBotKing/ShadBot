"""
ShadBot Agent Platform

ML improvement cycle model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class ImprovementCycle:
    """
    Represents ML improvement iteration.
    """

    model_name: str

    iteration: int

    evaluation_score: float

    previous_score: float

    improved: bool

    decision: str

    id: UUID = field(
        default_factory=uuid4,
    )
