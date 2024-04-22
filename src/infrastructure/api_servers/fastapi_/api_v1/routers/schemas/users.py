import typing as t

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import Field

from common import StrictBaseModel
from domain import entities


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


class UserIdSchema(StrictBaseModel):
    id: int

    def to_entity(self) -> entities.user.UserId:
        return entities.user.UserId(id=self.id)


class CreateUserSchema(UserCredentialsSchema):
    pass
