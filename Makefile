.DEFAULT_GOAL := all

format:
	black *.py
lint:
	pylint *.py
run:
	python app.py
test:
	python -m pytest

all:	format lint test
