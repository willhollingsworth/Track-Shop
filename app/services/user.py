"""User service functions for authentication and session management."""

import bcrypt
from sqlmodel import Session, select

from app.models import User


def hash_password(password: str) -> str:
    """Hash a plaintext password using bcrypt."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def authenticate_user(session: Session, email: str, password: str) -> User | None:
    """Authenticate user by email and password."""
    user = session.exec(select(User).where(User.email == email)).first()
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        return user
    return None
