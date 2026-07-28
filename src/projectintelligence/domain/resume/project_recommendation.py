"""
ShadBot Project Intelligence

Project Recommendation
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectRecommendation:
    """
    Represents an actionable recommendation generated from
    project intelligence.

    Recommendations are produced by the Resume Engine to help
    developers and downstream AI agents determine the most
    appropriate next actions for the project.
    """

    title: str

    description: str

    priority: str

    rationale: str

    expected_outcome: str
