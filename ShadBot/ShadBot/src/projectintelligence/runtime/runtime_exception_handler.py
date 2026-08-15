"""
ShadBot Project Intelligence

Runtime Exception Handler
"""

from __future__ import annotations

import logging
from traceback import format_exception

logger = logging.getLogger(__name__)


class RuntimeExceptionHandler:
    """
    Centralized exception handling for the Project Intelligence Runtime.
    """

    def handle(
        self,
        exception: Exception,
    ) -> None:
        """
        Handle an unhandled runtime exception.

        The exception is logged and then re-raised so the caller can
        decide how to terminate the execution.
        """

        logger.exception(
            "Project Intelligence runtime failed.",
        )

        logger.debug(
            "".join(
                format_exception(
                    type(exception),
                    exception,
                    exception.__traceback__,
                ),
            ),
        )

        raise exception

    def safe_handle(
        self,
        exception: Exception,
    ) -> Exception:
        """
        Log an exception and return it without raising.

        Useful when the caller wants to propagate the exception
        through a result object instead of immediately failing.
        """

        logger.exception(
            "Project Intelligence runtime failed.",
        )

        logger.debug(
            "".join(
                format_exception(
                    type(exception),
                    exception,
                    exception.__traceback__,
                ),
            ),
        )

        return exception
