"""
ShadBot Agent Platform

Unit tests for 8.4 Async Execution.
"""

from __future__ import annotations

from agentplatform.application.communication.async_execution import (
    AsyncExecutionService,
)


def test_async_execution_service_submits_and_tracks() -> None:
    service = AsyncExecutionService()
    task = service.submit_task(
        "ML_Train",
        {"epochs": 10},
        lambda p: f"Trained {p['epochs']} epochs",
        "CRITICAL",
    )
    assert task.status == "COMPLETED"
    assert "10 epochs" in str(task.result)
    assert service.tracker.get_task(task.task_id) == task
