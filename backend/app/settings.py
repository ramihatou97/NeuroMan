import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "MyPlatform"
    ENV: str = os.getenv("ENV", "development")
    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Singleton settings instance for import everywhere
settings = Settings()