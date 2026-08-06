"""
ShadBot Agent Platform

Attention management service.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.attention import (
    AttentionContext,
)

from .context_ranker import (
    ContextRanker,
)


class AttentionManager:
    """
    Manages focused reasoning context.
    """

    def __init__(
        self,
        ranker: ContextRanker | None = None,
    ) -> None:

        self._ranker = ranker or ContextRanker()

        self._contexts: dict[
            UUID,
            list[AttentionContext],
        ] = {}

    def add(
        self,
        context: AttentionContext,
    ) -> None:
        """
        Add context item.
        """

        if context.project_id not in self._contexts:
            self._contexts[context.project_id] = []

        self._contexts[context.project_id].append(
            context,
        )

    def get_focused_context(
        self,
        project_id: UUID,
        limit: int = 10,
    ) -> list[AttentionContext]:
        """
        Retrieve highest priority contexts.
        """

        contexts = self._contexts.get(
            project_id,
            [],
        )

        ranked = self._ranker.rank(
            contexts,
        )

        return ranked[:limit]

    def clear(
        self,
        project_id: UUID,
    ) -> None:
        """
        Clear project attention.
        """

        self._contexts.pop(
            project_id,
            None,
        )
