import secrets
from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(StrEnum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore", env_file=".env")

    APP_ENV: AppEnv = AppEnv.DEV
    APP_TITLE: str = "FastAPI Example Application"
    SECRET_KEY: str = secrets.token_urlsafe(32)
