SHELL = /bin/bash

.ONESHELL:

.PHONY: help setup check clean run test


help:
	@echo "make setup"
	@echo "       setups the project"
	@echo "make test"
	@echo "       runs pytest with coverage report"
	@echo "make check"
	@echo "       runs linters and formatters"
	@echo "make clean"
	@echo "       cleans outputs and pycache"
	@echo "make run"
	@echo "       runs the main.py file"

.DEFAULT_GOAL = help

BUMP = patch


check: 
	@echo "Runnint lint and formatters..."
	@poetry run black .
	@poetry run ruff . --fix
	@poetry run pylint {{cookiecutter.project_name}}
	
run: 
	@echo "Running {{cookiecutter.project_name}}/main.py..."
	@poetry run python {{cookiecutter.project_name}}/main.py

test:
	@echo "Running pytest..."
	@poetry run pytest

setup:
	@echo "Setting up project..."
	@poetry install
	@poetry run pre-commit install

clean:
	@echo "Cleaning..."
	@rm -rf .pytest_cache/
	@rm -rf srcgen/
	@rm -rf dist/
	@rm -rf .ruff_cache
	@rm -rf .hypothesis
	@rm -rf .coverage
	@find tests | grep -E "(__pycache__$$)" | xargs rm -rf