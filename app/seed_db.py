"""Apply dummy seed data to database."""

from sqlmodel import Session

from app.db import engine
from app.models import Track, User


def seed_db() -> None:
    """Seed the database with dummy data."""
    with Session(engine) as session:
        # Example seed data
        user = User(email="admin@example.com", password="admin", admin=True)
        track = Track(
            artist="Artist",
            title="Song",
            price=1.99,
            genre="House",
            bpm=128,
            music_key="C#m",
            label="Label",
        )
        session.add(user)
        session.add(track)
        session.commit()
        print("Database seeded.")


if __name__ == "__main__":
    seed_db()
