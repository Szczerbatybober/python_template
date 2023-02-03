FROM python:3.10-buster

RUN pip install --upgrade pip
RUN pip install poetry


COPY ./pyproject.toml pyproject.toml
COPY ./poetry.lock poetry.lock
COPY ./poetry.toml poetry.toml
ENV PIP_DEFAULT_TIMEOUT=100

RUN poetry install --no-root
COPY . .
RUN poetry install

CMD ["poetry", "run", "python", "{{cookiecutter.project_name}}/main.py"]