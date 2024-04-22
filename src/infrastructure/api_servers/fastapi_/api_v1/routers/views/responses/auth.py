import typing as t

from ..auth import TokenInfo
from . import base


LoginResponse: t.TypeAlias = TokenInfo  # Strict schema defined by FastAPI


class InvalidCredentialsResult(base.ErrorResult):
    code: int = base.error.ErrorCode.Unauthorized
    message: str = "Invalid credentials"


class InvalidCredentialsResponse(base.error.ErrorResponse):
    error: InvalidCredentialsResult

    @classmethod
    def new(cls) -> t.Self:
        return cls(error=InvalidCredentialsResult())
