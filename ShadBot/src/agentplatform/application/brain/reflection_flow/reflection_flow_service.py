"""
ShadBot Agent Platform

Unified service for 5.9 Reflection Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult
from .execution_review import ExecutionReviewer, ExecutionReviewResult
from .failure_analysis import FailureAnalyzer, FailureAnalysisResult
from .improvement_suggestion import ImprovementProposal, ImprovementSuggester
from .self_critique import SelfCritiquer, SelfCritiqueResult


@dataclass(frozen=True, slots=True)
class CompleteReflectionPackage:
    review: ExecutionReviewResult
    analysis: FailureAnalysisResult
    proposal: ImprovementProposal
    critique: SelfCritiqueResult


class ReflectionFlowService:
    """
    Orchestrates execution review, failure analysis, suggestion, and self-critique.
    """

    def __init__(
        self,
        reviewer: ExecutionReviewer | None = None,
        analyzer: FailureAnalyzer | None = None,
        suggester: ImprovementSuggester | None = None,
        critiquer: SelfCritiquer | None = None,
    ) -> None:
        self._reviewer = reviewer or ExecutionReviewer()
        self._analyzer = analyzer or FailureAnalyzer()
        self._suggester = suggester or ImprovementSuggester()
        self._critiquer = critiquer or SelfCritiquer()

    def reflect(self, results: Sequence[AgentResult]) -> CompleteReflectionPackage:
        rev = self._reviewer.review(results)
        ana = self._analyzer.analyze(results)
        prop = self._suggester.suggest(ana)
        crit = self._critiquer.critique(rev)
        return CompleteReflectionPackage(
            review=rev,
            analysis=ana,
            proposal=prop,
            critique=crit,
        )
