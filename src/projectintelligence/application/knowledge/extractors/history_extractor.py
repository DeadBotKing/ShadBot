"""
ShadBot Project Intelligence

History Extractor
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.application.git.models.git_context import (
    GitContext,
)


@dataclass(slots=True)
class HistoryExtractor:
    """
    Extracts historical knowledge from Git analysis.
    """

    def extract(
        self,
        git_context: GitContext,
    ) -> list[str]:
        """
        Extract historical project changes.
        """

        history: list[str] = []

        for commit in git_context.recent_commits:
            history.append(
                f"{commit.short_hash}: {commit.message}",
            )

        return history
