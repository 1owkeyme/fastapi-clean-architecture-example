import typing as t

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .usecases import ReadUserAccessTokenUsecaseDependency

reusable_oauth2: OAuth2PasswordBearer | None = None


def __get_reusable_oauth2() -> OAuth2PasswordBearer:
    if reusable_oauth2 is None:
        raise RuntimeError  # TODO: raise HTTPException or smth
    return reusable_oauth2


__BearerTokenDependency = t.Annotated[str, Depends(__get_reusable_oauth2)]

async def __get_current_user(read_user_access_token_usecase:ReadUserAccessTokenUsecaseDependency,bearer_token: __BearerTokenDependency):
    await read_user_access_token_usecase.execute(bearer_token)

OAuth2PasswordRequestFormDependency = t.Annotated[OAuth2PasswordRequestForm, Depends()]
