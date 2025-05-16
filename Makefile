deps:
	poetry install

test: deps
	poetry run pytest -v tests/

run: deps
	poetry run python src/log_alert_generator/log_alert.py

fmt:
	poetry run pre-commit run --all-files