"""Order handling service."""

from sqlmodel import Session

from app.models import Order, OrderTrack, Track
from app.schemas import Cart


def create_order_from_cart(
    session: Session,
    user_id: int,
    cart: Cart,
) -> Order:
    """Create a completed order from a shopping cart."""
    subtotal = 0.0
    track_prices: dict[int, float] = {}

    for item in cart.items:
        track = session.get(Track, item.track_id)
        if track is None:
            msg = f"Track with ID {item.track_id} not found."
            raise ValueError(msg)
        track_prices[item.track_id] = track.price
        subtotal += track.price

    # Calculate tax (using 10% as an example)
    tax = subtotal * 0.10
    total = subtotal + tax

    # Create order
    order = Order(
        user_id=user_id,
        subtotal=round(subtotal, 2),
        tax=round(tax, 2),
        total=round(total, 2),
    )
    session.add(order)
    session.flush()

    # Create order tracks
    for item in cart.items:
        if order.order_id is None:
            msg = "Order ID should not be None."
            raise ValueError(msg)
        order_track = OrderTrack(
            order_id=order.order_id,
            track_id=item.track_id,
            price_at_purchase=track_prices[item.track_id],
        )
        session.add(order_track)

    session.commit()
    session.refresh(order)

    return order


def get_order_details(
    session: Session,
    order_id: int,
) -> Order | None:
    """Get order details."""
    return session.get(Order, order_id)
