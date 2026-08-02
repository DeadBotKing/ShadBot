"""
ShadBot Agent Platform

LLM model routing.
"""

from __future__ import annotations

from agentplatform.domain.agents import AgentRole


class ModelRouter:
    """
    Selects LLM model based on agent role.
    """

    def resolve(
        self,
        role: AgentRole,
    ) -> str:
        if role is AgentRole.ARCHITECT:
            return "qwen2.5-coder-14b-dev"

        if role is AgentRole.REVIEWER:
            return "qwen2.5-coder-14b-dev"

        if role is AgentRole.ENGINEER:
            return "qwen2.5-coder-14b-dev"

        if role is AgentRole.RESEARCHER:
            return "deepseek-coder:6.7b"

        if role is AgentRole.TRADER:
            return "qwen2.5-coder:7b"

        raise ValueError(
            f"Unsupported agent role: {role}",
        )
