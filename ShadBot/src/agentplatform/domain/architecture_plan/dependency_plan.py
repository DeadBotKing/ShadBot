"""
Dependency planning model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DependencyPlan:
    """
    Dependency decision.
    """

    name: str

    version: str | None

    reason: str
