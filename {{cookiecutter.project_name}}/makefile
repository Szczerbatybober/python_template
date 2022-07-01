.PHONY: checklist
checklist: 
	poetry run black .
	poetry run isort .
	poetry run flake8 .
	poetry run pylint {{cookiecutter.project_dir}}
	poetry run pyright .

.PHONY: tests
tests:
	echo "Running Coverage, report adn html"
	poetry run coverage run
	poetry run coverage report
	poetry run coverage html