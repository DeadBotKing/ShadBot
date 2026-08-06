"""
ShadBot Agent Platform

Learning result merger.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.learning import (
    LearningResult,
    LearningStatus,
)


@dataclass(slots=True)
class LearningResultMerger:
    """
    Combines multiple learning results
    into one unified learning outcome.

    Responsibilities
    ----------------
    - Merge learned knowledge
    - Aggregate confidence
    - Produce unified summary

    Does not:
    - Persist memories
    - Validate policy
    - Execute learning
    """

    def merge(
        self,
        results: list[LearningResult],
    ) -> LearningResult:
        """
        Merge learning outputs.
        """

        if not results:
            return LearningResult(
                status=LearningStatus.FAILED,
                learned_items=(),
                confidence=0.0,
                summary="No learning results available.",
            )

        items: list[str] = []

        confidence_values: list[float] = []

        summaries: list[str] = []

        completed = True

        for result in results:

            items.extend(
                result.learned_items,
            )

            confidence_values.append(
                result.confidence,
            )

            summaries.append(
                result.summary,
            )

            if result.status != LearningStatus.COMPLETED:
                completed = False

        confidence = sum(
            confidence_values,
        ) / len(
            confidence_values,
        )

        return LearningResult(
            status=(LearningStatus.COMPLETED if completed else LearningStatus.FAILED),
            learned_items=tuple(
                dict.fromkeys(items),
            ),
            confidence=confidence,
            summary=" | ".join(
                summaries,
            ),
        )
