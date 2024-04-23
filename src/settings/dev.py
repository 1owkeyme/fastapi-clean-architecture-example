import logging

from pydantic_settings import SettingsConfigDict

from .app import AppSettings


class DevAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file=".env.dev")

    logging_level: int = logging.DEBUG
