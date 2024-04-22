import typing as t
from enum import StrEnum

from common import StrictBaseModel
from domain import entities


class TokenType(StrEnum):
    BEARER = "Bearer"


class TokenInfo(StrictBaseModel):
    access_token: str
    token_type: TokenType = TokenType.BEARER

    @classmethod
    def from_access_token_entity(cls, entity: entities.auth.AccessToken) -> t.Self:
        return cls(access_token=entity)
