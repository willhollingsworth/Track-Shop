"""Reset database."""

from sqlalchemy import text

from app import models  # Required for reset to work correctly
from app.db.db import engine


def reset_db() -> None:
    """Reset the database by dropping and recreating all tables."""
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
        conn.commit()
    models.SQLModel.metadata.create_all(engine)
    print("Database reset complete.")


if __name__ == "__main__":
    reset_db()
