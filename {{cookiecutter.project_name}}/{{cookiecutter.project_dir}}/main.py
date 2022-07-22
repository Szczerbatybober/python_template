from datetime import date

from {{cookiecutter.project_dir}}.logger import init_logger
from {{cookiecutter.project_dir}}.greeter.greeter import Greeter


def entry() -> None:
    logger = init_logger()
    logger.info("Starting the app")
    sample_greeter = Greeter(def_date=date.today())
    print(sample_greeter.get_greeting("TW"))
    print(sample_greeter.get_random_name())


if __name__ == "__main__":
    entry()
