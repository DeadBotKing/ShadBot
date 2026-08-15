"""
ShadBot Agent Platform

LLM Provider contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentplatform.domain.agents import AgentRole


class LLMProvider(ABC):
    """
    Base contract for all LLM providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text from prompt.
        """

        raise NotImplementedError

    def generate_for_agent(
        self,
        role: AgentRole,
        prompt: str,
    ) -> str:
        """
        Generate text for specific agent role.

        Default implementation falls back
        to generic generation.
        """

        return self.generate(
            prompt,
        )
