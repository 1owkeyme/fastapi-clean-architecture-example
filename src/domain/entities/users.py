from common import StrictBaseModel

from .characters import Character


class User(StrictBaseModel):
    username: str
    hashed_password: str
    characters: list[Character]
