import logging
from datetime import date

from hypothesis import given
from hypothesis.strategies import text

from python_template import __version__
from python_template.logger import init_logger
from python_template.sample.sample_class import SampleClass


def test_version():
    assert __version__ == "0.1.0"


def test_logger():
    logger = init_logger()
    assert isinstance(logger, logging.Logger)


@given(text())
def test_python_test(test_str):
    sample_class = SampleClass(def_date=date.today())
    assert isinstance(sample_class.get_greeting(name=test_str), str)
