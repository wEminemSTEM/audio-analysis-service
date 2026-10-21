from app.core.config import get_settings
import pytest


@pytest.fixture(autouse=True)
def set_test_environment(monkeypatch):
    get_settings.cache_clear()
    monkeypatch.setenv("environment", "test")


def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "local"}


def test_openapi_docs_available(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "Audio Analysis Service"
