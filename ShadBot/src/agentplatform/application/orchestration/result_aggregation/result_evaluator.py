"""
ShadBot Agent Platform

Result Evaluator component for 6.5 Result Aggregation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from .result_normalizer import NormalizedAgentOutput


@dataclass(frozen=True, slots=True)
class AggregatedEvaluation:
    all_successful: bool
    success_ratio: float
    failed_agents: tuple[str, ...]


class ResultEvaluator:
    """
    Evaluates aggregated normalized outputs for overall success.
    """

    def evaluate(self, outputs: Sequence[NormalizedAgentOutput]) -> AggregatedEvaluation:
        total = len(outputs)
        if total == 0:
            return AggregatedEvaluation(True, 1.0, ())
        failed = tuple(o.agent_name for o in outputs if not o.success)
        ratio = (total - len(failed)) / total
        return AggregatedEvaluation(
            all_successful=(len(failed) == 0),
            success_ratio=round(ratio, 2),
            failed_agents=failed,
        )
