from pydantic_settings import SettingsConfigDict

from .app import AppSettings


class ProdAppSettings(AppSettings):
    model_config = SettingsConfigDict(env_file=".env.prod")
