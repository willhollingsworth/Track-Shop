"""Database connection setup with SQLModel."""

import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

# check env vars exist
try:
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")
except KeyError:
    msg = "missing value in .env file"
    raise OSError(msg)


# Build the database URL from environment variables
DATABASE_URL = f"postgresql://{user}:{password}@localhost:5432/{db_name}"

engine = create_engine(DATABASE_URL, echo=True)


# Dependency for FastAPI endpoints
def get_session():
    with Session(engine) as session:
        yield session
