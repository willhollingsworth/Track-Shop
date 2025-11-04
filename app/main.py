"""Main application entry point for the Track Shop FastAPI app."""

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.routers import cart, home, tracks
from app.routers.users import login, register

# load environment variables
load_dotenv()

# setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(title="Track Shop")

# load and check for middleware secret key
secret_key = os.getenv("MIDDLEWARE_SECRET_KEY")
if not secret_key:
    msg = "Secret key not set in .env"
    raise ValueError(msg)

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=secret_key)

# Include home routes
app.include_router(home.router)

# Include user routes
app.include_router(register.router)
app.include_router(login.router)

# Include track routes
app.include_router(tracks.router)

# include cart routes
app.include_router(cart.router)
