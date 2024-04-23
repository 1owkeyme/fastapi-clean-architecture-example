import typing as t

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from domain import usecases

from .. import schemas
from . import usecases as usecases_dependencies


__BearerTokenDependency = t.Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login"))]


async def __get_current_user_id(
    read_user_access_token_usecase: usecases_dependencies.auth.ReadUserAccessTokenUsecaseDependency,
    bearer_token: __BearerTokenDependency,
) -> schemas.id_.Id:
    try:
        id_entity = await read_user_access_token_usecase.execute(bearer_token)
    except usecases.interfaces.services.security.token_errors.InvalidTokenError:
        raise  # TODO:

    return schemas.id_.Id.from_id_entity(id_entity)


CurrentUserIdDependency = t.Annotated[schemas.id_.Id, Depends(__get_current_user_id)]
EnsureCurrentUserIdDependency = Depends(__get_current_user_id)


async def __get_current_super_user_id(
    current_user_id: CurrentUserIdDependency,
    is_user_super_user_usecase: usecases_dependencies.user.IsUserSuperUserUsecaseDependency,
) -> schemas.id_.Id:
    if await is_user_super_user_usecase.execute(current_user_id.to_id_entity()):
        return current_user_id

    raise  # TODO:


CurrentSuperUserIdDependency = t.Annotated[schemas.id_.Id, Depends(__get_current_super_user_id)]
EnsureCurrentSuperUserIdDependency = Depends(__get_current_super_user_id)
OAuth2PasswordRequestFormDependency = t.Annotated[OAuth2PasswordRequestForm, Depends()]
