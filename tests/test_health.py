import pytest

from app.core.config import get_settings


@pytest.fixture
def set_test_environment(monkeypatch):
    get_settings.cache_clear()
    monkeypatch.setenv("ENVIRONMENT", "test")
    yield
    get_settings.cache_clear()


def test_health_returns_ok(set_test_environment, client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "environment": "test"}


def test_openapi_docs_available(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert response.json()["info"]["title"] == "Audio Analysis Service"
