"""
ShadBot Agent Platform

Research source model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResearchSource:
    """
    External research source.
    """

    name: str

    url: str

    source_type: str
