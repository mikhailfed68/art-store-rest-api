format:
	poetry run isort .
	poetry run black .

lint:
	poetry run flake8 .

test:
	poetry run python3 manage.py test

check-all: format lint test

start:
	poetry run python3 manage.py runserver

start-in-docker:
	sleep 3
	python3 -m manage runserver 0.0.0.0:8000

shell:
	poetry run python3 manage.py shell

collect:
	poetry run python3 manage.py collectstatic


.PHONY: format lint test start shell collect
