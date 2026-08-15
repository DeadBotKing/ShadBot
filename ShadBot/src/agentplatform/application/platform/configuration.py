"""
ShadBot Agent Platform

Configuration System component for Phase 11 Platform Finalization.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class PlatformConfigPackage:
    environment: str
    debug: bool
    default_llm_model: str
    max_concurrent_agents: int
    settings: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, object]:
        return {
            "environment": self.environment,
            "debug": self.debug,
            "default_llm_model": self.default_llm_model,
            "max_concurrent_agents": self.max_concurrent_agents,
            "settings": self.settings,
        }


class ConfigurationManager:
    """
    Loads, validates, and manages platform configuration settings.
    """

    def get_config(self, env: str = "production") -> PlatformConfigPackage:
        return PlatformConfigPackage(
            environment=env,
            debug=(env == "development"),
            default_llm_model="qwen3-coder-next:latest",
            max_concurrent_agents=8,
            settings={"enable_model_routing": True, "strict_quality_gate": True},
        )
