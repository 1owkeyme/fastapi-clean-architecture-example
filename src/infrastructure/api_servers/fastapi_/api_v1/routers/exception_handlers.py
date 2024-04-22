import logging
import typing as t
from http import HTTPStatus

from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from .views.responses.base.error import HTTPErrorResponse, ValidationErrorResponse


logger = logging.getLogger(__name__)


async def handle_http_exception(
    request: Request,  # noqa: ARG001
    exc: HTTPException,
) -> JSONResponse:
    details = exc.detail

    msg_warn = f"HTTP exception occurred.\nDetails: {details}."
    logger.warning(msg_warn)

    body = HTTPErrorResponse(message=details)

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

    body = ValidationErrorResponse.create(details)

    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=body.model_dump(),
    )


EXCEPTION_TO_HANDLER: (
    dict[int | t.Type[Exception], t.Callable[[Request, t.Any], t.Coroutine[t.Any, t.Any, Response]]] | None
) = {
    HTTPException: handle_http_exception,
    ValidationError: handle_request_validation_exception,
}
