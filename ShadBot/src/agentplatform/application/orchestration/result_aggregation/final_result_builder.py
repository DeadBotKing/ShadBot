"""
ShadBot Agent Platform

Final Result Builder component for 6.5 Result Aggregation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4
from .conflict_resolution import ConflictResolutionReport
from .result_evaluator import AggregatedEvaluation
from .result_normalizer import NormalizedAgentOutput


@dataclass(frozen=True, slots=True)
class AggregatedResultPackage:
    aggregation_id: UUID
    success: bool
    message: str
    evaluation: AggregatedEvaluation
    conflict_report: ConflictResolutionReport
    agent_outputs: tuple[NormalizedAgentOutput, ...]
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class FinalResultBuilder:
    """
    Builds the final aggregated result package.
    """

    def build(
        self,
        outputs: tuple[NormalizedAgentOutput, ...],
        eval_res: AggregatedEvaluation,
        conflict_res: ConflictResolutionReport,
    ) -> AggregatedResultPackage:
        msg = "All agents executed successfully." if eval_res.all_successful else f"Partial execution: failed agents {eval_res.failed_agents}"
        return AggregatedResultPackage(
            aggregation_id=uuid4(),
            success=eval_res.all_successful,
            message=msg,
            evaluation=eval_res,
            conflict_report=conflict_res,
            agent_outputs=outputs,
        )
