import logging.config

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {"root": {"level": "DEBUG", "handlers": ["stdout"]}},
}

logging.config.dictConfig(config=logging_config)
logger = logging.getLogger("steganography")
