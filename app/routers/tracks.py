"""Tracks router."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlmodel import Session

from app.db.db import get_session
from app.services.track import get_random_tracks, get_tracks_by_genre
from app.templates_env import templates

router = APIRouter()


@router.get("/popular")
def popular(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
) -> object:
    """Popular songs. Currently shows random tracks."""
    tracks = get_random_tracks(session)
    return templates.TemplateResponse(
        "popular.html",
        {"request": request, "tracks": tracks},
    )


@router.get("/recommended")
def recommended(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
) -> object:
    """Recommended songs. Currently shows random tracks."""
    tracks = get_random_tracks(session)
    return templates.TemplateResponse(
        "recommended.html",
        {"request": request, "tracks": tracks},
    )


@router.get("/genre/{genre_name}")
def genre(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    genre_name: str,
) -> object:
    """Songs by genre."""
    tracks = get_tracks_by_genre(session, genre_name)
    return templates.TemplateResponse(
        "genre.html",
        {"request": request, "tracks": tracks, "genre_name": genre_name},
    )
