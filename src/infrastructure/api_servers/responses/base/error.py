from common import StrictBaseModel


class ErrorResult(StrictBaseModel):
    message: str
    code: int


class ErrorResponse(StrictBaseModel):
    error: ErrorResult
