"""
ShadBot Project Intelligence

Project Intelligence Bootstrap Tests
"""

from projectintelligence.application.bootstrap.project_intelligence_bootstrap import (
    ProjectIntelligenceBootstrap,
)
from projectintelligence.application.engine.project_intelligence_engine import (
    ProjectIntelligenceEngine,
)


def test_project_intelligence_bootstrap_builds_engine():
    """
    Bootstrap should create a fully wired Project Intelligence Engine.
    """

    bootstrap = ProjectIntelligenceBootstrap()

    engine = bootstrap.build()

    assert isinstance(
        engine,
        ProjectIntelligenceEngine,
    )

    assert engine.orchestrator is not None
