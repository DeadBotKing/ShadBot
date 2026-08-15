"""
ShadBot Agent Platform

Plugin Architecture component for Phase 11 Platform Finalization.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class LoadedPlugin:
    plugin_name: str
    version: str
    enabled: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "plugin_name": self.plugin_name,
            "version": self.version,
            "enabled": self.enabled,
        }


class PluginManager:
    """
    Discovers, loads, and manages platform extension plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, LoadedPlugin] = {}

    def load_plugin(self, name: str, version: str = "1.0") -> LoadedPlugin:
        plg = LoadedPlugin(name, version, True)
        self._plugins[name] = plg
        return plg

    def list_plugins(self) -> tuple[LoadedPlugin, ...]:
        return tuple(self._plugins.values())
