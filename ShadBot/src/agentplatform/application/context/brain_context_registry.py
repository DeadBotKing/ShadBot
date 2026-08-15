"""
ShadBot Agent Platform

Brain context provider registry.
"""

from __future__ import annotations

from typing import Any


class BrainContextRegistry:
    """
    Registry for brain context providers.
    """

    def __init__(self) -> None:
        self._providers: dict[str, Any] = {}

    def register(
        self,
        name: str,
        provider: Any,
    ) -> None:
        """
        Register provider.
        """

        self._providers[name] = provider

    def get_providers(
        self,
    ) -> dict[str, Any]:
        """
        Return registered providers.
        """

        return self._providers.copy()
