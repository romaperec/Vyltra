from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database configuration settings."""

    DATABASE_URL: str = "postgresql+asyncpg://name:pass@localhost:5432/vyltra"
    DATABASE_ECHO: bool = False


database_config = DatabaseConfig()


# class JWTConfig(BaseSettings):
#     """JWT configuration settings."""

#     SECRET_KEY: str = "81764b7444bc16bd9c5502b576aa27eb0de2e35cb2e6f003e3f612fe6bae855c"
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
#     REFRESH_TOKEN_EXPIRE_DAYS: int = 7


# jwt_config = JWTConfig()
