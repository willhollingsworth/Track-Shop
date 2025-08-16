from sqlmodel import Session, SQLModel

from app.db import engine
from app.models import Track, User


def reset_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    print("Database reset complete.")


def seed_db():
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
    reset_db()
    seed_db()
