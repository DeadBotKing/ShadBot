"""
ShadBot Agent Platform

Memory extractor.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.memory import MemoryEntry
from agentplatform.domain.review import ReviewResult


class MemoryExtractor:
    """
    Extracts reusable knowledge from review results.
    """

    def extract(
        self,
        project_id: UUID,
        review: ReviewResult,
    ) -> list[MemoryEntry]:
        """
        Convert review feedback into memories.
        """

        memories: list[MemoryEntry] = []

        for issue in review.issues:
            memories.append(
                MemoryEntry(
                    project_id=project_id,
                    content=issue,
                    source="reviewer",
                    confidence=0.9,
                )
            )

        for suggestion in review.suggestions:
            memories.append(
                MemoryEntry(
                    project_id=project_id,
                    content=suggestion,
                    source="reviewer",
                    confidence=0.85,
                )
            )

        return memories
