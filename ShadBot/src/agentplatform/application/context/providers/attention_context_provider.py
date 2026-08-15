"""
ShadBot Agent Platform

Attention context provider.
"""

from __future__ import annotations

from typing import Any


class AttentionContextProvider:
    """
    Selects and prioritizes important context
    before sending data to the brain.
    """

    def __init__(
        self,
        priority_rules: dict[str, int] | None = None,
    ) -> None:

        self._priority_rules = priority_rules or {}

    def provide(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Build focused attention context.
        """

        prioritized = sorted(
            context.items(),
            key=lambda item: self._priority_rules.get(
                item[0],
                0,
            ),
            reverse=True,
        )

        return {
            "focused_context": dict(
                prioritized,
            ),
            "priority_rules": (self._priority_rules),
        }
