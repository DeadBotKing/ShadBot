"""
ShadBot Project Intelligence

Pipeline Integration Test
"""

from pathlib import Path
from unittest.mock import Mock

from projectintelligence.application.context.context_builder import (
    ContextBuilder,
)
from projectintelligence.application.git.mapping.git_context_mapper import (
    GitContextMapper,
)
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
from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.application.state.builders.project_state_builder import (
    ProjectStateBuilder,
)
from projectintelligence.application.state.project_state_service import (
    ProjectStateService,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_project_intelligence_pipeline_integration() -> None:
    project = ProjectEntity(
        name="TestProject",
        workspace=Path("."),
    )

    workspace_scanner = Mock()
    snapshot_builder = Mock()
    language_detector = Mock()
    framework_detector = Mock()
    dependency_analyzer = Mock()
    git_analyzer = Mock()

    workspace_scanner.scan.return_value = [
        "main.py",
    ]

    snapshot_builder.build.return_value = ProjectSnapshot(
        project_id=project.project_id,
        workspace=project.workspace,
    )

    language_detector.detect.return_value = [
        "Python",
    ]

    framework_detector.detect.return_value = [
        "Django",
    ]

    dependency_analyzer.analyze.return_value = {
        "django": "5",
    }

    git_analyzer.analyze.return_value = GitContext(
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

    knowledge_builder = KnowledgeBuilder(
        technology_extractor=TechnologyExtractor(),
        architecture_extractor=ArchitectureExtractor(),
        dependency_extractor=DependencyExtractor(),
        convention_extractor=ConventionExtractor(),
        constraint_extractor=ConstraintExtractor(),
        history_extractor=HistoryExtractor(),
        intelligence_notes_extractor=IntelligenceNotesExtractor(),
        rule_engine_factory=RuleEngineFactory(),
    )

    git_context_mapper = GitContextMapper()
    context_builder = ContextBuilder()

    project_state_builder = ProjectStateBuilder()

    project_state_service = ProjectStateService(
        builder=project_state_builder,
    )

    pipeline = ProjectIntelligencePipeline(
        workspace_scanner=workspace_scanner,
        snapshot_builder=snapshot_builder,
        language_detector=language_detector,
        framework_detector=framework_detector,
        dependency_analyzer=dependency_analyzer,
        git_analyzer=git_analyzer,
        knowledge_builder=knowledge_builder,
        git_context_mapper=git_context_mapper,
        context_builder=context_builder,
        project_state_service=project_state_service,
    )

    result = pipeline.run(project)

    assert result.success is True
    assert result.snapshot is not None
    assert result.context is not None
    assert result.context.git_state is not None
    assert result.context.git_state.branch_name == "main"
