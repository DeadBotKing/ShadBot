"""
ShadBot Project Intelligence

Configuration Container
"""

from __future__ import annotations

from dataclasses import dataclass

from projectintelligence.configuration.git_settings import (
    GitSettings,
)
from projectintelligence.configuration.intelligence_settings import (
    IntelligenceSettings,
)
from projectintelligence.configuration.project_settings import (
    ProjectSettings,
)
from projectintelligence.configuration.storage_settings import (
    StorageSettings,
)


@dataclass(slots=True)
class ConfigurationContainer:
    """
    Central configuration holder.
    """

    project: ProjectSettings

    storage: StorageSettings

    git: GitSettings

    intelligence: IntelligenceSettings
