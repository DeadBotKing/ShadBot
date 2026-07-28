"""
ShadBot Project Intelligence

Knowledge Builder
"""

from __future__ import annotations

from dataclasses import dataclass

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
from projectintelligence.application.knowledge.rules.factories.rule_engine_factory import (
    RuleEngineFactory,
)
from projectintelligence.domain.knowledge.project_knowledge import (
    ProjectKnowledge,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)
from projectintelligence.application.git.models.git_context import (
    GitContext,
)


@dataclass(slots=True)
class KnowledgeBuilder:
    """
    Builds ProjectKnowledge from project snapshot analysis.
    """

    technology_extractor: TechnologyExtractor

    architecture_extractor: ArchitectureExtractor

    dependency_extractor: DependencyExtractor

    convention_extractor: ConventionExtractor

    constraint_extractor: ConstraintExtractor

    history_extractor: HistoryExtractor

    intelligence_notes_extractor: IntelligenceNotesExtractor

    rule_engine_factory: RuleEngineFactory

    def build(
        self,
        snapshot: ProjectSnapshot,
        git_context: GitContext,
    ) -> ProjectKnowledge:
        """
        Build project knowledge from extracted information.
        """

        (
            technologies,
            frameworks,
            languages,
        ) = self.technology_extractor.extract(
            snapshot,
        )

        (
            architecture_description,
            architecture_patterns,
        ) = self.architecture_extractor.extract(
            snapshot,
        )

        (
            project_conventions,
            coding_rules,
        ) = self.convention_extractor.extract(
            snapshot,
        )

        knowledge = ProjectKnowledge(
            project_id=snapshot.project_id,
            technologies=technologies,
            frameworks=frameworks,
            languages=languages,
            dependency_map=self.dependency_extractor.extract(
                snapshot,
            ),
            architecture_description=architecture_description,
            architecture_patterns=architecture_patterns,
            project_conventions=project_conventions,
            coding_rules=coding_rules,
            known_constraints=self.constraint_extractor.extract(
                snapshot,
            ),
            historical_changes=self.history_extractor.extract(
                git_context,
            ),
            intelligence_notes=self.intelligence_notes_extractor.extract(
                snapshot,
            ),
        )

        rule_engine = self.rule_engine_factory.create()

        results = rule_engine.execute(
            knowledge,
        )

        for result in results:
            knowledge.findings.extend(
                result.findings,
            )

        return knowledge