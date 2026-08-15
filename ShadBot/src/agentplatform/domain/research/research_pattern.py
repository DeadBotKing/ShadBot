"""
ShadBot Agent Platform

Research pattern domain model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResearchPattern:
    """
    Technical pattern discovered during research.
    """

    name: str

    description: str

    applicability: str
