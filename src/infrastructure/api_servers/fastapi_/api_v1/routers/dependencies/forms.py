import typing as t

from fastapi import Depends, Form

from domain import entities


class UserCredentialsForm:
    def __init__(
        self,
        *,
        username: t.Annotated[str, Form()],
        password: t.Annotated[str, Form()],
    ) -> None:
        self.username = username
        self.password = password

    def to_user_plain_credentials_entity(
        self,
    ) -> entities.user.PlainCredentials:
        return entities.user.PlainCredentials(
            username=self.username,
            password=self.password,
        )


UserCredentialFormDependency = t.Annotated[UserCredentialsForm, Depends()]
