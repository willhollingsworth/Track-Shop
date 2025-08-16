from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String, unique=True, index=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, default=False)


class Track(db.Model):
    __tablename__ = "tracks"

    track_id = db.Column(db.Integer, primary_key=True, index=True)
    artist = db.Column(db.String, unique=True, index=True, nullable=False)
    title = db.Column(db.String, unique=True, index=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String, nullable=False)
    bpm = db.Column(db.Integer, nullable=False)
    music_key = db.Column(db.String, nullable=False)
    label = db.Column(db.String, nullable=False)


class Cart(db.Model):
    __tablename__ = "carts"

    cart_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
