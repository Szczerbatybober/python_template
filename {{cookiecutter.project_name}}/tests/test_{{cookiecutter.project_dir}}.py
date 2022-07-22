import logging
from datetime import date

from hypothesis import given
from hypothesis.strategies import text
import responses

from {{cookiecutter.project_dir}} import __version__
from {{cookiecutter.project_dir}}.logger import init_logger
from {{cookiecutter.project_dir}}.greeter.greeter import Greeter


def test_version():
    assert __version__ == "0.1.0"


def test_logger():
    logger = init_logger()
    assert isinstance(logger, logging.Logger)


@given(text())
def test_python_test(test_str):
    sample_class = Greeter(def_date=date.today())
    assert isinstance(sample_class.get_greeting(name=test_str), str)

@responses.activate
def test_mock_request():
    sample_class = Greeter(def_date=date.today())
    return_value = {
        "results": [
            {"name": {"first": "Test name", "last": "test last_name", "title": "mrs"}}
        ]
    }
    responses.get(url=sample_class.API_ENDPOINT, json=return_value, status=200)

    assert sample_class.get_random_name() == "Test name"

