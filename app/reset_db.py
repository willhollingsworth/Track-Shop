"""Reset database."""

from sqlmodel import SQLModel

from app import models  # noqa: F401 # Required for reset to work correctly
from app.db import engine


def reset_db() -> None:
    """Reset the database by dropping and recreating all tables."""
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    print("Database reset complete.")


if __name__ == "__main__":
    reset_db()
