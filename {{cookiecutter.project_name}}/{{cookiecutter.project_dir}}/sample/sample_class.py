import logging
from datetime import date

logger = logging.getLogger(__name__)


class SampleClass:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, def_date: date):
        self.class_date = def_date
        logger.info(f"{type(self).__name__} initialized with {self.class_date}")

    def get_greeting(self, name: str) -> str:
        return (
            f"Hello, {name}, it is {self.class_date.strftime(self.DATE_FORMAT)} today"
        )
