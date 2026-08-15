"""
ShadBot Agent Platform

Memory Updater
"""

from __future__ import annotations

from agentplatform.domain.memory import (
    MemoryRepository,
)

from .memory_update_request import (
    MemoryUpdateRequest,
)
from .memory_update_result import (
    MemoryUpdateResult,
)


class MemoryUpdater:
    """
    Updates long-term agent memory.
    """

    def __init__(
        self,
        repository: MemoryRepository,
    ) -> None:

        self._repository = repository

    def update(
        self,
        request: MemoryUpdateRequest,
    ) -> MemoryUpdateResult:
        """
        Persist memory update.
        """

        updated_memory = self._repository.update(
            request.memory,
        )

        return MemoryUpdateResult(
            memory_id=updated_memory.memory_id,
            updated=True,
            message=("Memory updated successfully"),
        )
