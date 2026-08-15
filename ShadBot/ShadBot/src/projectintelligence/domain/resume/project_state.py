"""
ShadBot Project Intelligence

Project State
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectState:
    """
    Represents the current high-level state of a project.

    This object summarizes the overall condition of the project
    independently of implementation details.
    """

    current_phase: str

    current_sub_phase: str

    architecture_version: str

    completed_components: int

    pending_components: int

    total_components: int

    completion_percentage: float
