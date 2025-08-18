"""Apply dummy seed data to database from yaml file."""

from pathlib import Path

import yaml
from sqlmodel import Session

import app.models
from app.db.db import engine

SEED_DATA_PATH = "app/db/seed_data.yaml"


def seed_db() -> None:
    """Seed data from YAML file into the database."""
    with Path(SEED_DATA_PATH).open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    with Session(engine) as session:
        for table, details in data.items():
            model_cls = getattr(app.models, table, None)
            if not model_cls:
                print(f"Skipping unknown table: {table}")
                continue
            fields = details.get("fields")
            entries = details.get("entries", [])
            if not fields or not entries:
                print(f"No fields or entries for table: {table}")
                continue
            for entry in entries:
                entry_dict = dict(zip(fields, entry, strict=False))
                print(f"Seeding {table} with entry: {entry_dict}")
                model_instance = model_cls(**entry_dict)
                session.add(model_instance)
        session.commit()


if __name__ == "__main__":
    seed_db()
