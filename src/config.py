from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database configuration settings."""

    DATABASE_URL: str = "postgresql+asyncpg://name:pass@localhost:5432/vyltra"
    DATABASE_ECHO: bool = False


database_config = DatabaseConfig()
