import logging
import os
from enum import IntEnum, unique

import services
from domain import usecases
from infrastructure.api_servers.fastapi_ import FastAPIServer
from infrastructure.repositories.sqlalchemy_ import SQLAlchemy
from settings import get_app_settings


logger = logging.getLogger(__name__)


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        settings = get_app_settings()
        settings.configure_logging()

        bcrypt_password_service = services.security.password.BCryptPasswordService()
        jwt_service = services.security.token.JWTService()

        sql_alchemy = SQLAlchemy(str(settings.POSTGRES_DSN))

        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=sql_alchemy,
            hash_service=bcrypt_password_service,
            token_service=jwt_service,
            secret=settings.SECRET_KEY,
            access_token_expires_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        moview_usecases_builder = usecases.movie.MovieUsecasesBuilder(movie_repository=sql_alchemy)
        review_usecases_builder = usecases.review.ReviewUsecasesBuilder(review_repository=sql_alchemy)

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
        msg_crit = "Got unhandled error during service initialization"
        logger.critical(msg_crit, exc_info=True)
        return ExitCode.FAILURE

    try:
        api_server.run(port=settings.SERVING_PORT)
    except Exception:
        msg_crit = "Got unhandled error during service process"
        logger.critical(msg_crit, exc_info=True)
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    exit_code = main()

    os._exit(exit_code)
