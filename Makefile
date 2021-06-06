SRC_DIRS := app

precommit: format check

check:
	python -m isort $(SRC_DIRS) --check --diff
	python -m black $(SRC_DIRS) --check
	flake8 $(SRC_DIRS)

format:
	python -m isort $(SRC_DIRS)
	python -m black $(SRC_DIRS)

run:
	gunicorn app.wsgi:app --bind 0.0.0.0:5000 --timeout 100 --reload --log-file - --log-level debug

test:
	pytest tests/ -v --cov=app
