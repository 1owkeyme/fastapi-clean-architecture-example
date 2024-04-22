import typing as t

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import Field

from common import StrictBaseModel
from domain import entities

from .id_ import IdSchema


class UserCredentialsSchema(StrictBaseModel):
    username: str = Field(examples=["Frank"])
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


class UserIdSchema(IdSchema):
    def to_entity(self) -> entities.user.UserId:
        return entities.user.UserId(id=self.id)

    @classmethod
    def from_entity(cls, entity: entities.user.UserId) -> t.Self:
        return cls(id=entity.id)


class CreateUserSchema(UserCredentialsSchema):
    pass
