cov:
	python3 -m pytest -s --cov=src --cov-report=term-missing --cov-report=html:coverage_html tests

fmt:
	PYTHONPATH=$$(pwd) python3 -m black src tests

play:
	PYTHONPATH=$$(pwd) python3 src/main.py
