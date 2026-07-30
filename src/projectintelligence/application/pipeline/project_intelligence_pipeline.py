"""
ShadBot Project Intelligence

Project Intelligence Pipeline
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from projectintelligence.application.context.context_builder import (
    ContextBuilder,
)
from projectintelligence.application.contracts.analysis.dependency_analyzer import (
    IDependencyAnalyzer,
)
from projectintelligence.application.contracts.analysis.framework_detector import (
    IFrameworkDetector,
)
from projectintelligence.application.contracts.analysis.language_detector import (
    ILanguageDetector,
)
from projectintelligence.application.contracts.project.workspace_scanner import (
    IWorkspaceScanner,
)
from projectintelligence.application.contracts.snapshot.snapshot_builder import (
    ISnapshotBuilder,
)
from projectintelligence.application.git.mapping.git_context_mapper import (
    GitContextMapper,
)
from projectintelligence.application.git.services.git_analyzer import (
    GitAnalyzer,
)
from projectintelligence.application.knowledge.knowledge_builder import (
    KnowledgeBuilder,
)
from projectintelligence.application.pipeline.pipeline_result import (
    PipelineResult,
)
from projectintelligence.application.resume.models.resume_build_context import (
    ResumeBuildContext,
)
from projectintelligence.application.state.project_state_service import (
    ProjectStateService,
)
from projectintelligence.domain.history.snapshot_history import (
    SnapshotHistory,
)
from projectintelligence.domain.project.project_entity import (
    ProjectEntity,
)


@dataclass(slots=True)
class ProjectIntelligencePipeline:
    """
    Executes the complete Project Intelligence pipeline.
    """

    workspace_scanner: IWorkspaceScanner
    snapshot_builder: ISnapshotBuilder
    language_detector: ILanguageDetector
    framework_detector: IFrameworkDetector
    dependency_analyzer: IDependencyAnalyzer
    git_analyzer: GitAnalyzer
    knowledge_builder: KnowledgeBuilder
    context_builder: ContextBuilder
    git_context_mapper: GitContextMapper
    project_state_service: ProjectStateService

    def run(
        self,
        project: ProjectEntity,
    ) -> PipelineResult:
        """
        Execute the Project Intelligence pipeline.
        """

        files = self.workspace_scanner.scan(
            project.workspace,
        )

        snapshot = self.snapshot_builder.build(
            project,
        )

        snapshot.detected_languages = list(
            self.language_detector.detect(
                files,
            )
        )

        snapshot.detected_frameworks = list(
            self.framework_detector.detect(
                files,
            )
        )

        snapshot.dependencies = self.dependency_analyzer.analyze(
            project.workspace,
        )

        git_context = self.git_analyzer.analyze(
            project.project_id,
        )

        git_state = self.git_context_mapper.map(
            git_context,
        )

        knowledge = self.knowledge_builder.build(
            snapshot,
            git_context,
        )

        context = self.context_builder.build(
            snapshot,
            knowledge,
            git_context,
        )

        context.git_state = git_state

        history = SnapshotHistory(
            history_id=uuid4(),
            project_id=project.project_id,
            created_at=datetime.now(timezone.utc),
        )

        resume_context = ResumeBuildContext(
            snapshot=snapshot,
            knowledge=knowledge,
            history=history,
            context=context,
        )

        state = self.project_state_service.build(
            resume_context,
        )

        return PipelineResult(
            snapshot=snapshot,
            knowledge=knowledge,
            history=history,
            state=state,
            context=context,
            git_context=git_context,
        )
