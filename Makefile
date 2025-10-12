.PHONY: prod-install prod-run dev-install dev-run db-dev-up db-dev-reset db-dev-down check-env check-docker

# production
prod-install:
	uv sync --frozen --no-dev && uv cache prune --ci

prod-run:
	uv run gunicorn app.app:app


# development	
dev-install:
	uv sync --frozen && uv cache prune --ci

dev-run: db-dev-up check-db db-dev-reset
	uv run fastapi dev

dev-run-persistent: db-dev-up check-db
	uv run fastapi dev --reload


# dev checks
check-env:
	uv run python scripts/check_env.py

check-docker:
	uv run python scripts/check_docker.py

check-db:
	uv run python scripts/check_db.py

# dev database
db-dev-up: check-env check-docker
	docker compose up -d postgres-dev

db-dev-reset:
	uv run python -m app.db.reset_db 
	timeout 1
	uv run python -m app.db.seed_db

db-dev-down:
	docker compose down