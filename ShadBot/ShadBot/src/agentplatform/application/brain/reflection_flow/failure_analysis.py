"""
ShadBot Agent Platform

Failure Analysis component for 5.9 Reflection Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class FailureAnalysisResult:
    has_failures: bool
    error_summary: tuple[str, ...]
    root_cause_category: str


class FailureAnalyzer:
    """
    Analyzes failed agent execution results for patterns and root causes.
    """

    def analyze(self, results: Sequence[AgentResult]) -> FailureAnalysisResult:
        errors = tuple(r.message for r in results if not r.success)
        has_fail = bool(errors)
        category = "None"
        if has_fail:
            if any("timeout" in e.lower() or "connection" in e.lower() for e in errors):
                category = "Infrastructure / Network"
            elif any("syntax" in e.lower() or "attribute" in e.lower() for e in errors):
                category = "Code Defect"
            else:
                category = "General Execution Failure"
        return FailureAnalysisResult(
            has_failures=has_fail,
            error_summary=errors,
            root_cause_category=category,
        )
