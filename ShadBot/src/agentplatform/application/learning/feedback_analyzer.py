"""
ShadBot Agent Platform

Feedback analyzer.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.domain.learning import (
    LearningEvent,
)


@dataclass(slots=True)
class FeedbackAnalyzer:
    """
    Analyze execution feedback and extract
    reusable learning signals.

    Responsibilities
    ----------------
    - Detect failures
    - Detect successful patterns
    - Extract improvement points
    - Produce normalized learning candidates

    Does not:
    - Persist data
    - Call LLM
    - Modify agent behavior directly
    """

    def analyze(
        self,
        event: LearningEvent,
    ) -> tuple[str, ...]:
        """
        Extract learning items from event.
        """

        items: list[str] = []

        content = event.content

        failures = content.get(
            "failures",
            [],
        )

        if isinstance(
            failures,
            list,
        ):
            for failure in failures:
                items.append(
                    f"failure_pattern: {failure}",
                )

        successes = content.get(
            "successes",
            [],
        )

        if isinstance(
            successes,
            list,
        ):
            for success in successes:
                items.append(
                    f"success_pattern: {success}",
                )

        improvements = content.get(
            "improvements",
            [],
        )

        if isinstance(
            improvements,
            list,
        ):
            for improvement in improvements:
                items.append(
                    f"improvement_rule: {improvement}",
                )

        return tuple(
            items,
        )
