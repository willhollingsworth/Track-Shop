# Track-Shop
A Learning project for a full-stack e-commerce site.

## Tech Stack

-   **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
-   **Database:** [PostgreSQL](https://www.postgresql.org/)
-   **ORM:** [SQLModel](https://sqlmodel.tiangolo.com/)
-   **Dependency Management:** [uv](https://github.com/astral-sh/uv)
-   **Development:** [Docker](https://www.docker.com/) 
-   **Deployment:** [Render.com](https://render.com/)

## Features

-   Local development environment using Docker for PostgreSQL.
-   Makefile for streamlined installation, development, and deployment workflows.
-   Secure handling of secrets using environment files.
-   Ready for production deployment with a `render.yaml` configuration file.

## Requirements

- Python 3.13
- [uv](https://github.com/astral-sh/uv)
- [Docker](https://www.docker.com/) (for local development)
- **Make**: For task automation (install on Windows with `winget install GnuWin32.Make`)

## Local Development
1. **Install dependencies:**
   ```sh
   make dev-install
   ```

2. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill out the required fields.

3. **Run the development server:**
   ```sh
   make dev-run
   ```

## Production
#### TODO: Add remote postgresSQL steps

1. **Install dependencies:**
```sh
make prod-install
```
2. **Run the prod server:**
```sh
make prod-run
```


### Available Make Commands

```bash
# Local Development
make dev-install     # Install all dependencies including dev tools
make dev-run         # Start development server with hot reload

# Production
make prod-install    # Install all dependencies
make prod-run        # Start production development server

# Checks
make check-env       # Checks that the .env exists locally
make check-docker    # Checks the local dev environment is running docker
make check-db        # Checks the db is running and responds to queries 

# Local Development DB Commands
make db-dev-up       # Start PostgreSQL container
make db-dev-reset    # Reset and seed database
make db-dev-down     # Stop PostgreSQL container
```

### Code Quality

The  project uses modern Python tooling:

- **Ruff**: For fast linting and code formatting
- **Pyright(strict)**: For enforcing type safety and static analysis