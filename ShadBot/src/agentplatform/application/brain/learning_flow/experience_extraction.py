"""
ShadBot Agent Platform

Experience Extraction component for 5.11 Learning Flow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence
from agentplatform.domain.results import AgentResult


@dataclass(frozen=True, slots=True)
class ExtractedExperience:
    agent_name: str
    success: bool
    lesson_learned: str
    reusable_pattern: str | None


class ExperienceExtractor:
    """
    Extracts reusable lessons and experiences from agent results.
    """

    def extract(self, results: Sequence[AgentResult]) -> tuple[ExtractedExperience, ...]:
        experiences: list[ExtractedExperience] = []
        for r in results:
            agent = str(r.data.get("agent", "unknown"))
            lesson = "Successful workflow standard" if r.success else f"Avoid failure condition: {r.message}"
            pattern = "Layered service pattern" if (r.success and agent == "architect") else None
            experiences.append(
                ExtractedExperience(
                    agent_name=agent,
                    success=r.success,
                    lesson_learned=lesson,
                    reusable_pattern=pattern,
                )
            )
        return tuple(experiences)
