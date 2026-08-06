"""
ShadBot Agent Platform

Brain context factory.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from agentplatform.domain.context import BrainContext

from .brain_context_manager import (
    BrainContextManager,
)


class BrainContextFactory:
    """
    Creates configured brain contexts.

    Provider registration is handled
    through dependency injection.
    """

    def __init__(
        self,
        manager: BrainContextManager,
    ) -> None:

        self._manager = manager

    def register_provider(
        self,
        name: str,
        provider: Any,
    ) -> None:
        """
        Register a context provider.
        """

        self._manager.register_provider(
            name,
            provider,
        )

    def create(
        self,
        project_id: UUID,
    ) -> BrainContext:
        """
        Create final brain context.
        """

        return self._manager.build(
            project_id,
        )
