"""
ShadBot Agent Platform

Hyperparameter experiment model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class HyperparameterExperiment:
    """
    Represents ML hyperparameter experiment.
    """

    model_name: str

    parameters: dict[str, object]

    expected_metric: str

    notes: str = ""

    id: UUID = field(
        default_factory=uuid4,
    )
