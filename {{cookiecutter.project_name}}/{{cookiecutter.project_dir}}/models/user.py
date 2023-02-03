from pydantic import Field
from uuid import UUID, uuid4
from {{cookiecutter.project_name}}.models.camel_model import CamelModel


class User(CamelModel):
    id: UUID = Field(default_factory=uuid4)
    first_name: str
    last_name: str | None
    title: str | None
