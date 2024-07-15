.PHONY: install lint format
install:
	pipenv lock
	pipenv sync --dev

lint: install
	pipenv run lint

format: install
	pipenv run format