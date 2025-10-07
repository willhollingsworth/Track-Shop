"""Login router."""

from fastapi import APIRouter, Request
from starlette.responses import Response

from app.templates_env import templates

router = APIRouter()


@router.get("/login")
def login_page(request: Request) -> Response:
    """Display login page."""
    return templates.TemplateResponse("login.html", {"request": request})
