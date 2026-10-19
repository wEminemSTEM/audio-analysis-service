import pytest
from fastapi.testclient import TestClient

from app.main import create_app


@pytest.fixture
def client() -> TestClient:
    """A test client that sends requests to the app in memory (no server needed)."""
    return TestClient(create_app())
