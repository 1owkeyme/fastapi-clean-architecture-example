import logging
import secrets
import sys
import typing as t
from types import FrameType
from typing import cast

from loguru import logger
from pydantic import AfterValidator, Field, computed_field
from pydantic.networks import AnyUrl, PostgresDsn
from pydantic_core import MultiHostUrl

from .base import BaseAppSettings


def remove_trailing_slashes(urls: list[AnyUrl]) -> list[AnyUrl]:
    sanitized_urls = []
    for url in urls:
        sanitized_urls.append(AnyUrl(str(url).rstrip("/")))
    return sanitized_urls


class AppSettings(BaseAppSettings):
    def model_post_init(
        self,
        __context: t.Any,  # noqa: ARG002, ANN401 # since that's pydantic typing
    ) -> None:
        self.__configure_logging()

    API_V1_PREFIX: str = "/api/v1"

    OPENAPI_URL: str = "/openapi.json"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    SECRET_KEY: str = secrets.token_urlsafe(32)

    SERVING_PORT: int = 4343
    CORS_ORIGINS: t.Annotated[list[AnyUrl], AfterValidator(remove_trailing_slashes)] = Field(default_factory=list)

    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USERNAME: str = Field(alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

    ECHO_SQL: bool = False

    @computed_field  # type:ignore[misc]
    @property
    def POSTGRES_DSN(self) -> PostgresDsn:  # noqa: N802
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            username=self.POSTGRES_USERNAME,
            password=self.POSTGRES_PASSWORD,
            path=self.POSTGRES_DB,
        )

    FIRST_SUPER_USER_USERNAME: str
    FIRST_SUPER_USER_PASSWORD: str

    logging_level: int = logging.INFO
    existing_loggers: tuple[str, ...] = ("uvicorn.asgi", "uvicorn.access")

    def __configure_logging(self) -> None:
        logging.getLogger().handlers = [LogInterceptHandler()]
        for logger_name in self.existing_loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [LogInterceptHandler(level=self.logging_level)]

        logger.remove(0)
        logger.add(
            sys.stdout,
            filter=lambda record: record["level"].no < logging.WARNING,
            level=logging.getLevelName(logging.INFO),
        )
        logger.add(
            sys.stderr,
            filter=lambda record: record["level"].no >= logging.WARNING,
            level=logging.getLevelName(logging.WARNING),
        )


class LogInterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )
