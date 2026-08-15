"""
ShadBot Agent Platform

Memory context provider.
"""

from __future__ import annotations

from typing import Any

from agentplatform.application.memory import MemoryService


class MemoryContextProvider:
    """
    Provides memory data for brain context.
    """

    def __init__(
        self,
        memory_service: MemoryService,
    ) -> None:

        self._memory_service = memory_service

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build memory context.
        """

        return {
            "memories": [],
            "source": "memory_service",
        }
