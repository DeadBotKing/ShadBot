"""
ShadBot Agent Platform

Unified Reasoning Engine for 5.5 Reasoning Flow.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from .decision_support import DecisionSupport, OptionEvaluation
from .problem_analysis import ProblemAnalyzer, ProblemAnalysisResult
from .reasoning_trace import ReasoningTrace


class ReasoningEngine:
    """
    Orchestrates problem analysis, option evaluation, and reasoning tracing.
    """

    def __init__(
        self,
        analyzer: ProblemAnalyzer | None = None,
        support: DecisionSupport | None = None,
    ) -> None:
        self._analyzer = analyzer or ProblemAnalyzer()
        self._support = support or DecisionSupport()

    def execute_reasoning(self, instructions: str, trace_id: UUID | None = None) -> dict[str, Any]:
        trace = ReasoningTrace(trace_id=trace_id)
        
        # 1. Problem Analysis
        trace.record_step("Analyzing input instructions for problem scope", "Problem identified")
        analysis = self._analyzer.analyze(instructions)

        # 2. Decision Support
        trace.record_step("Evaluating candidate technical options", "Options scored")
        evaluations = self._support.evaluate_options(analysis.options)

        # 3. Best Option Selection
        recommended = [ev for ev in evaluations if ev.recommended]
        best_option = recommended[0].option if recommended else "Default Option"
        trace.record_step(f"Selecting recommended option: {best_option}", "Decision supported")

        return {
            "analysis": analysis,
            "evaluations": evaluations,
            "selected_option": best_option,
            "trace": trace,
            "trace_summary": trace.summary(),
        }
