"""Login router."""

from fastapi import APIRouter, Depends, Form, Request, status
from sqlmodel import Session
from starlette.responses import RedirectResponse, Response

from app.db.db import get_session
from app.services.user import authenticate_user
from app.templates_env import templates

router = APIRouter()


@router.get("/login")
def login_page(request: Request) -> Response:
    """Display login page."""
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login_user(
    request: Request,
    session: Session = Depends(get_session),
    email: str = Form(...),
    password: str = Form(...),
) -> Response:
    user = authenticate_user(session, email, password)
    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid email or password"},
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    # Set user_id in session
    request.session["user_id"] = user.user_id
    return RedirectResponse(url="/", status_code=303)


@router.get("/logout")
def logout(request: Request) -> Response:
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)
