from enum import StrEnum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(StrEnum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    app_env: AppEnv = AppEnv.PROD
