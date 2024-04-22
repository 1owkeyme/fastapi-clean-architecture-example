import typing as t

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from domain import usecases

from ..schemas.users import UserIdSchema
from . import usecases as usecases_dependencies


__BearerTokenDependency = t.Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login"))]
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTM4NzQ1MjIsInN1YiI6OH0.Y3_VLZO9YX5hb4K_mW-x8gfrE7LFcittR3lKVaU0CV8
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTM4NzQ1MjIsInN1YiI6OH0.Y3_VLZO9YX5hb4K_mW-x8gfrE7LFcittR3lKVaU0CV8


async def __get_current_user_id(
    read_user_access_token_usecase: usecases_dependencies.ReadUserAccessTokenUsecaseDependency,
    bearer_token: __BearerTokenDependency,
) -> UserIdSchema:
    try:
        user_id_entity = await read_user_access_token_usecase.execute(bearer_token)
    except usecases.interfaces.security.token_errors.InvalidTokenError:
        raise  # TODO:

    return UserIdSchema.from_entity(user_id_entity)


CurrentUserIdDependency = t.Annotated[UserIdSchema, Depends(__get_current_user_id)]
EnsureCurrentUserIdDependency = Depends(__get_current_user_id)


async def __get_current_super_user_id(
    current_user_id: CurrentUserIdDependency,
    is_user_super_user_usecase: usecases_dependencies.IsUserSuperUserUsecaseDependency,
) -> UserIdSchema:
    if await is_user_super_user_usecase.execute(current_user_id.to_entity()):
        return current_user_id

    raise  # TODO:


CurrentSuperUserIdDependency = t.Annotated[UserIdSchema, Depends(__get_current_super_user_id)]
EnsureCurrentSuperUserIdDependency = Depends(__get_current_super_user_id)


OAuth2PasswordRequestFormDependency = t.Annotated[OAuth2PasswordRequestForm, Depends()]
