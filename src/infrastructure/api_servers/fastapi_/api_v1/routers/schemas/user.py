import typing as t

from fastapi.security import OAuth2PasswordRequestForm
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


class UserCredentials(Username):
    password: str = Field(examples=["C0wperw00d"])

    @classmethod
    def from_oauth2_password_request_form_data(cls, form: OAuth2PasswordRequestForm) -> t.Self:
        return cls(username=form.username, password=form.password)

    def to_user_plain_credentials_entity(
        self,
    ) -> entities.user.PlainCredentials:
        return entities.user.PlainCredentials(
            username=self.username,
            password=self.password,
        )


class CreateUser(UserCredentials):
    pass


class UserId(StrictBaseModel):
    user_id: int = Field(gt=0, examples=[43])

    @classmethod
    def from_id_entity(cls, entity: entities.Id) -> t.Self:
        return cls(user_id=entity.id)
