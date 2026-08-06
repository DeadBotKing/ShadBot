"""
ShadBot Agent Platform

Agent Profile Binding
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class ProfileBinding:
    """
    Profile capability attached to an agent.
    """

    profile: Any

    def get(
        self,
    ) -> Any:
        """
        Return agent profile.
        """

        return self.profile
