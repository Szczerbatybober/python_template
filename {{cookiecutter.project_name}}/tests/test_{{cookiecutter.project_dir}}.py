import logging
from datetime import date

from hypothesis import given
from hypothesis.strategies import text
from unittest.mock import patch

from {{cookiecutter.project_dir}} import __version__
from {{cookiecutter.project_dir}}.logger import init_logger
from {{cookiecutter.project_dir}}.sample.sample_class import SampleClass


def test_version():
    assert __version__ == "0.1.0"


def test_logger():
    logger = init_logger()
    assert isinstance(logger, logging.Logger)


@given(text())
def test_python_test(test_str):
    sample_class = SampleClass(def_date=date.today())
    assert isinstance(sample_class.get_greeting(name=test_str), str)

@patch('{{cookiecutter.project_dir}}.sample.sample_class._get_random_user')
def test_mock_request(mock_random_user):
    sample_class = SampleClass(def_date=date.today())
    mock_random_user.return_value = {
        "results": [
            {
                "name" : {
                "first": "Test name"
                }
            }
        ]
    }
    assert sample_class.get_random_name() == "Test name"
