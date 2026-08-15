"""
ShadBot Agent Platform

Self improvement engine.
"""

from __future__ import annotations

from agentplatform.application.improvement.self_improvement_contract import (
    SelfImprovementContract,
)
from agentplatform.domain.improvement import (
    ImprovementRequest,
    ImprovementResult,
)


class ImprovementEngine:
    """
    Coordinates self improvement lifecycle.

    Flow:

    Request
      ↓
    Analyze
      ↓
    Validate
      ↓
    Apply

    The engine does not own:
    - LLM reasoning
    - memory
    - code generation
    - model training

    It only orchestrates improvement.
    """

    def __init__(
        self,
        contract: SelfImprovementContract,
    ) -> None:

        self._contract = contract

    def execute(
        self,
        request: ImprovementRequest,
    ) -> ImprovementResult:
        """
        Execute improvement lifecycle.
        """

        result = self._contract.analyze(
            request,
        )

        if not self._contract.validate(
            result,
        ):
            return result

        self._contract.apply(
            result,
        )

        return result
