"""
ShadBot Agent Platform

Research finding model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResearchInsight:
    """
    Extracted research insight.
    """

    statement: str

    impact: str

    recommendation: str
