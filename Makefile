SHELL := /bin/bash
.PHONY: all clean install test black isort format-code sort-imports flake8 mypy black-check isort-check lint run run-dev

# Misc Section
help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: clean install test

install:
	poetry install

clean:
	@find . -name '*.pyc' -exec rm -rf {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name 'Thumbs.db' -exec rm -rf {} +
	@find . -name '*~' -exec rm -rf {} +
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf .mypy_cache

# Test Section
test:
	pytest tests/ -v

test-coverage:
	pytest --cov=src tests/ -v

#Run Serction
run:
	@gunicorn "src.app:create_app()" -k gevent -b 0.0.0.0:8000 -w 4 --preload --access-logfile=- --error-logfile=- --log-level info

run-dev:
	@flask run --host=0.0.0.0 --port=8000 --reload --debugger --with-threads

# Lint Section
lint:
	@./scripts/lint.sh $(MODE)

mypy:
	@mypy src/
