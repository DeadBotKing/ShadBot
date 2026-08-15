"""
ShadBot Agent Platform

Phase 11 Platform Finalization module.
"""

from .api_layer import APIRequest, APIResponse, PlatformAPIGateway
from .configuration import ConfigurationManager, PlatformConfigPackage
from .database_integration import DatabaseConnectionReport, EnterpriseDatabaseAdapter
from .deployment import DeploymentManager, DeploymentPackage
from .logging_system import EnterpriseLogger, StructuredLogRecord
from .platform_service import PlatformFinalizationService
from .plugin_architecture import LoadedPlugin, PluginManager

__all__ = [
    "PlatformConfigPackage",
    "ConfigurationManager",
    "StructuredLogRecord",
    "EnterpriseLogger",
    "APIRequest",
    "APIResponse",
    "PlatformAPIGateway",
    "DatabaseConnectionReport",
    "EnterpriseDatabaseAdapter",
    "LoadedPlugin",
    "PluginManager",
    "DeploymentPackage",
    "DeploymentManager",
    "PlatformFinalizationService",
]
