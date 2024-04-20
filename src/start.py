import os
from enum import IntEnum, unique

from infrastructure.api_server.fastapi_ import FastAPIServer


@unique
class ExitCode(IntEnum):
    SUCCESS = 0
    FAILURE = 1


def main() -> int:
    try:
        # TODO: use settings
        api_server = FastAPIServer()
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
