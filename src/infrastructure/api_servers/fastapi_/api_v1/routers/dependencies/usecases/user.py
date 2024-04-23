import typing as t
from http import HTTPStatus

from fastapi import Depends, HTTPException

from domain import usecases


user_usecases_builder: usecases.user.UserUsecasesBuilder | None = None


def __get_user_usecases_builder() -> usecases.user.UserUsecasesBuilder:
    if user_usecases_builder is None:
        raise HTTPException(status_code=HTTPStatus.SERVICE_UNAVAILABLE, detail="Usecases are not initialized")
    return user_usecases_builder


def __get_create_user_usecase() -> usecases.user.CreateUserUsecase:
    return __get_user_usecases_builder().construct_create_user_usecase()


CreateUserUsecaseDependency = t.Annotated[usecases.user.CreateUserUsecase, Depends(__get_create_user_usecase)]


def __get_delete_user_usecase() -> usecases.user.DeleteUserByIdUsecase:
    return __get_user_usecases_builder().construct_delete_user_by_id_usecase()


DeleteUserByIdUsecaseDependency = t.Annotated[usecases.user.DeleteUserByIdUsecase, Depends(__get_delete_user_usecase)]


def __get_get_all_users_usecase() -> usecases.user.GetAllUsersUsecase:
    return __get_user_usecases_builder().construct_get_all_users_usecase()


GetAllUsersUsecaseDependency = t.Annotated[usecases.user.GetAllUsersUsecase, Depends(__get_get_all_users_usecase)]


def __get_get_all_user_reviews_usecase() -> usecases.user.GetAllUserReviewsByIdUsecase:
    return __get_user_usecases_builder().construct_get_all_user_reviews_by_id_usecase()


GetAllUserReviewsByIdUsecaseDependency = t.Annotated[
    usecases.user.GetAllUserReviewsByIdUsecase, Depends(__get_get_all_user_reviews_usecase)
]


def __get_get_user_by_id_usecase() -> usecases.user.GetUserByIdUsecase:
    return __get_user_usecases_builder().construct_get_user_by_id_usecase()


GetUserByIdUsecaseDependency = t.Annotated[usecases.user.GetUserByIdUsecase, Depends(__get_get_user_by_id_usecase)]


def __get_is_user_super_user_usecase() -> usecases.user.IsUserSuperUserUsecase:
    return __get_user_usecases_builder().construct_is_user_super_user_usecase()


IsUserSuperUserUsecaseDependency = t.Annotated[
    usecases.user.IsUserSuperUserUsecase, Depends(__get_is_user_super_user_usecase)
]
