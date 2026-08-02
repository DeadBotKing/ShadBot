"""
ShadBot Agent Platform

Memory context builder.
"""

from __future__ import annotations

from agentplatform.domain.memory import MemoryEntry


class MemoryContextBuilder:
    """
    Converts agent memories into prompt-consumable context.
    """

    def build(
        self,
        memories: list[MemoryEntry],
    ) -> dict[str, object]:
        """
        Build memory context.
        """

        return {
            "learned_knowledge": [
                {
                    "content": memory.content,
                    "source": memory.source,
                    "confidence": memory.confidence,
                }
                for memory in memories
            ],
        }
