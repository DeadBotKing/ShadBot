"""
ShadBot Agent Platform

Semantic memory.
"""

from __future__ import annotations

from typing import Any


class SemanticMemory:
    """
    Stores permanent knowledge.
    """

    def __init__(self) -> None:
        self._knowledge: dict[
            str,
            dict[str, Any],
        ] = {}

    def store(
        self,
        key: str,
        value: dict[str, Any],
    ) -> None:

        self._knowledge[key] = value

    def retrieve(
        self,
        key: str,
    ) -> dict[str, Any]:

        return self._knowledge.get(
            key,
            {},
        )
