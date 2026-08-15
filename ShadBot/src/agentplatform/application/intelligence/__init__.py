"""
ShadBot Agent Platform

Application intelligence module.
"""

from .evolution_service import (
    EvolutionService,
)
from .project_intelligence_factory import (
    ProjectIntelligenceFactory,
)
from .project_intelligence_lifecycle import (
    ProjectIntelligenceLifecycle,
)
from .project_vision_builder import (
    ProjectVisionBuilder,
)
from .project_vision_service import (
    ProjectVisionService,
)

__all__ = [
    "EvolutionService",
    "ProjectIntelligenceFactory",
    "ProjectIntelligenceLifecycle",
    "ProjectVisionBuilder",
    "ProjectVisionService",
]
