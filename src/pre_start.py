import asyncio
import os
from enum import IntEnum, unique

from loguru import logger
from tenacity import retry, stop_after_attempt, wait_fixed

import services
from domain import usecases
from infrastructure.repositories import sqlalchemy_
from settings import get_app_settings


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


__MAX_ATTEMPTS = 60 * 5
__WAIT_INTERVAL = 1


@retry(stop=stop_after_attempt(__MAX_ATTEMPTS), wait=wait_fixed(__WAIT_INTERVAL))
def get_pong(get_all_users_usecase: usecases.user.GetAllUsersUsecase) -> None:
    try:
        asyncio.run(get_all_users_usecase.execute())
    except Exception as exc:
        msg_err = f"{exc}"
        logger.error(msg_err)
        raise


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

    except Exception:
        msg_crit = "Got unhandled error during service initialization"
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    try:
        get_pong(user_usecases_builder.construct_get_all_users_usecase())
    except Exception:
        msg_crit = "Got unhandled error during service process"
        logger.opt(exception=True).critical(msg_crit)
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    msg_info = "Initilization service has started"
    logger.info(msg_info)

    exit_code = main()

    msg_info = "Initilization service has finished"
    logger.info(msg_info)

    os._exit(exit_code)
