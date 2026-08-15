"""
ShadBot Agent Platform

Review result domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ReviewResult:
    """
    Structured review output.
    """

    approved: bool

    issues: list[str] = field(default_factory=list)

    suggestions: list[str] = field(default_factory=list)
