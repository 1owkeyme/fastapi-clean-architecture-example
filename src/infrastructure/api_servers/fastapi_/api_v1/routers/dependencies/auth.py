import typing as t

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from domain import usecases

from .. import schemas
from . import auth_errors as err
from . import usecases as usecases_dependencies


__BearerTokenDependency = t.Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login"))]


async def __get_current_user_public(
    read_user_access_token_usecase: usecases_dependencies.auth.ReadUserAccessTokenUsecaseDependency,
    get_user_by_id_usecase: usecases_dependencies.user.GetUserByIdUsecaseDependency,
    bearer_token: __BearerTokenDependency,
) -> schemas.user.UserPublic:
    try:
        unverified_id_entity = await read_user_access_token_usecase.execute(bearer_token)
    except usecases.auth.errors.InvalidCredentialsError:
        raise err.UnauthenticatedError from None

    try:
        user_public_entity = await get_user_by_id_usecase.execute(unverified_id_entity)
    except usecases.user.errors.UserNotFoundError as exc:
        raise err.UnauthenticatedError from exc
    return schemas.user.UserPublic.from_entity(user_public_entity)


CurrentUserDependency = t.Annotated[schemas.user.UserPublic, Depends(__get_current_user_public)]
EnsureCurrentUserDependency = Depends(__get_current_user_public)


async def __get_current_super_user(
    current_user: CurrentUserDependency,
    is_user_super_user_usecase: usecases_dependencies.user.IsUserSuperUserUsecaseDependency,
) -> schemas.id_.Id:
    if await is_user_super_user_usecase.execute(current_user.to_id_entity()):
        return current_user

    raise err.UnauthorizedError


CurrentSuperUserDependency = t.Annotated[schemas.id_.Id, Depends(__get_current_super_user)]
EnsureCurrentSuperUserDependency = Depends(__get_current_super_user)
