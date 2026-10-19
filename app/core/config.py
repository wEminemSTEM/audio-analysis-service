"""Application settings.

Values are read from environment variables (or a local .env file), so the same
code runs locally, in Docker, and on AWS with only configuration changing.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Audio Analysis Service"
    environment: str = "local"  # local | test | production
    api_v1_prefix: str = "/api/v1"


@lru_cache
def get_settings() -> Settings:
    """Return one shared Settings instance (cached so .env is read once)."""
    return Settings()
