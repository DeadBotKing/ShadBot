"""
ShadBot Agent Platform

Learning Loop orchestrator.
"""

from __future__ import annotations

from dataclasses import dataclass

from agentplatform.application.learning.feedback_analyzer import (
    FeedbackAnalyzer,
)
from agentplatform.application.learning.learning_engine import (
    LearningEngine,
)
from agentplatform.application.learning.learning_policy import (
    LearningPolicy,
)
from agentplatform.application.learning.learning_result_merger import (
    LearningResultMerger,
)
from agentplatform.application.learning.learning_validator import (
    LearningValidator,
)
from agentplatform.domain.learning import (
    LearningEvent,
    LearningResult,
    LearningStatus,
)


@dataclass(slots=True)
class LearningLoop:
    """
    Complete autonomous learning lifecycle.

    Pipeline
    --------
    Event
      ↓
    Policy Check
      ↓
    Feedback Analysis
      ↓
    Learning Engine
      ↓
    Validation
      ↓
    Result

    Does not:
    - Persist memory
    - Call LLM directly
    - Modify agent behavior

    Integration points:
    - Brain
    - Memory System
    - Reflection System
    """

    policy: LearningPolicy

    analyzer: FeedbackAnalyzer

    engine: LearningEngine

    validator: LearningValidator

    merger: LearningResultMerger

    def run(
        self,
        event: LearningEvent,
    ) -> LearningResult:
        """
        Execute one complete learning cycle.
        """

        if not self.policy.should_learn(
            event,
        ):
            return LearningResult(
                status=LearningStatus.FAILED,
                learned_items=(),
                confidence=0.0,
                summary="Learning policy rejected event.",
            )

        items = self.analyzer.analyze(
            event,
        )

        confidence = self.policy.calculate_confidence(
            event,
        )

        result = self.engine.process(
            event=event,
            learned_items=items,
            confidence=confidence,
            summary="Learning cycle completed.",
        )

        if not self.validator.validate(
            result,
        ):
            return LearningResult(
                status=LearningStatus.FAILED,
                learned_items=result.learned_items,
                confidence=result.confidence,
                summary="Learning validation failed.",
            )

        return self.merger.merge(
            [
                result,
            ],
        )
