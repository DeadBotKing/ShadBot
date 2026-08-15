"""
ShadBot Agent Platform

Unified service for 5.11 Learning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID
from agentplatform.domain.memory import MemoryRepository
from agentplatform.domain.results import AgentResult
from .experience_extraction import ExperienceExtractor, ExtractedExperience
from .knowledge_update import KnowledgeUpdater, KnowledgeUpdateReport
from .pattern_recognition import PatternRecognizer, RecognizedPattern
from .strategy_improvement import StrategyAdjustment, StrategyImprover


@dataclass(frozen=True, slots=True)
class CompleteLearningPackage:
    experiences: tuple[ExtractedExperience, ...]
    patterns: tuple[RecognizedPattern, ...]
    knowledge_report: KnowledgeUpdateReport
    strategy: StrategyAdjustment


class LearningFlowService:
    """
    Orchestrates extraction, pattern recognition, knowledge update, and strategy adjustment.
    """

    def __init__(
        self,
        repository: MemoryRepository,
        extractor: ExperienceExtractor | None = None,
        recognizer: PatternRecognizer | None = None,
        improver: StrategyImprover | None = None,
    ) -> None:
        self._extractor = extractor or ExperienceExtractor()
        self._recognizer = recognizer or PatternRecognizer()
        self._updater = KnowledgeUpdater(repository)
        self._improver = improver or StrategyImprover()

    def learn(self, project_id: UUID, results: Sequence[AgentResult]) -> CompleteLearningPackage:
        exps = self._extractor.extract(results)
        pats = self._recognizer.recognize(exps)
        report = self._updater.update_knowledge(project_id, pats)
        strat = self._improver.improve(pats)
        return CompleteLearningPackage(
            experiences=exps,
            patterns=pats,
            knowledge_report=report,
            strategy=strat,
        )
