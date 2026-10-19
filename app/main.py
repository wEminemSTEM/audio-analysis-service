"""FastAPI entry point.

Run locally with:  uvicorn app.main:app --reload
Interactive API docs are then at http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.api.routes import health
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Build the app. A factory function makes it easy to create fresh
    instances in tests with different settings."""
    settings = get_settings()

    app = FastAPI(title=settings.app_name, version="0.1.0")

    # Unversioned: infrastructure endpoints that should never change shape.
    app.include_router(health.router)

    # Versioned: the public API. A /v2 can be added later without breaking /v1 clients.
    app.include_router(api_router, prefix=settings.api_v1_prefix)

    return app


app = create_app()
