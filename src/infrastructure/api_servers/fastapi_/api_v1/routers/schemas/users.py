from pydantic import Field

from common import StrictBaseModel
from domain import entities


class UserId(StrictBaseModel):
    id: int

    def to_entity(self) -> entities.user.UserId:
        return entities.user.UserId(id=self.id)


class CreateUserSchema(StrictBaseModel):
    username: str = Field(examples=["Frank"])
    password: str = Field(examples=["C0wperw00d"])

    def to_user_plain_credentials_entity(
        self,
    ) -> entities.user.PlainCredentials:
        return entities.user.PlainCredentials(
            username=self.username,
            password=self.password,
        )
