from fastapi import APIRouter, Request

from app.templates_env import templates

router = APIRouter()


@router.get("/register")
def register_page(request: Request) -> object:
    """Display registration page."""
    return templates.TemplateResponse("register.html", {"request": request})
