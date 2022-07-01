from datetime import date

from {{cookiecutter.project_dir}}.logger import init_logger
from {{cookiecutter.project_dir}}.sample.sample_class import SampleClass


def entry() -> None:
    logger = init_logger()
    sample_greeter = SampleClass(def_date=date.today())
    logger.error(sample_greeter.get_greeting("TW"))


if __name__ == "__main__":
    entry()
