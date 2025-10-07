.PHONY: install install-dev dev db-dev-up db-dev-reset db-dev-down prod

install:
	uv sync --frozen --no-dev && uv cache prune --ci

install-dev:
	uv sync --frozen && uv cache prune --ci

dev: db-dev-up db-dev-reset
	uv run fastapi dev

db-dev-up:
	docker compose up -d postgres-dev
	timeout 10

db-dev-reset:
	uv run python -m app.db.reset_db 
	timeout 2
	uv run python -m app.db.seed_db

db-dev-down:
	docker compose down

prod:
	uv run gunicorn app.app:app
