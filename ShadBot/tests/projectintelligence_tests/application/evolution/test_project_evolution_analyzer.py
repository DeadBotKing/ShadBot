"""
ShadBot Project Intelligence

Project Evolution Analyzer Tests
"""

from pathlib import Path
from uuid import uuid4

from projectintelligence.application.evolution.project_evolution_analyzer import (
    ProjectEvolutionAnalyzer,
)
from projectintelligence.application.evolution.strategies.file_evolution_strategy import (
    FileEvolutionStrategy,
)
from projectintelligence.domain.evolution.evolution_type import (
    EvolutionType,
)
from projectintelligence.domain.snapshot.project_snapshot import (
    ProjectSnapshot,
)


def test_project_evolution_analyzer_detects_added_removed_and_modified_files():

    project_id = uuid4()

    previous = ProjectSnapshot(
        project_id=project_id,
        workspace=Path("."),
        file_hashes={
            "a.py": "111",
            "b.py": "222",
        },
    )

    current = ProjectSnapshot(
        project_id=project_id,
        workspace=Path("."),
        file_hashes={
            "a.py": "999",
            "c.py": "333",
        },
    )

    analyzer = ProjectEvolutionAnalyzer(
        strategies=(FileEvolutionStrategy(),),
    )

    evolution = analyzer.analyze(
        previous,
        current,
    )

    assert len(evolution.changes) == 3

    change_types = {(change.path, change.change_type) for change in evolution.changes}

    assert (
        "a.py",
        EvolutionType.MODIFIED,
    ) in change_types

    assert (
        "b.py",
        EvolutionType.REMOVED,
    ) in change_types

    assert (
        "c.py",
        EvolutionType.ADDED,
    ) in change_types
