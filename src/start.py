import os
from enum import IntEnum, unique

import services
from domain import usecases
from infrastructure.api_servers.fastapi_ import FastAPIServer
from infrastructure.repositories.sqlalchemy_ import SQLAlchemy
from settings import get_app_settings


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        settings = get_app_settings()

        sha256_hash_service = services.security.hash_.BCryptHashService()
        repository = SQLAlchemy(str(settings.POSTGRES_DSN))

        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=repository,
            hash_service=sha256_hash_service,
        )
        moview_usecases_builder = usecases.movie.MovieUsecasesBuilder(movie_repository=repository)
        review_usecases_builder = usecases.review.ReviewUsecasesBuilder(review_repository=repository)

        api_server = FastAPIServer(
            user_usecases_builder=user_usecases_builder,
            movie_usecases_builder=moview_usecases_builder,
            review_usecases_builder=review_usecases_builder,
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
