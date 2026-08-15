"""
ShadBot Agent Platform

Memory Ranker
"""

from __future__ import annotations

from agentplatform.application.brain.memory_flow.retrieval import (
    MemoryRetrievalResult,
)

from .memory_score import MemoryScore
from .ranked_memory_result import RankedMemoryResult


class MemoryRanker:
    """
    Orders retrieved memories by relevance.
    """

    def rank(
        self,
        retrieval_result: MemoryRetrievalResult,
        query_keywords: tuple[str, ...] = (),
    ) -> RankedMemoryResult:
        """
        Rank retrieved memories.
        """

        ranked = tuple(
            sorted(
                (
                    MemoryScore(
                        record=record,
                        score=float(
                            getattr(
                                record,
                                "relevance_score",
                                getattr(record, "confidence", 0.0),
                            )
                        ),
                    )
                    for record in retrieval_result.records
                ),
                key=lambda item: item.score,
                reverse=True,
            )
        )

        return RankedMemoryResult(
            ranked_items=ranked,
            total_items=len(
                ranked,
            ),
        )
