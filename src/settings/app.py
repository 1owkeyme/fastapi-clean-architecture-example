import logging

from pydantic import computed_field
from pydantic.networks import PostgresDsn
from pydantic_core import MultiHostUrl

from .base import BaseAppSettings


class AppSettings(BaseAppSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    @computed_field
    @property
    def POSTGRES_DSN(self) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            username=self.POSTGRES_USERNAME,
            password=self.POSTGRES_PASSWORD,
            path=self.POSTGRES_DB,
        )

    logging_level: int = logging.INFO
    loggers: tuple[str, ...] = ()

    def configure_logging(self) -> None:
        pass
