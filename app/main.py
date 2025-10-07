"""Main application entry point for the Track Shop FastAPI app."""

from fastapi import FastAPI

from app.routers import home, tracks
from app.routers.users import login, register

app = FastAPI(title="Track Shop")


# Include home routes
app.include_router(home.router)

# Include user routes
app.include_router(register.router)
app.include_router(login.router)

# Include track routes
app.include_router(tracks.router)
