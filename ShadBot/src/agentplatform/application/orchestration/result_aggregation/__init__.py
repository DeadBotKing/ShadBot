"""
ShadBot Agent Platform

6.5 Result Aggregation module.
"""

from .aggregation_reporter import AggregationReporter
from .conflict_resolution import ConflictResolutionReport, ConflictResolver
from .final_result_builder import AggregatedResultPackage, FinalResultBuilder
from .result_aggregation_service import ResultAggregationService
from .result_collector import ResultCollector
from .result_evaluator import AggregatedEvaluation, ResultEvaluator
from .result_normalizer import NormalizedAgentOutput, ResultNormalizer

__all__ = [
    "ResultCollector",
    "NormalizedAgentOutput",
    "ResultNormalizer",
    "AggregatedEvaluation",
    "ResultEvaluator",
    "ConflictResolutionReport",
    "ConflictResolver",
    "AggregatedResultPackage",
    "FinalResultBuilder",
    "AggregationReporter",
    "ResultAggregationService",
]
