"""
ShadBot Agent Platform

Unit tests for 5.3 Memory Flow (Retriever, Ranker, Injector, Updater).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import uuid4

from agentplatform.application.brain.memory_flow.injection import (
    MemoryInjector,
)
from agentplatform.application.brain.memory_flow.ranking import (
    MemoryRanker,
)
from agentplatform.application.brain.memory_flow.retrieval import (
    MemoryQuery,
    MemoryRetriever,
)
from agentplatform.application.brain.memory_flow.update import (
    MemoryUpdateRequest,
    MemoryUpdater,
)
from agentplatform.domain.memory import (
    MemoryRecord,
    MemoryType,
)
from agentplatform.infrastructure.memory import (
    InMemoryMemoryRepository,
)


def test_memory_retriever_filters_and_limits() -> None:
    repo = InMemoryMemoryRepository()
    project_id = uuid4()

    rec1 = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "Clean Architecture guidelines"},
        source_agent="architect",
        confidence=0.9,
    )
    rec2 = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "Database optimization SQL"},
        source_agent="engineer",
        confidence=0.8,
    )
    repo.save(rec1)
    repo.save(rec2)

    retriever = MemoryRetriever(repo)
    query = MemoryQuery(
        goal_id=project_id,
        capability="architecture_design",
        keywords=("architecture",),
        max_results=5,
    )

    result = retriever.retrieve(query, project_id=project_id)
    assert result.total_records == 1
    assert result.records[0].memory_id == rec1.memory_id


def test_memory_ranker_scores_similarity_importance_freshness() -> None:
    project_id = uuid4()

    old_rec = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "architecture design"},
        source_agent="architect",
        confidence=0.5,
        created_at=datetime.now(timezone.utc) - timedelta(days=30),
    )
    new_rec = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "architecture design"},
        source_agent="architect",
        confidence=0.95,
        created_at=datetime.now(timezone.utc),
    )

    from agentplatform.application.brain.memory_flow.retrieval import (
        MemoryRetrievalResult,
    )

    retrieval_result = MemoryRetrievalResult(
        records=(old_rec, new_rec),
        total_records=2,
    )

    ranker = MemoryRanker()
    ranked_result = ranker.rank(retrieval_result, query_keywords=("architecture",))

    assert ranked_result.total_items == 2
    # The newer and higher confidence record should be ranked first
    assert ranked_result.ranked_items[0].record.memory_id == new_rec.memory_id
    assert ranked_result.ranked_items[0].score > ranked_result.ranked_items[1].score


def test_memory_injector_creates_injected_memories() -> None:
    project_id = uuid4()

    rec1 = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "info 1"},
        source_agent="architect",
    )
    rec2 = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.KNOWLEDGE,
        content={"text": "info 2"},
        source_agent="engineer",
    )

    from agentplatform.application.brain.memory_flow.ranking import (
        MemoryScore,
        RankedMemoryResult,
    )

    ranked = RankedMemoryResult(
        ranked_items=(
            MemoryScore(rec1, 0.9),
            MemoryScore(rec2, 0.7),
        ),
        total_items=2,
    )

    injector = MemoryInjector()
    injected_result = injector.inject(ranked)

    assert injected_result.total_memories == 2
    assert injected_result.injected_memories[0].injection_order == 1
    assert injected_result.injected_memories[1].injection_order == 2


def test_memory_updater_persists_to_repository() -> None:
    repo = InMemoryMemoryRepository()
    project_id = uuid4()

    rec = MemoryRecord(
        project_id=project_id,
        memory_type=MemoryType.DECISION,
        content={"decision": "use Postgres"},
        source_agent="architect",
    )

    updater = MemoryUpdater(repo)
    request = MemoryUpdateRequest(
        goal_id=uuid4(),
        memory=rec,
        reason="Architecture decision recorded",
    )

    result = updater.update(request)
    assert result.updated is True
    assert result.memory_id == rec.memory_id
    assert len(repo.get_project_memory(project_id)) == 1
