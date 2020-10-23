.PHONY: test
.PHONY: format

test:
	poetry run black --check custom_components
	poetry run flake8 custom_components

format:
	poetry run black custom_components

install:
	poetry install



