"""Cart router module."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlmodel import Session
from starlette.responses import Response

from app.db.db import get_session
from app.services.cart import (
    add_to_cart,
    get_cart,
    get_cart_count,
    remove_from_cart,
)

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/cart/modal-content")
def get_cart_modal_content(
    request: Request,
) -> Response:
    """Return just the cart modal content."""
    cart = get_cart(request)
    return templates.TemplateResponse(
        "cart_modal_content.html",
        {
            "request": request,
            "cart": cart.items,
            "total": cart.total,
            "count": cart.count,
        },
    )


@router.post("/cart/add/{track_id}")
def add_item(
    track_id: int,
    request: Request,
    session: Annotated[Session, Depends(get_session)],
) -> Response:
    """Add item to cart with validation and return updated button."""
    add_to_cart(request, session, track_id)
    cart = get_cart(request)

    response = templates.TemplateResponse(
        "cart_with_button_update.html",
        {
            "request": request,
            "cart": cart.items,
            "total": cart.total,
            "count": cart.count,
            "track_id": track_id,
            "is_in_cart": True,
            "swap_oob": True,
        },
    )
    response.headers["HX-Trigger"] = "cartUpdated"
    return response


@router.post("/cart/remove/{track_id}")
def remove_item(track_id: int, request: Request) -> Response:
    """Remove item from cart and return updated button."""
    remove_from_cart(request, track_id)
    cart = get_cart(request)

    response = templates.TemplateResponse(
        "cart_with_button_update.html",
        {
            "request": request,
            "cart": cart.items,
            "total": cart.total,
            "count": cart.count,
            "track_id": track_id,
            "is_in_cart": False,
            "swap_oob": True,
        },
    )
    response.headers["HX-Trigger"] = "cartUpdated"
    return response


@router.get("/cart/count")
def cart_count(request: Request) -> Response:
    """Return cart count for navbar updates."""
    count = get_cart_count(request)
    return Response(content=str(count), media_type="text/plain")
