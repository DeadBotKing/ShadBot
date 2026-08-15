"""
ShadBot Agent Platform

7.4 State Management module.
"""

from .consistency_validation import StateConsistencyReport, StateConsistencyValidator
from .runtime_state_model import RuntimeStateModel
from .state_cleanup import StateCleanupManager
from .state_management_service import StateManagementServiceLayer
from .state_storage import RuntimeStateStorage
from .state_synchronization import RuntimeStateSynchronizer, StateSyncReport
from .transition_manager import RuntimeStateTransitionManager

__all__ = [
    "RuntimeStateModel",
    "RuntimeStateStorage",
    "RuntimeStateTransitionManager",
    "StateSyncReport",
    "RuntimeStateSynchronizer",
    "StateConsistencyReport",
    "StateConsistencyValidator",
    "StateCleanupManager",
    "StateManagementServiceLayer",
]
