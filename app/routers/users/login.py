from fastapi import APIRouter, Request

from app.templates_env import templates

router = APIRouter()


@router.get("/login")
def login_page(request: Request) -> object:
    """Display login page."""
    return templates.TemplateResponse("login.html", {"request": request})
