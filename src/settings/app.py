import logging
import typing as t

from pydantic import AfterValidator, Field, computed_field
from pydantic.networks import AnyUrl, PostgresDsn
from pydantic_core import MultiHostUrl

from .base import AppEnv, BaseAppSettings


def remove_trailing_slashes(urls: list[AnyUrl]) -> list[AnyUrl]:
    sanitized_urls = []
    for url in urls:
        sanitized_urls.append(AnyUrl(str(url).rstrip("/")))
    return sanitized_urls


class AppSettings(BaseAppSettings):
    API_V1_PREFIX: str = "/api/v1"

    OPENAPI_URL: str = "/openapi.json"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # TODO:

    DOMAIN: str = "localhost"  # TODO:

    @computed_field  # type: ignore[misc]
    @property
    def SERVER_URL(self) -> str:  # noqa: N802
        if self.APP_ENV is AppEnv.DEV:
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    CORS_ORIGINS: t.Annotated[
        list[AnyUrl], AfterValidator(remove_trailing_slashes)
    ] = Field(default_factory=list)

    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = ""

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

    logging_level: int = logging.INFO
    loggers: tuple[str, ...] = ()

    def configure_logging(self) -> None:
        pass
