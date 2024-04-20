from enum import StrEnum

from pydantic_settings import BaseSettings


class AppEnv(StrEnum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnv = AppEnv.PROD
