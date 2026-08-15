"""
ShadBot Agent Platform

Brain context manager.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from agentplatform.domain.context import BrainContext

from .brain_context_registry import (
    BrainContextRegistry,
)


class BrainContextManager:
    """
    Builds unified context for Agent Brain.

    Responsible for:
    - Provider orchestration
    - Context aggregation
    - BrainContext creation
    """

    def __init__(
        self,
        registry: BrainContextRegistry | None = None,
    ) -> None:

        self._registry = registry or BrainContextRegistry()

    def register_provider(
        self,
        name: str,
        provider: Any,
    ) -> None:
        """
        Register context provider.
        """

        self._registry.register(
            name,
            provider,
        )

    def build(
        self,
        project_id: UUID,
    ) -> BrainContext:
        """
        Build unified brain context.
        """

        contexts: dict[str, dict[str, Any]] = {}

        for name, provider in self._registry.get_providers().items():
            contexts[name] = provider.provide()

        return BrainContext(
            project_id=project_id,
            project_intelligence=contexts.get(
                "project_intelligence",
                {},
            ),
            memory_context=contexts.get(
                "memory",
                {},
            ),
            goal_context=contexts.get(
                "goal",
                {},
            ),
            attention_context=contexts.get(
                "attention",
                {},
            ),
            planning_context=contexts.get(
                "planning",
                {},
            ),
            reasoning_context=contexts.get(
                "reasoning",
                {},
            ),
            decision_context=contexts.get(
                "decision",
                {},
            ),
            reflection_context=contexts.get(
                "reflection",
                {},
            ),
            validation_context=contexts.get(
                "validation",
                {},
            ),
            profile_context=contexts.get(
                "profile",
                {},
            ),
            learning_context=contexts.get(
                "learning",
                {},
            ),
        )
