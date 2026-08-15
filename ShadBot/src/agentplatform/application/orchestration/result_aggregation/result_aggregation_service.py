"""
ShadBot Agent Platform

Unified service for 6.5 Result Aggregation.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.results import AgentResult
from .aggregation_reporter import AggregationReporter
from .conflict_resolution import ConflictResolver
from .final_result_builder import AggregatedResultPackage, FinalResultBuilder
from .result_collector import ResultCollector
from .result_evaluator import ResultEvaluator
from .result_normalizer import ResultNormalizer


class ResultAggregationService:
    """
    Orchestrates collection, normalization, evaluation, conflict resolution, building, and reporting.
    """

    def __init__(
        self,
        collector: ResultCollector | None = None,
        normalizer: ResultNormalizer | None = None,
        evaluator: ResultEvaluator | None = None,
        resolver: ConflictResolver | None = None,
        builder: FinalResultBuilder | None = None,
        reporter: AggregationReporter | None = None,
    ) -> None:
        self._collector = collector or ResultCollector()
        self._normalizer = normalizer or ResultNormalizer()
        self._evaluator = evaluator or ResultEvaluator()
        self._resolver = resolver or ConflictResolver()
        self._builder = builder or FinalResultBuilder()
        self._reporter = reporter or AggregationReporter()

    def aggregate(self, results: Sequence[AgentResult]) -> tuple[AggregatedResultPackage, str]:
        collected = self._collector.collect(results)
        norm = self._normalizer.normalize(collected)
        ev = self._evaluator.evaluate(norm)
        conf = self._resolver.resolve(norm)
        pkg = self._builder.build(norm, ev, conf)
        rep = self._reporter.report(pkg)
        return pkg, rep
