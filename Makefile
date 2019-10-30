.DEFAULT_GOAL := all

format:
	black *.py
lint:
	pylint *.py
run:
	python app.py
test:
	python -m pytest --cov=.

all:	format lint test
