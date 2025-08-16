from flask import Flask, render_template

from app.config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)

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
