"""
ShadBot Agent Platform

Goal analyzer.
"""

from __future__ import annotations

from uuid import UUID

from agentplatform.domain.goal import (
    Goal,
    Intent,
    IntentType,
)


class GoalAnalyzer:
    """
    Converts raw requests into structured goals.
    """

    def analyze(
        self,
        project_id: UUID,
        request: str,
        context: dict[str, object] | None = None,
    ) -> Goal:
        """
        Analyze user request and create goal.
        """

        intent = self._detect_intent(
            request,
        )

        return Goal(
            project_id=project_id,
            description=request,
            intent=intent,
            expected_output=self._extract_outputs(
                request,
            ),
            constraints=self._extract_constraints(
                context,
            ),
            success_criteria=self._build_success_criteria(
                request,
            ),
            priority=self._estimate_priority(
                request,
            ),
        )

    def _detect_intent(
        self,
        request: str,
    ) -> Intent:
        """
        Detect request intention.
        """

        text = request.lower()

        mapping = (
            ("fix", IntentType.FIX),
            ("bug", IntentType.FIX),
            ("create", IntentType.CREATE),
            ("build", IntentType.CREATE),
            ("modify", IntentType.MODIFY),
            ("change", IntentType.MODIFY),
            ("optimize", IntentType.OPTIMIZE),
            ("analyze", IntentType.ANALYZE),
            ("explain", IntentType.EXPLAIN),
            ("review", IntentType.REVIEW),
            ("continue", IntentType.CONTINUE),
        )

        for keyword, intent_type in mapping:
            if keyword in text:
                return Intent(
                    intent_type=intent_type,
                    confidence=0.8,
                    explanation=(f"Detected by keyword: {keyword}"),
                )

        return Intent(
            intent_type=IntentType.EXECUTE,
            confidence=0.5,
            explanation="Default execution intent.",
        )

    @staticmethod
    def _extract_outputs(
        request: str,
    ) -> tuple[str, ...]:
        """
        Estimate expected outputs.
        """

        return (
            "completed task result",
            "validated execution outcome",
        )

    @staticmethod
    def _extract_constraints(
        context: dict[str, object] | None,
    ) -> tuple[str, ...]:
        """
        Extract known constraints.
        """

        if not context:
            return ()

        constraints = context.get(
            "constraints",
            [],
        )

        if not isinstance(
            constraints,
            list,
        ):
            return ()

        return tuple(str(item) for item in constraints)

    @staticmethod
    def _build_success_criteria(
        request: str,
    ) -> tuple[str, ...]:
        """
        Define completion criteria.
        """

        return (
            "requested objective achieved",
            "result validated",
        )

    @staticmethod
    def _estimate_priority(
        request: str,
    ) -> int:
        """
        Estimate priority.
        """

        text = request.lower()

        if "urgent" in text:
            return 10

        if "critical" in text:
            return 10

        return 5
