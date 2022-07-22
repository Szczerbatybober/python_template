from datetime import date

from {{cookiecutter.project_dir}}.logger import init_logger
from {{cookiecutter.project_dir}}.sample.greeter import Greeter


def entry() -> None:
    logger = init_logger()
    logger.info("Starting the app")
    sample_greeter = GreeterClass(def_date=date.today())
    print(sample_greeter.get_greeting("TW"))
    print(sample_greeter.get_random_name())


if __name__ == "__main__":
    entry()
