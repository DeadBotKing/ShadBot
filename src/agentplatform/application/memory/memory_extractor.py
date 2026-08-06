"""
ShadBot Agent Platform

Memory extractor.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.memory import (
    MemoryRecord,
    MemoryType,
)
from agentplatform.domain.review import (
    ReviewResult,
)


class MemoryExtractor:
    """
    Extracts reusable knowledge from agent results.
    """

    def extract(
        self,
        project_id: UUID,
        review: ReviewResult,
    ) -> list[MemoryRecord]:
        """
        Convert review feedback into persistent memories.
        """

        memories: list[MemoryRecord] = []

        for issue in review.issues:
            memories.append(
                MemoryRecord(
                    project_id=project_id,
                    agent="reviewer",
                    memory_type=MemoryType.LESSON_LEARNED,
                    content={
                        "issue": issue,
                    },
                    confidence=0.9,
                )
            )

        for suggestion in review.suggestions:
            memories.append(
                MemoryRecord(
                    project_id=project_id,
                    agent="reviewer",
                    memory_type=MemoryType.IMPROVEMENT,
                    content={
                        "suggestion": suggestion,
                    },
                    confidence=0.85,
                )
            )

        return memories
