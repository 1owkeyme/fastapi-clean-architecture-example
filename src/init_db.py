import asyncio
import os
from enum import IntEnum, unique

import services
from domain import entities, usecases
from infrastructure.repositories.sqlalchemy_ import SQLAlchemy
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

        sql_alchemy = SQLAlchemy(str(settings.POSTGRES_DSN))

        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=sql_alchemy,
            hash_service=bcrypt_password_service,
            token_service=jwt_service,
            secret=settings.SECRET_KEY,
            access_token_expires_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        )
        first_super_user_plain_credentials = entities.user.PlainCredentials(
            username=settings.FIRST_SUPER_USER_USERNAME,
            password=settings.FIRST_SUPER_USER_PASSWORD,
        )
    except Exception:
        # TODO: logging
        return ExitCode.FAILURE

    try:
        asyncio.run(user_usecases_builder.construct_create_user_usecase().execute(first_super_user_plain_credentials))
    except Exception:
        # TODO: logging
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    exit_code = main()

    os._exit(exit_code)
