"""
ShadBot Agent Platform

Resource Attention component for 5.13 Attention Flow.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ResourceLimitSet:
    max_tokens: int
    max_context_items: int
    allow_deep_reasoning: bool


class ResourceAttentionManager:
    """
    Sets runtime token and context limits based on primary attention allocation.
    """

    def set_limits(self, primary_topic: str) -> ResourceLimitSet:
        if "architecture" in primary_topic.lower() or "critical" in primary_topic.lower():
            return ResourceLimitSet(
                max_tokens=8192,
                max_context_items=50,
                allow_deep_reasoning=True,
            )
        return ResourceLimitSet(
            max_tokens=4096,
            max_context_items=20,
            allow_deep_reasoning=False,
        )
