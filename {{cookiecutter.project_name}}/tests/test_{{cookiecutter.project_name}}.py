from hypothesis import given
from hypothesis.strategies import text
import pytest

from {{cookiecutter.project_name}} import __version__


def test_version():
    assert __version__ == "0.1.0"


@given(text())
@pytest.mark.smoke
def test_python_test(test_str):
    assert isinstance(test_str, str)
