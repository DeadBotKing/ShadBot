"""
ShadBot Agent Platform

Handoff Context Builder component for 6.4 Agent Handoff.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any
from agentplatform.domain.context import AgentExecutionContext
from .handoff_request import HandoffRequest


class HandoffContextBuilder:
    """
    Builds the execution context for a target agent from a HandoffRequest.
    """

    def build_context(self, context: AgentExecutionContext, request: HandoffRequest) -> AgentExecutionContext:
        meta = dict(context.metadata)
        agent_res = dict(meta.get("agent_results", {}))
        agent_res[request.source_agent_name] = request.previous_result.data
        meta["agent_results"] = agent_res

        if "architecture_plan" in request.previous_result.data:
            meta["architecture_plan"] = request.previous_result.data["architecture_plan"]
        if "research_report" in request.previous_result.data:
            meta["research_report"] = request.previous_result.data["research_report"]
        if "project_vision" in request.previous_result.data:
            meta["project_vision"] = request.previous_result.data["project_vision"]

        return replace(
            context,
            metadata=meta,
        )
