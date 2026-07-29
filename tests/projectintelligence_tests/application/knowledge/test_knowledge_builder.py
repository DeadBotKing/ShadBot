from __future__ import annotations

from pathlib import Path
from uuid import uuid4

from projectintelligence.application.git.models.git_context import (
    GitContext,
)
from projectintelligence.application.git.models.git_status import (
    GitStatus,
)
from projectintelligence.application.knowledge.extractors.architecture_extractor import (
    ArchitectureExtractor,
)
from projectintelligence.application.knowledge.extractors.constraint_extractor import (
    ConstraintExtractor,
)
from projectintelligence.application.knowledge.extractors.convention_extractor import (
    ConventionExtractor,
)
from projectintelligence.application.knowledge.extractors.dependency_extractor import (
    DependencyExtractor,
)
from projectintelligence.application.knowledge.extractors.history_extractor import (
    HistoryExtractor,
)
from projectintelligence.application.knowledge.extractors.intelligence_notes_extractor import (
    IntelligenceNotesExtractor,
)
from projectintelligence.application.knowledge.extractors.technology_extractor import (
    TechnologyExtractor,
)
from projectintelligence.application.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from projectintelligence.application.knowledge.rules.factories.rule_engine_factory import (
    RuleEngineFactory,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_knowledge_builder_builds_project_knowledge() -> None:
    snapshot = ProjectSnapshot(
        project_id=uuid4(),
        workspace=Path("."),
    )

    snapshot.detected_languages = ["Python"]
    snapshot.detected_frameworks = ["Django"]
    snapshot.dependencies = {
        "django": "5",
    }

    git_context = GitContext(
        status=GitStatus(
            is_repository=True,
            is_dirty=False,
            ahead=0,
            behind=0,
            current_branch="main",
        ),
        current_commit=None,
        branches=(),
        changes=(),
        recent_commits=(),
    )

    builder = KnowledgeBuilder(
        technology_extractor=TechnologyExtractor(),
        architecture_extractor=ArchitectureExtractor(),
        dependency_extractor=DependencyExtractor(),
        convention_extractor=ConventionExtractor(),
        constraint_extractor=ConstraintExtractor(),
        history_extractor=HistoryExtractor(),
        intelligence_notes_extractor=IntelligenceNotesExtractor(),
        rule_engine_factory=RuleEngineFactory(),
    )

    knowledge = builder.build(
        snapshot,
        git_context,
    )

    assert knowledge.project_id == snapshot.project_id

    assert "Python" in knowledge.languages

    assert "Django" in knowledge.frameworks

    assert "django" in knowledge.dependency_map
