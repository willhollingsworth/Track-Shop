"""Main application entry point for the Track Shop FastAPI app.

Sets up static files, templates, and the root endpoint.
"""

from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, func, select

from app.db.db import get_session
from app.models import Track

app = FastAPI(title="Track Shop")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request, session: Annotated[Session, Depends(get_session)]) -> object:
    """Home page showing 5 random tracks."""
    tracks = session.exec(
        select(Track).order_by(func.random()).limit(5),
    ).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tracks": tracks},
    )


@app.get("/popular")
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


@app.get("/recommended")
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
