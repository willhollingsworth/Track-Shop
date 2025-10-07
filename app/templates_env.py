"""Template configuration for FastAPI using Jinja2."""

from fastapi.templating import Jinja2Templates

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")
