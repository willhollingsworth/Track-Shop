.PHONY: install start dev prod

install:
	uv sync --frozen && uv cache prune --ci

start:
	uv run flask --app app.app:app run --host=0.0.0.0 --port=8000

dev:
	uv run flask --app app.app:app run --debug

prod:
	uv run gunicorn app.app:app