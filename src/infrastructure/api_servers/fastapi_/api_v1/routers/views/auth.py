import typing as t
from enum import StrEnum, unique

from common import StrictBaseModel
from domain import entities


@unique
class TokenType(StrEnum):
    BEARER = "bearer"


class TokenInfo(StrictBaseModel):
    token_type: TokenType = TokenType.BEARER
    access_token: str

    @classmethod
    def from_access_token_entity(cls, entity: entities.auth.AccessToken) -> t.Self:
        return cls(access_token=entity)
