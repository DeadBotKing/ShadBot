"""
ShadBot Agent Platform

Reasoning engine.
"""

from __future__ import annotations

from agentplatform.application.llm import LLMProvider
from agentplatform.application.prompt import PromptBuilder
from agentplatform.domain.cognition import (
    ReasoningRequest,
    ReasoningResult,
)


class ReasoningEngine:
    """
    Core reasoning capability.

    Responsibilities:
    - Convert reasoning request into prompt
    - Execute LLM reasoning
    - Produce structured reasoning result
    """

    def __init__(
        self,
        llm_provider: LLMProvider,
        prompt_builder: PromptBuilder | None = None,
    ) -> None:

        self._llm_provider = llm_provider
        self._prompt_builder = prompt_builder or PromptBuilder()

    def execute(
        self,
        request: ReasoningRequest,
    ) -> ReasoningResult:
        """
        Execute reasoning process.
        """

        try:
            prompt = self._prompt_builder.build(
                request.agent_role,
                request.context,
            )

            if hasattr(
                self._llm_provider,
                "generate_for_agent",
            ):
                response = self._llm_provider.generate_for_agent(
                    request.agent_role,
                    prompt,
                )
            else:
                response = self._llm_provider.generate(
                    prompt,
                )

            return ReasoningResult(
                success=True,
                response=str(response),
                confidence=1.0,
                metadata={
                    "mode": request.mode.value,
                    "agent_role": request.agent_role.value,
                    "objective": request.objective,
                },
            )

        except Exception as exc:
            return ReasoningResult(
                success=False,
                response="",
                confidence=0.0,
                metadata={
                    "error": str(exc),
                    "mode": request.mode.value,
                },
            )
