"""
ShadBot Project Intelligence

Evolution Summary for Agent Context
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class EvolutionSummary:
    """
    Agent-facing summary of project evolution.

    This model exposes only stable evolution
    information required by coding agents.
    """

    recent_changes: tuple[str, ...] = field(
        default_factory=tuple,
    )

    added_files: tuple[str, ...] = field(
        default_factory=tuple,
    )

    removed_files: tuple[str, ...] = field(
        default_factory=tuple,
    )

    modified_files: tuple[str, ...] = field(
        default_factory=tuple,
    )

    impact_summary: str | None = None
