import asyncio
import logging
import os
from enum import IntEnum, unique

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

import services
from domain import usecases
from infrastructure.repositories import sqlalchemy_
from settings import get_app_settings


logger = logging.getLogger(__name__)


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


__MAX_ATTEMPTS = 60 * 5
__WAIT_INTERVAL = 1


@retry(
    stop=stop_after_attempt(__MAX_ATTEMPTS),
    wait=wait_fixed(__WAIT_INTERVAL),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
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
        settings.configure_logging()

        bcrypt_password_service = services.security.password.BCryptPasswordService()
        user_alchemy = sqlalchemy_.user.AlchemyUserRepository(str(settings.POSTGRES_DSN))

        user_usecases_builder = usecases.user.UserUsecasesBuilder(
            user_repository=user_alchemy,
            password_service=bcrypt_password_service,
        )

    except Exception:
        msg_crit = "Got unhandled error during service initialization"
        logger.critical(msg_crit, exc_info=True)
        return ExitCode.FAILURE

    try:
        get_pong(user_usecases_builder.construct_get_all_users_usecase())
    except Exception:
        msg_crit = "Got unhandled error during service process"
        logger.critical(msg_crit, exc_info=True)
        return ExitCode.FAILURE

    return ExitCode.SUCCESS


if __name__ == "__main__":
    msg_info = "Initilization service has started"
    logger.info(msg_info)

    exit_code = main()

    msg_info = "Initilization service has finished"
    logger.info(msg_info)

    os._exit(exit_code)
