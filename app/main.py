"""Main application entry point for the Track Shop FastAPI app.

Sets up static files, templates, and the root endpoint.
"""

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI(title="Track Shop")

# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request) -> _TemplateResponse:
    """Render the home page using the index.html Jinja2 template."""
    return templates.TemplateResponse("index.html", {"request": request})
