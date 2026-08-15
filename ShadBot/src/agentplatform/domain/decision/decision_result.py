"""
ShadBot Agent Platform

Decision result model.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .decision_status import DecisionStatus


@dataclass(frozen=True, slots=True)
class DecisionResult:
    """
    Result produced by decision engine.
    """

    status: DecisionStatus

    reason: str

    retry_required: bool

    metadata: dict[str, object] = field(
        default_factory=dict,
    )
