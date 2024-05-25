"""Module to handle application logging"""
import json
import logging
import logging.config
import os
import sys
from datetime import datetime

LOGGING_ROOT_DIR = f'logs/{datetime.now().strftime("%Y-%m-%d--%H-%M-%S")}'
log = logging.getLogger("utils-logger")


class Logger:
    """Class to define loggers for utils and api modules that write
    logs into as well as stdout as into file"""

    FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    LOG_FILE = "logs/logs.log"
    CONFIG = {
        "version": 1,
        "formatters": {"formatter": {"format": FORMAT}},
        "handlers": {
            "console_stdout": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "formatter",
                "stream": sys.stdout,
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                # file catches more logs than stdout
                "formatter": "formatter",
                "filename": LOG_FILE,
                "encoding": "utf8",
                "mode": "a",
                "maxBytes": 5 * 1024 * 1024,  # 5 MB
                "backupCount": 5,
            },
        },
        "loggers": {
            "root": {
                "level": "NOTSET",
                "handlers": ["console_stdout", "file"],
                "propagate": False,
            },
            "utils-logger": {
                "handlers": ["console_stdout", "file"],
                "propagate": False,
            },
            "endpoints-logger": {
                "handlers": ["console_stdout", "file"],
                "propagate": False,
            }
        },
    }

    @classmethod
    def init_logger(cls) -> None:
        """Initializes logger instances"""
        try:
            logging.config.dictConfig(cls.CONFIG)
        except (ValueError, TypeError, AttributeError, ImportError) as e:
            log.error(f"Error occured during initialization of logger: {str(e)}")
            raise
