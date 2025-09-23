from pydantic_settings import BaseSettings
from pydantic import computed_field
from typing import List
import os

class Settings(BaseSettings):
    API_PREFIX: str = "/api"

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    ALLOWED_ORIGINS: str = "*"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?sslmode=require"
        )

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "..", "..", "..", ".env")
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()