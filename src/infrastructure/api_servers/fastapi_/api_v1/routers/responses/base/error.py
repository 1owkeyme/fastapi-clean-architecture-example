import typing as t
from enum import IntEnum
from http import HTTPStatus

from common import StrictBaseModel


class ErrorCode(IntEnum):
    UNAUTHENTICATED = HTTPStatus.UNAUTHORIZED
    UNAUTHORIZED = HTTPStatus.FORBIDDEN
    VALIDATION_ERROR = HTTPStatus.UNPROCESSABLE_ENTITY
    UNHANDLED_SERVER_ERROR = HTTPStatus.INTERNAL_SERVER_ERROR


class ErrorResult(StrictBaseModel):
    code: ErrorCode
    message: str


class ErrorResponse(StrictBaseModel):
    error: ErrorResult


class HTTPErrorResponse(StrictBaseModel):
    message: str


class ValidationErrorResult(ErrorResult):
    code: ErrorCode = ErrorCode.VALIDATION_ERROR
    message: str


class ValidationErrorResponse(ErrorResponse):
    error: ValidationErrorResult

    @classmethod
    def new(cls, details: str) -> t.Self:
        message = f"Got invalid data in request.\nDetails: `{details}`"
        return cls(error=ValidationErrorResult(message=message))


class UnhandledErrorResult(ErrorResult):
    code: ErrorCode = ErrorCode.UNHANDLED_SERVER_ERROR
    message: str = "Unhandled server error has occurred"


class UnhandledErrorResponse(ErrorResponse):
    error: UnhandledErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=UnhandledErrorResult())
