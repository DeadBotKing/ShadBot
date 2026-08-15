"""
ShadBot Agent Platform

Agent Eye Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class EyeBinding:
    """
    Provides perception capability to an agent.

    Eyes are responsible for observing
    external project/environment state.
    """

    project_intelligence: Any

    def observe(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Observe project state through intelligence layer.
        """

        return self.project_intelligence.analyze(
            *args,
            **kwargs,
        )
