"""Service functions for track-related operations."""

from collections.abc import Sequence

from sqlmodel import Session, func, select

from app.models import Track


def get_random_tracks(session: Session, limit: int = 5) -> Sequence[Track]:
    """Return a list of random tracks."""
    return session.exec(select(Track).order_by(func.random()).limit(limit)).all()


def get_track_by_id(session: Session, track_id: int) -> Track | None:
    """Return a track by its ID."""
    return session.exec(select(Track).where(Track.track_id == track_id)).first()


def get_tracks(
    session: Session,
    genre: str | None = None,
    limit: int = 20,
) -> list[Track]:
    """Return a list of tracks, optionally filtered by genre."""
    if genre:
        statement = select(Track).where(func.lower(Track.genre).like(func.lower(genre)))
    else:
        statement = select(Track).order_by(func.random())
    statement = statement.limit(limit)
    return list(session.exec(statement).all())


def search_tracks(session: Session, query: str, limit: int = 5) -> list[Track]:
    """Search for tracks by title or artist name."""
    min_query_length = 2
    if not query or len(query) < min_query_length:
        return []

    search_pattern = f"%{query}%"
    statement = (
        select(Track)
        .where(
            (func.lower(Track.title).like(func.lower(search_pattern)))
            | (func.lower(Track.artist).like(func.lower(search_pattern))),
        )
        .limit(limit)
    )
    return list(session.exec(statement).all())
