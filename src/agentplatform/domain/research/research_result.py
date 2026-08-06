"""
ShadBot Agent Platform

Research result domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ResearchResult:
    """
    Structured research output.
    """

    findings: list[str] = field(default_factory=list)

    alternatives: list[str] = field(default_factory=list)

    recommendation: str = ""

    confidence: float = 0.0
