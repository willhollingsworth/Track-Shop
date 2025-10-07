"""Main application entry point for the Track Shop FastAPI app."""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.requests import Request
from sqlmodel import Session

from app.db.db import get_session
from app.routers import tracks
from app.routers.users import login, register
from app.services.track import get_random_tracks
from app.templates_env import templates

app = FastAPI(title="Track Shop")

# Include user routes
app.include_router(register.router)
app.include_router(login.router)

# Include track routes
app.include_router(tracks.router)


@app.get("/")
def home(request: Request, session: Annotated[Session, Depends(get_session)]) -> object:
    """Home page showing 5 random tracks."""
    tracks = get_random_tracks(session)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tracks": tracks},
    )
