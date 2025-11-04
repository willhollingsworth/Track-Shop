"""Pydantic schemas.

Used for data validation
"""

from fastapi import Form
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ValidationInfo,
    computed_field,
    field_validator,
)
from pydantic_core import PydanticCustomError


class UserRegister(BaseModel):
    """Schema for user registration."""

    email: EmailStr
    password: str = Field(
        ...,
        min_length=8,
        max_length=30,
        json_schema_extra={
            "description": "Password must be at least 8 characters long",
        },
    )
    confirm_password: str
    phone: str = Field(
        ...,
        min_length=8,
        max_length=30,
        json_schema_extra={
            "description": "Phone number must be at least 8 characters long",
        },
    )
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)

    @field_validator("confirm_password")
    @classmethod
    def passwords_match(cls, value: str, info: ValidationInfo) -> str:
        """Ensure password and confirm_password match."""
        password = info.data.get("password")
        if password and value != password:
            raise PydanticCustomError(
                "password_mismatch",
                "Passwords do not match",
            )
        return value

    @field_validator("phone")
    @classmethod
    def phone_number_valid(cls, value: str) -> str:
        """Ensure phone number is valid"""
        phone_number = value
        strip_chars = " -()+"
        for c in strip_chars:
            phone_number = phone_number.replace(c, "")
        if not phone_number.isdigit():
            code = "phone_number_invalid"
            msg = "Phone Number is not a valid number"
            raise PydanticCustomError(
                code,
                msg,
            )
        return value

    @classmethod
    def as_form(
        cls,
        email: str = Form(...),
        password: str = Form(...),
        confirm_password: str = Form(...),
        phone: str = Form(...),
        first_name: str = Form(...),
        last_name: str = Form(...),
    ) -> "UserRegister":
        """Handle ingestion of form data."""
        return cls(
            email=email,
            password=password,
            confirm_password=confirm_password,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
        )


class CartTrack(BaseModel):
    """Represents a single track in the shopping cart."""

    track_id: int
    title: str
    artist: str
    price: float


class Cart(BaseModel):
    """Represents the user's shopping cart."""

    items: list[CartTrack] = []

    @computed_field
    @property
    def total(self) -> float:
        """Calculate the total price of all items in the cart."""
        return sum(item.price for item in self.items)

    @computed_field
    @property
    def count(self) -> int:
        """Get the number of items in the cart."""
        return len(self.items)
