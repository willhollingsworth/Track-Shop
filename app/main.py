"""Main application entry point for the Track Shop FastAPI app."""

import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.routers import cart, checkout, order, search, tracks
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

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include track routes
app.include_router(tracks.router)

# Include user routes
app.include_router(register.router)
app.include_router(login.router)

# include cart routes
app.include_router(cart.router)

# include checkout routes
app.include_router(checkout.router)

# include order routes
app.include_router(order.router)

# include search routes
app.include_router(search.router)
