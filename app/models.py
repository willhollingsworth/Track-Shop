"""Database models.

Each Python class maps to a database table via SQLModel.
"""

from datetime import UTC, datetime

from sqlmodel import Field, SQLModel


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


class Cart(SQLModel, table=True):
    """Shopping cart for users."""

    cart_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class Order(SQLModel, table=True):
    """Completed Orders placed by users."""

    order_id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
