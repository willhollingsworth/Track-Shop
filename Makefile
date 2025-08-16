.PHONY: install install-dev dev db-dev-up db-dev-down prod

install:
	uv sync --frozen --no-dev && uv cache prune --ci

install-dev:
	uv sync --frozen && uv cache prune --ci

dev: db-dev-up
	uv run flask --app app.app:app run --debug

db-dev-up:
	docker compose up -d postgres-dev

db-dev-down:
	docker compose down

prod:
	uv run gunicorn app.app:app
