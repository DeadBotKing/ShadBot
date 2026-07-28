"""
ShadBot Project Intelligence

Recommendation Engine
"""

from __future__ import annotations

from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.domain.resume.project_recommendation import (
    ProjectRecommendation,
)


class RecommendationEngine:
    """
    Generates actionable recommendations from project intelligence.
    """

    def generate(
        self,
        context: ResumeBuildContext,
    ) -> list[ProjectRecommendation]:
        """
        Generate recommendations based on current project state.
        """

        recommendations: list[ProjectRecommendation] = []

        if not context.snapshot.test_status:
            recommendations.append(
                ProjectRecommendation(
                    title="Add Testing Intelligence",
                    description=(
                        "Analyze project tests and determine current "
                        "testing coverage and quality status."
                    ),
                    priority="Medium",
                    rationale=(
                        "Testing visibility is required before autonomous "
                        "engineering operations."
                    ),
                    expected_outcome=(
                        "Agents can make safer changes with quality awareness."
                    ),
                )
            )

        if not context.knowledge.architecture_patterns:
            recommendations.append(
                ProjectRecommendation(
                    title="Complete Architecture Analysis",
                    description=(
                        "Extract architectural patterns and project design "
                        "decisions."
                    ),
                    priority="High",
                    rationale=(
                        "Architecture understanding is required for "
                        "planning complex modifications."
                    ),
                    expected_outcome=(
                        "AI agents gain architecture-aware reasoning."
                    ),
                )
            )

        if not context.history.differences:
            recommendations.append(
                ProjectRecommendation(
                    title="Enable Project Evolution Tracking",
                    description=(
                        "Collect snapshot differences to understand project "
                        "changes over time."
                    ),
                    priority="Low",
                    rationale=(
                        "Historical context improves future recommendations."
                    ),
                    expected_outcome=(
                        "The system can reason about project evolution."
                    ),
                )
            )

        if not recommendations:
            recommendations.append(
                ProjectRecommendation(
                    title="Continue Engineering Analysis",
                    description=(
                        "Project intelligence baseline is available; "
                        "continue deeper analysis."
                    ),
                    priority="Low",
                    rationale=(
                        "Continuous analysis improves project understanding."
                    ),
                    expected_outcome=(
                        "More accurate context becomes available to agents."
                    ),
                )
            )

        return recommendations