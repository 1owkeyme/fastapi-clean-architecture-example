import typing as t
from http import HTTPStatus

from fastapi import Depends, HTTPException

from domain import usecases


auth_usecases_builder: usecases.auth.AuthUsecasesBuilder | None = None


def __get_auth_usecases_builder() -> usecases.auth.AuthUsecasesBuilder:
    if auth_usecases_builder is None:
        raise HTTPException(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="Usecases are not initialized")
    return auth_usecases_builder


def __get_authenticate_user_usecase() -> usecases.auth.AuthenticateUserUsecase:
    return __get_auth_usecases_builder().construct_authenticate_user_usecase()


AuthenticateUserUsecaseDependency = t.Annotated[
    usecases.auth.AuthenticateUserUsecase, Depends(__get_authenticate_user_usecase)
]


def __get_create_user_access_token_usecase() -> usecases.auth.CreateUserAccessTokenUsecase:
    return __get_auth_usecases_builder().construct_create_user_access_token_usecase()


CreateUserAccessTokenUsecaseDependency = t.Annotated[
    usecases.auth.CreateUserAccessTokenUsecase, Depends(__get_create_user_access_token_usecase)
]


def __get_read_user_access_token_usecase() -> usecases.auth.ReadUserAccessTokenUsecase:
    return __get_auth_usecases_builder().construct_read_user_access_token_usecase()


ReadUserAccessTokenUsecaseDependency = t.Annotated[
    usecases.auth.ReadUserAccessTokenUsecase, Depends(__get_read_user_access_token_usecase)
]
