import typing as t

from ..base import ErrorResponse, ErrorResult


class ValidationErrorResult(ErrorResult):
    code: int = 5002
    message: str


class ValidationErrorResponse(ErrorResponse):
    error: ValidationErrorResult

    @classmethod
    def create(cls, details: str) -> t.Self:
        message = f"Got invalid data in request.\nDetails: `{details}`"
        return cls(error=ValidationErrorResult(message=message))
