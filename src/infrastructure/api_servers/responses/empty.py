import typing as t

from .base import SuccessResponse


class EmptyResponse(SuccessResponse):
    result: dict

    @classmethod
    def construct(cls) -> t.Self:
        return cls(result={})
