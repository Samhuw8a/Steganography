import logging.config

logging_config: dict = {
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
    "loggers": {"root": {"level": "INFO", "handlers": ["stdout"]}},
}

logging.config.dictConfig(config=logging_config)
logger = logging.getLogger("steganography")


def non_verbal_conf() -> None:
    logging_config["formatters"]["simple"]["format"] = "%(message)s"
    logging_config["loggers"]["root"]["level"] = "WARN"
    logging.config.dictConfig(config=logging_config)


def debug_conf() -> None:
    logging_config["loggers"]["root"]["level"] = "DEBUG"
    logging_config["formatters"]["simple"]["format"] = "%(levelname)s: %(message)s"
    logging.config.dictConfig(config=logging_config)
