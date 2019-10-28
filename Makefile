lint:
	pylint *.py
test:
	python -m pytest
run:
	python app.py
format:
	black *.py
