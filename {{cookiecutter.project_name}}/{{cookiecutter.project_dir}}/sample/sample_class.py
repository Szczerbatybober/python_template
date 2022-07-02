import logging
from datetime import date
import requests

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

    def get_random_name(self) -> str:
        random_user = self._fetch_response()
        try:
            return random_user["results"][0]["name"]["first"]
        except KeyError:
            logger.error("Could not fetch data from the api, defaulting to John")
            return "John"

    def _fetch_response(self) -> dict:
        response = requests.get("https://randomuser.me/api/")
        if response.ok:
            return response
        else:
            return {}
