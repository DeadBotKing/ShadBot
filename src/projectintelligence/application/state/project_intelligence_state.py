"""
ShadBot Project Intelligence

Project Intelligence State
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectIntelligenceState:
    """
    High-level state produced by the Project Intelligence pipeline.
    """

    current_phase: str

    current_sub_phase: str

    architecture_version: str

    completed_components: int

    pending_components: int

    total_components: int

    completion_percentage: float
