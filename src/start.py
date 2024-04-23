import os
from enum import IntEnum, unique

from loguru import logger

import services
from domain import usecases
from infrastructure.api_servers.fastapi_ import FastAPIServer
from infrastructure.repositories import sqlalchemy_
from settings import get_app_settings


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        settings = get_app_settings()

        bcrypt_password_service = services.security.password.BCryptPasswordService()
        jwt_service = services.security.token.JWTService()
        user_alchemy = sqlalchemy_.user.AlchemyUserRepository(str(settings.POSTGRES_DSN))
        movie_alchemy = sqlalchemy_.movie.AlchemyMovieRepository(str(settings.POSTGRES_DSN))
        review_alchemy = sqlalchemy_.review.AlchemyReviewRepository(str(settings.POSTGRES_DSN))

        auth_usecases_builder = usecases.auth.AuthUsecasesBuilder(
            user_repository=user_alchemy,
            password_service=bcrypt_password_service,
            token_service=jwt_service,
            secret=settings.SECRET_KEY,
            access_token_expires_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=user_alchemy,
            password_service=bcrypt_password_service,
        )
        moview_usecases_builder = usecases.movie.MovieUsecasesBuilder(movie_repository=movie_alchemy)
        review_usecases_builder = usecases.review.ReviewUsecasesBuilder(review_repository=review_alchemy)

        api_server = FastAPIServer(
            auth_usecases_builder=auth_usecases_builder,
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
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    try:
        api_server.run(port=settings.SERVING_PORT)
    except Exception:
        msg_crit = "Got unhandled error during service process"
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    exit_code = main()

    os._exit(exit_code)
