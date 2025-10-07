"""Tracks router."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, func, select

from app.db.db import get_session
from app.models import Track
from app.templates_env import templates

router = APIRouter()


@router.get("/popular")
def popular(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
) -> object:
    """Popular songs. Currently shows random tracks."""
    tracks = session.exec(
        select(Track).order_by(func.random()).limit(6),
    ).all()
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
    tracks = session.exec(
        select(Track).order_by(func.random()).limit(6),
    ).all()
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
    tracks = session.exec(
        select(Track)
        .where(func.lower(Track.genre) == genre_name.lower())
        .order_by(func.random())
        .limit(6),
    ).all()
    return templates.TemplateResponse(
        "genre.html",
        {"request": request, "tracks": tracks, "genre_name": genre_name},
    )
