"""Home router."""

from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from sqlmodel import Session

from app.db.db import get_session
from app.services.track import get_random_tracks
from app.templates_env import templates

router = APIRouter()


@router.get("/")
def home(request: Request, session: Annotated[Session, Depends(get_session)]) -> object:
    """Home page showing 5 random tracks."""
    tracks = get_random_tracks(session)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tracks": tracks},
    )
