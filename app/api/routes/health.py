"""Health check endpoint.

Load balancers, Docker, and CI use this to confirm the service is up.
Later (week 1-2) it can also report whether the database is reachable.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.config import get_settings

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str
    environment: str


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", environment=get_settings().environment)
