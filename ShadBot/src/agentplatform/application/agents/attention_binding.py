"""
ShadBot Agent Platform

Agent Attention Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class AttentionBinding:
    """
    Attention capability attached to an agent.
    """

    attention_provider: Any

    def focus(
        self,
        context: Any,
    ) -> Any:
        """
        Select relevant context.
        """

        return self.attention_provider.select(
            context,
        )
