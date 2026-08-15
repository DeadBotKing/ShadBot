"""
ShadBot Agent Platform

Memory Retriever
"""

from __future__ import annotations

from typing import Any

from agentplatform.domain.memory import (
    MemoryRepository,
)

from .memory_query import (
    MemoryQuery,
)
from .memory_retrieval_result import (
    MemoryRetrievalResult,
)


class MemoryRetriever:
    """
    Retrieves memories required by the Brain.
    """

    def __init__(
        self,
        repository: MemoryRepository,
    ) -> None:

        self._repository = repository

    def retrieve(
        self,
        query: MemoryQuery,
        **kwargs: Any,
    ) -> MemoryRetrievalResult:
        """
        Retrieve memories.
        """
        pid = getattr(query, "goal_id", None) or kwargs.get("project_id")
        try:
            records = self._repository.search(
                capability=query.capability,
                keywords=query.keywords,
                limit=query.max_results,
            )
        except TypeError:
            q_str = " ".join(query.keywords) if query.keywords else query.capability
            records = self._repository.search(
                project_id=pid,
                query=q_str,
            )

        return MemoryRetrievalResult(
            records=tuple(records),
            total_records=len(records),
        )
