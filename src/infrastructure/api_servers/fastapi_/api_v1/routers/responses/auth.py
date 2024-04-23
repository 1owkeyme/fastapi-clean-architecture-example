import typing as t

from ..schemas.auth import TokenInfo
from . import base


LoginResponse: t.TypeAlias = TokenInfo  # Strict schema defined by FastAPI


class InvalidCredentialsResult(base.ErrorResult):
    code: base.error.ErrorCode = base.error.ErrorCode.UNAUTHORIZED
    message: str = "Invalid credentials"


class InvalidCredentialsResponse(base.error.ErrorResponse):
    error: InvalidCredentialsResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=InvalidCredentialsResult())


class UnauthenticatedErrorResult(base.error.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.UNAUTHENTICATED
    message: str = "Access denied. Please log in to continue"


class UnauthenticatedErrorResponse(base.error.ErrorResponse):
    error: UnauthenticatedErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=UnauthenticatedErrorResult())


class UnauthorizedErrorResult(base.ErrorResult):
    code: base.ErrorCode = base.ErrorCode.UNAUTHORIZED
    message: str = "Permission denied. Access restricted"


class UnauthorizedErrorResponse(base.error.ErrorResponse):
    error: UnauthorizedErrorResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=UnauthorizedErrorResult())
