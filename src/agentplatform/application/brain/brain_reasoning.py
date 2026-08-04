"""
ShadBot Agent Platform

Brain reasoning engine.
"""

from __future__ import annotations

from agentplatform.application.llm import LLMProvider
from agentplatform.application.prompt import PromptBuilder
from agentplatform.domain.agents import AgentRole
from agentplatform.domain.context import AgentExecutionContext


class BrainReasoning:
    """
    Responsible for LLM reasoning execution.
    """

    def __init__(
        self,
        llm: LLMProvider,
        prompt_builder: PromptBuilder | None = None,
    ) -> None:
        self._llm = llm
        self._prompt_builder = prompt_builder or PromptBuilder()

    def reason(
        self,
        role: AgentRole,
        context: AgentExecutionContext,
    ) -> str:
        """
        Execute reasoning process.
        """

        prompt = self._prompt_builder.build(
            role,
            context,
        )

        if hasattr(
            self._llm,
            "generate_for_agent",
        ):
            return self._llm.generate_for_agent(
                role,
                prompt,
            )

        response = self._llm.generate(
            prompt,
        )

        return str(response)
