import logging
import typing as t
from http import HTTPStatus

from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from domain import usecases

from . import views


logger = logging.getLogger(__name__)


async def handle_http_exception(
    request: Request,  # noqa: ARG001
    exc: HTTPException,
) -> JSONResponse:
    details = exc.detail

    msg_warn = f"HTTP exception occurred.\nDetails: {details}."
    logger.warning(msg_warn)

    body = views.responses.base.error.HTTPErrorResponse(message=details)

    return JSONResponse(
        status_code=exc.status_code,
        content=body.model_dump(),
    )


async def handle_request_validation_exception(
    request: Request,  # noqa: ARG001
    exc: ValidationError,
) -> JSONResponse:
    details = exc.json(include_url=False)

    msg_warn = f"Request didn't pass validation.\nDetails: {details}."
    logger.warning(msg_warn)

    body = views.responses.base.error.ValidationErrorResponse.new(details)

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=body.model_dump(),
    )


async def handle_usecase_critical_exception(
    request: Request,  # noqa:ARG001
    exc: usecases.interfaces.errors.UsecaseCriticalError,  # noqa:ARG001
) -> JSONResponse:
    msg_crit = "Unhandled usecase critical error has occurred"
    logger.critical(msg_crit, exc_info=True)

    body = views.responses.base.error.UnhandledErrorResponse.new()

    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


async def handle_usecase_exception(
    request: Request,  # noqa:ARG001
    exc: usecases.interfaces.errors.UsecaseError,  # noqa:ARG001
) -> JSONResponse:
    msg_err = "Unhandled usecase error has occurred"
    logger.error(msg_err, exc_info=True)

    body = views.responses.base.error.UnhandledErrorResponse.new()

    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


# TODO: test this one
EXCEPTION_TO_HANDLER: (
    dict[int | t.Type[Exception], t.Callable[[Request, t.Any], t.Coroutine[t.Any, t.Any, Response]]] | None
) = {
    usecases.interfaces.errors.UsecaseCriticalError: handle_usecase_critical_exception,
    usecases.interfaces.errors.UsecaseError: handle_usecase_exception,
    HTTPException: handle_http_exception,
    ValidationError: handle_request_validation_exception,
}
