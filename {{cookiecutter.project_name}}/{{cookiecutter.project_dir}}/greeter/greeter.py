import logging
import json
from datetime import date
import requests
from dacite import from_dict
from dacite.dataclasses import DefaultValueNotFoundError
from dacite.exceptions import MissingValueError
from {{cookiecutter.project_dir}}.models.user import UserAPIResponse

logger = logging.getLogger(__name__)


class Greeter:
    DATE_FORMAT = "%Y-%m-%d"
    API_ENDPOINT = "https://randomuser.me/api?inc=gender,name"

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
            logger.info(f"{random_user=}")
            user_api_response = from_dict(data_class=UserAPIResponse, data=random_user)
            return self._get_name_from_user(user_api_response)
        except (MissingValueError, DefaultValueNotFoundError):
            logger.error(
                "Could not parse data from the api, defaulting to John", exc_info=1
            )
            logger.error(f"{random_user=}")
            return "John"

    def _fetch_response(self) -> dict:
        response = requests.get(self.API_ENDPOINT)
        if response.ok:
            logger.info(response.content)
            return json.loads(response.content)
        else:
            logger.warning("Could not fetch the response from remote api")
            logger.warning(f"The Response was {response}")
            return {}

    def _get_name_from_user(self, user_api_response: UserAPIResponse) -> str:
        return user_api_response.results[0].name.first
