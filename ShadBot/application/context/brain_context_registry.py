"""
ShadBot Agent Platform

Brain context provider registry.
"""

from __future__ import annotations

from typing import Any


class BrainContextRegistry:
    """
    Stores registered context providers.
    """

    def __init__(self) -> None:
        self._providers: dict[str, Any] = {}

    def register(
        self,
        name: str,
        provider: Any,
    ) -> None:
        self._providers[name] = provider

    def providers(
        self,
    ) -> dict[str, Any]:
        return self._providers.copy()