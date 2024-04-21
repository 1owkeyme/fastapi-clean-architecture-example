from ..base import ErrorResponse, ErrorResult


class InternalErrorResult(ErrorResult):
    code: int = 5001
    message: str = "Got internal error"


class InternalErrorResponse(ErrorResponse):
    error: InternalErrorResult = InternalErrorResult()
