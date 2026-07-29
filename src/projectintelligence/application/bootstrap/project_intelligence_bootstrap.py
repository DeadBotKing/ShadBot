"""
ShadBot Project Intelligence

Project Intelligence Bootstrap
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from projectintelligence.infrastructure.git.git_python_repository import (
    GitPythonRepository,
)

from projectintelligence.application.context.context_builder import (
    ContextBuilder,
)
from projectintelligence.application.dependency.dependency_analyzer import (
    DependencyAnalyzer,
)
from projectintelligence.application.dependency.parser_registry import (
    ParserRegistry,
)
from projectintelligence.application.dependency.parser_selector import (
    ParserSelector,
)
from projectintelligence.application.engine.project_intelligence_engine import (
    ProjectIntelligenceEngine,
)
from projectintelligence.application.framework.framework_detector import (
    FrameworkDetector,
)
from projectintelligence.application.framework.framework_registry import (
    FrameworkRegistry,
)
from projectintelligence.application.framework.signature_matcher import (
    SignatureMatcher,
)
from projectintelligence.application.git.mapping.git_context_mapper import (
    GitContextMapper,
)
from projectintelligence.application.git.services.git_analyzer import (
    GitAnalyzer,
)
from projectintelligence.application.git.services.git_branch_detector import (
    GitBranchDetector,
)
from projectintelligence.application.git.services.git_change_detector import (
    GitChangeDetector,
)
from projectintelligence.application.git.services.git_history_analyzer import (
    GitHistoryAnalyzer,
)
from projectintelligence.application.git.services.git_status_detector import (
    GitStatusDetector,
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
from projectintelligence.application.language.extension_registry import (
    ExtensionRegistry,
)
from projectintelligence.application.language.language_detector import (
    LanguageDetector,
)
from projectintelligence.application.language.language_statistics import (
    LanguageStatistics,
)
from projectintelligence.application.orchestration.project_intelligence_orchestrator import (
    ProjectIntelligenceOrchestrator,
)
from projectintelligence.application.persistence.services.context_storage_service import (
    ContextStorageService,
)
from projectintelligence.application.persistence.services.history_storage_service import (
    HistoryStorageService,
)
from projectintelligence.application.persistence.services.knowledge_storage_service import (
    KnowledgeStorageService,
)
from projectintelligence.application.persistence.services.persistence_service import (
    PersistenceService,
)
from projectintelligence.application.persistence.services.resume_storage_service import (
    ResumeStorageService,
)
from projectintelligence.application.persistence.services.snapshot_history_service import (
    SnapshotHistoryService,
)
from projectintelligence.application.persistence.services.snapshot_storage_service import (
    SnapshotStorageService,
)
from projectintelligence.application.persistence.services.state_storage_service import (
    StateStorageService,
)
from projectintelligence.application.pipeline.project_intelligence_pipeline import (
    ProjectIntelligencePipeline,
)
from projectintelligence.application.resume.completion_analyzer import (
    CompletionAnalyzer,
)
from projectintelligence.application.resume.pending_task_analyzer import (
    PendingTaskAnalyzer,
)
from projectintelligence.application.resume.project_state_analyzer import (
    ProjectStateAnalyzer,
)
from projectintelligence.application.resume.project_summary_builder import (
    ProjectSummaryBuilder,
)
from projectintelligence.application.resume.recommendation_engine import (
    RecommendationEngine,
)
from projectintelligence.application.resume.resume_generator import (
    ResumeGenerator,
)
from projectintelligence.application.snapshot.directory_tree_builder import (
    DirectoryTreeBuilder,
)
from projectintelligence.application.snapshot.hash_calculator import (
    HashCalculator,
)
from projectintelligence.application.snapshot.snapshot_builder import (
    SnapshotBuilder,
)
from projectintelligence.application.state.builders.project_state_builder import (
    ProjectStateBuilder,
)
from projectintelligence.application.state.project_state_service import (
    ProjectStateService,
)
from projectintelligence.infrastructure.filesystem.directory_walker import (
    DirectoryWalker,
)
from projectintelligence.infrastructure.filesystem.file_collector import (
    FileCollector,
)
from projectintelligence.infrastructure.filesystem.ignore_manager import (
    IgnoreManager,
)
from projectintelligence.infrastructure.filesystem.workspace_scanner import (
    WorkspaceScanner,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_context_repository import (
    InMemoryContextRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_history_repository import (
    InMemoryHistoryRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_knowledge_repository import (
    InMemoryKnowledgeRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_resume_repository import (
    InMemoryResumeRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_snapshot_repository import (
    InMemorySnapshotRepository,
)
from projectintelligence.infrastructure.persistence.repositories.in_memory_state_repository import (
    InMemoryStateRepository,
)


@dataclass(slots=True)
class ProjectIntelligenceBootstrap:
    """
    Composition root for the Project Intelligence Engine.

    Responsible for constructing the complete dependency graph.
    """

    def build(self):
        """
        Build the complete Project Intelligence Engine.
        """
        snapshot_repository = InMemorySnapshotRepository()

        context_repository = InMemoryContextRepository()

        knowledge_repository = InMemoryKnowledgeRepository()

        history_repository = InMemoryHistoryRepository()

        state_repository = InMemoryStateRepository()

        resume_repository = InMemoryResumeRepository()

        snapshot_storage = SnapshotStorageService(
            repository=snapshot_repository,
        )

        context_storage = ContextStorageService(
            repository=context_repository,
        )

        knowledge_storage = KnowledgeStorageService(
            repository=knowledge_repository,
        )

        history_storage = HistoryStorageService(
            repository=history_repository,
        )

        state_storage = StateStorageService(
            repository=state_repository,
        )

        resume_storage = ResumeStorageService(
            repository=resume_repository,
        )

        persistence_service = PersistenceService(
            snapshot_storage=snapshot_storage,
            context_storage=context_storage,
            knowledge_storage=knowledge_storage,
            history_storage=history_storage,
            state_storage=state_storage,
            resume_storage=resume_storage,
        )

        directory_walker = DirectoryWalker()

        ignore_manager = IgnoreManager()

        file_collector = FileCollector()

        workspace_scanner = WorkspaceScanner(
            directory_walker=directory_walker,
            ignore_manager=ignore_manager,
            file_collector=file_collector,
        )

        hash_calculator = HashCalculator()

        directory_tree_builder = DirectoryTreeBuilder()

        snapshot_builder = SnapshotBuilder(
            workspace_scanner=workspace_scanner,
            hash_calculator=hash_calculator,
            directory_tree_builder=directory_tree_builder,
        )

        extension_registry = ExtensionRegistry()

        language_statistics = LanguageStatistics()

        language_detector = LanguageDetector(
            extension_registry=extension_registry,
            language_statistics=language_statistics,
        )


        framework_registry = FrameworkRegistry()

        signature_matcher = SignatureMatcher()

        framework_detector = FrameworkDetector(
            framework_registry=framework_registry,
            signature_matcher=signature_matcher,
        )


        parser_registry = ParserRegistry()

        parser_selector = ParserSelector(
            parser_registry=parser_registry,
        )

        dependency_analyzer = DependencyAnalyzer(
            parser_selector=parser_selector,
        )

        git_repository = GitPythonRepository(
            repository_path=Path.cwd(),
        )


        git_status_detector = GitStatusDetector(
            git_repository=git_repository,
        )

        git_branch_detector = GitBranchDetector(
            git_repository=git_repository,
        )

        git_change_detector = GitChangeDetector(
            git_repository=git_repository,
        )

        git_history_analyzer = GitHistoryAnalyzer(
            git_repository=git_repository,
        )


        git_analyzer = GitAnalyzer(
            status_detector=git_status_detector,
            branch_detector=git_branch_detector,
            change_detector=git_change_detector,
            history_analyzer=git_history_analyzer,
        )


        git_context_mapper = GitContextMapper()

        technology_extractor = TechnologyExtractor()

        architecture_extractor = ArchitectureExtractor()

        dependency_extractor = DependencyExtractor()

        convention_extractor = ConventionExtractor()

        constraint_extractor = ConstraintExtractor()

        history_extractor = HistoryExtractor()

        intelligence_notes_extractor = IntelligenceNotesExtractor()

        rule_engine_factory = RuleEngineFactory()


        knowledge_builder = KnowledgeBuilder(
            technology_extractor=technology_extractor,
            architecture_extractor=architecture_extractor,
            dependency_extractor=dependency_extractor,
            convention_extractor=convention_extractor,
            constraint_extractor=constraint_extractor,
            history_extractor=history_extractor,
            intelligence_notes_extractor=intelligence_notes_extractor,
            rule_engine_factory=rule_engine_factory,
        )


        context_builder = ContextBuilder()


        project_state_builder = ProjectStateBuilder()

        project_state_service = ProjectStateService(
            builder=project_state_builder,
        )

        summary_builder = ProjectSummaryBuilder()

        completion_analyzer = CompletionAnalyzer()

        pending_task_analyzer = PendingTaskAnalyzer()

        recommendation_engine = RecommendationEngine()

        project_state_analyzer = ProjectStateAnalyzer()


        resume_generator = ResumeGenerator(
            summary_builder=summary_builder,
            completion_analyzer=completion_analyzer,
            pending_task_analyzer=pending_task_analyzer,
            recommendation_engine=recommendation_engine,
            project_state_analyzer=project_state_analyzer,
        )


        snapshot_history_service = SnapshotHistoryService(
            repository=snapshot_repository,
        )

        pipeline = ProjectIntelligencePipeline(
            workspace_scanner=workspace_scanner,
            snapshot_builder=snapshot_builder,
            language_detector=language_detector,
            framework_detector=framework_detector,
            dependency_analyzer=dependency_analyzer,
            git_analyzer=git_analyzer,
            knowledge_builder=knowledge_builder,
            context_builder=context_builder,
            git_context_mapper=git_context_mapper,
            project_state_service=project_state_service,
        )


        orchestrator = ProjectIntelligenceOrchestrator(
            pipeline=pipeline,
            persistence_service=persistence_service,
            snapshot_history_service=snapshot_history_service,
            resume_generator=resume_generator,
        )


        return ProjectIntelligenceEngine(
            orchestrator=orchestrator,
        )