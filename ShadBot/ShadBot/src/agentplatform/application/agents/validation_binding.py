"""
ShadBot Agent Platform

Agent Validation Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from agentplatform.application.brain.brain_validation import (
    BrainValidation,
)


@dataclass(frozen=True, slots=True)
class ValidationBinding:
    """
    Validation capability attached to an agent.
    """

    validation: BrainValidation

    def validate(
        self,
        target: Any,
    ) -> dict[str, object]:
        """
        Validate execution output.
        """

        return self.validation.validate(
            target,
        )
