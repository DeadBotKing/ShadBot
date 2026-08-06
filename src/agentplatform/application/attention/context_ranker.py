"""
ShadBot Agent Platform

Context ranking service.
"""

from __future__ import annotations

from agentplatform.domain.attention import (
    AttentionContext,
)


class ContextRanker:
    """
    Ranks contexts for agent reasoning.
    """

    def rank(
        self,
        contexts: list[AttentionContext],
    ) -> list[AttentionContext]:
        """
        Sort contexts by importance.
        """

        return sorted(
            contexts,
            key=lambda item: (
                item.priority,
                item.score,
                item.created_at,
            ),
            reverse=True,
        )
