"""
ShadBot Project Intelligence

Evolution Change
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.domain.evolution.evolution_type import (
    EvolutionType,
)


@dataclass(frozen=True, slots=True)
class EvolutionChange:
    """
    Represents one detected project change.
    """

    path: str

    change_type: EvolutionType

    category: str

    description: str
