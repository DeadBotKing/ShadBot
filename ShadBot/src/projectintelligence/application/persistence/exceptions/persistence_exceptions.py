"""
ShadBot Project Intelligence

Persistence Exceptions
"""

from __future__ import annotations


class PersistenceError(Exception):
    """
    Base exception for persistence layer.
    """


class PersistenceConnectionError(PersistenceError):
    """
    Raised when a persistence provider cannot be reached.
    """


class PersistenceOperationError(PersistenceError):
    """
    Raised when a persistence operation fails.
    """


class EntityNotFoundError(PersistenceError):
    """
    Raised when an entity cannot be found.
    """


class DuplicateEntityError(PersistenceError):
    """
    Raised when an entity already exists.
    """


class PersistenceConfigurationError(PersistenceError):
    """
    Raised when persistence configuration is invalid.
    """
