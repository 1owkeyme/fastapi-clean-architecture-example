import typing as t
from http import HTTPStatus

from loguru import logger
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from domain import usecases

from . import responses
from .dependencies import auth_errors


async def handle_http_exception(
    request: Request,
    exc: HTTPException,
) -> JSONResponse:
    if exc.status_code == HTTPStatus.UNAUTHORIZED:
        return await handle_unauthenticated_error(request, None)

    details = exc.detail

    msg_warn = f"HTTP exception occurred.\nDetails: {details}."
    logger.warning(msg_warn)

    body = responses.base.error.HTTPErrorResponse(message=details)

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

    body = responses.base.error.ValidationErrorResponse.new(details)

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=body.model_dump(),
    )


async def handle_usecase_critical_exception(
    request: Request,  # noqa: ARG001
    exc: usecases.errors.UsecaseCriticalError,  # noqa: ARG001
) -> JSONResponse:
    msg_crit = "Unhandled usecase critical error has occurred"
    logger.opt(exception=True).critical(msg_crit)

    body = responses.base.error.UnhandledErrorResponse.new()

    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


async def handle_usecase_exception(
    request: Request,  # noqa: ARG001
    exc: usecases.errors.UsecaseError,  # noqa: ARG001
) -> JSONResponse:
    msg_err = "Unhandled usecase error has occurred"
    logger.opt(exception=True).error(msg_err)

    body = responses.base.error.UnhandledErrorResponse.new()

    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


async def handle_unauthenticated_error(
    request: Request,  # noqa: ARG001
    exc: auth_errors.UnauthenticatedError | None = None,  # noqa: ARG001
) -> JSONResponse:
    msg_warn = "Access denied for incoming request"
    logger.warning(msg_warn)

    body = responses.auth.UnauthenticatedErrorResponse.new()
    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


async def handle_unauthorized_error(
    request: Request,  # noqa: ARG001
    exc: auth_errors.UnauthorizedError,  # noqa: ARG001
) -> JSONResponse:
    msg_warn = "Permission denied for incoming  request"
    logger.warning(msg_warn)

    body = responses.auth.UnauthorizedErrorResponse.new()
    return JSONResponse(status_code=HTTPStatus.OK, content=body.model_dump())


EXCEPTION_TO_HANDLER: (
    dict[int | t.Type[Exception], t.Callable[[Request, t.Any], t.Coroutine[t.Any, t.Any, Response]]] | None
) = {
    HTTPException: handle_http_exception,
    ValidationError: handle_request_validation_exception,
    usecases.errors.UsecaseCriticalError: handle_usecase_critical_exception,
    usecases.errors.UsecaseError: handle_usecase_exception,
    auth_errors.UnauthenticatedError: handle_unauthenticated_error,
    auth_errors.UnauthorizedError: handle_unauthorized_error,
}
