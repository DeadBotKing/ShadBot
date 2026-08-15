"""
ShadBot Agent Platform

Episodic memory.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class Episode:

    id: UUID

    agent: str

    event: str

    result: dict[str, Any]

    created_at: datetime


class EpisodicMemory:
    """
    Stores past agent executions.
    """

    def __init__(self) -> None:
        self._episodes: list[Episode] = []

    def remember(
        self,
        agent: str,
        event: str,
        result: dict[str, Any],
    ) -> Episode:

        episode = Episode(
            id=uuid4(),
            agent=agent,
            event=event,
            result=result,
            created_at=datetime.now(
                timezone.utc,
            ),
        )

        self._episodes.append(
            episode,
        )

        return episode

    def recall(
        self,
        agent: str,
    ) -> list[Episode]:

        return [item for item in self._episodes if item.agent == agent]
