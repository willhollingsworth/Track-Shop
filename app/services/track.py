"""Service functions for track-related operations."""

from collections.abc import Sequence

from sqlmodel import Session, func, select

from app.models import Track


def get_random_tracks(session: Session, limit: int = 5) -> Sequence[Track]:
    """Return a list of random tracks."""
    return session.exec(select(Track).order_by(func.random()).limit(limit)).all()


def get_tracks_by_genre(
    session: Session,
    genre_name: str,
    limit: int = 6,
) -> Sequence[Track]:
    """Return a list of tracks by genre."""
    return session.exec(
        select(Track).where(func.lower(Track.genre) == genre_name.lower()).limit(limit),
    ).all()


def get_track_by_id(session: Session, track_id: int) -> Track | None:
    """Return a track by its ID."""
    return session.exec(select(Track).where(Track.track_id == track_id)).first()
