"""Utility functions for formatting."""

from pydantic import ValidationError


def format_validation_error(e: ValidationError) -> str:
    """Return a human-readable message from a Pydantic ValidationError."""
    if not e.errors():
        return "Invalid input."
    err = e.errors()[0]
    msg = err.get("msg", "Invalid input.")
    if "string_too_" in err["type"]:
        msg = msg.replace("String", str(err["loc"][0]))
    return msg
