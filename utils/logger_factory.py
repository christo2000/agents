import sys
import os

from pathlib import Path
from loguru import logger
from typing import Optional

from config.logger_config import SYS_FORMAT, SYS_DEBUG_LEVEL, SYS_COLOR, FILE_MAX_SIZE, LOG_DIR, RETENTION, \
    FILE_COMPRESS_FORMAT, FILE_FORMAT, FILE_LEVEL_DEBUG, FILE_COLORIZE


# Custom exception class similar to ExceptionCalls
class ExceptionCalls(Exception):
    def __init__(self, message: str, cause: Optional[Exception] = None):
        super().__init__(message)
        self.cause = cause


class LoggerHandling:

    def __init__(self):
        self._setup_logger()

    def _setup_logger(self):
        logger.remove()  # remove default handler

        # Console handler
        logger.add(
            sys.stdout,
            format=SYS_FORMAT,
            level=SYS_DEBUG_LEVEL,
            colorize=SYS_COLOR
        )

        # Single file handler (all levels)
        # Path(LOG_BASE_PATH)
        log_file_path = os.path.join(Path.cwd().parent, LOG_DIR, "app.log")
        logger.add(
            log_file_path,
            rotation=FILE_MAX_SIZE,
            retention=RETENTION,
            compression=FILE_COMPRESS_FORMAT,
            format=FILE_FORMAT,
            level=FILE_LEVEL_DEBUG,   # usually "DEBUG"
            colorize=FILE_COLORIZE
        )

    def info(self, log_message: str) -> None:
        logger.info(f" message: {log_message}")

    def error(self, exception: Exception, log_message: str) -> None:
        logger.error(
            f" message: {log_message} | Exception: {exception.__class__.__name__} - {str(exception)}"
        )

    def trace(self, log_message: str) -> None:
        logger.trace(f" message: {log_message}")

    def success(self, log_message: str) -> None:
        logger.success(f" message: {log_message}")

    def warning(self, log_message: str) -> None:
        logger.warning(f" message: {log_message}")

    def critical(self, exception: Exception, log_message: str) -> None:
        logger.critical(
            f" message: {log_message} | Exception: {exception.__class__.__name__} - {str(exception)}"
        )

    def debug(self, log_message: str) -> None:
        logger.debug(f" message: {log_message}")
