from enum import StrEnum

from common import StrictBaseModel


class TokenType(StrEnum):
    BEARER = "Bearer"


class TokenInfo(StrictBaseModel):
    access_token: str
    token_type: TokenType = TokenType.BEARER
