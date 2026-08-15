"""
ShadBot Agent Platform

Research result domain model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ResearchResult:
    """
    Structured research output.
    """

    findings: list[str] = field(default_factory=list)
    alternatives: list[str] = field(default_factory=list)
    recommendation: str = ""
    confidence: float = 0.0
    query: str = ""
    summary: str = ""
    sources: list[str] = field(default_factory=list)
    raw_data: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, object]:
        return {
            "query": self.query,
            "summary": self.summary,
            "findings": self.findings,
            "alternatives": self.alternatives,
            "recommendation": self.recommendation,
            "confidence": self.confidence,
            "sources": self.sources,
            "raw_data": self.raw_data,
        }
