"""Checkout router."""

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, status
from pydantic import ValidationError
from sqlmodel import Session
from starlette.responses import RedirectResponse, Response

from app.db.db import get_session
from app.schemas import PaymentInfo
from app.services.cart import CART_KEY, get_cart
from app.services.order import create_order_from_cart
from app.services.user import get_current_user
from app.templates_env import templates
from app.utils import formatting

router = APIRouter()


@router.get("/checkout", name="checkout")
def checkout_page(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
) -> Response:
    """Display checkout page."""
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    cart = get_cart(request)
    if not cart.items:
        return RedirectResponse(url="/", status_code=303)

    # Calculate tax
    subtotal = cart.total
    tax = subtotal * 0.1
    total = subtotal + tax

    return templates.TemplateResponse(
        "checkout.html",
        {
            "request": request,
            "cart": cart.items,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
        },
    )


@router.post("/checkout", name="checkout")
def process_checkout(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    cc_number: Annotated[str, Form(...)],
    cv_number: Annotated[str, Form(...)],
    expiry: Annotated[str, Form(...)],
    name: Annotated[str, Form(...)],
    address: Annotated[str, Form(...)],
) -> Response:
    """Process checkout payment."""
    user = get_current_user(request, session)
    if not user:
        return RedirectResponse(url="/login", status_code=303)

    cart = get_cart(request)
    if not cart.items:
        return RedirectResponse(url="/", status_code=303)

    # Validate payment info
    try:
        _payment_info = PaymentInfo(
            cc_number=cc_number,
            cv_number=cv_number,
            expiry=expiry,
            name=name,
            address=address,
        )
    except ValidationError as e:
        error_msg = formatting.format_validation_error(e)
        subtotal = cart.total
        tax = subtotal * 0.1
        total = subtotal + tax

        return templates.TemplateResponse(
            "checkout.html",
            {
                "request": request,
                "cart": cart.items,
                "subtotal": subtotal,
                "tax": tax,
                "total": total,
                "error": error_msg,
                # Preserve form values
                "form_data": {
                    "name": name,
                    "cc_number": cc_number,
                    "expiry": expiry,
                    "cv_number": cv_number,
                    "address": address,
                },
            },
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # Create order from cart
    if user.user_id is None:
        return RedirectResponse(url="/login", status_code=303)
    order = create_order_from_cart(session, user.user_id, cart)

    # Clear cart
    request.session[CART_KEY] = {"items": []}

    return RedirectResponse(url=f"/order/{order.order_id}", status_code=303)
