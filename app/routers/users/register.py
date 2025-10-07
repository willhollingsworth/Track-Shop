"""Register router."""

from fastapi import APIRouter, Request
from starlette.responses import Response

from app.templates_env import templates

router = APIRouter()


@router.get("/register")
def register_page(request: Request) -> Response:
    """Display registration page."""
    return templates.TemplateResponse("register.html", {"request": request})
