"""Register router."""

import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from pydantic import ValidationError
from sqlmodel import Session, select
from starlette.responses import RedirectResponse, Response

from app.db.db import get_session
from app.models import User
from app.schemas import UserRegister
from app.services.user import hash_password
from app.templates_env import templates
from app.utils import formatting

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

router = APIRouter()


@router.get("/register")
def register_page(request: Request) -> Response:
    """Display registration page."""
    return templates.TemplateResponse("register.html", {"request": request})


@router.post("/register")
def register_user(  # noqa: PLR0913, PLR0917
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    email: Annotated[str, Form(...)],
    password: Annotated[str, Form(...)],
    confirm_password: Annotated[str, Form(...)],
    phone: Annotated[str, Form(...)],
) -> Response:
    logger.info(
        "attempting to register: email=%s",
        email,
    )
    try:
        # schema for validation
        form_data = UserRegister(
            email=email,
            password=password,
            confirm_password=confirm_password,
            phone=phone,
        )
    except ValidationError as e:
        # if the validation fails return a meaningful error message
        error_msg = formatting.format_validation_error(e)
        logger.info("user registering error: %s", error_msg)

        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": error_msg},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Check if email already exists
    existing_user = session.exec(
        select(User).where(User.email == form_data.email),
    ).first()
    if existing_user:
        return templates.TemplateResponse(
            "register.html",
            {"request": request, "error": "Email already registered"},
        )

    # Create new user with hashed password
    new_user = User(
        email=form_data.email,
        password=hash_password(form_data.password),
        phone=form_data.phone,
    )
    session.add(new_user)
    session.commit()
    logger.info("user registration successful: email=%s", new_user.email)
    return RedirectResponse(url="/login", status_code=303)
