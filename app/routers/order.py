"""Order router."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlmodel import Session
from starlette.responses import RedirectResponse, Response

from app.db.db import get_session
from app.services.order import get_order_details
from app.services.user import get_current_user
from app.templates_env import templates

router = APIRouter()


@router.get("/order/{order_id}", name="order_detail")
def order_detail_page(
    request: Request,
    order_id: int,
    session: Annotated[Session, Depends(get_session)],
) -> Response:
    """Display order details page."""
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    order = get_order_details(session, order_id)

    # If order doesn't exist or doesn't belong to user (and user is not admin)
    if not order or (order.user_id != user.user_id and not user.admin):
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        "order_detail.html",
        {
            "request": request,
            "order": order,
        },
    )
