"""Search router for track search functionality."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Query, Request
from sqlmodel import Session
from starlette.responses import Response

from app.db.db import get_session
from app.services.track import search_tracks
from app.templates_env import templates

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/search")
def search(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    search_string: Annotated[str, Query(min_length=0, max_length=100)] = "",
) -> Response:
    """Search for tracks and return autocomplete results."""
    tracks = search_tracks(session, search_string) if search_string else []
    logger.info("Found %d tracks", len(tracks))

    return templates.TemplateResponse(
        "partials/search_results.html",
        {
            "request": request,
            "tracks": tracks,
            "search_string": search_string,
        },
    )
