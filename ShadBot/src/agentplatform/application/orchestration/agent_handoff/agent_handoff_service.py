"""
ShadBot Agent Platform

Unified service for 6.4 Agent Handoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from agentplatform.domain.context import AgentExecutionContext
from .context_builder import HandoffContextBuilder
from .handoff_history import HandoffHistoryTracker
from .handoff_request import HandoffRequest
from .handoff_validation import HandoffValidationResult, HandoffValidator
from .transition_manager import AgentTransitionManager, AgentTransitionRecord


@dataclass(frozen=True, slots=True)
class CompleteHandoffPackage:
    context: AgentExecutionContext
    validation: HandoffValidationResult
    transition: AgentTransitionRecord


class AgentHandoffService:
    """
    Orchestrates handoff requests, context building, validation, transition recording, and history tracking.
    """

    def __init__(
        self,
        builder: HandoffContextBuilder | None = None,
        validator: HandoffValidator | None = None,
        transition_mgr: AgentTransitionManager | None = None,
        history_tracker: HandoffHistoryTracker | None = None,
    ) -> None:
        self._builder = builder or HandoffContextBuilder()
        self._validator = validator or HandoffValidator()
        self._transition_mgr = transition_mgr or AgentTransitionManager()
        self._history_tracker = history_tracker or HandoffHistoryTracker()

    def handoff(self, context: AgentExecutionContext, request: HandoffRequest) -> CompleteHandoffPackage:
        val = self._validator.validate(request)
        if not val.valid:
            raise RuntimeError(val.reason)

        new_context = self._builder.build_context(context, request)
        rec = self._transition_mgr.record_transition(request)
        self._history_tracker.add_record(rec)

        return CompleteHandoffPackage(
            context=new_context,
            validation=val,
            transition=rec,
        )
