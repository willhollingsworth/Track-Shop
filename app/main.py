"""Main application entry point for the Track Shop FastAPI app.

Sets up static files, templates, and the root endpoint.
"""

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI(title="Track Shop")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request) -> _TemplateResponse:
    """Render the home page using the index.html Jinja2 template."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/popular")
def popular(request: Request) -> _TemplateResponse:
    """Render the home page using the index.html Jinja2 template."""
    return templates.TemplateResponse("popular.html", {"request": request})


@app.get("/recommended")
def recommended(request: Request) -> _TemplateResponse:
    """Render the home page using the index.html Jinja2 template."""
    return templates.TemplateResponse("recommended.html", {"request": request})


@app.get("/new")
def new(request: Request) -> _TemplateResponse:
    """Render the home page using the index.html Jinja2 template."""
    return templates.TemplateResponse("new.html", {"request": request})
