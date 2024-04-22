import typing as t
from enum import IntEnum
from http import HTTPStatus

from common import StrictBaseModel


class ErrorCode(IntEnum):
    Unauthenticated = 401
    Unauthorized = 403


class ErrorResult(StrictBaseModel):
    message: str
    code: int


class ErrorResponse(StrictBaseModel):
    error: ErrorResult


class HTTPErrorResponse(StrictBaseModel):
    message: str


class ValidationErrorResult(ErrorResult):
    code: int = HTTPStatus.UNPROCESSABLE_ENTITY
    message: str


class ValidationErrorResponse(ErrorResponse):
    error: ValidationErrorResult

    @classmethod
    def create(cls, details: str) -> t.Self:
        message = f"Got invalid data in request.\nDetails: `{details}`"
        return cls(error=ValidationErrorResult(message=message))
