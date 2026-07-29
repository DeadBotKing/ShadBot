"""
ShadBot Project Intelligence

Completion Analyzer
"""

from __future__ import annotations

from datetime import datetime, timezone

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.resume.completed_work import (
    CompletedWork,
)


class CompletionAnalyzer:
    """
    Analyzes completed project components from intelligence artifacts.
    """

    def analyze(
        self,
        context: ResumeBuildContext,
    ) -> list[CompletedWork]:
        """
        Detect completed work units from project intelligence data.
        """

        completed: list[CompletedWork] = []

        now = datetime.now(timezone.utc)

        if context.snapshot.detected_languages:
            completed.append(
                CompletedWork(
                    title="Language Detection",
                    description=(
                        "Project programming languages have been identified "
                        "through workspace analysis."
                    ),
                    category="Analysis",
                    completed_at=now,
                    impact=(
                        "Enables language-aware project understanding "
                        "for downstream intelligence services."
                    ),
                )
            )

        if context.snapshot.detected_frameworks:
            completed.append(
                CompletedWork(
                    title="Framework Detection",
                    description=(
                        "Project frameworks have been detected from "
                        "workspace structure and dependencies."
                    ),
                    category="Analysis",
                    completed_at=now,
                    impact=(
                        "Provides technology context for architectural "
                        "reasoning."
                    ),
                )
            )

        if context.knowledge.dependency_map:
            completed.append(
                CompletedWork(
                    title="Dependency Analysis",
                    description=(
                        "Project dependencies have been analyzed and mapped."
                    ),
                    category="Knowledge",
                    completed_at=now,
                    impact=(
                        "Allows agents to understand external project "
                        "requirements."
                    ),
                )
            )

        if context.knowledge.architecture_patterns:
            completed.append(
                CompletedWork(
                    title="Architecture Analysis",
                    description=(
                        "Architectural patterns have been extracted "
                        "from project knowledge."
                    ),
                    category="Architecture",
                    completed_at=now,
                    impact=(
                        "Improves architecture-aware planning."
                    ),
                )
            )

        if context.history.differences:
            completed.append(
                CompletedWork(
                    title="Project Evolution Tracking",
                    description=(
                        "Historical changes have been analyzed."
                    ),
                    category="History",
                    completed_at=now,
                    impact=(
                        "Provides project evolution awareness."
                    ),
                )
            )

        return completed