# Track-Shop
A Learning project for a full-stack e-commerce site.

## Table of Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Requirements](#requirements)
- [Local Development](#local-development)
- [Production](#production)
- [User Authentication](#user-authentication)
- [Checks](#checks)
- [Available Make Commands](#available-make-commands)
- [Code Quality](#code-quality)

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

## User Authentication
### Overview
- **Session Management**: Uses Starlette's `SessionMiddleware` for server-side sessions, storing user IDs securely in encrypted cookies.
- **Password Security**: Passwords are hashed using `bcrypt` for one-way encryption before being stored in the database, see `app/services/user.py`
- **Validation**: Strict validation is enforced server-side with Pydantic schemas as defined in `app/schemas.py`. Additional more basic local validation is provided by Bootstrap.


### Registration Flow
Verifies a user's data then creates a new user.

1. **Register Page** : The user navigates to `/register` which routes to `app/routers/users/register.py` as a `GET` request and serves `app/templates/register.html`
2. **Form Submission**: The user submits the form which routes to `app/routers/users/register.py` as `POST` request. It checks against the schema defined in `app/schemas.py` and reports any errors. If there are none then an email duplicate check is run and if it passes a new user account is created and stored as per `app/models.py` 

### Login Flow
Checks a user's credentials then logs them in.

1. **Login Page** : The user navigates to `/login` which routes to `app/routers/users/login.py` as a `GET` request and serves `app/templates/login.html`
2. **Login Submission**: The user submits the form which routes to `app/routers/users/login.py` as `POST` request. Authentication is checked with `app/services/user.py`. If valid their `Session User ID` is added, creating a local encrypted cookie.
3. **Logged-in state**: Every page loaded can now read this `User ID`, allowing functionality like `app/templates/base.html` to toggle between a login and logout button with `{% if request.session.get('user_id') %}`


## Checks
Several checks are included in the `scripts` folder to ensure each step of the app running process is correct.
- `scripts/check_env.py` verifies the local `.env` exists in the root folder
- `scripts/check_docker.py` verifies the local docker process is running and responds to commands
- `scripts/check_db.py` verifies the local postgres database is running and responds to queries. This helps ensure an adequate delay between `MAKE` commands 


## Available Make Commands

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

## Code Quality

The project uses modern Python tooling:

- **Ruff**: For fast linting and code formatting
- **Pyright(strict)**: For enforcing type safety and static analysis

