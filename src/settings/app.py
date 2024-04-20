import logging

from pydantic.types import StrictInt, StrictStr

from .base import BaseAppSettings


class AppSettings(BaseAppSettings):
    logging_level: StrictInt = logging.INFO
    loggers: tuple[StrictStr, ...] = ()

    def configure_logging(self) -> None:
        pass
