"""Module responsible for initializing logger"""

import logging
import logging.config

import yaml


def init_logger() -> logging.Logger:
    with open("logconfig.yaml", "rt", encoding="utf-8") as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("Logger configured!")
    return logger
