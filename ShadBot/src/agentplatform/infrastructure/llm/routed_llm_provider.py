"""
ShadBot Agent Platform

Routed LLM provider.
"""

from __future__ import annotations

from agentplatform.application.llm import LLMProvider
from agentplatform.domain.agents import AgentRole

from .model_router import ModelRouter
from .ollama_provider import OllamaProvider


class RoutedLLMProvider(LLMProvider):
    """
    LLM provider with agent-aware model routing.
    """

    def __init__(
        self,
        router: ModelRouter | None = None,
    ) -> None:
        self._router = router or ModelRouter()

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text.

        Default fallback model.
        """

        provider = OllamaProvider(
            model="qwen2.5-coder:7b",
        )

        return provider.generate(
            prompt,
        )

    def generate_for_agent(
        self,
        role: AgentRole,
        prompt: str,
    ) -> str:
        """
        Generate response using selected agent model.
        """

        model = self._router.resolve(
            role,
        )

        provider = OllamaProvider(
            model=model,
        )

        return provider.generate(
            prompt,
        )
