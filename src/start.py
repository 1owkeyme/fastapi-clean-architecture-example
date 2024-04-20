import os
from enum import IntEnum, unique

from infrastructure.api_servers.fastapi_ import FastAPIServer
from settings import get_app_settings


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        settings = get_app_settings()

        api_server = FastAPIServer(
            app_title=settings.APP_TITLE,
            api_v1_prefix=settings.API_V1_PREFIX,
            openapi_url=settings.OPENAPI_URL,
            cors_origins=[str(origin) for origin in settings.CORS_ORIGINS],
        )
    except Exception:
        # TODO: logging
        return ExitCode.FAILURE

    try:
        api_server.run(1111)
    except Exception:
        # TODO: logging
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    exit_code = main()

    os._exit(exit_code)
