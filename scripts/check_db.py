"""Script to check local Postgres.

- checks if local db is running by attempting a connection
- check if db accepts a simple query
"""

import os
import sys
import time

import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build the database URL (reusing logic from app/db/db.py for consistency)
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
DATABASE_URL = f"postgresql://{user}:{password}@localhost:5432/{db_name}"


def is_db_running() -> bool:
    """Check if PostgreSQL is running by attempting a connection."""
    try:
        with psycopg2.connect(DATABASE_URL) as conn:
            # Execute a simple query to verify the connection
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1;")
        print(".", flush=True)
        return True
    except:
        print(".", end="", flush=True)
        return False


def is_db_responding() -> bool:
    """Check if the database responds to a simple query."""
    try:
        with psycopg2.connect(DATABASE_URL) as conn, conn.cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()
            return result == (1,)
    except:
        return False


if __name__ == "__main__":
    print("Checking if PostgreSQL is running...", end="")
    for _ in range(10):  # Retry a few times
        if is_db_running():
            break
        time.sleep(1)
    else:
        print("Error: PostgreSQL is not running!")
        sys.exit(1)
    print("PostgreSQL is running. Checking if it's responding to queries...")
    if is_db_responding():
        print("Database is responding to queries. All checks passed.")
        sys.exit(0)
    else:
        print("Error: Database is not responding to queries!")
        sys.exit(1)
