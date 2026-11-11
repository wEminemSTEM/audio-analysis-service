"""Application settings.

Values are read from environment variables (or a local .env file), so the same
code runs locally, in Docker, and on AWS with only configuration changing.
"""

from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Audio Analysis Service"
    environment: str = "local"
    postgres_user: str = "audio_app"
    postgres_password: SecretStr = SecretStr("super_secret_password")
    postgres_db: str = "audio_analysis"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    api_v1_prefix: str = "/api/v1"

    @property
    def database_url(self) -> URL:
        return URL.create(
            drivername="postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )


@lru_cache
def get_settings() -> Settings:
    """Return one shared Settings instance (cached so .env is read once)."""
    return Settings()
