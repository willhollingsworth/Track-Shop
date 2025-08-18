# Track-Shop
A Learning project for a full stack e-commerce site.

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
- **Make**: For task automation (install on windows with `winget install GnuWin32.Make`)

## Local Development
1. **Install dependencies:**
   ```sh
   make dev-install
   ```

2. **Set up environment variables:**
   - Copy `.env.example` to `.env` and edit as needed.

3. **Run the development server:**
   ```sh
   make dev
   ```

## Production
#### TODO: Add remote postgres steps

1. **Install dependencies:**
```sh
make install
```
2. **Run the prod server:**
```sh
make prod
```


### Available Make Commands

```bash
make install-dev    # Install all dependencies including dev tools
make dev           # Start development server with hot reload
make db-dev-up     # Start PostgreSQL container
make db-dev-reset  # Reset and seed database
make db-dev-down   # Stop PostgreSQL container
```

### Code Quality

The  project uses modern Python tooling:

- **Ruff**: For fast linting and code formatting
- **Pyright(strict)**: For enforcing type safety and static analysis