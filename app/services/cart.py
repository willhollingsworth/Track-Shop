"""Cart service module."""

from fastapi import Request
from pydantic import ValidationError
from sqlmodel import Session

from app.schemas import Cart, CartTrack
from app.services.track import get_track_by_id  # Assumes this exists in track.py

CART_KEY = "shopping_cart"


def get_cart(request: Request) -> Cart:
    """Retrieve the cart from the session."""
    raw_cart = request.session.get(CART_KEY, {"items": []})
    try:
        return Cart.model_validate(raw_cart)
    except (ValidationError, TypeError, ValueError):
        # If validation fails, return empty cart
        return Cart(items=[])


def add_to_cart(
    request: Request,
    session: Session,
    track_id: int,
) -> None:  # Added session parameter
    """Add a track to the cart."""
    cart = get_cart(request)
    track = get_track_by_id(session, track_id)

    # track not found or no track id
    if not track or not track.track_id:
        return

    # track already in cart
    if any(item.track_id == track_id for item in cart.items):
        return

    # add track to cart
    cart.items.append(
        CartTrack(
            track_id=track.track_id,
            title=track.title,
            artist=track.artist,
            price=track.price,
        ),
    )
    request.session[CART_KEY] = cart.model_dump()


def remove_from_cart(request: Request, track_id: int) -> None:
    """Remove a track from the cart."""
    cart = get_cart(request)
    cart.items = [item for item in cart.items if item.track_id != track_id]
    request.session[CART_KEY] = cart.model_dump()


def get_cart_count(request: Request) -> int:
    """Get the number of items in the cart."""
    return len(get_cart(request).items)


def is_track_in_cart(request: Request, track_id: int) -> bool:
    """Check if a track is already in the cart."""
    cart = get_cart(request)
    return any(item.track_id == track_id for item in cart.items)
