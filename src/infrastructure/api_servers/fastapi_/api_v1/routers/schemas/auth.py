import typing as t
from enum import StrEnum, unique

from pydantic import Field

from common import StrictBaseModel
from domain import entities


@unique
class TokenType(StrEnum):
    BEARER = "bearer"


class TokenInfo(StrictBaseModel):
    token_type: TokenType = TokenType.BEARER
    access_token: str = Field(
        examples=[
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.ZU43TYZENiuLdKJPpd-hnkFhRkpLPurixsKr-8m-kBc"
        ]
    )

    @classmethod
    def from_access_token_entity(cls, entity: entities.auth.AccessToken) -> t.Self:
        return cls(access_token=entity)
