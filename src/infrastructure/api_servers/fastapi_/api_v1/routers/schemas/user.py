import typing as t

from pydantic import Field

from common import StrictBaseModel
from domain import entities

from .id_ import Id


class Username(StrictBaseModel):
    username: str = Field(examples=["Frank"])


class UserPublic(Id, Username):
    @classmethod
    def from_entity(cls, entity: entities.user.UserPublic) -> t.Self:
        return cls(id=entity.id, username=entity.username)


class UserId(StrictBaseModel):
    user_id: int = Field(gt=0, examples=[43])

    @classmethod
    def from_id_entity(cls, entity: entities.Id) -> t.Self:
        return cls(user_id=entity.id)
