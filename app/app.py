import os

from dotenv import load_dotenv
from flask import Flask, render_template

from app.models import db

load_dotenv()
app = Flask(__name__)

# SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
    f"@localhost:5432/{os.getenv('POSTGRES_DB')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.cli.command()
def reset_db() -> None:
    """Reset the database."""
    db.drop_all()
    db.create_all()
    print("Database reset complete.")


@app.route("/")
def home() -> str:
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
