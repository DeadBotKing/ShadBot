"""
ShadBot Agent Platform

Agent experience memory.
"""

from __future__ import annotations

from typing import Any


class ExperienceMemory:
    """
    Stores learned behaviors.
    """

    def __init__(self) -> None:
        self._experiences: list[dict[str, Any]] = []

    def add(
        self,
        experience: dict[str, Any],
    ) -> None:

        self._experiences.append(
            experience,
        )

    def all(
        self,
    ) -> list[dict[str, Any]]:

        return list(
            self._experiences,
        )
