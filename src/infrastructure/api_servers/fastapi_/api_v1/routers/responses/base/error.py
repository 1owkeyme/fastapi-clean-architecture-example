import typing as t

from common import StrictBaseModel

from .error_codes import ErrorCode


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


