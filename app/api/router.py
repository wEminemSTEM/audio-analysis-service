"""Collects every versioned route module into one router.

New features (auth, uploads, tracks, analysis) each get their own module in
app/api/routes/ and are registered here.
"""

from fastapi import APIRouter

api_router = APIRouter()

# Example for later:
# from app.api.routes import uploads
# api_router.include_router(uploads.router, prefix="/uploads")
