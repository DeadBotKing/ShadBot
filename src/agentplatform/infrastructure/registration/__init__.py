"""
Agent registration infrastructure module.
"""

from agentplatform.infrastructure.registration.agent_registration import (
    register_default_agents,
)

from .capability_registration import register_default_capabilities

__all__ = [
    "register_default_agents",
    "register_default_capabilities",
]
