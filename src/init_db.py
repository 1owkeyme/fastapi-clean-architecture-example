import asyncio
import os
from enum import IntEnum, unique

from loguru import logger

import services
from domain import entities, usecases
from infrastructure.repositories import sqlalchemy_
from settings import get_app_settings


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        settings = get_app_settings()
        settings.__configure_logging()

        bcrypt_password_service = services.security.password.BCryptPasswordService()
        user_alchemy = sqlalchemy_.user.AlchemyUserRepository(str(settings.POSTGRES_DSN))

        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=user_alchemy,
            password_service=bcrypt_password_service,
        )

        first_super_user_plain_credentials = entities.user.PlainCredentials(
            username=settings.FIRST_SUPER_USER_USERNAME,
            password=settings.FIRST_SUPER_USER_PASSWORD,
        )
    except Exception:
        msg_crit = "Got unhandled error during service initialization"
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    try:
        asyncio.run(user_usecases_builder.construct_create_user_usecase().execute(first_super_user_plain_credentials))
    except Exception:
        msg_crit = "Got unhandled error during service process"
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    msg_info = "Database initialization service has started"
    logger.info(msg_info)

    exit_code = main()

    msg_info = "Database initialization service has finished"
    logger.info(msg_info)

    os._exit(exit_code)
