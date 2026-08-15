"""
ShadBot Agent Platform

Capability Matcher component for 6.2 Agent Selection.
"""

from __future__ import annotations

from typing import Sequence
from agentplatform.domain.contracts import AgentContract


class CapabilityMatcher:
    """
    Matches candidate agents against required capabilities.
    """

    def filter_capable(self, agents: Sequence[AgentContract], required_capability: str) -> tuple[AgentContract, ...]:
        matched: list[AgentContract] = []
        req_lower = required_capability.lower()
        for agent in agents:
            caps = getattr(agent, "capabilities", [])
            cap_strs = [c.capability_type.value.lower() for c in caps]
            if req_lower in cap_strs or not cap_strs:
                matched.append(agent)
        return tuple(matched) or tuple(agents)
