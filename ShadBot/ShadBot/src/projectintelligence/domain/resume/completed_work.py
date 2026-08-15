"""
ShadBot Project Intelligence

Completed Work
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class CompletedWork:
    """
    Represents a completed unit of work within the project.

    Each instance describes a completed milestone, feature,
    implementation, or architectural task that is important
    for understanding the project's evolution.
    """

    title: str

    description: str

    category: str

    completed_at: datetime

    impact: str
