# Track-Shop
A full stack e-commerce web app for selling song. Built with Flask and PostgreSQL.

## Requirements

- Python 3.13
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Dev Requirements
- Docker (for local PostgreSQL database)

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