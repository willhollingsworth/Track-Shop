"""Database models.

Each Python class maps to a database table via SQLModel.
"""

from datetime import UTC, datetime

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    """Authenticated users."""

    user_id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    password: str
    phone: str
    first_name: str
    last_name: str
    creation_date: datetime = Field(default_factory=lambda: datetime.now(UTC))
    admin: bool = Field(default=False)

    # Relationships
    orders: list["Order"] = Relationship(back_populates="user")


class Track(SQLModel, table=True):
    """Music tracks available for purchase."""

    track_id: int | None = Field(default=None, primary_key=True)
    artist: str
    title: str
    price: float
    genre: str
    bpm: int
    music_key: str
    label: str


class Order(SQLModel, table=True):
    """Completed Orders placed by users."""

    order_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    subtotal: float
    tax: float
    total: float

    # Relationships
    order_tracks: list["OrderTrack"] = Relationship(back_populates="order")
    user: "User" = Relationship(back_populates="orders")


class OrderTrack(SQLModel, table=True):
    """Many-to-many: orders to tracks."""

    order_id: int = Field(foreign_key="order.order_id", primary_key=True)
    track_id: int = Field(foreign_key="track.track_id", primary_key=True)
    price_at_purchase: float

    # Relationships
    order: Order = Relationship(back_populates="order_tracks")
    track: Track = Relationship()
