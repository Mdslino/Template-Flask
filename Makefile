SHELL := /bin/bash
.PHONY: all clean install test black isort format-code sort-imports flake8 mypy black-check isort-check lint

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: clean install test 

test:
	pytest tests/ -v

test-coverage:
	pytest --cov=src tests/ -v

install:
	poetry install

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

black:
	@black .

isort:
	@isort .

format-code: black isort

sort-imports:
	@isort .

flake8:
	@flake8 src/

mypy:
	@mypy src/

black-check:
	@black --check src/

isort-check:
	@isort --check-only src/

lint: flake8 black-check isort-check
