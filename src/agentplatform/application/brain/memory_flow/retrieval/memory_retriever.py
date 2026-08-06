"""
ShadBot Agent Platform

Memory Retriever
"""

from __future__ import annotations

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
    ) -> MemoryRetrievalResult:
        """
        Retrieve memories.
        """

        records = self._repository.search(
            capability=query.capability,
            keywords=query.keywords,
            limit=query.max_results,
        )

        return MemoryRetrievalResult(
            records=tuple(records),
            total_records=len(records),
        )
