"""Database connection setup with SQLModel."""

import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

# Build the database URL from environment variables
DATABASE_URL = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@localhost:5432/{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DATABASE_URL, echo=True)


# Dependency for FastAPI endpoints
def get_session():
    with Session(engine) as session:
        yield session
