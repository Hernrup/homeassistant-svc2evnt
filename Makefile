.PHONY: test
.PHONY: format

test:
	black --check custom_components
	flake8 custom_components

format:
	black custom_components



