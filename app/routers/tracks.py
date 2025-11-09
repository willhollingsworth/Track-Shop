"""Tracks router."""

from collections.abc import Callable
from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from starlette.responses import RedirectResponse, Response

from app.db.db import get_session
from app.services import cart, track
from app.templates_env import templates

router = APIRouter()


TRACK_PAGE_TITLES: dict[str, dict[str, str]] = {
    "/popular": {
        "title": "Popular Songs",
        "subtitle": "Discover the most popular tracks right now.",
    },
    "/recommended": {
        "title": "Recommended",
        "subtitle": "Songs Recommended by us",
    },
    "/": {
        "title": "All Tracks",
        "subtitle": "Browse our complete collection of tracks.",
    },
}


GENRE_TITLES: dict[str, Callable[[str], str]] = {
    "title": lambda genre: f"{str(genre).title()} Tracks",
    "subtitle": lambda genre: f"Explore the best {str(genre).title()} tracks.",
}


@router.get("/track/{track_id}", name="track_detail")
def track_detail_page(
    request: Request,
    track_id: int,
    session: Annotated[Session, Depends(get_session)],
) -> Response:
    """Display detailed track information page."""
    track_data = track.get_track_by_id(session, track_id)

    # If track doesn't exist, redirect to home
    if not track_data:
        return RedirectResponse(url="/", status_code=303)

    # Get cart info for the "Add to Cart" button
    user_cart = cart.get_cart(request)
    track_ids = [item.track_id for item in user_cart.items]
    is_in_cart = track_id in track_ids

    return templates.TemplateResponse(
        "track_detail.html",
        {
            "request": request,
            "track": track_data,
            "cart": user_cart,
            "is_in_cart": is_in_cart,
        },
    )


@router.get("/", name="home")
@router.get("/popular", name="popular")
@router.get("/recommended", name="recommended")
@router.get("/genre/{genre_name}", name="genre")
def tracks_page(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    genre_name: str | None = None,
) -> Response:
    """Tracks page showing tracks, optionally filtered by genre."""
    path = request.url.path
    tracks = track.get_tracks(session, genre=genre_name)
    user_cart = cart.get_cart(request)

    # handle page titles and subtitles
    if genre_name:
        page_title = GENRE_TITLES["title"](genre_name)
        page_subtitle = GENRE_TITLES["subtitle"](genre_name)
    else:
        page_title = TRACK_PAGE_TITLES[path]["title"]
        page_subtitle = TRACK_PAGE_TITLES[path]["subtitle"]

    return templates.TemplateResponse(
        "track_listing.html",
        {
            "request": request,
            "tracks": tracks,
            "cart": user_cart,
            "page_title": page_title,
            "page_subtitle": page_subtitle,
        },
    )
