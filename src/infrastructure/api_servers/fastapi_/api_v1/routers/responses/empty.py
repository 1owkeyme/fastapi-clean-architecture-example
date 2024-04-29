import typing as t

from common import StrictBaseModel

from .base import SuccessResponse


class EmptyResult(StrictBaseModel):
    pass


class EmptyResponse(SuccessResponse):
    result: StrictBaseModel

    @classmethod
    def new(cls) -> t.Self:
        return cls(result=EmptyResult())
