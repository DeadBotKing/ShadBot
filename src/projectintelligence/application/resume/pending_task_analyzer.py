"""
ShadBot Project Intelligence

Pending Task Analyzer
"""

from __future__ import annotations

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.resume.pending_work import (
    PendingWork,
)


class PendingTaskAnalyzer:
    """
    Analyzes unfinished project intelligence tasks.
    """

    def analyze(
        self,
        context: ResumeBuildContext,
    ) -> list[PendingWork]:
        """
        Detect pending work from current project state.
        """

        pending: list[PendingWork] = []

        if not context.snapshot.detected_languages:
            pending.append(
                PendingWork(
                    title="Language Detection",
                    description=(
                        "Project programming languages have not been analyzed."
                    ),
                    category="Analysis",
                    priority="High",
                    reason=(
                        "Language intelligence is required for deeper "
                        "project understanding."
                    ),
                )
            )

        if not context.snapshot.detected_frameworks:
            pending.append(
                PendingWork(
                    title="Framework Detection",
                    description=("Project frameworks have not been identified."),
                    category="Analysis",
                    priority="Medium",
                    reason=("Framework awareness improves architecture analysis."),
                )
            )

        if not context.knowledge.dependency_map:
            pending.append(
                PendingWork(
                    title="Dependency Analysis",
                    description=("Project dependencies have not been mapped."),
                    category="Knowledge",
                    priority="High",
                    reason=("Dependency knowledge is required for agent decisions."),
                )
            )

        if not context.knowledge.architecture_patterns:
            pending.append(
                PendingWork(
                    title="Architecture Analysis",
                    description=("Architecture patterns have not been identified."),
                    category="Architecture",
                    priority="Medium",
                    reason=("Architecture understanding is incomplete."),
                )
            )

        if not context.history.differences:
            pending.append(
                PendingWork(
                    title="Project Evolution Tracking",
                    description=("Historical project changes are not available."),
                    category="History",
                    priority="Low",
                    reason=("Historical awareness improves future planning."),
                )
            )

        if not context.snapshot.test_status:
            pending.append(
                PendingWork(
                    title="Testing Intelligence",
                    description=("Project testing status has not been analyzed."),
                    category="Quality",
                    priority="Medium",
                    reason=(
                        "Quality visibility is required for reliable "
                        "engineering decisions."
                    ),
                )
            )

        return pending
