"""
ShadBot Project Intelligence

Project Summary
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectSummary:
    """
    Human-readable summary describing the current project.

    This object contains concise information that allows both
    developers and AI systems to quickly understand the project
    without reading the complete project knowledge.
    """

    title: str

    overview: str

    architecture_summary: str

    current_focus: str

    latest_changes: str

    next_goal: str
