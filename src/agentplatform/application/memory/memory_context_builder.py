"""
ShadBot Agent Platform

Memory context builder.
"""

from __future__ import annotations

from agentplatform.domain.memory import (
    MemoryRecord,
)


class MemoryContextBuilder:
    """
    Converts project memories into LLM context.
    """

    def build(
        self,
        memories: list[MemoryRecord | dict[str, object]],
    ) -> dict[str, object]:
        """
        Build memory context for agent reasoning.
        """

        knowledge: list[dict[str, object]] = []

        for memory in memories:

            if isinstance(
                memory,
                dict,
            ):
                knowledge.append(
                    {
                        "agent": memory.get(
                            "agent",
                            "",
                        ),
                        "type": memory.get(
                            "type",
                            "",
                        ),
                        "content": memory.get(
                            "content",
                            {},
                        ),
                        "confidence": memory.get(
                            "confidence",
                            0.0,
                        ),
                        "created_at": memory.get(
                            "created_at",
                            "",
                        ),
                    }
                )

                continue

            knowledge.append(
                {
                    "agent": memory.agent,
                    "type": memory.memory_type.value,
                    "content": memory.content,
                    "confidence": memory.confidence,
                    "created_at": memory.created_at.isoformat(),
                }
            )

        return {
            "learned_knowledge": knowledge,
            "memory_count": len(
                knowledge,
            ),
        }
