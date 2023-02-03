from loguru import logger

from {{cookiecutter.project_name}}.models.user import User


def entry() -> None:
    logger.debug("Loggin hey ho")
    user: User = User(first_name="Szcz")
    logger.info(f"Created user with {user.id=}")


if __name__ == "__main__":
    entry()
