"""
ShadBot Agent Platform

Capability Executor
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from agentplatform.application.agents import RuntimeAgent
from agentplatform.domain.agents import AgentCapability


@dataclass(frozen=True, slots=True)
class CapabilityExecutionResult:
    """
    Standard capability execution result.
    """

    capability: AgentCapability

    success: bool

    output: Any = None

    error: str | None = None


class CapabilityExecutor:
    """
    Enterprise capability execution engine.

    Responsibilities
    ----------------
    - Verify capability ownership.
    - Resolve runtime binding.
    - Execute capability.
    - Normalize outputs.
    - Catch execution failures.
    """

    def execute(
        self,
        *,
        agent: RuntimeAgent,
        capability: AgentCapability,
        **kwargs: Any,
    ) -> CapabilityExecutionResult:

        if not agent.supports(capability):

            return CapabilityExecutionResult(
                capability=capability,
                success=False,
                error=(
                    f"Agent '{agent.role.value}' "
                    f"does not support capability "
                    f"'{capability.value}'."
                ),
            )

        try:

            handler = self._resolve_handler(
                agent=agent,
                capability=capability,
            )

            result = handler(
                **kwargs,
            )

            return CapabilityExecutionResult(
                capability=capability,
                success=True,
                output=result,
            )

        except Exception as exc:

            return CapabilityExecutionResult(
                capability=capability,
                success=False,
                error=str(exc),
            )

    def _resolve_handler(
        self,
        *,
        agent: RuntimeAgent,
        capability: AgentCapability,
    ) -> Callable[..., Any]:

        mapping: dict[
            AgentCapability,
            Callable[..., Any],
        ] = {
            AgentCapability.ARCHITECTURE_ANALYSIS: agent.eyes.observe,
            AgentCapability.DESIGN_REVIEW: agent.reasoning.reason,
            AgentCapability.DEPENDENCY_ANALYSIS: agent.reasoning.reason,
            AgentCapability.CODE_GENERATION: agent.reasoning.reason,
            AgentCapability.CODE_REFACTORING: agent.reasoning.reason,
            AgentCapability.TEST_GENERATION: agent.reasoning.reason,
            AgentCapability.CODE_REVIEW: agent.validation.validate,
            AgentCapability.BUG_DETECTION: agent.validation.validate,
            AgentCapability.SECURITY_REVIEW: agent.validation.validate,
            AgentCapability.RESEARCH: agent.reasoning.reason,
            AgentCapability.TRADING_ANALYSIS: agent.reasoning.reason,
            AgentCapability.FEATURE_ENGINEERING: agent.learning.learn,
            AgentCapability.MODEL_EVALUATION: agent.learning.improve,
        }

        handler = mapping.get(
            capability,
        )

        if handler is None:

            raise RuntimeError(f"No executor mapped for " f"{capability.value}")

        return handler
