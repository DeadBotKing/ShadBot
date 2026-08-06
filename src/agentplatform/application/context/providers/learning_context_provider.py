"""
ShadBot Agent Platform

Learning loop context provider.
"""

from __future__ import annotations

from typing import Any


class LearningContextProvider:
    """
    Provides self improvement context.
    """

    def __init__(
        self,
        learning_service: Any,
    ) -> None:

        self._learning_service = learning_service

    def provide(
        self,
    ) -> dict[str, Any]:
        """
        Build learning context.
        """

        if hasattr(
            self._learning_service,
            "context",
        ):
            return self._learning_service.context()

        return {
            "status": "ready",
            "source": "learning_loop",
        }
