"""
ShadBot Agent Platform

Reflection Analysis component for Phase 10 Self Improvement System.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class ReflectionAnalysisResult:
    total_executions: int
    success_ratio: float
    detected_bottlenecks: tuple[str, ...]
    learning_potential: str

    def to_dict(self) -> dict[str, object]:
        return {
            "total_executions": self.total_executions,
            "success_ratio": self.success_ratio,
            "detected_bottlenecks": list(self.detected_bottlenecks),
            "learning_potential": self.learning_potential,
        }


class ReflectionAnalyzer:
    """
    Analyzes historical execution results to discover improvement opportunities.
    """

    def analyze(self, results: Sequence[AgentResult]) -> ReflectionAnalysisResult:
        total = len(results)
        if total == 0:
            return ReflectionAnalysisResult(0, 1.0, (), "None")
        successes = sum(1 for r in results if r.success)
        ratio = round(successes / total, 2)
        potential = "HIGH" if ratio < 0.85 else "LOW"
        return ReflectionAnalysisResult(
            total_executions=total,
            success_ratio=ratio,
            detected_bottlenecks=() if ratio == 1.0 else ("agent_retry_overhead",),
            learning_potential=potential,
        )
