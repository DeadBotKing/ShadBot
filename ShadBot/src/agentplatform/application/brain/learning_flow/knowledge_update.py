"""
ShadBot Agent Platform

Knowledge Update component for 5.11 Learning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from uuid import UUID
from agentplatform.domain.memory import MemoryRecord, MemoryRepository, MemoryType
from .pattern_recognition import RecognizedPattern


@dataclass(frozen=True, slots=True)
class KnowledgeUpdateReport:
    updated_records: int
    patterns_recorded: tuple[str, ...]


class KnowledgeUpdater:
    """
    Persists recognized patterns into project knowledge memory.
    """

    def __init__(self, repository: MemoryRepository) -> None:
        self._repository = repository

    def update_knowledge(self, project_id: UUID, patterns: Sequence[RecognizedPattern]) -> KnowledgeUpdateReport:
        recorded: list[str] = []
        for pat in patterns:
            record = MemoryRecord(
                project_id=project_id,
                memory_type=MemoryType.KNOWLEDGE,
                content={"pattern": pat.pattern_name, "occurrences": pat.occurrence_count},
                source_agent="learning_flow",
                confidence=pat.confidence,
            )
            self._repository.save(record)
            recorded.append(pat.pattern_name)
        return KnowledgeUpdateReport(
            updated_records=len(recorded),
            patterns_recorded=tuple(recorded),
        )
