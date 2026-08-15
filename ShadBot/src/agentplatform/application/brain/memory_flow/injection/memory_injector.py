"""
ShadBot Agent Platform

Memory Injector
"""

from __future__ import annotations

from agentplatform.application.brain.memory_flow.ranking import (
    RankedMemoryResult,
)

from .injected_memory import InjectedMemory
from .memory_injection_result import MemoryInjectionResult


class MemoryInjector:
    """
    Injects ranked memories into the reasoning pipeline.
    """

    def inject(
        self,
        ranked_result: RankedMemoryResult,
    ) -> MemoryInjectionResult:
        """
        Inject ranked memories.
        """

        injected = tuple(
            InjectedMemory(
                record=item.record,
                score=item.score,
                injection_order=index,
            )
            for index, item in enumerate(
                ranked_result.ranked_items,
                start=1,
            )
        )

        return MemoryInjectionResult(
            injected_memories=injected,
            total_memories=len(
                injected,
            ),
        )
