"""
ShadBot Project Intelligence

Project Intelligence Bootstrap Tests
"""

from pathlib import Path

from projectintelligence.application.bootstrap.project_intelligence_bootstrap import (
    ProjectIntelligenceBootstrap,
)
from projectintelligence.application.engine.project_intelligence_engine import (
    ProjectIntelligenceEngine,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


def test_project_intelligence_bootstrap_builds_engine():
    """
    Bootstrap should create a fully wired Project Intelligence Engine.
    """

    bootstrap = ProjectIntelligenceBootstrap()

    project = ProjectEntity(
        name="Test Project",
        workspace=Path.cwd(),
    )

    engine = bootstrap.build(
        project=project,
    )

    assert isinstance(
        engine,
        ProjectIntelligenceEngine,
    )

    assert engine.orchestrator is not None
