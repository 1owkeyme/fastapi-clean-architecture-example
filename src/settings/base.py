import secrets
from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(StrEnum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


_DEFAULT_APP_ENV = AppEnv.DEV


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    APP_ENV: AppEnv = _DEFAULT_APP_ENV
    APP_TITLE: str = "FastAPI Example Application"
    SECRET_KEY: str = secrets.token_urlsafe(32)
