"""
ShadBot Agent Platform

Improvement Suggestion component for 5.9 Reflection Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from .failure_analysis import FailureAnalysisResult


@dataclass(frozen=True, slots=True)
class ImprovementProposal:
    category: str
    suggestion: str
    priority: str


class ImprovementSuggester:
    """
    Proposes actionable improvements based on failure analysis.
    """

    def suggest(self, analysis: FailureAnalysisResult) -> ImprovementProposal:
        if not analysis.has_failures:
            return ImprovementProposal(
                category="Optimization",
                suggestion="Continue execution standard; no failures detected.",
                priority="Low",
            )
        if analysis.root_cause_category == "Code Defect":
            return ImprovementProposal(
                category="Code Quality",
                suggestion="Add pre-commit linting and strict type checking.",
                priority="High",
            )
        return ImprovementProposal(
            category="System Resilience",
            suggestion="Increase retry budget and fallback timeout resilience.",
            priority="High",
        )
