from common import StrictBaseModel


class HTTPErrorResponse(StrictBaseModel):
    message: str
