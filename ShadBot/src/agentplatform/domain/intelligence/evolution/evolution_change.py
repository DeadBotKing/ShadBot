"""
ShadBot Agent Platform

Evolution change model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class EvolutionChange:
    """
    Represents one project change.
    """

    change_type: str

    target: str

    description: str
